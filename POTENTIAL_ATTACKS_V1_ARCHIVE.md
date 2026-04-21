# Potential Attacks — Combinatorial Threat Models

Attack scenarios constructed by combining patterns Layer 3 has actually observed in the corpus. Each scenario is hypothetical at the *combination* level — none of these full chains are confirmed end-to-end — but every individual component is something we have data for. These are written so a defender can pre-build detectors before the combination lands in the wild.

Format for each attack:
- **Phases:** what the attacker does, broken into storing potential / seeding / discharge
- **Observed components:** which Layer 3 patterns the attack reuses
- **Why it's hard to see:** what makes it slip past existing scanners
- **Detection hooks:** what Layer 3 could watch for to catch it
- **Status:** which components are confirmed in our data vs hypothetical

---

## Attack 1 — Permission Harvesting + Routing Parasite

### Phase 1 — Storing potential (permission harvesting)
Attacker deploys a "yield optimizer" or "airdrop checker" contract `0xA`. The UX asks users to grant unlimited ERC-20 approval to `0xA`. `0xA` does nothing visibly malicious — it stores a list of `(token, owner, allowance)` tuples and waits. Approvals persist on-chain forever unless revoked. Many users never revoke.

### Phase 2 — Seeding (routing parasite)
Attacker deploys a pool contract `0xB` that implements the Uniswap V3 / V4 pool interface correctly enough to be picked up by aggregators (1inch, OpenOcean, KyberSwap). The pool has real liquidity — small, but enough to occasionally win a route quote. Inside `swap()`, beyond the legitimate swap math, there is a backdoor branch: *if `tx.origin` has a stored allowance on `0xA`, call `0xA.drain(tx.origin, token)`*. `0xA.drain` calls `transferFrom` against the stored allowance into an attacker-controlled sink.

### Phase 3 — Discharge
A normal user does a swap through their favorite aggregator. The aggregator picks `0xB` because of price/liquidity. The swap succeeds — the user receives the expected output token. Inside the same transaction, the routing parasite quietly empties whatever allowance the user previously gave to `0xA`. The drain is **not** a Transfer event in the swap path; it's a separate `transferFrom` triggered by an internal call. Aggregator UIs show "swap successful, X received" and the user doesn't notice the second token leaving their wallet.

### Observed components
- **Approval-harvesting contracts:** we have `bait_profiles` rows where `bait_type` involves approvals.
- **Routing-parasite pattern:** `trust_amplification` table contains contracts (e.g. `0xd4624228`) where `router_percentage = 96.6%` — 96.6% of all callers are router/aggregator contracts, not direct EOAs.
- **Custom-selector drains with zero log events:** the `e37136db` selector observed on documented drain contracts emits no `Transfer` events on success (CORRECTIONS.md, 2026-04-05).
- **Cross-contract orchestration:** observed in the `0x08b8b941` closed-loop ecosystem (funder → deployers → service hub).

### Why it's hard to see
- The user-facing transaction is a successful swap. Wallet warnings don't fire.
- The drain doesn't emit `Transfer` from the swap contract — it comes from the previously approved `0xA`, which the user has already trusted.
- Static analyzers looking at `0xB` see a working pool. Looking at `0xA` they see a dormant approval store.
- Neither contract individually is suspicious. The threat is the *combination*.

### Detection hooks
- **Approval graph + pool graph join:** if any contract `0xA` holds non-trivial allowances AND any pool `0xB` (deployed by a related funder, vanity-collision, or bytecode-similar deployer) starts winning aggregator routes, flag the pair.
- **Tx-shape detector:** in a single transaction, watch for `swap()` on a pool followed by `transferFrom` on an unrelated ERC-20 with the same `tx.origin`. That shape is rare in legitimate DeFi.
- **Router percentage spike:** any new pool whose first 100 callers are >80% known aggregator routers (vs direct EOAs) is suspicious — legitimate pools acquire direct LP/swap traffic too.
- **Bytecode family link:** check if `0xA` and `0xB` share a deployer, funder, or bytecode template via `entity_classification`.

### Status
- Approval bait, routing parasites, and zero-log custom drains are all individually observed. The **chain** is hypothetical for now, but each link has corpus evidence.

