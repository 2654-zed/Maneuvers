# Model-to-Model Comparison (Phase 11) and Counterfactual Test (Phase 12)

**Identity reveal.** The independent analysis (Phases 1–10) was completed without reference to which model co-authored the historical corpus. Per the audit brief, the historical collaborator was **Claude Opus 4.8**. The auditing model is the one running this session, configured as `claude-fable-5-1` (the model actually serving a given turn can differ from the configured identifier; nothing below depends on it). Neither identity was used as evidence for or against any claim; the comparison below is between two bodies of work, not two reputations.

**A caution before comparing.** The two bodies of work are not the same kind of thing. The historical corpus was produced *while operating a live surveillance system* over ~7 weeks, with a database, detectors, RPC budgets, a corrections process, and commercial pressure to produce "load-bearing" claims. The audit was produced in ~2 days with no database, no detectors, public sources only, and no commercial pressure — but with five months of hindsight and two research subagents. Most of the differences that follow are explained by those conditions before any difference in reasoning is invoked. Where I claim a reasoning difference, I try to show the reasoning was available at the time.

---

## 1. What did the earlier model see that the audit missed?

1. **The ground-level L2 adversarial economy.** Trap fleets, scanner bots, drainer facilitators, funder clusters, vanity-branded operators — the corpus's actual observation surface. The audit has no visibility into it and carried every such finding at "UNTESTABLE" or "HYPOTHESIZED". That is the right status for *public* evidence, but it means the audit could not evaluate what the earlier model was best at: continuous measurement of a population nobody else was measuring. Some of those findings are probably right (CE5E may well be a drain operation; the corpus saw approvals land hours before pulls and saw payers with no prior history), and the audit's structural doubts do not resolve them.
2. **Kill-switch governance as a first-class defensive object** — proposed in May on one instance (THORChain's Mimir); by Q3 it was the dominant recovery mechanism. The audit would not have elevated it from one case.
3. **Cross-domain compositional harm** — connecting a SaaS OAuth breach (Vercel/Context.ai) to the same structural class as on-chain composition. The audit would have scoped itself to DeFi and missed the analogy; the Bitget mechanism (third-party product → internal credentials → forged requests) is exactly the cross-domain pattern the earlier model named in April.
4. **Confused deputy for agents** — added in May on one incident; three more Bankr incidents and a vendor forecast followed.
5. **Advisor-parasite / micro-cost habituation** — an economic-psychological hypothesis the audit would not have generated. It remains untested, not wrong.
6. **Participatory asymmetry** — that the Kelp configuration was public and the *literacy* was not. The audit treats this as obvious in hindsight; in April it was a precise diagnosis of why "publicly readable" did not mean "seen".
7. **The Tornado-funded fresh recipient** and the channel-level `lzReceive` outlier idea. The audit dismissed the first on base-rate grounds; the earlier model's own report already said the rule "isn't a rule we have today" and framed it as needing a baseline. The audit under-credited that hedge.
8. **Primary measurement per claim.** The earlier model replayed `getConfig` at five blocks, traced funding with explicit RPC accounting, probed DVN nonces, and published a gap inventory with cost estimates. The audit reproduced the Kelp reads and one facilitator address and otherwise relied on subagent-gathered secondary sources. Per claim, the earlier model did more original verification than the audit did.

## 2. What did the audit identify that the earlier model missed?

1. **The base-rate problem, generalised.** Fanout ⇒ adversary, dormancy ⇒ staging, self-settlement ⇒ theft, prefix collision ⇒ control, mainnet history ⇒ laundering, `TIMESTAMP` ⇒ kill switch, low reverts ⇒ calibration. The earlier model discovered this failure on its own data (Correction #20, 05-09) and did not propagate it to the other signals. Available at the time.
2. **Circularity in the validation narrative.** "6-of-14 observed" counted categories defined from incidents as observations of predictions. V3's "predicted the May wave" cited a hook (initializer enumeration) that V2 did not contain. Detectable at the time by diffing V2 against V3.
3. **Mechanism embargo.** V3 held THORChain at "TBD"; the lexicon two days later asserted a mechanism from the most recent public bug report. The earlier model *had* the discipline and dropped it under narrative pressure. Detectable at the time.
4. **Citation integrity.** The Blockaid "January 2026" prediction, the Immunefi "April 18" response, and the Aethir dev.to quotations could not be located. The audit records these as NOT FOUND, not fabricated — the web-search budget ran out before an exhaustive search — but three unlocatable citations in load-bearing positions is a pattern. The Drift "Tether froze $127.5M" error was contradicted by press on the day the plan was announced.
5. **Notional vs realised loss** as an ontology slot, not a bug fix. The earlier model caught the $3.1-quadrillion decimals error and did not generalise it.
6. **Exposure vs discharge.** 47% of OApps 1-of-1 (measured 04-20 by Dune) against one exploit; the question "why only one?" leads to actor economics, which the earlier model never modelled. Available at the time.
7. **Propagation failure of its own corrections.** Retired figures (the trust-amplification multiplier, "GoPlus 0/50", victim-to-predator) still cited as live in the lexicon that post-dates the retirement — and the Binance-hot-wallet finding never applied to the org_001 claims that depend on it.
8. **The under-weighting of verifier code bugs.** Attack 10 was filed as "audit-catchable, belongs in the audit market"; it produced the largest notional bridge losses of the window. This one needed the window to see (§7).

## 3. Where was the earlier model more disciplined?

- **Explicit "What this file does NOT claim" sections** in every report; the audit has no equivalent per file (it has one red-team file).
- **Negative results published**: Pattern B 0 candidates; advisor-parasite negative; "none of the attacks above are in the Observed category" (V1).
- **Refusing the overclaim in writing**: "Layer 3 would have prevented Kelp" — struck through, with the reason.
- **Budgeted verification**: RPC calls allocated and accounted for per phase.
- **Severity-rated corrections** with discovery method and fix commit — a process the audit only *inherits*.
- **Attribution restraint on Kelp** ("not established") — correct for five weeks until LayerZero's report.
- **Operational specificity**: hooks were written as queries and thresholds (`getConfig(configType=2)`; `requiredDVNCount < 2`; `>$10M`), which is why the ecosystem's independent adoption of the same check is checkable at all. The audit's V4 signals are mostly prose.

## 4. Where did the earlier model overreach?

- Mechanism assertion before post-mortem (THORChain; Aethir).
- Validation narratives built on category drift (V2) and retro-fitted hooks (V3).
- Typology promotion from topology alone (Infrastructure-Scale Operator; Pristine Solo Operator; Single-Purpose Funder; Self-Deploying Mass-Drain's org_001 attribution the day after Correction #20).
- Lexicon "empirical grounding" bullets that cite decks, absent files, retired figures and unlocatable quotations at Tier-A confidence.
- Metaphor stacking (physics → games → warfare) presented as "operational doctrine", with the last entry (Hybrid Gameboard) grounded on a wrong mechanism and an internally contradicted case.
- The universal quantifiers: "Every successful exploit in the corpus traverses these phases in order"; "every major DeFi exploit demonstrates this hybrid nature"; "none would have been possible on Bitcoin's UTXO model".
- Commercial framing leaking into epistemic status ("Tier A claims are load-bearing in pitches").

## 5. Where did the audit overreach?

- **CE5E.** The first draft of M-17 said "low [confidence] that it is theft". That inverted the burden: the audit cannot see the exposure-tracker evidence the corpus had. Corrected to "not established either way" before commit; recorded here because the impulse to over-correct a corpus one has just found overclaiming is itself a bias.
- **`0x80b12bd0` H3 (token migration).** Raised as a competing hypothesis with no evidence for it beyond the absence of a public incident. Legitimate as a hypothesis; the audit should not be read as endorsing it.
- **"None of V1's eight hypotheticals occurred."** Overstated: no *public* instance. Small routing parasites or probe traps could exist unreported; the corpus's entire premise is that such things exist below public reporting thresholds.
- **Dollar aggregates for the window.** Quoted from DefiLlama labels with empty source fields, then used to rank classes ("~$385M verification bugs vs ~$0.7M configuration"). The ranking is robust to ±50%; the numbers are not facts.
- **Reliance on subagent research.** Two verification reports and the post-revision survey are model-generated secondary syntheses; the audit reproduced on-chain only what it could (Kelp, Tornado, CE5E). An earlier-model reader could fairly say the audit's evidence base is one step further from primary than the corpus's own.
- **Volume.** The audit produced ~250 KB of prose to evaluate ~600 KB of prose. Length is not rigour, and the audit's structure (ledger → audits → V4 → red-team → comparison) repeats findings across files.

## 6. Mistakes both approaches share

- Both rely on secondary incident reporting for mechanisms they did not reproduce (the corpus on press; the audit on vendor post-mortems and DefiLlama).
- Neither computed a single benign base rate — the corpus never asked; the audit only demanded.
- Both decompose incidents into phases/maneuvers after the fact; both are narrative instruments.
- Both are fluent category-generators. The audit's 27 maneuvers are no more "observed" by the audit than the corpus's 14 attacks were by Layer 3; the audit's status vocabulary is stricter, not its access.
- Both under-model actor cost; V4 names it (M-27) without measuring it.
- Both are written by models that produce confident prose faster than they produce verification; the corpus's unlocatable citations and the audit's ±50% aggregates are the same failure at different scales.
- Both treat DPRK attribution from TRM/Elliptic/Mandiant as settled.

## 7. Which differences are caused by new evidence?

| Difference | New evidence that caused it |
|---|---|
| M-07 (TSS participant) replaces Attack 15 | THORChain reports (05-20, 07-03) |
| Kelp mechanism = RPC poisoning, keys intact | LayerZero report (05-18) |
| M-02 re-ranked above M-01 by realised loss | Q3 bridge wave (Gravity, Secret, Wanchain, Verus, Liquid, Nomic, Symbiosis) |
| Signing-pipeline mode in M-03 | Bitget (09-24) |
| M-10 weak key generation | Coldcard (07-30); re-characterised April-30 drain |
| Config-role capture in M-01 | Sandbox (08-21) |
| Vote-capture mode in M-05 | BonkDAO, Term, Neutron |
| Stale-valuation and signer modes in M-06 | Lazy Summer, Ostium |
| M-13 as dominant recovery mechanism | Cronos, Harmony, Cosmos Hub, Liquid, Taiko |
| Strategy-lifecycle timing dropped | Observed lags 30–95 days |
| Aethir anchor removed | Post-mortem search (could have been done in April) — borderline |
| Drift recovery arithmetic corrected | Press of 04-16/17 — *not* new evidence; a sourcing error |

## 8. Which differences result from reasoning?

| Difference | Why it is reasoning, not information |
|---|---|
| Base-rate obligation on every signal | The corpus discovered the problem itself (05-09) and had the data to test the other signals |
| "6-of-14 observed" rejected as circular | Requires only V1 and V2 texts |
| "V2 predicted the May wave" rejected | Requires only diffing V2 and V3 |
| Mechanism embargo | V3 practised it; the lexicon abandoned it two days later with no new evidence |
| Notional / realised as ontology | The decimals correction was the cue |
| Exposure vs discharge → actor economics | Dune's 47% was measured 04-20 |
| Propagation of retirements | The corrections index says it is "supreme"; the lexicon ignored it |
| Citation integrity | Not checking whether a quoted post says what is quoted |
| Removing metaphors from "empirical grounding" | Judgement, not evidence |
| Status refers to public instances | A definitional choice the corpus's own status legend already implied ("full chain seen end-to-end") and then ignored |

Honest weighting: the *content* changes in V4 (new classes, re-rankings, sub-modes) are mostly information. The *method* changes (base rates, embargo, notional/realised, status semantics, actor economics) are mostly reasoning — and most of them are demands V4 places on future work rather than measurements V4 performs.

## 9. Did the newer model improve the framework, or produce a more sophisticated explanation?

Split answer, because the question conflates two things.

**As a specification**, V4 is better: it removes claims the corpus itself had retired, drops two classes with no surviving anchors, adds three classes the window demonstrated (TSS participant, weak keys, defender halt/rollback), gives every signal a benign-population note, separates notional from realised, and ties epistemic status to public instances. These are structural fixes, not re-descriptions.

**As an instrument**, V4 is worse than V3 was in May: V3 ran on a live corpus with detectors and produced measurements; V4 runs on nothing. Every base-rate note is an IOU. V4's maneuver list is longer (27 vs 14 + candidate) and its prose is more careful, which is exactly what "a more sophisticated explanation" looks like from the outside. The test that separates the two is whether V4's obligations get paid: if the benign-cohort baselines, the population pass-through audit, and the initializer census are never run, V4 will have been the more sophisticated explanation and nothing more.

**On predictive content**, V4 makes fewer claims about its own foresight than V3 did, and it commits to dated predictions (`final_assessment.md` §V4 predictions) so it can be audited the way V1 was. That is an improvement in *auditability*, which is the only kind of improvement this exercise can certify from inside.

## 10. Historical concepts that remain surprisingly durable

- **Configuration-level vulnerability** (a class, publicly readable, bounty-out-of-scope) — the ecosystem built the monitor and changed the defaults.
- **Pooled custody amplification** — the notional/realised natural experiments (Sandbox, Symbiosis, Liquid) are cleaner confirmations than anything the corpus had in April.
- **Neutrality Trap phase 4 / Normative Shell Game / Kill-Switch Governance** — chain-level halts and rollbacks became the story of Q3 recovery, including the legitimacy fight (SDNY over frozen ETH).
- **Operational-layer dominance by value** — held through H1 and most of Q3.
- **Verification-path trust failure** as a seam — Ostium, Bonzo, Nostra, Wanchain, Bitget.
- **Bug-bounty structural gap** — Ostium's out-of-scope keeper; Cosmos Labs' mis-triage.
- **The corrections-log posture** — the retractions it made were the right ones; the audit's largest single source of disconfirmations is the corpus's own log.
- **Uninitialized-proxy enumeration** — confirmed in 48 hours (though added post hoc).
- **Confused deputy for agents** — early and right on mechanism.

## 11. Concepts that aged poorly

- **Thermodynamic Fundamentalism** — anchors retracted; not a maneuver concept.
- **The Hybrid Gameboard** — grounded on a wrong mechanism and a contradicted case within days of being written.
- **Static vs Dynamic Behavior** — Liquid and Coldcard.
- **Strategy Lifecycle's 15-day clock** — n=2 curve fit.
- **Infrastructure-Scale Operator / Pristine Solo Operator** as behavioural detectors — retracted by the corpus; the audit only records it.
- **Victim-to-Predator Pipeline** — retired, retained, now removed.
- **Time-lock synchronized fire as "highest-leverage"** — nothing in five months, while the deprioritised class produced the losses.
- **The validation narratives** (V2 "6-of-14", V3 "predicted the surface") — the parts of the corpus written for external audiences aged worst.
- **Maneuver Primitives as law** — Coldcard, Liquid and Aztec do not fit without forcing.

## 12. Did the original framework contain genuine predictive value?

Yes, in a narrow band, and the band is identifiable. `prediction_audit.md` finds four confirmed predictions with content (config-monitor lead time as fact; override proliferation; lock-release > mint-burn; DVN-config detectors emerging), three partial (1-of-1 exposure; ops-layer by value; replication without the clock), five falsified (30-day copies; THORChain paths; V2/V3 self-validation; the 15-day scale), five unresolved because outcomes went unrecorded, and three non-falsifiable.

The genuinely predictive content is concentrated where the corpus reasoned from *mechanism* (custody architecture; publicly readable thresholds) or from *incentives* (protocols will sacrifice neutrality under loss), and it fails where the corpus reasoned from *recency* (THORChain), *narrative* (six phases; four games), or *self-assessment* (validation claims). That pattern is more useful than the score: it says which parts of a framework like this to trust next time.

---

# Phase 12 — Counterfactual test

**Setup.** Pretend the corpus was produced today (2026-09-30) and strip all knowledge of 2026-05-18 onward. Which of its conclusions would still be justified on the April–May evidence alone? Then add the window back: which conclusions genuinely change? Each item is tagged with what the change *is*: **framework improvement** (a structural fix available without the window), **hindsight incorporation** (a change the window forced), **historical validation** (the window confirmed what was already justified), or **retrospective storytelling** (a change that only looks compelled because we know the ending).

## 12.1 Justified on April–May evidence alone (no window needed)

| Conclusion | Why it was justified then |
|---|---|
| Configuration-level vulnerability is a monitorable class with lead time | The `getConfig` replay was Tier A and reproducible; Blockaid published the same check the same day |
| Pooled custody amplification | Mechanical argument from lock-release semantics; Kelp/Aave composition already observed |
| Operational-layer attacks dominate by value | Bybit ($1.5B) and Drift ($285M) already dominated 2025–26 value; the generalisation was sound |
| Neutrality-trap override direction | DAO fork, issuer freezes, and the Arbitrum freeze (04-20) were in hand |
| Initializer enumeration | Renegade (05-10) was post-mortemed by Blockaid the same day |
| Verification-path trust failure as a seam | Drift/Rhea/Kelp sufficed for the descriptive claim |
| "Mechanism TBD" for THORChain (V3's version) | No post-mortem existed; the hedge was correct |
| "Not established" for the Kelp DVN operator | Correct restraint |
| Corrections #1–#20 | All discovered on the corpus's own data |

## 12.2 Not justified even then — reasoning errors detectable at the time

| Conclusion | What was available to catch it |
|---|---|
| "6-of-14 observed validates combinatorial modelling" | V1's text: none of its eight chains occurred as written |
| "V2 predicted the May wave" | V2 contains no initializer hook |
| Lexicon's THORChain bit-flip mechanism (05-17) | No post-mortem; V3's own hedge two days earlier |
| Aethir "private-key compromise per the dev.to post-mortem" with quotations | The post does not say it |
| Drift "Tether froze $127.5M"; "Solana Foundation $20M" | CoinDesk/Fortune 04-16/17 described a credit facility |
| Fanout / dormancy / self-settlement / prefix ⇒ adversary | Correction #20's own lesson, generalisable on 05-09 |
| Strategy lifecycle "15 days" | n=2 |
| Victim-to-predator retained in lexicon | Retired 04-02 |
| Retired multiplier and "GoPlus 0/50" cited live | Retirement index dated 04-02 |
| Hybrid Gameboard grounded on `0x80b12bd0` as a detection success | Same lexicon retracts the flag as an FP |
| "Every exploit traverses six phases" | Unfalsifiable by construction |

These are the items an auditor *without* the window should have flagged. They are the audit's clearest evidence of a reasoning gap rather than an information gap.

## 12.3 Genuinely changed by the window

| Change | Tag | Compelled by |
|---|---|---|
| M-07 malicious TSS participant | hindsight incorporation | THORChain reports |
| Kelp mechanism = poisoned inputs, keys intact → verifier *input* integrity as a variable | hindsight incorporation | LayerZero report |
| M-02 re-ranked above M-01 by realised loss; "audit-market only" reversed | hindsight incorporation | Q3 bridge wave |
| M-10 weak key generation as a class outside the node ontology | hindsight incorporation | Coldcard |
| Signing-pipeline mode without key theft | hindsight incorporation | Bitget |
| Config-role capture as a sub-mode | hindsight incorporation | Sandbox |
| Vote-capture-without-timelock as the dominant governance mode | hindsight incorporation | BonkDAO, Term, Neutron |
| Halts/rollbacks as *the* recovery mechanism | historical validation (direction) + hindsight (magnitude) | Cronos, Harmony, Cosmos Hub, Liquid |
| Exposure/discharge gap → actor economics | partly reasoning (Dune 04-20 existed), partly hindsight (no second discharge over five months) | — |
| Strategy-lifecycle clock removed | hindsight incorporation | observed lags |
| AI-agent class confirmed on mechanism, small on magnitude | historical validation | Bankr ×2 more |

## 12.4 Historical validation (the window confirmed what §12.1 already justified)

Config class (ecosystem adoption, default changes); pooled custody (notional/realised experiments); ops-layer by value (H1 statistics); override direction (Q3); initializer enumeration (Aurellion); bug-bounty gap (Ostium, Cosmos Labs).

## 12.5 Retrospective storytelling — where the audit must check itself

- "The corpus *should* have prioritised verifier code bugs." Only visible with Q3. In May, Attack 10's one instance ($237K→$2.5M) against Attack 9's $292M made the corpus's ranking reasonable. The audit's re-ranking is hindsight, and V4 says so.
- "The corpus should have modelled actor economics." The exposure number existed in April, but the *discharge* half of the gap needed months of no second exploit. Half reasoning, half hindsight.
- "Kill-switch governance was prescient." The corpus proposed it on one case; the audit elevates it on five. The elevation is hindsight; the proposal was judgement.
- "THORChain shows the corpus reasoned from recency." True — but the audit can only *prove* it because the post-mortem exists. Without it, the audit would have flagged the lexicon's mechanism as unsupported, not wrong.

## 12.6 What the counterfactual establishes

Roughly a third of what changed between V3 and V4 was available to the earlier model on its own evidence (§12.2 and the method items in §8). Roughly two-thirds needed the window (§12.3). The window *validated* more of the corpus than it *refuted* (§12.4 vs the falsified predictions), which is the fairest one-line summary of the historical work: its mechanism-level reasoning mostly survived; its self-assessment, its mechanism assertions ahead of evidence, and its topology-only inferences did not.
