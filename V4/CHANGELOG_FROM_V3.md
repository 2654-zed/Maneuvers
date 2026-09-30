# V4 — Changelog from V3

What V4 keeps, downgrades, removes, and adds, with the evidence that drove each decision. The historical V1/V2/V3 files and `docs/lexicon.md` are unchanged; this file is the bridge.

## Preserved (survived contact with time)

| V3 / lexicon concept | V4 | Why it survived |
|---|---|---|
| Attack 9 Cross-Chain DVN Verification Failure | M-01 | Reproduced on-chain; population exposure measured by others (47% 1-of-1); ecosystem adopted the hook; a second instance (Sandbox) via role capture |
| Attack 10 Proof Verification Bypass | M-02 (broadened) | ≥10 public instances in the window, ~$385M notional — the class the corpus under-weighted |
| Attack 11a key compromise | M-03 (broadened to signing-pipeline integrity) | Wasabi, Volo, Humanity, Taiko, SingularityNET, Bitget |
| Attack 11b unprotected initializer | M-04 | Renegade + Aurellion |
| Attack 13 governance-scale compromise | M-05 (broadened to vote capture) | BonkDAO, Term, Neutron, AFX |
| Attack 12 fake-collateral oracle manipulation | M-06 (broadened to stale/forged/aggregator modes) | Bonzo, Lazy Summer, Ostium, Moonwell, Tectonic, Nostra |
| Confused Deputy (agentic) | M-09 | Bankr ×3; x402 censuses |
| Neutrality Trap phase 4 / Kill-Switch Governance | M-13 | Halts and rollbacks became the dominant Q3 recovery mechanism |
| Pooled Custody Amplification | property of M-01/M-02 (amplifier) | Notional-vs-realised gap in Sandbox, Symbiosis, Hyperbridge, Liquid |
| Configuration-Level Vulnerability | precondition class of M-01, M-05, M-06 | LayerZero docs/Config Checker/defaults; Aave AST tiers |
| Verification-Path Trust Failure | descriptive seam across M-01/M-02/M-06/M-12 | Ostium, Bonzo, Nostra, Wanchain, Bitget |
| Operational Layer Attack | M-03 + M-11 + M-12 | Value-share statistics (Blockaid 74%; TRM ~76%) |
| Bug-Bounty Structural Gap | retained as context (not a maneuver) | Ostium scope; Cosmos Labs mis-triage; THORChain bounty retirement |
| Epistemic tiers + corrections log | retained and tightened (status now refers to public instances; base-rate obligation added) | The corpus's best asset; its failure was propagation |
| Stored Potential / Adversarial Topology | retained as a *heuristic* with an explicit untested-discrimination caveat | Fits many cases; no discharge-rate measurement; counterexamples (Aztec, Coldcard, Liquid) |
| Strategy Lifecycle | retained as "replication happens", timing removed | Lags 2–95 days; 15-day scale was n=2 |
| Protocol-Family Specialist | M-16 | TrustedVolumes (attributed) + same-flaw recurrences |
| Pattern D | M-15 (with control-group obligation) | Count real; discrimination unmeasured |
| Attacks 1, 2-fleet, 3, 4, 6, 7, 8, 14 | M-19–M-25 (HYPOTHESIZED) | No instances; kept as hypotheses with base-rate notes |

## Downgraded

