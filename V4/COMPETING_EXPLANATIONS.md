# V4 — Competing Explanations (Phase 10)

For each important observation the historical work relied on, this file sets out competing hypotheses, the evidence for and against each, what would discriminate between them, and what additional observation would settle it. The goal is to make the framework more scientific, not more comprehensive. Observations are drawn from the corpus (`OBS-C`), from the audit's own on-chain checks (`OBS-A`), and from the post-revision incident record (`OBS-P`).

Evidence codes as in `MANEUVERS.md`.

---

## 1. OBS-C/A — Facilitator self-settlement (CE5E and siblings)

**Observation.** An EOA on Arbitrum holds unlimited, non-expiring Permit2 allowances from many payers; it calls `Permit2.transferFrom` with itself as payee in single-second batches of round-number amounts; payers' balances go to zero; it forwards USDC/USDT out within hours; the same shape persists from April to late September 2026 (`OC` §5). The corpus classified it as a rogue x402 facilitator draining phishing victims (Tier A "68 drains, $929K").

| | H1 — Phishing drain operation | H2 — Legitimate settlement / merchant-of-record facilitator | H3 — Laundering front: operator cycles own funds through fresh wallets to look like payments |
|---|---|---|---|
| For | Unlimited, never-expiring allowances; zero post-balance; the corpus's Permit2-exposure tracker saw approvals ~3 h before pulls; round-number amounts fit a phishing UI presenting round sums | Single-second batch pulls are how a settlement processor closes a period; round amounts are how invoices look; repeat payers over five months (`0xa3a1d7a5` again in September); recurring micro-payments ($0.000023–$3.39) from four addresses at fixed intervals are a metering pattern; smart-account `execute`-shaped inflows; no victim reports in five months; no security-firm coverage | The corpus itself found 42% of top-value "victims" were the operator's own pass-through wallets; nonces of 80–120K on sibling facilitators imply industrial automation; pass-through fraction "likely higher" per the corpus |
| Against | No public victim; a phishing operation this size ($929K in 7 days from one facilitator) with no ScamSniffer/SlowMist footprint in five months is anomalous; repeat payers contradict "one approval + one sweep" | Unlimited never-expiring allowances are unusual for a merchant (though the x402 ERC-20 extension does use Permit2 for gasless payment); the corpus reports payers with prior "exposure" alerts | Laundering usually minimises on-chain visibility; a five-month public, stable address is poor laundering opsec |
| Discriminating evidence | Phishing kits or domains pointing at the address; victims complaining; whole-balance sweeps with no repeat interaction | Identification of the service; payers who keep balances and keep paying; off-chain invoices; payer diversity that matches a customer base | Funding of "payers" from the facilitator's own sinks *before* they pay (the corpus's pass-through test) applied to the whole population, not four samples |
| What would settle it | Full-population deposit-source audit (payer funded by facilitator-linked sink?) plus an off-chain identity check on the facilitator. Both are within the corpus owner's reach; neither has been recorded. |

**V4 stance.** M-17, HYPOTHESIZED. The corpus's inference from structure to theft is unsupported; H2 and H3 are live.

## 2. OBS-C — Coffee Fleet: same-prefix bots hit same-prefix traps

**Observation.** 84 `0xc0ffee…` bots repeatedly hit traps deployed by `0xc0ffeefeed8b…`; 100% c0ffee-on-c0ffee victim overlap; fleet of 56–322 contracts (counts vary by file).

| | H1 — Single operator runs both sides ("observed-harm theater" to game risk scorers) | H2 — Self-testing: an operator fuzzing its own traps with its own bots before deployment against real victims | H3 — Two parties sharing a vanity prefix (a tooling default or a public bot template) |
|---|---|---|---|
| For | Prefix identity; 100% overlap; the corpus's self-loop detector found deployers calling their own contracts | Same evidence; explains why the "victims" never learn (they are not victims); explains zero real-victim overlap | Vanity generators ship with example prefixes; `0xc0ffee` is a well-known hex-word |
| Against | If theater, who is the audience? No scorer is known to weight "has been hit" | Same | 100% overlap with no outside victims is a coincidence H3 must explain |
| Discriminating evidence | Funding linkage between bots and deployer (H1/H2) vs. independent funding (H3); whether any real third-party victim ever appears (H1 predicts eventually yes; H2 predicts a later external campaign; H3 predicts no relation) |
| What would settle it | Funding-graph join of the 84 bots and the deployer; timeline of any non-c0ffee caller. Corpus-internal; not recorded here. |

**V4 stance.** Operational branding retained as a signal; motive left open.

## 3. OBS-C — High-fanout funders

**Observation.** Twelve funders account for 22,165 deployers (42.7% of corpus); none share downstream deployers.

| | H1 — Adversarial infrastructure-scale operators mimicking CEX topology | H2 — They are CEXes and bridge solvers | H3 — Mixed: a few adversarial operators hide among exchanges |
|---|---|---|---|
| Outcome | Corpus's own OLI audit (05-09): ≥7 of 12 are Binance, OKX, MEXC, Bybit, Relay, Orbiter → H1 rejected for the majority; H3 open for the untagged 5 |
| What would settle the rest | Tags or KYC-onramp signatures on the remaining five; downstream trap-confirmation rate per funder against a labelled-exchange baseline |

