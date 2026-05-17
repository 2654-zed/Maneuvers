# Extraction Event 008 — KelpDAO LayerZero DVN Configuration Failure

**Event date:** 2026-04-18
**Chain:** Ethereum (destination, monitored_chain=1). Source: Unichain.
**Purpose:** Corpus expansion. Largest April-2026 exploit; configuration-layer variant of the cross-chain infrastructure cluster.
**Status:** Draft INSERT. Nothing executed. Paired with deeper retrospective at `reports/kelp_retrospective_replay.md` (scoped separately, 50-call RPC budget).

---

## The one-line frame

**The configuration was publicly observable for weeks pre-exploit** — `EndpointV2.getConfig` returns `requiredDVNCount=1` on both chains; LayerZero's own documented best practice is `>=2 required DVNs`. The exploit took zero code defects, zero compromised admin keys, zero novel mechanism — just an attacker willing to compromise a single validator in a system that accepted single-validator attestation.

## Tier A claims

Sourced from `github.com/DK27ss/KelpDAO-294m-PoC` + Blockaid statement + LayerZero network response.

**Attack**
- Attack tx: `0x1ae232da212c45f35c1525f851e4c41d529bf18af862d9ce9fd40bf709db4222`
- Ethereum block: 24,908,285 (pre-state block 24,908,284)
- Entry: single call to `EndpointV2.lzReceive`, gas used 94,456
- Source chain: Unichain (srcEid 30320)
- 116,500 rsETH minted to attacker at nonce 308 — ≈ 18% of rsETH circulating supply
- 40,000 rsETH at nonce 309 BLOCKED via Kelp's `TransfersBlocked` at 2026-04-19 18:23:11 UTC

**Key addresses**
- Kelp OFTAdapter (Ethereum): `0x85d456B2DfF1fd8245387C0BfB64Dfb700e98Ef3`
- Required DVN (Ethereum): `0x589dedbd617e0cbcb916a9223f4d1300c294236b`
- Required DVN (Unichain): `0x282b3386571f7f794450d5789911a9804fa346b4`
- Attack recipient (fresh address): `0x8B1b6c9A6DB1304000412dd21Ae6A70a82d60D3b`

**Configuration at time of attack (verifiable via `getConfig(configType=2)`)**
| Chain | requiredDVNCount | optionalDVNCount | optionalDVNThreshold |
|---|---|---|---|
| Unichain (source) | 1 | 0 | 0 |
| Ethereum (destination) | 1 | 0 | 0 |

**Downstream propagation**
- Attacker deposited stolen rsETH to Aave V3 as collateral on **Ethereum AND Arbitrum**
- Borrowed ~$236M WETH against the rsETH
- Bad debt on Aave V3 post-unbacked

## Tier B interpretations

- **Attack family:** cross-chain DVN verification failure. Distinct from Aethir (operational key compromise) and Hyperbridge (code-layer MMR bypass); all three are April-2026 cross-chain infrastructure cluster events.
- **Stored-potential pre-attack:** CRITICAL. Per the core interpretive rule, maximum capability (mint authority) + maximum trust binding (Kelp + LayerZero) + maximum victim exposure (rsETH holders) + zero constraint (1-of-1 DVN). Exactly the state the framework identifies as loaded-not-safe.
- **Detection surface:** DVN configuration enumeration. LayerZero DVN configs are read-only public data on-chain; a surveillance module that polled OApp configurations and flagged `requiredDVNCount=1` would have scored Kelp CRITICAL with significant lead time. The retrospective replay report quantifies "significant" via historical `getConfig` calls at earlier blocks.
- **Why not Circle/Tether freeze:** rsETH is a yield-bearing LRT (Liquid Restaking Token), not a stablecoin. No Circle or Tether pathway applies. Recovery likely requires protocol-native action by Kelp and downstream counterparties (Aave, LayerZero).

## What Layer 3 currently catches vs misses

