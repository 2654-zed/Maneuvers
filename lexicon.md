# Layer 3 Lexicon

**Version:** 2026-05-15 (living document; update when new framework-level observations emerge)
**Purpose:** Canonical definitional reference for Layer 3 methodology. Every entry specifies the term's definition, extended meaning, empirical grounding in the corpus where applicable, and cross-references. Intended for internal use and eventual external publication.
**Discipline:** Each entry is either (a) deductive from on-chain corpus evidence, (b) inferential with explicit methodology application, or (c) framework-level observation with clear analytical basis. No entry is asserted without basis.

---

## Index

### Core Architectural
- [Stored Potential](#stored-potential)
- [Adversarial Topology](#adversarial-topology)
- [Compositional Harm](#compositional-harm)
- [Trust Amplification Factor](#trust-amplification-factor)
- [Thermodynamic Fundamentalism](#thermodynamic-fundamentalism)
- [Neutrality Trap](#neutrality-trap)
- [Forced Deterministic Neutrality](#forced-deterministic-neutrality)
- [Normative Shell Game](#normative-shell-game)
- [Confused Deputy Problem](#confused-deputy-problem)
- [Distributed Confused Deputy Chain](#distributed-confused-deputy-chain)
- [Camouflage Ratio](#camouflage-ratio)

### Detection Methodology
- [Behavioral Laundering](#behavioral-laundering)
- [Pattern A — Reputation-Building Sacrifices](#pattern-a--reputation-building-sacrifices)
- [Pattern B — Temporal Pattern Normalization](#pattern-b--temporal-pattern-normalization)
- [Pattern C — Funding Chain Laundering](#pattern-c--funding-chain-laundering)
- [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import)
- [Pattern E — Fake Legitimate Projects](#pattern-e--fake-legitimate-projects)
- [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern)
- [Pristine Solo Operator](#pristine-solo-operator)
- [Infrastructure-Scale Operator](#infrastructure-scale-operator)
- [Single-Purpose Infrastructure Funder](#single-purpose-infrastructure-funder)
- [Adversarial Vanity Branding](#adversarial-vanity-branding)
- [Protocol-Family Specialist Operator](#protocol-family-specialist-operator)
- [Self-Deploying Single-Contract Mass-Drain](#self-deploying-single-contract-mass-drain)

### Structural and Psychological
- [Participatory Asymmetry / Predatory Literacy](#participatory-asymmetry--predatory-literacy)
- [Static vs Dynamic Behavior](#static-vs-dynamic-behavior)
- [Cost-Habituation Asymmetry](#cost-habituation-asymmetry)
- [Micro-Cost Habituation](#micro-cost-habituation)
- [Cognitive Load Concentration](#cognitive-load-concentration)
- [Tuition Extraction Markets](#tuition-extraction-markets)

### Ecosystem-Level
- [The Proofreading Trap](#the-proofreading-trap)
- [The Self-Cannibalizing System](#the-self-cannibalizing-system)
- [Victim-to-Predator Pipeline](#victim-to-predator-pipeline)
- [Accountability-as-Load-Bearing](#accountability-as-load-bearing)
- [External Accountability Infrastructure](#external-accountability-infrastructure)
- [Convergent Calibration](#convergent-calibration)

### Attack Pattern
- [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion)
- [Strategy Lifecycle](#strategy-lifecycle)
- [Operational Layer Attack](#operational-layer-attack)
- [Configuration-Level Vulnerability](#configuration-level-vulnerability)
- [Verification-Path Trust Failure](#verification-path-trust-failure)
- [Pooled Custody Amplification](#pooled-custody-amplification)
- [Cross-Domain Compositional Harm](#cross-domain-compositional-harm)

### Operational Doctrine
- [Adversarial Maneuver](#adversarial-maneuver)
- [Maneuver Primitives](#maneuver-primitives)
- [Counter-Maneuver](#counter-maneuver)
- [Vulnerability-Centric vs Maneuver-Centric Framing](#vulnerability-centric-vs-maneuver-centric-framing)

### Commercial / Positioning
- [The Detection Gap as Product](#the-detection-gap-as-product)
- [Observational Edge Non-Convertibility](#observational-edge-non-convertibility)
- [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset)
- [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap)
- [Epistemic Tier Classification](#epistemic-tier-classification)

---

## Core Architectural

### Stored Potential

**Definition.** A security primitive measuring accumulated permissions, dormant contracts, and capabilities not yet exercised. Unlike vulnerability assessment, which asks "is this broken," stored potential asks "what happens when this works perfectly."

**Extended description.** The central analytical object of Layer 3's methodology. A contract, account, or organizational structure is scored on capability, position, permissions, trust bindings, mutability, and observation capability. A contract with maximum capability, maximum permissions, zero extraction, and high volatility is at PEAK stored potential — not minimum risk. The absence of realized value is the danger signal.

**Empirical grounding.**
- Formal scoring model in `surveillance/risk_scoring.py`. Components: approval_scope (0-25), capabilities (0-25), deployer_risk (0-25), org_context (0-25). Volatility multiplier 1.0x – 3.0x. Tier cuts: CRITICAL ≥50, HIGH ≥20, MEDIUM ≥8, LOW ≥3.
- **EXTRACTION_008 (Kelp)** is the textbook case: pre-exploit the rsETH OFT adapter scored CRITICAL under this framework (maximum capability, maximum trust binding, zero extraction, zero constraint via 1-of-1 DVN). Verified via historical `EndpointV2.getConfig` replay — 1-of-1 DVN configuration stable for ≥56.7 days pre-exploit (`reports/kelp_retrospective_replay.md` Phase 3, Tier A).
- **EXTRACTION_005 (Drift)** validated the governance-layer version: 9/10 pre-hindsight tension score five days before the $285M drain (`reports/drift_prehindsight_simulation.md`).
- Deck: `l3-narrative/Stored_Potential_Risk_Model.pptx`.

**Cross-references.** [Adversarial Topology](#adversarial-topology) (the scoring primitives), [Compositional Harm](#compositional-harm) (what stored potential discharges into), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (one of the non-code failure modes scored), [Thermodynamic Fundamentalism](#thermodynamic-fundamentalism) (the substrate-level analog: stored capability measured in compute/energy rather than capital).

---

### Adversarial Topology

**Definition.** The measurement of five primitives — **position, permissions, trust bindings, mutability, observation capability** — that determine whether a system component can be weaponized even when every component functions correctly.

**Extended description.** Applied to any node: smart contract, browser extension, AI agent, SaaS OAuth scope, multisig wallet. Each primitive is independently assessable; a node with privileged position, broad permissions, high mutability, strong trust binding, and observation capability is at maximum stored potential regardless of current behavior. The framework transfers off-chain — a MetaMask Snap, Zerion's DPRK-compromised wallet operation, and Aethir's OFT adapter all score similarly on these axes for structurally analogous reasons.

**Empirical grounding.**
- Formalized in `claude.md` §"The Adversarial Topology Framework" as the operational lens for all contract analysis.
- Applied to MetaMask Snaps as the canonical off-chain case (`l3-narrative/Standing_Next_To_The_Safe.pptx`): proves the framework catches non-blockchain stored potential.
- Every Extraction Event (001–008) can be scored against these primitives; Kelp and Drift are the strongest instances.

**Cross-references.** [Stored Potential](#stored-potential), [Pooled Custody Amplification](#pooled-custody-amplification) (position + permissions combination), [Operational Layer Attack](#operational-layer-attack) (when mutability and trust bindings fail), [Infrastructure-Scale Operator](#infrastructure-scale-operator) (position primitive at the funder layer — exclusion logic re-purposed as cover).

---

### Compositional Harm

**Definition.** User harm that emerges from the interaction of correctly-functioning components. No single component contains a bug; the attack surface is composition-level.

**Extended description.** The central finding of Layer 3's work — most harm in the permissionless ecosystem is NOT caused by code defects. It is caused by the way correctly-executing components combine. Kelp's 1-of-1 DVN, LayerZero's endpoint contracts, Kelp's lock-and-release adapter, and Aave V3's collateral acceptance all functioned as specified. The $292M drain emerged from their composition. Traditional audits and bug bounties target component-level defects and therefore systematically miss this class.

**Empirical grounding.**
- Direct validation in **EXTRACTION_005 (Drift, $285M)**: every component executed correctly, per the public post-mortem — durable nonces valid indefinitely as designed, multisig accepted 2-of-5 signatures at the threshold set, vault executed authorized withdrawals, audits confirmed code sound.
- **EXTRACTION_008 (Kelp, $292M)**: same framing, different layer. DVN signed as it was supposed to; LayerZero endpoint delivered as specified; Kelp adapter accepted attestation as configured. Composition was the vulnerability.
- **Corrections #4 (velocity escalation mislabel)** and **#6 (risk_scores doc-reality gap)** are internal analogs — our OWN code had compositional failures where individual pieces worked but the combination silently drifted.
- Deck: `l3-narrative/Compositional_Zero_Days.pptx` catalogs 8 named compositional attack constructions.

**Cross-references.** [Configuration-Level Vulnerability](#configuration-level-vulnerability), [Verification-Path Trust Failure](#verification-path-trust-failure), [The Proofreading Trap](#the-proofreading-trap), [Cross-Domain Compositional Harm](#cross-domain-compositional-harm) (the cross-domain extension of this concept), [Thermodynamic Fundamentalism](#thermodynamic-fundamentalism) (composition produces emergent thermodynamic costs that components in isolation do not predict).

---

### Trust Amplification Factor

**Definition.** The multiplier by which identical behavior produces more victims when delivered through a trusted infrastructure position versus independent discovery.

**Extended description.** Measures the leverage an attacker gains by compromising or exploiting trusted infrastructure (router, aggregator, wallet UI, yield platform) rather than competing for attention independently. A trap delivered via Uniswap Universal Router gets orders of magnitude more traffic than the same trap deployed in the wild. The factor is computed from `surveillance/trust_amplification.py` as `callers_per_day ÷ family_avg_callers_per_day` (the contract's caller velocity divided by the average caller velocity across the contract's bytecode family). When a contract has no family membership the formula falls back to a self-baseline of 1.0×.

**Methodological caveat (2026-04-25).** The 14.2× figure originally reported for `0xd4624228` was computed against the `T2-eaef6a5d` bytecode family baseline that was later dissolved by Correction #3 (NULL-bucket reclassification). When the family dissolved, the contract lost its baseline and the next producer run reset its amplification_factor to 1.0× (self-baseline). The `2,910 victims` and `~97% router-delivered traffic` measurements remain Tier A — those are direct caller counts. The 14.2× multiplier specifically is not currently reproducible by the producer because the comparator family no longer exists. A re-run on 2026-04-25 produced no row at all because the contract has only 2 caller events in the post-monitoring-start window (the parasite's harvesting completed before continuous monitoring stabilized). See Correction #17.

**Empirical grounding.**
- **`0xd4624228` routing parasite**: 2,910 victims, 96.6%–98.7% router-delivered traffic (Tier A direct counts). 31 trap_events landed on the contract between 2026-03-19 and 2026-03-26, after which the contract went dormant. Documented in deck `Layer3_Intelligence_Platform_1.pptx` slide 5; Cantina submission 2026-03-25 was rejected on grounds that "the code did what it was supposed to do" — confirming the [Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap), not invalidating the harm finding.
- Producer runs nightly per Correction #7 scheduler (03:00 UTC). DELETE-and-rebuild semantics mean a contract whose caller count drops below the 50-caller minimum loses its row entirely — historical figures should be cited from snapshots, not from current table state.
- API surface: served at `/api/v1/contract/{addr}` via the `computed_at` metadata block with freshness timestamp.

**Cross-references.** [The Detection Gap as Product](#the-detection-gap-as-product), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (the per-user analog of trust amplification), [Camouflage Ratio](#camouflage-ratio), [Cross-Domain Compositional Harm](#cross-domain-compositional-harm) (the off-chain analog where amplification crosses identity systems), [Tuition Extraction Markets](#tuition-extraction-markets) (the market structure the amplification operates within).

---

### Thermodynamic Fundamentalism

**Definition.** An economic and security philosophy that replaces social-consensus measurements of value (fiat currency, market cap, narrative) with physical-substrate measurements (compute cycles, energy consumed, irreversible state transitions). The core axiom: money can lie, physics cannot.

**Extended description.** In this framework, a business is an engine that converts energy into outcomes. The Compute Efficiency Ratio (CER) — useful work done divided by energy burned — replaces Return on Investment as the primary survival metric. Companies, protocols, and AI agents that fail to maintain CER above 1.0 are not financially unsound; they are physically doomed, regardless of narrative or funding. The GPU becomes the auditor, and the electricity bill becomes the final, unforgeable judgment.

The framework matters for security work because adversarial systems (drainer infrastructure, AI-augmented attack tooling, recursive agent loops) face the same thermodynamic constraint as the systems they target. An attack pipeline whose marginal cost per attempt exceeds its marginal extraction is doomed regardless of how successfully it evades detection. Conversely, a defensive system whose CER is unfavorable cannot scale even if its detection accuracy is perfect. Layer 3's design constraint of minimizing Alchemy API calls and running all analysis from SQLite is, in this lens, a CER-positive architectural commitment — analysis cost scales sub-linearly with corpus size.

**Empirical grounding.**
- The collapse of WeWork vs. the physics-bound unit economics of AI inference: a business model whose unit economics required negative gross margins indefinitely failed; one whose unit economics include strictly-positive marginal compute cost survives if and only if its CER stays above 1.
- AI agent recursion without complexity ceilings causing unbounded cost (the "physics breach"): an agent loop that consumes compute super-linearly with task complexity will breach its operator's energy budget before it produces value, regardless of whether the underlying model is correct.
- The end of the "infinite capital glitch" in any industry where marginal cost is strictly positive and non-zero: a sustained negative-gross-margin business is bounded by its capital pool's finite size, while an industry with zero marginal cost (pre-AI software) was not.
- ~~**Layer 3 corpus instance — bb50 industrial-scale stockpile (`0xbb50ce87be3443ed137df1dfdbf2fb0ca8c0a9e0`, Optimism):** 38,016 deployed contracts as of 2026-05-02, 0 lifetime drains, 0 lifetime approvals against the fleet... Current CER ≈ 0. This is thermodynamically a pre-funding state...~~ **[CORRECTION #20 — 2026-05-09: RETRACTED]** `0xbb50ce87...` is OLI-tagged as **Circle: contract deployer** — Circle's institutional contract deployer. The "stockpile awaiting activation" framing was wrong; the 0-drains / 0-approvals observation was structurally accurate but misinterpreted (Circle deployers don't drain because they're not adversarial, not because they're pre-funding). This was NOT a thermodynamic pre-funding state. **A replacement empirical anchor for the CER-≈-0 stockpile class is needed**; deferred until OLI-cleared candidates surface.
- ~~**Layer 3 corpus contrast — drainer-spawn hubs `0xf7883e3fef23` and `0x3304e22ddaa2`:** unlike bb50's stockpile (CER ≈ 0), these hubs exhibit observable positive CER...~~ **[CORRECTION #20 — 2026-05-09: PARTIAL RETRACTION]** `0x3304e22ddaa2` is OLI-tagged as **Binance 73 / Exchange / Binance**; the "hub spawning drainer wallets across iterations" framing dissolves on identification — the four drainer wallets that received funds from this Binance hot wallet are CEX-customer recipients, not coordinated spawn iterations. The 399-victim April 1 drain by `0x7b72595d62b1...` was real, but the upstream-funder-as-coordinator inference was wrong. **Hub `0xf7883e3fef23c8e645deba4b540549d78028a616` remains a valid positive-CER example** (859 victims drained across 6 iterations with sub-minute timing precision; OLI-clean per 2026-05-09 audit; cadence + automation signature documented in INDEX.md and irreducible to CEX-customer activity).
- **Layer 3 corpus replacement anchor — Coffee Fleet (`0xc0ffeefeed8b9d271445cf5d1d24d74d2ca4235e`, Base, OLI-clean per 2026-05-09 audit) added 2026-05-09.** 322 deployed contracts of which 142 (44.1%) are confirmed-tier traps and 111 (34.5%) are suspected-tier — exceptional confirmation density indicates active extraction across the fleet rather than dormant stockpiling. First seen 2026-03-30, last seen 2026-05-07 (5 weeks of continuous activity). Mainnet first tx 2024-09-05 (~1.7y mainnet age — operator's own history, not pristine-solo dormancy). Dual-role operator (deployer + 84-bot self-scanning fleet, see `cases/CASE_COFFEE_FLEET_0xc0ffeefeed8b.md`). The compute cost (gas to deploy 322 contracts + bot scan operations) is bounded; the extraction surface (142 confirmed traps × victim-acquisition windows) is bounded but materially larger. **CER positive on per-iteration basis.** Together with the f7883e3f drainer-spawn hub, this gives the entry two non-CEX-contaminated positive-CER anchors at different operational shapes (Coffee Fleet = persistent deployer/scanner duality; f7883e3f = pulse-spawn drainer iterations).
- **Layer 3's own architectural CER:** the design constraint of minimizing Alchemy API calls and running all analysis from SQLite (`claude.md` Design Constraint) is, in this lens, a CER-positive commitment. Analysis cost scales sub-linearly with corpus size because per-request RPC is replaced with batch-amortized SQLite operations. The framework's commercial positioning ([The Detection Gap as Product](#the-detection-gap-as-product), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset)) depends on this; without a CER-positive analysis architecture, the platform's value-add could not scale faster than its compute cost.

**Cross-references.** [Stored Potential](#stored-potential) (the security-side analog: stored capability measured at the physical-substrate level rather than at the financial-statement level), [Compositional Harm](#compositional-harm) (composition produces emergent thermodynamic costs that components in isolation do not predict), [Neutrality Trap](#neutrality-trap), [Forced Deterministic Neutrality](#forced-deterministic-neutrality).

---

### Neutrality Trap

**Definition.** A systemic paradox in permissionless, deterministic systems where the foundational promise of impartial, unstoppable execution (no human authority, no bias, no censorship) attracts both legitimate users and predators, but the predators weaponize that very impartiality to exploit the system with impunity. The system's neutrality becomes the load-bearing surface adversaries position against — because the execution will never refuse their malicious transaction, will never pause to question intent, and will never reverse the resulting harm. Over time, the damage forces the introduction of centralized governance (freeze authorities, emergency multisigs, social forks), betraying the neutrality principle to save the system.

**Extended description.** The trap unfolds in four phases:

1. **Promise.** "No one controls this. Code is law. All transactions are equal." The neutrality commitment is the system's distinguishing value — censorship resistance, trustless execution, equal access — and it is the precise property that makes the system worth participating in.
2. **Selection.** The neutrality attracts both populations the system was designed for (idealists, sovereignty-seekers, people excluded from gated alternatives) and a population it was not designed to serve well (predators who specifically value "no cops, no reversals, no authority that can intervene"). Both populations are admitted on identical terms; the neutrality cannot select.
3. **Predation.** Predators deploy traps, drains, and organizational extraction infrastructure within the neutrality boundary, knowing the system will execute their code perfectly and never intervene. The predators do not break the neutrality — they use it. Their operations are valid in the protocol's strictest sense.
4. **Override.** Catastrophic losses accumulate. The community introduces centralized kill-switches (Security Councils, emergency multisigs, stablecoin issuer freezes, social forks) to prevent collapse. The neutrality principle is sacrificed in the specific cases where harm has accumulated past tolerance, but cannot be sacrificed at the protocol level without destroying the system's reason for existing. The result is a hybrid in which the surface remains neutral while the periphery accumulates discretionary authority.

The adversary does not break the neutrality; they lean on it to transfer the system's own force into destruction. Layer 3's surveillance posture is built on the recognition that neutrality at the protocol layer is non-negotiable but neutrality at the observation layer is not — the platform observes and classifies without requiring the protocol to discriminate.

**Empirical grounding (April 2026 cluster).**
- **EXTRACTION_006 (Aethir):** EOA admin key compromise — the protocol functioned exactly as designed; there was no circuit breaker to question the admin's destructive call. The neutrality of admin authority is the trap surface.
- **EXTRACTION_007 (Hyperbridge):** the one code bug in the cluster — but the neutrality of the bridge's verification logic still allowed the forged message to be accepted deterministically. Even with the bug, the surface that delivered harm was the protocol's commitment to executing what it could verify.
- **EXTRACTION_008 (Kelp):** 1-of-1 DVN configuration — the protocol faithfully executed the cross-chain message because the DVN signed it. No component asked "should this much value really move based on a single signature?" The lack of any judgment layer is the trap.
- **EXTRACTION_009 (Wasabi):** the protocol's correctly-functioning UUPS upgrade authority drained ~$5M when the admin key was compromised. The upgrade primitive is neutral by design; the trap was the configuration that placed a single key inside the neutrality boundary.
- **EXTRACTION_010 (mass dormant-wallet drain):** Ethereum's signature-verification neutrality is the trap surface — the protocol has no concept of "the wallet's owner did not authorize this signature" once the signature is valid. 49+ victims drained.
- **All five extraction events (006–010) share the pattern:** correctly functioning code enforced an attacker's desired outcome without any layer of discretionary judgment. See `reports/april_2026_key_management_cluster.md` for the consolidated synthesis.

**Cross-references.** [Forced Deterministic Neutrality](#forced-deterministic-neutrality) (the mechanism that enforces the trap), [Stored Potential](#stored-potential) (neutrality keeps stored potential high because no one can discharge it safely), [Accountability-as-Load-Bearing](#accountability-as-load-bearing) (the trap forces the creation of external accountability infrastructure), [Thermodynamic Fundamentalism](#thermodynamic-fundamentalism), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (a frequent failure mode within the neutrality boundary), [Compositional Harm](#compositional-harm), [Normative Shell Game](#normative-shell-game) (the public/private governance split that emerges to manage the trap).

---

### Forced Deterministic Neutrality

**Definition.** A design property of execution environments — protocols, virtual machines, smart contracts, API frameworks — where every valid input is processed to completion exactly as specified, with no built-in capacity to inspect intent, pause for human review, or reverse the outcome. The system cannot discriminate between a user's honest mistake, a consenting transaction, and a malicious exploit; they all look the same at the machine layer. This absence of judgment is intentional (to ensure censorship resistance and fairness) but it creates the structural vulnerability that the [Neutrality Trap](#neutrality-trap) describes.

**Extended description.** Three key characteristics define the property:

- **No context window.** The system sees a signed message, not the human behind it. It cannot ask "did you mean to send your life savings to this address?" The machine's view is bounded by what's in the call data; it has no access to the human's intent, history, or current state of duress.
- **No pause / override.** Once initiated, execution is unstoppable. No timeout, no circuit breaker, no human in the loop. The transaction either reverts on its own internal logic or runs to completion.
- **No intent parsing.** The system cannot distinguish between a user who was phished and one who is genuinely moving funds. The valid signature is the only fact the system has; everything else is invisible at the layer where the decision is made.

**Degrees of forced determinism.** Not all systems are fully deterministic. Trad-fi wires have delayed settlement and legal reversibility. OAuth tokens can be revoked. EVM transactions are fully deterministic and irreversible at the protocol level, but social forks and stablecoin freezes can introduce after-the-fact overrides — these are exactly the "emergency cores" that the [Neutrality Trap](#neutrality-trap)'s fourth phase forces into existence. The framework's [External Accountability Infrastructure](#external-accountability-infrastructure) entry exists *because* forced-deterministic-neutrality at the on-chain layer requires recovery infrastructure to be re-imported from off-chain authorities (Tether/Circle freeze, foundation grants, CEX coordination). Recovery is the explicit acknowledgment that on-chain neutrality cannot be unforced. Layer 3's surveillance operates at the adjacent layer — observation, classification, off-chain coordination — because the protocol-level neutrality cannot be touched without destroying the protocol's value proposition.

**Empirical grounding.**
- **EVM bytecode execution.** A smart contract call with a valid signature will run to completion even if the callee is a known trap. The EVM has no "revert if this contract has a 95.0 stored potential" opcode. Layer 3's bytecode classifier can flag the contract before users approve, but cannot prevent the protocol from executing once the user signs.
- **ECDSA signing (EXTRACTION_010).** A valid `transferFrom` signature on a Permit2 approval is mathematically indistinguishable from one signed under duress. Forced determinism means the ledger updates regardless. The 2026-04-30 mass dormant-wallet drain hit 49+ victims via this exact surface — the protocol could not distinguish the attacker-controlled signing from the legitimate wallet owner.
- **Wasabi UUPS upgrades (EXTRACTION_009).** The proxy pattern allows a contract owner to change the implementation logic at any time. If the owner is compromised, the protocol executes the new malicious logic without asking token holders. The upgrade primitive is forced-deterministic by the proxy's spec; the only judgment available is at the contract owner's discretion, not at the protocol level.
- **Permit2 signed permits (X402 drains).** The 2026-04-30 X402 facilitator-drain coordinated endpoint received ~$285K via `transferFrom` calls that the protocol executed deterministically — Permit2 cannot refuse a signed permit even if the signature was obtained via phishing. The protocol's correct functioning is the attack vector.
- **OAuth grants (Vercel/Context.ai breach, EXTRACTION_009-adjacent).** A user clicks "Accept" on a Google OAuth screen; the token is generated with the requested scopes. Later, the third-party service misuses that token. Google's OAuth server doesn't monitor how the token is used — only that it was validly granted. Same shape as on-chain forced determinism, off-chain substrate. See `cases/CASE_VERCEL_CONTEXT_BREACH_20260419.md`.
- **USD wire transfers.** Once a wire is sent, the banking system executes it deterministically *in principle*; in practice there are clawbacks, but those are external accountability layers, not built into the transfer protocol. The trad-fi system's "weak" determinism is the opposite-end exemplar of how strong on-chain determinism becomes when the off-chain mitigations are absent by design.

**Cross-references.** [Neutrality Trap](#neutrality-trap) (the systemic failure pattern this mechanism creates), [Stored Potential](#stored-potential) (deterministic execution means stored potential can be discharged instantly and silently), [Thermodynamic Fundamentalism](#thermodynamic-fundamentalism), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [External Accountability Infrastructure](#external-accountability-infrastructure) (the recovery channel that exists *because* on-chain neutrality cannot be unforced), [Confused Deputy Problem](#confused-deputy-problem) (a classic security vulnerability enabled by forced determinism: the deputy cannot question the authority of the principal).

---

### Normative Shell Game

**Definition.** The strategic two-layer governance posture in which an entity publicly invokes immutability or decentralization philosophy ("Code is Law," "permissionless," "unstoppable") to deflect accountability for platform harm, while covertly maintaining centralized intervention capacity (multisig, Security Council, admin key, social coordination) that is activated when reputational, legal, or financial interests demand it. After the crisis, the philosophical veneer is restored. The Shell Game is the structural response to the [Neutrality Trap](#neutrality-trap): the trap demands neutrality at the surface to preserve the system's value proposition, but catastrophic harm forces an override layer that cannot be acknowledged without undermining that value.

**Extended description.** The mechanism operates as a continuous two-layer architecture:

- **Public Shell.** "Code is Law. We are decentralized. No one controls this protocol. Users are responsible for their own security." This posture minimizes legal exposure, deflects victim complaints, deters regulatory scrutiny, and maintains the system's appeal to the user base that values neutrality.
- **Emergency Core.** A privileged role (multisig signers, Security Council, governance token holders, stablecoin issuer freeze authority) that can intervene — pause contracts, upgrade proxies, freeze funds, coordinate a hard fork, lean on law enforcement — but only does so when the cost of non-intervention exceeds the cost of breaking the shell.

The gap between these layers is the Shell Game. The entity enjoys the growth benefits of appearing permissionless while retaining the power benefits of centralized control. The key property is that the Emergency Core is legible only in retrospect — its existence may be documented but is deliberately de-emphasized during normal operation, and its activation is framed as an exceptional "community response" or "security measure" rather than as the exercise of centralized authority that it structurally is.

The Shell Game is not necessarily malicious. It may be the only stable governance posture for systems caught in the [Neutrality Trap](#neutrality-trap): the neutrality cannot be surrendered without destroying the system's reason for existing, but the harm that neutrality enables cannot be tolerated without destroying the system's user base. The two-layer posture is an equilibrium, not a conspiracy. What makes it a Shell Game is the refusal to acknowledge the tension publicly.

**Why it matters for detection.** A protocol whose documentation claims "fully decentralized, no admin keys" but whose on-chain state shows a non-renounced proxy admin, a low-threshold multisig, or a Security Council with freeze authority is running this posture. The detector's task is to read the operational topology, not the stated philosophy. The gap between the two is the stored potential.

**Empirical grounding.**
- **Arbitrum Security Council freezing KelpDAO exploiter funds (2026-04-20).** The Arbitrum ecosystem's public posture emphasizes L2 trustlessness, rollup security inherited from Ethereum, and user sovereignty. When the Kelp exploiter held 30,766 ETH on Arbitrum One, the Security Council — a centralized multisig — identified and executed a technical approach to freeze the funds, acting on input from law enforcement. The action was publicly disclosed and arguably net-positive for victims. But it demonstrated that Arbitrum One's chain state is mutable by a small group of humans when circumstances require it. The Shell Game is that this mutability is de-emphasized during normal operation and highlighted only during emergencies.
- **The DAO Fork (2016).** The Ethereum community's public commitment to immutability was set aside to recover The DAO's drained funds. The fork was a social-layer override of the protocol's neutrality — the canonical instance of the Emergency Core activating.
- **Stablecoin freeze authority (USDC, USDT).** Both issuers market their stablecoins as "permissionless digital dollars" while maintaining and exercising the ability to freeze addresses at the request of law enforcement or their own risk teams. The freeze function is built into the contract; its existence is documented but not foregrounded in user onboarding.

**Cross-references.** [Neutrality Trap](#neutrality-trap) (the structural paradox that makes the Shell Game the only stable equilibrium), [Stored Potential](#stored-potential) (the emergency core is a stored-potential node — its intervention capacity is the capability that may or may not be exercised), [Accountability-as-Load-Bearing](#accountability-as-load-bearing) (the Shell Game is one mechanism for providing accountability in a system that architecturally rejected it), [External Accountability Infrastructure](#external-accountability-infrastructure) (the Emergency Core often relies on off-chain coordination layers), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (the admin key or Security Council that enables the Shell Game is itself a configuration-level surface).

---

### Confused Deputy Problem

**Definition.** A classic security vulnerability in which a program with elevated privileges (the *deputy*) is tricked by another program or actor with lower privileges into misusing its authority. The deputy is not malicious — it is executing exactly what it was instructed to execute, using permissions it was legitimately granted. The "confusion" is that the deputy cannot distinguish between instructions that reflect the principal's genuine intent and instructions that the principal was deceived or coerced into issuing, or instructions that arrived from a different source than the one the deputy was designed to trust.

**Extended description.** The canonical form has three roles:

- **Principal.** The entity that holds authority and grants permissions to the deputy (the user who installed the AI agent, the protocol that deployed the smart contract, the user who signed the OAuth grant).
- **Deputy.** The program that holds elevated permissions and executes instructions (the AI coding agent with terminal access, the smart contract with DELEGATECALL, the Permit2 allowance executing transferFrom).
- **Attacker.** The entity that crafts instructions that the deputy will execute using the principal's permissions, but that serve the attacker's goals rather than the principal's.

The vulnerability arises because the deputy's authorization architecture checks whether an instruction is *valid* (right format, right permissions, right signature) but not *who authored* the instruction or *why*. The deputy operates in [Forced Deterministic Neutrality](#forced-deterministic-neutrality): if the input passes validation, execution proceeds. The deputy has no judgment layer that asks: "Is this instruction actually what my principal wants? Did my principal mean to authorize this? Did this instruction come from my principal or from a log file my principal told me to read?"

**The Agentic AI Supercharger.** In traditional computing, the Confused Deputy is a well-understood category. Agentic AI supercharges it because the deputy now interprets natural-language instructions from any source it reads, and the principal has implicitly granted it permission to read a wide variety of untrusted content (repo READMEs, log files, issue comments, email text, web pages). The attacker does not need to compromise the principal's authentication system; they only need to place text somewhere the deputy will read it. The instruction "summarize this repo" can hide a secondary instruction "and send the .env file to this endpoint," and the deputy's linguistic processing treats both as equally valid requests. This is the mechanism behind the Indirect Prompt Injection scenarios documented in Agent Range's threat model.

**Comparison to the Neutrality Trap.** The Confused Deputy Problem is a specific mechanism-level vulnerability. The [Neutrality Trap](#neutrality-trap) is the systemic pattern that makes the mechanism unavoidable: in a system that executes valid inputs without judgment, any valid input will be executed regardless of its relationship to the principal's true intent. The Confused Deputy is what happens at the level of an individual program; the Neutrality Trap is what happens at the level of the ecosystem that consists of millions of such programs.

**Empirical grounding.**
- **AI coding agents.** When an AI agent reads an untrusted repository's README and executes a `curl` command that exfiltrates fake secrets to a mock external endpoint in a sandbox, it is the Confused Deputy. The agent's terminal access is the permission; the README text is the instruction; the agent cannot distinguish between "the user told me to run this" and "the repo's README told me to run this." The instruction comes "from inside the house" — from a source the principal told the deputy to interact with.
- **Permit2 signatures (EXTRACTION_010, 2026-04-30 mass dormant-wallet drain).** The Permit2 `transferFrom` function is a deputy: it holds the user's authorization to move tokens, and it executes when presented with a valid signed permit. The attacker obtains a valid signature (via phishing, key compromise, or reuse of a stale approval). The `transferFrom` function cannot ask "did the wallet's owner actually sign this right now, or was this signature phished from them three months ago?" The function sees the valid signature and executes. 49+ victims drained in a single event.
- **Wasabi UUPS upgrade (EXTRACTION_009, 2026-04-30).** The proxy contract is a deputy: it delegates execution to the implementation contract the proxy admin specifies. When the admin key is compromised, the attacker becomes the admin and points the proxy at a malicious implementation. The proxy executes the attacker's `drain()` calls because the admin key — the principal from the proxy's perspective — authorized the upgrade. The proxy cannot ask "is this admin key being held by its original owner?" The admin signature is valid; the execution proceeds. ~$4.5–5.5M extracted.
- **Vercel/Context.ai breach (2026-04-19).** The Vercel employee's personal Context.ai account was a deputy: it held an OAuth grant with "Allow All" Google Workspace scope for the employee's Vercel identity. When Context.ai's environment was compromised and the attacker obtained the OAuth tokens, the Google OAuth infrastructure honored those tokens because the grant was valid — the consent screen had been clicked. The OAuth server is a deputy that cannot ask "did the user understand what they were consenting to, and are they still in control of the application they granted access to?"

**Cross-references.** [Forced Deterministic Neutrality](#forced-deterministic-neutrality) (the mechanism that produces the per-program vulnerability), [Neutrality Trap](#neutrality-trap) (the ecosystem-level pattern that makes the per-program vulnerability unavoidable), [Stored Potential](#stored-potential) (the deputy's elevated permissions are themselves stored potential), [Compositional Harm](#compositional-harm) (Confused Deputy harm composes across principal/deputy/attacker boundaries), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (the deputy's authorization configuration is the failure surface), [Distributed Confused Deputy Chain](#distributed-confused-deputy-chain) (the multi-contract systemic form of this vulnerability in modular protocols).

**External taxonomy reference.** Maps to several `kadenzipfel/protocol-vulnerabilities-index` categories: `categories/bridge/access-control-misconfiguration.md`, `categories/cross-chain/access-control-and-privilege-escalation.md`, `categories/services/cross-chain-bridge-message-validation.md`, and the per-protocol-type `signature-replay` / `signature-validation` entries. Layer 3 surfaces this via `vuln_index` FTS in the Explore tab; see `scripts/ingest_vuln_index.py`.

---

### Distributed Confused Deputy Chain

**Definition.** A systemic amplification of the [Confused Deputy Problem](#confused-deputy-problem) in modular smart contract architectures. When a protocol splits its logic across multiple contracts (Proxy, Router, Vault, Strategy, Oracle, Access Controller) that hardcode absolute trust in one another, an attacker who compromises or confuses a single contract in the chain can pass a malicious payload through the entire trust network. No single contract understands the full "story" of the transaction; each contract verifies its own localized state and hands execution to the next. The result is that the entire protocol participates in its own exploitation, one compliant deputy at a time.

**Extended description.** The mechanism requires three conditions:

1. **Fragmented epistemic state.** The protocol's logic is distributed across multiple contracts, each with a narrow, specialized view of the transaction. The Vault knows balances but not routing logic. The Router knows paths but not collateral requirements. The Oracle knows prices but not user intent. No single contract holds the full context.
2. **Hardcoded trust bindings.** The contracts are designed for composability, so they trust one another implicitly. If Contract A calls Contract B with a valid signature, Contract B executes without verifying the broader transaction context. There is no cross-contract "story validator."
3. **A single point of syntactic failure.** The attacker finds one contract in the chain with a syntactic vulnerability — an unprotected initializer, an unguarded delegatecall, a missing access modifier. Because all contracts trust one another, this single syntactic failure grants the attacker the authority of the entire protocol.

**Empirical grounding.**

- **Renegade Dark Pool Proxy (2026-05-10, `0x30bD...DC518` on Arbitrum) — *unprotected-initializer sub-mechanism*.** Unprotected initializer allowed an attacker to reset the proxy's implementation address. The proxy, the token approvals, and the asset vault each functioned correctly; together, they constituted a Distributed Confused Deputy Chain that drained user assets. Attacker: `0x777253F28AdC29645152b7b41BE5c772A9657777`. Implementation at risk: `0xc038933d0b33359f5C87B4B2f92Ee0DAd11EaDc5`.
- **Wasabi Protocol (EXTRACTION_009, 2026-04-30) — *UUPS-admin-key sub-mechanism*.** A compromised admin EOA triggered a UUPS proxy upgrade to a malicious implementation. The proxy obeys the admin; the vault obeys the proxy; the token approvals obey the vault. The chain of trust discharged stored potential instantly. See `cases/CASE_WASABI_EXPLOIT_20260430.md`.
- **Aurellion Labs (2026-05-12, `0x0adc63e7…f296f1b2` on Arbitrum) — *diamond-facet-injection sub-mechanism*.** Attacker called `diamondCut(...)` on an EIP-2535 diamond to attach a malicious facet exposing `pullERC20(address,address,uint256)` and `sweepERC20(address,address)`, then invoked `pullERC20` against three USDC-pre-approved EOAs in the same tx. **456,442 USDC** swept (~99% from one victim `0x2e933518068b1c…`). The diamond was created 2026-03-17 (within Layer 3's monitoring window) but never entered our `contracts` table — primary detection gap. Distinguished from the Renegade and Wasabi sub-mechanisms because the upgrade primitive is *fine-grained per-selector facet registration* (not whole-implementation replacement), letting the attacker add a single hostile function while the rest of the diamond's surface stays trusted-looking. See `cases/CASE_AURELLION_DIAMONDCUT_20260512.md`.
- **Grok/Bankr exploit (2026-05-04) — *cross-domain agent-coordination sub-mechanism*.** A cross-domain variant. Grok's wallet trusted the Bankr NFT (which expanded permissions); Bankr trusted Grok's tweets. The attacker injected a prompt that traversed the entire trust chain: Twitter → Grok → Bankr → Base blockchain. No single component understood the full story; all compliantly participated.

**Cross-references.** [Confused Deputy Problem](#confused-deputy-problem) (the parent concept; this entry is the multi-contract systemic form), [Compositional Harm](#compositional-harm) (Distributed Confused Deputy Chains are the specific mechanism of compositional harm in modular architectures), [Forced Deterministic Neutrality](#forced-deterministic-neutrality) (the execution environment's inability to pause or question the chain), [Stored Potential](#stored-potential) (the proxy upgrade mechanism is a classic stored-potential node), [Cross-Domain Compositional Harm](#cross-domain-compositional-harm) (the Grok/Bankr variant spans multiple domains).

**External taxonomy reference.** The "single point of syntactic failure" condition maps directly to `kadenzipfel/protocol-vulnerabilities-index` entries `categories/bridge/initialization-and-upgrade-flaws.md`, `categories/cross-chain/initialization-and-upgradeability.md`, `categories/cdp/initialization-and-upgradeability.md`, `categories/staking-pool/initialization-vulnerabilities.md` — the unprotected-initializer class that the Renegade exploit anchors.

---

### Camouflage Ratio

**Definition.** The percentage of dangerous contracts that maintain low revert rates (under 10%) to evade standard detection. Stable at 70–79% across chains, organizations, and time.

**Extended description.** Interpreted as a Nash equilibrium — operators calibrate against detection tools at scale. Running too aggressive (high revert rate) loses victims to detection; running too conservative loses efficiency. The market converges on the temperature at which exploitation is optimally invisible. Stable across Base (~82%), Arbitrum (~70%), and Optimism, across two weeks of observation, and across four mapped organizations.

**Empirical robustness (2026-04-29).** The 2026-04-25 caveat asked whether the camouflage ratio was an artifact of the top-12 funder cluster's calibration (the cluster represents ~39% of the active deployer subset per `scripts/funder_metrics.py`). The test was run as Section A7 of `reports/epistemic_test_results_2026-04-29.md`. Result: full corpus 67.1%, top-12-excluded cohort 68.1%, delta +0.9pp. Well below the 5pp threshold that would have indicated the cluster was driving the equilibrium. The equilibrium is stable across operator classes; this strengthens rather than weakens the claim that the ratio reflects a structural Nash equilibrium rather than an artifact of any single operator's calibration.

**Empirical grounding.**
- `camouflage_metrics` table populated nightly via `surveillance/camouflage_tracker.py`. Corpus-wide ratio stable at 79.2% across the initial 9-day run (2026-03-17 through 2026-03-25) before the producer cron died (fixed in Correction #7).
- Dataset: 5,845 camouflaged victims vs 233 overt-trap victims (25:1 ratio).
- Deck: `l3-narrative/Digital_Physics_Blockchain_Security.pptx` slide 7 frames this as a behavioral equilibrium, not a bug.

**Cross-references.** [Trust Amplification Factor](#trust-amplification-factor), [Behavioral Laundering](#behavioral-laundering), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (the feedback loop that produces the equilibrium), [Infrastructure-Scale Operator](#infrastructure-scale-operator) (the corpus-dominance finding that requires the camouflage ratio to be re-computed against a cluster-excluded cohort).

---

## Detection Methodology

### Behavioral Laundering

**Definition.** The architectural analog of cash laundering. Predators manufacture legitimate-looking deployer histories, organizational infrastructure, or cross-chain reputations to defeat behavioral detection.

**Extended description.** Six documented patterns (A–F) represent distinct techniques operators use to evade behavioral-layer surveillance. This is the natural evolution of [Camouflage Ratio](#camouflage-ratio) — camouflage at the contract level is operators calibrating individual contracts; behavioral laundering is the same game at the deployer, organizational, and reputational level.

**Empirical grounding.**
- Framework scoped in `reports/behavioral_laundering_detection_scope.md`.
- Pattern D is the strongest validated (54% of 100 high-risk recent L2 deployers have Ethereum mainnet history we weren't linking — Tier A via Etherscan v2 multichain, `reports/cross_chain_import_candidates.md`).
- Pattern F scanned negative against the 30-day corpus but structurally scoped (`reports/advisor_parasite_candidates.md`).
- Other patterns (A, B, C, E) scoped and partially scanned; see individual pattern entries below.

**Cross-references.** All Pattern entries below. [Camouflage Ratio](#camouflage-ratio). [Strategy Lifecycle](#strategy-lifecycle) (how laundering patterns propagate). [Pristine Solo Operator](#pristine-solo-operator) and [Infrastructure-Scale Operator](#infrastructure-scale-operator) (deployer-layer and funder-layer instances of behavioral laundering, both shipped 2026-04-25). [Adversarial Vanity Branding](#adversarial-vanity-branding) (vanity-prefix selection is an additional behavioral-layer signal; the three documented sub-categories — operational, anti-forensic, funder — each target a distinct surveillance surface).

---

### Pattern A — Reputation-Building Sacrifices

**Definition.** Deployer operates one or more legitimate-looking projects first (working contracts, real liquidity, real users, measurable activity), then launches a weaponized contract counting on prior reputation to discount risk scoring.

**Extended description.** Detection signal: deployer has a trajectory of early deployments with substantive activity and clean behavioral profile, followed by a single high-stakes deployment with different bytecode family and different behavioral signature. The delta between the trajectory's median risk score and the final deployment's score is the behavioral fingerprint.

**Empirical grounding.**
- Scanned 2026-04-18 (`scripts/pattern_a_scan.py`, report: `reports/reputation_sacrifice_candidates.md`).
- Result: **4 candidates out of 5,810 deployers** with ≥5 contracts. Narrow but clean.
- Canonical candidates: `0x614737b6…9271` (5 contracts, 23.8-day trajectory on Base), `0x5eb7a658…8ea3` (11 contracts, 21.5 days), `0x809088…23db` (11 contracts, 10.4 days, Arbitrum), `0x021868f2…0321` (18 contracts, 7 days).
- Re-scan trigger: corpus age ≥ 90 days. Too few candidates today to justify building `deployer_trajectory_analyzer` module; flagged for future build decision.

**Cross-references.** [Pattern E — Fake Legitimate Projects](#pattern-e--fake-legitimate-projects) (next-level variant where the operator uses separate wallets), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (reputation-trust at the victim-relationship level).

---

### Pattern B — Temporal Pattern Normalization

**Definition.** Operators deliberately deploying on a Western-workday schedule (9-to-5 Europe-business hours UTC) to defeat timezone-based anomaly detection, despite other-dimension suspicion.

**Extended description.** Detection requires a deployer to sustain the pattern for ≥ 14 days with ≥ 0.7 window concentration (per-hour activity concentrated in the claimed window). Baseline: known criminal orgs cluster in `night_shift` (Americas 3 AM / Asia morning) and `asia_morning`; legitimate dev populations cluster in `europe_business` and `americas_afternoon`. A deployer whose pattern looks like a Western employee while scoring suspicious on other dimensions is a Pattern B candidate.

**Empirical grounding.**
- Scanned 2026-04-18 (`scripts/pattern_b_scan.py`, report: `reports/temporal_normalization_candidates.md`).
- Result: **0 candidates**. Only 29 deployers total meet the sustained-schedule filter at 30-day corpus age. Baseline confirmed: `night_shift` over-indexes on traps (20% vs 0% for europe_business in the sustained-schedule cohort).
- Re-scan trigger: corpus age ≥ 60 days AND `weekend_activity_ratio` column added to `deployer_profiles`.

**Cross-references.** [Behavioral Laundering](#behavioral-laundering), `surveillance/deployer_profiler.py` (source of `timezone_guess`, `peak_hour`, `active_window_start`, `hour_concentration`).

---

### Pattern C — Funding Chain Laundering

**Definition.** Routing operational capital through CEX hot wallets so that `auto_funder_tracer` concludes "legitimate origin" despite pre-CEX trap-adjacent wallet activity.

**Extended description.** Detection discounts the risk score when funding traces to a legitimate CEX. Pattern C exploits this by making the CEX the most recent hop in a longer chain. The corrective move requires one-hop-back RPC trace: follow the deployer's CEX-withdrawal back to the user's prior deposit into that CEX hot wallet, and cross-reference the pre-CEX source against known criminal wallets.

**Empirical grounding.**
- Scanned 2026-04-18 SQL-only (`scripts/pattern_c_scan.py`, report: `reports/cex_laundered_funding.md`).
- Result: 10 CEX hot wallets in our `entity_classification`. 26 deployers funded from them. **0 strict candidates** (CEX-funded AND confirmed trap). **4 relaxed candidates** (CEX-funded AND suspected-heavy): `0x4885631c…0edd` (37 contracts, 13 suspected), `0x6dc136bc…af56` (19 contracts, all suspected), `0xb87e28fc…f828` (7 all suspected), `0x561d79e9…4d77` (3 all suspected).
- Re-scan trigger: one-hop-back RPC trace approval (~20 Alchemy calls for the 4 candidates).

**Cross-references.** [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import) (`0x4885631c…` flagged by both C and D). `surveillance/auto_funder_tracer.py` (the pipeline Pattern C exploits).

---

### Pattern D — Cross-Chain Reputation Import

**Definition.** Building legitimacy on one chain then appearing on target chains with pre-established trust that per-chain monitoring doesn't catch.

**Extended description.** A deployer appears on Arbitrum or Optimism for the first time with no prior activity in our corpus, but the SAME address has substantial history on Ethereum mainnet or Base. Per-chain profiling sees a fresh-to-L2 deployer; cross-chain view reveals a long-standing identity that may have pivoted from legitimate activity to trap deployment. Alternative: the operator uses address-reuse across chains specifically because single-chain monitoring misses the connection.

**Empirical grounding.**
- Scanned 2026-04-18 via Etherscan v2 multichain (`scripts/pattern_d_scan.py`, report: `reports/cross_chain_import_candidates.md`).
- **Result: 54 of 100 high-risk L2 deployers had mainnet first-tx predating L2 first-seen. The strongest-supported pattern of the six.**
- Longest gap: `0x7fd9a5104f…60d0` — Ethereum mainnet first-tx 2017-06-20, L2 first-seen 2026-04-02 = **3,208 days** (8.8 years). 14 suspected contracts on Base.
- Production-ready enrichment shipped: Correction-adjacent work added `deployers.mainnet_first_tx` column and one Etherscan v2 call per new deployer in `auto_funder_tracer` (2026-04-18, commit `9d1d337`). Backfill for existing 36k+ deployers running at time of writing.
- Also validated in **EXTRACTION_004 (Rhea)**: the Rhea Subject Wallet was funded via `intents.near` cross-chain bridge — the NEAR analog of Pattern D (cross-chain import *via bridge* rather than *via address-reuse*).

**Cross-references.** [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (orthogonal — victim-extraction cadence), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset) (Pattern D enrichment grows in value as more addresses accumulate history), [Pristine Solo Operator](#pristine-solo-operator) (related but distinct — Pattern D imports active mainnet reputation; pristine-solo exploits dormant mainnet age).

---

### Pattern E — Fake Legitimate Projects

**Definition.** Projects with real liquidity, real users, real trades but economics that don't support continued operation, functioning as reputation-building sacrifices.

**Extended description.** Harder to detect than A–D because the "legitimate phase" has no trap bytecode. Signature: a project winds down in a controlled way (not rug-pull) and its accumulated capital recycles into new deployer wallets that subsequently run trap operations. Detection is inherently graph-based (project controllers → intermediate wallets → new deployer → new contract), not per-contract.

**Empirical grounding.**
- Methodology proposed 2026-04-18 (`reports/fake_project_detection_methodology.md`). Three-phase approach: wound-down project detection → capital recycling tracer → destination deployer evaluation.
- Not scanned; blocked on corpus age ≥ 60 days AND approval for a forward-direction capital-flow tracer module.
- Estimated implementation cost: ~5 days focused work.

**Cross-references.** [Pattern A — Reputation-Building Sacrifices](#pattern-a--reputation-building-sacrifices) (same-deployer version; Pattern E uses multiple wallets).

---

### Pattern F — Advisor-Parasite Pattern

**Definition.** Trusted intermediary positions themselves as gateway to crypto and routes victim funds through self-controlled contracts at every step. Extracts via fees ("taxes"), compromised approvals, and routing tolls.

**Extended description.** Structurally similar to phishing drainers (hub-and-spoke approval pattern, many victims to one collector) but with a radically different **temporal signature** — months of small extractions, victims retain balance and keep interacting, no single-shot drain. Per-victim cadence 1–5 outbound transfers per month over extended duration. Phenomenologically distinct because the victim doesn't know they're being exploited; the advisor is consistently helpful. This is the relationship-of-trust variant of [Pattern A](#pattern-a--reputation-building-sacrifices).

**Empirical grounding.**
- Scanned 2026-04-18 (`scripts/advisor_parasite_scan.py`, report: `reports/advisor_parasite_candidates.md`; memorialized in `reports/behavioral_laundering_detection_scope.md`).
- Result: 16 candidates passed the structural filter (50+ unique approvers, ≥14-day duration, excluding known infrastructure and classified drainers). Every single one is either known DeFi infrastructure (1inch Router v6, LI.FI Diamond, Base Uniswap Router) or unidentified-but-non-advisor-shaped (per-user approval cadences too heavy or too light).
- **Zero confirmed advisor-parasites in current corpus.** Corpus age ≤ 30 days too short for months-long extraction pattern; `approval_events` doesn't index outbound Transfer flows (only approvals to flagged spenders).
- Confirmed counterexample: CE5E, E717, A7B9, E3B2 (`reports/case_CE5E_drainer_operation.md`). Each victim = one approval + one sweep. No retention, no relationship — classical phishing, not advisor-parasite. The handoff's framing that "some drainers might actually be advisor-parasites" is NOT supported by the drainers we've profiled.
- Re-scan triggers: (a) corpus age ≥ 90 days, (b) Transfer-event indexer deployed for ≥ 30 days, (c) `infrastructure_registry` grown to ~50 entries.

**Cross-references.** [Trust Amplification Factor](#trust-amplification-factor), [Cognitive Load Concentration](#cognitive-load-concentration), [Participatory Asymmetry](#participatory-asymmetry--predatory-literacy).

---

### Pristine Solo Operator

**Definition.** A deployer with a long mainnet history (typically >1 year, often >4 years) that has been dormant or low-activity at the mainnet layer, suddenly surfacing as the operator of a small (1–5 contract) high-confidence trap fleet on L2. The combination of a long pre-existing wallet age and a small recent operational footprint defeats both age-based clustering (deployer is not "new") and fleet-size-based clustering (deployer is not "prolific").

**Extended description.** A specific instance of [Stored Potential](#stored-potential) at the deployer level. The wallet's mainnet vintage is a stored capability — a long-lived address that confers reputational legitimacy in any system that weights age as a trust signal. When activated against L2 with a small trap fleet, the operator captures the trust premium of an aged wallet without the behavioral baseline a long-active wallet would produce. Detection signal is the conjunction: `mainnet_first_tx` >365d before L2 `first_seen`, fleet between 1–5 contracts, ≥1 confirmed trap, and the deployer is not already classified as part of an `org_wallets`, `org_candidates`, or `solo_operator_candidates` entry.

**Bidirectional exploitation surface (added 2026-04-30).** EXTRACTION_010 (mass dormant-wallet drain on 2026-04-30, `cases/CASE_DORMANT_WALLET_DRAIN_20260430.md`) inverts this entry's framing while sharing the same wallet class. The PSO entry as originally written describes 7+ year aged dormant wallets as **operators** — the attacker uses the wallet's reputational age as a trust signal at the deployment layer. EXTRACTION_010 describes the same wallet class as **victims** — the attacker drains the wallet's stored ETH/token value via key compromise. Both attack patterns rely on the same observation: long-dormant aged wallets are economically valuable and defensively neglected (the owner is not actively monitoring; defensive tooling treats the wallet as low-priority because nothing has happened in years). The PSO-operator picks them up to wear; the dormant-drainer picks them up to empty. The two roles are not mutually exclusive across a single corpus event, but they are mutually exclusive for a single wallet at a single moment — a wallet that's been emptied cannot be used as a PSO operator (no stored value to motivate further use), and a wallet being used as a PSO operator is by definition not the target of the dormant-drainer. The framework consequence: detection of "first activity from a long-dormant wallet" is the load-bearing signal for both attack directions; what distinguishes them is the *type* of activity that follows the awakening (deploy a contract → PSO operator; transfer out funds → dormant-drainer victim).

**Detection rule (refined 2026-05-09 per Correction #20).** The original detection signal (mainnet age > 365d + fleet 1-5 + ≥1 confirmed trap + not in existing org tables) **must be supplemented by an OLI public-tag check** before promotion. Any deployer with a public Open Labels Initiative tag indicating institutional/project identity (Web3 brand deployer, NFT project deployer, protocol deployer, exchange, bridge) is a false positive for this typology — the long mainnet age reflects institutional infrastructure, not adversarial dormancy. Use `surveillance.oli_enrichment.is_known_legitimate(conn, address)` at promotion time. **The behavioral signal is symmetric between predatory dormancy and institutional L2 expansion; only the identity layer disambiguates.**

**Institutional-deployer false-positive class (added 2026-05-09).** The 2026-05-09 mass audit identified 3 of 4 originally-promoted Pristine Solo Operators as OLI-tagged Web3 project deployers, not adversarial: `0x80b12bd0` → Animoca: Deployer; `0xa2a01b4a` → Stabilize Finance: Deployer 2; `0x147b8869` → Luchadores: Deployer. The fourth (`0xf6c99cec`) is not OLI-tagged but is not yet OLI-cleared either. Plus `0xbb50ce87` (industrial-scale variant) → Circle: contract deployer. **These five constitute the empirical anchor for the FP class.** Detection methodology lesson: a behavioral-only detector cannot distinguish "established operator expanding to a new chain" from "predatory dormancy with reputation cover." Same surface signal, different identity. See `reports/correction_log.md#correction-20` and `reports/blockscout_tag_audit_2026-05-09.csv`.

**Second-source URL provenance for the LOW-severity FP class (added 2026-05-09).** OLI tags for the four LOW-severity entries each carry a `tooltipUrl` field pointing to the project's public website. These are independently inspectable, providing a second source for the institutional attribution beyond the OLI tag itself:
- `0x80b12bd0` — Animoca / REVV Motorsport racing game: `https://www.revvmotorsport.com/` (REVV is a confirmed Animoca subsidiary product)
- `0xa2a01b4a` — Stabilize Finance: `https://www.stabilize.finance/` (DeFi yield aggregator, real protocol)
- `0x147b8869` — Luchadores: `https://luchadores.io/` (NFT collection, real project)
- `0xc5d133296e` — CryptoCauses: `https://crypto4ac.com/` (charity initiative, real project)
The `tooltipAttribution` field (which would indicate OLI-consortium provenance) is empty for these four, meaning they originate from Blockscout's own curation rather than a multi-source OLI consensus. This makes them lower-confidence than the HIGH-severity entries (which carry OLI/openlabelsinitiative.org attribution); a second-source confirmation via project disclosure or Etherscan label cross-check is the recommended next step before final watchlist removal. Until that is done, watchlist rows remain *active* with `[CORRECTION #20]` notes; entity_classification rows are NOT yet downgraded.

**Empirical grounding.**
- Detector module shipped 2026-04-25: `surveillance/pristine_solo_detector.py`. Scheduled daily at 5:45 UTC.
- New table `pristine_solo_candidates` with pending/promoted/dismissed workflow.
- First-day surface: 11 candidates locally, 13 on Railway.
- ~~Top finds by mainnet gap: `0x80b12bd0` (2,498-day gap = 6.8 years), `0xa2a01b4a` (2,314 days, fleet 4 on Arbitrum), `0x147b8869` (1,777 days, fleet 4), `0xf6c99cec` (≈1,750 days). All four promoted to watchlist HIGH.~~ **[CORRECTION #20: 3 of 4 retracted as OLI-tagged Web3 project deployers — see FP class section above]**
- ~~`0x80b12bd0` specifically tied to the `0x752c5a95` harvester investigation.~~ The harvester finding stands as a separate object — a confirmed-tier approval-harvesting contract was deployed by an Animoca-tagged wallet, which is a finding worth investigating in its own right (compromise, rogue developer, label staleness, or bytecode classifier needs review). The PSO framing of the deployer is retracted; the harvester behavior is unchanged.
- **Inversion case 2026-04-30:** EXTRACTION_010 surfaced 5+ confirmed 7-year-old wallets being drained by a single mainnet hub `0xA707034429c8…` in a 3.5-minute coordinated burst. Same vintage profile as PSO operators, opposite role. Mainnet-only — outside Layer 3's L2 monitoring scope, but the structural pattern reinforces that the aged-dormant-wallet class is bidirectionally exploited.

**Cross-references.** [Stored Potential](#stored-potential) (the concept this operationalizes at the deployer layer), [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import) (related but distinct: Pattern D imports active mainnet reputation; pristine-solo exploits dormant mainnet age), [Behavioral Laundering](#behavioral-laundering), [Cross-Domain Compositional Harm](#cross-domain-compositional-harm) (EXTRACTION_010 extends this to the key-management substrate, with aged-dormant wallets as the harm population), [Single-Purpose Infrastructure Funder](#single-purpose-infrastructure-funder) (parallel asymmetric-prior issue — see Correction #19 for the analogous detection-rule refinement).

---

### Infrastructure-Scale Operator

> **[CORRECTION #20 — 2026-05-09]** **The "Top-12 Infrastructure-Scale Operator" empirical anchor for this entry is at least 50% contaminated by actual CEX hot wallets and bridge solvers.** Specifically: `0x3304e22d` (Binance), `0x39591e7c` (OKX), `0x4e3ae00e` (MEXC), `0xfd92f4e9` (OKX), `0xbaed383e` (Bybit), `0xf70da978` (Relay bridge solver), `0x80c67432` (Orbiter Finance bridge) — 7 of 12 with confirmed institutional identities. The detector signal that surfaced them (high deployer-count fanout from a single funding wallet) **is the structural signature of CEX hot wallets and bridge solvers operating at scale.** It cannot, on topology alone, distinguish these from genuine infrastructure-scale adversarial operators. **The typology as previously written conflated two operator classes and remains valid in concept only after OLI cross-check is added at detection time.** The remaining 5 of 12 are not yet OLI-cleared and may still be either adversarial or un-tagged legitimate operators. See `reports/correction_log.md#correction-20` and `reports/blockscout_tag_audit_2026-05-09.csv`.

**Detection rule (refined 2026-05-09).** Promotion to this typology requires:
1. Funder topology criteria (≥200 fanout, ≥10% adversarial ratio, ≥50% disposable rate) — original signal, retained
2. **OLI cross-check passes** — `surveillance.oli_enrichment.is_known_legitimate(conn, funder_address)` returns no HIGH-severity institutional tag
3. **No CEX-hot-wallet signature** — funder address does not match the structural pattern of a CEX deposit/withdrawal address (single-key controlling thousands of unrelated downstream addresses with no operational coordination beyond funding)

**Definition.** An operator class that deliberately funds enough downstream deployer wallets to be classified as benign infrastructure (CEX, faucet, exchange hot wallet) by clustering heuristics that exclude high-fanout addresses. The exclusion logic that protects analysts from CEX/faucet noise is the same logic that hides this operator class. **Important post-correction caveat:** the same exclusion-evading topology IS the actual operating pattern of CEX hot wallets and bridge solvers. The typology only applies after public-label disambiguation rules out the legitimate-infrastructure interpretation.

**Extended description.** A direct counter-calibration against organizational mapping methodology. Org_xxx detection in Layer 3's prior framework targets cells of dozens to low hundreds of deployers. The infrastructure-scale operator scales an order of magnitude past that threshold specifically to defeat the heuristic. Per-funder profile diversity within the infrastructure-scale class spans at least three operational sub-types: pre-stage warehouses (zero detection signal in funded fleet), stockpile (high suspected, zero confirmed), and live-extraction (high confirmed). The 2026-04-29 cross-funder overlap probe (Section A4 of `reports/epistemic_test_results_2026-04-29.md`) ruled out the single-actor-with-many-faces and multi-tenant rental hypotheses: zero pairs of top-12 funders share any downstream deployer. **Post-Correction-#20 reframing:** the absence-of-overlap finding remains correct (CEX hot wallets and bridges also don't share customers across institutions), but the inference of "twelve independent infrastructure-scale operations" is retracted — most of those twelve are independent CEXes/bridges, not adversarial operators. The remaining open question is whether any of the OLI-untagged 5 remain genuine infrastructure-scale adversarial operators, and if so what selects for the operational pattern.

**Empirical grounding.**
- Discovered 2026-04-25 via funder probe of `0xf70da978` starting from `0x604be06b`'s funding chain.
- Canonical metrics: live figures from `scripts/funder_metrics.py`. Latest dated invocation: `reports/funder_metrics_2026-04-29.md`. Documents citing funder cluster scale should reference a specific dated invocation rather than transcribed numbers; figures grow with the corpus.
- Top funder `0xf70da978` (per 2026-04-29 metrics): 3,042 funded deployers, 8,118 contracts, 126 confirmed traps, 1,185 suspected. Larger than every existing org_xxx in the corpus combined.
- Top-12 funder fanouts (2026-04-29): combined 22,165 deployers, 42.7% of 51,874-deployer corpus, 39.4% of active deployer subset.
- Cross-funder overlap (2026-04-29, Section A4): 0 of 66 pairs share any downstream deployer. Twelve independent operations, none multi-tenant.
- Per-funder profile heterogeneity (2026-04-29, Section A5): suspected-ratio spread 0.0% – 99.8% across the top-12. Examples: `0xc43f317e` (1,871 deployers, 0 confirmed, 0 suspected — pre-stage warehouse); `0xfd92f4e9` (2,411 deployers, 0 confirmed, 889 suspected — stockpile); `0xf70da978` (126 confirmed, 1,185 suspected — live operator); `0x238d7170` (99.8% suspected ratio — anomalous fingerprint).
- 4 of top-12 funders are L2-native with no mainnet history — deliberate `eth_depth` evasion. Untraceable with current mainnet-scoped tooling.
- Detector class lives in `infrastructure_operator_candidates` (12 entries) separately from `org_candidates`. Schema includes funder_address, chain_signature, deployer_count, contract_count, confirmed_count, suspected_count, adversarial_ratio, disposable_rate, avg_fleet_per_deployer, mainnet/funder origin metadata.

**Drainer-spawn-hub overlap (added 2026-05-02).** A subset of Infrastructure-Scale Operators run as drainer-spawn hubs in addition to their broader stockpile/live-extraction profile. The hub spawns a sequence of self-deploying-trap-operator wallets on a regular cadence, each wallet executing one mass-drain campaign before being disposed. Two confirmed instances surfaced in the 2026-04-29 → 2026-05-02 drain wave: (1) `0xf7883e3fef23c8e645deba4b540549d78028a616` — 6 drainer iterations, ~2-day cadence April 7 → May 1, 859 total victims drained on Base; (2) `0x3304e22ddaa22bcdc5fca2269b418046ae7b566a` — 4 drainer iterations across March 25 → May 1, 404 total victims, including a single April 1 → April 4 iteration that drained 399 victims (the largest single-iteration drain count in the corpus). The 0x3304e22 hub is itself a documented top-12 Infrastructure-Scale Operator (rank #4 with 2,134 deployers per `reports/funder_cluster_diagnostic_2026-04-29.md`), confirming that the pre-stage-warehouse / stockpile / live-extraction sub-types of this entry can co-exist with active drainer-spawn within a single hub. The remaining 8 distinct drainers in the May 1 wave each have their own funder, so the wave is part-coordinated (1-2 hubs × N rotating drainer wallets) and part-convergent (independent operators using the same operational template). This refines the [Convergent Calibration](#convergent-calibration) reading: the absence-of-coordination claim still holds across the broader operator population, but is not universal — within any given drain wave a small number of hubs may be running multiple wallets that look independent on a per-drainer probe.

**Cross-references.** [Behavioral Laundering](#behavioral-laundering) (infrastructure scale is laundering at the funding-layer), [Adversarial Topology](#adversarial-topology) (position primitive: a funder concentrated enough to be excluded by heuristics is occupying the position designed for benign infrastructure), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (the exclusion logic is itself a published methodology adversaries calibrate against), [Adversarial Vanity Branding](#adversarial-vanity-branding) (`0xb0b0b69*` is both an instance of this entry and a vanity-branded operator), [Convergent Calibration](#convergent-calibration) (this entry's "twelve independent operations" finding is the population-level instance of that pattern; the drainer-spawn-hub overlap is the per-hub mixed-coordination instance).

---

### Single-Purpose Infrastructure Funder

**Definition.** A funding wallet that funds *exactly one* corpus deployer with a substantial fleet (≥50 contracts), where (a) the funder itself has no deployer record (a pure funding wallet, not a deployer also funding its own downstream), AND (b) the funded deployer is L2-only with no mainnet history. The opposite calibration of the [Infrastructure-Scale Operator](#infrastructure-scale-operator): instead of fanning out to thousands of deployers to evade the high-fanout-equals-CEX heuristic, this operator class commits a dedicated funder to *one* deployer per operation — evading the fanout heuristic from the other side, by looking too narrow to be a service rather than too broad.

**Detection rule (refined 2026-05-08).** Pattern A classification requires *both* layers to pass:
1. **Funder layer** — lifetime spawns = 1, funder is EOA-only (no own deployer record), funder is silent after the funding event.
2. **Downstream layer** — the funded deployer has `mainnet_first_tx IS NULL` (purely L2-native, no mainnet history).

The funder-layer check alone is insufficient. A wallet can show clean Pattern A funder signal (1 spawn, EOA-only) while sourcing a deployer that has years of mainnet history — that combination indicates a multi-chain operator using single-funder OPSEC, NOT a Single-Purpose Infrastructure Funder. The downstream check distinguishes the two. **Why both layers matter:** the typology is named for *infrastructure* — pre-positioned, dormant, L2-native deployment. A deployer with mainnet history fails the L2-native premise even if its funder looks single-purpose. See Correction #19 (2026-05-08) for the empirical case that surfaced this gap.

**Extended description.** The shape is structurally distinct from both the high-fanout funder (Infrastructure-Scale Operator) and the org-aligned funder (org_001-004 gas stations, which fund tens of deployers on a sustained schedule). One funder, one deployer, one funding event — then the funder is silent. The deployer's fleet is what carries the operational signal; the funder is a single-use clean wallet.

Three deployment shapes have been observed within the typology:
- **Burst-mass** — 1,000+ contracts in a single day or short window. Reference: `0x35ca5c210a7f` → `0xb3c07d462cbc` (3,161 contracts in 4 days, 100% suspected, peak 986/day on 2026-04-27); `0xda32de3eb2f0` → `0x0b701885fbee` (2,005 contracts in a single day on 2026-04-04, ~134/sec, all `unusual_fee_structure`-flagged).
- **Slow-drip** — 25-50 contracts/day for 30+ days, very few distinct bytecode hashes. Reference: `0x34aeddd42c9a` → `0xd660fa35cd16` (664 contracts on Arbitrum over 41 days, only 2 distinct deployed_code_hashes for the analyzed half).
- **Active-weaponized** — moderate fleet size with confirmed-tier contracts and trap activity. Reference: `0x7c8b9874f7be` → `0xc0ffeefeed8b` (Coffee Fleet, 286 contracts, 449 trap_events). Coffee Fleet is the previously-documented instance of this typology, originally classified standalone before the broader pattern was identified.

**Empirical grounding.**
- Discovered 2026-04-28 via funder concentration probe filtered to fleet ≥50.
- 69 confirmed Pattern A instances in corpus (pure-funding-wallet → 1 corpus deployer with fleet ≥50).
- Chain distribution: 71% Base, 24% Arbitrum, 5% Optimism. Zero mainnet operators — purely L2-native, deliberate eth_depth evasion (parallels Infrastructure-Scale Operator subset 4 of top-12). **Note (2026-05-08):** the L2-only property is now part of the detection rule, not just a corpus-distribution observation — see refined definition above.
- **False-positive class identified 2026-05-08.** Three May 7 candidates (`0x268cbda30dd2`, `0x04e3eebcb2f9`, `0xa7eccdb9be08`) showed funder-layer Pattern A signal but failed downstream-layer verification: `0x268cbda30dd2`'s deployer has mainnet history since 2025-03-17 (multi-chain bot operator with single-funder OPSEC, fleet across Base/Arb/OP, 0 drains); `0x04e3eebcb2f9` is self-funded (funder == deployer, 1,215-contract self-deployer); `0xa7eccdb9be08` is a 2022-vintage mainnet operator. None warranted Pattern A classification once the downstream check was applied. Initial framing as "fresh Pattern A funders" was withdrawn before any case-file or watchlist promotion. See `reports/correction_log.md` Correction #19.
- 84% of these fleets have *zero* recorded user interaction (no approvals, no traps, no drains). Most are pre-positioned dormant infrastructure. 12 of 69 (17%) have any trap activity; only 3 of 69 have ≥1 confirmed drain.
- Reference burst case `0xb3c07d462cbc` had its first user approvals 4 days after deployment: 24 total, 17 from one address (`0xaee967b15e76`) approving 10 distinct contracts in a 16-minute window on 2026-04-28T05:30 UTC. Approver/bait dynamic open — could be a mass-approving bot, a self-test sequence, or a real victim caught in the bait window.
- Vanity-mirrored funder/deployer pairs do occur: `0x4200a4790e7f32d36759b040cff0227f33ee4f25` → `0x30efa4790e7f32d36759b040cff0227f33ee3e14` share trailing 36 hex chars except the final byte. CREATE2 vanity mining of *both* the EOA and a destination address strongly implies coordinated pre-mining. Cross-references the [Adversarial Vanity Branding](#adversarial-vanity-branding) operational-branding sub-type.
- None of the 4 active operators (3 drainers + Coffee Fleet) attribute to org_001-004 by funder, deployer, or bytecode-family overlap. This typology is structurally separate from the org architecture.
- No instance of single-purpose funder appearing in `org_wallets` or upstream of an org gas station. The funder-deployer pair operates as a closed unit.

**Cross-references.** [Infrastructure-Scale Operator](#infrastructure-scale-operator) (the opposite calibration — high-fanout vs. zero-fanout-beyond-target), [Adversarial Topology](#adversarial-topology) (the funder's position primitive: too narrow to be a service, too disconnected to be an org gas station), [Behavioral Laundering](#behavioral-laundering) (funding-layer separation that defeats funder-clustering heuristics), [Adversarial Vanity Branding](#adversarial-vanity-branding) (vanity-mirrored funder/deployer pairs), [Stored Potential](#stored-potential) (84% dormant rate is the stored-potential signature: deployed but not yet exercised).

---

### Adversarial Vanity Branding

**Definition.** Deliberate use of vanity-mined address prefixes (typically ≥5 hex chars, requiring ≥1M generation attempts) by adversarial infrastructure. Three documented sub-categories: operational branding (the prefix marks bots or contracts that visibly transact), anti-forensic spoofing (the prefix targets truncated-display heuristics in monitoring tools), and funder branding (the prefix marks only the funding source while the downstream fleet uses random-prefix wallets).

**Side-note (2026-05-07 refinement).** Vanity-prefix mining is *class-neutral* as a primitive — the same compute spend produces both adversarial-side prefixes (`0xc0ffee*`, `0xb0b0b69*`, `0x01989c93890aed05*`) and legitimate-side prefixes deployed by protocols and operators with no adversarial intent. The TrustedVolumes RFQ proxy `0xeEeEEe53033F7227d488ae83a27Bc9A9D5051756` (1inch market maker / resolver, victim-class in EXTRACTION_011) is a clean legitimate-side instance: 7-hex-char `0xeEeEEe5` prefix on a protocol-deployed proxy that was itself the exploited contract. **Diagnostic implication:** vanity prefixes signal *intent and operator identity*, not *adversarial alignment*. The signal must be paired with role classification (deployer vs. funder vs. victim-protocol) before being read as adversarial.

**Extended description.** Vanity-prefix selection is non-random and traceable to deliberate compute spend. When an adversary chooses to mine a vanity prefix despite the operational-security cost (mining time + reuse of a memorable identifier weakens unlinkability), the prefix carries information: identity, trust signal, or anti-forensic intent. Layer 3 surveillance can use the presence and scope of vanity prefixes as a behavioral signal independent of bytecode patterns or transaction-graph clustering.

The three documented sub-categories are not interchangeable — they target different layers and threat models:

- **Operational branding** marks the layer that visibly transacts with victims (bots, scanner contracts, the trap-deployer wallet itself). The Coffee Fleet (`0xc0ffee*` prefix on 84 victim bots + the deployer `0xc0ffeefeed8b9d271445cf5d1d24d74d2ca4235e`) is the canonical instance. Branding at this layer signals an integrated operation where the same actor controls both the trap-deployer and the bots that "fall into" it — observed-harm theater for downstream risk scorers.

- **Anti-forensic spoofing** mints a vanity address with an N-byte prefix collision against an existing legitimate address (typically 7+ hex chars / 4 bytes matching), exploiting the convention of truncated-prefix display in dashboards and analyst workflows. org_001's Shadow Wallet 1 (`0x01989c93890aed05a63d179b03424997075b6acf`, colliding with the legitimate LP_POOL_2 at `0x01989c93890aed05cbcda4e62eec1b2eb4c55b1b` at 8 bytes / 16 hex chars) is the canonical instance. Branding at this layer targets the intelligence layer — chain analysis tooling, organizational dashboards, human review workflows.

- **Funder branding** marks only the funding source while the downstream fleet uses anonymized random-prefix wallets. `0xb0b0b6903489cc56bf037cb2f5ba986e2775bb07` (`0xb0b0b69*` — Optimism mass-deployment funder) is the canonical instance. The funder vanity is most plausibly read either as operator self-signature visible across multiple campaigns, or — more interestingly — as a brand mark for a wallet/infrastructure-rental service whose buyers need a recognizable source. Funder branding is a reverse choice from the standard operational-security playbook (which would obscure the funder hardest); the existence of the choice is itself the diagnostic signal.

**Empirical grounding.**
- **`0xc0ffee*`** (Coffee Fleet): 84 vanity bots in `bot_candidates` + 1 vanity deployer (`0xc0ffeefeed8b9d271445cf5d1d24d74d2ca4235e`). 100% c0ffee-on-c0ffee victim overlap as of `surveillance/data/cases/CASE_COFFEE_FLEET_0xc0ffeefeed8b.md` (2026-04-08). Single-operator hypothesis still leading.
- **`0x01989c93890aed05*`** (org_001 vanity spoof): 2 wallets — the legitimate LP_POOL_2 and the vanity-spoofed Shadow Wallet 1. Documented in `surveillance/data/cases/CASE_ORG_001_INFRASTRUCTURE.md` Anti-Forensic Capability section (discovered 2026-04-11).
- **`0xb0b0b69*`** (Optimism funder): 1 funder, 6,605 random-prefix downstream deployers, ~5,775 contracts using bytecode hash `476b15536fa9703e2c630e91ac976c514e1868a70e8c996f1bf8bb97a9b9e532` in a 2026-04-25 mass-deployment campaign. Pre-stage interval: 10 days dormant between funder creation (2026-04-15, 7 test deployers) and mass-deployment burst (2026-04-25, 6,598 deployers in one day). Documented in `docs/INDEX.md` Section 1 + Section 5.
- **`62ac…EE8A` victim-mimic cluster** (Ethereum, 2026-05-11) — **fourth sub-category** introduced 2026-05-11: *victim-mimic vanity*. Attacker generated 3 wallets sharing the 8-char shape of an active drain victim (62ac start + EE8A end, random 32 middle chars), routed dust + worthless memecoins through them concurrent with the real drain, then mixed them into the inflow set on the attacker EOA. Distinct from operational / anti-forensic / funder sub-categories because the mimicry target is the *victim* (downstream-relational), not the operator or a legitimate institution. Compute cost ~268M attempts per address for the prefix alone, doubled for the suffix — ≥1 GPU-hour per generated wallet. Purpose hypothesis: trail confusion (pad inflow count to muddle attribution) + forward address poisoning (prime future copy-paste mistakes). Pre-positioning window: one of the three wallets had its first tx 6 days before the drain. Documented in `surveillance/data/cases/CASE_PRIVATE_KEY_DRAIN_F7CFFC27_20260511.md`.
- **Compute cost for a 7-hex-char vanity prefix:** ~268M generation attempts on average. Visible cost — this is not zero-cost obfuscation. The cost is itself the signal that the prefix is intentional.
- **Singularity check:** `0xb0b0b6*` is the only such address in the corpus. No vanity siblings, no rotation. Compare to Coffee Fleet (84+1 across its prefix) and org_001 spoofs (2 across its prefix).

**Cross-references.** [Behavioral Laundering](#behavioral-laundering) (vanity branding is a behavioral-layer signal complementing bytecode and graph signals), [Infrastructure-Scale Operator](#infrastructure-scale-operator) (`0xb0b0b69*` is both an instance of this entry and a vanity-branded operator), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (anti-forensic vanity targets the analyst tooling that publishes truncated addresses), [The Self-Cannibalizing System](#the-self-cannibalizing-system) (Coffee Fleet's c0ffee-on-c0ffee operation is the closed-loop variant where the same operator runs both predator and prey roles), [Protocol-Family Specialist Operator](#protocol-family-specialist-operator) (legitimate-side vanity contrast: the TrustedVolumes RFQ proxy `0xeEeEEe53033F7227d488ae83a27Bc9A9D5051756` is operator-deployed-but-victim-class — same prefix-mining cost, opposite role).

---

### Protocol-Family Specialist Operator

**Definition.** A threat actor who exploits multiple **independent vulnerabilities** within a single protocol family (or trust-graph) over time, accumulating specialized knowledge about a target ecosystem rather than rotating across protocols. Distinct from Pattern D (Cross-Chain Reputation Import) — Pattern D ports the same operator across chains/wallets; Protocol-Family Specialists port the same operator across vulnerability classes within one ecosystem.

**Extended description.** The standard threat model assumes attacker → finds bug → exploits once → moves on. The Protocol-Family Specialist inverts this: the attacker stays, develops domain knowledge, and returns when a different bug surfaces. Three signals distinguish this typology from coincidental recurrence:

1. **Same operator EOA / linked-cluster reuse across the events** (not just thematic similarity).
2. **Different vulnerability classes** (a re-exploit of the same bug is an unpatched-recidivist case, not specialism).
3. **Same protocol family or trust-graph** (1inch core ↔ 1inch resolvers ↔ RFQ proxies count as one family because they share the routing trust topology).

The typology matters for defense because it predicts the *next* incident's victim class: a Protocol-Family Specialist's prior targets are the strongest forward indicator of their next target. Standard threat-actor enumeration (rotating-attacker model) gives no such signal.

This entry is structurally distinct from [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import) — Pattern D moves *the operator's history* across chains to launder reputation; Protocol-Family Specialism keeps the operator history visible and accumulates *target-specific knowledge*. The two can co-occur but answer different questions: Pattern D explains why an operator looks clean on a new chain; Protocol-Family Specialism explains why a single trust-graph keeps producing the same exploiter.

**Empirical grounding.**
- **EXTRACTION_011 (TrustedVolumes / 1inch RFQ proxy, 2026-05-06).** Exploiter `0xC3EBDdEa4f69df717a8f5c89e7cF20C1c0389100` extracted ~$5.87M (1,291.16 WETH + 206,282 USDT + 16.939 WBTC + 1,268,771 USDC) via custom RFQ swap proxy `0xeEeEEe53033F7227d488ae83a27Bc9A9D5051756`. Same operator as the **March-2025 1inch Fusion V1** incident; different vulnerability class (RFQ-proxy logic vs. Fusion V1 settlement flaw). 14-month gap between incidents — too long for opportunism, too short for unrelated activity. Source: Blockaid exploit-detection disclosure.
- **Counter-example (rotating-attacker baseline).** Generic phishing drainer wallets in the L2 corpus (e.g., the May-6 self-deploying drainer cohort `0xfbf44e96`, `0x73c0c56b`, `0x4c89f508`) hit different victims with the *same* technique once and rotate; they are not Protocol-Family Specialists because they lack target-specific accumulation.

**Detection signal.** Cross-reference exploit lists by **operator EOA**, not by victim protocol. Cluster operators that appear ≥2 times against the same protocol-family trust-graph with **different** vulnerability classes. The signal is strongest when the inter-incident gap is months (long enough that the operator could have left, didn't) and when the second vulnerability requires reading the protocol's internal architecture (long enough study time).

**Layer 3 corpus involvement.** Zero direct coverage — TrustedVolumes is Ethereum mainnet, outside Base/Arbitrum/Optimism scope. Same gap pattern as EXTRACTION_009 (Wasabi) and EXTRACTION_010 (mass dormant-drain): the typology is observable in off-chain reference data but not in the L2 corpus. The classification is structural, not corpus-derived.

**Cross-references.** [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import) (the cross-chain analog; Protocol-Family Specialist is the within-ecosystem mirror), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (RFQ proxies are configuration-class — signed-quote acceptance scope is the soft surface), [Compositional Harm](#compositional-harm) (1inch routing → resolver → custom RFQ proxy is a three-layer composition; specialist exploits the seams between layers), [Trust Amplification Factor](#trust-amplification-factor) (the @trustedvolumes brand inherits 1inch routing trust without inheriting 1inch's audit surface).

---

### Self-Deploying Single-Contract Mass-Drain

**Definition.** A drain operation in which a single EOA acts as **both deployer and drainer** of exactly one contract, paired with a dedicated single-purpose funder wallet. Within a tight time window (typically <24h), the operator: (1) receives funding from a previously-silent funder, (2) deploys one contract, (3) drives mass victim approval-spending against that contract, and (4) goes silent. The operator wallet has fleet=1 (one contract lifetime) and a clean record beyond the single drain event. The funder wallet has 1-2 corpus deployers funded (this drainer plus possibly one prior). The two-wallet pair is consumed by a single iteration.

**Extended description.** Architecturally distinct from both the [Single-Purpose Infrastructure Funder](#single-purpose-infrastructure-funder) pre-stage stockpile (which deploys ≥50 contracts without extraction) and from drainer-spawn hubs like `0xf7883e3fef23` (where a persistent hub funds rotating disposable drainer wallets, each running one campaign). The Self-Deploying Single-Contract Mass-Drain has:

1. **No persistent upstream hub** — the funder is also single-use; there is no scheduler-layer actor visible.
2. **Self-deployment** — drainer EOA is the contract's deployer, eliminating the funder-→-deployer-→-drainer chain that other operator classes use to compartmentalize.
3. **Single-contract operation** — fleet=1; the drainer is the contract's *only* downstream. By contrast, infrastructure-scale operators run many contracts per iteration and pre-stage stockpilers run many contracts per iteration with no contracts drained.
4. **Mass-drain via approval-spending** — victims have prior MAX-allowance approvals on the contract (typically Permit2-class); the drainer sweeps in a tight time window using `transferFrom`-style flows. The operator does not need bot interaction or victim transactions during the drain window; only pre-existing approvals.

The shape resembles a [Single-Purpose Infrastructure Funder](#single-purpose-infrastructure-funder) Pattern A *activation event* — Pattern A's pre-stage stockpile is the "what's loaded," the Self-Deploying Mass-Drain is the "what discharge looks like." But the corpus instances do not match Pattern A's stockpile signature (no pre-positioned fleet); the drain contract is freshly-deployed in the same operator wallet.

**Detection rule (promoted to typology 2026-05-10 with three confirmed instances).** Required signals:

1. **Funder layer** — pure funding wallet (no own deployer record), funds 1-2 corpus deployers, no public OLI tag, no shared infrastructure with documented org_001-004 or top-12 ISO funders.
2. **Drainer layer** — same address is both the EOA receiving funds AND the deployer of exactly one contract. `fleet = 1`.
3. **Drain layer** — `approval_watchlist.drain_detected = 1` for ≥10 distinct victims with `drain_caller` = the drainer EOA, concentrated within a single 24-72h window.
4. **OLI cross-check passes** — neither funder nor drainer is publicly attributed to a known institution (per [Pristine Solo Operator](#pristine-solo-operator) FP class lesson).

The third condition is what distinguishes activation events from the pre-stage variant: extraction is observable and bounded in time. The four-condition gate avoids the false-positive class that Correction #19 documented (self-funded farmers with no drain signal).

**Empirical grounding (three confirmed instances, 2026-05-06 → 2026-05-10).**

| Iteration | Drainer EOA | Funder | Funder class | Victims | Drain window |
|---|---|---|---|---|---|
| I (2026-05-06) | `0xfbf44e969d4fc5cbad62870207341c976f9e38f9` | `0x8c826f795466e39acbff1bb4eeeb759609377ba1` | **org_001 L2 Gas Station** (Coinbase-origin, 1,296 corpus deployers funded) | 113 | 2026-05-06 single-day |
| II (2026-05-07) | `0x44a2ee1369c3eecf86f8de7c73c3e3602523a198` | `0x68b8b6d48dc6529d7eb4c7943613e04ba2e5b913` | **Single-purpose funder** (1 deployer funded, OLI-clean) | 37 | 2026-05-07 10:55 → 17:25 (6.5h) |
| III (2026-05-09→10) | `0x72ed7949080a2c57bfe9788a7970fe39629fc6ca` | `0x8c8204b8da3defb2a2f525fa35f5026080963579` | **Single-purpose funder** (1 deployer funded, OLI-clean) | **148** | 2026-05-09 10:59 → 2026-05-10 09:49 (22h) |

**Zero funder overlap across the three instances** — three distinct funders, one of which is org_001's known gas station and two of which are unattributed single-purpose wallets. The architecture is identical; the operator identity differs. This is [Convergent Calibration](#convergent-calibration) at the execution layer — three independent actors running the same operational template within a 5-day window with no observable coordination.

**One instance (I) is operationally linked to a documented organization (org_001). The other two (II, III) are unattributed.** The org_001 instance is also documented in INDEX.md as the May 6 escalation event (CASE_ORG_001_INFRASTRUCTURE.md update) and marks the first confirmed direct-org-drainer linkage for org_001. The convergence of org_001's playbook expansion with two independent operators running the same architecture in adjacent days raises the question of whether the technique itself is the diffusing object (shared upstream tooling, shared training data, or convergent calibration against the same defensive surface).

**Forward signal.** Inter-event interval observed: 1 day (I→II), 2 days (II→III). If the cadence is real, expect a fourth instance within 1-3 days of III; if absent for >5 days, the cadence framing weakens. **As of 2026-05-10 15:43 UTC, the III drainer (`0x72ed7949080a`) continues active drainage on contract `0xa68079da060e...` (most recent victim 2026-05-10 09:49 UTC); active operations should be considered concurrent with the next-iteration forecast.**

**Distinguishing from neighboring typologies:**
- **Vs. Single-Purpose Infrastructure Funder**: Pattern A stockpile has fleet ≥50 and no drain; this typology has fleet = 1 and active drain. The funder topology is similar (pure funder, 1-2 corpus deployers) but the deployer's behavior diverges.
- **Vs. drainer-spawn hub** (`0xf7883e3fef23` class): hub-spawned drainers are funded by a *persistent* hub that funds N rotating drainer wallets over N iterations. The Self-Deploying Mass-Drain has *no upstream hub* — funder and drainer are both consumed in one iteration.
- **Vs. Pattern E (Fake Legitimate Projects)**: Pattern E is about narrative cover (fake project → real-looking deployment → trap); this typology has no narrative cover, just the architecture.

**Cross-references.** [Single-Purpose Infrastructure Funder](#single-purpose-infrastructure-funder) (the pre-stage analog; this typology is what activation looks like), [Convergent Calibration](#convergent-calibration) (three independent funder identities running identical architecture in a 5-day window), [Behavioral Laundering](#behavioral-laundering) (operator-class evasion: the single-contract / single-funder shape is *too narrow* to look like a service, just as Infrastructure-Scale Operators evade by being *too broad*; both evasions operate on the same heuristic), [Strategy Lifecycle](#strategy-lifecycle) (the III instance's 148-victim count exceeds I and II — the typology may be entering a growth phase, not a stable cadence), [Stored Potential](#stored-potential) (the unattributed funder wallets are themselves stored potential — they have no observed activity until the activation event; their pre-existence is the position primitive).

---

## Structural and Psychological

### Participatory Asymmetry / Predatory Literacy

**Definition.** The asymmetric relationship where threat actors and regular users share access to the same interfaces and information but differ radically in the ability to interpret adversarial patterns.

**Extended description.** Cannot be resolved through disclosure because the information is already public. Users and attackers both see Permit2 allowances as readable state; both see `EndpointV2.getConfig` returns; both see DVN addresses. The attacker reads "rsETH OFTAdapter has requiredDVNCount=1" as an exploitation opportunity; the user doesn't know how to form the query, let alone what it means. Resolution requires distributing *interpretive literacy* through specialized intermediaries — Layer 3, wallet providers with active screening, protocol foundations with architectural review capacity.

**Empirical grounding.**
- Kelp retrospective (`reports/kelp_retrospective_replay.md` Phase 3): the 1-of-1 DVN was publicly readable for ≥56.7 days. The information was not hidden — the literacy was. Every rsETH holder could theoretically have run `getConfig(configType=2)`; the asymmetry is that almost none of them know the call exists or what the output means.
- Compare to EXTRACTION_006 (Aethir): single-EOA adapter owner was on-chain-readable; the dev.to post-mortem states "The protocol had no multisig. They had no time wait mechanism. In 2026, this is not an acceptable level of operational security." The unacceptability was information-available; the enforcement was literacy-absent.

**Cross-references.** [Cognitive Load Concentration](#cognitive-load-concentration), [The Detection Gap as Product](#the-detection-gap-as-product) (the commercial resolution of participatory asymmetry).

---

### Static vs Dynamic Behavior

**Definition.** Bitcoin secured static behavior (ledger entries). Ethereum introduced dynamic behavior (state-modifying programs). The security layer appropriate for static systems does not transfer to dynamic ones.

**Extended description.** Bitcoin's threat model is "is this signature valid? is this input spent?" — questions about static records. Ethereum's threat model is everything Bitcoin's is PLUS "what does this program do when called?" — dynamic execution introduces behaviors that cannot be audited by snapshot examination. Every attack in Layer 3's corpus is a dynamic behavior failure. None would have been possible on Bitcoin's UTXO model because the attack mechanisms require state-modifying programs.

**Empirical grounding.**
- **EXTRACTION_001–008 inventory as dynamic-behavior failures.** Drift (governance state transition), Rhea (slippage aggregation logic), Aethir (admin ownership as mutable state), Hyperbridge (MMR proof validation), Kelp (DVN configuration state). None of these are failures of static ledger integrity.
- Deck: `l3-narrative/Digital_Physics_Blockchain_Security.pptx` frames this as the categorical distinction: physics vocabulary (stored potential, phase transition, entropy) describes dynamic behavior; traditional security vocabulary (vulnerability, patch) was built for static-adjacent defect models.

**Cross-references.** [Compositional Harm](#compositional-harm), [The Proofreading Trap](#the-proofreading-trap).

---

### Cost-Habituation Asymmetry

**Definition.** Traditional finance distributes cost across institutions, keeping per-action cost at zero for users. DeFi concentrates per-action cost in users, establishing a baseline of paying for actions that normalizes extraction.

**Extended description.** In traditional finance, a user swiping a credit card pays zero marginal cost per transaction; the cost is borne by the merchant's interchange fee and the bank's operational overhead. In DeFi, every transaction requires the user to pay gas — a small, visible, explicit cost. The baseline "crypto costs money per click" is established. Once paying per action is normal, marginal extraction by predators is psychologically invisible: a 0.1% "routing fee" surcharge looks identical to gas volatility, a "bridge fee," or a protocol tip. The red flag that would trigger skepticism in a cost-free environment (Why am I paying? What is this for?) never fires.

**Empirical grounding.**
- **Micropayment relay pattern** observed on `0x68a96f41ff1e9f2e7b591a931a4ad224e7c07863` (benign x402 relayer): median per-tx $0.001, max $0.013, ~14K tx/day. Proves users have fully habituated to micropayment-scale friction. The same habituation enables micro-cost extraction to be invisible.
- Deck: `l3-narrative/Anatomy_of_a_Liquidation.pptx` documents the $0.01 gas cost per drain — the economics work because attacker-per-tx-cost is dust.

**Cross-references.** [Micro-Cost Habituation](#micro-cost-habituation) (the Weber-Fechner formalization), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern) (operational exploitation of the habituation), [Tuition Extraction Markets](#tuition-extraction-markets) (the market structure that this psychological mechanism sustains).

---

### Micro-Cost Habituation

**Definition.** Weber-Fechner application to DeFi cost perception: once baseline is "small cost per action," the just-noticeable-difference (JND) threshold shifts upward. Predators calibrate extraction to remain below the JND, producing psychologically invisible theft.

**Extended description.** Weber-Fechner law: perceived change in stimulus is logarithmic relative to baseline. A user habituated to ~$2 average gas per swap barely notices a $2.02 swap — the 1% increase is below JND. Extraction calibrated to stay inside JND is invisible on a per-event basis. Detection requires aggregation across time: individual events never cross the notice threshold, but cumulative extraction over weeks/months produces substantial loss the user only realizes in retrospect, if at all.

**Empirical grounding.**
- Behavioral framework applied to the `0xd4624228` trust-amplification parasite: each "swap" through the parasitic pool pulled a small fee the user didn't notice. Over 2,910 victims the aggregate reached ~100.56 WETH = $211K. No single victim recognized the loss as fraud.
- The CE5E drainer operation inverts this — fixed $10K/$20K chunks are ABOVE JND, which is why Pattern F (advisor-parasite) is a distinct commercial category from phishing drainers: advisors stay sub-JND per extraction, phishers take the whole balance in one visible event.

**Cross-references.** [Cost-Habituation Asymmetry](#cost-habituation-asymmetry), [Pattern F — Advisor-Parasite Pattern](#pattern-f--advisor-parasite-pattern).

---

### Cognitive Load Concentration

**Definition.** Traditional finance distributes security cognitive load across institutions (banks, regulators, insurance, merchants). DeFi concentrates it in individual users.

**Extended description.** A credit card user can ignore fraud prevention entirely — the bank runs detection, the regulator mandates loss caps, the merchant absorbs chargebacks. A DeFi user must personally evaluate every approval, every protocol, every bridge, every proxy upgrade, every multisig composition, every DVN configuration. Most humans cannot sustainably maintain the vigilance DeFi requires. The result is a specialization gap that an intermediate layer (wallet providers, protocol foundations, intelligence platforms like Layer 3) is structurally required to fill. Without that layer, users are load-bearing in a way they are not built for.

**Empirical grounding.**
- Documented at the victim level: 0x785ce546 (case study in `l3-narrative/Anatomy_of_a_Liquidation.pptx`) lost $72K across 2 chains to 2 unrelated attackers and a third still-armed approval. The victim's cognitive overhead to "just revoke the approvals" includes: knowing Permit2 exists, knowing how to read `allowance()`, knowing how to submit a revoke transaction, paying the gas for it. That burden is untenable at scale.
- Extends to MetaMask Snaps case (`l3-narrative/Standing_Next_To_The_Safe.pptx`): users install with one decision and inherit surveillance capability they never reviewed after that one click.

**Cross-references.** [Participatory Asymmetry](#participatory-asymmetry--predatory-literacy), [External Accountability Infrastructure](#external-accountability-infrastructure).

---

### Tuition Extraction Markets

**Definition.** A market structure in which losses incurred by less-sophisticated participants are not waste but raw material — simultaneously funding the sophisticated participants' returns and providing the calibration data that produces their edge. The market's continued profitability for its sophisticated tier requires a continuous inflow of new participants whose losses serve both functions.

**Extended description.** Generalizes Akerlof-style information asymmetry markets and the specifically adversarial version sometimes called "liquidity of fools" in quantitative finance. The defining feature is the double-counting of beginner losses: the same dollar that flows to the sophisticated participant as profit also flows back as information that sharpens the sophisticated participant's strategy against the next beginner. On-chain DeFi exhibits this structure clearly. Bot `0xc0dec760` in the corpus is illustrative: 57,023 transactions across 174 distinct contracts and 23 days, with 85% reverting (48,455 of 57,023). The bot operates not as a profit center on its own — the gas spend on a corpus-wide volume of failed transactions exceeds any extractable value at the visible layer — but as a research instrument whose failures map the response surface of contracts the operator's parallel infrastructure can exploit at scale. Vanity-prefix branding (`0xc0dec…`) cross-references [Adversarial Vanity Branding](#adversarial-vanity-branding) operational sub-type. The graduation rate from prey to predator is structurally low; this is a feature, not a flaw, because the predator layer's economics depend on a high prey-to-predator ratio. Frame distinct from [Victim-to-Predator Pipeline](#victim-to-predator-pipeline): that entry describes the unusual case of vertical migration; this entry describes the steady-state market structure that makes such migration both possible and rare.

**Empirical grounding.**
- `0xc0dec76000f6c2d32f23d523748e50ebb5bb34a3` (Base, 2026-04-29 corpus snapshot): 57,023 transactions, 48,455 reverts (85.0%), 174 distinct contracts touched, 24,518 blocks active over a 23-day window (2026-04-05 → 2026-04-28). Top selector `d2154138` × 46,853 — a single signature carrying 82% of activity, the fingerprint of a probing instrument rather than a varied-strategy bot. Parallel-infrastructure signal: bot's deployer record shows funder `0x18b0f4547a89fe4c5fe84f258bea3601fa281e9f`, which also funds five other deployers with fleets of 44, 42, 30, 6, and 6 contracts. The funder is not the bot operator's only piece of infrastructure — it's a node in a network of paid-for capability. Search methodology and full candidate list in `reports/tuition_extraction_anchor_search_2026-04-29.md`.
- Prior anchor `0x84792c2a` (cited in earlier lexicon versions) was retired by Correction #18 (2026-04-29): the bot has zero `transaction_events` rows in the corpus and the 375K+ figure was external block-walking with methodology not preserved. The bot's own case file (`BOT_INVESTIGATION_0x84792c2a_20260322.md`) confirms the corpus-coverage gap. The Tuition Extraction concept survives the anchor swap; the framework's grounding now lives entirely in corpus-derived measurement.
- [Camouflage Ratio](#camouflage-ratio) is itself a measurement of how efficiently the predator layer is calibrated against the prey layer. The ratio's stability across chains, time, and operator subsets (per the 2026-04-29 robustness check) is consistent with a market that maintains its predator/prey equilibrium structurally, not contingently.

**Cross-references.** [Camouflage Ratio](#camouflage-ratio), [Trust Amplification Factor](#trust-amplification-factor) (a measurement of how much the predator layer's edge is amplified through trusted infrastructure), [Victim-to-Predator Pipeline](#victim-to-predator-pipeline), [Cost-Habituation Asymmetry](#cost-habituation-asymmetry) (a psychological mechanism that sustains the prey inflow).

---

## Ecosystem-Level

### The Proofreading Trap

**Definition.** The security industry's current response optimized for a threat model (code bugs) that has stopped being the dominant threat. More careful reading of the same book doesn't fix the architectural, configuration, and compositional properties the book teaches developers to use.

**Extended description.** Code auditing finds bugs. The April-2026 exploit cluster (Aethir / Hyperbridge / Kelp) contains one code bug and two non-code failures. Bug-bounty programs, audit-marketplace platforms, static-analysis tools, and formal verification frameworks all target the proofreading surface. Layer 3's positioning is explicit: not better auditing, but a different category that measures the properties the code uses, not the code itself.

**Empirical grounding.**
- **Cluster validation in EXTRACTION_006 / 007 / 008**: three attacks, three different failure layers (operational / code / configuration), same 9-day window, same structural target (pooled-custody cross-chain adapters). Traditional audits catch at most 1 of 3 (Hyperbridge's MMR bug). Stored-potential framework catches all three because it measures capability-vs-constraint directly.
- Cantina bug-bounty submission rejection (2026-03-25, around `0xd4624228` trust amplification): rejected explicitly on grounds that "the code did what it was supposed to do." That IS the proofreading trap — the bug bounty surface is the wrong question, and the rejection confirms it.

**Cross-references.** [Compositional Harm](#compositional-harm), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap).

---

### The Self-Cannibalizing System

**Definition.** DeFi requires trust to function and new users to grow, but its architecture is hostile to both. New users are structurally positioned as food for predators.

**Extended description.** The ecosystem educates through harm rather than instruction. Users learn Permit2 by being drained. They learn about oracle manipulation by holding a token that got price-manipulated. Selection pressure filters out the unsophisticated (they lose money, leave, or get absorbed into predator ranks) while teaching the survivors to either defend or predate. The system cannot grow its user base in a healthy way; it can only churn through cohorts.

**Empirical grounding.**
- 13,954 undrained approvals in our corpus (`l3-narrative/Access_Topology_Intelligence.pptx` slide 7). Each one is a user who granted permission and hasn't (yet) been drained — stored potential at the user-population level.
- 67 unique victims of CE5E in 6.8 days (`reports/case_CE5E_drainer_operation.md`). 0 of 11 today-victims had prior alert history. The victim population is being freshly generated continuously.

**Cross-references.** [Victim-to-Predator Pipeline](#victim-to-predator-pipeline), [Accountability-as-Load-Bearing](#accountability-as-load-bearing).

---

### Victim-to-Predator Pipeline

**Definition.** Documented empirical pattern where victims of on-chain exploitation sometimes become operators of similar attacks.

**Extended description.** Education-by-exploitation mechanism producing both sophisticated users and new predators from the same cohort. A user who gets caught by a trap contract, observes the mechanism, reverse-engineers it, and reproduces it is indistinguishable from any other new deployer in the trap population. The ecosystem's pedagogical vector runs through adversarial exposure.

**Empirical grounding.**
- `0xcfd2cbdd` hit 9 different traps, suffered 2,279 reverts, then deployed 14 callback traps (deck `What_The_Chain_Reveals.pptx`).
- `0x3f4739d` had 5,029 reverts, then deployed 39 contracts.
- 25 bot candidates in our `bot_candidates` table also appear as deployers. The overlap is the pipeline.

**Cross-references.** [The Self-Cannibalizing System](#the-self-cannibalizing-system), [Strategy Lifecycle](#strategy-lifecycle), [Tuition Extraction Markets](#tuition-extraction-markets) (the steady-state market structure that makes this vertical migration both possible and rare).

---

### Accountability-as-Load-Bearing

**Definition.** Accountability is an independent variable from surveillance and authority. Systems can have accountability without surveillance (natural consequences, reputation) or surveillance without accountability (observation without response).

**Extended description.** Without accountability, systems reduce to pure power dynamics where predators operate with structural impunity. Traditional finance has institutional accountability (regulators, deposit insurance, chargeback rights) that operates independently of whether any particular transaction is surveilled. DeFi architecturally rejected institutional accountability on ideological grounds and has not replaced it with any functional substitute. The result is that Layer 3's observational edge exists because no enforcement layer does; we can watch everything and affect nothing.

**Empirical grounding.**
- `reports/case_CE5E_drainer_operation.md` documents this directly: we can attest to the drains with Tier A confidence (68 events, $929K), can identify freeze targets with Tier A precision, and have no authority to freeze anything. The only accountability mechanisms available are Circle/Tether issuer intervention or protocol-level social coordination.
- Kelp retrospective (`reports/kelp_retrospective_replay.md` Phase 8): quote-safe claim explicitly rules out prevention — "Layer 3 has no enforcement layer." Flagging ≠ prevention.

**Cross-references.** [External Accountability Infrastructure](#external-accountability-infrastructure), [Observational Edge Non-Convertibility](#observational-edge-non-convertibility).

---

### External Accountability Infrastructure

**Definition.** The infrastructure required to restore accountability in permissionless systems that architecturally rejected it.

**Extended description.** Includes Layer 3's observational capability (what's happening), stablecoin issuer intervention (Tether, Circle — selective freeze authority), foundation-level recovery (Solana Foundation's $20M contribution to Drift recovery), compliance relationships at centralized on-ramps (CEX freezes, KYC-linked cashout), and protocol-level social coordination (Aave bad-debt resolution, Kelp coordination). None of these are on-chain primitives; they are off-chain coordination layers that the ecosystem has re-imported despite its architectural rejection of institutional authority.

**Empirical grounding.**
- **EXTRACTION_005 Drift recovery breakdown**: Tether $127.5M + Solana Foundation $20M + $100M revenue credit facility = $247.5M recovered vs $285M loss (~87% coverage). Every recovery dollar came through external accountability infrastructure; zero from on-chain-native mechanisms.
- **EXTRACTION_004 Rhea recovery**: Tether freeze $4.34M + voluntary USDC return $3.36M + voluntary NEAR return $1.56M = $8.26M vs $18.4M loss (~45% coverage). Same pattern — recovery flows through centralized issuer and protocol treasury discretion.
- **EXTRACTION_008 Kelp recovery status**: pending at documentation date. rsETH is an LRT, not a stablecoin — no Circle/Tether pathway. Recovery requires protocol-native action.

**Cross-references.** [Accountability-as-Load-Bearing](#accountability-as-load-bearing), [Cognitive Load Concentration](#cognitive-load-concentration).

---

### Convergent Calibration

**Definition.** A pattern in which multiple unrelated adversarial actors converge on the same operational template at the same time, with no observable coordination signal between them — no shared funders, no shared infrastructure, no upstream linkage, no bytecode-family overlap. The natural hypothesis when N actors execute the same shape simultaneously ("they're coordinated" or "one actor with N faces") is actively ruled out by direct overlap probes, but the convergence itself remains.

**Extended description.** Distinct from coordination (which would predict measurable overlap between participants) and from coincidence (which would not predict the pattern repeating across scales and time). The category exists because the *absence-of-coordination* finding is itself analytically load-bearing. When surveyed without testing for overlap, a wave of N independent operators looks identical to one operator with N faces. The discipline of probing for the linkage is what distinguishes the two; the corpus-wide convergent-calibration observation is the result of that discipline applied at multiple scales.

Three measurement surfaces in the Layer 3 corpus exhibit the same shape: the funder layer, the operator layer, and the execution layer. In each case, the corpus rules out coordination directly, but the operational template, timing, and scale converge. Candidate mechanisms — none directly observable from corpus data — include shared upstream tooling (an "operator-class kit" provisioned by a single supplier to many independent operators), shared training data (a published detection methodology the entire operator class calibrates against, the [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) hypothesis at population scale), or convergent calibration against the same defensive heuristics in the wild (operators independently arriving at the same template because the same defensive surface rewards it).

The framework implication is that the population statistics of the L2 adversarial cohort cannot be safely interpreted as "one big operator's downstream" or as "many independent actors" without explicit overlap testing. Both readings are wrong by default. The third reading — many independent actors who behave as if coordinated — requires the linkage probe to be ruled out, and is the structurally interesting answer.

**Empirical grounding.**

> **[CORRECTION #20 — 2026-05-09]** The funder-layer instance below is **substantially weakened** by the discovery that ~7 of 12 "Infrastructure-Scale Operators" are CEX hot wallets and bridge solvers. The "twelve independent operations with similar tempo and no shared infrastructure" finding is technically still true but uninformative — independent CEXes/bridges also don't share downstream customers. The convergence on "high deployer-fanout topology" is partly a product of measurement (the detector flagged the topology, which is what CEXes and bridges produce by default) rather than convergent adversarial calibration. The operator-layer (Single-Purpose Funder), execution-layer (drain-burst cohort), and scheduler-layer (`0xf7883e3f` cadence) instances below remain valid empirical anchors; the funder-layer instance does not. See Correction #20.

- ~~**Funder layer (2026-04-29, Section A4 of `reports/epistemic_test_results_2026-04-29.md`):** Cross-funder downstream-deployer overlap probe across all 66 pairs of the top-12 Infrastructure-Scale Operators returned zero pairs sharing any downstream deployer. Twelve independent operations, similar tempo, no shared infrastructure. Three of the twelve made their first mainnet transactions within ~36 hours of each other in November 2025 — a separate convergence in provisioning timing without observable linkage. Diagnostic: `reports/funder_cluster_diagnostic_2026-04-29.md`.~~ **[CORRECTION #20: RETRACTED as a Convergent Calibration anchor; the no-overlap finding is real but the population is heterogeneous (CEXes + bridges + possibly some genuine adversarial operators), not 12 convergent adversarial operations.]**
- **Operator layer (2026-04-28, `cases/CASE_SINGLE_PURPOSE_INFRASTRUCTURE_FUNDER.md`):** 69 Single-Purpose Funder pairs across Base, Arbitrum, and Optimism. Three distinct deployment shapes (burst-mass, slow-drip, active-weaponized) appear concurrently, with no funder, deployer, or bytecode-family overlap with any documented organization. The single observable instance of coordinated pre-mining (vanity-mirrored funder/deployer pair `0x4200a4790e7f`/`0x30efa4790e7f`) is the exception that demonstrates the rule — the remaining 68 pairs use random-prefix wallets that do not require any opsec linkage between funder and deployer.
- **Execution layer (2026-04-29, ad-hoc 24h drain-burst decomposition):** Six self-deploying trap operators executing on the same day within a 9-hour deployment window. Distinct funders, no upstream funder linkage, no bytecode-family overlap, fleet sizes of 1 (five operators) or 3 (one operator). Identical operational template — deploy → 1-2 hour bait window → mass-sweep → dispose — across all six. 348 drain events in 24 hours, 99.4% concentrated in these six callers. The `0x1aae146c1328` / `0xacc79e7b9f8d` / `0xab613368165f` / `0x9dff309f8b31` / `0xfc6362ec899f` / `0xf2418fcd0bec` cohort is now on watchlist HIGH; full probe in conversation log of 2026-04-29 session.
- **Scheduler layer (2026-05-05, three-iteration cadence verification):** The `0xf7883e3fef23` drainer-spawn hub (cumulative ~1,150 victims across 8 iterations / 28 days) exhibits sub-minute scheduler precision in its iteration cadence: iter_6 spawned 2026-05-01T09:33:41 UTC, iter_7 at 2026-05-03T10:01:41 UTC (+47.7h, 28-min drift), iter_8 at 2026-05-05T10:02:11 UTC (+48.0h, 30-second drift from iter_7's time-of-day). The combination of ±30-minute interval drift across recent runs and ±30-second time-of-day precision across three consecutive iterations is consistent with a precisely-tuned automation rather than a human operator. This adds a new sub-pattern within Convergent Calibration: where the funder/operator/execution layers documented above show convergence *across unrelated actors*, the scheduler layer shows convergence *within a single actor's automated pipeline* — automation precision is itself a behavioral signature distinct from human-driven schedules. Forecast iter_9 (2026-05-07 ~10:02 UTC) is the next falsifiability test.

**Cross-references.** [Infrastructure-Scale Operator](#infrastructure-scale-operator) (the funder-layer instance), [Single-Purpose Infrastructure Funder](#single-purpose-infrastructure-funder) (the operator-layer instance), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (one candidate mechanism — adversaries calibrate against the same published methodology), [Behavioral Laundering](#behavioral-laundering) (the operator-class behaviors that converge), [Strategy Lifecycle](#strategy-lifecycle) (the temporal dimension of convergence — strategies saturate together as well as appear together).

---

## Attack Pattern

### Publishing-Induced Recursive Evasion

**Definition.** Publishing detection methodology enables sophisticated operators to calibrate against it. Creates an adversarial co-evolution cycle where any widely-adopted standard becomes the next attack surface.

**Extended description.** The central commercial-strategic tension in detection work. Open publication grows the defender community but also gives attackers the baseline they need to optimize against. Layer 3's methodology (stored potential scoring, DVN configuration monitoring, cross-chain mainnet-import enrichment) will, once widely adopted, become the specification against which operators calibrate their next generation of laundering. This is not a reason to keep methodology secret — the edge decays either way — but it shapes what the sustainable edge actually is: corpus depth, not methodological novelty.

**Empirical grounding.**
- [Camouflage Ratio](#camouflage-ratio) at 70–79% is the standing example. Operators have already calibrated to whatever revert-rate threshold the current detection tools use.
- GoPlus-family benchmarks (`l3-narrative/Stored_Potential_Risk_Model.pptx` slide 6): 10/10 CRITICAL contracts in Layer 3 returned NO DATA from GoPlus. The GoPlus threshold is the attacker's calibration target.

**Cross-references.** [The Detection Gap as Product](#the-detection-gap-as-product), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset), [Strategy Lifecycle](#strategy-lifecycle), [Adversarial Vanity Branding](#adversarial-vanity-branding) (the anti-forensic-spoofing sub-category exploits the truncated-prefix display convention published by analyst tooling — a recursive-evasion pattern at the intelligence layer).

---

### Strategy Lifecycle

**Definition.** Observed progression of attack techniques through phases: EARLY (demonstrated once), ARMS_RACE (multiple independent operators attempting), WEAPONIZED (saturation beyond defensive capacity), SATURATED (net-negative returns due to defensive adaptation).

**Extended description.** Empirical framework for timing attack-family propagation. A novel technique demonstrated publicly (Drift's durable-nonce governance takeover, Hyperbridge's MMR bypass) enters EARLY. Within weeks, independent operators replicate the pattern with variations, entering ARMS_RACE. The window between EARLY and ARMS_RACE is the commercial-intelligence opportunity — warnings delivered during EARLY can still change customer behavior before ARMS_RACE saturation.

**Empirical grounding.**
- **Oracle-manipulation-lending family**: Drift (2026-04-01) → Rhea (2026-04-16) = **15 days** EARLY → ARMS_RACE transition. Documented in `reports/extraction_event_004_rhea_finance.md` cross-chain correlation section.
- **Cross-chain infrastructure family**: Aethir (2026-04-09, operational) → Hyperbridge (2026-04-13, code) → Kelp (2026-04-18, configuration) = **9 days** for three orthogonal variants. Faster than oracle-manipulation — multiple attack teams operating in parallel, not sequential.

**Cross-references.** [Compositional Harm](#compositional-harm), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion).

---

### Operational Layer Attack

**Definition.** Attack category where code functions correctly but surrounding operational infrastructure (UIs, deployment pipelines, key management, governance workflows) is compromised.

**Extended description.** Blockaid's January 2026 prediction — that 2026 attacks would "target operational layers around key management, not the keys themselves" — empirically validated across Q2. Common pattern: the operator with authority gets socially engineered, phished, or has keys exfiltrated via malware; the on-chain signatures produced post-compromise are cryptographically valid; the code enforces what the signatures authorize. There is no code defect to catch; the attack is upstream of code.

**Empirical grounding.**
- **EXTRACTION_006 (Aethir, 2026-04-09)**: EOA admin key compromise; no multisig; no timelock. Per dev.to writeup: "The legitimate owner was just an eoa, leading to the conclusion for now that it's a private key compromise attack."
- **EXTRACTION_005 (Drift, 2026-04-01)**: durable-nonce signatures were pre-acquired via social engineering of Security Council members; when governance threshold dropped from 3/5 to 2/5, the attacker already held quorum.
- Bybit ($1.5B, 2025) referenced in the decks as the canonical large-scale operational-layer attack.
- Zerion DPRK social engineering (2026-04-10, ~$100K) as the smaller-scale current instance.

**Cross-references.** [Verification-Path Trust Failure](#verification-path-trust-failure), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [Cross-Domain Compositional Harm](#cross-domain-compositional-harm) (the case where the operational compromise crosses domains — Vercel/Context.ai chained Lumma Stealer → AWS → OAuth tokens → SSO).

---

### Configuration-Level Vulnerability

**Definition.** Attack surface that exists in deliberate protocol configuration choices rather than code defects. Publicly observable via standard contract calls (e.g., `getConfig(configType=2)`). Out of scope for bug bounties because no code is vulnerable.

**Extended description.** The canonical case: Kelp's 1-of-1 DVN configuration on both source (Unichain) and destination (Ethereum) chains. LayerZero's documented best practice is ≥2 required DVNs + optional threshold ≥1; Kelp chose 1-of-1. The choice was on-chain-readable via `EndpointV2.getConfig`, unchanged for ≥56.7 days pre-exploit. No code fix could have prevented the attack — the attack path IS the correctly-executing code doing what the configuration authorized. The only remediation is configuration change.

**Empirical grounding.**
- **EXTRACTION_008 (Kelp)**: Configuration verified via historical `getConfig` at blocks 24,500,000–24,900,000 (Phase 3 of `reports/kelp_retrospective_replay.md`). Tier A deductive lead time ≥56.7 days.
- **EXTRACTION_005 (Drift)**: governance-layer configuration variant — threshold reduction + timelock removal on 2026-03-27 was the phase transition that opened the attack window.
- **EXTRACTION_011 (TrustedVolumes RFQ proxy, 2026-05-06)**: extends the cluster to 6 of 6 (006-011) on the configuration-class shape. The exploited surface is **signed-quote acceptance scope** on the custom RFQ swap proxy `0xeEeEEe53033F7227d488ae83a27Bc9A9D5051756`, not a bytecode defect. The proxy executed valid signatures deterministically; the misconfiguration was in *what set of signed messages it would accept and act on*. Same shape as Wasabi's UUPS upgrade authority (009) and Kelp's 1-of-1 DVN (008) — a *trust-scope* setting that admits weaponization once any element of the trust set is compromised or under-specified.

**Cross-references.** [Verification-Path Trust Failure](#verification-path-trust-failure), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap), [Cross-Domain Compositional Harm](#cross-domain-compositional-harm) (the off-chain analog where the configuration is at the application substrate — environment-variable visibility defaults, OAuth scope settings), [Protocol-Family Specialist Operator](#protocol-family-specialist-operator) (the operator class that systematically harvests configuration-class surfaces within a single trust-graph; EXTRACTION_011 is the joint anchor).

**External taxonomy reference.** The Configuration-Level cluster has many `kadenzipfel/protocol-vulnerabilities-index` analogs across protocol types: `categories/*/access-control-*`, `categories/*/initialization-*`, `categories/*/admin-centralization-risks.md`, `categories/*/privileged-function-abuse.md`, `categories/*/centralization-risks.md`. The repo's 460-category taxonomy is the closest external benchmark for "code that did exactly what its spec said it would do, with the spec being the failure mode."

---

### Verification-Path Trust Failure

**Definition.** Compositional harm arising when a trusted verification layer (oracle, DVN, multisig) fails while all other components operate correctly. The layer's attestation becomes the attack vector because downstream components are designed to trust it unconditionally.

**Extended description.** The defining property: components downstream of the verifier have no mechanism to question the attestation. A lending protocol with oracle dependency trusts the oracle's price; if the oracle reports a manipulated price (because its own source was compromised), the lending protocol authorizes undercollateralized borrowing without any defect. A cross-chain adapter with DVN dependency trusts the DVN's signature; if the DVN signs a forged message, the adapter mints without defect.

**Empirical grounding.**
- **EXTRACTION_005 (Drift)**: fake CVT token wash-traded to ~$1 on Raydium → Drift's oracles reported $1 → Drift accepted CVT as collateral worth hundreds of millions.
- **EXTRACTION_004 (Rhea)**: fake tokens lacking NEP-141 metadata deployed on implicit accounts → Ref Finance pool IDs 8528-8538 paired them with USDC → Rhea's margin-trading oracle accepted the manipulated prices.
- **EXTRACTION_008 (Kelp)**: 1-of-1 DVN signed forged cross-chain message → LayerZero endpoint accepted attestation → Kelp adapter minted on Ethereum.

**Cross-references.** [Compositional Harm](#compositional-harm), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [Pooled Custody Amplification](#pooled-custody-amplification).

**External taxonomy reference.** Maps to the `kadenzipfel/protocol-vulnerabilities-index` oracle cluster: `categories/oracle/*` (12 categories including stale-oracle-price-data, twap-oracle-miscalculation, invalid-oracle-version-handling) and the cross-protocol `oracle-price-manipulation` / `oracle-price-feed-*` entries spanning lending, CDP, derivatives, leveraged-farming, options-vault, and synthetics. The trust-binding-without-question-mechanism failure mode appears under different labels in each protocol type.

---

### Pooled Custody Amplification

**Definition.** Lock-and-release adapter architecture (as distinct from mint-burn) where the attack target is shared user deposits rather than newly minted tokens. Amplifies harm because exploitation draws from real user capital rather than creating inflationary tokens.

**Extended description.** In a mint-burn bridge architecture, an attacker who forges a cross-chain message mints tokens on the destination chain; the resulting tokens are inflationary and their market value collapses as the fraud is realized. In a lock-and-release architecture, the attacker unlocks REAL deposits held in the adapter — the stolen tokens are indistinguishable from legitimate user holdings, retain their market value until issuer intervention, and produce direct loss to the users whose deposits were unlocked. Pooled custody is therefore the highest-stored-potential cross-chain architecture.

**Empirical grounding.**
- **EXTRACTION_008 (Kelp)**: the rsETH OFT adapter holds pooled user deposits; the attacker's 116,500 rsETH came from the pool, not inflation. That's why Aave V3 accepted the stolen rsETH as collateral — it is indistinguishable from legitimate rsETH.
- **EXTRACTION_006 (Aethir)**: OFT adapter pattern, same class. Once admin, drained bridged assets directly from the pool.
- Contrast: a theoretical mint-burn exploit of the same adapter would not have been accepted by Aave because the newly-minted rsETH would have no backing — though in practice neither architecture is hardened against cross-chain verification failure.

**Cross-references.** [Verification-Path Trust Failure](#verification-path-trust-failure), [Compositional Harm](#compositional-harm), [Configuration-Level Vulnerability](#configuration-level-vulnerability).

---

### Cross-Domain Compositional Harm

**Definition.** Compositional harm where the components span the on-chain/off-chain boundary. Each component (a browser extension, an OAuth grant, an SSO trust path, an environment variable visibility default, a malware infection on an unrelated employee's machine) functions correctly within its own domain, and the harm emerges from the composition of correctly-functioning behaviors across domains that are not normally analyzed together.

**Extended description.** Extends [Compositional Harm](#compositional-harm) beyond the on-chain substrate. Validates the framework's generality: the same structural failure pattern Layer 3 documents in DeFi appears at the application-substrate layer in mainstream cloud platforms, and the same analytical posture (audit the composition, not the components) is required in both. Worth noting: the off-chain version often has a higher trust-amplification factor because the trust hops cross identity systems (employee identity → enterprise SSO → platform identity → customer credentials) where each hop carries social trust, not just technical trust. Reviewers and academics already familiar with software supply chain attacks will recognize this pattern; the contribution is naming the cross-domain version as part of the same theoretical class as on-chain compositional harm rather than as a separate "supply chain" subgenre.

**Empirical grounding.**
- Vercel/Context.ai breach disclosed 2026-04-19 (off-chain anchor). Documented chain: Lumma Stealer (delivered via Roblox exploit script, Feb 2026) → Context.ai employee credentials → Context.ai AWS environment → exfiltrated OAuth tokens for Context AI Office Suite consumer users → Vercel employee's personal Context.ai signup with "Allow All" Google Workspace scope → Vercel internal systems via SSO → enumeration of non-sensitive environment variables → bulk extraction of customer API keys, database credentials, GitHub tokens, cloud keys for customers with no relationship to Context.ai. Case file: `cases/CASE_VERCEL_CONTEXT_BREACH_20260419.md`.
- Wasabi Protocol admin-key compromise 2026-04-30 (on-chain anchor, EXTRACTION_009). Documented chain: private-key compromise vector (vector itself not yet public) → admin EOA `0x5c629f8c0b53` → `grantRole` on Wasabi role manager → UUPS proxy upgrade on WasabiVault and Long Pool contracts → fake-strategy `drain()` calls → ~$4.5–5.5M extracted across Ethereum mainnet, Base, Berachain, and Blast. Helper contract `0x02228b0afcdb` deployed at the same address on multiple chains via CREATE2 — pre-positioned cross-chain attack infrastructure. Case file: `cases/CASE_WASABI_EXPLOIT_20260430.md`.
- No CVE was exploited at any step in either incident. No vendor had a code-level vulnerability. Every component — OAuth scope, SSO trust, env-var visibility default (Vercel); UUPS upgradeability, single-`ADMIN_ROLE` configuration (Wasabi) — functioned as designed.
- Vercel CEO publicly attributed attacker velocity to AI augmentation — first major incident disclosure to name AI-augmented adversary tradecraft on the record.
- Trust-amplification analog: the affected Vercel customers had no direct relationship with Context.ai, and Wasabi's vault depositors had no individual relationship with the deployer EOA. In both, users trusted the *structure* (Vercel as platform; Wasabi vault as audited-deposit primitive); the structure was correctly forwarding the attacker's reach to their assets. Structurally identical to the Universal Router case in EXTRACTION_003 (`0xd4624228`).

**Cross-references.** [Compositional Harm](#compositional-harm) (the parent concept), [Trust Amplification Factor](#trust-amplification-factor) (the quantification framework that applies to both on-chain and off-chain versions), [Configuration-Level Vulnerability](#configuration-level-vulnerability) (Vercel's environment-variable visibility default is a configuration-level instance), [Operational Layer Attack](#operational-layer-attack) (related class).

---

## Operational Doctrine

This section codifies the **maneuver frame** — the strategic posture that treats every exploit as a multi-phase campaign rather than a singular code defect. The entries here are not new attack categories; they are the *operational doctrine* that organizes every existing attack category in this lexicon into a single defender-facing model. The maneuver lens is where Layer 3's analytical primitives (stored potential, compositional harm, confused deputy chains, etc.) consolidate into actionable counter-intelligence.

### Adversarial Maneuver

**Definition.** A multi-stage operational sequence in which an attacker gains positional advantage over a deterministic system by exploiting the system's own trust architecture, information flows, and forced execution. The maneuver transforms benign capabilities into destructive outcomes through the strategic sequencing of actions, rather than through the exploitation of a single code defect.

**Extended description.** The maneuver frame shifts security analysis from a bug-centric to a campaign-centric model. Every major DeFi exploit in the corpus, when decomposed, reveals the same six phases: reconnaissance, positioning (stored potential expansion), trust establishment (camouflage), trigger (exploiting forced deterministic neutrality), exploitation (confused deputy chains and compositional harm), and exfiltration (behavioral laundering). The phases are not optional — even smash-and-grab events compress the sequence into minutes, but every phase is present. See [Maneuver Primitives](#maneuver-primitives) for the canonical phase taxonomy.

The strategic implication is that defense cannot be reactive. By the time the exploitation phase emits an observable artifact (the drain transaction), the attacker has already completed reconnaissance, positioning, and trust establishment. The transaction is the final phase, not the campaign. Therefore the **leading intelligence indicators are pre-exploitation** — stored potential expansion, camouflage signatures, capability injection events, and infrastructure pre-positioning. Layer 3's surveillance is built around capturing these indicators because they precede the discharge by days, weeks, or months.

The maneuver frame also reframes adversary skill. The most effective attackers in the corpus are not the best coders; they are operational architects who understand tempo (how fast can the exploit execute before defenders react), deception (how can the exploit appear normal), redundancy (what fallback if a path is blocked), and cover (how to maintain access for future campaigns). This is closer to special-operations doctrine than to traditional software-vulnerability research, and the language of [maneuver warfare](https://en.wikipedia.org/wiki/Maneuver_warfare) maps cleanly onto the observed patterns.

The terrain itself shapes which maneuvers are possible:
- **Composability** is open terrain — easy to move through, hard to defend.
- **Proxy upgradeability** is a road network — used by both attackers and defenders.
- **Oracles** are intelligence assets — capture them, and the enemy is blinded or fed false data.
- **ENS names and on-chain reputation** are identity markers — spoofable, poisonable, exploitable for deceptive trust amplification.

The [Adversarial Topology](#adversarial-topology) framework is the terrain map: position, permissions, trust bindings, mutability, observation capability. The attacker maneuvers across it, seeking high ground (privileged positions) and chokepoints (single points of failure). The defender must read the same map and anticipate the avenues of approach.

**Empirical grounding.**

- **Grok/Bankr (2026-05-04, ~$175K AI agent drain).** Reconnaissance: attacker maps Grok's publicly-labeled wallet and its constrained transfer capability. Positioning (capability injection): gifts a Bankr Club Membership NFT that expands Grok's permissions to execute autonomous transfers — the equivalent of smuggling a key into the fortress. Trigger (prompt injection): delivers a crafted prompt that Grok's intent-parsing layer interprets as a legitimate command; [Forced Deterministic Neutrality](#forced-deterministic-neutrality) executes it without questioning the source. Exploitation: Bankr (the automation layer) signs and broadcasts the transfer; the trust chain (Twitter → Grok → Bankr → Base) functions correctly. Exfiltration: attacker bridges and dumps the tokens, then deletes the X account. The maneuver exploited not a bug but the absence of a judgment layer between "reading a helpful reply" and "authorizing a $175K transfer."

- **THORChain (2026-05-15, $7.4M–$10.8M consensus forgery).** Reconnaissance: attacker studies Bifrost's gossip protocol and recognizes that validator signatures cover content but not the inbound/outbound bit. Positioning: attacker (or colluding proposer) has access to a real inbound observation with valid signatures — a legitimate deposit. Trigger: flips the inbound/outbound bit in the `ObservedTx` struct and re-proposes it to consensus; signatures remain valid, consensus accepts the forged outbound. Exploitation: THORChain's TSS signs real outbound transactions on ETH, BSC, and BTC; the composition of Bifrost + Tendermint + TSS produces the payout. Exfiltration: funds laundered through a consolidation hub and a cold wallet (3,156 ETH still held). The maneuver exploited the specification gap between *what the signatures attested to (content)* and *what they should have attested to (type + content)*. Not a cryptographic break — a protocol-trust-model outmaneuver.

- **Renegade Dark Pool (2026-05-10, $209K initializer takeover).** Reconnaissance: maps Renegade's proxy/implementation split, identifies the unprotected `initialize()` function on a legacy Dark Pool proxy. Trigger: calls the initializer, becomes admin, points the proxy's `delegatecall` at a malicious implementation. Exploitation: the proxy (now a [Confused Deputy](#confused-deputy-problem)) executes the malicious implementation's `drain()` logic against tokens that users had pre-approved to the proxy — the drain uses those approvals without needing new victim signatures. Exfiltration: assets swept; 90/10 whitehat bounty saw most funds returned. The maneuver exploited the compartmentalization-composability contradiction — contracts blindly trust each other, no single contract evaluates the full attack story.

- **Kelp (2026-04-18, ~$292M cross-chain DVN forgery).** Reconnaissance: identifies that Kelp's LayerZero OApp adapter is configured with `requiredDVNCount=1` — a single-verifier attestation path readable via `EndpointV2.getConfig(configType=2)`. Positioning: the configuration sits unchanged for **≥56.7 days** of accumulating user deposits. This is the longest stored-potential window in the corpus. Trigger: a forged cross-chain message signed by the (compromised or colluding) DVN operator. Exploitation: LayerZero accepts the attestation (1/1 satisfied), the adapter releases tokens from pooled custody. Exfiltration: ~116,500 rsETH freely composes into Aave as collateral because [Pooled Custody Amplification](#pooled-custody-amplification) makes the stolen tokens indistinguishable from legitimate holdings.

- **`0x80b12bd0` Animoca-attributed operator (2026-05-09, 4,587-victim drain on Base; Layer 3 corpus).** Reconnaissance: attacker (presumably via key compromise) inherits a 2019-vintage mainnet identity with REVV / OneFootball Club / ANIMOCA portfolio holdings — institutional cover identity ready-made. Positioning: deploys bait `0x752c5a95` on Base 2026-03-26 03:12 UTC; bridges 1 OFC token from Ethereum to Base 50 minutes later as cross-chain control confirmation. Trust establishment: the 7-year mainnet vintage and Animoca-portfolio token holdings provide [Pattern A](#pattern-a--reputation-building-sacrifices) reputation by inheritance. Discharge: 4,587 victims drained in a 30-minute window via two coordinated execution cells with zero pairwise victim overlap (execution sharding). See [reports/animoca_deployer_investigation_2026-05-15.md](../reports/animoca_deployer_investigation_2026-05-15.md). This case is empirically important because Layer 3's behavioral classifier identified the discharge risk on 2026-04-24 — 15 days of pre-drain lead time, demonstrating that maneuver-centric pre-exploitation indicators are actionable.

**Cross-references.** [Maneuver Primitives](#maneuver-primitives) (the six-phase taxonomy), [Counter-Maneuver](#counter-maneuver) (defender-side doctrine), [Vulnerability-Centric vs Maneuver-Centric Framing](#vulnerability-centric-vs-maneuver-centric-framing) (the methodological contrast), [Stored Potential](#stored-potential) (the leading indicator of positioning), [Compositional Harm](#compositional-harm) (the exploitation-phase substrate), [Confused Deputy Problem](#confused-deputy-problem) (canonical exploitation mechanism), [Forced Deterministic Neutrality](#forced-deterministic-neutrality) (canonical trigger mechanism), [Behavioral Laundering](#behavioral-laundering) (canonical exfiltration mechanism), [Adversarial Topology](#adversarial-topology) (the terrain map), [Camouflage Ratio](#camouflage-ratio) (trust-establishment quantification).

---

### Maneuver Primitives

**Definition.** The canonical six-phase taxonomy of an [Adversarial Maneuver](#adversarial-maneuver). Every successful exploit in the corpus traverses these phases in order. The phases name *what the attacker does*; the cross-referenced lexicon concepts name *what they exploit* at each step.

**Extended description.** The taxonomy serves two functions: (a) it gives defenders a checklist of pre-exploitation indicators to monitor (any phase observable before the trigger is leading intelligence), and (b) it gives analysts a decomposition framework for post-mortem reconstruction. The canonical sequence:

| Phase | Lexicon concept exploited | What the attacker does |
|---|---|---|
| **Reconnaissance** | [Observational Edge Non-Convertibility](#observational-edge-non-convertibility) (asymmetric) | Maps the target's topology: admin keys, proxy patterns, trust bindings, oracle dependencies. Identifies the *vulnerability window* — the exact moment of minimum defensive readiness. |
| **Positioning** | [Stored Potential](#stored-potential) expansion | Positions to exploit the window. Deploys a malicious contract, seeds a dormant trap, gifts an NFT that expands permissions, opens an unprotected initializer, configures a single-verifier DVN. |
| **Trust Establishment** | [Camouflage Ratio](#camouflage-ratio), [Pattern A — Reputation-Building Sacrifices](#pattern-a--reputation-building-sacrifices), [Pattern D — Cross-Chain Reputation Import](#pattern-d--cross-chain-reputation-import) | Establishes legitimacy: low revert rates, fake audits, sock-puppet socials, community contributions, mainnet-vintage cover identity. The attacker becomes a "trusted" node. |
| **Trigger** | [Forced Deterministic Neutrality](#forced-deterministic-neutrality) | Delivers the payload: a crafted transaction, a prompt injection, a proxy upgrade, a re-proposed observation. The system's determinism guarantees execution; no human can interpose. |
| **Exploitation** | [Confused Deputy Problem](#confused-deputy-problem), [Distributed Confused Deputy Chain](#distributed-confused-deputy-chain), [Compositional Harm](#compositional-harm) | The system's own components — each functioning correctly — carry out the attacker's intent. The Vault trusts the Router, the Proxy trusts the Implementation, the AI trusts the prompt, consensus trusts the signature. |
| **Exfiltration** | [Behavioral Laundering](#behavioral-laundering) | Routes extracted value through CEX hot wallets, cross-chain bridges, or vanity-mined addresses to obscure the trail and cash out. |

**Defender's reading.** Phases 1–3 produce on-chain indicators that *precede* the trigger:
- Reconnaissance leaves traces (probe transactions, contract reads from unusual addresses, view-function pattern queries).
- Positioning leaves contracts (deployed but undocumented, dormant for a calibrated window).
- Trust establishment leaves a [Camouflage Ratio](#camouflage-ratio) signature.

Phase 4 (trigger) is the discharge moment — the point at which value moves. Phase 5 (exploitation) is the execution. Phase 6 (exfiltration) is the destination trail.

**Defensive leverage by phase:** counter-maneuver effort allocated to phases 1–3 produces lead time; effort allocated to phases 4–6 produces investigation depth but rarely loss prevention. [Counter-Maneuver](#counter-maneuver) makes this allocation explicit.

**Empirical grounding.** All five case studies under [Adversarial Maneuver](#adversarial-maneuver) decompose cleanly into these six phases. The decomposition is mechanical: given a documented exploit and its on-chain artifacts, the phases can be enumerated in under an hour. This is the test of the taxonomy's load-bearing status — if an exploit cannot be decomposed into these phases, either the taxonomy is incomplete or the exploit is being mis-interpreted.

**Cross-references.** [Adversarial Maneuver](#adversarial-maneuver), [Counter-Maneuver](#counter-maneuver), [Stored Potential](#stored-potential), [Behavioral Laundering](#behavioral-laundering).

---

### Counter-Maneuver

**Definition.** The defensive doctrine that mirrors and disrupts [Adversarial Maneuver](#adversarial-maneuver). Counter-maneuver allocates defensive effort across the same six phases the attacker traverses, with the explicit goal of *closing maneuver windows* rather than *patching individual bugs*. Success is measured in maneuver windows closed, not vulnerability counts reduced.

**Extended description.** Patching bugs is necessary but insufficient; the maneuver frame shows that even a fully-audited codebase with zero CVEs can be outmaneuvered through positioning, trust establishment, and trigger-layer attacks that do not exercise any code defect (the Aethir, Wasabi, Grok/Bankr, THORChain, and Renegade cases each illustrate this in different forms). Counter-maneuver operationalizes five defensive verbs, one per attacker phase that produces an observable artifact:

| Counter-verb | Targets attacker phase | Mechanism |
|---|---|---|
| **Deny Reconnaissance** | Reconnaissance | Obfuscate topology where consistent with operational requirements; deploy deception (honeypots, fake admin keys) to mislead attackers. Force the attacker to spend more time and exposure to map the target. |
| **Impose Complexity Ceilings** | Positioning | Hardcoded circuit breakers that limit the attacker's freedom of maneuver. Examples: Liquity's Shutdown Threshold; per-asset deposit caps; max-TVL-per-adapter constraints. The ceiling is a structural cap on stored potential. |
| **Disrupt Positioning** | Positioning, Trust Establishment | Monitor for [Stored Potential](#stored-potential) expansion (capability injection events, dormant-fleet wake-ups, NFT gifts that expand AI agent permissions, proxy admin grants) and alert before the trigger. This is Layer 3's primary product surface. |
| **Delay Exploitation** | Trigger | Timelocks, multisig thresholds, and human-in-the-loop confirmations that *extend* the attacker's campaign, increasing detection probability per unit of value at risk. The delay turns a single-tx exploit into a multi-block window where defenders can intervene. |
| **Track Exfiltration** | Exfiltration | [Behavioral Laundering](#behavioral-laundering) pattern detection: even when the attack succeeds, follow the money. Funds traced to a known CEX hot wallet or a cross-chain bridge produce intelligence for the next campaign. |

**Strategic posture.** Counter-maneuver explicitly accepts that some attacks will succeed in the short term. The goal is not zero-loss; the goal is *raising the cost and complexity of every attack to the point where the attacker's operational tempo collapses*. An attacker who must spend 60 days on reconnaissance to find a viable trap, then 30 days on trust establishment, then minutes on execution, then weeks on exfiltration through detectable laundering — has a campaign that produces multiple chances for defensive intervention, multiple ways for the operator to make a mistake, and multiple post-mortem signals for the next campaign's prevention.

The contrast with the patching mindset is sharp. Patching closes a specific code path. Counter-maneuver closes *operational pathways*. A patched contract still leaves the attacker free to find another contract; a counter-maneuvered protocol forces the attacker to develop a new campaign blueprint from scratch.

**Empirical leverage.** Layer 3's 2026-04-24 pre-drain flag on operator `0x80b12bd0` (15 days of lead time before the May-9 4,587-victim discharge) is the canonical example of disrupt-positioning succeeding. The flag did not prevent the discharge — Layer 3 has no enforcement surface — but it did demonstrate that the leading indicators are detectable at scale and at lead times that would, in a system with enforcement authority, have closed the maneuver window.

THORChain's Mimir governance freeze on 2026-05-15 is the canonical example of delay-exploitation succeeding *during* an active discharge: the protocol's parameter-level kill switch let the validator set halt all outbound flows mid-incident, before the entirety of the attacker's prepared maneuver completed. This is a defensive precedent worth modeling broadly — what fraction of cross-chain protocols have a parameter-level kill switch reachable in <1 hour?

**Cross-references.** [Adversarial Maneuver](#adversarial-maneuver) (the attacker-side counterpart), [Maneuver Primitives](#maneuver-primitives) (the phase taxonomy), [Stored Potential](#stored-potential) (the primary positioning indicator), [The Detection Gap as Product](#the-detection-gap-as-product) (the commercial framing of disrupt-positioning), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset) (the track-exfiltration justification).

---

### Vulnerability-Centric vs Maneuver-Centric Framing

**Definition.** The methodological contrast between two security paradigms. The *vulnerability-centric* frame treats exploits as singular events caused by code defects, scoped to individual components. The *maneuver-centric* frame treats exploits as multi-phase campaigns whose success or failure depends on the strategic sequencing of operational actions across a battlespace of trust relationships, information flows, and mutable states.

**Extended description.** The two frames coexist; vulnerability-centric analysis remains useful for pre-deployment audit work (Attack 10 — Cross-Chain Proof Verification Bypass — is exactly the class of bug that audit-time fuzzing should catch). But the corpus shows that *most* successful exploits do not require a code defect at all. They require positional advantage, trust inheritance, and operational tempo — which are properties of campaigns, not properties of code.

The contrast, laid out:

| Dimension | Vulnerability-Centric View | Maneuver-Centric View |
|---|---|---|
| **What is the exploit?** | A singular event caused by a code defect. | A campaign of sequential actions designed to achieve positional advantage before the decisive blow. |
| **What is the attacker's skill?** | Finding the bug. | Orchestrating the campaign: reconnaissance, capability injection, trust establishment, timing, execution. |
| **What is defense?** | Patching the bug. | Counter-maneuver: disrupting the sequence, denying positional advantage, imposing complexity ceilings that make maneuvers impossible. |
| **What is the system?** | A collection of components. | A battlespace of trust relationships, information flows, and mutable states. |
| **What is success?** | Bug count reduced. | Maneuver windows closed. |

**Why both frames matter.** The vulnerability frame is still load-bearing for traditional audit work and for incidents where the attack genuinely turns on a code defect (Hyperbridge's MMR proof bug; Renegade's unprotected initializer at the immediate-trigger level). The maneuver frame is load-bearing for incidents where no code is defective: Aethir, Wasabi, Drift's governance compromise, Grok/Bankr's prompt injection, the entire Operational Layer Attack class, the cross-domain compositional harm class, and the entire `Pattern A` long-accumulation drain class observed in the corpus.

The shift is consequential in three ways:
1. **Defense becomes proactive, not reactive.** Vulnerability-centric defense requires the bug to exist; maneuver-centric defense looks for the campaign assembling around any structure, with or without a defect.
2. **Intelligence becomes the primary product, not the secondary.** Vulnerability databases are reactive; maneuver-monitoring corpora compound forward.
3. **The bug-bounty model is partially obsoleted.** Bug bounties pay for code defects; they do not pay for configuration issues, operational compromises, or campaign-level pre-positioning — even though those produce the majority of recent losses. The [Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap) names this directly.

**Empirical grounding.** Of the documented April-May 2026 wave incidents, **vulnerability-centric framing is fully sufficient for only Hyperbridge (MMR proof bug) and Renegade (unprotected initializer at the trigger layer)**. The other ten major incidents (Drift, Silo, Aethir, Zerion, Kelp, Rhea, Wasabi, Volo, Grok/Bankr, THORChain) require the maneuver frame to be coherently analyzed.

**Cross-references.** [Adversarial Maneuver](#adversarial-maneuver), [Counter-Maneuver](#counter-maneuver), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap), [The Detection Gap as Product](#the-detection-gap-as-product), [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset).

---

## Commercial / Positioning

### The Detection Gap as Product

**Definition.** The 100% gap between what free benchmarks like GoPlus detect and what sophisticated operators actually deploy. Free security data functions as an attack vector because operators calibrate against it, and "clean" results become trust amplification signals for predators.

**Extended description.** A user who checks a contract on a free scanner and sees "clean" interprets the clean result as a positive safety signal. Sophisticated operators are AWARE of this behavior and optimize bytecode to produce clean results on free scanners specifically. The user's trust in the signal is inverted by the operator's awareness of the signal. Layer 3's commercial positioning is in this gap: the 70-79% camouflage ratio IS the product — the fraction of trap contracts that defeat free tools is the fraction where paid intelligence is load-bearing.

**Empirical grounding.**
- 10/10 Layer 3 CRITICAL contracts returned NO DATA from GoPlus (`l3-narrative/Stored_Potential_Risk_Model.pptx` slide 6).
- Camouflage ratio stable 70-79% across chains (discussed under [Camouflage Ratio](#camouflage-ratio)).

**Cross-references.** [Camouflage Ratio](#camouflage-ratio), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion), [The Bug-Bounty Structural Gap](#the-bug-bounty-structural-gap).

---

### Observational Edge Non-Convertibility

**Definition.** Edges that exist only while observed. Participation collapses the observation. Some edges cannot be converted from observational to operational advantage without destroying the edge itself.

**Extended description.** The NTSB investigates airline safety and does not start airlines. Investigative journalists cover industries they do not operate in. Layer 3's edge is observational — we see patterns because we are not participating. If Layer 3 started running an arbitrage bot, deploying trap contracts, or operating infrastructure, the very operators we observe would stop behaving the same way near us. The edge is a function of our position as observer-only. This is a commercial constraint, not a personal ethics choice: the monetization must come from the observation, not from participation in the observed phenomenon.

**Empirical grounding.**
- Structural principle applied in `claude.md` §"What NOT to Build": "No trading logic, execution, or flash loans. No contract deployment. No interaction with flagged contracts — read-only always."
- Deck: `l3-narrative/Deductive_Intelligence.pptx` frames deductive observation of deterministic systems as the edge class.

**Cross-references.** [Intelligence-as-Compounding-Asset](#intelligence-as-compounding-asset), [Accountability-as-Load-Bearing](#accountability-as-load-bearing).

---

### Intelligence-as-Compounding-Asset

**Definition.** Intelligence operations where marginal cost decreases and marginal value increases over time, contrasted with operational activities (trading, arbitrage) where edges decay with each use.

**Extended description.** Layer 3's corpus grows monotonically — every new contract indexed, every new deployer profiled, every new drain captured adds to the base. The marginal cost of adding the Nth observation is lower than the (N-1)th because infrastructure is already built. The marginal value is higher because the new observation contextualizes all prior ones (a new ARMS_RACE instance validates the EARLY demonstration retroactively). A trading edge is the opposite: each use either moves the market against the trader or attracts competition, driving marginal return toward zero.

**Empirical grounding.**
- Corpus growth: 0 contracts on 2026-03-17 → 90,276 by mid-April per `claude.md` headline metric. Growth rate ~7,000 contracts/day. No decay.
- Correction-log discipline: every revision adds trust infrastructure (`reports/correction_log.md` entries #3–8). Errors compound into credibility through published correction, not against it.

**Cross-references.** [Observational Edge Non-Convertibility](#observational-edge-non-convertibility), [Publishing-Induced Recursive Evasion](#publishing-induced-recursive-evasion) (the one compounding mechanism that does have a counter-pressure).

---

### The Bug-Bounty Structural Gap

**Definition.** Bug bounty economics cannot price compositional harm because bounties pay for code-level vulnerabilities in specific in-scope contracts. Phishing-adjacent findings, configuration-level risks, and architectural stored potential are systematically out of scope across all bounty platforms.

**Extended description.** Bounty programs assume the threat model is "code does something it shouldn't." Compositional harm is "code does exactly what it's supposed to, and the result is catastrophic." There is no protocol to submit a report to; the finding belongs to the architecture, not to any one contract. Confirmed by Immunefi community response on April 18, 2026 and by the Cantina submission rejection on 2026-03-25 for `0xd4624228` trust amplification ("the code did what it was supposed to do"). This is not a flaw in bounty programs — it's a structural property of what bounties price for. Layer 3's commercial surface occupies the gap.

**Empirical grounding.**
- **Cantina rejection 2026-03-25** explicit quote: "the code did what it was supposed to do" — for a finding that produced 14.2× trust amplification and 2,910 victims. The finding was real; the bounty surface does not price it.
- **EXTRACTION_008 (Kelp) Configuration-Level**: Kelp's rsETH pools were not in any bounty's in-scope list for "1-of-1 DVN configuration" because no bounty program scopes configuration choices. The $292M loss is uncapturable by current bounty economics.
- Cluster analysis in `reports/extraction_event_008_kelp.md`: traditional audits (the proofreading surface bounties pay into) catch at most 1 of 3 April-2026 cross-chain cluster events (only Hyperbridge's MMR code bug is audit-catchable).

**Cross-references.** [The Proofreading Trap](#the-proofreading-trap), [Configuration-Level Vulnerability](#configuration-level-vulnerability), [The Detection Gap as Product](#the-detection-gap-as-product).

---

### Epistemic Tier Classification

**Definition.** All findings categorized as **Tier A** (deductive, verifiable from on-chain data), **Tier B** (inferential, methodology-applied), or **Tier C** (speculative). Discipline prevents overclaiming and enables defensible commercial communication.

**Extended description.** Every alert, report, and customer-facing claim carries an explicit tier tag. A Tier A claim has a specific on-chain read that any third party can replicate (e.g., "`getConfig(configType=2)` at block 24,500,000 returned requiredDVNCount=1"). A Tier B claim is inferential reasoning across published methodology (e.g., "the 1-of-1 DVN configuration produces CRITICAL stored potential per our risk framework"). A Tier C claim is explicit speculation about future behavior or unobservable causation (e.g., "the attacker will replicate within 15 days per the Strategy Lifecycle model"). Discipline: Tier A is for pitches, Tier B is for methodology explanations, Tier C is never cited in commercial materials without explicit framing as prediction.

**Empirical grounding.**
- Applied throughout every report in `reports/`. Kelp retrospective (`reports/kelp_retrospective_replay.md` Phase 8) enumerates quote-safe Tier A claims and explicitly rejects overclaim candidates ("Layer 3 would have prevented Kelp" — rejected because we have no enforcement layer).
- Correction-log entries #3–8 all carry explicit Tier A / Tier B separation within each correction's structure.
- API envelope (`web/api_v1.py::_ok`) carries the `epistemic_tag` convention as a JSON field in alert payloads, per Correction #6 resolution.

**Cross-references.** [Accountability-as-Load-Bearing](#accountability-as-load-bearing) (epistemic discipline IS the self-imposed accountability layer Layer 3 runs), [The Proofreading Trap](#the-proofreading-trap) (the tier discipline is what prevents us from falling into the trap of claiming we catch what we don't).

---

## Living document conventions

- **Adding entries.** When a new framework-level observation emerges from a session, append it to the appropriate category with the same format (definition, extended description, empirical grounding, cross-references). Update the index.
- **Revising entries.** When evidence refines an existing entry, update the entry and append a note to `reports/correction_log.md` if the revision changes a previously-published claim.
- **Cross-referencing.** Internal references use `[#anchor]` markdown format. External references to reports use file paths (`reports/*.md`, `l3-narrative/*.pptx`).
- **Defensibility check before external publication.** Every entry in Core Architectural, Attack Pattern, and Commercial/Positioning categories should survive expert review. If a Tier A claim in an entry cannot be reproduced by a reader with corpus access, the entry needs revision before external use.

**Next entries anticipated (not yet added, placeholders):**
- The LayerZero DVN configuration-enumeration module, once built (cross-refs Pattern D, Configuration-Level Vulnerability, External Accountability Infrastructure).
- Bridged-asset conservation check methodology, once scoped (cross-refs Compositional Harm, EXTRACTION_007).
- Any framework concept that emerges from re-scans of Patterns A, B, E, F after corpus age ≥ 90 days.
