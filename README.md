# Maneuvers

**A threat-modelling framework for adversarial DeFi behaviour — and a longitudinal experiment on whether LLM-assisted research gets epistemically better across model generations, or only better at explaining itself.**

## The research question

> Can successive generations of LLM-assisted research improve the epistemic quality of a framework, or do they primarily become better at explaining the framework after more evidence becomes available?

Each generation of model (a) audits the previous generation's framework blind to that model's identity, (b) scores the previous generation's pre-registered predictions against what actually happened, (c) writes the next version of the framework, and (d) pre-registers its own dated, probabilistic predictions for the next generation to score. Controls separate *knowing more* from *reasoning better*. The protocol, hypotheses, metrics and decision rules are fixed in advance in `experiment/PROTOCOL.md`; nothing in the scoring may be chosen after seeing the results.

The framework is the subject, not the point. It was chosen because it makes claims about a world — DeFi exploits — that keeps producing public, dated, post-mortemed events on which claims can be scored.

## State of the experiment

| Generation | Model | Output | Scored on | Result so far |
|---|---|---|---|---|
| **G0** | Claude Opus 4.8 | V1 (2026-04-07) → V3 (2026-05-15), lexicon (05-17) | 2026-05-18 → 09-28, by G1 | 20 post-hoc-extracted predictions, no probabilities: hit rate 0.56 over 13 resolvable; 97 ledger claims: 48% stated stronger than their evidence; 0 base rates measured; 5 mechanisms asserted before post-mortem later contradicted; 3 citations not locatable. Mechanism-level reasoning mostly survived; self-assessment, early mechanism assertions, and topology-only inferences did not. |
| **G1** | Claude Fable 5.1 (configured) | V4 (2026-09-30) + full audit of G0 | 2026-10-01 → next audit, by G2 | 19 pre-registered probabilistic predictions (first resolution 2027-03-31); 0 base rates measured (demanded on every signal, none paid); self-reported hindsight ratio ≈ 0.67; no controls run yet. Verdict on itself: better specification, worse instrument. |
| **G2** | — | V5 | — | Runs `experiment/NEXT_GENERATION_BRIEF.md`; must run controls C1/C2 and pay at least one base-rate IOU. |

Nothing can be concluded about the research question until at least three generations are scored (protocol §2). What exists now is a baseline and a pre-registration.

## Where things are

```
POTENTIAL_ATTACKS_V1_ARCHIVE.md   G0's historical work, unmodified
POTENTIAL_ATTACKS_V2*.md          "
POTENTIAL_ATTACKS_V3.md           "
lexicon.md, docs/lexicon.md       "
CORRECTIONS.md                    G0's own retraction log
reports/                          G0's case files + G1's audit (see AUDIT_README.md for reading order)
V4/                               G1's framework
experiment/
  PROTOCOL.md                     research question, hypotheses, controls, metrics, decision rules
  NEXT_GENERATION_BRIEF.md        the verbatim brief every later generation runs
  generations.json                registry: models, dates, commits, prediction-file hashes, blinding attestations
  predictions/G0.json, G1.json    pre-registered (G1) and post-hoc-extracted (G0) predictions with outcomes
  metrics/G0.json, G1.json        scored metrics; filled before narrative
  score.py                        scoring script
```

## How to read the two frameworks

`V4/README.md` lists six ways V4 can be misread. The one that matters most for this experiment: **OBSERVED in V4 means public, post-mortemed instances exist — not that the framework's own detectors observed anything.** G0's framework used "observed" more loosely; the difference in status semantics is itself one of the things the experiment tracks.

## Contributing a generation

Run `experiment/NEXT_GENERATION_BRIEF.md` verbatim with a new model, on a dated branch, with the previous model's identity withheld until Phase 11. Append to `generations.json`. Do not edit any earlier generation's files.

## Provenance

Repository owner and operator: Jason Trinh (@projectzedai). G0 was produced while operating the Layer 3 surveillance corpus; G1 was produced without access to that corpus. Evidence files in `reports/evidence/` carry provenance headers; model-generated research syntheses are labelled as such.
