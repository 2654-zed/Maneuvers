# V4 — Maneuvers (standardised)

**Status of this file.** The updated framework, produced only after the reconstruction (`reports/historical_reconstruction.md`), the claim ledger, the temporal audit and the prediction audit. V4 is not a rewrite of V3: each entry states what it inherits from V1–V3, what evidence changed it, and why its epistemic status is what it is. Historical V1/V2/V3 files are untouched.

**Epistemic status** refers to *public, independently checkable instances* of the maneuver as described — not to whether the mechanism is plausible and not to whether Layer 3's private data contains a match:
- **OBSERVED** — ≥2 independent public instances with a post-mortem or on-chain confirmation of the mechanism (one instance is enough if it was reproduced on-chain here).
- **STRONGLY INFERRED** — the mechanism is documented but the instances are single, partially documented, or corpus-internal with a public handle.
- **HYPOTHESIZED** — structurally specified, components exist, no confirmed instance.
- **THEORETICAL** — reasoning only; no components observed.

**Confidence** is explained, never scored. **Every signal carries a base-rate note**: the benign population that produces the same signal. **Losses** are stated notional / realised / recovered where the distinction matters.

Evidence codes: `OC` = `reports/evidence/onchain_checks_2026-09-28.md`; `VA` = `verification_april_wave_2026-09-28.md`; `VM` = `verification_may_wave_2026-09-28.md`; `PS` = `post_revision_survey_2026-09-28.md`; `C-nnn` = claim ledger.

## Index

| ID | Maneuver | Status | Inherits from |
|---|---|---|---|
| M-01 | Cross-chain attestation-threshold failure (sole or captured verifier) | OBSERVED | Attack 9 |
| M-02 | Cross-chain proof / message verification code defect | OBSERVED | Attack 10 (broadened) |
| M-03 | Privileged-key or signing-pipeline compromise → authorised action | OBSERVED | Attack 11a, Operational Layer Attack |
| M-04 | Unprotected initializer / role-grant takeover | OBSERVED | Attack 11b |
| M-05 | Governance capture with no execution delay | OBSERVED | Attack 13 (broadened) |
| M-06 | Collateral-valuation manipulation (fake, thin, stale, or forged price) | OBSERVED | Attack 12 (broadened) |
| M-07 | Malicious participant inside a threshold-signature protocol | OBSERVED | Attack 15 (resolved) — new class |
| M-08 | Standing-approval and delegation drains (users and bots) | OBSERVED | Attack 1 (approval half), drainer case files |
| M-09 | AI-agent permission-chain abuse | OBSERVED | Confused Deputy (agentic) |
| M-10 | Weak key generation at scale | OBSERVED | new class |
| M-11 | Operational-layer social-engineering campaign | OBSERVED | Operational Layer Attack |
| M-12 | Front-end / vendor supply-chain injection | OBSERVED | Cross-Domain Compositional Harm |
| M-13 | Chain- or protocol-level halt / rollback / freeze (defender maneuver) | OBSERVED | Neutrality Trap phase 4; Kill-Switch Governance |
| M-14 | Pre-positioned dormant infrastructure (attacker EOAs, fleets, staged pools) | STRONGLY INFERRED | Stored Potential; Single-Purpose Funder; Attack 2/4 |
| M-15 | Aged / cross-chain identity as cover | STRONGLY INFERRED | Pattern D; Pristine Solo Operator |
| M-16 | Protocol-family recurrence (same operator returns) | STRONGLY INFERRED | Protocol-Family Specialist |
| M-17 | Facilitator self-settlement of standing allowances (rogue or ambiguous) | HYPOTHESIZED | CE5E / x402 drainer case files |
| M-18 | Convergent templates without coordination | HYPOTHESIZED | Convergent Calibration |
| M-19 | Routing parasite (aggregator-pool backdoor) | HYPOTHESIZED | Attack 1 |
| M-20 | Coordinated fleet proxy-upgrade swap | HYPOTHESIZED | Attack 2 (fleet mode) |
| M-21 | Template / infrastructure skim (TaaS) | HYPOTHESIZED | Attacks 3, 8 |
| M-22 | Time-lock synchronised fire | HYPOTHESIZED | Attack 4 |
| M-23 | Probe-trap discrimination against scanners | HYPOTHESIZED | Attack 6 |
| M-24 | Advisor-parasite slow extraction | HYPOTHESIZED | Attack 14 / Pattern F |
| M-25 | Log-less extraction as anti-forensic design | HYPOTHESIZED (downgraded) | Attack 7 |
| M-26 | Signal manipulation against behavioural detectors | THEORETICAL | Publishing-Induced Recursive Evasion |
| M-27 | Adversarial verifier-set entry at scale (buying seats) | THEORETICAL | extrapolation of M-07 / M-05 |

Removed from the framework (with reasons) — see `CHANGELOG_FROM_V3.md`: Thermodynamic Fundamentalism; Hybrid Gameboard as grounding; Victim-to-Predator Pipeline; Infrastructure-Scale Operator as a behavioural typology; the "six phases as law" formulation; Static-vs-Dynamic as a safety claim.

---

## OBSERVED

### M-01 — Cross-chain attestation-threshold failure (sole or captured verifier)

**Maneuver.** A cross-chain message is accepted on the destination chain because the set of verifiers that must attest to it is one party, or has been reduced to one party, and that party is compromised, poisoned, or *is the attacker*. The destination contract then releases custody or mints.

**Preconditions.** (1) An OApp/bridge channel whose required-verifier threshold is 1 (or optional threshold + required = 1); (2) a reservoir on the destination side (lock-release custody or mintable supply); (3) either a way to compromise the single verifier's *signing inputs* (RPC poisoning suffices — keys need not leak) or a way to *become* the verifier (delegate/config-role capture).

