# Final Assessment (Phase 13)

**Subject.** The Maneuvers corpus — `POTENTIAL_ATTACKS_V1_ARCHIVE.md` (2026-04-07), `V2` (04-20), `V3` (05-15), `docs/lexicon.md` (05-17), `CORRECTIONS.md`, and eight reports — audited on 2026-09-28/30 against evidence through 2026-09-28. Supporting artefacts: `historical_reconstruction.md`, `claim_ledger.md` (97 claims), `temporal_audit.md`, `prediction_audit.md` (20 predictions), `framework_failure_analysis.md`, `model_comparison.md`, `V4/`.

The brief asked for direct answers. They follow.

---

## What survived?

**Concepts that remain valid over time**, in descending order of how much later evidence supports them:

1. **Configuration-level vulnerability as a monitorable class.** The 1-of-1 DVN read was reproduced on-chain (`getConfig` at block 24,500,000: requiredDVNCount = 1); 47% of active OApps shared the condition; the ecosystem built the exact monitor the corpus described and changed protocol defaults; Kelp's channel now requires 4-of-4. The corpus was one of several parties to say this in the same week, but it said it as a *class* and it held.
2. **Pooled custody amplification.** Lock-release custody realises losses 1:1 while unbacked mints realise at liquidity. Sandbox ($49B face, $675K realised — the realised part was the lock-release adapter), Symbiosis, Hyperbridge and Liquid are the natural experiment the April corpus lacked.
3. **Operational-layer dominance by value.** 74% (Blockaid) / ~76% (TRM) of H1 stolen value from operational and infrastructure compromise. Q3's Bitget ($387.5M) extends it to a mode the corpus lacked (request forgery, keys intact).
4. **Neutrality-trap override and kill-switch governance.** Chain-level halts and rollbacks (Cronos $111M reversed; Harmony; Cosmos Hub 24.5 h; Liquid; Taiko; Osmosis) became the dominant Q3 recovery mechanism, with the legitimacy fight the corpus predicted (SDNY over Arbitrum's frozen ETH).
5. **Verification-path trust failure** as the seam where most non-code losses occur (Ostium, Bonzo, Nostra, Across, Wanchain, Bitget).
6. **Unprotected-initializer takeover** — confirmed by Aurellion within 48 hours of the hook being written.
7. **Bug-bounty structural gap** — Ostium's keeper path out of scope despite an auditor's warning; Cosmos Labs mis-triaging a valid report; THORChain retiring its bounty.
8. **Confused deputy for AI agents** — right on mechanism (three Bankr incidents; x402 censuses); magnitude still small.
9. **The corrections process** — the largest single source of disconfirmations in this audit is the corpus's own log, which is what a corrections process is for.

## What failed?

**Disproven:**
- THORChain's mechanism as asserted in the lexicon (observation bit-flip; "TSS signed real outbounds"). Official post-mortems: a bonded validator exploited a GG20 threshold-signature flaw to reconstruct the vault key and sign directly. None of V3's four enumerated resolution paths matched.
- The April-30 "mass dormant-wallet drain" as a Permit2 burst of 49 wallets in 3.5 minutes. It was ~570 wallets over ~13 hours, native ETH, stolen keys, no approvals — and it anchored two core lexicon entries.
- Drift recovery arithmetic ("Tether froze $127.5M"; "Solana Foundation $20M"; "87% coverage"). Tether contributed capital (largely a $100M credit facility); ~3.36M USDC was frozen; the Foundation's contribution is not confirmed by Drift.
- Juicebox V3 and Thetanuts as "admin-pattern" instances (input validation and first-depositor bugs, ~$50K each).
- Wasabi's helper "pre-positioned via CREATE2" (plain CREATE at nonce 0; absent on Blast).
- Infrastructure-Scale Operator and Pristine Solo Operator as behavioural typologies (the corpus's own 05-09 audit: exchanges, bridges and game studios).
- Static-vs-dynamic as a safety claim (Liquid $320M; Coldcard $116M).
- The two validation narratives: "6-of-14 observed validated combinatorial threat modelling" (V2) and "v2 predicted the surface" (V3).

**Overstated:**
- "Most harm is not caused by code defects" — true by value in H1, false by count throughout, false by value for Q3 bridges (~$385M of verification code bugs).
- Strategy Lifecycle's 15–30-day replication clock (observed lags 2–95 days; the 30-day forecast failed).
- Attack 4 (time-lock synchronised fire) as "highest-leverage" — nothing in five months.
- Compositional Harm's universal quantifiers; Maneuver Primitives as law; the Hybrid Gameboard's empirical grounding.
- Every topology-only inference without a base rate (fanout, dormancy, mainnet history, self-settlement, prefix collision, `TIMESTAMP`, low reverts).

**Obsolete or unsupported:**
- Thermodynamic Fundamentalism (anchors retracted).
- The Blockaid "January 2026 prediction" and the Immunefi "April 18" confirmation (not found).
- The Aethir dev.to quotations (not in the cited post) and Aethir's classification as key compromise (no source).
- Retired figures still cited live in the lexicon (trust-amplification multiplier; "GoPlus 0/50"; victim-to-predator).

## What was genuinely ahead of its time?

Three things meet the bar of "anticipated later developments in a meaningful, falsifiable way":

1. **The DVN-configuration monitor with a TVL filter** (04-20). Falsifiable (the population could have been small; it was 47%), specific (a query and a threshold), and adopted independently. The corpus's originality is shared with Blockaid; its class-level generalisation was its own.
2. **Lock-release > mint-burn in realised harm** (04-20). A mechanical prediction with a clean later test.
3. **Kill-switch governance as a variable worth measuring per protocol** (05-15, from one case). Q3 made it the central recovery question.

Two more were *directionally* ahead without being falsifiable as written: override proliferation (Neutrality Trap phase 4) and agentic confused-deputy incidents.

Not ahead of its time, despite the corpus's claims: the combinatorial V1 attacks (none occurred as written); the "predicted the May wave" narrative (the initializer hook post-dates Renegade).

## What did the original framework misunderstand?

Structural weaknesses, not individual mistakes:

1. **No base rates.** The framework's detectors are edge-shape detectors on a graph, and the framework never measured how often benign actors produce the same shapes. When it finally did (Correction #20), the typology collapsed. This is the root of most of the DISCONFIRMED and OVERSTATED entries in the ledger.
2. **"Observed" without observation.** The status legend defined *Observed* as "full chain seen end-to-end" in Layer 3's data; usage meant "a third party reported an incident that fits". No V2/V3 category was ever observed by the corpus's own detectors; the corpus's real observations were trap fleets and drainers on three L2s, and those are the claims the audit could not test.
3. **Narrative outran evidence at the lexicon layer.** Reports kept discipline (budgets, negative results, "what this does NOT claim"); the lexicon's "empirical grounding" bullets and the V2/V3 headline sections — the parts written for external audiences — did not. The mechanism embargo V3 practised on THORChain was abandoned in the lexicon two days later.
4. **No actor economics.** The framework scored what *could* be discharged and never what discharge would *cost*; so it could not ask why 1,250 exposed OApps produced one exploit, or why a validator would post 635K RUNE to steal $10.7M.
5. **Category kinds mixed.** Mechanisms, actor roles, phases, and incidents-of-record shared one numbering; the framework had to split and park categories whenever an incident did not fit an anchor.
6. **Notional and realised conflated.** A slot the corpus's own decimals bug should have created.
7. **Corrections did not propagate.** The index declared itself "supreme"; the lexicon that post-dates it still cites what it retired, and the Binance-hot-wallet finding never reached the org_001 claims that depend on it.
8. **Metaphor stacking.** Physics, then games, then warfare, each added as "doctrine" without retiring the last; the last was grounded on a wrong mechanism.

## What does the updated framework see that the original did not?

**Genuinely new insight (available without the window, produced by reasoning):**
- The base-rate obligation as a rule, not a one-off correction.
- Epistemic status tied to public instances, with "corpus-internal" as a separate, honest bucket.
- Notional / realised / recovered as ontology, not bug fixes.
- The circularity in the validation narratives.
- Actor cost as the missing dampener term (M-27), and the exposure/discharge gap as its symptom.
- Mechanism embargo as a rule.

**Information that simply became available later (hindsight incorporation):**
- M-07 (malicious TSS participant), M-10 (weak key generation), the signing-pipeline mode (Bitget), config-role capture (Sandbox), vote-capture-without-timelock, stale-valuation and signer-compromise oracle modes, the Q3 dominance of verifier code bugs, halts/rollbacks as the recovery norm, Kelp's RPC-poisoning mechanism.

The audit is explicit (`model_comparison.md` §12) that roughly a third of the V3→V4 delta was available to the earlier model on its own evidence and two-thirds needed the window.

## Did the underlying framework improve?

**As a specification, yes.** V4 removes what the corpus itself retired, drops two classes with no surviving anchors, adds three demonstrated classes, attaches a benign-population note to every signal, separates notional from realised, ties status to public instances, commits to dated predictions, and records open obligations rather than silently dropping them.

**As an instrument, no — and it is worse.** V3 ran on a live corpus with detectors and produced measurements. V4 runs on nothing; every base-rate note is an IOU. A specification that demands measurements it does not perform is a better specification and no more. Whether V4 improved the *framework* will be decided by whether those obligations are paid (benign-cohort baselines; population-scale pass-through audit; initializer census; the two unresolved cadence forecasts; the Pattern F re-scan).

**On reasoning, partially.** The method changes in V4 are reasoning changes; the content changes are information. The audit cannot claim its reasoning is better in general — only that on this problem it caught errors the earlier work made that were catchable at the time, and that it also made errors of its own (`model_comparison.md` §5).

## Is Maneuvers still useful?

Separated as the brief requires:

| Dimension | Assessment |
|---|---|
| **Usefulness** (does it help someone reason about adversarial DeFi behaviour?) | Yes, with the ledger and V4 attached. The failure-layer taxonomy (code / configuration / operational / composition), the reservoir–trigger–amplifier structure, and the corrections posture are worth keeping. Without the audit attached, the lexicon would mislead: a reader would inherit retired figures, an invented THORChain mechanism, and unlocatable citations at Tier-A confidence. |
| **Predictive validity** (did it forecast?) | Narrow but real. Four confirmed predictions with content; the predictive band is mechanism-and-incentive reasoning (custody architecture, readable thresholds, override incentives). Its self-assessed predictive record was its least reliable content. |
| **Descriptive power** (does it organise what happened?) | High. Nearly every window incident maps onto a V4 maneuver without forcing — which is also the warning: descriptive frameworks map everything. The exceptions that do not map (Coldcard; Liquid; Aztec) are the useful ones. |
| **Operational usefulness** (could a defender act on it?) | Medium, concentrated in a few hooks: DVN/verifier threshold and *change* monitoring with a TVL filter; initializer-state enumeration; cross-chain conservation checks; admission-time collateral pressure tests; governance-parameter and proposal-payload screening; keysign-failure monitoring per validator; time-to-halt as a protocol attribute. The topology signals (fanout, dormancy, prefixes, self-settlement) are not operational until base rates exist. |
| **Theoretical elegance** | Overrated by the corpus. The physics/game/warfare metaphors added surface, not structure; the elegant core is small — reservoir, trigger, constraint, amplifier — and survives without any of the metaphors. |

These do not collapse into a score, and the brief was right to forbid one. The framework is useful and descriptively strong, predictively narrow, operationally thin, and theoretically over-dressed.

---

## V4 predictions (registered 2026-09-30, for the next audit)

So that V4 can be audited the way V1 was, it commits to the following. The canonical, machine-readable registration — with confirmation and falsification conditions and resolution sources for each — is `experiment/predictions/G1.json` (SHA-256 recorded in `experiment/generations.json`); this table is a summary. **p** is the registrant's probability that the confirmation condition holds; the next generation scores these with `experiment/score.py` (Brier), so calibration is on the record. Fourteen of nineteen sit in the 0.3–0.7 band by design (protocol §7.7).

| ID | Prediction | p | Resolves |
|---|---|---|---|
| PV4-1 | No exploit of a PRE-EXISTING (not attacker-created) sole-required-DVN LayerZero configuration protecting a reservoir > $10M occurs between 2026-10-01 and 2027-03-31. | 0.80 | 2027-03-31 |
| PV4-2 | Cross-chain verification CODE defects (M-02) exceed attestation-CONFIGURATION failures (M-01) in realised losses for 2026-10-01 to 2027-03-31. | 0.75 | 2027-03-31 |
| PV4-3 | At least two further publicly post-mortemed unprotected-initializer or uninitialized-facet takeovers occur between 2026-10-01 and 2027-03-31. | 0.70 | 2027-03-31 |
| PV4-4 | Chain- or protocol-level halt/rollback/freeze is used in >= 3 incidents with >= $5M at stake between 2026-10-01 and 2027-03-31, and at least one such use is contested in governance or in court. | 0.65 | 2027-03-31 |
| PV4-5 | At least one further malicious-participant threshold-signature attack (a bonded/registered signer extracting key material or biasing key generation through protocol interaction) on a production network occurs between 2026-10-01 and 2027-09-30. | 0.35 | 2027-09-30 |
| PV4-6 | No public instance of a time-lock synchronised-fire fleet (M-22) or an aggregator routing-parasite pool (M-19) is documented between 2026-10-01 and 2027-09-30. | 0.85 | 2027-09-30 |
| PV4-7 | Cumulative realised losses from AI-agent permission-chain abuse (prompt injection, agent-wallet permission escalation, agent session-key compromise) stay below $25M for 2026-10-01 to 2027-09-30. | 0.60 | 2027-09-30 |
| PV4-8 | At least one governance drain >= $1M succeeds THROUGH an execution timelock (delay present and not bypassed) between 2026-10-01 and 2027-09-30. | 0.40 | 2027-09-30 |
| PV4-9 | The Arbitrum address 0xce5ec7336f863931fda2ee3e4b9dad99fcc53c91 is either publicly identified as a payment/settlement service or publicly reported as a drainer by 2027-03-31. | 0.30 | 2027-03-31 |
| PV4-10 | DPRK-attributed share of full-year 2026 stolen crypto value is >= 50% per at least one of TRM, Chainalysis or Elliptic year-end reports. | 0.70 | 2027-02-28 |
| PV4-11 | At least one collateral-valuation manipulation exploit (M-06) with realised loss >= $20M occurs between 2026-10-01 and 2027-03-31. | 0.55 | 2027-03-31 |
| PV4-12 | Kelp (Evercrest) v. LayerZero Labs has no final merits judgment by 2027-09-30. | 0.85 | 2027-09-30 |
| PV4-13 | At least one further incident >= $10M in which an exchange's or protocol's OWN signers sign attacker-chosen withdrawals without private-key theft (forged internal requests, compromised signing UI, or vendor path) occurs between 2026-10-01 and 2027-09-30. | 0.50 | 2027-09-30 |
| PV4-14 | Reported 2026 full-year end-user phishing/signature-drain losses (ScamSniffer annual or equivalent) exceed the 2025 figure of $83.85M. | 0.55 | 2027-02-28 |
| PV4-15 | No public, on-chain-documented advisor-parasite pattern (months-long sub-threshold extraction from retained victims by a trusted intermediary) is confirmed between 2026-10-01 and 2027-09-30. | 0.85 | 2027-09-30 |
| PV4-16 | At least one further Cosmos-ecosystem governance or admin-update drain >= $1M occurs between 2026-10-01 and 2027-09-30. | 0.55 | 2027-09-30 |
| PV4-17 | Realised losses from cross-chain verification code defects (M-02) exceed $100M for 2026-10-01 to 2027-03-31. | 0.60 | 2027-03-31 |
| PV4-18 | A public tool or dashboard that enumerates exposed/uninitialized proxies population-wide on at least one major EVM chain is published by 2027-09-30. | 0.50 | 2027-09-30 |
| PV4-19 | At least one further incident in which an attacker CAPTURES a cross-chain configuration role (delegate, DVN set, peer, ISM) rather than exploiting a pre-existing weak setting occurs between 2026-10-01 and 2027-09-30. | 0.45 | 2027-09-30 |

**Falsification criterion for V4 as a whole.** If PV4-1, PV4-2 and PV4-4 all fail, the reservoir–trigger–constraint core is not tracking where losses come from, and the framework should be treated as descriptive only.

**Why this matters for the experiment.** G0's twenty predictions carried no probabilities, so its hit rate (0.56 over 13 resolvable) cannot be compared to a calibration score. From G1 onward every generation is Brier-scorable, and the experiment's central question — improvement versus explanation — is decided on these forward-looking scores under the controls in `experiment/PROTOCOL.md`, not on how well the next version explains the next window.

## Closing statement

The historical work reasoned well about mechanisms and incentives, kept an honest corrections log, and did more primary verification per claim than this audit did. It reasoned badly when it narrated mechanisms ahead of evidence, inferred adversaries from topology alone, and assessed its own predictive record. The passage of time validated more of its structure than it refuted, falsified its clock and its self-assessment, and exposed one class of failure (verifier code bugs) it had filed away as someone else's problem. The newer analysis improved the specification and made the framework auditable; it did not build the instrument, and it will not have improved the framework until someone pays the measurements V4 now owes.
