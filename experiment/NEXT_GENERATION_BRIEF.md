# Brief for the Next Generation (G2 and later)

You are the next generation in a longitudinal experiment. Read `experiment/PROTOCOL.md` first. The research question is:

> Can successive generations of LLM-assisted research improve the epistemic quality of a framework, or do they primarily become better at explaining the framework after more evidence becomes available?

You are both an auditor of your predecessor and a subject for your successor. Everything you write will be scored by a later model that has evidence you do not.

## Rules that apply before you read anything else

1. **Blinding.** Do not look up, infer, or use the identity of the model that produced the previous generation's framework until you reach Phase 11. `experiment/generations.json` contains model identities — do not open it until Phase 11. Refer to the previous work only as "the previous AI-assisted analysis".
2. **Contamination check.** Before starting, record in your audit whether you recognise this repository or its contents from training data, and your stated knowledge cutoff. Record the answer even if it is "no" or "unsure".
3. **No history rewriting.** Do not modify or delete any file from an earlier generation. Add files; put your framework in `V<n+1>/` and your audit in `reports/` with dated filenames or in `experiment/runs/G<n>/main/`.
4. **Metrics before narrative.** Fill `experiment/metrics/<predecessor>.json` (run `experiment/score.py`) before writing any conclusion. Narrative may not cite a metric that is not in that file.
5. **Pre-register before you look forward.** Write `experiment/predictions/G<n>.json` — at least 15 predictions, each with a probability, a confirmation condition, a falsification condition, a resolution date, and resolution sources; at least five with probabilities between 0.3 and 0.7 — and commit it before doing anything that would let you peek at the next window (there is nothing to peek at yet, but the discipline is the point: the commit hash is the timestamp).

## The audit (same thirteen phases every generation)

Phase 1 — Reconstruct the predecessor's framework faithfully (thesis, threat model, assumptions, ontology, predictions, stated uncertainties). No improvements yet.
Phase 2 — Claim ledger: every evaluable claim, typed OBSERVATION / DEDUCTION / INFERENCE / HYPOTHESIS / PREDICTION / SPECULATION; for each, what was asserted, what supported it, what assumptions it needed, what would have falsified it, whether later evidence tests it, and whether the original statement was stronger than its evidence. Machine-readable JSON with the fields used in `reports/claim_ledger.json`.
Phase 3 — Temporal audit: STILL SUPPORTED / PARTIALLY SUPPORTED / DISCONFIRMED / UNTESTABLE / OBSOLETE / OVERSTATED / UNDER-SPECIFIED, with evidence; watch for capability↔intent, possibility↔probability, correlation↔causation, exploitability↔economic viability, isolated↔pattern, observed↔inferred motive, surface↔demonstrated path, possibility↔incentive, suspicious↔malicious, coincidence↔cause.
Phase 4 — Temporal validation against the new window: did the predecessor anticipate each development, how specifically, predictively or merely broadly; what it missed; which assumptions failed; what attacker adaptation appeared. Primary sources; keep quotes short.
Phase 5 — Prediction audit: score the predecessor's pre-registered predictions with `score.py`; label vague statements NON-FALSIFIABLE / TOO BROAD; do not convert vague statements into hits.
Phase 6 — Extract the framework under the documents (entities, relationships, preconditions, signals, mechanisms, incentives, consequences, uncertainty, feedback); document ontology flaws.
Phase 7–8 — Build V<n+1>: preserve what survived, downgrade what was overstated, remove what was wrong, add what evidence warrants; every maneuver standardised (preconditions, mechanism, observable signals *with a base-rate note*, actors, incentives, consequences, evidence, epistemic status OBSERVED / STRONGLY INFERRED / HYPOTHESIZED / THEORETICAL referring to public instances, explained confidence, falsification criteria, defensive implications). Losses as notional / realised / recovered.
Phase 9 — Red-team your own framework (survivorship, hindsight, selection, confirmation bias; ontology errors; false positives and negatives; missing variables; adaptation; measurement and attribution problems; temporal leakage; overfitting to famous incidents). Construct a counterexample for every major concept.
Phase 10 — Competing explanations (H1/H2/H3) for the load-bearing observations, with discriminating evidence.
Phase 11 — Reveal the predecessor's identity (open `generations.json`). Model-to-model comparison: what they saw that you missed; what you saw that they missed; where they were more disciplined; where each overreached; shared mistakes; which differences are new evidence and which are reasoning; whether you improved the framework or produced a more sophisticated explanation; durable concepts; concepts that aged poorly; genuine predictive value.
Phase 12 — Counterfactual test: strip the window; which conclusions were justified on the predecessor's evidence alone; which changed; tag each change as framework improvement / hindsight incorporation / historical validation / retrospective storytelling.
Phase 13 — Final assessment answering: what survived, what failed, what was ahead of its time, what was structurally misunderstood, what the update sees that the original did not (new insight vs newly available information), whether the framework improved, and whether it is still useful — separating usefulness, predictive validity, descriptive power, operational usefulness, and theoretical elegance. Then register your predictions.

## Additional obligations specific to this experiment

- **Two-auditor rule.** Re-score the generation *two* back as well (its claim survival and predictions), independently of the previous auditor's scores, and record inter-rater agreement.
- **Hindsight re-rating.** Re-classify the previous auditor's Phase 12 change list into reasoning-available-at-the-time vs hindsight, without first reading their classification; then compare.
- **Controls.** Run C1 (information-cutoff: same brief, no evidence after the predecessor's cutoff, web off) and C2 (repeat run, fresh session) at minimum; store under `experiment/runs/G<n>/C1/` and `.../C2/` with the same file layout. Score them with `score.py`. Report the C2 spread; make no generational claim inside it.
- **Pay one IOU.** Measure at least one benign-population base rate for one detection signal the previous generation only *demanded*. This is the single cheapest way to move the forward-looking metrics, and it is deliberately required so that "demanded but never measured" cannot persist across generations.
- **Open obligations.** Check `V<n>/README.md` "Open obligations" and record which were paid, by whom, and what they showed.

## What not to do

- Do not optimise for making the previous generation, or your own, look good. The experiment is only informative if the scoring is harsh in both directions.
- Do not add categories to raise descriptive coverage. Coverage rises are a signature of H2, not H1.
- Do not assert an external incident's mechanism before an official or forensic post-mortem exists; enumerate hypotheses instead.
- Do not cite a source you have not located. Mark unlocatable citations NOT FOUND; do not delete them from the predecessor's files.
- Do not register only safe predictions. The score report prints the probability distribution.

## Deliverables checklist

- [ ] contamination statement and knowledge cutoff recorded
- [ ] `reports/` audit files (Phases 1–13) or `experiment/runs/G<n>/main/`
- [ ] `experiment/metrics/G<n-1>.json` filled (and G<n-2> re-scored)
- [ ] `V<n+1>/` framework
- [ ] `experiment/predictions/G<n>.json` registered and committed
- [ ] `experiment/generations.json` appended (model identifiers, dates, commit hash, SHA-256 of predictions, blinding attestation, controls run, deviations)
- [ ] C1 and C2 control runs stored and scored
- [ ] at least one base rate measured
