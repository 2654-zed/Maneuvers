# Extraction Event 007 — Hyperbridge Token Gateway MMR Proof Bypass

**Event date:** 2026-04-13
**Chain:** Ethereum (monitored_chain=1 — on our monitored chains)
**Purpose:** Corpus expansion. Code-level variant in the April-2026 cross-chain infrastructure cluster.
**Status:** Draft INSERT. Nothing executed.

---

## The one-line frame

**The only April-2026 bridge exploit caused by an actual code bug** — a missing out-of-bounds check on Merkle Mountain Range leaf-index validation that let crafted proofs bypass verification. Distinct from Aethir (operational) and Kelp (configuration).

## Tier A claims

- 2026-04-13: `HandlerV1.handlePostRequests` accepted a crafted MMR proof with an out-of-bounds leaf index, bypassing proof validation
- Two-phase attack:
  - **Phase 1:** ~245 ETH extracted via an early-test message (testing the vulnerability)
  - **Phase 2:** ~1B bridged DOT tokens minted on Ethereum without a corresponding source-chain burn
- Chains affected as bridging destinations: Ethereum, Base, BNB, Arbitrum
- Initial on-chain loss estimate: $237K (reconciliation pending; bridged-DOT holders' fair-value impact may revise)

Source material: Hyperbridge public incident statement + the GitHub commit history for the affected function.

## Tier B interpretations

- **Attack family:** cross-chain proof verification bypass. Distinct subcategory from the operational (Aethir) and configuration (Kelp) failures in the same April-2026 cluster.
- **Audit-catchable?** This is the ONE exploit in the April-2026 cross-chain cluster that a traditional code audit could plausibly have caught. The bug was in verifiable code paths at a specific function. Whether audits actually reviewed `handlePostRequests` at the depth needed to catch an out-of-bounds check is unknown — empirical fact is the bug reached production.
- **Detection-surface implication:** The downstream ECONOMIC signal was detectable in near-real-time: a ~1B-token mint on Ethereum with no corresponding source-chain burn is a bridged-asset accounting anomaly. A surveillance module that enumerates bridged-asset mint events and cross-checks against known source-chain burns (cross-chain conservation check) would have caught this within minutes. Not built; architectural extension candidate.

## Why this matters for the corpus story

Hyperbridge is the reference point against which Aethir and Kelp are measured. The April-2026 cluster contains three architecturally distinct failure modes:

- **Aethir:** off-chain operational failure (key compromise)
- **Hyperbridge:** on-chain code failure (missing validation guard)
- **Kelp:** on-chain configuration failure (1-of-1 DVN)

A single architectural class (pooled-custody cross-chain messaging) failed in three orthogonal ways within nine days. **The diversity of failure modes is the commercial point.** A security posture defending only against code bugs (traditional audits) catches Hyperbridge but misses Aethir and Kelp. A posture that also watches operational controls catches Aethir. A posture that enumerates configurations catches Kelp. Layer 3's stored-potential framework catches all three by measuring the same underlying property — capability without sufficient constraint — rather than any specific failure mode.

## What Layer 3 would have caught pre-attack

- **Nothing in our current detection surface.** The MMR bypass is Solidity logic for cross-chain verification, outside the trap-signature space our classifier targets.
- Catchable in principle via bridged-asset conservation check (inbound mints vs outbound burns); would require dedicated cross-chain ingest module.
- The ~$237K initial loss estimate is below the commercial-attention threshold for most security teams; this event probably gets under-reported.

## What Layer 3 would NOT have caught

- The specific MMR leaf-index bypass as a code-review finding. Our pipeline doesn't do static analysis of bridge-verification functions. Code audits remain the right tool for this failure mode.
- Phase 1 of the attack (~245 ETH) was small enough to plausibly look like test traffic. Without the conservation check, distinguishing it from legitimate bridge activity is hard.

## Cross-links

- **EXTRACTION_006 (Aethir)** — cluster sibling, 4 days earlier, operational-layer variant
- **EXTRACTION_008 (Kelp)** — cluster sibling, 5 days later, configuration-layer variant, 1,232× the dollar scale
- **EXTRACTION_005 (Drift)** — a different-family parent: Drift was oracle-manipulation-lending, not cross-chain-bridge. Mentioned for contrast in the April-2026 exploit calendar.

## What the INSERT contains

Summary contains Tier A facts (date, contract name, two-phase attack description, initial dollar figure). Notes carry the Tier B interpretation with explicit labels: attack-family classification, audit-catchability framing, cluster grouping, and the conservation-check detection proposal.

`chain='ethereum'`, `monitored_chain=1`. **This is the first monitored-chain event in our extraction_events table** (001–003 are on monitored L2s without specific chain tagging; 004–006 are off-chain reference). Hyperbridge is the first case where our chain-scoped analysis directly applies.

## What this file does NOT claim

- No attribution of the exploit operator to a specific actor.
- No claim about which audit (if any) reviewed `handlePostRequests` before deployment.
- No final dollar figure — initial $237K estimate is likely to be revised as bridged-DOT holders reconcile their positions.
- No protocol-partner outreach implied. This event is documented for corpus consistency; commercial conversations about bridges should reference the entire April-2026 cluster, not individual events.
