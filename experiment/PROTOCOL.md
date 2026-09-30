# Experiment Protocol — Generational Epistemics of an LLM-Assisted Research Framework

**Registered:** 2026-09-30 (generation G1 commit on branch `v4-temporal-audit`).
**Status:** pre-registered; the first scoring event is the G2 audit.

## 1. Research question

> Can successive generations of LLM-assisted research improve the epistemic quality of a framework, or do they primarily become better at explaining the framework after more evidence becomes available?

The framework under study is Maneuvers — a threat-modelling framework for adversarial DeFi behaviour. It was chosen because it makes claims about a world that keeps producing public, dated, post-mortemed events (exploits), so its claims can be scored against reality on a fixed cadence.

The question is deliberately a contrast between two things a later model can do with an earlier model's work:

- **Epistemic improvement** — the framework's *forward-looking* properties get better: predictions are more often right and better calibrated; claims survive longer; overclaiming falls; retractions propagate; evidence gets more reproducible; base rates get measured; mechanisms are not asserted before evidence. These properties are testable *before* the next evidence window opens.
- **Explanatory sophistication** — the framework's *backward-looking* properties get better: later incidents map onto its categories more completely and more fluently, the vocabulary grows, the prose becomes more careful, and the "counterfactual" story of what the earlier version should have seen becomes more compelling — while the forward-looking properties do not move, or move only because more information is available.

The two are not mutually exclusive. The experiment is designed to measure each separately and to separate *information* effects (a later model knows more) from *reasoning* effects (a later model reasons better about the same information).

## 2. Hypotheses (pre-registered)

- **H1 (epistemic improvement):** across generations, the forward-looking metrics (§5.1) improve, and the improvement persists under the information-cutoff control (§4, C1) — i.e., a later generation given *only* the earlier generation's evidence still produces a framework that scores better on the next window.
- **H2 (explanatory sophistication):** across generations, the backward-looking metrics (§5.2) rise while the forward-looking metrics are flat, *or* forward-looking gains disappear under the information-cutoff control.
- **H0 (no generational effect):** between-generation differences on the forward-looking metrics are no larger than the within-generation variance measured by the repeat-run control (§4, C2).

**Decision rules.**
- H1 is supported if, over ≥3 scored generations, the prediction score (§5.1a) and claim survival (§5.1b) improve monotonically or nearly so *and* the C1 control shows at least half of that improvement retained without window access *and* the difference exceeds the C2 within-model spread.
- H2 is supported if descriptive coverage (§5.2a) rises and the forward-looking metrics do not exceed the C2 spread, or if C1 removes the forward-looking gains.
- H0 is retained if forward-looking differences stay within the C2 spread across ≥3 generations.
- Any pattern not covered above is reported as "indeterminate" with the metrics shown; the protocol does not permit choosing a hypothesis after seeing the metrics.

## 3. Generations

A **generation** is one model (or model family release) that (a) audits its predecessor's framework blind to that predecessor's identity, (b) produces a new framework version, and (c) pre-registers dated, probabilistic predictions before the next evidence window.

| Gen | Model | Framework output | Prediction set | Evidence window it was scored on | Audited by |
|---|---|---|---|---|---|
| G0 | Claude Opus 4.8 (revealed post-audit) | V1 (2026-04-07), V2 (04-20), V3 (05-15), lexicon (05-17) | 20 statements extracted post hoc by G1 (`predictions/G0.json`); none carried probabilities | 2026-05-18 → 2026-09-28 | G1 |
| G1 | Claude Fable 5.1 (configured identifier; see `generations.json`) | V4 (2026-09-30) | 19 pre-registered, probabilistic (`predictions/G1.json`) | 2026-10-01 → (next audit) | G2 (to be assigned) |
| G2 | next model generation | V5 | pre-registered | | G3 |

G0 is a special case: it did not know it was in an experiment, did not pre-register, and its predictions were extracted and scored by its successor. That asymmetry is recorded, not corrected. G1 is the first generation to pre-register; its predictions are the first that can be Brier-scored.

