# Potential Attacks v2 — Combinatorial Threat Models After the April 2026 Wave

**Revision date:** 2026-04-20
**Predecessor:** `POTENTIAL_ATTACKS_V1_ARCHIVE.md` (dated 2026-04-07; preserved verbatim as an evidence record of what the framework anticipated before the April wave).

Attack scenarios constructed by combining patterns Layer 3 has observed in the corpus. Each scenario is hypothetical at the **combination** level; every individual component has corpus evidence. The April 2026 exploit wave — Drift (Apr 1), Silo (Apr 3), Aethir (Apr 9), Zerion (Apr 10), Hyperbridge (Apr 13), Dango (Apr 13), Rhea (Apr 16), Kelp (Apr 18) — validated several v1 attacks, introduced new categories that v1 did not anticipate, and sharpened the vocabulary we now use for all of them.

**Format (unchanged from v1):**
- **Phases:** storing potential → seeding → discharge
- **Observed components:** which Layer 3 patterns the attack reuses
- **Why it's hard to see:** what makes it slip past existing scanners
- **Detection hooks:** what Layer 3 watches for
- **Status:** observed / components-observed-chain-hypothetical / architecturally-valid-unconfirmed, with an explicit **Epistemic Tier** tag per [the lexicon's tier discipline](docs/lexicon.md#epistemic-tier-classification)

**What's new in v2:**
1. A "Validated in April 2026" section cross-referencing each v1 attack against the `extraction_events` table so readers can see what moved from hypothetical → confirmed.
2. Six new attack categories introduced by the April wave (Attacks 9-14).
3. Lexicon vocabulary threaded throughout. Terms: [Stored Potential](docs/lexicon.md#stored-potential), [Compositional Harm](docs/lexicon.md#compositional-harm), [Configuration-Level Vulnerability](docs/lexicon.md#configuration-level-vulnerability), [Verification-Path Trust Failure](docs/lexicon.md#verification-path-trust-failure), [Pooled Custody Amplification](docs/lexicon.md#pooled-custody-amplification), [Operational Layer Attack](docs/lexicon.md#operational-layer-attack), [Behavioral Laundering](docs/lexicon.md#behavioral-laundering), [Participatory Asymmetry](docs/lexicon.md#participatory-asymmetry--predatory-literacy), [Trust Amplification Factor](docs/lexicon.md#trust-amplification-factor).
4. Every attack's Status field now carries an explicit Tier tag.

---

## Validated in April 2026

| v1 attack | What v1 predicted | What actually happened | Cross-ref |
|---|---|---|---|
| Attack 1 — Permission Harvesting + Routing Parasite | Approval-bait + aggregator-pool parasite combine | Partial: `CE5E`, `E717`, `A7B9` drainer operations (approval + hub-and-spoke) ongoing through April. Full routing-parasite compound chain still not observed. | [case_CE5E_drainer_operation.md](reports/case_CE5E_drainer_operation.md) |
| Attack 2 — Dormant Fleet + Proxy Upgrade Swap | Proxy-upgrade coordinated across fleet | **Partially validated in simpler form:** Aethir (EXTRACTION_006, 2026-04-09) compromised a **single-contract** proxy-class OFT adapter via private-key compromise rather than fleet upgrade. The single-contract mode is now confirmed as a live category; the fleet-coordinated version remains hypothetical. | [extraction_event_006_aethir.md](reports/extraction_event_006_aethir.md) |
| Attack 3 — TaaS Template with Hidden Skim | Shared TaaS template with hidden operator hook | Not observed. T1-d5351e977044 family (435 deployers / 2 funders) still unexplained but no hidden-skim flow traced. | [extraction_event_008_kelp.md](reports/extraction_event_008_kelp.md) for comparison on closed-loop architectures |
| Attack 4 — Time-Lock Synchronized Fire | 1000+ TIMESTAMP-gated contracts flip at T | Not observed. 1,315 TIMESTAMP-gated contracts in corpus; thresholds still unextracted. Remains the highest-value speculative category. | — |
| Attack 5 — Cross-Chain Rotation Evasion | Deployer rotates chains to shed reputation | **Superseded by** [Pattern D — Cross-Chain Reputation Import](docs/lexicon.md#pattern-d--cross-chain-reputation-import). Framework now formalized: 54/100 high-risk L2 deployers have mainnet first-tx predating L2 first-seen. The v1 description stands but now lives inside the broader Behavioral Laundering taxonomy. | [cross_chain_import_candidates.md](reports/cross_chain_import_candidates.md) |
| Attack 6 — Probe-Trap Targeting Scanners | Differential response by prober address | Not observed. Coffee fleet still heavily targeted; no mark-and-serve discrimination captured. | — |
| Attack 7 — Custom Selector Drain Avoiding Logs | `e37136db` hidden-extraction hypothesis | **Leading hypothesis unchanged.** No contradictory evidence; no confirmation either. 500+ empty-log successful drains still observed. | CORRECTIONS.md 2026-04-05 |
| Attack 8 — Infrastructure-Layer TaaS Skim | `0x08b8b941` hub siphons downstream fleet | Not observed. Unconfirmed as of April 7, unconfirmed as of April 20. Architecture still valid, hub pattern still real. | — |

**New categories the April wave established** (Attacks 9–14 below): Cross-Chain DVN Verification Failure (Kelp), Cross-Chain Proof Verification Bypass (Hyperbridge), Pooled Custody Adapter Compromise (Aethir and its class), Oracle Manipulation via Fake-Token Collateral (Drift and Rhea), Operational Layer Compromise (Drift and Aethir as keyholder failures; Zerion as social-engineering), Advisor-Parasite (Pattern F — see [lexicon.md#pattern-f](docs/lexicon.md#pattern-f--advisor-parasite-pattern)).

---

## Part I — Preserved v1 attacks

Still valid as hypotheticals; included here with updated language but no architectural changes. Read the v1 archive for the original detailed treatment.

### Attack 1 — Permission Harvesting + Routing Parasite

Contract `0xA` harvests unlimited approvals ("yield optimizer", "airdrop checker"). Dormant store of [Stored Potential](docs/lexicon.md#stored-potential) via persistent on-chain allowances. Contract `0xB` is a valid Uniswap-interface pool; inside `swap()`, a branch checks whether `tx.origin` has an allowance on `0xA` and calls `0xA.drain(tx.origin, token)` as a side effect of an otherwise successful swap.

**Lexicon framing.** Classic [Compositional Harm](docs/lexicon.md#compositional-harm): the user-visible transaction is a successful swap; the extraction is invisible because it reuses a previously-granted approval. Individual components (approval-harvester, valid pool, custom-selector drain) are each scanable; the combination is not.

**Observed components:** `bait_profiles` approval-bait entries, `trust_amplification.router_percentage = 96.6%` on `0xd4624228`, `e37136db` empty-log selector (CORRECTIONS.md 2026-04-05), closed-loop hub `0x08b8b941`.

**Detection hooks** (unchanged):
- Approval-graph × pool-graph join on shared funder/deployer/bytecode-family
- Transaction-shape detector: swap followed by same-tx `transferFrom` on unrelated ERC-20
- Router-percentage spike on new pools (first 100 callers >80% aggregator)
- Bytecode-family link between the approver and the parasite

**Status: components observed, chain hypothetical. Epistemic Tier B.**

---

### Attack 4 — Time-Lock Synchronized Fire

1000+ contracts gated by `block.timestamp >= T` for the same `T`. Benign pre-T. At T, all branches flip simultaneously. This is a coordinated [Configuration-Level Vulnerability](docs/lexicon.md#configuration-level-vulnerability) exploit where the "configuration" is the shared threshold — the code is honest, the threshold is adversarial.

**Why this didn't happen in April.** None of the eight documented April events used coordinated time-flip. Drift and Rhea used configuration vulnerabilities, but each event exploited a single configuration state, not a cross-fleet synchronized flip. The signature Layer 3 is watching for — many contracts sharing T — would be distinguishable from all eight April events.

**Observed components:** 1,315 TIMESTAMP-gated contracts, age-as-trust scoring bias in every existing scanner, dormant fleet patterns (see follow-up finding on deployer `0xcadf9ebe…` with 20 contracts, 19 dormant, 1 fired).

**Detection hooks** (unchanged):
- Symbolic time-branch extraction across the 1,315-contract pool
- T-value clustering across deployers
- Pre-flip simulation with `block.timestamp = T+1` vs `T-1`

**Open work:** building the T-value calendar is still the highest-leverage addition. Nothing in the April wave gave us a forcing example, so this stays at the top of the speculative work list.

**Status: components observed, chain hypothetical. Epistemic Tier B.**

---

### Attack 6 — Probe-Trap Targeting Scanners

Contract behaves correctly for non-prober callers; responds differently to the probe selectors that scanners use. Variant A burns gas on the prober; variant B marks the address for later discriminated response. This is the Layer-3-aware version of the [Publishing-Induced Recursive Evasion](docs/lexicon.md#publishing-induced-recursive-evasion) dynamic — operators adapt specifically to the tools used by observers.

**Lexicon framing.** The discriminated-response variant is a [Verification-Path Trust Failure](docs/lexicon.md#verification-path-trust-failure) in the scanner's epistemology: the scanner believes its probes produce representative snapshots of contract behavior; the operator has engineered the probe-to-probe divergence.

**Observed components:** coffee fleet (scanner bots starting with `0xc0ffee…`), differential probe responses in several corpus traps, repeated re-trapping of the same bots (CORRECTIONS.md 2026-04-04 — `0x5901663c` hit 9× in 2 days).

**Detection hooks** (unchanged):
- Multi-perspective probing from a known-prober vs fresh address
- Gas-cost-on-probe outliers
- Caller-discriminated branches in bytecode (CALLER/ORIGIN + storage-read against a prober map)

**Status: architecturally valid, unconfirmed. Epistemic Tier C.**

---

### Attack 7 — Custom Selector Drain Avoiding Logs

Non-standard selector (e.g., the observed `e37136db`) moves value via direct storage manipulation, low-level `call`, or bare `selfbalance` sweep — not through `Token.transfer/transferFrom` from a contract that emits. No Transfer events. Etherscan Token Transfers tab is blank. Dune queries indexing on Transfer see nothing.

**Why this remains the leading hypothesis.** 500+ empty-log successful drains continue to accumulate in the corpus. No alternative hypothesis has been proposed that explains both the selector prevalence and the empty-log pattern. Detection work requires `debug_traceTransaction` access, which is behind Alchemy's growth tier and is therefore out-of-reach for many defenders.

**Detection hooks** (unchanged):
- Empty-log successful transaction on a contract that *should* emit
- Selector-frequency vs event-frequency divergence
- Balance-delta scanning (expensive fallback when trace is unavailable)

**Status: components observed, chain the leading hypothesis. Epistemic Tier A** for the observed empty-log pattern; **Tier B** for the hidden-extraction interpretation.

---

### Attack 8 — Infrastructure-Layer TaaS Skim

Operator `0x08b8b941` provides shared services (oracle relayers, fee routers, gas optimizers) to customer trap operators. Customers' traps `delegatecall` to the shared logic or route fees through a shared router. The infrastructure operator can push malicious upgrades, modify the fee router, or manipulate oracle prices — extraction happens one layer above any individual trap.

**Lexicon framing.** This is [Pooled Custody Amplification](docs/lexicon.md#pooled-custody-amplification) applied at the TaaS layer: the shared infrastructure is the pool, customer trap revenue is the custody, the infrastructure operator can release to themselves. Also a [Verification-Path Trust Failure](docs/lexicon.md#verification-path-trust-failure) if customers assume the shared infrastructure is neutral.

**Observed components:** `0x08b8b941` closed-loop (funds deployers AND deploys service contracts AND those deployers later call back into the service contracts), post-deployment callback pattern, delegatecall service contracts.

**Detection hooks** (unchanged):
- Hub-and-spoke fund flow analysis
- Shared-logic upgrade monitoring with cascade re-scoring
- Cross-graph dependency mapping for entities in multiple roles

**Status: components observed, extraction hypothesis unconfirmed. Epistemic Tier B.**

---

## Part II — Updated v1 attacks

Attacks where v1's description is structurally still valid but is now load-bearing against a more recent event. v1 text is preserved in the archive; the narrative here reflects what April taught us.

### Attack 2 — Dormant Fleet + Proxy Upgrade Swap — Single-Contract Variant Confirmed

**v1 predicted:** 100+ proxies deployed, sat dormant, upgraded together at a chosen block, then destroyed.

**What Aethir (EXTRACTION_006, 2026-04-09) did:** single-contract version. An OFTAdapter proxy contract on BNB Chain with an EOA admin. Attacker acquired the EOA private key (mechanism: private-key compromise per the published dev.to post-mortem) and drained bridged assets directly. No fleet coordination; no upgrade orchestration. **One contract, one upgrade, one drain.**

**What this confirms:** the proxy-admin-compromise primitive is live. Every single-owner EOA-admin proxy adapter is a latent instance of this category. The scale-up to fleet-coordinated version remains hypothetical but the atomic building block — "compromise admin key, use authorized upgrade path, extract" — is now a validated attack mode.

**Lexicon framing.** Attacks 2 and 11 (see Part III) are the same category at different scales. Attack 2 is the fleet-level Operational Layer Attack; Attack 11 is the single-contract case with [Pooled Custody Amplification](docs/lexicon.md#pooled-custody-amplification) providing the loss-amplification path.

**Observed components** (expanded from v1):
- Dormant deployer fleets, 1,974 proxy contracts in corpus
- **EXTRACTION_006 (Aethir) as a single-contract instance of the category**
- EIP-1967 proxy upgrade events monitored by `proxy_upgrade_watcher.py`
- Mega-fleet activation patterns (`0x0b701885`)

**Detection hooks** (updated):
- Proxy upgrade slot-write monitoring with pre-fetch of new implementation bytecode (now a hard requirement, not a nice-to-have — Aethir demonstrated the admin can destroy evidence)
- Fleet-correlation on upgrade (v1)
- **New:** single-contract high-stored-potential adapters where admin is an EOA without multisig or timelock — enumerate these and treat them as pre-validated Aethir-class risk

**Status: single-contract variant observed (EXTRACTION_006), fleet-coordinated variant components observed, assembly hypothetical. Epistemic Tier A** for Aethir; **Tier B** for fleet-coordinated.

---

### Attack 5 — Cross-Chain Rotation — Superseded by Pattern D (Cross-Chain Reputation Import)

**v1 predicted:** operators rotate across chains to shed reputation on each prior chain.

**What actually crystallized:** the behavior is real, but it's now one of six patterns in the [Behavioral Laundering](docs/lexicon.md#behavioral-laundering) framework, formalized as [Pattern D — Cross-Chain Reputation Import](docs/lexicon.md#pattern-d--cross-chain-reputation-import). The measurement shipped: 54/100 high-risk L2 deployers have mainnet first-tx predating L2 first-seen. `deployers.mainnet_first_tx` is a production column, populated by `auto_funder_tracer` at one Etherscan v2 call per new deployer; the 36k-row backfill completed 2026-04-21.

**Concrete example from follow-up** (2026-04-21): deployer `0xcadf9ebe57ce822cb4f2f36c514599f7b4f98154` has `mainnet_first_tx = 2025-10-25`, L2 first-seen `2026-03-17`, a 5-month gap. 20 contracts deployed in scripted-velocity bursts (2 seconds apart on `2026-03-25 02:53` and `04:56`). 1 confirmed trap (fired `2026-04-21 01:43`, 23 minutes after its first interaction); 19 dormant. This is exactly the Pattern D signature — prior mainnet identity + velocity burst on L2 + scripted deploy-and-wait trap fleet.

**Detection hooks** (updated):
- `deployers.mainnet_first_tx` enrichment live across all chains (shipped)
- Pattern D scanner: `python -m surveillance.pattern_d_scan` emits candidates with mainnet-activity-before-L2 gaps ≥ 60 days
- Cross-chain bytecode join (v1)
- Cross-chain funder join (v1)
- Rhea analog: cross-chain reputation import **via bridge** (EXTRACTION_004 used `intents.near` bridge funding — a non-address-reuse variant)

**Status: Pattern D validated, cross-chain rotation confirmed observed. Epistemic Tier A** for the 54/100 measurement.

---

## Part III — New categories the April wave established

These attacks are the category-level additions the v1 document could not have anticipated. Every one has at least one confirmed empirical instance.

### Attack 9 — Cross-Chain DVN Verification Failure (Kelp category)

**Storing potential.** Adapter contract deployed on two or more chains. Owner configures LayerZero DVN setup with `requiredDVNCount = 1` (single-verifier) on both send and receive paths. The configuration is publicly readable via `EndpointV2.getConfig(configType=2)` but does not appear in any bounty's in-scope contract list because configuration is not code.

**Seeding.** Adapter receives user deposits on the source chain (Unichain, BNB, etc.). Deposits accumulate in pooled custody. The DVN configuration sits unchanged for weeks or months; Layer 3 corpus shows Kelp's was unchanged for **≥56.7 days** pre-exploit.

**Discharge.** A single actor (the DVN operator, or anyone with the DVN's private key) signs a forged cross-chain message: "transfer N tokens to address X on the destination chain." The LayerZero endpoint on the destination accepts the attestation (because 1/1 is satisfied), the adapter processes the message, and releases N tokens from the pooled custody to address X.

**Lexicon framing.** The canonical [Configuration-Level Vulnerability](docs/lexicon.md#configuration-level-vulnerability) and [Verification-Path Trust Failure](docs/lexicon.md#verification-path-trust-failure) compound. Amplified by [Pooled Custody Amplification](docs/lexicon.md#pooled-custody-amplification) — the stolen tokens are indistinguishable from legitimate holdings because they come from the pool, not from new issuance. This is what let the attacker's ~116,500 rsETH be accepted as Aave collateral without triggering any red flag. Out-of-scope for [bug bounties](docs/lexicon.md#the-bug-bounty-structural-gap) by construction.

**Observed components:**
- **EXTRACTION_008 (Kelp, 2026-04-18, ~$292M).** Tier A lead time ≥56.7 days via historical `getConfig` at blocks 24,500,000–24,900,000 ([Phase 3 of retrospective](reports/kelp_retrospective_replay.md)).
- LayerZero OApp ecosystem has many deployments; DVN configurations vary. Industry-wide exposure.
- Tornado Cash funding of attacker wallet 6.5 hours before exploit (Phase 4 of retrospective) — an operational-layer signature distinct from the configuration issue.

**Why it's hard to see:**
- No code is defective. Every contract on the path executed exactly what it was authorized to execute.
- `getConfig` reads are rarely part of any scanner's default check.
- Downstream systems (Aave, Morpho) trust that LayerZero attestation = legitimate backing, so the tokens freely compose into the rest of DeFi before the fraud is realized.
- Bug bounty platforms don't scope configuration.

**Detection hooks:**
- **`EndpointV2.getConfig(configType=2)` read on every LayerZero OApp adapter**; alert on `requiredDVNCount < 2` OR `optionalDVNCount + threshold < 2`. This is the central hook.
- **DVN-operator monitoring:** track DVN signing frequency, source addresses, and divergence from published DVN identities (if a DVN's private key was leaked, signing patterns change).
- **Pooled-custody TVL × single-verifier correlation:** any adapter holding >$10M in pooled deposits with a 1-of-1 DVN is a pre-validated Kelp-class risk.
- Record every `getConfig` result historically so lead time is measurable post-facto (Kelp's ≥56.7 days was detectable in principle).

**Status: observed (EXTRACTION_008). Epistemic Tier A** for the configuration-level observation; **Tier B** for the generalization across the LayerZero OApp ecosystem.

---

### Attack 10 — Cross-Chain Proof Verification Bypass (Hyperbridge category)

**Storing potential.** Bridge contract uses a cryptographic proof system for cross-chain state attestations — Merkle tree, Merkle Mountain Range (MMR), succinct ZK proof, or similar. The proof-verification code is intricate. Edge cases in handling specific proof shapes (empty branches, single-leaf trees, wrap-around indices) may accept structurally malformed proofs as valid.

**Seeding.** Users deposit into the bridge. The proof-verification bug exists but is not exercised by normal operation — legitimate proofs always have the expected shape.

**Discharge.** Attacker crafts a proof that exploits the edge-case handling — e.g., an MMR proof with a specific shape that `HandlerV1.handlePostResponse` accepts despite not being a valid Merkle inclusion proof. The bridge processes the forged state attestation as if it were real and releases corresponding assets.

**Lexicon framing.** This is the code-level sibling of Attack 9. Attack 9 is [Configuration-Level](docs/lexicon.md#configuration-level-vulnerability); Attack 10 is a classic audit-catchable code defect (the MMR verification bug IS a coding bug). However, the amplification — [Pooled Custody Amplification](docs/lexicon.md#pooled-custody-amplification) — is identical: the bridge holds user funds, the forged proof unlocks them. Distinguishing code-level vs configuration-level matters for **where the defense goes**: Attack 10 is audit-catchable and belongs in pre-deployment review; Attack 9 is not and belongs in continuous on-chain monitoring.

**Observed components:**
- **EXTRACTION_007 (Hyperbridge, 2026-04-13, ~$237K).** MMR proof-validation bug in `HandlerV1.handlePostResponse`. ([extraction_event_007_hyperbridge.md](reports/extraction_event_007_hyperbridge.md)).
- Many bridges use MMR or equivalent; Hyperbridge's exploit is not isolated to one design.

**Why it's hard to see:**
- Proof-verification code is typically reviewed by protocol developers; third-party audits may not include bridge proof systems unless specifically scoped.
- The bug is exercised by a specific proof shape that does not occur in normal operation; test suites using legitimate proofs won't cover it.
- Between the deploy and the exploit, the bridge operates without producing any observable wrongness.

**Detection hooks:**
- **Proof-failure mode fuzzing** during audit. If the audit scope explicitly includes the proof-verification code path, this bug class is catchable. Layer 3 doesn't do code audits; this hook lives in the audit market.
- **Cross-chain state-change monitoring** for bridges: any state attestation that causes a large release should cross-check the proof against a second, independent proof verifier. Layer 3 could run this as an on-chain monitor.
- **Bridge TVL vs state-attestation volume correlation:** a sudden large release that doesn't match a corresponding source-chain deposit is an anomaly regardless of the proof's apparent validity.

**Status: observed (EXTRACTION_007). Epistemic Tier A** for the incident; **Tier B** for the generalization across bridge architectures.

---

### Attack 11 — Pooled Custody Adapter Compromise (Aethir category)

**Storing potential.** OFT adapter or lock-and-release adapter deployed with an EOA admin (no multisig, no timelock). Adapter accumulates user deposits in pooled custody. Admin key sits on a single device / in a single engineer's wallet.

**Seeding.** The TVL accumulates over weeks or months. The admin privilege includes the ability to mint, pause, or withdraw. The admin identity is typically a matter of public record (deployer address is on Etherscan) and the private key is in the custodian's operational setup.

**Discharge.** Private key is compromised via (a) phishing of the keyholder, (b) malware on the keyholder's device, (c) supply-chain attack on wallet software, (d) social engineering a key export, or (e) direct insider action. Attacker uses the authorized admin function to mint-or-drain the pool. The on-chain signature is cryptographically valid; the code enforces exactly what the signature authorizes.

**Lexicon framing.** This is the textbook [Operational Layer Attack](docs/lexicon.md#operational-layer-attack) validated by Blockaid's January 2026 prediction: "2026 attacks will target operational layers around key management, not the keys themselves." The amplification is [Pooled Custody Amplification](docs/lexicon.md#pooled-custody-amplification) — the drained tokens are indistinguishable from legitimate holdings, retain market value, and compose into downstream DeFi.

**Observed components:**
- **EXTRACTION_006 (Aethir, 2026-04-09, ~$400K)**: BNB Chain, `AethirOFTAdapter`, EOA admin, private-key compromise. Dev.to post-mortem explicitly identifies EOA-without-multisig as the operational structure ([extraction_event_006_aethir.md](reports/extraction_event_006_aethir.md)).
- **EXTRACTION_005 (Drift, 2026-04-01, ~$285M)**: governance-layer variant — durable-nonce pre-signing from socially-engineered Security Council members, threshold reduction from 3/5 → 2/5 as the phase transition that opened the window.
- **Zerion DPRK attack (2026-04-10, ~$100K)**: the small-scale social-engineering version of the same category.
- **Bybit ($1.5B, 2025)**: the canonical large-scale operational-layer attack; cited as precedent in the decks.

**Why it's hard to see:**
- No code is defective.
- No on-chain configuration is unusual until the moment of the attack.
- The attack IS a signature the protocol was designed to accept.
- Defense lives in operational security (key management, multisig policies, timelock on admin functions), which is not auditable from on-chain data.

**Detection hooks:**
- **`infrastructure_registry`-based enumeration of all high-TVL single-admin adapters.** Any adapter with an EOA admin, no multisig, and a pooled-custody mechanism is pre-validated as Aethir-class risk.
- **Admin-role timelock checking**: adapters where admin functions can be invoked with zero delay are categorically higher-risk than ones with a 48-hour timelock.
- **Cross-check with private-key leak intelligence**: if an adapter's admin address matches an address seen in known phishing / malware exfiltration databases, alert.
- **Post-compromise detection**: sudden admin-invoked large transfer that drains >X% of custody. This catches the attack at block N but the funds are already moving.

**Status: observed (EXTRACTION_006, EXTRACTION_005, Zerion). Epistemic Tier A.**

---

### Attack 12 — Oracle Manipulation via Fake-Token Collateral (Drift / Rhea category)

**Storing potential.** Attacker deploys a fake token with no real utility. Seeds a pool (Raydium, Ref Finance, equivalent) with small real liquidity on one side and the fake token on the other. Wash-trades against themselves to establish a price history. Protocol oracles reading the pool report the wash-traded price as truth.

**Seeding.** The fake-token price stabilizes at a calibrated target — typically ~$1 to make the token accepted as stablecoin-class collateral. The time between pool seeding and exploitation is calibrated against the oracle's TWAP window; if the oracle averages over 24h, the attacker waits 24h+ before the next phase. The protocol's governance / configuration does not flag the new token.

**Discharge.** Attacker deposits the fake token into a lending or margin protocol that accepts it as collateral. The oracle reports the fake-token value as legitimate. The protocol authorizes a loan or margin position worth the reported value; the attacker extracts the borrowed real assets. The fake token collapses post-extraction; the borrowed real assets have already moved to the attacker's settlement path.

**Lexicon framing.** This is the canonical [Verification-Path Trust Failure](docs/lexicon.md#verification-path-trust-failure): the lending protocol has no defect; the oracle has no defect; the pool executed its AMM math correctly. The failure is at the *composition* — the oracle is asked to provide a truth it cannot verify (the token's fundamental value), and the protocol trusts the attestation unconditionally. The downstream extraction is [Compositional Harm](docs/lexicon.md#compositional-harm) at its purest.

**Observed components:**
- **EXTRACTION_004 (Rhea, 2026-04-16, ~$18.4M)**: fake tokens without NEP-141 metadata deployed on implicit accounts on NEAR. Ref Finance pool IDs 8528-8538 paired them with USDC. Rhea's margin-trading oracle accepted the manipulated prices. ([extraction_event_004_rhea_finance.md](reports/extraction_event_004_rhea_finance.md))
- **EXTRACTION_005 (Drift, 2026-04-01, ~$285M)**: fake CVT token on Raydium wash-traded to ~$1; Drift's oracle accepted it as collateral for ~$285M in real assets across two transactions four slots apart. ([extraction_event_005_drift.md](reports/extraction_event_005_drift.md))
- **Silo (2026-04-03)** referenced as contemporaneous; same category.

**Why it's hard to see:**
- The fake token isn't a trap contract; it's a legitimate token with no reason to be flagged.
- The wash-trading activity on the pool looks like organic early liquidity.
- The oracle is behaving correctly relative to its data source.
- No single component is defective; the harm is compositional.
- Prediction requires watching "which new tokens on which pools get admitted to which protocols as collateral" — a graph-level analysis that doesn't map cleanly onto any existing free scanner.

**Detection hooks:**
- **Pool-lifecycle monitor**: track new token-pool creations across Raydium, Ref Finance, Uniswap V3, etc., and identify pools where liquidity is asymmetric (one-sided seeding) and where swap volume is concentrated between a small number of addresses.
- **Oracle-input graph**: for every lending / margin protocol, enumerate which pools feed which price oracle, and flag any pool that has been in the feed for less than N days OR whose liquidity has been dominated by self-trades.
- **New-collateral admission monitor**: many protocols have governance-gated collateral lists. Monitor those governance processes for admission of tokens whose TWAP is dominated by wash activity.
- **Post-admission grace-period pressure testing**: when a protocol admits a new collateral token, simulate the economic impact of a 90% price drop and surface the borrow capacity at the admission price. That's the extraction ceiling.

**Status: observed (EXTRACTION_004, EXTRACTION_005). Epistemic Tier A.**

---

### Attack 13 — Operational Layer Compromise at Governance Scale

**Storing potential.** Protocol runs governance via a council (Security Council, Admin Council, Foundation Board). The council holds privileges like setting parameters, changing signature thresholds, enabling/disabling timelocks, or approving upgrades. Members of the council have their personal wallets and keys outside the protocol's operational security envelope.

**Seeding.** Attacker identifies council members. Via phishing (LinkedIn recruiter pitch, fake security advisory email, job offer that requires a "test task"), malware-laden wallet software, or social engineering, the attacker acquires either (a) private keys directly, or (b) durable nonce signatures that can be broadcast later without the member's knowledge. The council member does not know their credentials have been compromised.

**Discharge.** Attacker chooses the moment when enough compromised signatures exist to reach the active threshold. Often this requires waiting for the protocol to change its own rules — e.g., a governance vote to reduce threshold from 3/5 to 2/5, or to remove a timelock. Once threshold is met, the attacker submits their pre-signed governance action. The action executes; the protocol is mis-configured or drained.

**Lexicon framing.** An extreme [Operational Layer Attack](docs/lexicon.md#operational-layer-attack). Often layered with a [Configuration-Level Vulnerability](docs/lexicon.md#configuration-level-vulnerability) — the governance action that the attacker executes is usually to weaken a protection (lower threshold, remove timelock) before the extraction. The Drift case shows both: threshold reduction on 2026-03-27 was the phase transition; the attack followed on 2026-04-01.

**Observed components:**
- **EXTRACTION_005 (Drift, 2026-04-01)**: durable-nonce signatures pre-acquired from Security Council members. When the threshold dropped from 3/5 to 2/5, the attacker already had 2 valid signatures.
- **Bybit ($1.5B, 2025)** precedent.
- **Zerion (2026-04-10, ~$100K)** as smaller-scale phishing variant.

**Why it's hard to see:**
- Compromise happens off-chain.
- The signatures are cryptographically valid.
- The code honors them. There is no defect to catch.
- The phase transition (threshold change, timelock removal) may be pre-announced and voted on by the legitimate council, making it look like ordinary governance.

**Detection hooks:**
- **Governance-parameter monitor**: any reduction in signature threshold, removal of timelock, or broadening of admin scope on a high-TVL protocol should trigger a watch period. Layer 3 has no visibility into this today.
- **Durable-nonce signature lifetime tracking**: Solana's durable nonce mechanism allows signatures to be valid indefinitely. Protocols using it should track outstanding durable-nonce instructions against expected operations.
- **Council-member activity monitoring**: unusual patterns in council members' personal wallets (sudden inactivity, new-device signing, atypical asset movements) as leading indicators.
- **Phishing-infrastructure intelligence**: track known phishing campaigns targeting council-level roles (LinkedIn recruiter phishing, fake tech-interview malware) and cross-reference to protocols those targets work on.

**Status: observed (EXTRACTION_005, Bybit). Epistemic Tier A** for the incidents; **Tier B** for generalization to "any council-governed protocol with durable-signature mechanisms."

---

### Attack 14 — Advisor-Parasite Pattern (Pattern F in Behavioral Laundering)

**Storing potential.** A trusted intermediary — an "advisor," "crypto concierge," "onboarding consultant" — positions themselves as the victim's gateway to crypto. They manage wallet setup, approve-to-this-router decisions, bridge routing, tax optimization. Approvals and routing permissions accumulate in self-controlled contracts.

**Seeding.** The advisor relationship is durable — months or years. The victim retains balance and continues to interact; the advisor takes small, regular cuts framed as "service fees," "gas reimbursement," "tax collection," or "routing optimization." Each individual extraction is below the victim's [Just-Noticeable-Difference](docs/lexicon.md#cost-habituation-asymmetry) threshold. The victim does not realize they are being exploited because the relationship is consistently helpful.

**Discharge.** Phenomenologically, there is no single-shot discharge. The extraction is continuous, calibrated to the victim's cost-habituation window, and sustained over the duration of the advisor relationship. Aggregate extraction over 12-24 months can exceed an equivalent phishing drain; per-victim NOI is lower; total NOI across many victims can exceed a phishing operation's total.

**Lexicon framing.** The relationship-of-trust variant of [Pattern A — Reputation-Building Sacrifices](docs/lexicon.md#pattern-a--reputation-building-sacrifices). Exploits [Participatory Asymmetry](docs/lexicon.md#participatory-asymmetry--predatory-literacy) (victim lacks pattern-recognition vocabulary), [Micro-Cost Habituation](docs/lexicon.md#micro-cost-habituation) (each charge below the JND threshold), and [Cognitive Load Concentration](docs/lexicon.md#cognitive-load-concentration) (victim offloads crypto decisions to the advisor specifically because they find crypto cognitively heavy).

**Observed components:**
- Scanned 2026-04-18 (`scripts/advisor_parasite_scan.py`, [reports/advisor_parasite_candidates.md](reports/advisor_parasite_candidates.md)).
- Result: 16 candidates passed the structural filter (50+ approvers, ≥14-day duration, infrastructure excluded). Every one turned out to be legitimate DeFi infrastructure OR an unidentified pattern that did not match the advisor-parasite cadence.
- **Zero confirmed advisor-parasites in current corpus.** Corpus age ≤ 30 days is too short for the months-long extraction signature. `approval_events` doesn't index outbound Transfer flows (only approvals to flagged spenders).
- Confirmed counterexamples: CE5E, E717, A7B9, E3B2 are classical phishing drainers (single-approval + single-sweep per victim, no retention), not advisor-parasites.

**Why it's hard to see:**
- The victim does not report the relationship as adversarial.
- Each individual transaction is below the JND threshold and indistinguishable from legitimate service fees.
- Structural signature (50+ approvers, ≥14-day duration) overlaps heavily with legitimate DeFi routers — the hard filter is "is this a router or is this an advisor," which is not derivable from on-chain data alone.
- Requires both (a) Transfer-event indexing of outbound victim flows, and (b) corpus age ≥ 90 days to resolve the months-long cadence.

**Detection hooks:**
- **Transfer-event flow indexer** for all addresses that hold ≥50 approvals (dependency: not yet deployed).
- **Per-victim cadence histograms**: distinguish 1-2 outbound transfers/month × 12 months (advisor) from 1 approval + 1 sweep (phishing) from 10 outbound/day (infrastructure).
- **Off-chain OSINT integration**: advisor-parasites often have public-facing personas (Twitter, LinkedIn, YouTube presence as "crypto guides"). Cross-referencing on-chain addresses to such personas is a viable detection layer.
- **Rescan triggers**: (a) corpus age ≥ 90 days, (b) Transfer-event indexer deployed ≥ 30 days, (c) `infrastructure_registry` ≥ 50 entries. None of these are currently satisfied.

**Status: components partially observed, pattern remains unconfirmed in Layer 3's corpus, architecturally well-specified. Epistemic Tier C** — speculation about a pattern that has structural justification but no confirmed Layer 3 instance yet.

---

## Cross-cutting notes

**Why a v2 now.** April 2026 shipped 8 major exploits across 18 days. Several fit v1's anticipated categories at the single-contract scale (Aethir as Attack-2-mini); several established entirely new categories (Kelp's cross-chain DVN failure, Hyperbridge's MMR bypass, Drift/Rhea's fake-collateral oracle manipulation, governance-scale operational compromises). The cost of *not* updating is that the threat-modeling document slides out of load-bearing status — it loses its value as a pre-built detector manifesto if it's two weeks behind the frontier. v2 restores that load-bearing status, incorporates the lexicon vocabulary, and preserves v1 as an archive.

**What still separates these from generic threat-modeling.** Each attack cites specific `extraction_events` rows, deployer addresses, selectors, or configuration reads from the Layer 3 corpus. They are not abstract. Every one either points at a confirmed incident or at corpus patterns that would be mechanical to assemble.

**Status legend (unchanged from v1):**
- **Observed:** the full chain seen end-to-end
- **Components observed, chain hypothetical:** every link in the corpus, assembly not confirmed
- **Architecturally valid, unconfirmed:** threat model sound, at least one component hypothetical

**v2 status count:**
- Observed: 6 attacks (Attacks 5, 9, 10, 11, 12, 13)
- Components observed, chain hypothetical: 5 attacks (Attacks 1, 2, 4, 7, 14)
- Architecturally valid, unconfirmed: 3 attacks (Attacks 3, 6, 8) — preserved from v1 unchanged

6-of-14 **observed** is a material change from v1's 0-of-8. The April wave validated the combinatorial threat-modeling approach: attacks that were hypothetical in v1 either landed as described (Aethir → Attack 2 single-contract) or established new categories that were structurally predictable from the primitives (Kelp, Hyperbridge, Drift, Rhea). The v1 archive is therefore itself evidence of framework maturity over time.

**Epistemic tier discipline.** Every attack now carries an explicit [Epistemic Tier](docs/lexicon.md#epistemic-tier-classification) tag in the Status line. Tier A claims are load-bearing in pitches and external materials. Tier B claims are for methodology discussion. Tier C claims are never cited in commercial materials without explicit framing as prediction.

**Relation to the correction log.** Every retraction or revision of a v2 attack's Status (observed → unconfirmed, or the reverse) is a correction-log-triggering event. v1 had no such discipline; the archive records what we got right AND what we overclaimed in 2026-04-07, and Correction #4 onward in [reports/correction_log.md](reports/correction_log.md) documents revisions across the framework broadly.

---

## Appendix — v1 → v2 crosswalk

| v1 | v2 | Change |
|---|---|---|
| 1 Permission Harvesting + Routing Parasite | 1 (Part I) | Preserved, language updated |
| 2 Dormant Fleet + Proxy Upgrade Swap | 2 (Part II) + 11 (Part III) | Split. Fleet version preserved as 2; single-contract variant (Aethir) formalized as new Attack 11 |
| 3 TaaS Template with Hidden Skim | omitted from Part I; preserved in archive | Still valid, not updated; reinstate if it lands |
| 4 Time-Lock Synchronized Fire | 4 (Part I) | Preserved |
| 5 Cross-Chain Rotation Evasion | 5 (Part II) + Pattern D lexicon entry | Superseded by Pattern D framework; v2 points to lexicon |
| 6 Probe-Trap Targeting Scanners | 6 (Part I) | Preserved |
| 7 Custom Selector Drain Avoiding Logs | 7 (Part I) | Preserved |
| 8 Infrastructure-Layer TaaS Skim | 8 (Part I) | Preserved |
| — | 9 Cross-Chain DVN Verification Failure | NEW — Kelp category |
| — | 10 Cross-Chain Proof Verification Bypass | NEW — Hyperbridge category |
| — | 11 Pooled Custody Adapter Compromise | NEW — Aethir category (single-contract cousin of v1 Attack 2) |
| — | 12 Oracle Manipulation via Fake-Token Collateral | NEW — Drift / Rhea category |
| — | 13 Operational Layer Compromise at Governance Scale | NEW — Drift governance, Zerion social-engineering |
| — | 14 Advisor-Parasite Pattern | NEW — Pattern F; structurally specified, not yet observed |
