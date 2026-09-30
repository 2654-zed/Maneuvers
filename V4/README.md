# V4 — README

**What this is.** The updated Maneuvers framework produced by the 2026-09-28 longitudinal audit of the V1–V3 corpus (2026-04-07 → 2026-05-17). It is the result of: historical framework + temporal evidence (2026-05-18 → 2026-09-28) + failed assumptions + new observations + framework corrections. It is not a rewrite of V3.

**Files.**

| File | Purpose |
|---|---|
| `FRAMEWORK.md` | Phase 6: the framework that sat under V1–V3 (entities, relationships, preconditions, signals, mechanisms, incentives, consequences, uncertainty, feedback), its structural flaws, and the corrected V4 ontology |
| `MANEUVERS.md` | Phases 7–8: 27 standardised maneuvers with preconditions, mechanism, signals (each with a base-rate note), actors, incentives, consequences, evidence, epistemic status (OBSERVED / STRONGLY INFERRED / HYPOTHESIZED / THEORETICAL), explained confidence, falsification criteria, defensive implications |
| `COMPETING_EXPLANATIONS.md` | Phase 10: H1/H2/H3 tables for the observations the historical work leaned on hardest, with discriminating evidence |
| `CHANGELOG_FROM_V3.md` | What was preserved, downgraded, removed, added — and why |

**Audit artefacts that V4 depends on** (in `../reports/`): `historical_reconstruction.md` (Phase 1), `claim_ledger.md` / `claim_ledger.json` (Phase 2), `temporal_audit.md` (Phases 3–4), `prediction_audit.md` (Phase 5), `framework_failure_analysis.md` (Phase 9), `model_comparison.md` (Phases 11–12), `final_assessment.md` (Phase 13), and `evidence/` (on-chain checks, verification reports, post-revision survey, ledger build script).

**Rules V4 follows that V3 did not.**
1. Epistemic status refers to public, independently checkable instances — not to fit, and not to private data.
2. Every signal carries a base-rate note naming the benign population that produces the same signal.
3. Losses are notional / realised / recovered.
4. No mechanism is asserted for an external incident before a forensic post-mortem; until then it is "TBD" with enumerated hypotheses.
5. Retired claims are removed, not annotated.
6. Predictions get outcomes recorded, including "unresolved".

**Status counts.** OBSERVED 13 · STRONGLY INFERRED 3 · HYPOTHESIZED 9 · THEORETICAL 2.

**Six ways to misread V4** (from `../reports/framework_failure_analysis.md` §7): OBSERVED means public instances exist, not that Layer 3 observed it; base-rate notes are obligations, not measurements; value-weighted claims are not count-weighted claims; demoted hypotheses are unobserved, not refuted; M-13 records rollbacks, it does not endorse them; window-period dollar aggregates come from DefiLlama labels with empty source fields and should be read as ±50%.

**Experiment context.** V4 is generation G1's framework in the longitudinal experiment in `experiment/PROTOCOL.md`. Its pre-registered predictions are `experiment/predictions/G1.json`; G2 scores them and writes V5.

**Open obligations on the corpus owner** (things V4 could not resolve from public data): outcomes of the two cadence forecasts (P-02, P-03); the Pattern F re-scan at ≥90 days; the population-scale pass-through audit for the facilitator addresses; the asset/destination query for the `0x80b12bd0` event; OLI checks on the `T1-d5351e977044` funders and on the Iteration-I mass-drain funder; a benign-cohort baseline for every topology signal.
