# Framework Failure Analysis — Red-Teaming V4 (Phase 9)

**Question:** what would make the entire V4 framework misleading? This file attacks V4 (`V4/MANEUVERS.md`, `V4/FRAMEWORK.md`) with the same severity applied to V1–V3, and records where V4 inherits the historical corpus's weaknesses despite trying not to. Where an attack succeeds, the framework text has been amended or the entry carries a caveat; where it partly succeeds, the residual is stated.

Two provenance reminders that bear on everything below. First, the evidence base for the temporal window is largely secondary (DefiLlama labels, vendor post-mortems, press) gathered by research agents; the audit's own primary reads cover Kelp, the Tornado funding, one facilitator address, and one dev.to post. Second, the audit had no access to Layer 3's database; every corpus-internal observation is carried at the status public evidence supports, which is a decision with its own bias (see §1.3).

---

## 1. Biases in the audit and in V4

### 1.1 Survivorship bias
V4's OBSERVED maneuvers are the ones that produced incidents large enough to be post-mortemed. Classes that succeed quietly (slow extraction, sub-JND skims, laundering fronts, farming that never becomes a trap) leave no post-mortem and therefore no OBSERVED status. This is the same bias that made Attack 14 (advisor-parasite) unprovable for the corpus. **Effect:** V4 systematically under-weights low-drama, high-frequency maneuvers and over-weights the top of DefiLlama's list. **Mitigation in V4:** HYPOTHESIZED status is kept for those classes rather than dropping them; but "kept as hypothesis" is not "measured".

### 1.2 Hindsight bias
Several V4 entries are *broadened* versions of V3 entries (M-02, M-03, M-05, M-06) because the window produced sub-modes V3 lacked. Broadening after the fact is exactly how V2 turned Attack 2 into a "validated" category. **Test applied:** each broadening names the specific incidents that forced it and does not claim the original entry anticipated them. **Residual:** the *decision* to broaden rather than split is a judgment the incidents did not compel; a different auditor might have created seven new maneuvers instead of widening four.

### 1.3 Selection bias (evidence surface)
The audit could verify what is public. This produces an asymmetry: corpus-internal observations were downgraded to HYPOTHESIZED for lack of public confirmation, while public incidents were promoted to OBSERVED on the strength of vendor post-mortems the audit could not independently reproduce (only Kelp was reproduced on-chain). **Effect:** the audit may be too hard on Layer 3's private observations (CE5E may really be a phishing drain) and too easy on vendor narratives (Bitget's mechanism rests on Bitget's and Hypernative's accounts). **Mitigation:** every OBSERVED entry states its evidence source; none claims reproduction it does not have.

### 1.4 Confirmation bias (the audit's thesis)
The audit's emerging thesis — "topology signals without base rates generate false positives" — is itself a lens. Having found Correction #20, the audit looked for the same fault elsewhere and found it repeatedly (fanout, dormancy, prefix collision, self-settlement). It is possible some of those signals do discriminate and the audit is pattern-matching to its own finding. **Mitigation:** each base-rate note says what benign population produces the signal and what would discriminate; none asserts the signal is useless. **Residual:** the audit did not compute any base rate either — it only demanded them.

