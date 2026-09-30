# Phase 1 — Faithful Reconstruction of the Historical Work

**Scope of this document.** What the previous AI-assisted analysis was trying to do, reconstructed from the repository as it stood at commit `11593d1` (2026-05-17). No improvement, no hindsight. Where I quote the corpus I quote it verbatim; where I paraphrase I say so. Citations point at file and section. The identity of the model that co-authored the corpus was not used anywhere in this reconstruction.

**Corpus inventory (what "the historical work" is).**

| File | Dated | Role |
|---|---|---|
| `POTENTIAL_ATTACKS_V1_ARCHIVE.md` | 2026-04-07 | Eight hypothetical attack chains assembled from corpus primitives; "written so a defender can pre-build detectors before the combination lands in the wild" |
| `POTENTIAL_ATTACKS_V2.md` (= `_V2_ARCHIVE.md`, byte-identical) | 2026-04-20 | Re-issue after the "April 2026 wave"; adds Attacks 9–14 derived from incidents; adds a "Validated in April 2026" table and Epistemic Tier tags |
| `POTENTIAL_ATTACKS_V3.md` | 2026-05-15 | Adds the late-April/May incidents; splits Attack 11 into 11a/11b; parks Attack 15 as a candidate pending THORChain forensics |
| `lexicon.md` (root, version 2026-05-15) and `docs/lexicon.md` (canonical, 2026-05-17) | | Definitional reference: 46 entries across Core Architectural, Detection Methodology, Structural/Psychological, Ecosystem-Level, Attack Pattern, Operational Doctrine, Commercial. The 05-17 copy adds one entry (The Hybrid Gameboard); otherwise identical |
| `CORRECTIONS.md` | 2026-03-31 → 2026-04-16 | Claim-retraction log with a "Quick Retirement Index" and propagation watch-list |
| `reports/*.md` (8 files) | 2026-04-18 (7 files) and undated | Case/extraction-event write-ups (Rhea, Aethir, Hyperbridge, Kelp, Kelp replay, CE5E drainer, Pattern D scan, Pattern F scan) |

Git history: four commits, all uploads (2026-04-20, 2026-05-15 ×2, 2026-05-17). There is no line-level authorship history; the corpus was developed elsewhere ("the Layer 3 ai lang corpus") and snapshot here. Many referenced artifacts do not exist in this repository (`reports/drift_*.md`, `reports/correction_log.md`, `reports/epistemic_test_results_2026-04-29.md`, `cases/*.md`, `docs/INDEX.md`, decks). The reconstruction is therefore of a *partial* corpus; where a claim depends on an absent file I mark it as such.

---

## 1. Central hypothesis / thesis

The corpus states its thesis in three registers.