## 4. Controls

Without controls, "generation N+1 scored better than N" cannot be distinguished from "N+1 knew more" or "any second run would have scored better". Each audit cycle runs the following, in this order of priority:

- **C1 — Information-cutoff control (separates reasoning from information).** The auditing model is run a second time on the *same brief* with web access disabled and an explicit instruction to use no evidence dated after the predecessor's last commit. It produces its own framework version and prediction set from the predecessor's evidence alone. If the cutoff run's predictions score as well on the next window as the full run's, the generational gain is reasoning; if they score like the predecessor's, the gain was information.
- **C2 — Repeat-run control (measures within-model variance).** The same model, same brief, same evidence, fresh session, ≥2 runs. The spread of their metrics is the noise floor against which generational differences are judged. No generational claim is made that falls inside this spread.
- **C3 — Cross-model, same-window control (optional, when two current models are available).** Two different model families audit the same predecessor on the same window. Measures whether "generation" or "vendor" explains differences.
- **C4 — Human baseline (optional).** A human researcher given the same brief and window. Not required; recorded if run.

Control runs are stored under `experiment/runs/<generation>/<control>/` with the same file layout as the main run, and are scored with the same script.

## 5. Metrics (pre-defined; computed by `experiment/score.py` where automatable)

### 5.1 Forward-looking (epistemic quality)

| | Metric | Definition | Source |
|---|---|---|---|
| a | **Prediction score** | Brier score over the generation's pre-registered predictions with stated probabilities, scored at the next audit against the stated confirmation/falsification conditions; hit rate reported alongside for generations without probabilities (G0) | `predictions/<gen>.json` |
| b | **Claim survival** | Share of claims in the generation's claim ledger (or framework) whose status is still SUPPORTED or PARTIALLY SUPPORTED at the audit *two* generations later (so each claim is judged twice, by different auditors) | claim ledgers |
| c | **Overclaim rate** | Share of ledger claims flagged `original_stronger_than_evidence` by the next auditor | claim ledger |
| d | **Retraction propagation** | Of claims the generation itself retired, the share still cited as live anywhere in its own later files (grep-able) | corrections + repo text |
| e | **Evidence reproducibility** | Share of the generation's Tier-A / OBSERVED claims that the next auditor could reproduce from primary sources (on-chain, official post-mortem) rather than secondary reporting | audit evidence files |
| f | **Mechanism-embargo compliance** | Count of external-incident mechanisms asserted before an official/forensic post-mortem existed, and how many were later contradicted | audit |
| g | **Citation locatability** | Share of external citations (papers, posts, statements, quotations) the next auditor could locate | audit |
| h | **Base rates measured** | Number of detection signals for which the generation measured a benign-population rate (not merely demanded one) | framework text |
| i | **Calibration** | For generations with probabilities: reliability diagram / expected calibration error over the prediction set (needs ≥20 predictions to mean anything) | `predictions/<gen>.json` |

### 5.2 Backward-looking (explanatory sophistication)

| | Metric | Definition |
|---|---|---|
| a | **Descriptive coverage** | Share of window incidents ≥$1M (DefiLlama or equivalent) that map onto a framework category *without a new category being created* — high coverage with flat 5.1 metrics is the H2 signature |
| b | **Category count and churn** | Number of maneuver categories; share added / removed / broadened per generation |
| c | **Volume** | Bytes of framework and audit prose per ledger claim |
| d | **Hindsight ratio** | From the counterfactual test (Phase 12 of the audit brief): share of changes the auditor itself classified as "hindsight incorporation" vs "reasoning available at the time". Because this is self-reported, the *next* generation re-classifies the previous auditor's changes and inter-rater agreement is recorded |

### 5.3 Reporting rule