| Concept | From → To | Reason |
|---|---|---|
| Attack 7 log-less drain "anti-forensic design" | leading hypothesis → M-25 HYPOTHESIZED, asset-type prerequisite | Empty logs are default for native ETH; intent not shown |
| Attack 4 time-lock synchronized fire | "highest-leverage speculative category" → M-22, demoted priority | No instance; `TIMESTAMP` count lacks a base rate; the class the corpus deprioritised (M-02) produced the losses |
| CE5E / x402 rogue facilitators | observed drain operation → M-17 HYPOTHESIZED | Shape verified and persisting; victimhood not established; no public footprint in five months |
| Single-Purpose Infrastructure Funder | typology → signal inside M-14 with a farming base-rate note | 84%-dormant mass deployment fits farming as well as staging |
| Pristine Solo Operator | detector → identity-gated component of M-15 | 3 of 4 anchors institutional (corpus's own correction) |
| Convergent Calibration | pattern → M-18 HYPOTHESIZED | Funder anchor retracted; remaining instances cannot exclude one actor |
| Adversarial Vanity Branding (anti-forensic and victim-mimic sub-types) | four sub-categories → operational/funder branding kept as signals; anti-forensic spoofing reassigned to third-party poisoning by default; victim-mimic dropped | Poisoners of org_001 found the next day; victim-mimic built on a <$20K cluster with uncertain mechanism |
| Maneuver Primitives | law → checklist with "absent" as a legal value | Coldcard, Liquid, Aztec do not decompose without forcing |
| Compositional Harm / Proofreading Trap | "most harm" → "most *value-weighted* harm in H1 2026; not count-weighted; not true of Q3 bridges" | TRM/Blockaid counts vs values; Q3 bridge wave |
| Static vs Dynamic Behavior | categorical safety claim → dropped as a claim; retained as history | Liquid ($320M) and Coldcard ($116M) |
| Camouflage Ratio | "Nash equilibrium" → an unexplained measurement with no benign baseline | 04-29 figures outside the stated range; no control cohort |

## Removed

| Concept | Reason |
|---|---|
| Thermodynamic Fundamentalism | Both corpus anchors retracted as an issuer and an exchange; not a maneuver concept; unfalsifiable |
| The Hybrid Gameboard (as grounding) | Two of four empirical groundings wrong or internally contradicted (THORChain mechanism; `0x80b12bd0` retracted as FP and cited as success); metaphor, not model |
| Victim-to-Predator Pipeline | Retired by the corrections log (49 → 2) and never removed from the lexicon |
| Infrastructure-Scale Operator (behavioural typology) | ≥7 of 12 anchors were exchanges/bridges; the "evasion" story was inverted |
| Attack 15 as enumerated | THORChain resolved to a class none of the four paths described; replaced by M-07 |
| The Blockaid "January 2026 prediction" | Not found |
| The Immunefi "April 18" confirmation | Not found |
| Aethir as the anchor for key-compromise | Root cause unverified; the quoted post-mortem sentences are not in the cited post |
| "Every major DeFi exploit demonstrates …" formulations | Replaced by counted instances with named exceptions |
| Retired figures still cited in the lexicon (trust-amplification multiplier; GoPlus 0/50 / "100% gap") | Propagation of the corpus's own retirements |

## Added (genuinely new, evidence-driven)

| V4 | Evidence |
|---|---|
| M-07 Malicious participant inside a threshold-signature protocol | THORChain official reports; a class absent from V1–V3 |
| M-10 Weak key generation at scale | Coldcard $116M; the April-30 dormant drain (re-characterised) |
| M-12 Front-end / vendor supply-chain injection as its own maneuver | Bybit, Polymarket, Bitget, Context.ai |
| M-13 Halt / rollback / freeze as a *defender maneuver* with preconditions | Cronos, Harmony, Cosmos Hub, Liquid, Taiko, Osmosis, THORChain |
| Signing-pipeline integrity mode inside M-03 | Bitget |
| Config-role capture inside M-01 | Sandbox |
| Stale-valuation and forged-signed-price modes inside M-06 | Lazy Summer, Ostium |
| Base-rate obligation on every signal | Correction #20 generalised |
| Notional / realised / recovered loss accounting | Sandbox, Symbiosis, Hyperbridge, Tectonic, Liquid |
| Actor economics (cost of access; M-27) | THORChain bond; BonkDAO purchase; Drift six-month operation |
| M-26 signal manipulation | The inverse of Correction #20 |

## What V4 does not do

- It does not claim any of its maneuvers were *predicted* by V1–V3 unless the prediction audit says so (`reports/prediction_audit.md`).
- It does not re-score Layer 3's private observations; corpus-internal claims are carried at the status the public evidence supports.
- It does not resolve the cadence forecasts (P-02, P-03) or the Pattern F re-scan; those remain open obligations on the corpus owner.
