# Prediction Audit — Maneuvers V1–V3 and the Layer 3 Lexicon

**Audit date:** 2026-09-28. **Rule applied:** a statement counts as a prediction only if, at the time it was written, a specific future observation could have confirmed or falsified it. Vague statements are labelled `NON-FALSIFIABLE / TOO BROAD` and are not converted into successes after the fact. Where the corpus made a prediction *about its own private data* (cadence forecasts), the outcome is "unresolved" unless the repository records it — I do not assume it fired because it would flatter the framework, or that it failed because it would flatter the audit.

Outcome vocabulary: CONFIRMED · PARTIALLY CONFIRMED · FALSIFIED · UNRESOLVED · NON-FALSIFIABLE / TOO BROAD. Strength: strong / moderate / weak, with the reason.

Evidence references: `reports/evidence/*` and `reports/claim_ledger.md` (C-numbers).

---

## Dated, explicit predictions

### P-01 — Oracle-manipulation copies within 30 days
- **Original:** "Expect further copies within 30 days per the strategy_lifecycle model." (`reports/extraction_event_004_rhea_finance.md`, 2026-04-18; family = fake token + manipulated oracle + lending drain)
- **Confirmation:** a public fake-collateral/oracle-manipulation lending exploit between 2026-04-18 and 2026-05-18.
- **Falsification:** none in that window.
- **What happened:** none in the window (V3 itself records "No v3 additions" for Attack 12 on 05-15). Next public instances: Bonzo 07-11, Lazy Summer 07-05 (stale valuation), Moonwell 08-27, Tectonic 08-30, Nostra 09-17.
- **Outcome:** FALSIFIED (timing); the family did recur after ~80 days.
- **Strength:** moderate — the window and the class were both explicit.
- **Remaining uncertainty:** whether the corpus would count a $359K oracle-misconfiguration (Silo) as a "copy"; it did not, and neither do I.

### P-02 — Drainer-spawn hub iteration 9
- **Original:** "Forecast iter_9 (2026-05-07 ~10:02 UTC) is the next falsifiability test." (lexicon, *Convergent Calibration*, 2026-05-05; hub `0xf7883e3fef23…`)
- **Confirmation:** a new drainer wallet spawned by the hub within ±30 min of 2026-05-07 10:02 UTC.
- **Falsification:** no spawn within, say, ±6 h.
- **What happened:** the repository does not record the outcome; the hub address is public but the "iteration" definition depends on Layer 3's drainer classification, which I cannot reproduce without the corpus. No public reporting.
- **Outcome:** UNRESOLVED.
- **Strength:** n/a. **Note:** this is the best-formed prediction in the corpus — dated to the minute, with a stated tolerance. That its outcome was not recorded in the 05-15/05-17 files (which post-date it by 8–10 days) is a process failure the corpus's own conventions ("re-scan trigger", "correction-log-triggering event") should have prevented.

### P-03 — Fourth self-deploying mass-drain instance
- **Original:** "If the cadence is real, expect a fourth instance within 1-3 days of III; if absent for >5 days, the cadence framing weakens." (lexicon, *Self-Deploying Single-Contract Mass-Drain*, 2026-05-10; III = 2026-05-09/10)
- **Confirmation:** a fourth instance by 2026-05-13. **Falsification:** none by 2026-05-15.
- **What happened:** not recorded; V3 (05-15) and the lexicon (05-17) are silent.
- **Outcome:** UNRESOLVED. The silence after the stated 5-day window is weak evidence for the "cadence framing weakens" branch, but I will not convert silence into a result.