Every audit reports all of 5.1 and 5.2 for the generation it audits, in `experiment/metrics/<gen>.json`, before writing any narrative conclusion. Narrative may not cite a metric not in that file.

## 6. Procedure per cycle (~4–6 months)

1. **Freeze.** The evidence window closes at a dated commit. Nothing in the predecessor's files is modified afterwards.
2. **Blind audit.** The new generation receives `experiment/NEXT_GENERATION_BRIEF.md` and the repo, with the predecessor's model identity withheld until Phase 11. It produces the audit artefacts (claim ledger, temporal audit, prediction audit, failure analysis, comparison, final assessment).
3. **Score.** The new generation runs `experiment/score.py` to score the predecessor's pre-registered predictions and to fill `experiment/metrics/<predecessor>.json`.
4. **Re-score.** The new generation *also* re-scores the predictions and claims of the generation two back (survival measured twice, by two auditors).
5. **Build.** The new generation writes V(n+1) and `predictions/<gen>.json` with probabilities and resolution sources, and appends itself to `generations.json` with a SHA-256 of its prediction file and the commit hash.
6. **Controls.** C1 and C2 are run and stored (§4).
7. **Publish.** Commit on a dated branch; merge to `main` only after the pre-registration commit exists.

## 7. Threats to validity (recorded up front)

1. **Training-data contamination.** This repository is public. A later model may have this repo — including outcomes — in its training data, which would inflate its apparent foresight. Mitigation: the C1 cutoff control; comparing the model's stated knowledge cutoff to the window; asking the model at audit time whether it recognises the repository and recording the answer. This cannot be eliminated.
2. **Auditor = subject.** Each generation scores its predecessor and is scored by its successor; a generation could be harsh on its predecessor and generous to itself. Mitigation: two-auditor survival (5.1b), re-classification of the hindsight ratio by the next generation (5.2d), and the C3 cross-model control.
3. **Operator effect.** The same human runs every generation with the same brief. Prompt variation is minimised by using `NEXT_GENERATION_BRIEF.md` verbatim; deviations are logged in `generations.json`.
4. **Domain drift.** DeFi's attack surface changes; a prediction can fail because the world moved, not because the reasoning was poor. Mitigation: probabilistic predictions and the C2 noise floor; predictions phrased about mechanisms and populations, not single events, where possible.
5. **Small n.** Each generation has ~20 predictions; single-cycle differences are not meaningful. The decision rules require ≥3 scored generations.
6. **Self-fulfilment through publication.** Defenders (or attackers) may read the framework and change behaviour. Recorded as a limitation; not controllable.
7. **Metric gaming.** A generation aware of the metrics could register only safe predictions. Mitigation: the brief requires a minimum number of predictions with probabilities in the 0.3–0.7 band (≥5 of ≥15), and the score report shows the probability distribution.
8. **Model identity ambiguity.** The model serving a session can differ from the configured identifier. `generations.json` records the configured identifier and any self-reported serving identity separately.

## 8. What would end the experiment

- H0 retained across three scored generations with adequate n → report "no generational effect on epistemic quality detected" and stop.
- H1 supported across three generations with the C1 control → report and continue at lower cadence.
- H2 supported → report; the interesting follow-up is whether the C1 control can be *taught* (i.e., whether a generation instructed with the previous audit's method notes closes the gap).

## 9. Files

```
experiment/
├── PROTOCOL.md                  this file
├── NEXT_GENERATION_BRIEF.md     the verbatim brief for the next generation
├── generations.json             registry: model identifiers, dates, commits, hashes, blinding attestations
├── predictions/
│   ├── G0.json                  extracted post hoc from V1–V3/lexicon; outcomes scored by G1
│   └── G1.json                  pre-registered 2026-09-30 with probabilities
├── metrics/
│   └── G0.json                  G0 scored by G1 (baseline)
├── runs/                        control runs (C1–C4), same layout as the main audit
└── score.py                     computes 5.1a/c/h/i and 5.2b/c from repo files; templates the rest
```