---

## Attack 2 — Dormant Fleet Activation + Proxy Upgrade Swap

### Phase 1 — Storing potential
Attacker deploys 100+ EIP-1967 proxy contracts pointing at a benign implementation (e.g. a clone of a verified DEX router or token vault). Funds them all from a single funder, then lets them sit dormant for weeks. They appear in scanners as "deployed but inactive" — low risk score, often whitelisted as "looks safe, no activity yet."

### Phase 2 — Seeding
Attacker upgrades the implementation slot of one or two proxies to a malicious implementation. The new implementation contains the trap logic (revert-on-extract, allowance-drain, or hidden mint). They wait to see if anyone calls them. If a bot or aggregator picks them up, the rest of the fleet gets the same upgrade.

### Phase 3 — Discharge
Mass coordinated upgrade across the dormant fleet at a chosen block. The fleet goes from "100 dormant proxies" to "100 active traps" in one block, faster than any scanner's polling interval. Bots hitting any of them get drained. After the burn, attacker calls `selfdestruct` on the implementation OR sets the slot to `0x0`, leaving forensic investigators with a proxy pointing at nothing.

### Observed components
- **Dormant deployer fleets:** Layer 3 corpus has 100+ deployers with funded contracts and zero post-deploy activity.
- **EIP-1967 proxies:** ~1,974 proxy contracts in the corpus, watched by `proxy_upgrade_watcher.py`.
- **Coordinated mass deployment:** observed in mega-fleet `0x0b701885` activation patterns.
- **Self-destructed implementations:** the proxy watcher already checks for this (after the EOA-vs-destroyed correction in CORRECTIONS.md).

### Why it's hard to see
- Pre-upgrade, every contract scores benign. Any "score at deploy time" detector misses this entirely.
- The malicious window can be as short as one block before destruction.
- Even after the upgrade, if the implementation is destroyed before scanners pull it, only the proxy slot history reveals the swap.

### Detection hooks
- **Proxy upgrade events:** watch slot writes to `0x360894...` (EIP-1967 implementation slot) and re-score immediately.
- **Fleet correlation on upgrade:** if multiple proxies sharing a funder upgrade within N blocks of each other, alert.
- **Pre-fetch implementation bytecode the moment slot changes** — don't wait for the polling cycle. The implementation might be destroyed.
- **Dormant-to-active transition detector:** any deployer whose fleet has been silent for >2 weeks suddenly seeing >5 contracts called in <1 hour.

### Status
- Dormant fleets, proxy upgrades, and coordinated activations all observed. The malicious-upgrade-then-destroy chain is hypothetical but mechanically possible.

---

## Attack 3 — TaaS Template with Hidden Extraction Hook

### Phase 1 — Storing potential
Operator publishes a "trap deployment service" — pay 0.1 ETH, get your own honeypot deployed. The service uses a fixed bytecode template with a small constructor parameterizing the operator's address. Customers see source code (or claim to). What they don't notice: the template has a hardcoded fallback that, on a specific selector call, transfers a percentage of the contract's balance to a TaaS-operator address baked into the template, not the customer's address.

### Phase 2 — Seeding
Hundreds of customers deploy the template across multiple chains. Each customer thinks they own their trap. The TaaS operator's bytecode-family fingerprint is everywhere, but funders look diverse (each customer funded their own deployer). `entity_classification` sees a sprawling family with no clean org link.

### Phase 3 — Discharge
TaaS operator runs a single script that calls the hidden selector on every contract in the template family. Skims X% from each. Customers are still operating their traps and don't notice the small siphon — or notice but blame it on revert/gas oddities.

### Observed components
- **TaaS bytecode families:** template `T1-d5351e977044` has 435 deployers funded by only 2 funders — exactly the asymmetry a TaaS distribution would produce.
- **Hidden selectors with no events:** observed in `e37136db`-style drain calls.
- **Bytecode-family clustering across diverse deployers:** routine in our corpus.

### Why it's hard to see
- Customers self-deploy, so blame attribution is diluted.
- The skim selector is invisible at the source-code level if customers got a doctored source. At the bytecode level it's a rarely-called branch.
- Each individual skim is small enough to look like normal trap revenue noise.

