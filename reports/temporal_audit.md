# Temporal Audit — Maneuvers V1–V3 and the Layer 3 Lexicon

**Audit date:** 2026-09-28. **Historical window:** 2026-04-07 (V1) → 2026-05-17 (lexicon). **Evidence window:** 2026-05-18 → 2026-09-28.
**Inputs:** `reports/claim_ledger.md` (claim-level status), `reports/evidence/onchain_checks_2026-09-28.md` (my own RPC reads), `reports/evidence/verification_april_wave_2026-09-28.md`, `reports/evidence/verification_may_wave_2026-09-28.md`, `reports/evidence/post_revision_survey_2026-09-28.md`.
**Labels** (used as defined in the audit brief, not casually): STILL SUPPORTED · PARTIALLY SUPPORTED · DISCONFIRMED · UNTESTABLE · OBSOLETE · OVERSTATED · UNDER-SPECIFIED.

A note on what "observed" can mean here. The corpus monitored Base, Arbitrum and Optimism for trap-adjacent bytecode. Every major incident it classifies (Drift, Rhea, Aethir, Hyperbridge, Kelp, Wasabi, Volo, Renegade, THORChain, Grok/Bankr, TrustedVolumes) happened outside that surface and entered the corpus from third-party reporting. When I write "supported by later evidence" I mean the *category* recurred in public incidents, not that Layer 3's detectors observed anything. Where the corpus's own detectors are the evidence (CE5E, Coffee Fleet, Pattern D scans), I say so.

---

## Part A — Status of every maneuver and framework concept

### A.1 The numbered attacks