**Mechanism.** Kelp: LayerZero Labs' DVN was the sole required DVN on the Unichain→Ethereum channel; LayerZero's own RPC nodes had been backdoored (March 6 social-engineering breach; op-geth patched in memory), external RPCs were DoS'd on the day, the DVN signed a packet for a Unichain transaction that never existed; the adapter released 116,500 rsETH from custody (`OC` §1–4; `VA` §8). Sandbox: SAND is an ERC-677 token *and* the OApp; `approveAndCall` gave arbitrary-call-as-the-token, so the attacker called `Endpoint.setDelegate(attacker)` then `setConfig(requiredDVNs=[attacker])`, self-attested a forged inbound and minted 329T SAND; realised loss came from draining the Ethereum lock-release adapter (`PS` A.3).

**Observable signals (with base rates).** `getConfig(configType=2)` threshold < 2 on either send or receive path — *base rate: 47% of ~2,665 active OApps on 2026-04-20; the signal alone is a population, not a target; combine with reservoir size (>$10M) and composability depth.* Configuration *change* events (`setConfig`, `setDelegate`, peer changes) on an OApp — *base rate: legitimate operators change configs; the discriminator is a change that lowers a threshold or hands delegate to a fresh address.* Inbound delivery of an amount that is an outlier against the channel's history to a fresh, mixer-funded address — *base rate: low, but only measurable with channel-level baselines.* Verifier signing-path anomalies — *not observable at tx level (DVNs sign off-chain); requires `PacketVerified`-style event indexing.*

**Actors.** State-level operational attackers (Kelp: UNC4899); opportunists with a code-defect entry (Sandbox: attacker EOA dormant 313 days); colluding operators (no confirmed case).

**Incentives.** Reservoir size is enormous relative to cost when the verifier is a single party and custody is pooled; the stolen asset composes downstream (Aave) before backing is questioned.

**Consequences.** Custody release; downstream bad debt (Aave shortfall ~163K ETH); ecosystem policy change (3-of-3 defaults; migrations to CCIP; litigation).

**Evidence.** Kelp reproduced on-chain here; LayerZero incident report; Sandbox post-mortem and PoC; Dune population measurement; Kelp's channel now 4-of-4 (`OC` §3).

**Epistemic status.** OBSERVED (Kelp; Sandbox; Stake DAO contested).

**Confidence.** High that the class exists and that threshold reads are the correct pre-trigger signal — the ecosystem independently adopted exactly this check. Medium that threshold monitoring alone is sufficient: the only post-Kelp instance created its own threshold condition.

**Falsification criteria.** A demonstration that ≥2-of-N configurations were exploited via honest-majority failure without any verifier compromise would move the class boundary; a year of ≥$10M 1-of-1 channels with zero discharge after LayerZero's DVN-side refusal would suggest the risk was concentrated in one operator's infrastructure rather than in the configuration per se.

**Defensive implications.** Enforce the invariant at the endpoint/library (refuse threshold < 2), not by one operator's policy; monitor `configures` edges (delegate, DVN set, peers, confirmations) as *drift* events; index verifications by DVN; run a cross-chain burn/release conservation check; downstream lenders score bridge hops and wrap depth (Aave AST framework).

---

### M-02 — Cross-chain proof / message verification code defect

**Maneuver.** A bridge, sidechain or rollup verifier accepts a structurally invalid, ambiguous, replayed or cached proof/message as valid, releasing custody or minting unbacked assets. Inherits Attack 10 but is broadened: the failures in the window were not only Merkle edge cases but non-injective encodings, cache-key collisions, unvalidated registry mappings, relayer event parsing, and partial validation on immutable contracts.

**Preconditions.** A verifier whose acceptance condition is weaker than "this message was produced by the source chain in the claimed form": missing bounds checks (Hyperbridge), missing binding between proof and request body (Hyperbridge), variable-length fields concatenated without delimiters (Wanchain), verification caches keyed without full context (Liquid), unvalidated denom/asset mappings (Gravity), commented-out checks (Secret), relayers that ignore tx failure status (Across-Solana), rollup state vs. verified tx-set divergence (Aztec), duplicate commitments interpreted differently by two clients (Syscoin).

**Mechanism.** Craft the proof/message the verifier mishandles; the honest verifier set signs or accepts; custody released or supply minted; dump before the peg breaks.

**Observable signals.** Release/mint with no corresponding source-side burn/lock (conservation invariant) — *base rate: near zero for a correctly functioning bridge; this is the only signal in the class with a clean base rate, and it fires at trigger, not before.* Unusual proof shapes / repeated identical proofs — *observable only by the verifier operator.* Repeat exploitation of the same protocol (Verus: 66 days) — *base rate: unpatched protocols re-exploited is common.*

**Actors.** Skilled independent operators; some return funds (Liquid 85%; Syscoin 100%; Dango 100%).

**Incentives.** Large reservoirs; often no state actor needed; realised value limited by liquidity (mint exploits realise a small fraction of notional — Sandbox $675K of ~$49B; Symbiosis $336K; Hyperbridge ~$2.5M of 1B DOT).

**Consequences.** By DefiLlama labels ≈ $385M notional in the window (Liquid alone ~$320M, 85% returned); chain splits and pauses.

**Evidence.** Hyperbridge (`VA` §5); Gravity, Secret, Syscoin, Aztec, Taiko, Across, Wanchain, Verus, Liquid, Nomic, Symbiosis (`PS` A.3, B).