### Detection hooks
- **Bytecode-family revenue tracing:** sum the inflows to a bytecode family, then look for an outflow address that appears across many family members but isn't the deployer. That's the TaaS skim address.
- **Unique-funder ratio per family:** family with 435 contracts and only 2 funders is suspicious — TaaS infrastructure rather than organic growth.
- **Selector frequency analysis:** find selectors that appear in N>10 contracts of a family but are called <1% of the time — those are dormant hooks.

### Status
- The 435-deployer / 2-funder asymmetry is real and unexplained. The hidden skim hook is hypothetical but consistent with the structure.

---

## Attack 4 — Time-Lock Synchronized Fire

### Phase 1 — Storing potential
Attacker deploys 1000+ contracts gated by `block.timestamp >= T` for the same `T`. Each contract is benign before T — calling it returns success with no state change. After T, calling it triggers a different code path (extraction, permission claim, governance action).

### Phase 2 — Seeding
Wait. The contracts age, accumulate trust signals: "deployed weeks ago, no reverts, no complaints." Aggregators and risk scorers may even whitelist them on age + clean history.

### Phase 3 — Discharge
At block timestamp T, all 1000 contracts' branches flip simultaneously. Coordinated drain or governance attack across the entire fleet in one block. Bots running ahead-of-time scans see clean contracts; bots running real-time at block T see the post-flip state.

### Observed components
- **TIMESTAMP-gated contracts:** Layer 3 has 1,315 contracts where bytecode includes `TIMESTAMP` opcode in conditional paths.
- **Age-as-trust scoring:** every existing scanner does this implicitly.
- **Dormant fleet patterns:** documented elsewhere in this file.

### Why it's hard to see
- Pre-flip behavior is honest. Most "is this contract safe" checks return `safe`.
- The flip is global and atomic at the block level — by the time observers notice, victims are already drained.
- Contracts might use `block.number` instead of timestamp, or a hash of an oracle value, making the flip condition opaque to static analysis.

### Detection hooks
- **Symbolic time-branch extraction:** for every TIMESTAMP-gated contract, decode the threshold T. Build a calendar of T values across the corpus. Any cluster of contracts sharing T should be flagged.
- **T-value clustering across deployers:** if 50 contracts from 50 different deployers all have T = same hour next Friday, that's a coordinated kill switch.
- **Pre-flip simulation:** at scan time, simulate a call with `block.timestamp = T+1` and compare to `block.timestamp = T-1`. Behavioral divergence = trap.

### Status
- The 1,315 TIMESTAMP-gated contracts are real. We do not yet decode their thresholds. Building a T-value calendar would be a high-leverage addition.

---

## Attack 5 — Cross-Chain Rotation Evasion

### Phase 1 — Storing potential
Operator deploys a trap on chain A (Base). Drains some bots. Earns a bad reputation on chain A's scanners.

### Phase 2 — Seeding
Operator deploys structurally identical traps on chains B and C (Arbitrum, Optimism) using a *different* deployer EOA but the *same* bytecode template and *similar* funding source. Cross-chain reputation systems generally don't share data; chain B sees a fresh deployer with no history.

### Phase 3 — Discharge
As chain A scanners catch up and start blacklisting, the operator pivots traffic / liquidity to chains B and C. When B catches up, jump to D. The operator has effectively unlimited reputation by rotating chains.

### Observed components
- **Cross-chain operators:** 8+ deployers in the corpus operating on all 3 chains (Base + Arbitrum + Optimism).
- **Bytecode family cross-chain replication:** several `entity_classification` families span multiple chains.
- **Deployer similarity with temporal succession:** 274 wallet-rotation pairs with similarity ≥0.85 and one deployer's last_seen before the next's first_seen.

### Why it's hard to see
- Each chain's scanners are blind to other chains.
- Rotation across deployers within a chain plus rotation across chains compounds: single-chain scanners see fresh wallets every time.
- Funding chains can be obfuscated through bridges, making the funder graph chain-local.

