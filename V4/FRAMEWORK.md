# V4 — Framework Reconstruction and Ontology

**Purpose.** Phase 6 of the audit: extract the conceptual framework that sat underneath the V1–V3 documents and the lexicon, represent it structurally, say where the ontology is flawed, and state the corrected ontology that V4 uses. This file does not add maneuvers; `MANEUVERS.md` does.

---

## 1. The framework as it existed (reconstructed, not improved)

### 1.1 Entities

| Class | Instances the historical work reasoned about | Where it is scored |
|---|---|---|
| **Node** (any object with capability) | contract (trap, bait, proxy, implementation, adapter, pool, oracle, token, router, endpoint, diamond), account (EOA, multisig, council, agent wallet), off-chain service (RPC, OAuth grant, SSO trust path, wallet UI) | Adversarial Topology: position, permissions, trust bindings, mutability, observation capability → Stored Potential score |
| **Actor** | deployer, funder/gas station, operator, victim, scanner/MEV bot, admin/keyholder, council member, DVN operator, validator, relayer/executor, CEX, issuer, law enforcement, bounty platform, AI agent | Behavioral Laundering patterns; operator typologies; Epistemic tiers for attribution |
| **Aggregate** | bytecode family, fleet, organisation (`org_xxx`), funder cluster, drain wave/iteration, protocol family/trust graph | entity_classification; funder metrics; Protocol-Family Specialist |
| **Arena** | chain (monitored vs reference), protocol (lending, bridge, DEX, governance), off-chain domain (SaaS, identity) | The Hybrid Gameboard (late) |
| **Event** | deploy, approve, call/revert, upgrade/initialise, attest/verify, release/mint, bridge/rotate, drain, launder, freeze/halt | extraction_events; trap_events; corrections |

### 1.2 Relationships (edge types)

`funds` · `deploys` · `calls` / `reverts-on` · `approves` (allowance) · `delegatecalls` · `upgrades` / `initialises` · `attests` / `verifies` · `holds-custody-of` · `composes-into` (stolen asset accepted as collateral) · `bridges` / `rotates-to` · `launders-through` · `mimics` (prefix collision; victim-mimic) · `labels` (OLI / explorer tag) · `governs` (council / token vote over parameters) · `configures` (owner → threshold, delegate, peer).

The historical work's detectors are almost all *edge-shape* detectors: fanout on `funds`, self-loops on `calls`, router share on `calls`, dormancy on `deploys`, threshold on `configures`, self-settlement on `approves`→`calls`.

### 1.3 Preconditions (what must be true before a maneuver can occur), as the corpus stated them

| Maneuver family | Precondition |
|---|---|
| Attestation-threshold failure | a verifier set of size 1 (or threshold 1) on a channel that releases pooled custody |
| Proof-verification bypass | a proof shape the verifier mishandles; no challenge period; no supply cap |
| Privileged-key compromise | a single key (or low-threshold set) with zero-delay authority over custody or code |
| Acquired-admin via defect | an initializer or role grant callable by anyone |
| Governance-scale compromise | council/token authority over parameters; no timelock; pre-signable instructions (durable nonces) |
| Fake-collateral oracle manipulation | a lending/margin protocol that admits a token whose price source can be dominated by the attacker |
| Approval drains | outstanding unlimited allowances to an attacker-controlled spender |
| Trap fleets | age-as-trust in scanners; dormancy tolerated; bots that don't learn |
| Advisor-parasite | a durable trust relationship + per-action cost habituation |
| AI-agent abuse | an agent that reads untrusted text and holds transfer authority |

### 1.4 Signals (what a defender could observe), as the corpus listed them

Pre-trigger: `getConfig` threshold reads; admin type/timelock enumeration; callable initializers; dormant fleets and scripted deploy velocity; mainnet-history gaps; funder fanout; router share; vanity prefixes; new pools with one-sided liquidity feeding oracles; governance parameter changes; Tornado-funded fresh wallets; camouflage (low revert) signatures.
At trigger: `lzReceive` of an outlier amount to a fresh address; admin-invoked large transfer; proxy slot write; `Permit2.transferFrom` where caller == payee; single-second batch settlement.
Post-trigger: fan-out within seconds; CEX/THORChain/bridge routing; vanity sinks.

### 1.5 Mechanisms, incentives, consequences (as stated)

Mechanisms were narrated per attack (see `reports/historical_reconstruction.md` §9). Incentives were mostly implicit — "extract pooled custody", "sweep approvals", "skim a fleet" — with one explicit economic argument (Thermodynamic Fundamentalism: attack pipelines must have positive marginal return) and one explicit psychological one (Cost-Habituation / JND). Consequences: direct loss; compositional propagation (Aave bad debt); erosion of neutrality (override infrastructure); victim-to-predator conversion; corpus growth as "compounding intelligence".

### 1.6 Uncertainty (observable vs inferred), as the corpus separated it

Observable (Tier A): on-chain reads, counts, timestamps. Inferred (Tier B): role assignment (rogue, victim, hub, org member), intent (staging, laundering, spoofing), category membership (which Attack an incident "is"). Speculative (Tier C): lifecycle forecasts, advisor-parasite, calibration equilibria.

### 1.7 Feedback (adaptation), as the corpus modelled it