### 1.5 Overfitting to famous incidents
M-01, M-05, M-07 are each anchored on one dominant incident (Kelp, Drift, THORChain). The historical corpus did the same and paid for it (Attack 15's four paths were all Kelp-shaped). **Test:** each V4 entry lists ≥2 instances or says why one suffices. M-07 rests on one; its generality is explicitly flagged as medium. **Residual:** M-01's "config-role capture" sub-mode rests on Sandbox alone.

### 1.6 Temporal leakage
V4 was written knowing the outcomes. The counterfactual test (`model_comparison.md` §Phase 12) separates what would have been justified without the window from what changed. **Residual:** the *ordering* of V4's index (M-01 first) reflects Kelp's salience, not a pre-window priority.

### 1.7 Measurement problems
Loss figures across the window come from DefiLlama labels whose API rows in this period carry empty `source`/`description` fields. Notional and realised amounts differ by up to four orders of magnitude (Sandbox). Category shares (e.g., "~$385M cross-chain verification bugs") depend on which figure is used and on DefiLlama's classification, which the survey found disagrees with post-mortems in at least six cases (Gravity, Taiko, Harmony, Bitget, DxSale, Lazy Summer). **Effect:** any V4 sentence with a dollar aggregate should be read as ±50%.

### 1.8 Attribution problems
DPRK attribution appears throughout (Drift, Kelp, Bybit, Bitget-likely, AFX). It comes from TRM/Elliptic/Mandiant/CrowdStrike and, in Drift's case, changed designator (UNC4736 → UNC6862). V4 uses attribution only in "Actors" fields and never as evidence for mechanism. **Residual:** actor-economics reasoning (M-27) implicitly assumes rational, capital-constrained attackers; a state actor's cost function is different.

---

## 2. Ontology errors that may persist in V4

1. **Category kinds are still mixed.** M-13 (defender maneuver) sits in the same list as attacker maneuvers; M-15 (identity cover) is a *property of an actor*, not a maneuver; M-26/M-27 are extrapolations. A stricter ontology would separate attacker maneuvers, attacker properties, and defender maneuvers into three lists. V4 keeps one list for continuity with V1–V3 numbering conventions; this is a documented compromise, not a claim of cleanliness.
2. **"Precondition" and "signal" blur.** For M-01, "threshold < 2" is both. The distinction the framework needs — *what must be true* vs *what a defender can see* — collapses whenever the precondition is publicly readable. That is a feature of configuration classes, but it means V4's signal lists are partly restatements of preconditions.
3. **Reservoir is under-typed.** Pooled custody, standing allowances, mintable supply, treasury and governance authority are all "reservoirs" but have different realisation curves (custody realises 1:1; mints realise at liquidity; allowances realise at victim balance). V4 states notional/realised for losses but does not yet type reservoirs by realisation function.
4. **No model of the *chain* as an actor.** M-13 treats halts and rollbacks as maneuvers by "a party with authority". Who that party is (validators, sequencer operator, foundation, council) determines legitimacy cost and speed; V4 lists them without a model.
5. **Phase checklist still invites narrative.** Even with "absent" as a legal value, decomposing an incident into phases is done by the analyst after the fact; nothing forces the decomposition to be the same for two analysts. The checklist has descriptive, not evidential, value.

---

## 3. False positives and false negatives, by maneuver

| Maneuver | False-positive risk (benign behaviour flagged) | False-negative risk (malicious behaviour missed) |
|---|---|---|
| M-01 threshold/role capture | ~1,250 OApps at 1-of-1 in April; most were never exploited. TVL filter reduces but does not remove the FP population. | Poisoned signing inputs with intact keys and thresholds ≥2 if the *same* operator runs multiple DVNs; role capture via token-level calls (Sandbox) invisible to threshold reads until after `setConfig`. |
| M-02 verifier code defect | Conservation checks: near-zero FP. | Fires at trigger only; no pre-trigger signal exists for a latent bug. |
| M-03 key / pipeline compromise | EOA-admin + no timelock is the norm for small protocols; flags thousands. | Bitget-style request forgery is invisible on-chain until the withdrawal; Humanity-style all-keys-on-one-laptop is invisible full stop. |
| M-04 initializer | Abandoned contracts with nothing to steal. | Initializers reachable only through a facet or module the scanner does not enumerate (Aurellion). |
| M-05 governance | Routine parameter changes; legitimate whale votes. | Off-chain signature collection (Drift's durable nonces) before any on-chain trace. |
| M-06 collateral valuation | New tokens with thin liquidity are the majority of new tokens. | Stale valuation (Lazy Summer) does not look like manipulation; signer compromise (Ostium) looks like a price move. |
| M-07 TSS participant | Honest nodes fail keysigns under load. | A patient attacker spreads failures over weeks below any threshold. |
| M-08 approval drains | Approvals to new spenders are how every launch works. | Sweeps that stay below per-victim JND (the advisor-parasite problem). |
| M-09 agent abuse | Agents legitimately act on public instructions. | Injection through channels not monitored (DMs, tool outputs). |
| M-14 dormant staging | Dormant wallets awaken constantly; farming produces mass dormancy. | Staging on a chain the defender does not monitor (every major 2026 incident, from Layer 3's view). |
| M-15 identity cover | Every established operator expanding to a new chain. | Fresh identities (44% of the corpus's high-risk set had no mainnet history). |
| M-17 facilitator self-settlement | Any merchant-of-record processor. | A drainer that varies amounts and timing. |

---

## 4. Counterexamples per major concept

**Same observable, benign explanation.** Each row is a real or realistic case where the V4 signal fires on non-adversarial behaviour.

| Concept | Counterexample |
|---|---|
| Stored potential (high capability, no realised harm) | Circle's contract deployer (38,016 contracts, 0 drains) — retracted by the corpus itself; every large treasury multisig; every LayerZero OApp on defaults before July |
| Configuration-level exposure | The ~1,249 1-of-1 OApps that were never exploited; 2-of-2 configurations where both DVNs are the same operator (equally exposed, not flagged) |
| Dormant fleet activation | Points farmers claiming after a snapshot; a protocol upgrading 100 vault instances in one block |
| Aged identity on a new chain | Animoca's, Stabilize's, Luchadores' deployers (the corpus's own FPs) |
| Self-settlement of allowances | Any x402/Permit2 merchant facilitator; Uniswap's Universal Router pulling via Permit2 |
| Low revert rate ("camouflage") | Every well-tested contract |
| High funder fanout | Every exchange and bridge solver |
| Vanity prefix | TrustedVolumes' own `0xeEeEEe5…` proxy (victim-class, per the corpus); protocol deployers with branded addresses |
| Fresh Tornado-funded wallet | Privacy-seeking users; ~thousands of withdrawals per month |
| Same address across chains for an attacker helper | Every fresh EOA's first deployment (CREATE at nonce 0) |
| Governance parameter loosening | Protocols reducing multisig friction for legitimate operational reasons (Drift's migration was one, until it wasn't) |
| Chain halt / rollback | Scheduled upgrades; consensus bugs unrelated to attack |

**Can a malicious actor avoid the proposed signals?** Yes, for every topology signal, at low cost: route through routers, keep reverts low, split funders, age wallets, avoid vanity, fund from exchanges, use 2-of-2 with two DVNs under one operator, raise thresholds *after* installing yourself as a verifier (Sandbox showed the reverse: install yourself, then act). The signals that cost the attacker something — bond, TVL, time in a seat, keysign failures that get jailed — are the ones that resist evasion, and V4's ranking should follow cost-to-fake, not ease-of-measurement.

**Can the framework attribute coordination where none exists?** Yes — this was the corpus's dominant error (org_001 via a Binance hot wallet; twelve "independent operations" that were exchanges). V4's M-18 keeps convergence HYPOTHESIZED for that reason, but nothing in V4 prevents an analyst from re-inferring coordination from timing.

**Can independent actors converge on the same behaviour without coordination?** Yes, and the window demonstrates it at the defender level too: Blockaid, Layer 3, Dune, and LayerZero converged on the same DVN check within 48 hours without coordinating. Attacker-side convergence (Renegade/Aurellion) is equally explicable by public disclosure and scanning tools.

**Can an attacker manipulate the signals?** M-26 states it: every behavioural feature is manufacturable; identity labels can be bought (acquire a labelled wallet) or aged into; base rates themselves can be moved by flooding the benign population with attacker-controlled "benign" activity (which is what farming may already be doing to dormancy statistics).

---

## 5. Missing variables

1. **Cost of attack** (bond, capital, months of social engineering) — absent from V1–V3; present in V4 only as M-27 and a field name. No maneuver has a cost estimate.
2. **Reservoir realisation function** — see §2.3.
3. **Time-to-halt** per protocol — the M-13 variable; unmeasured anywhere.
4. **Verifier input integrity** — RPC/data-source diversity for oracles and DVNs; the Kelp mechanism; unmeasured.
5. **Composability depth** — how many hops a stolen asset can travel before backing is checked (rsETH → Aave in minutes; SAND → nowhere). Aave's AST framework is the first public attempt to score it.
6. **Label provenance and staleness** — the `0x80b12bd0` problem.
7. **Bug-report handling latency** — Cosmos Labs (4 months, mis-triaged), THORChain (bounty retired), Verus (66 days unpatched): time between disclosure and fix is a leading indicator the framework does not model.
8. **Disclosure-to-exploitation lag in the other direction** — Coldcard (exploited before disclosure); Cosmos EVM (exploited ~20 h after a vague backport). Silent patches are a signal to attackers.

---

## 6. Changing conditions that could invalidate V4

- **Architecture:** if OFT issuers migrate en masse to CCIP or to ≥3-of-3, M-01's precondition becomes rare and the class goes quiet without being wrong — the audit must not read quiet as falsified.
- **Attacker incentives:** DPRK's share (>$1B YTD) means value statistics are dominated by one actor's target selection; a change in that actor's priorities would reshuffle every value-weighted claim in V4 (including "operational layers dominate").
- **Economics:** M-27's rationality assumption fails for state actors and for reputational attackers (whitehats who keep 15%).
- **Detection adaptation:** if conservation monitoring becomes standard, M-02's realised losses fall while its notional losses (mint size) may not — V4's notional/realised split anticipates this.
- **Recovery norms:** if rollbacks become routine (Cronos, Harmony, Cosmos Hub), attacker economics shift toward chains without halt authority — a prediction V4 makes implicitly and should state (see `final_assessment.md`).

---

## 7. What would make V4 *misleading* rather than merely incomplete

1. If a reader took OBSERVED to mean "Layer 3 observed it". It means public instances exist. The V4 README says so; the risk remains.
2. If the base-rate notes were read as base rates. They are obligations, not measurements.
3. If the value-weighted claims were read as count-weighted. Most incidents in 2026 were still code bugs.
4. If the demotion of Attack 4 and Attack 7 were read as disconfirmation. They are unobserved, not refuted.
5. If M-13 were read as endorsement of rollbacks. It records that they happened and dominate recovery; the legitimacy cost is real and litigated.
6. If the window's DefiLlama aggregates were quoted as facts. They are labels with empty source fields.

---

## 8. Changes made to V4 as a result of this red-team

- M-01: added the explicit note that threshold reads flag a population and that the only post-Kelp instance created its own condition.
- M-07: generality flagged medium; single-instance status justified explicitly.
- M-14/M-15/M-17: base-rate notes strengthened; farming, institutional expansion and merchant settlement named as the default competing explanations.
- M-26/M-27: retained but labelled THEORETICAL with no claimed instances.
- FRAMEWORK §3: "no base rates" and "no actor economics" recorded as the framework's two most important structural weaknesses, in that order.
- README: the six "misleading if misread" items above are cross-referenced.