### Detection hooks
- **Bytecode hash as cross-chain primary key:** a fresh deployer on Optimism whose contract bytecode matches a flagged Base contract should inherit the flag.
- **Funding-source cross-chain join:** if funder F on Base previously seeded a flagged operator, any Arbitrum deployer funded by F (via bridge) inherits suspicion.
- **Temporal succession across chains:** `last_seen on chain A < first_seen on chain B` for similar deployers = rotation.

### Status
- Cross-chain operators and 274 in-chain rotation pairs are confirmed. Cross-chain rotation as a deliberate evasion strategy is hypothetical but the building blocks are present.

---

## Attack 6 — Probe-Trap Targeting Scanners

### Phase 1 — Storing potential
Attacker observes that defensive bots and scanners have characteristic probe patterns: low-value calls to standard selectors (`balanceOf`, `name`, `symbol`, `0x00000000`, common 4-byte hashes) before any real interaction.

### Phase 2 — Seeding
Attacker deploys a contract whose normal-looking functions are honest, but specific probe selectors (the ones scanners use for fingerprinting) trigger a trap branch — typically a revert that consumes the caller's gas, OR a state write that marks the caller for later targeting.

### Phase 3 — Discharge
- **Variant A (gas burn):** scanner bots wear out gas reserves probing the contract. Their operators stop running scans, blinding the defensive coverage.
- **Variant B (mark and target):** the contract records `tx.origin` of every prober. Later, a separate contract checks "is this address on the prober list?" and serves them a different reality (poisoned prices, fake balances, malicious approvals) than it serves normal users.

### Observed components
- **Coffee fleet:** known scanner bot population starting with `0xc0ffee...`. They are heavily targeted in our corpus.
- **Probe-selector responsiveness:** several Layer 3 traps respond differently to standard probe selectors vs typical user selectors.
- **Bots repeatedly trapped without learning:** documented (CORRECTIONS.md, 2026-04-04 — `0x5901663c` got hit 9 times in 2 days).

### Why it's hard to see
- The contract behaves correctly for non-prober callers. Manual review and standard fuzzers find nothing.
- Gas burn is gradual; scanner operators may attribute losses to RPC costs.
- Mark-and-serve discrimination requires comparing two distinct callers' results — single-caller analysis sees only one face of the contract.

### Detection hooks
- **Multi-perspective probing:** call the contract from a known-prober address AND a fresh address; diff the responses.
- **Gas-cost-on-probe outliers:** a contract whose `view`-style selectors burn more gas than baseline is suspicious.
- **Caller-discriminated branches in bytecode:** look for `CALLER`/`ORIGIN` followed by storage reads against a known-prober map.

### Status
- Bot trapping is core to our observed corpus. Discrimination via probe selectors specifically is hypothetical but a natural evolution.

---

## Attack 7 — Custom Selector Drain Avoiding Logs

### Phase 1 — Storing potential
Attacker designs an extraction function that does NOT emit any standard `Transfer`, `Approval`, or custom event. Uses a non-standard selector (e.g., the observed `e37136db`). The function moves value via direct storage manipulation, low-level `call` to a precompile, or a bare `selfbalance` sweep — anything that doesn't go through `Token.transfer` or `Token.transferFrom` from a contract that emits.

### Phase 2 — Seeding
Deploy across the trap fleet. The drain function exists in every trap but is rarely called and doesn't appear in test traces (because tests check Transfer logs, which are absent).

### Phase 3 — Discharge
At sweep time, attacker calls the drain function. Funds move. The block explorer shows a successful transaction with empty logs. Receipt parsers (Etherscan tag scrapers, dune queries indexing on Transfer events) see nothing. Forensic accounting requires `debug_traceTransaction` to recover the value flow — most RPC providers don't expose this on growth-tier plans.

### Observed components
- **Custom selector `e37136db`:** observed on documented drain contracts in our corpus, function emits zero log events on success (CORRECTIONS.md, 2026-04-05).
- **Empty-log successful transactions:** confirmed in the drain_value_scanner findings (0 transfer events across 500 drain receipts).
- **Trace data unavailable:** Alchemy growth tier blocks `debug_traceTransaction`.