Attacker: calibrate to published thresholds (recursive evasion); rotate chains/wallets; launder through CEX/bridges; mimic legitimate prefixes; converge on templates without coordination. Defender: publish detectors (and thereby leak calibration targets); re-import accountability from off-chain (freezes, councils); add identity layers when topology fails (Correction #20).

---

## 2. Structural representation

A compact statement of the framework's causal core, as it actually operated in the documents:

```
[Stored Potential] = f(capability, permissions, trust-bindings, mutability) − g(constraints: timelock, threshold, cap, judgment layer)

Discharge requires: (a) a TRIGGER path the system will execute deterministically
                    (b) a value RESERVOIR reachable from the trigger (pooled custody, allowances, collateral)
                    (c) an ACTOR with incentive and access to the trigger

Trigger classes:   forged attestation | forged proof | authorised action by a compromised/acquired key
                   | manipulated price accepted as truth | injected instruction to a deputy

Amplifiers:        lock-release custody; composability (stolen asset accepted downstream); zero delay

Dampeners:         thresholds ≥2; timelocks; caps; kill switches; issuer/council override (at neutrality cost)

Detection thesis:  (a) and (b) are readable on-chain before (c) acts ⇒ lead time exists
```

The framework's detectors sit on (a) and (b). It has almost nothing on (c) — actor incentive and access — which is why exposure (47% of OApps 1-of-1) and discharge (one event) diverged by three orders of magnitude without the corpus noticing the gap.

---

## 3. Where the ontology is flawed

1. **Category kinds are mixed.** Attack 9 is a mechanism; Attack 14 is an actor role; Pattern D is a laundering behaviour; "Positioning" is a phase; "the Kelp category" is an incident of record. Splitting Attack 11 and parking Attack 15 were symptoms: numbers were attached to incidents, not to mechanisms.

2. **"Observed" was overloaded.** The status legend defines *Observed* as "the full chain seen end-to-end" (in Layer 3's data). In practice it meant "a third party reported an incident that fits." No category in V2/V3 was ever observed by Layer 3's own detectors; the corpus's true observations are trap fleets, drainers and funders on three L2s.

3. **No base rates.** Every topology signal (fanout, dormancy, mainnet history, `TIMESTAMP`, empty logs, self-settlement, prefix collision, low revert rate) was read as adversarial without measuring its frequency in the benign population. The one signal that was later label-checked (fanout) collapsed. This is the framework's single most important structural weakness because it converts descriptive coverage into false positives.

4. **No notional / realised distinction.** "$3.1 quadrillion OP" was a decimals bug the corpus caught; "329T SAND ≈ $49B" is the same kind of number an unaudited pipeline would emit. The window's best evidence for the corpus's own custody thesis *is* the notional/realised gap, and the ontology had no slot for it.

5. **Identity is not first-class.** OLI/explorer labels entered as a patch (Correction #20) rather than as a node attribute. Attribution to organisations (`org_001`) was built on funding edges from what turned out to include a Binance hot wallet, and the correction never propagated.

6. **Actor economics are absent.** The framework scores what *could* be discharged, never what an actor would *pay* to discharge it (THORChain's attacker posted ~635K RUNE of bond; BonkDAO's bought ~1% of supply; Drift's ran a six-month in-person operation). Cost-of-attack is the missing dampener term.

7. **Missing layers.** Key-generation entropy (Coldcard, $116M); signing-pipeline request integrity without key theft (Bitget, $387.5M); adversarial participation inside threshold cryptography (THORChain); non-injective encodings and cache-key collisions in verifiers (Wanchain, Liquid); L1 consensus signature-mask bugs (Harmony); immutable, admin-renounced contracts with latent verification bugs (Aztec). None of these has a node, edge or phase in the historical ontology.

8. **Chain-level recovery is not modelled.** The corpus treated freezes/forks as the *cost* of the Neutrality Trap. In the window they became the primary *recovery mechanism* (Cronos, Harmony, Cosmos Hub, Liquid, Taiko). A framework about adversarial maneuver needs the defender's counter-maneuver at the chain layer as a first-class object, with its own preconditions (who can halt, how fast, at what legitimacy cost).

9. **Phases are asserted as law.** "Every exploit traverses six phases in order" is a narrative template, not an empirical property. It should be a checklist with an explicit "not applicable" outcome.

10. **The metaphor stack drifted.** Physics → games → warfare, each added without retiring the last. The Hybrid Gameboard (05-17) was grounded on a wrong mechanism (THORChain) and an internally contradicted case (`0x80b12bd0`).

---

## 4. The V4 ontology (corrections applied)

**Nodes** carry: `capability`, `authority` (who can change behaviour; threshold; delay), `reservoir` (custody, allowances, mintable supply — *with notional and realised valuations*), `verification dependencies` (what it trusts), `identity` (public labels, with provenance), `age/dormancy`, `mutability`.

**Actors** carry: `access` (key, seat, vote, role), `cost to obtain access`, `incentive` (reservoir reachable ÷ cost), `attribution confidence` (explicit tier, with the source), `prior recurrence` (protocol-family specialist test).

**Edges** as in §1.2, plus `configures` (owner/delegate → threshold, peer, feed source), `can-halt` (who can pause/rollback what, in how long), and `labels` with provenance.

**Maneuver** = (precondition set) → (trigger class) → (reservoir) → (amplifier/dampener) → (consequence), tagged with an **epistemic status** (OBSERVED / STRONGLY INFERRED / HYPOTHESIZED / THEORETICAL) that refers to *public, independently verifiable instances*, not to fit.

**Every signal** carries a **base-rate obligation**: a statement of the benign population that produces the same signal, and what discriminates. A signal without a base-rate note is a hypothesis, not a detector.

**Every loss** is stated as **notional / realised / recovered**.

**Phases** are a checklist (reconnaissance, positioning, trust, trigger, exploitation, exfiltration, *recovery*) in which "absent" is a legal value.

**Defender counter-maneuvers** (halt, rollback, freeze, coalition backstop, whitehat deal) are modelled as maneuvers with their own preconditions and legitimacy costs.
