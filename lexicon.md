# Layer 3 Lexicon

**Version:** 2026-04-18 (living document; update when new framework-level observations emerge)
**Purpose:** Canonical definitional reference for Layer 3 methodology. Every entry specifies the term's definition, extended meaning, empirical grounding in the corpus where applicable, and cross-references. Intended for internal use and eventual external publication.
**Discipline:** Each entry is either (a) deductive from on-chain corpus evidence, (b) inferential with explicit methodology application, or (c) framework-level observation with clear analytical basis. No entry is asserted without basis.

---

## Index

### Core Architectural
- [Stored Potential](#stored-potential)
- [Adversarial Topology](#adversarial-topology)
- [Compositional Harm](#compositional-harm)
- [Trust Amplification Factor](#trust-amplification-factor)
- [Camouflage Ratio](#camouflage-ratio)

### Detection Methodology
- [Behavioral Laundering](#behavioral-laundering)
- [Pattern A — Reputation-Building Sacrifices](#pattern-a--reputation-building-sacrifices)
- [Pattern B — Temporal Pattern Normalization](#pattern-b--temporal-pattern-normalization)
- [Pattern C — Funding Chain Laundering](#pattern-c--funding-chain-laundering)
- [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import)
- [Pattern E — Fake Legitimate Projects](#pattern-e--fake-legitimate-projects)
- [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern)

### Structural and Psychological
- [Participatory Asymmetry / Predatory Literacy](#participatory-asymmetry--predatory-literacy)
- [Static vs Dynamic Behavior](#static-vs-dynamic-behavior)
- [Cost-Habituation Asymmetry](#cost-habituation-asymmetry)
- [Micro-Cost Habituation](#micro-cost-habituation)
- [Cognitive Load Concentration](#cognitive-load-concentration)

### Ecosystem-Level
- [The Proofreading Trap](#the-proofreading-trap)
- [The Self-Cannibalizing System](#the-self-cannibalizing-system)
- [Victim-to-Predator Pipeline](#victim-to-predator-pipeline)
- [Accountability-as-Load-Bearing](#accountability-as-load-bearing)
- [External Accountability Infrastructure](#external-accountability-infrastructure)

### Attack Pattern
- [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion)
- [Strategy Lifecycle](#strategy-lifecycle)
- [Operational Layer Attack](#operational-layer-attack)
- [Configuration-Level Vulnerability](#configuration-level-vulnerability)
- [Verification-Path Trust Failure](#verification-path-trust-failure)
- [Pooled Custody Amplification](#pooled-custody-amplification)

### Commercial / Positioning
- [The Detection Gap as Product](#the-detection-gap-as-product)
- [Observational Edge Non-Convertibility](#observational-edge-non-convertibility)
- [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset)
- [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap)
- [Epistemic Tier Classification](#epistemic-tier-classification)

---

## Core Architectural

### Stored Potential

**Definition.** A security primitive measuring accumulated permissions, dormant contracts, and capabilities not yet exercised. Unlike vulnerability assessment, which asks "is this broken," stored potential asks "what happens when this works perfectly."

**Extended description.** The central analytical object of Layer 3's methodology. A contract, account, or organizational structure is scored on capability, position, permissions, trust bindings, mutability, and observation capability. A contract with maximum capability, maximum permissions, zero extraction, and high volatility is at PEAK stored potential — not minimum risk. The absence of realized value is the danger signal.

**Empirical grounding.**
- Formal scoring model in `surveillance/risk_scoring.py`. Components: approval_scope (0-25), capabilities (0-25), deployer_risk (0-25), org_context (0-25). Volatility multiplier 1.0x – 3.0x. Tier cuts: CRITICAL ≥50, HIGH ≥20, MEDIUM ≥8, LOW ≥3.
- **EXTRACTION_008 (Kelp)** is the textbook case: pre-exploit the rsETH OFT adapter scored CRITICAL under this framework (maximum capability, maximum trust binding, zero extraction, zero constraint via 1-of-1 DVN). Verified via historical `EndpointV2.getConfig` replay — 1-of-1 DVN configuration stable for ≥56.7 days pre-exploit (`reports/kelp_retrospective_replay.md` Phase 3, Tier A).
- **EXTRACTION_005 (Drift)** validated the governance-layer version: 9/10 pre-hindsight tension score five days before the $285M drain (`reports/drift_prehindsight_simulation.md`).
- Deck: `l3-narrative/Stored_Potential_Risk_Model.pptx`.

**Cross-references.** [Adversarial Topology](#adversarial-topology) (the scoring primitives), [Compositional Harm](#compositional-harm) (what stored potential discharges into), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (one of the non-code failure modes scored).

---

### Adversarial Topology

**Definition.** The measurement of five primitives — **position, permissions, trust bindings, mutability, observation capability** — that determine whether a system component can be weaponized even when every component functions correctly.

**Extended description.** Applied to any node: smart contract, browser extension, AI agent, SaaS OAuth scope, multisig wallet. Each primitive is independently assessable; a node with privileged position, broad permissions, high mutability, strong trust binding, and observation capability is at maximum stored potential regardless of current behavior. The framework transfers off-chain — a MetaMask Snap, Zerion's DPRK-compromised wallet operation, and Aethir's OFT adapter all score similarly on these axes for structurally analogous reasons.

**Empirical grounding.**
- Formalized in `claude.md` §"The Adversarial Topology Framework" as the operational lens for all contract analysis.
- Applied to MetaMask Snaps as the canonical off-chain case (`l3-narrative/Standing_Next_To_The_Safe.pptx`): proves the framework catches non-blockchain stored potential.
- Every Extraction Event (001–008) can be scored against these primitives; Kelp and Drift are the strongest instances.

**Cross-references.** [Stored Potential](#stored-potential), [Pooled Custody Amplification](#pooled-custody-amplification) (position + permissions combination), [Operational Layer Attack](#operational-layer-attack) (when mutability and trust bindings fail).

---

### Compositional Harm

**Definition.** User harm that emerges from the interaction of correctly-functioning components. No single component contains a bug; the attack surface is composition-level.

**Extended description.** The central finding of Layer 3's work — most harm in the permissionless ecosystem is NOT caused by code defects. It is caused by the way correctly-executing components combine. Kelp's 1-of-1 DVN, LayerZero's endpoint contracts, Kelp's lock-and-release adapter, and Aave V3's collateral acceptance all functioned as specified. The $292M drain emerged from their composition. Traditional audits and bug bounties target component-level defects and therefore systematically miss this class.

**Empirical grounding.**
- Direct validation in **EXTRACTION_005 (Drift, $285M)**: every component executed correctly, per the public post-mortem — durable nonces valid indefinitely as designed, multisig accepted 2-of-5 signatures at the threshold set, vault executed authorized withdrawals, audits confirmed code sound.
- **EXTRACTION_008 (Kelp, $292M)**: same framing, different layer. DVN signed as it was supposed to; LayerZero endpoint delivered as specified; Kelp adapter accepted attestation as configured. Composition was the vulnerability.
- **Corrections #4 (velocity escalation mislabel)** and **#6 (risk_scores doc-reality gap)** are internal analogs — our OWN code had compositional failures where individual pieces worked but the combination silently drifted.
- Deck: `l3-narrative/Compositional_Zero_Days.pptx` catalogs 8 named compositional attack constructions.

**Cross-references.** [Configuration-Level Vulnerability](#configuration-level-vulnerability), [Verification-Path Trust Failure](#verification-path-trust-failure), [The Proofreading Trap](#the-proofreading-trap).

---

### Trust Amplification Factor

**Definition.** The multiplier by which identical behavior produces more victims when delivered through a trusted infrastructure position versus independent discovery.

**Extended description.** Measures the leverage an attacker gains by compromising or exploiting trusted infrastructure (router, aggregator, wallet UI, yield platform) rather than competing for attention independently. A trap delivered via Uniswap Universal Router gets orders of magnitude more traffic than the same trap deployed in the wild. The factor is computed from `surveillance/trust_amplification.py` as (observed caller volume) ÷ (baseline similar-contract caller volume).

**Empirical grounding.**
- **`0xd4624228` routing parasite**: 14.2x amplification, 2,910 victims, 98.7% router-delivered traffic (verified via `trust_amplification` table, deck `Layer3_Intelligence_Platform_1.pptx` slide 5, Cantina submission 2026-03-25). This is the canonical measured instance.
- Producer runs nightly per Correction #7 scheduler (03:00 UTC).
- API surface: served at `/api/v1/contract/{addr}` via the `computed_at` metadata block with freshness timestamp.

**Cross-references.** [The Detection Gap as Product](#the-detection-gap-as-product), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (the per-user analog of trust amplification), [Camouflage Ratio](#camouflage-ratio).

---

### Camouflage Ratio

**Definition.** The percentage of dangerous contracts that maintain low revert rates (under 10%) to evade standard detection. Stable at 70–79% across chains, organizations, and time.

**Extended description.** Interpreted as a Nash equilibrium — operators calibrate against detection tools at scale. Running too aggressive (high revert rate) loses victims to detection; running too conservative loses efficiency. The market converges on the temperature at which exploitation is optimally invisible. Stable across Base (~82%), Arbitrum (~70%), and Optimism, across two weeks of observation, and across four mapped organizations.

**Empirical grounding.**
- `camouflage_metrics` table populated nightly via `surveillance/camouflage_tracker.py`. Corpus-wide ratio stable at 79.2% across the initial 9-day run (2026-03-17 through 2026-03-25) before the producer cron died (fixed in Correction #7).
- Dataset: 5,845 camouflaged victims vs 233 overt-trap victims (25:1 ratio).
- Deck: `l3-narrative/Digital_Physics_Blockchain_Security.pptx` slide 7 frames this as a behavioral equilibrium, not a bug.

**Cross-references.** [Trust Amplification Factor](#trust-amplification-factor), [Behavioral Laundering](#behavioral-laundering), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (the feedback loop that produces the equilibrium).

---

## Detection Methodology

### Behavioral Laundering

**Definition.** The architectural analog of cash laundering. Predators manufacture legitimate-looking deployer histories, organizational infrastructure, or cross-chain reputations to defeat behavioral detection.

**Extended description.** Six documented patterns (A–F) represent distinct techniques operators use to evade behavioral-layer surveillance. This is the natural evolution of [Camouflage Ratio](#camouflage-ratio) — camouflage at the contract level is operators calibrating individual contracts; behavioral laundering is the same game at the deployer, organizational, and reputational level.

**Empirical grounding.**
- Framework scoped in `reports/behavioral_laundering_detection_scope.md`.
- Pattern D is the strongest validated (54% of 100 high-risk recent L2 deployers have Ethereum mainnet history we weren't linking — Tier A via Etherscan v2 multichain, `reports/cross_chain_import_candidates.md`).
- Pattern F scanned negative against the 30-day corpus but structurally scoped (`reports/advisor_parasite_candidates.md`).
- Other patterns (A, B, C, E) scoped and partially scanned; see individual pattern entries below.

**Cross-references.** All Pattern entries below. [Camouflage Ratio](#camouflage-ratio). [Strategy Lifecycle](#strategy-lifecycle) (how laundering patterns propagate).

---

### Pattern A — Reputation-Building Sacrifices

**Definition.** Deployer operates one or more legitimate-looking projects first (working contracts, real liquidity, real users, measurable activity), then launches a weaponized contract counting on prior reputation to discount risk scoring.

**Extended description.** Detection signal: deployer has a trajectory of early deployments with substantive activity and clean behavioral profile, followed by a single high-stakes deployment with different bytecode family and different behavioral signature. The delta between the trajectory's median risk score and the final deployment's score is the behavioral fingerprint.

**Empirical grounding.**
- Scanned 2026-04-18 (`scripts/pattern_a_scan.py`, report: `reports/reputation_sacrifice_candidates.md`).
- Result: **4 candidates out of 5,810 deployers** with ≥5 contracts. Narrow but clean.
- Canonical candidates: `0x614737b6…9271` (5 contracts, 23.8-day trajectory on Base), `0x5eb7a658…8ea3` (11 contracts, 21.5 days), `0x809088…23db` (11 contracts, 10.4 days, Arbitrum), `0x021868f2…0321` (18 contracts, 7 days).
- Re-scan trigger: corpus age ≥ 90 days. Too few candidates today to justify building `deployer_trajectory_analyzer` module; flagged for future build decision.

**Cross-references.** [Pattern E — Fake Legitimate Projects](#pattern-e--fake-legitimate-projects) (next-level variant where the operator uses separate wallets), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (reputation-trust at the victim-relationship level).

---

### Pattern B — Temporal Pattern Normalization

**Definition.** Operators deliberately deploying on a Western-workday schedule (9-to-5 Europe-business hours UTC) to defeat timezone-based anomaly detection, despite other-dimension suspicion.

**Extended description.** Detection requires a deployer to sustain the pattern for ≥ 14 days with ≥ 0.7 window concentration (per-hour activity concentrated in the claimed window). Baseline: known criminal orgs cluster in `night_shift` (Americas 3 AM / Asia morning) and `asia_morning`; legitimate dev populations cluster in `europe_business` and `americas_afternoon`. A deployer whose pattern looks like a Western employee while scoring suspicious on other dimensions is a Pattern B candidate.

**Empirical grounding.**
- Scanned 2026-04-18 (`scripts/pattern_b_scan.py`, report: `reports/temporal_normalization_candidates.md`).
- Result: **0 candidates**. Only 29 deployers total meet the sustained-schedule filter at 30-day corpus age. Baseline confirmed: `night_shift` over-indexes on traps (20% vs 0% for europe_business in the sustained-schedule cohort).
- Re-scan trigger: corpus age ≥ 60 days AND `weekend_activity_ratio` column added to `deployer_profiles`.

**Cross-references.** [Behavioral Laundering](#behavioral-laundering), `surveillance/deployer_profiler.py` (source of `timezone_guess`, `peak_hour`, `active_window_start`, `hour_concentration`).

---

### Pattern C — Funding Chain Laundering

**Definition.** Routing operational capital through CEX hot wallets so that `auto_funder_tracer` concludes "legitimate origin" despite pre-CEX trap-adjacent wallet activity.

**Extended description.** Detection discounts the risk score when funding traces to a legitimate CEX. Pattern C exploits this by making the CEX the most recent hop in a longer chain. The corrective move requires one-hop-back RPC trace: follow the deployer's CEX-withdrawal back to the user's prior deposit into that CEX hot wallet, and cross-reference the pre-CEX source against known criminal wallets.

**Empirical grounding.**
- Scanned 2026-04-18 SQL-only (`scripts/pattern_c_scan.py`, report: `reports/cex_laundered_funding.md`).
- Result: 10 CEX hot wallets in our `entity_classification`. 26 deployers funded from them. **0 strict candidates** (CEX-funded AND confirmed trap). **4 relaxed candidates** (CEX-funded AND suspected-heavy): `0x4885631c…0edd` (37 contracts, 13 suspected), `0x6dc136bc…af56` (19 contracts, all suspected), `0xb87e28fc…f828` (7 all suspected), `0x561d79e9…4d77` (3 all suspected).
- Re-scan trigger: one-hop-back RPC trace approval (~20 Alchemy calls for the 4 candidates).

**Cross-references.** [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import) (`0x4885631c…` flagged by both C and D). `surveillance/auto_funder_tracer.py` (the pipeline Pattern C exploits).

---

### Pattern D — Cross-Chain Reputation Import

**Definition.** Building legitimacy on one chain then appearing on target chains with pre-established trust that per-chain monitoring doesn't catch.

**Extended description.** A deployer appears on Arbitrum or Optimism for the first time with no prior activity in our corpus, but the SAME address has substantial history on Ethereum mainnet or Base. Per-chain profiling sees a fresh-to-L2 deployer; cross-chain view reveals a long-standing identity that may have pivoted from legitimate activity to trap deployment. Alternative: the operator uses address-reuse across chains specifically because single-chain monitoring misses the connection.

**Empirical grounding.**
- Scanned 2026-04-18 via Etherscan v2 multichain (`scripts/pattern_d_scan.py`, report: `reports/cross_chain_import_candidates.md`).
- **Result: 54 of 100 high-risk L2 deployers had mainnet first-tx predating L2 first-seen. The strongest-supported pattern of the six.**
- Longest gap: `0x7fd9a5104f…60d0` — Ethereum mainnet first-tx 2017-06-20, L2 first-seen 2026-04-02 = **3,208 days** (8.8 years). 14 suspected contracts on Base.
- Production-ready enrichment shipped: Correction-adjacent work added `deployers.mainnet_first_tx` column and one Etherscan v2 call per new deployer in `auto_funder_tracer` (2026-04-18, commit `9d1d337`). Backfill for existing 36k+ deployers running at time of writing.
- Also validated in **EXTRACTION_004 (Rhea)**: the Rhea Subject Wallet was funded via `intents.near` cross-chain bridge — the NEAR analog of Pattern D (cross-chain import *via bridge* rather than *via address-reuse*).

**Cross-references.** [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (orthogonal — victim-extraction cadence), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset) (Pattern D enrichment grows in value as more addresses accumulate history).

---

### Pattern E — Fake Legitimate Projects

**Definition.** Projects with real liquidity, real users, real trades but economics that don't support continued operation, functioning as reputation-building sacrifices.

**Extended description.** Harder to detect than A–D because the "legitimate phase" has no trap bytecode. Signature: a project winds down in a controlled way (not rug-pull) and its accumulated capital recycles into new deployer wallets that subsequently run trap operations. Detection is inherently graph-based (project controllers → intermediate wallets → new deployer → new contract), not per-contract.

**Empirical grounding.**
- Methodology proposed 2026-04-18 (`reports/fake_project_detection_methodology.md`). Three-phase approach: wound-down project detection → capital recycling tracer → destination deployer evaluation.
- Not scanned; blocked on corpus age ≥ 60 days AND approval for a forward-direction capital-flow tracer module.
- Estimated implementation cost: ~5 days focused work.

**Cross-references.** [Pattern A — Reputation-Building Sacrifices](#pattern-a--reputation-building-sacrifices) (same-deployer version; Pattern E uses multiple wallets).

---

### Pattern F — Advisor-Parasite Pattern

**Definition.** Trusted intermediary positions themselves as gateway to crypto and routes victim funds through self-controlled contracts at every step. Extracts via fees ("taxes"), compromised approvals, and routing tolls.

**Extended description.** Structurally similar to phishing drainers (hub-and-spoke approval pattern, many victims to one collector) but with a radically different **temporal signature** — months of small extractions, victims retain balance and keep interacting, no single-shot drain. Per-victim cadence 1–5 outbound transfers per month over extended duration. Phenomenologically distinct because the victim doesn't know they're being exploited; the advisor is consistently helpful. This is the relationship-of-trust variant of [Pattern A](#pattern-a--reputation-building-sacrifices).

**Empirical grounding.**
- Scanned 2026-04-18 (`scripts/advisor_parasite_scan.py`, report: `reports/advisor_parasite_candidates.md`; memorialized in `reports/behavioral_laundering_detection_scope.md`).
- Result: 16 candidates passed the structural filter (50+ unique approvers, ≥14-day duration, excluding known infrastructure and classified drainers). Every single one is either known DeFi infrastructure (1inch Router v6, LI.FI Diamond, Base Uniswap Router) or unidentified-but-non-advisor-shaped (per-user approval cadences too heavy or too light).
- **Zero confirmed advisor-parasites in current corpus.** Corpus age ≤ 30 days too short for months-long extraction pattern; `approval_events` doesn't index outbound Transfer flows (only approvals to flagged spenders).
- Confirmed counterexample: CE5E, E717, A7B9, E3B2 (`reports/case_CE5E_drainer_operation.md`). Each victim = one approval + one sweep. No retention, no relationship — classical phishing, not advisor-parasite. The handoff's framing that "some drainers might actually be advisor-parasites" is NOT supported by the drainers we've profiled.
- Re-scan triggers: (a) corpus age ≥ 90 days, (b) Transfer-event indexer deployed for ≥ 30 days, (c) `infrastructure_registry` grown to ~50 entries.

**Cross-references.** [Trust Amplification Factor](#trust-amplification-factor), [Cognitive Load Concentration](#cognitive-load-concentration), [Participatory Asymmetry](#participatory-asymmetry--predatory-literacy).

---

## Structural and Psychological

### Participatory Asymmetry / Predatory Literacy

**Definition.** The asymmetric relationship where threat actors and regular users share access to the same interfaces and information but differ radically in the ability to interpret adversarial patterns.

**Extended description.** Cannot be resolved through disclosure because the information is already public. Users and attackers both see Permit2 allowances as readable state; both see `EndpointV2.getConfig` returns; both see DVN addresses. The attacker reads "rsETH OFTAdapter has requiredDVNCount=1" as an exploitation opportunity; the user doesn't know how to form the query, let alone what it means. Resolution requires distributing *interpretive literacy* through specialized intermediaries — Layer 3, wallet providers with active screening, protocol foundations with architectural review capacity.

**Empirical grounding.**
- Kelp retrospective (`reports/kelp_retrospective_replay.md` Phase 3): the 1-of-1 DVN was publicly readable for ≥56.7 days. The information was not hidden — the literacy was. Every rsETH holder could theoretically have run `getConfig(configType=2)`; the asymmetry is that almost none of them know the call exists or what the output means.
- Compare to EXTRACTION_006 (Aethir): single-EOA adapter owner was on-chain-readable; the dev.to post-mortem states "The protocol had no multisig. They had no time wait mechanism. In 2026, this is not an acceptable level of operational security." The unacceptability was information-available; the enforcement was literacy-absent.

**Cross-references.** [Cognitive Load Concentration](#cognitive-load-concentration), [The Detection Gap as Product](#the-detection-gap-as-product) (the commercial resolution of participatory asymmetry).

---

### Static vs Dynamic Behavior

**Definition.** Bitcoin secured static behavior (ledger entries). Ethereum introduced dynamic behavior (state-modifying programs). The security layer appropriate for static systems does not transfer to dynamic ones.

**Extended description.** Bitcoin's threat model is "is this signature valid? is this input spent?" — questions about static records. Ethereum's threat model is everything Bitcoin's is PLUS "what does this program do when called?" — dynamic execution introduces behaviors that cannot be audited by snapshot examination. Every attack in Layer 3's corpus is a dynamic behavior failure. None would have been possible on Bitcoin's UTXO model because the attack mechanisms require state-modifying programs.

**Empirical grounding.**
- **EXTRACTION_001–008 inventory as dynamic-behavior failures.** Drift (governance state transition), Rhea (slippage aggregation logic), Aethir (admin ownership as mutable state), Hyperbridge (MMR proof validation), Kelp (DVN configuration state). None of these are failures of static ledger integrity.
- Deck: `l3-narrative/Digital_Physics_Blockchain_Security.pptx` frames this as the categorical distinction: physics vocabulary (stored potential, phase transition, entropy) describes dynamic behavior; traditional security vocabulary (vulnerability, patch) was built for static-adjacent defect models.

**Cross-references.** [Compositional Harm](#compositional-harm), [The Proofreading Trap](#the-proofreading-trap).

---

### Cost-Habituation Asymmetry

**Definition.** Traditional finance distributes cost across institutions, keeping per-action cost at zero for users. DeFi concentrates per-action cost in users, establishing a baseline of paying for actions that normalizes extraction.

**Extended description.** In traditional finance, a user swiping a credit card pays zero marginal cost per transaction; the cost is borne by the merchant's interchange fee and the bank's operational overhead. In DeFi, every transaction requires the user to pay gas — a small, visible, explicit cost. The baseline "crypto costs money per click" is established. Once paying per action is normal, marginal extraction by predators is psychologically invisible: a 0.1% "routing fee" surcharge looks identical to gas volatility, a "bridge fee," or a protocol tip. The red flag that would trigger skepticism in a cost-free environment (Why am I paying? What is this for?) never fires.

**Empirical grounding.**
- **Micropayment relay pattern** observed on `0x68a96f41ff1e9f2e7b591a931a4ad224e7c07863` (benign x402 relayer): median per-tx $0.001, max $0.013, ~14K tx/day. Proves users have fully habituated to micropayment-scale friction. The same habituation enables micro-cost extraction to be invisible.
- Deck: `l3-narrative/Anatomy_of_a_Liquidation.pptx` documents the $0.01 gas cost per drain — the economics work because attacker-per-tx-cost is dust.

**Cross-references.** [Micro-Cost Habituation](#micro-cost-habituation) (the Weber-Fechner formalization), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (operational exploitation of the habituation).

---

### Micro-Cost Habituation

**Definition.** Weber-Fechner application to DeFi cost perception: once baseline is "small cost per action," the just-noticeable-difference (JND) threshold shifts upward. Predators calibrate extraction to remain below the JND, producing psychologically invisible theft.

**Extended description.** Weber-Fechner law: perceived change in stimulus is logarithmic relative to baseline. A user habituated to ~$2 average gas per swap barely notices a $2.02 swap — the 1% increase is below JND. Extraction calibrated to stay inside JND is invisible on a per-event basis. Detection requires aggregation across time: individual events never cross the notice threshold, but cumulative extraction over weeks/months produces substantial loss the user only realizes in retrospect, if at all.

**Empirical grounding.**
- Behavioral framework applied to the `0xd4624228` trust-amplification parasite: each "swap" through the parasitic pool pulled a small fee the user didn't notice. Over 2,910 victims the aggregate reached ~100.56 WETH = $211K. No single victim recognized the loss as fraud.
- The CE5E drainer operation inverts this — fixed $10K/$20K chunks are ABOVE JND, which is why Pattern F (advisor-parasite) is a distinct commercial category from phishing drainers: advisors stay sub-JND per extraction, phishers take the whole balance in one visible event.

**Cross-references.** [Cost-Habituation Asymmetry](#cost-habituation-asymmetry), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern).

---

### Cognitive Load Concentration

**Definition.** Traditional finance distributes security cognitive load across institutions (banks, regulators, insurance, merchants). DeFi concentrates it in individual users.

**Extended description.** A credit card user can ignore fraud prevention entirely — the bank runs detection, the regulator mandates loss caps, the merchant absorbs chargebacks. A DeFi user must personally evaluate every approval, every protocol, every bridge, every proxy upgrade, every multisig composition, every DVN configuration. Most humans cannot sustainably maintain the vigilance DeFi requires. The result is a specialization gap that an intermediate layer (wallet providers, protocol foundations, intelligence platforms like Layer 3) is structurally required to fill. Without that layer, users are load-bearing in a way they are not built for.

**Empirical grounding.**
- Documented at the victim level: 0x785ce546 (case study in `l3-narrative/Anatomy_of_a_Liquidation.pptx`) lost $72K across 2 chains to 2 unrelated attackers and a third still-armed approval. The victim's cognitive overhead to "just revoke the approvals" includes: knowing Permit2 exists, knowing how to read `allowance()`, knowing how to submit a revoke transaction, paying the gas for it. That burden is untenable at scale.
- Extends to MetaMask Snaps case (`l3-narrative/Standing_Next_To_The_Safe.pptx`): users install with one decision and inherit surveillance capability they never reviewed after that one click.

**Cross-references.** [Participatory Asymmetry](#participatory-asymmetry--predatory-literacy), [External Accountability Infrastructure](#external-accountability-infrastructure).

---

## Ecosystem-Level

### The Proofreading Trap

**Definition.** The security industry's current response optimized for a threat model (code bugs) that has stopped being the dominant threat. More careful reading of the same book doesn't fix the architectural, configuration, and compositional properties the book teaches developers to use.

**Extended description.** Code auditing finds bugs. The April-2026 exploit cluster (Aethir / Hyperbridge / Kelp) contains one code bug and two non-code failures. Bug-bounty programs, audit-marketplace platforms, static-analysis tools, and formal verification frameworks all target the proofreading surface. Layer 3's positioning is explicit: not better auditing, but a different category that measures the properties the code uses, not the code itself.

**Empirical grounding.**
- **Cluster validation in EXTRACTION_006 / 007 / 008**: three attacks, three different failure layers (operational / code / configuration), same 9-day window, same structural target (pooled-custody cross-chain adapters). Traditional audits catch at most 1 of 3 (Hyperbridge's MMR bug). Stored-potential framework catches all three because it measures capability-vs-constraint directly.
- Cantina bug-bounty submission rejection (2026-03-25, around `0xd4624228` trust amplification): rejected explicitly on grounds that "the code did what it was supposed to do." That IS the proofreading trap — the bug bounty surface is the wrong question, and the rejection confirms it.

**Cross-references.** [Compositional Harm](#compositional-harm), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap).

---

### The Self-Cannibalizing System

**Definition.** DeFi requires trust to function and new users to grow, but its architecture is hostile to both. New users are structurally positioned as food for predators.

**Extended description.** The ecosystem educates through harm rather than instruction. Users learn Permit2 by being drained. They learn about oracle manipulation by holding a token that got price-manipulated. Selection pressure filters out the unsophisticated (they lose money, leave, or get absorbed into predator ranks) while teaching the survivors to either defend or predate. The system cannot grow its user base in a healthy way; it can only churn through cohorts.

**Empirical grounding.**
- 13,954 undrained approvals in our corpus (`l3-narrative/Access_Topology_Intelligence.pptx` slide 7). Each one is a user who granted permission and hasn't (yet) been drained — stored potential at the user-population level.
- 67 unique victims of CE5E in 6.8 days (`reports/case_CE5E_drainer_operation.md`). 0 of 11 today-victims had prior alert history. The victim population is being freshly generated continuously.

**Cross-references.** [Victim-to-Predator Pipeline](#victim-to-predator-pipeline), [Accountability-as-Load-Bearing](#accountability-as-load-bearing).

---

### Victim-to-Predator Pipeline

**Definition.** Documented empirical pattern where victims of on-chain exploitation sometimes become operators of similar attacks.

**Extended description.** Education-by-exploitation mechanism producing both sophisticated users and new predators from the same cohort. A user who gets caught by a trap contract, observes the mechanism, reverse-engineers it, and reproduces it is indistinguishable from any other new deployer in the trap population. The ecosystem's pedagogical vector runs through adversarial exposure.

**Empirical grounding.**
- `0xcfd2cbdd` hit 9 different traps, suffered 2,279 reverts, then deployed 14 callback traps (deck `What_The_Chain_Reveals.pptx`).
- `0x3f4739d` had 5,029 reverts, then deployed 39 contracts.
- 25 bot candidates in our `bot_candidates` table also appear as deployers. The overlap is the pipeline.

**Cross-references.** [The Self-Cannibalizing System](#the-self-cannibalizing-system), [Strategy Lifecycle](#strategy-lifecycle).

---

### Accountability-as-Load-Bearing

**Definition.** Accountability is an independent variable from surveillance and authority. Systems can have accountability without surveillance (natural consequences, reputation) or surveillance without accountability (observation without response).

**Extended description.** Without accountability, systems reduce to pure power dynamics where predators operate with structural impunity. Traditional finance has institutional accountability (regulators, deposit insurance, chargeback rights) that operates independently of whether any particular transaction is surveilled. DeFi architecturally rejected institutional accountability on ideological grounds and has not replaced it with any functional substitute. The result is that Layer 3's observational edge exists because no enforcement layer does; we can watch everything and affect nothing.

**Empirical grounding.**
- `reports/case_CE5E_drainer_operation.md` documents this directly: we can attest to the drains with Tier A confidence (68 events, $929K), can identify freeze targets with Tier A precision, and have no authority to freeze anything. The only accountability mechanisms available are Circle/Tether issuer intervention or protocol-level social coordination.
- Kelp retrospective (`reports/kelp_retrospective_replay.md` Phase 8): quote-safe claim explicitly rules out prevention — "Layer 3 has no enforcement layer." Flagging ≠ prevention.

**Cross-references.** [External Accountability Infrastructure](#external-accountability-infrastructure), [Observational Edge Non-Convertibility](#observational-edge-non-convertibility).

---

### External Accountability Infrastructure

**Definition.** The infrastructure required to restore accountability in permissionless systems that architecturally rejected it.

**Extended description.** Includes Layer 3's observational capability (what's happening), stablecoin issuer intervention (Tether, Circle — selective freeze authority), foundation-level recovery (Solana Foundation's $20M contribution to Drift recovery), compliance relationships at centralized on-ramps (CEX freezes, KYC-linked cashout), and protocol-level social coordination (Aave bad-debt resolution, Kelp coordination). None of these are on-chain primitives; they are off-chain coordination layers that the ecosystem has re-imported despite its architectural rejection of institutional authority.

**Empirical grounding.**
- **EXTRACTION_005 Drift recovery breakdown**: Tether $127.5M + Solana Foundation $20M + $100M revenue credit facility = $247.5M recovered vs $285M loss (~87% coverage). Every recovery dollar came through external accountability infrastructure; zero from on-chain-native mechanisms.
- **EXTRACTION_004 Rhea recovery**: Tether freeze $4.34M + voluntary USDC return $3.36M + voluntary NEAR return $1.56M = $8.26M vs $18.4M loss (~45% coverage). Same pattern — recovery flows through centralized issuer and protocol treasury discretion.
- **EXTRACTION_008 Kelp recovery status**: pending at documentation date. rsETH is an LRT, not a stablecoin — no Circle/Tether pathway. Recovery requires protocol-native action.

**Cross-references.** [Accountability-as-Load-Bearing](#accountability-as-load-bearing), [Cognitive Load Concentration](#cognitive-load-concentration).

---

## Attack Pattern

### Publishing-Induced Recursive Evasion

**Definition.** Publishing detection methodology enables sophisticated operators to calibrate against it. Creates an adversarial co-evolution cycle where any widely-adopted standard becomes the next attack surface.

**Extended description.** The central commercial-strategic tension in detection work. Open publication grows the defender community but also gives attackers the baseline they need to optimize against. Layer 3's methodology (stored potential scoring, DVN configuration monitoring, cross-chain mainnet-import enrichment) will, once widely adopted, become the specification against which operators calibrate their next generation of laundering. This is not a reason to keep methodology secret — the edge decays either way — but it shapes what the sustainable edge actually is: corpus depth, not methodological novelty.

**Empirical grounding.**
- [Camouflage Ratio](#camouflage-ratio) at 70–79% is the standing example. Operators have already calibrated to whatever revert-rate threshold the current detection tools use.
- GoPlus-family benchmarks (`l3-narrative/Stored_Potential_Risk_Model.pptx` slide 6): 10/10 CRITICAL contracts in Layer 3 returned NO DATA from GoPlus. The GoPlus threshold is the attacker's calibration target.

**Cross-references.** [The Detection Gap as Product](#the-detection-gap-as-product), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset), [Strategy Lifecycle](#strategy-lifecycle).

---

### Strategy Lifecycle

**Definition.** Observed progression of attack techniques through phases: EARLY (demonstrated once), ARMS_RACE (multiple independent operators attempting), WEAPONIZED (saturation beyond defensive capacity), SATURATED (net-negative returns due to defensive adaptation).

**Extended description.** Empirical framework for timing attack-family propagation. A novel technique demonstrated publicly (Drift's durable-nonce governance takeover, Hyperbridge's MMR bypass) enters EARLY. Within weeks, independent operators replicate the pattern with variations, entering ARMS_RACE. The window between EARLY and ARMS_RACE is the commercial-intelligence opportunity — warnings delivered during EARLY can still change customer behavior before ARMS_RACE saturation.

**Empirical grounding.**
- **Oracle-manipulation-lending family**: Drift (2026-04-01) → Rhea (2026-04-16) = **15 days** EARLY → ARMS_RACE transition. Documented in `reports/extraction_event_004_rhea_finance.md` cross-chain correlation section.
- **Cross-chain infrastructure family**: Aethir (2026-04-09, operational) → Hyperbridge (2026-04-13, code) → Kelp (2026-04-18, configuration) = **9 days** for three orthogonal variants. Faster than oracle-manipulation — multiple attack teams operating in parallel, not sequential.

**Cross-references.** [Compositional Harm](#compositional-harm), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion).

---

### Operational Layer Attack

**Definition.** Attack category where code functions correctly but surrounding operational infrastructure (UIs, deployment pipelines, key management, governance workflows) is compromised.

**Extended description.** Blockaid's January 2026 prediction — that 2026 attacks would "target operational layers around key management, not the keys themselves" — empirically validated across Q2. Common pattern: the operator with authority gets socially engineered, phished, or has keys exfiltrated via malware; the on-chain signatures produced post-compromise are cryptographically valid; the code enforces what the signatures authorize. There is no code defect to catch; the attack is upstream of code.

**Empirical grounding.**
- **EXTRACTION_006 (Aethir, 2026-04-09)**: EOA admin key compromise; no multisig; no timelock. Per dev.to writeup: "The legitimate owner was just an eoa, leading to the conclusion for now that it's a private key compromise attack."
- **EXTRACTION_005 (Drift, 2026-04-01)**: durable-nonce signatures were pre-acquired via social engineering of Security Council members; when governance threshold dropped from 3/5 to 2/5, the attacker already held quorum.
- Bybit ($1.5B, 2025) referenced in the decks as the canonical large-scale operational-layer attack.
- Zerion DPRK social engineering (2026-04-10, ~$100K) as the smaller-scale current instance.

**Cross-references.** [Verification-Path Trust Failure](#verification-path-trust-failure), [Configuration-Level Vulnerability](#configuration-level-vulnerability).

---

### Configuration-Level Vulnerability

**Definition.** Attack surface that exists in deliberate protocol configuration choices rather than code defects. Publicly observable via standard contract calls (e.g., `getConfig(configType=2)`). Out of scope for bug bounties because no code is vulnerable.

**Extended description.** The canonical case: Kelp's 1-of-1 DVN configuration on both source (Unichain) and destination (Ethereum) chains. LayerZero's documented best practice is ≥2 required DVNs + optional threshold ≥1; Kelp chose 1-of-1. The choice was on-chain-readable via `EndpointV2.getConfig`, unchanged for ≥56.7 days pre-exploit. No code fix could have prevented the attack — the attack path IS the correctly-executing code doing what the configuration authorized. The only remediation is configuration change.

**Empirical grounding.**
- **EXTRACTION_008 (Kelp)**: Configuration verified via historical `getConfig` at blocks 24,500,000–24,900,000 (Phase 3 of `reports/kelp_retrospective_replay.md`). Tier A deductive lead time ≥56.7 days.
- **EXTRACTION_005 (Drift)**: governance-layer configuration variant — threshold reduction + timelock removal on 2026-03-27 was the phase transition that opened the attack window.

**Cross-references.** [Verification-Path Trust Failure](#verification-path-trust-failure), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap).

---

### Verification-Path Trust Failure

**Definition.** Compositional harm arising when a trusted verification layer (oracle, DVN, multisig) fails while all other components operate correctly. The layer's attestation becomes the attack vector because downstream components are designed to trust it unconditionally.

**Extended description.** The defining property: components downstream of the verifier have no mechanism to question the attestation. A lending protocol with oracle dependency trusts the oracle's price; if the oracle reports a manipulated price (because its own source was compromised), the lending protocol authorizes undercollateralized borrowing without any defect. A cross-chain adapter with DVN dependency trusts the DVN's signature; if the DVN signs a forged message, the adapter mints without defect.

**Empirical grounding.**
- **EXTRACTION_005 (Drift)**: fake CVT token wash-traded to ~$1 on Raydium → Drift's oracles reported $1 → Drift accepted CVT as collateral worth hundreds of millions.
- **EXTRACTION_004 (Rhea)**: fake tokens lacking NEP-141 metadata deployed on implicit accounts → Ref Finance pool IDs 8528-8538 paired them with USDC → Rhea's margin-trading oracle accepted the manipulated prices.
- **EXTRACTION_008 (Kelp)**: 1-of-1 DVN signed forged cross-chain message → LayerZero endpoint accepted attestation → Kelp adapter minted on Ethereum.

**Cross-references.** [Compositional Harm](#compositional-harm), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [Pooled Custody Amplification](#pooled-custody-amplification).

---

### Pooled Custody Amplification

**Definition.** Lock-and-release adapter architecture (as distinct from mint-burn) where the attack target is shared user deposits rather than newly minted tokens. Amplifies harm because exploitation draws from real user capital rather than creating inflationary tokens.

**Extended description.** In a mint-burn bridge architecture, an attacker who forges a cross-chain message mints tokens on the destination chain; the resulting tokens are inflationary and their market value collapses as the fraud is realized. In a lock-and-release architecture, the attacker unlocks REAL deposits held in the adapter — the stolen tokens are indistinguishable from legitimate user holdings, retain their market value until issuer intervention, and produce direct loss to the users whose deposits were unlocked. Pooled custody is therefore the highest-stored-potential cross-chain architecture.

**Empirical grounding.**
- **EXTRACTION_008 (Kelp)**: the rsETH OFT adapter holds pooled user deposits; the attacker's 116,500 rsETH came from the pool, not inflation. That's why Aave V3 accepted the stolen rsETH as collateral — it is indistinguishable from legitimate rsETH.
- **EXTRACTION_006 (Aethir)**: OFT adapter pattern, same class. Once admin, drained bridged assets directly from the pool.
- Contrast: a theoretical mint-burn exploit of the same adapter would not have been accepted by Aave because the newly-minted rsETH would have no backing — though in practice neither architecture is hardened against cross-chain verification failure.

**Cross-references.** [Verification-Path Trust Failure](#verification-path-trust-failure), [Compositional Harm](#compositional-harm), [Configuration-Level Vulnerability](#configuration-level-vulnerability).

---

## Commercial / Positioning

### The Detection Gap as Product

**Definition.** The 100% gap between what free benchmarks like GoPlus detect and what sophisticated operators actually deploy. Free security data functions as an attack vector because operators calibrate against it, and "clean" results become trust amplification signals for predators.

**Extended description.** A user who checks a contract on a free scanner and sees "clean" interprets the clean result as a positive safety signal. Sophisticated operators are AWARE of this behavior and optimize bytecode to produce clean results on free scanners specifically. The user's trust in the signal is inverted by the operator's awareness of the signal. Layer 3's commercial positioning is in this gap: the 70-79% camouflage ratio IS the product — the fraction of trap contracts that defeat free tools is the fraction where paid intelligence is load-bearing.

**Empirical grounding.**
- 10/10 Layer 3 CRITICAL contracts returned NO DATA from GoPlus (`l3-narrative/Stored_Potential_Risk_Model.pptx` slide 6).
- Camouflage ratio stable 70-79% across chains (discussed under [Camouflage Ratio](#camouflage-ratio)).

**Cross-references.** [Camouflage Ratio](#camouflage-ratio), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap).

---

### Observational Edge Non-Convertibility

**Definition.** Edges that exist only while observed. Participation collapses the observation. Some edges cannot be converted from observational to operational advantage without destroying the edge itself.

**Extended description.** The NTSB investigates airline safety and does not start airlines. Investigative journalists cover industries they do not operate in. Layer 3's edge is observational — we see patterns because we are not participating. If Layer 3 started running an arbitrage bot, deploying trap contracts, or operating infrastructure, the very operators we observe would stop behaving the same way near us. The edge is a function of our position as observer-only. This is a commercial constraint, not a personal ethics choice: the monetization must come from the observation, not from participation in the observed phenomenon.

**Empirical grounding.**
- Structural principle applied in `claude.md` §"What NOT to Build": "No trading logic, execution, or flash loans. No contract deployment. No interaction with flagged contracts — read-only always."
- Deck: `l3-narrative/Deductive_Intelligence.pptx` frames deductive observation of deterministic systems as the edge class.

**Cross-references.** [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset), [Accountability-as-Load-Bearing](#accountability-as-load-bearing).

---

### Intelligence-as-Compounding-Asset

**Definition.** Intelligence operations where marginal cost decreases and marginal value increases over time, contrasted with operational activities (trading, arbitrage) where edges decay with each use.

**Extended description.** Layer 3's corpus grows monotonically — every new contract indexed, every new deployer profiled, every new drain captured adds to the base. The marginal cost of adding the Nth observation is lower than the (N-1)th because infrastructure is already built. The marginal value is higher because the new observation contextualizes all prior ones (a new ARMS_RACE instance validates the EARLY demonstration retroactively). A trading edge is the opposite: each use either moves the market against the trader or attracts competition, driving marginal return toward zero.

**Empirical grounding.**
- Corpus growth: 0 contracts on 2026-03-17 → 90,276 by mid-April per `claude.md` headline metric. Growth rate ~7,000 contracts/day. No decay.
- Correction-log discipline: every revision adds trust infrastructure (`reports/correction_log.md` entries #3–8). Errors compound into credibility through published correction, not against it.

**Cross-references.** [Observational Edge Non-Convertibility](#observational-edge-non-convertibility), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (the one compounding mechanism that does have a counter-pressure).

---

### The Bug-Bounty Structural Gap

**Definition.** Bug bounty economics cannot price compositional harm because bounties pay for code-level vulnerabilities in specific in-scope contracts. Phishing-adjacent findings, configuration-level risks, and architectural stored potential are systematically out of scope across all bounty platforms.

**Extended description.** Bounty programs assume the threat model is "code does something it shouldn't." Compositional harm is "code does exactly what it's supposed to, and the result is catastrophic." There is no protocol to submit a report to; the finding belongs to the architecture, not to any one contract. Confirmed by Immunefi community response on April 18, 2026 and by the Cantina submission rejection on 2026-03-25 for `0xd4624228` trust amplification ("the code did what it was supposed to do"). This is not a flaw in bounty programs — it's a structural property of what bounties price for. Layer 3's commercial surface occupies the gap.

**Empirical grounding.**
- **Cantina rejection 2026-03-25** explicit quote: "the code did what it was supposed to do" — for a finding that produced 14.2× trust amplification and 2,910 victims. The finding was real; the bounty surface does not price it.
- **EXTRACTION_008 (Kelp) Configuration-Level**: Kelp's rsETH pools were not in any bounty's in-scope list for "1-of-1 DVN configuration" because no bounty program scopes configuration choices. The $292M loss is uncapturable by current bounty economics.
- Cluster analysis in `reports/extraction_event_008_kelp.md`: traditional audits (the proofreading surface bounties pay into) catch at most 1 of 3 April-2026 cross-chain cluster events (only Hyperbridge's MMR code bug is audit-catchable).

**Cross-references.** [The Proofreading Trap](#the-proofreading-trap), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [The Detection Gap as Product](#the-detection-gap-as-product).

---

### Epistemic Tier Classification

**Definition.** All findings categorized as **Tier A** (deductive, verifiable from on-chain data), **Tier B** (inferential, methodology-applied), or **Tier C** (speculative). Discipline prevents overclaiming and enables defensible commercial communication.

**Extended description.** Every alert, report, and customer-facing claim carries an explicit tier tag. A Tier A claim has a specific on-chain read that any third party can replicate (e.g., "`getConfig(configType=2)` at block 24,500,000 returned requiredDVNCount=1"). A Tier B claim is inferential reasoning across published methodology (e.g., "the 1-of-1 DVN configuration produces CRITICAL stored potential per our risk framework"). A Tier C claim is explicit speculation about future behavior or unobservable causation (e.g., "the attacker will replicate within 15 days per the Strategy Lifecycle model"). Discipline: Tier A is for pitches, Tier B is for methodology explanations, Tier C is never cited in commercial materials without explicit framing as prediction.

**Empirical grounding.**
- Applied throughout every report in `reports/`. Kelp retrospective (`reports/kelp_retrospective_replay.md` Phase 8) enumerates quote-safe Tier A claims and explicitly rejects overclaim candidates ("Layer 3 would have prevented Kelp" — rejected because we have no enforcement layer).
- Correction-log entries #3–8 all carry explicit Tier A / Tier B separation within each correction's structure.
- API envelope (`web/api_v1.py::_ok`) carries the `epistemic_tag` convention as a JSON field in alert payloads, per Correction #6 resolution.

**Cross-references.** [Accountability-as-Load-Bearing](#accountability-as-load-bearing) (epistemic discipline IS the self-imposed accountability layer Layer 3 runs), [The Proofreading Trap](#the-proofreading-trap) (the tier discipline is what prevents us from falling into the trap of claiming we catch what we don't).

---

## Living document conventions

- **Adding entries.** When a new framework-level observation emerges from a session, append it to the appropriate category with the same format (definition, extended description, empirical grounding, cross-references). Update the index.
- **Revising entries.** When evidence refines an existing entry, update the entry and append a note to `reports/correction_log.md` if the revision changes a previously-published claim.
- **Cross-referencing.** Internal references use `[#anchor]` markdown format. External references to reports use file paths (`reports/*.md`, `l3-narrative/*.pptx`).
- **Defensibility check before external publication.** Every entry in Core Architectural, Attack Pattern, and Commercial/Positioning categories should survive expert review. If a Tier A claim in an entry cannot be reproduced by a reader with corpus access, the entry needs revision before external use.

**Next entries anticipated (not yet added, placeholders):**
- The LayerZero DVN configuration-enumeration module, once built (cross-refs Pattern D, Configuration-Level Vulnerability, External Accountability Infrastructure).
- Bridged-asset conservation check methodology, once scoped (cross-refs Compositional Harm, EXTRACTION_007).
- Any framework concept that emerges from re-scans of Patterns A, B, E, F after corpus age ≥ 90 days.