**V4 stance.** Typology removed; the lesson generalised as the base-rate obligation.

## 4. OBS-C — Mass same-bytecode deployment from fresh L2 wallets, mostly dormant

**Observation.** 69 single-purpose funder→deployer pairs; e.g., 2,005 contracts in one day (~134/s); 3,161 in four days; 84% of fleets never interact with anyone; `0xb0b0b69…` funded 6,605 deployers / ~5,775 contracts in one day.

| | H1 — Pre-positioned trap infrastructure awaiting activation | H2 — Airdrop / points / sybil farming (wallet-count and contract-count metrics) | H3 — Smart-wallet or vault factories, test deployments, or a contract-deployment service's customers |
|---|---|---|---|
| For | Some fleets later fire (12 of 69 have trap activity; 3 have ≥1 drain); bytecode flagged `unusual_fee_structure` | 84% never interacting is exactly what farming produces (deploy, claim later, never use); L2 points programs in 2026 rewarded activity; identical bytecode across thousands of wallets is a farming template | Same-bytecode mass deployment is what a factory does; "unusual fee structure" flags are classifier heuristics, not evidence of intent |
| Against | If traps, the 84% dormancy across months is a poor return on gas | Farming usually shows later claim/interaction events (the corpus has not looked for them) | Factories usually deploy from one address, not 6,605 fresh ones |
| Discriminating evidence | Later activation as traps with third-party victims (H1); claims against points programs / airdrop contracts by the same wallets (H2); factory contract as deployer of record (H3) |
| What would settle it | Track the 69 fleets for 90 days for (a) any drain against a non-linked address, (b) any interaction with an airdrop/points contract. The corpus's corrections already show one "stockpile" was Circle's deployer. |

**V4 stance.** M-14 STRONGLY INFERRED for staging *in general*; the fleet-level signal carries a farming base-rate note.

## 5. OBS-C — Prefix collisions with org_001 wallets, high volume during a monitoring gap

**Observation.** Two wallets sharing 6–8 hex-char prefixes with org_001 infrastructure routed ~$2M+ each on April 8–11; the next day three third-party poisoners targeting org_001 were found.

| | H1 — org_001's own anti-forensic shadow wallets | H2 — Third-party address poisoners exploiting org_001's tx history | H3 — Unrelated wallets with coincidental prefixes (6-hex collisions are ~1 in 16.7M per pair — but the corpus searched many pairs) |
|---|---|---|---|
| For | Volume during the gap; the corpus's diamond-model reasoning | The corpus found active poisoners of org_001 within 24 h; poisoning of high-value wallets is industrialised (~$62M in two Dec/Jan hits) | Birthday-paradox effect across thousands of monitored addresses |
| Against | No key/funding linkage to org_001 shown | Poisoners usually send dust, not route $2M | Volume is hard to explain by coincidence |
| Discriminating evidence | Funding origin of the shadow wallets (org_001 gas stations → H1; unrelated → H2/H3); whether the $2M flows *originated* from org_001-controlled addresses (a poisoning payoff) |
| What would settle it | Funding-graph trace of the two wallets. Not recorded. |

**V4 stance.** Anti-forensic vanity spoofing downgraded; default explanation H2 unless linkage is shown.

## 6. OBS-C — `0x80b12bd0` (Animoca-tagged) deployer: 4,587 addresses drained in 30 minutes on 2026-05-09

| | H1 — Compromised institutional key used to run an approval-harvesting drain | H2 — Rogue insider at the institution | H3 — A token migration / claim / airdrop distribution by a game studio (4,587 "victims" = holders; 8,007 "approvals" = opt-ins) | H4 — Stale label: the address is no longer Animoca's |
|---|---|---|---|---|
| For | Bait contract deployed 03-26; harvested approvals for six weeks; 30-minute automated discharge at ~0.4 s/tx with two non-overlapping execution cells | Same on-chain facts | 7-year institutional identity; REVV/OFC/ANIMOCA holdings; a claim contract would collect approvals and then move tokens in bulk; no public victim report for a 4,587-victim drain | Labels drift; deployer wallets get sold or repurposed |
| Against | No public incident for a 4,587-victim, Animoca-linked drain (Blockaid/PeckShield silence is loud) | Same | Approval-harvesting "bait" classification by the bytecode classifier; the corpus calls the moved tokens a drain | The wallet still held Animoca-portfolio tokens |
| Discriminating evidence | Token identity and destination of the 4,587 transfers (to a sink → H1/H2; to holders or a migration contract → H3); Animoca disclosure; whether "victims" complained |
| What would settle it | One query: what token moved, to where. The corpus never states it. |