| # | Maneuver | Status | Evidence for the classification | Confusions present in the original |
|---|---|---|---|---|
| 1 | Permission Harvesting + Routing Parasite | **UNTESTABLE / STILL HYPOTHETICAL** | No public instance of an aggregator-routed pool with a backdoor that calls a harvester's stored allowances, through 2026-09-28. The nearest public event is inverted: JaredFromSubway's bot was drained by approval-trap tokens (2026-06-20, $7.5M) — bait for bots, not for aggregator users. | Possibility ↔ probability (the chain is mechanically possible; no incentive analysis explains why no one has built it in 5 months). |
| 2 | Dormant Fleet + Proxy Upgrade Swap | **PARTIALLY SUPPORTED (single-contract mode) / STILL HYPOTHETICAL (fleet mode)** | Single-key admin → upgrade → drain recurred (Wasabi 04-30; Humanity 06-08 — all seven production keys on one laptop → ProxyAdmin → bridge upgrade, $32–36M; DxSale 05-28 — 2021 locker owner role → 7702 batch unlock). No coordinated dormant-fleet upgrade observed. | Theoretical attack surface ↔ demonstrated path: V2 "validated" the fleet attack by relaxing it to one contract. Capability ↔ intent: dormant proxies are assumed adversarial. |
| 3 | TaaS Template with Hidden Skim | **UNTESTABLE** | No public instance; the 435-deployer/2-funder family is corpus-internal and its funders were never label-checked. | Suspicious ↔ malicious (fanout asymmetry is also a CEX/launchpad signature — the corpus learned this on 05-09 for a different family and did not apply it here). |
| 4 | Time-Lock Synchronized Fire | **STILL HYPOTHETICAL; signal OVERSTATED** | No synchronized-fire incident. The 1,315 `TIMESTAMP`-gated count carries no information without a benign base rate. | Correlation ↔ causation; possibility ↔ probability. |
| 5 | Cross-Chain Rotation → Pattern D | **PARTIALLY SUPPORTED** | The 54/100 count is Tier A; the laundering interpretation has no control group. Drift's attacker staged on Solana; Kelp's on Ethereum via Tornado; Rhea's via `intents.near`; the Sandbox attacker EOA was dormant 313 days — cross-chain/aged staging is common, but so is multi-chain use by everyone. | Correlation ↔ causation (mainnet history is treated as a laundering signal without a base rate). |
| 6 | Probe-Trap Targeting Scanners | **UNTESTABLE / STILL HYPOTHETICAL** | No public instance of caller-discriminated probe responses. | Possibility ↔ probability. |
| 7 | Custom Selector Drain Avoiding Logs | **UNDER-SPECIFIED** | Empty-log success is the default for native-ETH movements; the "anti-forensic design" inference needs the asset type, which the corpus never states. | Observed behaviour ↔ inferred motive. |
| 8 | Infrastructure-Layer TaaS Skim | **STILL HYPOTHETICAL (correctly hedged)** | Unconfirmed in April, unconfirmed now. | None — this is the corpus at its most disciplined. |
| 9 | Cross-Chain DVN Verification Failure | **STILL SUPPORTED (class); PARTIALLY SUPPORTED (hooks)** | Kelp reproduced on-chain (`onchain_checks` §1–4). Class confirmed as a population risk: 47% of active OApps were 1-of-1 (Dune, 04-20); LayerZero moved defaults to 3-of-3 (07-09), its DVN refuses sole-attestor status, Config Checker rule `less-than-2-dvns` shipped; Kelp's channel now 4-of-4/64 confirmations. Post-Kelp instance: The Sandbox (08-21) — attacker used ERC-677 `approveAndCall` on the token (which *is* the OApp) to `setDelegate` and `setConfig(requiredDVNs=[attacker])`, then self-attested a forged inbound. The corpus's hook list ("alert on requiredDVNCount<2"; "DVN signing patterns change if key leaked") covers neither delegate-role capture nor RPC poisoning with intact keys (the actual Kelp mechanism per LayerZero, 05-18). | Technical exploitability ↔ economic viability handled well (>$10M TVL filter). Attack possibility ↔ attacker incentive: exposure was enormous (~1,250 OApps) and discharge happened once — the corpus never asked why. |
| 10 | Cross-Chain Proof Verification Bypass | **STILL SUPPORTED (class) — and larger than the corpus thought** | Hyperbridge verified. In the window this became the largest realised-loss class by count among bridges: Gravity Bridge (05-30, $5.4M, unvalidated denom mapping), Alephium (05-30), Syscoin (06-07, 5B SYS minted, $0 realised), Secret/Axelar (06-10, $4.67M, checks commented out), Aztec Connect (06-14, $2.1M, partial proof validation on a renounced-admin contract), Taiko (06-21, prover key in GitHub → forged proofs), Across-Solana (07-17, ~$4.5M, relayer event spoofing), Wanchain (07-20, ~$10M, non-injective signed-message encoding), Verus (05-17 and 07-22, $19.1M, same flaw twice), Liquid (09-06, ~$320M, range-proof verification cache collision), Nomic (09-09, $3.15M), Symbiosis (09-10). | The corpus treated this as the *audit-catchable* class and therefore commercially uninteresting ("this hook lives in the audit market"). By value it produced ~$385M in the window versus ~$0.7M for the configuration class it emphasised. Isolated behaviour ↔ pattern: one instance (Hyperbridge) was treated as the minor sibling. |
| 11a | Pooled Custody Adapter Compromise — key mode | **STILL SUPPORTED (class); anchor UNDER-SPECIFIED** | Wasabi, Volo, Humanity, Triple-A ($9.7–12M), SingularityNET (09-19, cloud → bridge keys), Taiko, Ostium (oracle *signer* key), Duelbits. Aethir — the named anchor — has no public root cause; the only write-up says access-control defect (`verification_april_wave` §3; `onchain_checks` §6). Bitget (09-24, $387.5M) adds a mode the corpus lacked: no key theft; internal credentials let the attacker forge withdrawal requests that the exchange's own signers signed. | Observed behaviour ↔ inferred motive (Aethir's "private key compromise" was inferred and then quoted as sourced). |
| 11b | Acquired-admin via code defect (unprotected initializer) | **STILL SUPPORTED** | Renegade (05-10) verified; Aurellion (05-12) was the same class two days later (uninitialized SafeOwnable facet, then `diamondCut`), which the corpus mis-filed as a distinct "diamond" sub-mechanism. | None material. Note the hook was added *after* Renegade. |
| 12 | Oracle Manipulation via Fake-Token Collateral | **STILL SUPPORTED (class); two sub-modes missing** | May: none (as V3 said). July–September: Bonzo (Supra oracle contract flaw, $9M), Lazy Summer (stale valuation of a frozen token, $6M — no wash trading), Ostium (signed price with no sanity bounds, $23.75M), Moonwell (MAMO pumped 43× on thin liquidity, $8.7M), Tectonic ($120M gross, TONIC pumped 195–300× + exchange-rate donation; $111M reversed by rollback), Nostra (NSTR wash-traded 20 min; aggregator selected a $99 pool over a $0.006 quote). Silo (04-03) was oracle *misconfiguration* and never belonged in this family. | Isolated ↔ pattern handled well. Missing: stale-price and signer-compromise modes; the "typically ~$1 stablecoin-class" seeding detail was Drift-specific overfitting. |
| 13 | Operational Layer Compromise at Governance Scale | **PARTIALLY SUPPORTED** | Drift verified (core). In the window the dominant governance mechanism was not signer phishing but *vote capture with no execution delay*: BonkDAO (07-06, $20M; 1% approval threshold, 2.9% turnout, no timelock), Term Finance (08-23, $8.5M, thin governance tokens), Neutron (09-22, $9.3M, proposal executed 11 `Update Admin` actions on passage; Cosmos Hub halted 24.5h), AFX Bridge (07-22, $24M, 5 of 7 validator keys). The corpus's hook "timelock removal" is the load-bearing element; "council-member wallet monitoring" was not the mode that recurred. | Confused two mechanisms under one heading (compromised signers vs. purchased votes). |
| 14 | Advisor-Parasite (Pattern F) | **UNTESTABLE / STILL HYPOTHETICAL (correctly Tier C)** | No public instance; the corpus's re-scan triggers (corpus age ≥90 days) have passed with no recorded result. | None — handled well. |
| 15 | Native-Swap Bridge Drain (candidate) | **DISCONFIRMED as enumerated; class UNDER-SPECIFIED** | THORChain's official post-mortems: a bonded validator exploited a GG20 threshold-signature zero-day (malformed Paillier modulus + 864 deliberate failed rounds) to reconstruct a vault key and sign outbounds directly. None of the four enumerated paths (attestation forgery / proof defect / validator key compromise / native-swap asymmetry) matches; the corpus had no category for adversarial *participation* in threshold cryptography. V3's hedge ("mechanism TBD") was right; the lexicon's bit-flip narrative two days later was wrong (`verification_may_wave` §6). | Historical coincidence ↔ causal evidence: a separately disclosed and patched bug (V12, 04-28; commit af46db22) was narrated as the exploit because it was the most recent public THORChain vulnerability. |

