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

## V4 predictions (dated 2026-09-30, for the next audit)

So that V4 can be audited the way V1 was, it commits to the following. Each has a confirmation and a falsification condition; none is a hedge.

| ID | Prediction | Confirmed if | Falsified if |
|---|---|---|---|
| PV4-1 | No exploit of a *pre-existing* (not attacker-created) sole-required-DVN LayerZero configuration with >$10M reservoir by 2027-03-31 | none occurs | one occurs |
| PV4-2 | Cross-chain verification code defects (M-02) exceed attestation-configuration failures (M-01) in *realised* losses for 2026-10-01 → 2027-03-31 | M-02 realised > M-01 realised | M-01 realised > M-02 realised |
| PV4-3 | At least two further public unprotected-initializer / uninitialized-facet takeovers (M-04) by 2027-03-31 | ≥2 post-mortemed instances | <2 |
| PV4-4 | Chain- or protocol-level halt/rollback used in ≥3 incidents ≥$5M by 2027-03-31, and at least one contested in governance or court | both conditions | either fails |
| PV4-5 | At least one further malicious-participant TSS attack (M-07) on a production threshold-signing network by 2027-09-30 | one post-mortemed instance | none |
| PV4-6 | No public instance of time-lock synchronised fire (M-22) or routing parasite (M-19) by 2027-09-30 | none | one occurs — which would rehabilitate V1's combinatorial method |
| PV4-7 | AI-agent maneuvers (M-09) remain below $25M cumulative realised for 2026-10-01 → 2027-09-30 | below | above — which would mean the corpus's "supercharger" claim was right on magnitude and V4 too conservative |
| PV4-8 | At least one governance drain (M-05) succeeds *through* an execution timelock (i.e., delay present, not bypassed) by 2027-09-30 | one occurs | none — which would strengthen "no delay" as the load-bearing precondition |
| PV4-9 | The facilitator address `0xce5ec733…c91` is either publicly identified as a payment/settlement service or publicly reported as a drainer by 2027-03-31 | either | neither — the ambiguity itself persists, and M-17 stays HYPOTHESIZED |

**Falsification criterion for V4 as a whole.** If PV4-1, PV4-2 and PV4-4 all fail, the reservoir–trigger–constraint core is not tracking where losses come from, and the framework should be treated as descriptive only.

## Closing statement

The historical work reasoned well about mechanisms and incentives, kept an honest corrections log, and did more primary verification per claim than this audit did. It reasoned badly when it narrated mechanisms ahead of evidence, inferred adversaries from topology alone, and assessed its own predictive record. The passage of time validated more of its structure than it refuted, falsified its clock and its self-assessment, and exposed one class of failure (verifier code bugs) it had filed away as someone else's problem. The newer analysis improved the specification and made the framework auditable; it did not build the instrument, and it will not have improved the framework until someone pays the measurements V4 now owes.