**Empirical thesis** (lexicon, *Compositional Harm*): "most harm in the permissionless ecosystem is NOT caused by code defects. It is caused by the way correctly-executing components combine." Its instances are configuration choices (Kelp's 1-of-1 DVN), operational key management (Aethir, Drift, Wasabi), trust bindings between components (oracle→lending, DVN→endpoint→adapter→Aave), and permissions granted and never revoked (Permit2 allowances).

**Methodological thesis** (lexicon, *Stored Potential*): the correct risk object is not "is this broken?" but "what happens when this works perfectly?" — capability × permissions × trust bindings × mutability, discounted by constraints (timelocks, multisigs, verifier thresholds). "The absence of realized value is the danger signal." From this follows the claim that a pre-exploit observation surface exists (configuration reads, admin topology, dormant fleets, approval graphs) and that lead time is measurable ("≥56.7 days" for Kelp).

**Predictive/combinatorial thesis** (V1 cross-cutting notes): "Every attack here uses building blocks we've already observed; the gap is whether they'll be assembled into the full chain. Pre-building detectors for the assembled forms means the first instance in the wild gets caught immediately." V2 strengthens this into a validation claim: "The April wave validated the combinatorial threat-modeling approach." V3 strengthens it again: "v2's combinatorial framework, built two weeks before this wave, predicted the surface that produced these events."

A fourth, commercial register runs underneath: the "detection gap" between free scanners and the observed operator population "IS the product"; the framework is "load-bearing in pitches" (Tier A), and the corrections log exists to "make the project defensible under scrutiny."

## 2. Threat model

**Adversaries the corpus reasons about** (as named in the documents):
- Trap/honeypot deployers and deployer fleets on Base/Arbitrum/Optimism (the monitored chains), including "coffee fleet"-style operators that run both traps and the bots that hit them.
- Phishing/approval drainers ("rogue x402 facilitators" CE5E, E717, A7B9, E3B2, D270, 881E, F71C) sweeping Permit2 allowances.
- Organised operator cells (`org_001`–`org_004`) with gas stations, LP staging, CEX exits, vanity shadow wallets, and an MEV contract.
- Funders at scale ("Infrastructure-Scale Operators"; "Single-Purpose Infrastructure Funders"; "drainer-spawn hubs").
- Operational-layer attackers (DPRK-attributed social engineering, key theft, durable-nonce pre-signing); colluding or compromised verifiers (DVN operators, validators, council members).
- Fake-token/oracle manipulators against lending and margin protocols.
- "Advisor-parasites" (slow-extraction trusted intermediaries) — hypothesised, never observed.
- AI agents as confused deputies (prompt injection) — added late (May).

**Targets:** user approvals and balances; scanner/MEV bots; pooled-custody cross-chain adapters; lending/margin protocols; governance councils; proxy admin authority; off-chain identity systems (OAuth, SSO).

**Defender posture:** Layer 3 is explicitly observer-only ("we can watch everything and affect nothing"; "Layer 3 has no enforcement layer"). Enforcement is re-imported from issuers (Circle/Tether freezes), security councils, CEX compliance, and social coordination (*External Accountability Infrastructure*).

**Monitoring scope:** Base, Arbitrum, Optimism, via trap-adjacent bytecode ingest, Permit2/flagged-contract approvals, and org-wallet transfers. Ethereum mainnet, BNB, NEAR, Solana are *out of ingest scope*; every major April–May incident occurred outside the monitored surface, which the corpus states plainly ("The entire laundering flow is on Ethereum and outside our ingest scope"; "Zero direct coverage").

## 3. Assumptions (explicit and implicit)

Explicit:
- A1. Building blocks recombine; enumerating the assembly space anticipates attacks (V1 §Cross-Cutting Notes).
- A2. Age-as-trust is a bias in every existing scanner (V1 Attack 4; lexicon *Pristine Solo Operator*).
- A3. Operators calibrate against published detection thresholds; the observed revert-rate distribution is an equilibrium of that calibration (*Camouflage Ratio*, *Publishing-Induced Recursive Evasion*).
- A4. Attack techniques propagate through lifecycle phases within days to weeks (*Strategy Lifecycle*: "EARLY → ARMS_RACE within 15 days").
- A5. Configuration is publicly readable, therefore configuration-class stored potential is monitorable with lead time (*Configuration-Level Vulnerability*).
- A6. Lock-and-release custody produces more realised harm than mint-burn because stolen tokens are "indistinguishable from legitimate holdings" (*Pooled Custody Amplification*).
- A7. On-chain topology alone is insufficient for identity; an off-chain label layer (OLI) is required at promotion time (added 2026-05-09, Correction #20 — an assumption the corpus *acquired* after being wrong).

Implicit (never stated, but load-bearing):
- A8. Corpus observables (revert rate, fanout, mainnet history, `TIMESTAMP` opcode, empty logs, vanity prefixes) discriminate adversarial from benign populations without base-rate measurement. No control group appears anywhere in the corpus.
- A9. An incident reported by third parties that fits a category counts as that category being "observed", even when Layer 3 itself observed nothing (V2/V3 status legend vs. usage).
- A10. Persistent addresses (breaks on NEAR; acknowledged in the Rhea report).
- A11. The three monitored L2s are a representative sample of adversarial DeFi behaviour (never argued; contradicted by the corpus's own out-of-scope incident list).
- A12. Notional token amounts and realised USD losses can be treated interchangeably (e.g., "$3.1 quadrillion OP" needed a correction; "$292M" and "116,500 rsETH" are used without distinguishing extracted, borrowed, and bad-debt figures).

## 4. Attack / maneuver classes (as the corpus defined them)

**V1 hypotheticals (2026-04-07), all "components observed, chain hypothetical" or "architecturally valid, unconfirmed":**
1. Permission Harvesting + Routing Parasite; 2. Dormant Fleet + Proxy Upgrade Swap; 3. TaaS Template with Hidden Skim; 4. Time-Lock Synchronized Fire; 5. Cross-Chain Rotation Evasion; 6. Probe-Trap Targeting Scanners; 7. Custom Selector Drain Avoiding Logs; 8. Infrastructure-Layer TaaS Skim.

**V2 additions (2026-04-20), each anchored on an April incident:**
9. Cross-Chain DVN Verification Failure (Kelp); 10. Cross-Chain Proof Verification Bypass (Hyperbridge); 11. Pooled Custody Adapter Compromise (Aethir; Drift and Zerion as cousins); 12. Oracle Manipulation via Fake-Token Collateral (Drift, Rhea; Silo "same category"); 13. Operational Layer Compromise at Governance Scale (Drift, Bybit, Zerion); 14. Advisor-Parasite (Pattern F; Tier C, unobserved).

**V3 changes (2026-05-15):** Attack 11 split into 11a key-compromise (Aethir, Wasabi, Volo) and 11b acquired-admin-via-code-defect (Renegade); Attack 15 "Native-Swap Pooled-Custody Bridge Drain" parked as a candidate with four enumerated resolution paths pending THORChain forensics; Wasabi added to Attack 2 as a "multi-chain single-contract instance"; Juicebox V3 and Thetanuts listed as "continuation" instances (access-control / cross-chain admin variants) with amounts "pending".

**Lexicon-level pattern families (parallel to the numbered attacks):** Behavioral Laundering Patterns A–F (reputation sacrifices, temporal normalisation, CEX-laundered funding, cross-chain reputation import, fake legitimate projects, advisor-parasite); operator typologies (Pristine Solo Operator, Infrastructure-Scale Operator, Single-Purpose Infrastructure Funder, Self-Deploying Single-Contract Mass-Drain, Protocol-Family Specialist Operator); Adversarial Vanity Branding (four sub-categories); Maneuver Primitives (reconnaissance → positioning → trust establishment → trigger → exploitation → exfiltration) and five Counter-Maneuver verbs.

## 5. Entities and relationships

**Entities.** Contracts (trap, bait/approval-harvester, proxy + implementation, OFT/lock-release adapter, pool, oracle, token, router/aggregator, endpoint, diamond/facets); accounts (deployer, funder/gas station, operator EOA, victim, scanner bot, admin/owner key, council member, DVN operator, validator, relayer/executor, CEX hot wallet, laundering intermediary, vanity/shadow wallet); aggregates (bytecode family, deployer fleet, organisation `org_xxx`, funder cluster, drain wave/iteration); chains (monitored L2s vs. reference chains); protocols as composition partners (Aave, Morpho, Ref Finance, Raydium, LayerZero, Permit2, Squads); off-chain actors (phishing infrastructure, stablecoin issuers, security councils, bounty platforms, auditors, law enforcement, AI agents and their permission layers).

**Relationships the corpus reasons over.** *funds* (funder→deployer; CEX→wallet; Tornado→attacker), *deploys* (deployer→contract; template→fleet), *calls / is called by* (victim→trap; bot→trap; router→pool; deployer→own contract "self-loop"), *approves* (user→spender; Permit2 allowance), *delegatecalls / upgrades / initialises* (proxy→implementation; admin→proxy; anyone→unprotected initializer), *attests / verifies* (DVN→endpoint→adapter; oracle→lending protocol; validator set→vault), *holds custody of* (adapter→pooled deposits), *composes into* (stolen rsETH→Aave collateral), *bridges / rotates across* (chain A→chain B; address reuse; `intents.near`), *launders through* (vanity sink→CEX; THORChain→BTC), *mimics* (vanity prefix collision; victim-mimic wallets), *labels* (OLI tag→address; Etherscan tag).

## 6. Evidence standards

Stated: **Epistemic Tier Classification** — Tier A "deductive, verifiable from on-chain data"; Tier B "inferential, methodology-applied"; Tier C "speculative". Status legend for attacks: *Observed* (full chain seen end-to-end) / *Components observed, chain hypothetical* / *Architecturally valid, unconfirmed*. A corrections log with severity ratings, a retirement index, a propagation watch-list, and the rule "This index is supreme over any other file containing the same claim." Reports end with a "What this file does NOT claim" section. RPC budgets are declared and accounted for (Kelp replay: 15 of 50 calls).

Applied: unevenly. Reports (Kelp replay, CE5E, Pattern D/F scans) mostly keep to their own rules and publish negative results. The lexicon and the V2/V3 headline sections do not: incident mechanisms are asserted at Tier-A-like confidence from secondary sources within days (THORChain, Aethir), retired claims are still cited as live (the retired trust-amplification multiplier, the GoPlus "100% gap"), and "observed" is used for categories whose only instances are external incident reports.

## 7. Observation / deduction / inference / speculation — how the corpus distinguished them

- **Observation** = rows in Layer 3 tables or direct RPC reads (Tier A): caller counts, revert rates, `getConfig` returns, Tornado withdrawal timing, drain event logs.
- **Deduction** = arithmetic on observations (lead time ≥56.7 days from replayed blocks; 42% pass-through from a 4-victim audit).
- **Inference** = methodology-applied interpretation (Tier B): "1-of-1 DVN produces CRITICAL stored potential"; "self-settlement = rogue facilitator"; "54% mainnet history = reputation import".
- **Speculation** = explicitly Tier C: advisor-parasite, "attacker will replicate within 15 days", strategy-lifecycle forecasts.

The corpus is explicit that Tier C is "never cited in commercial materials without explicit framing as prediction." It does not, however, have a category for *third-party-reported incident facts*, which are treated as Tier A by adoption ("Sourced from … + Blockaid statement + LayerZero network response").

## 8. Implicit ontology

Three overlapping metaphor systems carry the ontology: **physics** (stored potential, discharge, phase transition, entropy, "digital physics"), **game theory/strategy** (hybrid gameboard: Go/Poker/Chess/Monopoly; Nash equilibrium camouflage), and **military doctrine** (maneuver, counter-maneuver, reconnaissance, tempo, terrain). Underneath them the working ontology is:

- *Nodes* scored on five primitives — position, permissions, trust bindings, mutability, observation capability (*Adversarial Topology*).
- *Failure layers* — code / configuration / operational (the Aethir–Hyperbridge–Kelp triad), later extended with "compositional" and "cross-domain".
- *Phases* — storing potential → seeding → discharge (V1–V3) and the six Maneuver Primitives (lexicon).
- *Populations* — predators, prey, "tuition" flows, victim-to-predator migration.
- *Layers of anti-forensics* — transaction layer (log-less drains), victim layer (Unicode token impersonation), intelligence layer (vanity spoofing).

The taxonomy mixes categories of different kinds: mechanism (DVN failure), actor role (advisor-parasite), operator topology (single-purpose funder), phase (positioning), and incident-of-record (the "Kelp category"). Attack numbers are attached to incidents rather than to mechanisms, which is why Attack 11 had to split and Attack 15 could not be resolved without a post-mortem.

## 9. Causal chains the corpus asserts

1. Low verifier threshold (1-of-1 DVN) → single compromised/colluding verifier → forged cross-chain message accepted by endpoint → adapter releases pooled custody → stolen token composes into lending markets as collateral → bad debt propagates (Kelp).
2. Single-key admin, no timelock → key compromise (phishing, malware, insider) → cryptographically valid authorised action (upgrade, mint, withdraw) → pool drained (Aethir, Wasabi, Volo).
3. Council members' keys or pre-signed durable nonces compromised → governance weakens its own threshold/timelock → attacker already holds quorum → drain (Drift).
4. Fake token + one-sided pool + wash trading → oracle reports fabricated price → protocol accepts as collateral → real assets borrowed → fake token collapses (Drift CVT, Rhea).
5. Proof-verification edge case → forged proof → unbacked mint (Hyperbridge).
6. Unprotected initializer → attacker becomes admin → malicious implementation → approvals swept (Renegade).
7. Dormant fleet + age-as-trust → coordinated activation at block T → simultaneous drain (V1 Attack 4; hypothetical).
8. Publishing detection methodology → operator calibration → detection decay → sustainable edge is corpus depth, not novelty (*Recursive Evasion*).
9. Neutral deterministic execution attracts predators → losses accumulate → emergency cores (councils, freezes, forks) are introduced → two-layer governance (*Neutrality Trap* → *Normative Shell Game*).
10. Per-action gas cost habituates users to paying → sub-JND extraction becomes invisible → advisor-parasite economics (*Cost-Habituation* → *Pattern F*).

## 10. Predictions

Dated, explicit forecasts found in the corpus (full audit in `reports/prediction_audit.md`):
- Rhea report (2026-04-18): "Expect further copies within 30 days per the strategy_lifecycle model."
- Lexicon *Convergent Calibration* (2026-05-05): "Forecast iter_9 (2026-05-07 ~10:02 UTC) is the next falsifiability test."
- Lexicon *Self-Deploying Single-Contract Mass-Drain* (2026-05-10): "expect a fourth instance within 1-3 days of III; if absent for >5 days, the cadence framing weakens."
- V3 Attack 15 (2026-05-15): four enumerated mechanism outcomes for THORChain, each mapping to an existing attack.
- V1/V2 Attack 4: the time-lock calendar is "the highest-leverage addition" — an implicit forecast that a synchronised-fire fleet will appear.
- Lexicon *Pattern F* and *Pattern A/B*: re-scan triggers at corpus age ≥60/90 days — implicit forecasts that candidates will surface once the window is long enough.
- Lexicon *Operational Layer Attack*: "2026 attacks will target operational layers around key management, not the keys themselves" (attributed to Blockaid, January 2026; adopted as the corpus's own expectation).
- V2 Attack 9: "any adapter holding >$10M in pooled deposits with a 1-of-1 DVN is a pre-validated Kelp-class risk" — a standing risk forecast about a population.
- V3 headline: "the framework's predictions retroactively match the next wave of incidents" — a claim *about* prediction rather than a prediction.

Directional expectations (not dated): recursive evasion will erode published signals; centralised overrides will proliferate after catastrophic loss; AI agents will multiply confused-deputy incidents; lock-and-release adapters will keep producing the largest realised losses.

## 11. Falsifiable claims

Falsifiable as stated: the Kelp lead-time replay (reproduced on-chain in `reports/evidence/onchain_checks_2026-09-28.md`); the Tornado funding gap; the 54/100 Pattern D count (given Layer 3's list); the iter_9 and fourth-instance cadence forecasts; the four THORChain resolution paths; the "no instance of Attack 4/6/7/8 yet" statements; camouflage-ratio range (70–79%) given the corpus; specific incident facts (dates, amounts, contract names).

Unfalsifiable as stated: "Every successful exploit in the corpus traverses these phases in order" (any narrative can be so decomposed); "every major DeFi exploit demonstrates this hybrid [four-game] nature"; "compositional harm is the central finding" without a count-vs-value definition; camouflage ratio "as a Nash equilibrium" (no calibration observable); "Thermodynamic Fundamentalism" (all anchors retracted); "Detection Gap as Product" (commercial).

## 12. Where the framework deliberately expressed uncertainty

The corpus is explicit about uncertainty in these places, and they should be credited:
- V1: "None of the attacks above are in the Observed category."
- Attack 7: "leading hypothesis"; Attack 8: "Unconfirmed as of April 7, unconfirmed as of April 20."
- Attack 14: Tier C; "Zero confirmed advisor-parasites"; "The hypothesis is not falsified; it's unprovable with the current data."
- Attack 15: "CANDIDATE, not promoted"; "Mechanism TBD pending forensics."
- Kelp: "No attribution of the compromised DVN operator. Whether the attacker obtained signing keys via compromise or was the DVN operator is not established"; "No prevention claim."
- Kelp replay: "the post-hoc 'we would have caught it' framing is only as good as the detector configuration we would have chosen to run"; explicit list of overclaims *not* used.
- Hyperbridge: "$237K initial estimate is likely to be revised."
- Pattern D: "The 54 cross-chain imports are not all malicious… correlation between import-pattern and malicious-intent is not established."
- CE5E: "do not cite the $3.63M concentration figure"; "No attribution to a named operator."
- Correction #20 and the Pristine Solo / Infrastructure-Scale retractions: "a behavioral-only detector cannot distinguish 'established operator expanding to a new chain' from 'predatory dormancy with reputation cover'."
- Volo: "full mechanism enumeration pending"; Juicebox/Thetanuts: amounts "(pending)".

The pattern is consistent: uncertainty is expressed carefully inside the report files and inside the corrections log, and expressed much less carefully in the lexicon's "empirical grounding" bullets and in the V2/V3 validation narratives, which were written for external use.
