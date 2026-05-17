# Extraction Event 006 — Aethir OFTAdapter (BNB Chain)

**Event date:** 2026-04-09
**Chain:** BNB Chain (OFF our monitored chains — Base / Arbitrum / Optimism)
**Purpose:** Corpus expansion. Precursor case to EXTRACTION_008 (Kelp). Same OFT-adapter attack family, different compromise mechanism.
**Status:** Draft INSERT. Nothing executed.

---

## The one-line frame

Same architecture, smaller scale, earlier date. **Aethir is the case study that shows the Kelp attack family was already live nine days before Kelp.** Both would score CRITICAL pre-attack on Layer 3's stored-potential framework; both proceeded to exploitation.

## Tier A claims

Sourced from the dev.to developer post-mortem (2026-04-09) and public BNB Chain explorer state.

- 2026-04-09 attacker gained admin privileges over `AethirOFTAdapter`
- The adapter owner was a **single EOA** — no multisig, no timelock
- Post-admin, the attacker drained bridged assets held by the adapter
- Laundering route: BNB Chain → TRON via Symbiosis Finance
- Gross drain ~$400K
- Net user loss <$90K after recovery actions (likely project-treasury backstop)

## Tier B interpretations

- **Attack family:** OFT-adapter admin compromise. Same family as EXTRACTION_008 (Kelp).
- **Compromise mechanism:** private-key compromise of the owning EOA. Distinct from Kelp's DVN configuration failure. Both are **non-code failures** — operational-control and architectural-configuration respectively — that expose maximum-capability contracts to single-point-of-failure seizure.
- **Stored-potential pre-attack:** VERY HIGH. Maximum capability (mint authority), single-point-of-failure permissions, maximum trust binding (Aethir brand), zero constraint (no timelock). Per the core interpretive rule from `CLAUDE.md`, this is peak stored potential — exactly the state the framework identifies as loaded, not safe.
- **Strategy Lifecycle placement:** precursor event in the April-2026 cross-chain infrastructure cluster. Aethir (04-09) → Hyperbridge (04-13) → Kelp (04-18) — three exploits in nine days against the same structural target (pooled-custody cross-chain adapters), three different mechanisms. Matches the EARLY→ARMS_RACE transition timing observed in the oracle-manipulation-lending family (Drift → Rhea, 15 days).

## What Layer 3 would have caught pre-attack

- Adapter-contract ownership enumeration: the single-EOA owner was on-chain-readable. A registry check "adapter of >= $N TVL has EOA owner with no multisig" would have flagged this pre-exploit.
- Our current infrastructure isn't positioned for this — we don't monitor BNB Chain, and the `infrastructure_registry` we just built (12 rows) covers Circle CCTP only, not LayerZero adapters.
- Extension path: add LayerZero OFT adapters + their ownership structures to `infrastructure_registry` across all chains. Enumeration is one-shot per adapter; maintenance is a weekly refresh. Out of scope for this entry; flagged for the cluster-analysis discussion after EXTRACTION_008 lands.

## What Layer 3 would NOT have caught

- The actual private-key compromise. That's an off-chain event — phishing of an Aethir dev, SIM swap, malware, key theft. Our observation surface doesn't reach into operational security at the employee/device level.
- The specific timing. We could have scored the adapter as CRITICAL pre-attack, but not predicted 2026-04-09 as the discharge date.

## Cross-links

- **EXTRACTION_008 (Kelp)** — same attack family, 9 days later, 730× the dollar scale
- **EXTRACTION_007 (Hyperbridge)** — same cluster, code-layer variant
- **EXTRACTION_005 (Drift)** — parallel pattern at governance layer (dropped timelock + threshold)
- **`reports/circle_bridge_infrastructure.md`** — analogous analysis of Circle's CCTP; same 'known-legitimate high-stakes infrastructure' class, with maximum capability and maximum trust binding. CCTP is the properly-configured version of what Aethir's adapter was not.

## What the INSERT contains

Full Tier A facts in the summary, Tier B interpretations in the notes with explicit labels. Raw JSON includes adapter contract name, compromise mechanism, pre-attack state (owner_type=EOA, multisig_present=False, timelock_present=False), laundering path, dollar figures, and sibling-event cross-references.

`chain='bnb'`, `monitored_chain=0`. Consistent with the Rhea (NEAR) and Drift (Solana) pattern for off-chain reference events.

## What this file does NOT claim

- No attribution of the key compromise to a specific actor. The dev.to post-mortem uses "private key compromise" as its root-cause framing; we don't attempt operator identification.
- No quantitative stored-potential score (would require the adapter's transaction history and capability graph — we don't index BNB Chain).
- No claim about Aethir's post-incident operational response.