**V4 stance.** The case is internally contradicted (flagged 04-24 as a Pristine Solo Operator, retracted 05-09 as an institutional FP, then cited 05-17 as a detection success). Not used as evidence for anything until H3 is excluded.

## 7. OBS-P — Kelp: 1-of-1 DVN signed a forged packet

| | H1 — DVN operator's signing key compromised | H2 — DVN operator colluded | H3 — Signing inputs poisoned; key intact |
|---|---|---|---|
| Corpus stance (04-18) | "not established" — correct restraint |
| Outcome | LayerZero's May 18 report (Mandiant/CrowdStrike): H3 — RPC nodes backdoored via a March 6 social-engineering breach; external RPCs DoS'd; forged responses fed only to the DVN path; no key exfiltration |
| Lesson | The corpus's secondary hook ("if a key leaked, signing patterns change") targeted H1 only. Verifier integrity has to be modelled at the *input* layer (what the signer reads), not only the key layer. |

## 8. OBS-P — THORChain: outbound transactions signed for the attacker

| | H1 — Consensus/observation forgery (ObservedTx bit flip; TSS signed real outbounds) | H2 — Validator key operational compromise | H3 — Malicious participant extracts key shares through the TSS protocol |
|---|---|---|---|
| Corpus stance | V3: four paths enumerated (none is H3); lexicon 05-17: asserted H1 |
| Outcome | H3 (official reports #1/#2): a bonded validator with a malformed Paillier modulus, 864 deliberate MtA failures, full key reconstruction, direct signing |
| Why the corpus chose H1 | A separately disclosed ObservedTx bug (V12, 04-28; patched 05-06/08) was the most recent public THORChain vulnerability; recency was read as cause |
| Lesson | Recency ≠ causality; "mechanism TBD" should have survived until the post-mortem. |

## 9. OBS-P — Exposure vs discharge for 1-of-1 DVN OApps

**Observation.** ~1,250 OApps were 1-of-1 in April; exactly one was exploited before defaults changed.

| | H1 — Exploitation required a compromised *specific* DVN operator (LayerZero Labs), so exposure was concentrated | H2 — Attackers prioritise by reservoir; only Kelp-scale TVL justified a months-long campaign | H3 — Defaults changed fast enough (DVN refusal from 04-19; 3-of-3 from 07-09) to close the window |
|---|---|---|---|
| Discriminating evidence | Which DVN most 1-of-1 OApps used (H1); TVL distribution of 1-of-1 OApps (H2); exploit attempts blocked after 04-19 (H3) |
| V4 stance | All three plausibly true; the historical framework's omission of actor economics (cost of the campaign vs reservoir) is what left the question unasked. |

## 10. OBS-P — Renegade and Aurellion, 48 hours apart, same class

| | H1 — One actor scanning for exposed initializers | H2 — Independent discovery (Renegade's public disclosure prompted others to scan) | H3 — Coincidence at ~30 incidents/month |
|---|---|---|---|
| Discriminating evidence | Funding/tooling linkage between the two attacker EOAs; whether Aurellion's attacker probed before Renegade's disclosure |
| V4 stance | M-18 (convergent templates) stays HYPOTHESIZED because H1 is not excluded. |

## 11. OBS-P — Same flaw exploited twice at Verus (66 days)

| | H1 — Same operator returned (protocol-family specialism) | H2 — Different operator found the unpatched flaw (recidivism of the *protocol*, not the attacker) |
|---|---|---|
| Discriminating evidence | Address linkage between the two exploits |
| V4 stance | M-16 distinguishes specialism (different flaw, same family) from recidivism (same flaw); Verus is recorded as recidivism until linkage is shown. |

## 12. OBS-C — Camouflage ratio ~70–79% (later 67–68%)

| | H1 — Nash equilibrium of operator calibration against revert-rate detectors | H2 — Base-rate property: most contracts, benign or not, have low revert rates, and the "dangerous" set is defined by other features | H3 — Classifier artefact: the corpus's "dangerous" label correlates with the features that also produce low reverts |
|---|---|---|---|
| Discriminating evidence | A benign-contract cohort's low-revert share (H2 predicts similar); the ratio's response to a change in published thresholds (H1 predicts movement); stability under re-labelling (H3 predicts sensitivity) |
| V4 stance | Measurement retained; equilibrium interpretation dropped until a benign baseline exists. |

---

## Cross-cutting discriminators the corpus never ran

1. **Base-rate cohorts.** For every topology signal, the same statistic on a random or labelled-benign sample.
2. **Deposit-source audit at population scale.** The pass-through test the corpus ran on four wallets, run on all.
3. **Identity with provenance.** OLI/explorer labels as a node attribute, applied *before* promotion, with staleness handling.
4. **Asset identity and destination.** For every "drain", what token, to where, and whether recipients are holders, sinks, or contracts.
5. **Linkage before convergence.** No "independent actors" claim without a funding/tooling overlap probe recorded.
6. **Mechanism embargo.** No mechanism assertion for an external incident before an official or forensic post-mortem; until then, "mechanism TBD" with enumerated hypotheses — which V3 did and the lexicon undid.
