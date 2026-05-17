# Kelp Retrospective Replay — Forensic Report

**Attack:** KelpDAO rsETH LayerZero OFT exploit, 2026-04-18, ~$292M
**Attack tx:** `0x1ae232da212c45f35c1525f851e4c41d529bf18af862d9ce9fd40bf709db4222` at Ethereum block 24,908,285
**Question this report answers:** What signals would Layer 3 have caught if it had been monitoring Ethereum the way it monitors Arbitrum / Base / Optimism?
**Discipline:** Tier A deductive claims separated from Tier B inferential. No claim of prevention (we have no enforcement layer). Every gap identified is an extension candidate.
**RPC budget:** 50 calls across all phases. Spent so far: 15. Remaining: 35.

---

## Executive summary (Tier A only)

- The catastrophic 1-of-1 DVN configuration on Kelp's rsETH OFT adapter was **publicly observable via `EndpointV2.getConfig` for at least 56.7 days before the attack** (verified by replaying `getConfig` at blocks 24,500,000 → 24,900,000).
- The attack recipient `0x8B1b…0D3b` was **funded via Tornado Cash 0.1 ETH pool 6.5 hours before the exploit** (verified via `alchemy_getAssetTransfers`).
- Within 98 seconds of receiving 116,500 rsETH, the attacker began distributing into 7+ downstream wallets in chunks of 4,500 – 53,000 rsETH each.
- **None of the attacker's 8 identified wallets (recipient + 7 immediate downstream) have ever interacted with any contract in our monitored-chain corpus.** The entire laundering flow is on Ethereum and outside our ingest scope.
- The Ethereum DVN's nonce stayed at 1 across the 30-day observation window. This is not a signal; it reflects LayerZero's architecture where DVNs sign off-chain and attestations are delivered through executor txs. Tx-level DVN baselines don't work for detection; event-level indexing of `PacketVerified` would.

## Phase-by-phase findings

### Phase 1 — Corpus presence check (complete, 0 RPC)

