# Temporal Audit — Reader's Index

This branch (`v4-temporal-audit`) adds a longitudinal evaluation of the historical Maneuvers corpus (V1 2026-04-07 → lexicon 2026-05-17) against evidence through 2026-09-28. Nothing historical was modified or deleted; `POTENTIAL_ATTACKS_V1_ARCHIVE.md`, `POTENTIAL_ATTACKS_V2*.md`, `POTENTIAL_ATTACKS_V3.md`, `lexicon.md`, `docs/lexicon.md`, `CORRECTIONS.md` and the original eight `reports/*.md` are byte-identical to `main`.

Read in this order:

1. `reports/historical_reconstruction.md` — what the original work was trying to do (Phase 1)
2. `reports/claim_ledger.md` (+ `.json`) — 97 claims, typed and statused (Phase 2)
3. `reports/temporal_audit.md` — status of every maneuver and concept; what the window tested (Phases 3–4)
4. `reports/prediction_audit.md` — 20 predictions with outcomes (Phase 5)
5. `V4/` — `FRAMEWORK.md` (Phase 6), `MANEUVERS.md` (Phases 7–8), `COMPETING_EXPLANATIONS.md` (Phase 10), `CHANGELOG_FROM_V3.md`, `README.md`
6. `reports/framework_failure_analysis.md` — the red team on V4 (Phase 9)
7. `reports/model_comparison.md` — model-to-model comparison and the counterfactual test (Phases 11–12; the historical model's identity is revealed only here)
8. `reports/final_assessment.md` — direct answers, plus V4's own dated predictions (Phase 13)

This audit is generation **G1** of the longitudinal experiment described in `experiment/PROTOCOL.md` (research question, hypotheses, controls, metrics). G0's predictions and G1's pre-registered predictions are in `experiment/predictions/`; scored metrics in `experiment/metrics/`.

Evidence: `reports/evidence/` — the audit's own on-chain reads, two fact-check reports, a post-revision incident survey, and the script that generates the claim ledger. Evidence files carry provenance headers; the two verification reports and the survey are model-generated research output and every figure in them is a pointer to a cited URL, not a primary fact.