### A.2 Behavioral-laundering patterns and operator typologies

| Concept | Status | Basis |
|---|---|---|
| Pattern A / B / C | **STILL HYPOTHETICAL** (negative scans published) | Nothing in the window tests them. |
| Pattern D — Cross-Chain Reputation Import | **PARTIALLY SUPPORTED** (count) / **UNDER-SPECIFIED** (interpretation) | No control group; the report itself concedes no malice correlation. Aged/cross-chain staging by attackers is real (Sandbox EOA dormant 313 days; Nostra pre-positioned since March) but so is ordinary multi-chain use. |
| Pattern E — Fake Legitimate Projects | **UNTESTABLE** | Never scanned. |
| Pristine Solo Operator | **DISCONFIRMED as a behavioural detector** (self-corrected 05-09); survives only with an identity gate | 3 of 4 promotions were institutional deployers. |
| Infrastructure-Scale Operator | **DISCONFIRMED** (self-corrected 05-09) | ≥7 of 12 anchors were exchanges/bridges. |
| Single-Purpose Infrastructure Funder | **UNDER-SPECIFIED** | 84%-dormant mass same-bytecode deployment from fresh L2 wallets is also airdrop/points farming and wallet factories; competing explanations were never tested. |
| Self-Deploying Single-Contract Mass-Drain | **UNTESTABLE externally; internally inconsistent** | Iteration I's funder (1,296 downstream deployers, "Coinbase-origin") has the exact high-fanout signature Correction #20 said must be label-checked; it was attributed to org_001 anyway. The cadence prediction (fourth instance in 1–3 days) is unresolved in the repository. |
| Protocol-Family Specialist Operator | **PARTIALLY SUPPORTED** | TrustedVolumes same-operator claim rests on Blockaid's word; Verus (same flaw, 66 days apart) is recurrence, not specialism. The concept is plausible and cheap to test (cluster by operator EOA). |
| Adversarial Vanity Branding | **PARTIALLY SUPPORTED** | Operational branding (Coffee Fleet) and funder branding are corpus-internal. Anti-forensic spoofing of org_001 is more parsimoniously third-party poisoning (the corpus found the poisoners the next day). The fourth "victim-mimic" sub-category was built from one sub-$20K poisoning cluster. |
| Convergent Calibration | **PARTIALLY SUPPORTED** | Funder-layer anchor retracted (CEXes don't share customers either). Execution-layer instance (six single-day drainers) and scheduler-layer instance (48h cadence) are corpus-internal and plausible. The Renegade→Aurellion 48-hour gap is the best public analogue and is equally consistent with one scanning actor. |
| Victim-to-Predator Pipeline | **OVERSTATED** | Retired by the corrections log (49 → 2), retained in the lexicon. |
| Tuition Extraction Markets | **UNDER-SPECIFIED** | The anchor bot's 85% revert rate is ordinary for a losing backrun bot. |

### A.3 Core lexicon concepts

| Concept | Status | Why |
|---|---|---|
| Compositional Harm / Proofreading Trap | **PARTIALLY SUPPORTED (value) / OVERSTATED (count)** | Blockaid H1: 74% of stolen value from operational/infrastructure compromise; TRM: ~76% of funds from ~15% of incidents. But by count smart-contract exploits dominate (TRM 125/207), and the Q3 bridge wave (~$385M) was classic verification *code* bugs. "Proofreading has stopped mattering" is wrong; "proofreading is not where the value-weighted risk is" is right for H1 and wrong for Q3 bridges. |
| Stored Potential / Adversarial Topology | **PARTIALLY SUPPORTED as heuristic; discriminative power UNTESTED** | Fits many cases descriptively; counterexamples exist (Aztec: admin renounced; Coldcard: no on-chain node at all; Liquid). No discharge-rate-by-tier measurement was ever made. |
| Configuration-Level Vulnerability | **STILL SUPPORTED** | The ecosystem built exactly the monitor the corpus described; the population was 47% exposed; defaults changed. The corpus's originality is limited (Blockaid published the same check on 04-18) but its class-level generalisation was correct and early. |
| Verification-Path Trust Failure | **STILL SUPPORTED (descriptive)** | Ostium, Bonzo, Nostra, Across, Wanchain, Bitget all fit. Names the seam; does not predict which verifier fails. |
| Pooled Custody Amplification | **STILL SUPPORTED** | The notional-vs-realised gap in the window is the cleanest confirmation the corpus received: Sandbox $49B face / $675K realised (the realised part was the lock-release adapter); Symbiosis 46B syBTC / $336K; Liquid's federation paid out real BTC. |
| Operational Layer Attack | **STILL SUPPORTED** (anchor Aethir removed; Blockaid citation not found) | Value-share statistics; Humanity, Triple-A, Taiko, SingularityNET, Bitget, LayerZero RPC poisoning. |
| Strategy Lifecycle | **PARTIALLY SUPPORTED / timing DISCONFIRMED** | Replication happens; lags in the window were 2–95 days; the fake-collateral "copies within 30 days" forecast failed. |
| Neutrality Trap phase 4 / Normative Shell Game | **STILL SUPPORTED** | Chain-level halts and rollbacks became the dominant Q3 recovery mechanism (Cronos $111M rollback; Harmony; Cosmos Hub; Liquid; Taiko; Osmosis). |
| Confused Deputy / Distributed Chain / Agentic supercharger | **STILL SUPPORTED (mechanism); magnitude unproven** | Bankr ×3; Sandbox; Humanity; Neutron; x402 research; Blockaid H2 forecast. AI-agent losses in the window total ≈$1M. |
| Maneuver Primitives ("every exploit traverses six phases") | **NON-FALSIFIABLE / OVERSTATED** | Coldcard, Liquid, Aztec do not decompose without forcing. Fine as a checklist. |
| Hybrid Gameboard | **NON-FALSIFIABLE; anchors weakened** | Its THORChain and `0x80b12bd0` groundings are wrong or internally contradicted. |
| Static vs Dynamic Behavior | **DISCONFIRMED as stated** | Liquid ($320M, Bitcoin sidechain) and Coldcard ($116M) — the two largest non-CEX Q3 losses — were verification and key-generation failures on Bitcoin-family systems. |
| Thermodynamic Fundamentalism | **UNTESTABLE / OBSOLETE** | Anchors retracted; not a maneuver concept. |
| Kill-Switch Governance (V3 candidate) | **STILL SUPPORTED — elevated** | THORChain solvency halts; Cronos halt; Osmosis freeze; Cosmos Hub halt; Arbitrum freeze. The question the corpus posed ("what fraction of protocols have a parameter-level kill switch reachable in <1 hour") is now the right question. |
| Bug-Bounty Structural Gap | **STILL SUPPORTED** | Ostium's keeper path out of scope despite auditor warning; Cosmos Labs mis-triaged a valid report; THORChain retired its bounty; no scope change at Immunefi/Cantina. The Immunefi "April 18" citation is not found. |
| Epistemic Tier discipline | **PARTIALLY SUPPORTED** | Applied to numbers in reports; violated for narrative, citations, and the lexicon's empirical-grounding bullets. |

### A.4 Incident facts (summary; details in the ledger)

Exact: Kelp (transaction, config, funding), Rhea, Renegade, Grok/Bankr, TrustedVolumes amounts, Vercel chain, Bybit, Wasabi mechanism.
Wrong or unsupported: THORChain mechanism; the April-30 dormant-wallet drain (scale ×10, duration ×200, "Permit2" wrong); Drift recovery arithmetic ("Tether froze $127.5M"); Aethir root cause and quotations; Juicebox/Thetanuts labels; Wasabi "CREATE2"; Silo family; Blockaid January prediction; Immunefi April 18.

---

## Part B — Temporal validation: what happened after 2026-05-17 and whether the framework anticipated it

For each development: **(1)** anticipated? **(2)** how specifically? **(3)** predictive or broad? **(4)** what was missed? **(5)** which assumption fails? **(6)** attacker adaptation?

### B.1 LayerZero's response and the DVN-configuration population
LayerZero's May 18 incident report (RPC poisoning; app owner had downgraded 2-of-2 → 1-of-1), May 8 apology ("we made a mistake by allowing our DVN to act as a 1/1 DVN"), 3-of-3 minimum default on July 9, Config Checker, DVN refusing sole-attestor role; Dune: 47% of ~2,665 OApps 1-of-1 on April 20; Kelp's channel now 4-of-4 (`onchain_checks` §3); ~$15B of announced OFT→CCIP migrations; Kelp v. LayerZero filed 2026-09-25.
1–3. Anticipated specifically: the corpus's central hook is the check the ecosystem adopted, and "industry-wide exposure" was right. Blockaid published the same script the same day, so this is convergent rather than unique foresight. 4. Missed: the config *change* event (2-of-2 → 1-of-1) as a signal class ("config drift"), the RPC-layer compromise path, and delegate/role capture. 5. Assumption "if a DVN's key leaked, signing patterns change" fails — keys never leaked. 6. Sandbox is the adaptation: when thresholds are watched, capture the role that sets thresholds.

### B.2 THORChain post-mortems and TSS migration
Reports #1/#2; v3.19–v3.20; GG20 → DKLS/FROST; trading resumed June 23; $10M refund pool; bug bounty had been retired March 31.
1. Not anticipated. 2. The candidate's four paths all missed. 3. n/a. 4. Missed class: malicious participant inside a threshold-cryptography protocol (a *bonded* insider, paying ~635K RUNE for the seat). 5. Assumption "validator set agreed ⇒ trust failure is at the attestation layer" fails; the failure was inside key generation/signing. 6. Adaptation: THORChain is moving cryptographic libraries and adding keysign-failure jailing — the "864 deliberate failures" signal is exactly the kind of pre-trigger indicator the corpus's Maneuver Primitives claim to look for, and no one was looking.

### B.3 The Q3 bridge/sidechain verification wave (~$385M)
Gravity, Secret, Syscoin, Aztec, Taiko, Across, Wanchain, Verus ×2, Liquid, Nomic, Symbiosis.
1–3. Anticipated only in the broadest sense (Attack 10 exists). The corpus explicitly de-prioritised this class as audit-catchable. 4. Missed: that verification code bugs would out-produce configuration failures by two orders of magnitude in the window; that non-injective message encodings (Wanchain) and cache-key collisions (Liquid) are a distinct verification-bug family; that renounced-admin immutable contracts (Aztec) are a *worse* case for the stored-potential ontology because there is no admin node to score. 5. Assumption A11 (proofreading has stopped mattering) fails for bridges. 6. Adaptation: the same flaw exploited twice at Verus 66 days apart says defenders, not attackers, failed to adapt.

### B.4 Governance capture without timelocks
BonkDAO, Term Finance, Neutron (+ Cosmos Hub halt), AFX validator multisig.
1–3. Broadly anticipated (Attack 13; the "timelock removal" hook). The specific mode — buy or borrow a thin token, pass a proposal, execute immediately — was not described. 4. Missed: token-acquisition monitoring (BonkDAO's attacker bought ~1% of supply on exchanges days before). 5. Assumption that governance compromise runs through signers. 6. n/a.

### B.5 Signing-pipeline integrity (Bitget, $387.5M)
Internal credentials from a third-party product → forged withdrawal requests → the exchange's own signers signed; Hypernative alerts fired at the 18:31 test tx and the drain ran for ~1h.
1. Not anticipated as a mode; broadly covered by "Operational Layer Attack". 4. Missed: that the highest-value ops-layer failure would involve *no key compromise at all*. 5. Assumption "operational layer = key management" is too narrow; the layer includes request provenance.

### B.6 Weak key generation at scale (Coldcard $116M; SecondFi; Zilliqa; RRWallet)
1. Not anticipated; outside the ontology (no on-chain node, no permission, no composition). 4. Missed entirely. 5. Assumption A11 ("dynamic behaviour is where harm lives") fails. 6. ≥15 independent attackers exploited before disclosure — the "publishing-induced" direction runs the other way here (disclosure lagged exploitation).

### B.7 AI-agent incidents (Bankr May 19, Jul 25; x402 vulnerability censuses; Coinbase agentic wallets with enclave keys and policy)
1–3. Anticipated specifically by the Confused Deputy entry (added May). Losses remain small (~$1M). 6. Adaptation on the defender side: policy/enclave layers between the model and the key — exactly the "judgment layer" the corpus said was missing.

### B.8 Chain-level rollbacks and halts as recovery
Cronos rolled back 10,961 blocks (reversing $111M of Tectonic); Harmony rollback; Cosmos Hub 24.5h halt + 4-of-6 recovery multisig; Liquid pause and chain split; Taiko halt; Osmosis freeze.
1–3. Anticipated directionally by Neutrality Trap phase 4 / Normative Shell Game / Kill-Switch Governance. Broad, but the direction was stated before the pattern became dominant, and the corpus named the tension (surface neutrality vs. periphery authority) that each of these events re-opened. Predictive in direction, not in specifics.

### B.9 Approval-trap economics against bots (JaredFromSubway, $7.5M)
1–3. The corpus's founding premise — traps target bots, and bots keep falling in — received its largest public confirmation, via a mechanism (approval left unconsumed by a conditional `transferFrom` skip after ~24h of profitable bait) that is V1's "trust establishment then discharge" arc in miniature. Not specifically predicted; strongly consistent.

### B.10 Aave/lending policy response
Asset Safety Tier framework (wrap depth, bridge hops; wrsETH via LayerZero OFT ineligible), LTV cuts, listing-criteria overhaul.
1–3. Anticipated by "Pooled Custody Amplification" and the "new-collateral admission monitor" hook; the corpus said downstream protocols "trust that LayerZero attestation = legitimate backing" — Aave now scores bridge hops explicitly.

### B.11 Aggregate statistics
Blockaid H1: $1.1B/212 incidents, 74% of value operational; TRM H1: $972M/207, ~76% of funds from infrastructure compromise, 66% DPRK; TRM through early September: $1.73B/333; DPRK >$1B YTD (Elliptic). 1–3. The corpus's value-weighted thesis is supported; its unstated count-weighted version is not.

### B.12 What no later evidence tests
Patterns A/B/E/F; Attacks 1, 3, 4, 6, 7, 8; the camouflage equilibrium; recursive evasion; convergent calibration; all org_001 claims; the cadence forecasts (iter_9; fourth mass-drain instance). These remain exactly as uncertain as they were — the corpus's private data is the only place they could be resolved, and the repository records no resolution.

---

## Part C — Where the framework was right, wrong, and undecidable, and why

**Right, and for the right reasons.** (a) Configuration-level exposure as a monitorable class: right because the corpus did the on-chain replay rather than trusting reports, and the replay reproduces. (b) Pooled-custody amplification: right because it is a mechanical property of lock-release custody, and the window produced the notional/realised natural experiment that proves it. (c) Operational-layer dominance by value: right because Bybit and Drift already showed it; the corpus generalised correctly. (d) Kill-switch governance and the neutrality-trap override: right because the corpus reasoned from incentives (protocols will sacrifice neutrality when losses exceed tolerance), not from a particular incident. (e) Uninitialized-proxy enumeration: right within 48 hours, though added post hoc. (f) The corrections-log posture: the retractions it made were correct and important (CEX contamination; pass-through victims).

**Wrong, and why.** (a) THORChain: the corpus narrated the most recent public vulnerability as the exploit — coincidence treated as cause. (b) Aethir/Blockaid/Immunefi: citations that do not resolve — the failure mode is fluent attribution without a retrievable source. (c) The dormant-wallet drain: a native-ETH key-compromise sweep of hundreds of wallets over 13 hours was rendered as a Permit2 burst of 49 wallets in 3.5 minutes, then used as the anchor for two core concepts. (d) "V2 predicted the May wave": category drift and retro-fitted hooks were presented as prediction. (e) Static-vs-dynamic: the largest Q3 losses came from Bitcoin-family verification and key layers. (f) Topology-only inference (fanout, self-settlement, dormant mass deployment, prefix collision): each rests on an unmeasured base rate; the one that was measured (fanout) collapsed.

**Undecidable from here.** Everything that lives only in Layer 3's database (org_001, CE5E's true nature, the cadence forecasts, the camouflage ratio). The honest statement is that the repository contains the claims but not the means to test them, and that five months of silence on the cadence forecasts is itself information the corpus should have recorded.