### P-04 — THORChain mechanism resolution paths
- **Original:** THORChain "resolves" to (1) validator-attestation forgery → Attack 9, (2) proof/attestation code defect → Attack 10, (3) validator-key operational compromise → Attack 11a, or (4) a native-swap settlement asymmetry → Attack 15. (V3, 2026-05-15)
- **Confirmation:** post-mortem matches one of the four. **Falsification:** post-mortem matches none.
- **What happened:** Exploit Reports #1 (05-20) and #2 (07-03): a bonded validator exploited a GG20 threshold-signature library flaw (malformed Paillier modulus; 864 deliberate MtA failures over 2.5 days) to reconstruct the vault key and sign directly.
- **Outcome:** FALSIFIED — none of the four. Closest is (2) if "attestation code" is stretched to "signing-protocol code", but the defining feature (an *insider participant* extracting key shares through protocol interaction) was not enumerated.
- **Strength:** strong — the enumeration was explicit and exhaustive by design ("three resolution paths … if, however, … a fourth pattern"). The corpus deserves credit for hedging; it does not get credit for coverage.
- **Remaining uncertainty:** whether Maya Protocol (08-18, $1.7M) is a second TSS instance (a THORChain podcast references a TSS fix "discovered and tested first by Maya"; unverified).

### P-05 — Kelp-class population risk
- **Original:** "any adapter holding >$10M in pooled deposits with a 1-of-1 DVN is a pre-validated Kelp-class risk"; "LayerZero OApp ecosystem has many deployments; DVN configurations vary. Industry-wide exposure." (V2 Attack 9, 2026-04-20)
- **Confirmation:** measured population of 1-of-1 OApps is large; and/or a second exploit of such an OApp.
- **Falsification:** population negligible, or no further discharge over a long horizon despite exposure.
- **What happened:** Dune (04-20): 47% of ~2,665 active OApps 1-of-1, 45% 2-of-2 — exposure confirmed. No second exploit of a *pre-existing* 1-of-1 OApp before LayerZero forced defaults to 3-of-3 (07-09); The Sandbox (08-21) is a config-role capture that *created* the 1-of-1 condition. Stake DAO (05-27, $91K) is listed by OAK as an OFT peer-config redirect (contested).
- **Outcome:** PARTIALLY CONFIRMED — exposure was real and large; repeat discharge did not occur, and the ecosystem removed the condition within ~80 days.
- **Strength:** moderate. **Uncertainty:** whether the absence of a second exploit reflects attacker preference, LayerZero's DVN-side refusal from 04-19, or simply that the one operator (LayerZero Labs) whose RPC was poisoned was the sole required DVN for most 1-of-1 OApps.