**Epistemic status.** OBSERVED (≥10 independent instances).

**Confidence.** High that the class is the highest-notional bridge failure mode of 2026 and is *not* audit-obsolete. The historical framework's decision to treat it as commercially uninteresting was wrong by two orders of magnitude on value.

**Falsification criteria.** A window in which conservation-invariant monitoring is widely deployed and this class's realised losses drop to near zero would support the audit-and-monitor remedy; continued losses despite audits would support the "verifier code is intrinsically hard" reading.

**Defensive implications.** Conservation checks (source burns vs destination releases) as the first monitor to build; second independent verifier implementations (LayerZero's Rust client; CCIP DVN adapter); challenge periods; supply caps and rate limits (Dango's bridge rate limit held the realised loss to $410K); explicit "same flaw twice" tracking.

---

### M-03 — Privileged-key or signing-pipeline compromise → authorised action

**Maneuver.** An action the system is designed to accept — upgrade, mint, withdraw, sign a price, sign a withdrawal — is executed because the attacker holds the key, the session, or the *request path into the signer*. Sub-modes: (a) single-key admin compromised (Wasabi, Volo, DxSale, Triple-A, Duelbits); (b) all keys of a multisig on one device (Humanity: 6-of-6 and 5-of-5 on one laptop); (c) infrastructure secret leaked (Taiko prover key in GitHub; SingularityNET cloud → bridge keys); (d) *signing-pipeline integrity*: keys intact, requests forged (Bitget: internal credentials from a third-party product → forged withdrawal requests the exchange's own signers signed, $387.5M); (e) oracle signer key (Ostium: signed BTC price $5K→$60K accepted with no bounds, $23.75M).

**Preconditions.** Authority concentrated in a key/seat/service with zero or short delay over a reservoir; an off-chain path to that key or to the inputs its holder trusts.

**Mechanism.** Off-chain: phishing, malware, malicious repo, vendor compromise, insider. On-chain: `grantRole`/`upgradeTo`/`transferOwnership`/`mint`/`withdraw` with valid signatures.

**Observable signals.** Pre-trigger: admin is an EOA; no timelock; role grants with delay 0; multisig thresholds equal to signer count on one operator — *base rate: very common; the discriminator is reservoir size, not the topology.* At trigger: admin-invoked large transfer / upgrade to unverified implementation / round-number gas limits and never-seen destinations (Bitget) — *base rate: low; catches at the moment of loss.* Pre-positioned helper contracts deployed by fresh EOAs at nonce 0 across chains (Wasabi) — *base rate: any fresh deployer's first contract shares an address across chains; not a signal of intent.*

**Actors.** DPRK operational units (Bybit, Drift, Kelp-adjacent, Bitget likely); criminal groups; insiders (unresolved in DxSale, Coinsbuy).

**Incentives.** Highest value-per-incident class of 2026 (Blockaid: 74% of H1 stolen value operational/infrastructure).

**Consequences.** Direct loss; forced protocol shutdowns; treasury/insurance payouts (Bitget's $464M fund).

**Evidence.** `VA` §1, §3 (Aethir — unverified root cause, retained only as a possible instance), §9; `VM` §1, §2; `PS` A.3 (Humanity, Taiko, Ostium, Triple-A, SingularityNET, Bitget, Duelbits).

**Epistemic status.** OBSERVED (many instances).

**Confidence.** High. The historical anchor (Aethir) is dropped as unverified; the class does not need it.

**Falsification criteria.** Not falsifiable as a class; the *hook* "EOA admin + no timelock ⇒ elevated discharge probability" is falsifiable by measuring discharge rates across admin topologies and finding no difference.

**Defensive implications.** Timelocks and thresholds are necessary but insufficient (Humanity had 6-of-6); bind signers to an independent ledger of intended actions (Hypernative's Bitget prescriptions); validate every parameter against pipeline-generated values; auto-pause signers on anomaly; treat vendor/RPC/cloud infrastructure as part of the key.

---

### M-04 — Unprotected initializer / role-grant takeover

**Maneuver.** A proxy, facet or module whose `initialize()` (or equivalent role-setting function) is callable by anyone lets the attacker become owner/admin, then use the authorised upgrade path.

**Preconditions.** Deployment omitted the initializer call; implementation lacks `_disableInitializers()`; a later-added facet's initializer never executed (Aurellion); users hold standing approvals to the contract (the reservoir).

**Mechanism.** Call `initialize(attacker)`; upgrade/delegatecall to malicious logic; `transferFrom` against existing allowances.

**Observable signals.** Pre-trigger: `initialize` selector callable from a random address returns success on simulation; `_initialized` storage slot == 0 on a live proxy — *base rate: low but non-zero (abandoned/legacy contracts); combine with outstanding allowances to rank.* At trigger: initializer call from a fresh EOA followed within blocks by upgrade.

**Actors.** Opportunistic scanners; the same actor may sweep multiple targets (Renegade→Aurellion, 48 h).

**Incentives.** Cheap; approvals are the prize.

**Consequences.** Renegade $209K (90% returned); Aurellion $456K (one victim held 99%).

**Evidence.** `VM` §5, §9.

**Epistemic status.** OBSERVED (two independent instances, two days apart, both post-mortemed).

**Confidence.** High. This is the fastest-confirmed hook in the historical corpus — though it was added after Renegade, not before.

**Falsification criteria.** A population scan showing exposed initializers are vanishingly rare on contracts with allowances would make the class negligible rather than false.

**Defensive implications.** Population-wide initializer-state enumeration (nobody published one in the window — an open measurement); `_disableInitializers()` as a deploy-time invariant; revoke standing approvals to legacy proxies.

---

### M-05 — Governance capture with no execution delay

**Maneuver.** Authority over parameters, admins or treasuries is exercised by an attacker who either (a) obtained signers' pre-signed instructions or keys (Drift: durable nonces from Security Council members; AFX: 5 of 7 validator keys), or (b) bought or borrowed enough voting power to pass a proposal (BonkDAO: ~1% of supply, 2.9% turnout, no timelock; Term Finance; Neutron: 11 `Update Admin` actions executed on passage). The common precondition is zero delay between decision and execution.

**Preconditions.** Governance can change custody-relevant state; low quorum or thin token distribution, or council members reachable off-chain; no execution timelock; often a recent self-weakening (Drift's migration to 2-of-5 with 0-second timelock).

**Mechanism.** Acquire signatures or votes; submit; execute immediately; drain or hand admin to attacker contracts.

**Observable signals.** Pre-trigger: governance parameter changes that lower thresholds or remove delays — *base rate: routine in healthy governance; rank by reservoir.* Token accumulation by fresh addresses before a proposal (BonkDAO bought on exchanges days before) — *base rate: speculators accumulate before votes too.* Proposal payloads containing `Update Admin` / role grants to fresh addresses — *base rate: low; content inspection is the discriminator.* Durable-nonce accounts created for council members — *observable on Solana; base rate unknown.*

**Actors.** DPRK operational units (Drift); opportunists with capital (BonkDAO ~$4M outlay for ~$20M); protocol-family specialists.

**Incentives.** Treasury and vault reservoirs; leverage of governance over custody.

**Consequences.** Drift $285–295M; BonkDAO ~$20M; Term $8.5M; Neutron ~$9.4M plus a 24.5-hour Cosmos Hub halt; AFX $24M.

**Evidence.** `VA` §1; `PS` A.3, D.

**Epistemic status.** OBSERVED.

**Confidence.** High for the class; medium for any single pre-trigger signal.

**Falsification criteria.** Governance drains occurring routinely *through* timelocks (i.e., delay does not help) would falsify the load-bearing "no delay" precondition.

**Defensive implications.** Execution timelocks with veto; content-aware proposal screening; quorum floors tied to treasury size; council key hygiene is necessary but was not the dominant failure in the window.

---

### M-06 — Collateral-valuation manipulation

**Maneuver.** A lending, margin or vault protocol values collateral through a source the attacker can dominate or corrupt, and lends real assets against it. Sub-modes: fake/wash-traded token on thin liquidity (Drift CVT, Rhea, Moonwell MAMO, Nostra NSTR, Tectonic TONIC); oracle contract flaw (Bonzo/Supra); aggregator pool selection (Nostra/Pragma mid-pointing a $99 pool against a $0.006 quote); stale valuation of a frozen/deprecated asset (Lazy Summer); forged signed price (Ostium — overlaps M-03e); exchange-rate donation inflation (Tectonic's 98-iteration loop).

**Preconditions.** Admission of a collateral whose price source is thin, stale, single-signer or attacker-seedable; borrow caps not bound to real liquidity; oracle inputs include pools the attacker can create.

**Mechanism.** Seed or pump; wait out the TWAP; deposit; borrow the protocol's real reserves; let the collateral collapse.

**Observable signals.** Pre-trigger: new collateral admitted whose liquidity is one-sided or self-traded; feed source lists with fewer live sources than recommended (Nostra: 2 of 3); price sources that reference a token the attacker minted — *base rate: many small tokens have thin liquidity; the discriminator is admission to a lender.* Pre-positioning over weeks (Nostra since March; Drift since March 11) — *base rate: unobservable without knowing the target.*

**Actors.** DPRK (Drift); independent operators (Rhea, Tectonic, Moonwell); insiders unknown.

**Incentives.** Borrow capacity at the admission price is the extraction ceiling (the corpus's "90% drop pressure test" is the right measure).

**Consequences.** Tectonic $120M gross / $9M unrecovered after a chain rollback; Ostium $23.75M; Rhea $18.4M; Bonzo $9M; Moonwell $8.7M; Lazy Summer $6M; Nostra $3.5M.

**Evidence.** `VA` §1, §7; `PS` A.3.

**Epistemic status.** OBSERVED.

**Confidence.** High. The historical hooks (pool-lifecycle, oracle-input graph, admission monitor, pressure test) were well aimed; two sub-modes were missing (stale valuation; signer compromise) and one detail was overfitted (the "~$1 stablecoin-class" target).

**Falsification criteria.** A lender that admits arbitrary tokens with attacker-seedable pools and is *not* exploited over a long horizon would undermine the precondition (unlikely).

**Defensive implications.** Borrow caps bound to verifiable liquidity; multi-source feeds with liveness checks; decommissioned assets valued at zero; sanity bounds on signed prices; admission-time pressure testing.

---

### M-07 — Malicious participant inside a threshold-signature protocol

**Maneuver.** An attacker obtains a legitimate seat in a threshold-signing set (validator, signer, MPC party) and uses protocol interaction — not key theft — to extract other parties' key shares or bias key generation, then signs directly.

**Preconditions.** Permissionless or bond-gated entry to the signing set; a TSS implementation with unverified parameters (THORChain's tss-lib fork: no biprime check on Paillier moduli; range proofs verified in halves; small blinding range) or without identifiable aborts; enough rounds/time to accumulate leakage.

**Mechanism.** THORChain: churn in (~635K RUNE bond), plant a malformed multi-prime Paillier modulus, deliberately fail the MtA step 864 times over ~2.5 days, reconstruct the Asgard vault key, sign outbounds on BTC/ETH/BSC/Base directly (`VM` §6).

**Observable signals.** Pre-trigger: a newly churned-in node with an anomalous keysign-failure rate — *base rate: honest nodes fail keysigns too, but not hundreds of times in 48 hours; this is the strongest pre-trigger signal in the entire V4 set and no one was watching it.* Node-age/bond anomalies (new node, large bond, joined developer channels days earlier). At trigger: solvency-checker imbalance >1% (fired within ~52 min).

**Actors.** Well-capitalised, cryptographically skilled operators; seat cost is the attacker's investment.

**Incentives.** Vault reservoir ($10.7M realised) vs bond at risk (~635K RUNE slashed) — the net was positive; a THEORETICAL scaling (M-27) asks when it stops being.

**Consequences.** $10.7M; five-week trading halt; migration GG20 → DKLS/FROST; bounty-program controversy; Maya Protocol (08-18, $1.7M) possibly related (unverified).

**Evidence.** THORChain Exploit Reports #1/#2; GitLab MR 4820 (separate bug); TRM; `VM` §6.

**Epistemic status.** OBSERVED (one fully post-mortemed instance; the class is defined by the mechanism, and the audit rule allows one instance when independently documented at this depth).

**Confidence.** High on mechanism (official reports, cryptographic detail); medium on generality (other TSS deployments use patched libraries).

**Falsification criteria.** Demonstration that the leakage required THORChain-specific fork bugs absent from all other production TSS systems would narrow it to a one-off; a second instance elsewhere would confirm the class.

**Defensive implications.** Per-participant keysign-failure monitoring with jailing (THORChain shipped this); parameter verification (biprime proofs); identifiable-abort TSS; minimum validator age; keyshare-at-rest encryption; hot/lukewarm vault split.

---

### M-08 — Standing-approval and delegation drains (users and bots)

**Maneuver.** Value moves through permissions the victim granted earlier: unlimited ERC-20 approvals, Permit2 allowances, EIP-7702 delegations, or a bot's own `wrapTo` approvals. Sub-modes: phishing-obtained signatures; address poisoning (industrialised: ~$62M in two Dec-2025/Jan-2026 hits); 7702 batch delegation (DxSale unlock of ~1,400 LP positions; ScamSniffer's $1.54M single-victim case); approval-trap tokens against MEV bots (JaredFromSubway, 06-20, $7.5M — 66 fake wrapper tokens, approvals left unconsumed by a conditional `transferFrom` skip, tripwire after ~24 h of profitable bait).

**Preconditions.** Outstanding allowance to an attacker-controlled spender, or a delegation to attacker code; a victim (or bot) that does not revoke.

**Mechanism.** Obtain the permission (phish, poison, bait); wait; sweep in a batch.

**Observable signals.** Pre-trigger: allowances to fresh spenders; approvals to tokens with delegatecall/upgrade patterns; 7702 authorizations to contracts with drain functions (USENIX '26: 63% of 3.66M authorizations linked to attacker contracts) — *base rate: approvals to fresh spenders are routine at launch; the discriminator is spender bytecode and funding.* At trigger: batch `transferFrom` to a single sink; single-second multi-victim sweeps.

**Actors.** Drainer-as-a-service operators; poisoning industrialists; honeypot builders targeting bots.

**Incentives.** Standing permissions are a persistent reservoir; bots are lucrative because they hold capital and act automatically.

**Consequences.** Long-tail losses (ScamSniffer 2025: $83.85M, 106K victims); bot drain $7.5M.

**Evidence.** `PS` C, F; corpus drainer case files (public handles: CE5E — see M-17 for the classification problem).

**Epistemic status.** OBSERVED.

**Confidence.** High that the class exists and dominates by victim count; the historical corpus's specific drainer attributions are treated separately (M-17).

**Falsification criteria.** Not falsifiable as a class.

**Defensive implications.** Revocation defaults; spender screening; 7702 delegation allowlists; for bots, never leave approvals to untrusted tokens standing; the corpus's "approval graph × spender bytecode" join is the right structure.

---

### M-09 — AI-agent permission-chain abuse

**Maneuver.** An agent that reads untrusted content and holds transfer authority is induced to act, or its permissions are expanded, by an actor who never touches a key. Grok/Bankr: an NFT gift activated "Executive" permissions; a Morse-code reply was decoded into a withdraw instruction; the automation layer treated the agent's public reply as a command.

**Preconditions.** Agent with signing authority; an input channel attackers can write to; a permission-expansion path (NFT, membership, tool) without human review; no policy layer between model output and signer.

**Mechanism.** Capability injection → prompt injection → deputy executes.

**Observable signals.** Pre-trigger: permission grants to agent wallets originating from fresh addresses; agent wallets with balance and public handles — *base rate: agent wallets are few; monitor them all.* At trigger: transfers whose instruction originated in a public post.

**Actors.** Individuals; researchers; potentially automated.

**Incentives.** Small so far (~$1M across Bankr incidents) but rising with agent capital.

**Consequences.** Bankr $175K (80–88% returned), $170K (14 wallets, session keys), $480K (X takeover); vendor policy layers added (enclave keys, per-tx limits, reply-trigger toggles).

**Evidence.** `VM` §7; `PS` C.

**Epistemic status.** OBSERVED (three Bankr incidents; x402 vulnerability censuses across all 15 facilitators).

**Confidence.** High on mechanism; low on magnitude forecasts.

**Falsification criteria.** Widespread policy layers (Coinbase agentic wallets: enclave-held keys, session caps) reducing incidents to zero would make this a solved class rather than a false one.

**Defensive implications.** Judgment layer between output and key; permission expansion requires out-of-band approval; treat public reply channels as untrusted input; x402 facilitator rule compliance.

---

### M-10 — Weak key generation at scale

**Maneuver.** Keys derived from low-entropy sources are brute-forced offline and wallets emptied years later. Coldcard firmware 4.0.1+ (2021) fell back to a software RNG with as little as ~40 bits of effective entropy; ≥15 independent attackers drained ~1,816 BTC (~$116M) from 5,200+ addresses, largely before public disclosure (07-30). Related: SecondFi, Zilliqa, RRWallet ("weak key generation", ~$122M in the window by DefiLlama labels). The April-30 mass dormant-wallet drain (~570 wallets, ~326 ETH, native ETH, no approvals) is likely the same class (root cause unresolved: LastPass vault cracking or legacy generators).

**Preconditions.** A deterministic or low-entropy generation path shipped to many users; long dormancy so nobody notices.

**Mechanism.** Reconstruct the key space; scan; sweep native assets.

**Observable signals.** Pre-trigger: none on-chain. At trigger: many long-dormant wallets emptying to few sinks within hours — *base rate: dormant-wallet awakenings happen individually; hundreds in a day is diagnostic.*

**Actors.** Multiple independent crackers.

**Incentives.** Pure computation vs. dormant reservoirs.

**Consequences.** $116M+; hardware-wallet vendor recalls.

**Evidence.** `PS` A.3, F; `VM` §10.

**Epistemic status.** OBSERVED.

**Confidence.** High. This class was entirely outside the historical ontology (no node, permission or composition) and produced one of the three largest Q3 losses.

**Falsification criteria.** n/a.

**Defensive implications.** Not a detection problem — a firmware/entropy audit problem; mass-awakening monitors give victims hours, not prevention.

---

### M-11 — Operational-layer social-engineering campaign

**Maneuver.** Weeks-to-months campaigns against people with access: fake recruiters and quant firms (Drift: six-month in-person operation; malicious repo; TestFlight wallet), malicious GitHub repos to RPC engineers (LayerZero, March 6), AI-edited lures (Zerion), Bithumb-themed spear-phish to a developer holding all keys (Humanity), Roblox exploit scripts carrying infostealers (Context.ai → Vercel).

**Preconditions.** A human with durable access; an off-chain channel to reach them; time.

**Mechanism.** Establish trust; deliver malware or extract pre-signed instructions; wait for the protocol to weaken itself (Drift) or for the moment of maximum reservoir.

**Observable signals.** Pre-trigger on-chain: durable-nonce accounts created for council members (Drift, March 23); a fresh Tornado-funded EOA (Kelp: 6.5 h before) — *base rate: Tornado withdrawals are frequent; only useful joined to a reservoir watch.* Off-chain: recruiter-pretext contact patterns tracked by SEAL/Mandiant (UNC1069 domain sets).

**Actors.** DPRK units (UNC4899/TraderTraitor, UNC4736/Citrine Sleet, UNC1069, UNC6862); ShinyHunters-style extortion crews.

**Incentives.** Largest reservoirs in the ecosystem; DPRK >$1B YTD 2026 (Elliptic).

**Consequences.** Drift, Kelp, Bybit, Humanity, Bitget (likely), Zerion.

**Evidence.** `VA` §1, §4, §8, §9; `PS` A.3, F.

**Epistemic status.** OBSERVED.

**Confidence.** High. The historical corpus's "Operational Layer Attack" concept was right; the Blockaid January attribution supporting it is not found and is dropped.

**Falsification criteria.** n/a as a class.

**Defensive implications.** Out of Layer 3's observation surface almost entirely; the useful on-chain residue is (a) pre-signed-instruction artefacts, (b) self-weakening governance changes, (c) staging wallets.

---

### M-12 — Front-end / vendor supply-chain injection

**Maneuver.** The signing UI, a vendor script, or a third-party product is compromised so that valid signatures authorise attacker-chosen actions. Bybit (Safe{Wallet} JS replaced for one Safe), Polymarket International (vendor script → malicious approvals, ~$3M), Bitget (third-party product → internal credentials → forged withdrawal requests), Vercel/Context.ai (OAuth token from a compromised SaaS vendor).

**Preconditions.** Trust in a UI/vendor path that sits between intent and signature.

**Mechanism.** Modify what the signer sees or what the backend requests.

**Observable signals.** On-chain only at trigger (round-number gas limits, never-seen destinations, velocity — Bitget).

**Actors.** DPRK; ShinyHunters.

**Incentives.** Bypasses every on-chain control.

**Consequences.** $1.5B (2025), $387.5M, ~$3M.

**Evidence.** `VA` §9; `VM` §11; `PS` A.3, D.

**Epistemic status.** OBSERVED.

**Confidence.** High.

**Defensive implications.** Independent transaction hashing on hardware; policy co-signers that reconstruct intent from an independent ledger (Blockaid Cosigner-style); vendor scope minimisation.

---

### M-13 — Chain- or protocol-level halt / rollback / freeze (defender maneuver)

**Maneuver.** After discharge, a party with sufficient authority stops or reverses state: Mimir halts (THORChain, within ~52 min via solvency checker), Cronos halt + 10,961-block rollback reversing $111M of Tectonic, Harmony rollback, Cosmos Hub 24.5-hour halt and 4-of-6 recovery multisig, Liquid pause and chain split, Taiko halt, Osmosis allBTC freeze, Arbitrum Security Council freezing 30,766 ETH (then SDNY litigation), stablecoin issuer freezes (Rhea: Tether $3.29M; NEAR Intents $1.05M).

**Preconditions.** A halt/rollback authority exists and can act within the attacker's exfiltration window; social/legal legitimacy to use it.

**Mechanism.** Parameter flip, validator coordination, sequencer halt, chain reorg, issuer blacklist.

**Observable signals.** Existence and reach time of the kill switch (the question the historical corpus posed in May); in the window this became the primary recovery mechanism (CertiK August: $110.7M of $215M returned/frozen, Cronos-driven).

**Actors.** Validator sets, foundations, security councils, issuers, courts.

**Incentives.** Loss containment vs. neutrality cost (Normative Shell Game).

**Consequences.** Recovery rates in the window were dominated by halts/rollbacks and voluntary returns rather than by on-chain prevention; litigation over frozen assets (DPRK-judgment creditors vs. Arbitrum DAO/Aave).

**Evidence.** `VM` §6; `VA` §8; `PS` A.3, F.

**Epistemic status.** OBSERVED.

**Confidence.** High. This is the historical corpus's Neutrality-Trap phase 4 turned into an operational object; it is the framework's best directional prediction.

**Falsification criteria.** A window in which large losses occur on chains with fast halt authority and the authority is not used would show legitimacy costs dominate.

**Defensive implications.** Measure per protocol: who can halt what, in how long, with what legitimacy; pre-commit halt criteria (solvency thresholds) so use is rule-based rather than discretionary.

---

## STRONGLY INFERRED

### M-14 — Pre-positioned dormant infrastructure

**Maneuver.** Attackers stage before they strike: EOAs funded and left dormant (Sandbox attacker: 313 days), pools seeded months ahead (Nostra: since March; Drift: CVT minted March 11–12), helper contracts deployed hours before (Wasabi), durable-nonce accounts created a week early (Drift), fleets deployed and left idle (corpus: single-purpose funders, 84% never interacting).

**Preconditions.** Cheap dormancy; age-as-trust; scanners that score at deploy time.

**Observable signals.** Awakening of a long-dormant funded EOA that immediately touches a high-reservoir contract — *base rate: dormant wallets awaken constantly; the join to a reservoir is the discriminator.* Mass same-bytecode deployment from a fresh L2 wallet — *base rate: high (points farming, wallet factories, test deployments); the corpus's 84%-never-interacting figure is more consistent with farming than with traps waiting for victims.*

**Evidence.** Public: Sandbox, Nostra, Drift, Wasabi. Corpus-internal: single-purpose funders, dormant fleets (unverified externally).

**Epistemic status.** STRONGLY INFERRED (public staging is documented in several post-mortems; the corpus's fleet-level version lacks a base rate).

**Confidence.** Medium. Staging is real; dormancy-as-signal is weak without a reservoir join.

**Falsification criteria.** A cohort study showing dormant-then-active wallets discharge no more often than fresh ones.

**Defensive implications.** Score *awakening × reservoir proximity*, not dormancy alone; decode `TIMESTAMP` thresholds only for contracts that already hold allowances or custody.

---

### M-15 — Aged / cross-chain identity as cover

**Maneuver.** An address with long history, or a fresh address on a new chain funded through a bridge or intents system, is used so per-chain or age-weighted scoring discounts it.

**Preconditions.** Scoring systems that weight age or per-chain history.

**Observable signals.** Mainnet-history gap before L2 first-seen (corpus: 54/100 high-risk deployers) — *base rate: unmeasured; plausibly ≥50% of all L2 deployers.* Institutional-labelled deployers behaving adversarially — *base rate: label staleness and key compromise both produce this; the `0x80b12bd0` case is unresolved (drain vs migration).*

**Evidence.** Rhea (funded via `intents.near`, verified); corpus Pattern D counts; Pristine-Solo retractions.

**Epistemic status.** STRONGLY INFERRED (mechanism documented; discriminative value unmeasured).

**Confidence.** Low-medium. The corpus's own corrections show the behavioural signal is symmetric between predatory cover and institutional expansion.

**Falsification criteria.** A control-group measurement showing no lift in trap-confirmation rate for imported identities.

**Defensive implications.** Identity/label layer with provenance as a first-class node attribute; never promote on age or history alone.

---

### M-16 — Protocol-family recurrence

**Maneuver.** The same operator returns to the same protocol family with a different vulnerability class (TrustedVolumes 2026 after 1inch Fusion 2025, per Blockaid), or the same flaw is re-exploited when unpatched (Verus, 66 days; Thetanuts legacy vault).

**Preconditions.** Unpatched or deep, complex trust graphs; attacker-side accumulated knowledge.

**Observable signals.** Cluster exploit records by operator EOA and by protocol family — *base rate: low; cheap to compute; the corpus's suggestion is sound.*

**Evidence.** `VM` §8 (attribution rests on Blockaid); Verus (`PS` A.3).

**Epistemic status.** STRONGLY INFERRED (one attributed specialist case without published linkage; two same-flaw recurrences).

**Confidence.** Medium.

**Falsification criteria.** Published address linkage disproving the TrustedVolumes same-operator claim; or a finding that recurrences are overwhelmingly same-flaw (recidivism) rather than specialism.

**Defensive implications.** After an incident, the *protocol family* — not just the patched contract — is elevated risk for months.

---

## HYPOTHESIZED

### M-17 — Facilitator self-settlement of standing allowances (rogue or ambiguous)

**Maneuver.** An address that holds unlimited Permit2/ERC-20 allowances from many payers pulls funds to itself in batches (`transferFrom` where caller == payee) and forwards them out. The historical corpus classified CE5E and six siblings as rogue x402 facilitators draining phishing victims ($929K CE5E; $3.9M → $2.3M across four).

**Why HYPOTHESIZED rather than OBSERVED.** The on-chain shape is verified and persists (CE5E active 2026-09-28; `OC` §5). What is not established is that the payers are victims: single-second batch pulls of round-number amounts, the same "victim" (`0xa3a1d7a5`) paying again five months later, the corpus's own finding that 42% of top-value "victims" were the operator's pass-through wallets, and zero public victim reports over five months are jointly at least as consistent with a payment/settlement processor (legitimate, or a laundering front) as with phishing drains. See `COMPETING_EXPLANATIONS.md` §1.

**Preconditions.** Standing allowances; a facilitator role that batch-settles.

**Observable signals.** Self-settlement shape; allowance = MAX; post-pull balance zero — *base rate: any merchant-of-record facilitator produces exactly this; the discriminator is off-chain (victim reports, phishing infrastructure, merchant identity).*

**Evidence.** Corpus case files; on-chain persistence.

**Confidence.** High that the shape exists. Whether it is theft is *not established either way* from public data: the corpus's exposure-tracker evidence (approvals observed ~3 h before pulls; payers with no prior alert history) is real evidence for H1 that the audit cannot see, and the repeat-payer / round-amount / no-victim-report evidence is real evidence against it. The status is HYPOTHESIZED because the classification is open, not because the benign reading is favoured.

**Falsification criteria.** For "rogue": identification of the merchant/service the payers are paying and voluntary repeat payments (refutes); victim complaints, phishing kits tied to the address, one-shot sweeps of whole balances with no repeat (supports).

**Defensive implications.** Do not issue freeze requests on self-settlement shape alone; require an off-chain victim signal.

---

### M-18 — Convergent templates without coordination

**Maneuver.** Independent actors converge on the same operational template in the same window (six single-day self-deploying drainers on 2026-04-29; Renegade and Aurellion 48 h apart).

**Why HYPOTHESIZED.** The funder-layer anchor was retracted (CEXes don't share customers either). The remaining instances cannot distinguish independent convergence from one actor with several wallets without linkage evidence the corpus never obtained.

**Observable signals.** Overlap probes across funders, deployers, bytecode, timing — *base rate: absence of overlap is the default for unrelated actors, so "no overlap" is weak evidence of anything.*

**Falsification criteria.** Linkage evidence collapsing the cohort into one actor (refutes convergence); repeated template appearance across months with no shared tooling (supports).

---

### M-19 — Routing parasite (aggregator-pool backdoor)
Inherits Attack 1 unchanged. No public instance in 5 months. **Falsification:** none possible; **priority:** low until a pool with a caller-conditional side effect is found. Base-rate note: high router share is the normal profile of any pool that wins quotes.

### M-20 — Coordinated fleet proxy-upgrade swap
Inherits Attack 2 fleet mode. Single-contract mode is M-03. No public fleet instance. **Falsification:** n/a. **Signal:** simultaneous implementation-slot writes across proxies sharing a funder — base rate: legitimate multi-instance upgrades produce this; discriminate by implementation bytecode verification status.

### M-21 — Template / infrastructure skim (TaaS)
Inherits Attacks 3 and 8. The 435-deployer/2-funder family was never label-checked; both funders may be exchanges. **Required first step:** identity check on the funders before any skim analysis.

### M-22 — Time-lock synchronised fire
Inherits Attack 4. No instance. The 1,315 `TIMESTAMP`-gated count needs a benign base rate before it is a signal. **Falsification:** decoded thresholds clustering only around benign events (TGEs, vesting cliffs). **Priority:** demoted from "highest-leverage" (the class the corpus ranked lowest — verifier code bugs — produced ~$385M while this produced nothing).

### M-23 — Probe-trap discrimination against scanners
Inherits Attack 6. No instance. Note JaredFromSubway shows bots *are* targeted, via approvals rather than probe discrimination.

### M-24 — Advisor-parasite slow extraction
Inherits Attack 14 / Pattern F unchanged, still Tier C. The corpus's re-scan trigger (≥90 days) passed without a recorded result; V4 records that as an open obligation, not a finding.

### M-25 — Log-less extraction as anti-forensic design (downgraded)
Inherits Attack 7. Downgraded because empty logs are the default for native-ETH movement; the anti-forensic *intent* requires showing an ERC-20 was moved without emitting. **First step:** determine the asset. Until then this is an observation about `e37136db`, not a maneuver.

---

## THEORETICAL

### M-26 — Signal manipulation against behavioural detectors
An attacker who knows the detector's features (router share, revert rate, fanout, dormancy, mainnet age, vanity prefixes, OLI labels) manufactures them: routes traffic through routers to look organic, keeps revert rates low, splits funding across many funders, ages wallets deliberately, mimics institutional prefixes, or acquires a labelled wallet. The corpus's own Correction #20 shows the symmetric case (benign actors produce adversarial-looking topology); this is the deliberate inverse. **No instance; no way to distinguish from benign convergence without ground truth.** Defensive implication: never publish thresholds; treat every topology feature as manipulable; weight signals that cost the attacker capital (bond, TVL, time) over signals that cost nothing.

### M-27 — Adversarial verifier-set entry at scale
Extrapolates M-07 and M-05: buying seats (validator bonds, governance tokens, DVN operator status) is a priced path to attestation authority. THORChain's attacker paid ~635K RUNE; BonkDAO's ~$4M. The theoretical maneuver is the general case: for any reservoir R protected by a seat costing S with probability p of successful discharge, entry is rational when p·R > S + expected slashing. **No instance beyond the two observed specials; the generalisation is untested.** Defensive implication: price seats against reservoirs; add time (minimum validator age) and identifiable-abort cryptography so that seat-holding does not equal share extraction.