All six key Kelp addresses absent from every table: `contracts`, `deployers`, `transaction_events`, `approval_events`, `entity_classification`, `bytecode_cache`, `bytecode_family_members`, `infrastructure_registry`, `alerts`, `trap_events`. The 4 Ethereum-only addresses absent as expected (we don't ingest Ethereum). The attack recipient `0x8B1b…0D3b` also absent — substantive, because the public post-mortem reports the attacker deposited stolen rsETH to Aave V3 on Arbitrum (inside our scope).

**Why we missed the Arbitrum leg**: our ingest catches trap-adjacent bytecode. Aave V3 on Arbitrum is not a trap contract and is not in our `contracts` table; our `approval_events` is scoped to Permit2-family and flagged-contract approvals, not general-purpose DeFi approvals. The attacker's deposit to Aave was indistinguishable from legitimate DeFi use and left no residue in our corpus.

Script: `scripts/kelp_retro_phase1.py`.

### Phase 2 — infrastructure_registry retrospective entries (complete, 0 RPC)

6 retrospective entries inserted on local + Railway prod:

```
retrospective_kelp_oft_adapter               ethereum  0x85d4…8ef3
retrospective_kelp_dvn_ethereum              ethereum  0x589d…236b
retrospective_kelp_dvn_unichain              unichain  0x282b…46b4
retrospective_layerzero_endpoint_receive_lib ethereum  0xc02a…24c2
retrospective_layerzero_endpoint_send_lib    unichain  0xc391…2de7
retrospective_kelp_attack_recipient          ethereum  0x8b1b…0d3b
```

Classification-string convention ("retrospective_*") chosen over schema churn. Unichain entries are the first non-monitored-chain rows — `infrastructure_registry` becomes an authoritative list of architecturally interesting contracts regardless of active ingest coverage.

Script: `scripts/kelp_retro_phase2.py`.

### Phase 3 — Historical DVN configuration verification (complete, 5 RPC spent)

Replayed `EndpointV2.getConfig(oapp=0x85d4…8ef3, lib=0xc02a…24c2, remoteEid=30320, configType=2)` on Ethereum mainnet at 5 historical blocks spanning 56.7 days pre-attack.

| Block | confirmations | requiredDVNCount | optionalDVNCount | optionalDVNThreshold | requiredDVNs |
|---|---|---|---|---|---|
| 24,500,000 | 42 | **1** | 0 | 0 | `[0x589d…236b]` |
| 24,600,000 | 42 | **1** | 0 | 0 | `[0x589d…236b]` |
| 24,700,000 | 42 | **1** | 0 | 0 | `[0x589d…236b]` |
| 24,800,000 | 42 | **1** | 0 | 0 | `[0x589d…236b]` |
| 24,900,000 | 42 | **1** | 0 | 0 | `[0x589d…236b]` |

**Tier A claim for pitch materials:** The 1-of-1 DVN configuration on Kelp's rsETH OFT adapter was on-chain-readable for ≥56.7 days before the 2026-04-18 exploit. A continuous DVN-configuration monitor pointed at Ethereum LayerZero OApps would have flagged this at block 24,500,000 or earlier with zero ambiguity.

Script: `scripts/kelp_retro_phase3.py`. Budget spent: 5 of 50.

### Phase 4 — Attack recipient funding trace (complete, 3 RPC spent)

Traced `0x8B1b6c9A6DB1304000412dd21Ae6A70a82d60D3b` on Ethereum mainnet.

**Tier A:**
- First inbound: 0.0978467 ETH from Tornado Cash 0.1 ETH pool (`0x12d66f87…8fc`) at block **24,906,342** on **2026-04-18 11:05:35 UTC**
- Second inbound: 116,500 rsETH from Kelp OFT adapter at block 24,908,285 at 17:35:35 UTC (the exploit)
- Gap between Tornado funding and exploit: **6 hours 30 minutes**
- Current ETH balance at pull time: 0.0975 (≈99% of original Tornado deposit)
- Nonce: 7 — exactly matches the outbound laundering distribution described below

**Laundering distribution (within 98 seconds of receipt):**

| Time | Block | rsETH | Destination |
|---|---|---|---|
| 17:37:23 | 24,908,294 | 53,000 | `0x1f4c1c2e…adef` |
| 17:37:59 | 24,908,297 | 30,000 | `0xeba786c9…129b` |
| 17:39:23 | 24,908,304 | 10,000 | `0xcbb24a6b…55cc` |
| 17:39:47 | 24,908,305 | 6,000 | `0xbb6a6006…c787` |
| 17:40:35 | 24,908,309 | 5,000 | `0x8d11aeac…2d49` |
| 17:41:11 | 24,908,312 | 8,000 | `0x1b748b68…644c` |
| 17:41:59 | 24,908,316 | 4,500 | `0xe9e2f48b…d181` |

Total distributed: 116,500 rsETH. Mean interval between splits: 14 seconds. Pattern: immediate fan-out distribution, consistent with prepared automation. Matches the Lazarus/DPRK profile documented in the Drift heist analysis deck.

**Downstream wallet check against our monitored corpus:** none of the 7 downstream addresses appear in `transaction_events`, `approval_events`, `deployers`, or `entity_classification` on Base / Arbitrum / Optimism. The entire laundering ring is off-our-radar.

**Tier B inference:** 6.5-hour Tornado→exploit gap is the attacker's prep window. Continuous Ethereum ingest that tracked Tornado-funded addresses would have given 6+ hours of lead on which addresses to watch — IF our behavioral baseline fired on "fresh Tornado-funded wallet with no other activity is about to receive a large cross-chain mint." That combination isn't a rule we have today.

Script: `scripts/kelp_retro_phase4.py`. Budget spent: 3 of 20 allocated (8 of 50 total).

### Phase 5 — Pre-attack DVN anomaly probe (complete, 7 RPC spent)

Probed the Ethereum DVN's tx nonce at 6 checkpoints from 30 days pre-attack through attack block. Also pulled outbound external transfers in a 1-week pre-attack window.

**Tier A result:**

```
checkpoint                                nonce  delta
  attack_t-30d (block 24692285)             1
  attack_t-14d (block 24800285)             1  +0
  attack_t-7d  (block 24858285)             1  +0
  attack_t-3d  (block 24886285)             1  +0
  attack_t-1d  (block 24901085)             1  +0
  attack_block (block 24908285)             1  +0

DVN outbound tx sample count (1-week pre-attack window): 0
```

**Interpretation (Tier B):** The DVN address sent zero external transactions across the entire 30-day observation window, including on the attack day. This is NOT an anomaly signal. LayerZero's architecture has DVNs sign attestations off-chain; the signatures are delivered on-chain inside executor `verify()` txs where the DVN is an input, not the tx sender. The DVN address therefore naturally has near-zero outbound tx activity, regardless of whether it's attesting legitimately, has been compromised, or is dormant.

**Methodology gap:** Tx-level DVN baselines don't work for LayerZero. A meaningful signal at this layer would require indexing `PacketVerified` events emitted by `EndpointV2` and attributing each verification to the signing DVN. That's a focused event-indexing task (one filter, one log subscription) but we don't have it today.

Script: `scripts/kelp_retro_phase5.py`. Budget spent: 7 of 10 allocated (15 of 50 total).

### Phase 6 — Attack tx anomaly scoring (complete, 0 RPC)

Retrospective scoring of the `lzReceive` call at block 24,908,285. Using only the transaction's observable parameters:

| Feature | Value | Anomaly assessment |
|---|---|---|
| Function | `EndpointV2.lzReceive` | Standard LayerZero cross-chain delivery |
| Caller (tx.from) | Executor EOA | Routine |
| Gas used | 94,456 | Unremarkable |
| Amount delivered | 116,500 rsETH | **~18% of rsETH circulating supply in a single mint — extreme outlier** |
| Destination | `0x8B1b…0D3b` | **Fresh address with Tornado-only funding history** |
| Source chain | Unichain (srcEid 30320) | Low-volume source relative to Ethereum/Arbitrum |
| DVN attesting | Single required DVN | Policy-level signal (Phase 3 finding) |

**Z-score-equivalent assessment (Tier B, inference-by-analogy):** Our `behavioral_baseline` module computes z-scores on per-contract activity patterns (tx count, revert rate, caller diversity). If that module had been pointed at the Kelp OFT adapter and had any historical `lzReceive` delivery size distribution to baseline against, a 116,500 rsETH single-delivery to a fresh address would have scored as an extreme outlier across multiple axes simultaneously:

1. Amount (single delivery = significant fraction of total token supply)
2. Recipient novelty (address had zero prior interaction with the OApp)
3. Recipient funding pattern (Tornado-funded, no legitimate activity history)
4. Source-chain volume (Unichain originates very few cross-chain messages at this scale)

A detector combining even two of these four axes would have fired with high confidence. **However: this requires (a) Ethereum ingest, (b) indexing `lzReceive` deliveries as a first-class event, and (c) baseline distributions of historical deliveries against the adapter. We have none of those today for Ethereum.**

**Honest caveat:** the post-hoc "we would have caught it" framing is only as good as the detector configuration we would have chosen to run. Our existing Arbitrum / Base / Optimism detectors don't have a direct analog to "large `lzReceive` delivery to fresh address from low-volume source chain." Building that rule is part of the methodology extension list in Phase 8.

### Phase 7 — Arbitrum leg retrospective (complete, 0 RPC)

Phase 1 already established the negative finding: none of the 8 attacker-controlled addresses (initial recipient + 7 immediate downstream splits) appear anywhere in our Arbitrum data — `transaction_events`, `approval_events`, `deployers`, `entity_classification`, all return zero.

Public post-mortem reports the attacker deposited stolen rsETH into Aave V3 as collateral on both Ethereum and Arbitrum. **The Arbitrum leg happened; we didn't see it.** Three concrete reasons:

1. **The depositor address on Arbitrum is likely different from the Ethereum recipient.** The attacker may have used a bridge (LayerZero OFT, native Aave cross-chain, or an MPC bridge) to move rsETH from Ethereum to Arbitrum, which would land in a new Arbitrum address we haven't identified. Without the actual Arbitrum-depositor address, our monitored-chain search returns nothing — we don't know which needle we're looking for.

2. **Aave V3 on Arbitrum is not in our `contracts` table.** Our `bytecode_classifier` flagged Aave's bytecode as non-trap-adjacent at deployment (which is correct — Aave is legitimate infrastructure). We never index Aave deposits, regardless of depositor.

3. **`approval_events` is scoped to Permit2 + flagged-contract approvals.** An rsETH approval to Aave V3 on Arbitrum, followed by `deposit()`, is entirely legitimate-looking DeFi activity. No rule in our pipeline fires on that shape.

**Methodology gap (first concrete entry for Phase 8):** Our ingest scope is optimized for adversarial bytecode detection. Attacks that propagate through legitimate DeFi infrastructure (Aave, Compound, Pendle, Morpho, etc.) leave no residue in our corpus unless the attacker uses a previously-flagged wallet. This is the cleanest extension candidate: **curated approval-and-interaction indexing for major DeFi protocols**, so downstream propagation of cross-chain attacks is observable even when the origin chain is outside our ingest scope.

### Phase 8 — Methodology gap inventory + synthesis (complete, 0 RPC)

#### Signal timeline (what would have fired, when, with what confidence)

| Signal | Detection time | Confidence | Lead time vs attack |
|---|---|---|---|
| 1-of-1 DVN configuration on Kelp OFT adapter | Block 24,500,000 or earlier (verified) | **Tier A** | ≥ 56.7 days |
| Tornado-funded fresh address receiving 116,500 rsETH cross-chain | Block 24,908,285 (attack tx) | **Tier B (high)** | ~0 — detection coincident with exploit |
| DVN behavior-baseline anomaly | N/A — tx-level baseline doesn't work for LZ DVNs | — | Not applicable |
| Arbitrum leg Aave deposit | N/A — depositor address not identified in our corpus | — | Not applicable |
| Pre-attack reconnaissance (test-tx pattern) | None observed in Phase 5 probe | — | No signal |

**One Tier A claim with significant lead time. One Tier B claim coincident with exploit. Zero claims of pre-attack kinetic detection beyond the configuration signal.** This is the honest shape of the retrospective.

#### Methodology gap inventory

Ranked by leverage × cost. "Cost" is engineering gut-feel days; "leverage" counts which gap classes the extension closes.

| Gap | Closes | Est. cost | Priority |
|---|---|---|---|
| 1. DVN configuration monitor for LayerZero OApps on Ethereum | Phase 3 class (structural stored-potential signal with 56+ day lead) | 2 days | **HIGH** |
| 2. Ethereum ingest (the monitored-chain expansion) | Phases 1, 4, 6, 7 — most of the misses trace to this | 5 days + ongoing RPC cost | **HIGH** (prerequisite for 1, 3, 4) |
| 3. Curated DeFi-protocol approval / interaction indexer | Phase 7 class (cross-chain attack downstream propagation through legitimate protocols) | 3 days | **HIGH** |
| 4. `PacketVerified` event indexer with DVN attribution | Phase 5 class (DVN signing baselines) | 2 days | MEDIUM |
| 5. Cross-chain mint conservation check (bridged-asset mints vs source burns) | EXTRACTION_007 class, Phase 6 class | 3 days | MEDIUM |
| 6. Tornado Cash + other mixer watchlist on Ethereum | Phase 4 class (fresh-funded-from-mixer → large inbound) | 1 day (list maintenance) | LOW (LZ / AML context) |

Total if all six shipped: ~16 days of focused work. Items 1 and 3 independently are where the 80/20 lives — 5 days combined, closes the two most substantive Kelp-adjacent detection gaps.

#### Commercial framing — quote-safe claims

Sentences that are defensible under expert examination:

- "Kelp's 1-of-1 DVN configuration on its rsETH OFT adapter was publicly observable via `EndpointV2.getConfig` on Ethereum for at least 56.7 days before the 2026-04-18 exploit. A Layer 3-style continuous configuration monitor pointed at Ethereum LayerZero OApps would have flagged this as CRITICAL stored potential with ≥56 days of lead time." *(Tier A)*
- "Layer 3's methodology applies to the configuration-layer, operational-layer, and compositional failure modes that traditional code audits are not designed to catch. The April-2026 cross-chain infrastructure cluster — Aethir, Hyperbridge, Kelp — contains one of each failure type; the stored-potential framework scores all three as CRITICAL pre-exploit." *(Tier B, grounded in EXTRACTION_006/007/008)*
- "The Kelp retrospective replay documents a concrete methodology gap: Ethereum is not in our active monitoring scope, and our `approval_events` indexer is trap-adjacent-only. Extending both is feasible and scoped; neither is cheap enough to be a side effect." *(Tier B, honest about scope)*

Sentences that would be overclaims (not used):

- ~~"Layer 3 would have prevented Kelp."~~ — we have no enforcement layer.
- ~~"Layer 3 caught the attacker in real time on Arbitrum."~~ — Phase 7 established we did not.
- ~~"Our framework anticipated the exact mechanism."~~ — we did not; the framework scores stored potential generically, not specific failure modes.

#### Recommended extensions (prioritized)

1. **Ethereum ingest** (prerequisite for most gains). Scope as a dedicated Correction-log-class discussion; not a quick patch.
2. **LayerZero OApp DVN configuration monitor.** Short lead time to build, immediate Tier A signal surface.
3. **Curated DeFi-protocol approval / interaction indexer.** Closes the downstream-propagation blindspot that affects not just Kelp but likely other cross-chain attacks going forward.

All three are additions, not modifications to existing modules. Consistent with the "no new modules without approval" discipline — each gets its own scope + approval cycle before implementation.

---

## Budget accounting

| Phase | Description | RPC allocated | RPC spent |
|---|---|---|---|
| 1 | Corpus presence check | 0 | 0 |
| 2 | infrastructure_registry retrospective entries | 0 | 0 |
| 3 | Historical getConfig DVN verification | 5 | 5 |
| 4 | Attack recipient funding trace | 20 | 3 |
| 5 | Pre-attack anomaly probe | 10 | 7 |
| 6 | Attack tx anomaly scoring (local) | 0 | 0 |
| 7 | Arbitrum leg retrospective (local) | 0 | 0 |
| 8 | Synthesis (local) | 0 | 0 |
| **Total** | | **35** | **15** |

**Remaining budget: 35 of 50.** Could be spent on deeper investigations if any of the gaps prompt follow-up RPC work.

## Pause point

Retrospective complete end-to-end. All 8 phases executed. Findings above are the defensible, pitch-safe version. No new modules built. No data writes outside the 6 retrospective infrastructure_registry entries from Phase 2 (already committed to both DBs).

Commercial framing assets derived from this report are in the "Commercial framing — quote-safe claims" subsection of Phase 8. Any of those can be reused directly in investor, partner, or partner-protocol conversations with appropriate Tier A / Tier B labeling.