### P-06 — Operational-layer attacks dominate 2026
- **Original:** "2026 attacks will target operational layers around key management, not the keys themselves" — attributed to Blockaid, January 2026, and adopted: "empirically validated across Q2." (lexicon, *Operational Layer Attack*)
- **Date of prediction:** the attribution is NOT FOUND (`verification_april_wave` §10). As a corpus prediction it dates from 2026-04-18/20.
- **Confirmation:** value-share of 2026 losses attributable to key management / operational infrastructure exceeds that of code defects.
- **Falsification:** code-defect losses dominate.
- **What happened:** Blockaid H1 (07-28): 74% of stolen value from operational/infrastructure compromise. TRM H1: ~76% of funds from infrastructure compromises (~15% of incidents). Q3: Bitget $387.5M (signing-pipeline), Coldcard $116M (key generation), Liquid $320M (verification code) — mixed.
- **Outcome:** CONFIRMED by value for H1; PARTIALLY CONFIRMED for the window as a whole (Q3's largest losses split between ops-layer and verification-code failures).
- **Strength:** moderate — the prediction is broad ("operational layers") and its source cannot be verified; the *specific* phrase "not the keys themselves" is oddly prescient of Kelp (RPC poisoning, keys intact) and Bitget (request spoofing, keys intact), but I cannot establish it was written before those events by anyone.

### P-07 — Time-lock synchronized fire will appear
- **Original:** "Remains the highest-value speculative category"; "building the T-value calendar is still the highest-leverage addition." (V1 04-07; V2 04-20; V3 05-15)
- **Confirmation:** a coordinated fleet whose behaviour flips at a shared timestamp. **Falsification:** not strictly possible ("speculative"); a long horizon with no instance is weak disconfirmation.
- **What happened:** no instance through 2026-09-28.
- **Outcome:** NON-FALSIFIABLE / TOO BROAD as written; weakly FALSIFIED as a priority call (the class the corpus ranked highest-leverage produced nothing while the class it ranked audit-market-only produced ~$385M).

### P-08 — Advisor-parasite candidates will surface with corpus age
- **Original:** re-scan triggers "(a) corpus age ≥ 90 days, (b) Transfer-event indexer deployed ≥ 30 days, (c) infrastructure_registry ≥ 50 entries." (V2/V3 Attack 14; lexicon Pattern F)
- **Confirmation/Falsification:** a re-scan at ≥90 days finding / not finding candidates.
- **What happened:** the corpus passed 90 days on ~2026-06-15; no re-scan is recorded.
- **Outcome:** UNRESOLVED. NON-FALSIFIABLE as written (triggers, not forecasts).

### P-09 — Strategy Lifecycle: EARLY → ARMS_RACE within ~15 days
- **Original:** "Within weeks, independent operators replicate the pattern with variations"; "Drift → Rhea = 15 days"; "9 days for three orthogonal variants." (lexicon)
- **Confirmation:** new public technique families replicated by independent operators within ~2–4 weeks.
- **Falsification:** replication lags routinely exceed the window, or "replication" is the same operator.
- **What happened (families first seen in the historical window):** uninitialized-proxy takeover: Renegade 05-10 → Aurellion 05-12 (2 days; possibly one actor). TSS/GG20: THORChain 05-15 → Maya 08-18 (95 days; link unverified). Config-role capture: Stake DAO 05-27 → Sandbox 08-21 (86 days; first instance contested). Governance no-timelock: BonkDAO 07-06 → Term 08-23 → Neutron 09-22 (48, 30 days). Same-flaw recurrence: Verus 05-17 → 07-22 (66 days, same bug). Fake collateral: Rhea 04-16 → Bonzo 07-11 (86 days).
- **Outcome:** PARTIALLY CONFIRMED (replication is real) / FALSIFIED (the 15-day scale; lags of 30–95 days dominate).
- **Strength:** moderate. **Uncertainty:** the corpus never defined how to distinguish independent replication from one actor or from base-rate coincidence at ~30 incidents/month.

### P-10 — Kelp-class configuration monitor would have fired ≥56 days early "with zero ambiguity"
- **Original:** "A continuous DVN-configuration monitor pointed at Ethereum LayerZero OApps would have flagged this at block 24,500,000 or earlier with zero ambiguity." (Kelp replay, Phase 3)
- **Confirmation:** the read reproduces (it does — `onchain_checks` §2). **Falsification:** the read does not reproduce.
- **Outcome:** CONFIRMED (the read). But it is a retrodiction, not a prediction, and "zero ambiguity" ignores that the same rule flagged ~1,250 OApps; the corpus's own >$10M TVL filter is what would have made it actionable.
- **Strength:** strong for the fact; n/a as foresight.

### P-11 — V3's validation claim: "v2 … predicted the surface that produced these events"
- **Original:** "Pre-deployment, the framework would have flagged Wasabi (EOA-admin perp adapter), Renegade (unprotected-initializer proxy), and the cross-chain surface generally." (V3, 2026-05-15)
- **Test:** does V2 (04-20) contain a hook that would flag each named event before it occurred?
- **What happened:** Wasabi — V2 lists "single-contract high-stored-potential adapters where admin is an EOA without multisig or timelock" (derived from Aethir, whose EOA premise is unverified): plausible hit at the category level. Renegade — V2 contains no initializer check; it was added in V3 *after* Renegade. "Cross-chain surface generally" — too broad to fail. Volo (Sui key compromise) fits the EOA-admin category; Juicebox and Thetanuts were mislabelled to fit.
- **Outcome:** PARTIALLY CONFIRMED (Wasabi, category level) / FALSIFIED (Renegade) / NON-FALSIFIABLE (cross-chain surface).
- **Strength:** strong for the Renegade finding — the V2 text is in the repository and does not contain the hook.

### P-12 — V2's validation claim: "6-of-14 observed … validated the combinatorial threat-modeling approach"
- **Original:** V2 cross-cutting notes, 2026-04-20.
- **Test:** did any V1 hypothetical (04-07) occur as specified?
- **What happened:** none of Attacks 1–8 occurred as specified through 2026-09-28. Attack 2 was "validated" only by dropping the fleet/coordination/self-destruct elements. Attacks 5, 9–13 were defined from the incidents they are said to have observed.
- **Outcome:** FALSIFIED as a validation of *combinatorial* modelling. What the April wave validated was the lexicon's *failure-layer* classification (code/config/ops), which is descriptive.

### P-13 — Neutrality-trap override / kill-switch proliferation
- **Original:** "Over time, the damage forces the introduction of centralized governance (freeze authorities, emergency multisigs, social forks)"; "what fraction of cross-chain protocols have a parameter-level kill switch reachable in <1 hour" is "worth modeling broadly." (lexicon, 2026-04-20 and 05-15)
- **Confirmation:** increasing frequency of chain- or protocol-level overrides after losses. **Falsification:** losses absorbed without overrides.
- **What happened:** Cronos rollback (08-30, reversing $111M), Harmony rollback (08-11), Cosmos Hub halt (09-22), Liquid pause/split (09-06), Taiko halt (06-21), Osmosis freeze (09-09), THORChain halts (05-15), Arbitrum freeze (04-20) and the SDNY fight over it.
- **Outcome:** CONFIRMED in direction. **Strength:** moderate — broad, but stated before the Q3 pattern and grounded in an incentive argument rather than an incident.

### P-14 — Pooled custody produces more realised harm than mint-burn
- **Original:** lock-and-release adapters are "the highest-stored-potential cross-chain architecture"; mint-burn exploits yield tokens whose "market value collapses as the fraud is realized." (lexicon, 2026-04-20)
- **Confirmation:** later incidents show realised losses concentrated in custody releases and mint exploits realising a small fraction of face value.
- **What happened:** Sandbox — 329T SAND minted (~$49B face), $675K realised, almost all from draining the Ethereum lock-release adapter; Symbiosis — 46B syBTC minted from $0.25, $336K realised; Hyperbridge — 1B DOT minted, ~$2.5M realised; Secret, Gravity, Liquid, Nomic — custody/escrow/reserve releases were the realised losses.
- **Outcome:** CONFIRMED. **Strength:** strong — a specific mechanical claim with a clean natural experiment.

### P-15 — Agentic AI will multiply confused-deputy incidents
- **Original:** "Agentic AI supercharges [the Confused Deputy]." (lexicon, May 2026)
- **What happened:** Bankr May 19 (14 wallets, session keys), Bankr Jul 25 (X takeover), Blockaid H2 forecast naming prompt injection/tool-use abuse, TRM: AI use in crypto crime +40% YoY; total AI-agent losses in the window ≈$1M.
- **Outcome:** PARTIALLY CONFIRMED (frequency up; magnitude small). **Strength:** weak — the statement had no threshold.

### P-16 — Camouflage ratio remains stable at 70–79%
- **Original:** "Stable at 70–79% across chains, organizations, and time." (lexicon)
- **What happened:** the corpus's own 04-29 robustness check reported 67.1%/68.1%; nothing external tests it.
- **Outcome:** UNRESOLVED externally; weakly FALSIFIED by the corpus's own later measurement (outside the stated range).

### P-17 — Publishing detection methodology will trigger operator calibration against it
- **Outcome:** NON-FALSIFIABLE / TOO BROAD in the window; no mechanism to observe calibration.

### P-18 — Pattern D signal "would sharpen" at corpus age ≥60 days
- **Outcome:** UNRESOLVED (no re-scan recorded).

### P-19 — "Kelp's ≥56.7 days was detectable in principle" → detection products will emerge
- **Original:** implicit in Attack 9's hooks and the Kelp replay's "quote-safe claims."
- **What happened:** Blockaid DVN auditor (04-18), Dune dashboard (04-20), LayerZero Config Checker and docs, Fireblocks DVN-config endpoint; no standalone Hypernative/Cyvers/Forta DVN-threshold product verified.
- **Outcome:** CONFIRMED (the detector class exists and is now vendor-supplied), with the caveat that the corpus was one of several parties saying the same thing in the same week.

### P-20 — "No prevention claim" (Kelp replay): flagging ≠ prevention
- **Original:** "Layer 3 has no enforcement layer"; overclaims explicitly rejected.
- **What happened:** Bitget's monitoring alerts fired at the 18:31 test transaction and the drain continued for about an hour; Hyperbridge was flagged ~15 minutes before its drain (vendor claim); Cosmos Labs had a valid report and mis-triaged it.
- **Outcome:** CONFIRMED — detection without an enforcement path did not prevent the largest losses in the window. Not a prediction in the corpus's sense, but the corpus's restraint here was right.

---

## Summary table

| ID | Prediction | Date | Outcome | Strength |
|---|---|---|---|---|
| P-01 | Oracle-manipulation copies within 30 days | 04-18 | FALSIFIED (timing) | moderate |
| P-02 | Hub iteration 9 at 05-07 10:02 UTC | 05-05 | UNRESOLVED (not recorded) | — |
| P-03 | Fourth mass-drain instance in 1–3 days | 05-10 | UNRESOLVED (not recorded) | — |
| P-04 | THORChain resolves to one of four paths | 05-15 | FALSIFIED (none of four) | strong |
| P-05 | 1-of-1 DVN population is large; Kelp-class risk pre-validated | 04-20 | PARTIALLY CONFIRMED | moderate |
| P-06 | Operational layers dominate 2026 | 04-20 (attribution not found) | CONFIRMED by value (H1); mixed Q3 | moderate |
| P-07 | Synchronized-fire fleet will appear | 04-07 | NON-FALSIFIABLE / TOO BROAD; weakly falsified as priority | — |
| P-08 | Advisor-parasite candidates at ≥90 days | 04-18 | UNRESOLVED | — |
| P-09 | ARMS_RACE within ~15 days | 04-18 | PARTIALLY CONFIRMED / timing FALSIFIED | moderate |
| P-10 | Config monitor fires ≥56 days early | 04-18 | CONFIRMED (retrodiction) | strong (fact) |
| P-11 | V2 predicted the May wave | 05-15 | PARTIALLY / FALSIFIED (Renegade) | strong |
| P-12 | April wave validated combinatorial modelling | 04-20 | FALSIFIED | strong |
| P-13 | Centralised overrides proliferate | 04-20 | CONFIRMED (direction) | moderate |
| P-14 | Lock-release > mint-burn in realised harm | 04-20 | CONFIRMED | strong |
| P-15 | Agentic AI multiplies confused-deputy incidents | 05 | PARTIALLY CONFIRMED | weak |
| P-16 | Camouflage ratio stable 70–79% | 04 | UNRESOLVED / weakly falsified by own data | — |
| P-17 | Recursive evasion | — | NON-FALSIFIABLE / TOO BROAD | — |
| P-18 | Pattern D sharpens at ≥60 days | 04-18 | UNRESOLVED | — |
| P-19 | DVN-config detectors will emerge | 04-18/20 | CONFIRMED (convergent) | moderate |
| P-20 | Flagging ≠ prevention | 04-18 | CONFIRMED | — |

**Machine-readable version.** These twenty items, with outcome values, are `experiment/predictions/G0.json`; `experiment/score.py G0` computes the hit rate (0.56 over 13 resolvable; no Brier score possible because G0 stated no probabilities). G2 re-scores them independently per `experiment/PROTOCOL.md` §6.

**Score, honestly stated.** Of twenty statements that can be read as predictions, four are confirmed with real content (P-10 as fact, P-13, P-14, P-19), three partially (P-05, P-06, P-09/P-15 by frequency only), five are falsified (P-01, P-04, P-11 in part, P-12, P-09 timing), five are unresolved because the corpus stopped recording outcomes, and three are non-falsifiable. The genuinely predictive content — the kind that could have changed a defender's behaviour before an event — is concentrated in P-05/P-19 (DVN configuration class), P-14 (custody architecture) and P-13 (override proliferation). The corpus's *claims about its own predictive record* (P-11, P-12) are the weakest items in it.