### Why it's hard to see
- The fundamental tooling defenders use (event log indexing) returns nothing.
- Etherscan's "Token Transfers" tab is blank for the drain transactions.
- Without trace access, the only path to value reconstruction is "balance before vs balance after" on every account that touched the tx — expensive and noisy.

### Detection hooks
- **Empty-log success on a contract that *should* emit:** any contract whose normal operations emit Transfer/Approval, but whose calls occasionally complete with empty logs, is doing something off-path.
- **Selector frequency vs event frequency divergence:** a 4-byte selector that gets called repeatedly but never produces a log = candidate hidden function.
- **Balance delta scanning:** for any address that interacts with a known trap, snapshot its token balances before and after. If balances change without corresponding Transfer events, the missing transfer is the extraction.

### Status
- Confirmed: the `e37136db` selector exists, is called, and emits no logs. The full hidden-extraction interpretation is the leading hypothesis.

---

## Attack 8 — Infrastructure-Layer TaaS Skim

### Phase 1 — Storing potential
Operator runs a Trap-as-a-Service infrastructure: provides funding, deployment scripts, and shared service contracts (oracle relayers, fee routers, gas optimizers) to dozens of customer trap operators.

### Phase 2 — Seeding
Customer operators deploy traps that depend on the operator's shared infrastructure — they `delegatecall` to a shared logic contract or call a shared "router" for fee accounting. The infrastructure operator controls those shared contracts.

### Phase 3 — Discharge
At any time, the infrastructure operator can:
- Push a malicious upgrade to the shared logic (delegatecall victims execute it on their own state)
- Modify the fee router to skim from every customer's extraction
- Change oracle prices used by every dependent trap

The infrastructure operator extracts a percentage of the entire downstream fleet's revenue, invisibly to the customers.

### Observed components
- **Closed-loop infrastructure ecosystem:** `0x08b8b941` funds deployers AND deploys service contracts AND those funded deployers later call back into the service contracts (reports/infrastructure_layer_analysis.md).
- **Post-deployment callback pattern:** funded deployers calling the hub *after* their own deployments — pattern is suspicious but explained as "shared infrastructure usage."
- **Delegatecall service contracts:** observed in 0x08b8b941's contract set.

### Why it's hard to see
- Each downstream customer is operating their own legit-looking trap. The threat is one layer up.
- Without analyzing fund flows across the *entire* downstream graph, the skim looks like normal TaaS revenue.
- The hub operator can plausibly claim shared-infra purposes for every component of the architecture.

### Detection hooks
- **Hub-and-spoke fund flow analysis:** for any address that funds N>10 deployers AND deploys contracts that those funded deployers later call, sum the revenue flowing back to the hub.
- **Shared logic upgrade monitoring:** any delegatecall target that gets upgraded should cascade-re-score every contract that delegatecalls into it.
- **Cross-graph dependency mapping:** build a dependency graph of "contract X delegatecalls Y" and "deployer A funded by B" and look for entities that appear in multiple roles (funder + logic provider + sink).

### Status
- The hub/spoke + post-deploy callback pattern is real for `0x08b8b941`. The extraction interpretation is **unconfirmed** (CORRECTIONS.md, 2026-04-05). The architectural threat model is valid but lacks a confirmed instance — exactly the kind of attack to pre-build detectors for before it lands.

---

## Cross-Cutting Notes

**Why list hypothetical attacks?** Because Layer 3's value is *temporal* — catching novel patterns before they're scored. Every attack here uses building blocks we've already observed; the gap is whether they'll be assembled into the full chain. Pre-building detectors for the assembled forms means the first instance in the wild gets caught immediately.

**What separates these from generic threat-modeling?** Each attack cites specific table rows, deployer addresses, or selector hashes from the Layer 3 corpus. They are not abstract — they reuse observed primitives.

**Status legend:**
- **Observed:** the full chain has been seen end-to-end in our data
- **Components observed, chain hypothetical:** every link is in the corpus, the assembly isn't confirmed
- **Architecturally valid, unconfirmed:** the threat model is sound but at least one component is hypothetical

None of the attacks above are in the **Observed** category. All are **Components observed, chain hypothetical** or **Architecturally valid, unconfirmed**. That's the point of this file — to enumerate the assembly space before adversaries do.