**Catches (retrospectively verifiable via Phase 7 of kelp_retrospective_replay.md):**
- Attack recipient's downstream Arbitrum Aave V3 deposits (if the attacker used our monitored chain post-Ethereum-mint, our `transaction_events` / `approval_events` should have captured it)

**Misses:**
- The entire Ethereum origin — we don't monitor Ethereum
- LayerZero OApp configurations — no module enumerates these
- DVN signing-activity baselines — not indexed
- Unichain — not monitored
- Code-level MMR-style bugs (see EXTRACTION_007 — bridges can fail in three orthogonal ways; our current surface catches none)

**Potentially catches if extensions approved:**
- DVN configuration monitoring (new module scoped in notes; cost estimate: ~150 LoC)
- Cross-chain mint-event conservation check (from EXTRACTION_007 notes): bridged-asset inbound mints vs source-chain burns — would have flagged the forged lzReceive within blocks

## Cluster framing (Aethir / Hyperbridge / Kelp)

| | Aethir (EXTRACTION_006) | Hyperbridge (EXTRACTION_007) | Kelp (EXTRACTION_008) |
|---|---|---|---|
| Date | 2026-04-09 | 2026-04-13 | 2026-04-18 |
| Failure layer | Operational (key) | Code (validation) | Configuration (DVN) |
| Loss | $400K | $237K | $292M |
| Audit-catchable? | No | Yes (in principle) | No |
| Publicly observable pre-attack | No | No | Yes (on-chain config read) |

Three orthogonal attack vectors in nine days against the same structural target. The diversity of failure modes is the commercial framing point: traditional audits (code-only) catch at most 1 of 3; Layer 3's stored-potential lens catches all 3 by measuring capability-vs-constraint directly.

## Cross-links

- **EXTRACTION_006 (Aethir)** — operational precursor, 9 days earlier
- **EXTRACTION_007 (Hyperbridge)** — code-layer cluster sibling, 5 days earlier
- **EXTRACTION_005 (Drift)** — parallel "stored potential via removed constraint" at governance layer; Drift dropped multisig threshold + timelock; Kelp accepted 1-of-1 DVN from deployment
- **`reports/kelp_retrospective_replay.md`** — the deep retrospective (scoped 50-RPC budget, 8 phases, paused at every phase boundary) that answers "what signals would Layer 3 have caught if it monitored Ethereum and LayerZero OApp configurations"
- **`reports/behavioral_laundering_detection_scope.md` Pattern D** — the 54% cross-chain reputation-import finding shares a substrate with this cluster: both are cross-chain-surface observations our single-chain profiling misses

## What the INSERT contains

Full Tier A facts in summary + raw_transactions JSON. Notes carry Tier B interpretations with explicit labels. `chain='ethereum'`, `monitored_chain=1`.

Note: EXTRACTION_007 and EXTRACTION_008 are both on Ethereum / `monitored_chain=1`. That doesn't mean our active monitor covered them — Ethereum is NOT currently in our ingest set. `monitored_chain=1` here reflects that Ethereum IS on the "chains we would monitor if we expanded" roster, vs 0 for truly out-of-scope (NEAR, Solana, BNB). The field distinguishes first-class-target chains from reference-data chains. If that's the wrong convention, the classification will be easy to revise; no other table joins this column today.

## What this file does NOT claim

- No prevention claim. Flagging stored potential is not the same as preventing exploitation. Layer 3 has no enforcement layer.
- No attribution of the compromised DVN operator. Whether the attacker obtained signing keys via compromise or was the DVN operator is not established.
- No final Recovery figure. Coordination between Kelp / LayerZero / Aave is ongoing as of documentation date.
- No quote-ready claim without retrospective validation. The retrospective replay report is where "would-have-caught" claims get Tier A substantiation (historical getConfig calls, DVN signing-activity baselines, etc.). Until that report lands, all "Layer 3 would have caught X" statements here are labeled Tier B.
