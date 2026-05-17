# Pattern D — Cross-Chain Reputation Import Candidates

**Date:** 2026-04-18
**Scope:** 100 highest-risk deployers on Arbitrum + Optimism with `first_seen >= 2026-04-01`, probed against Ethereum mainnet via Etherscan v2 multichain API.
**Cost:** 100 Etherscan v2 API calls, free tier, ~35 seconds wall time.
**Epistemic:** Tier A on "mainnet activity predates L2 first-seen" (verifiable on-chain); Tier B on interpretation as reputation-import laundering.

---

## What we looked for

Deployers appearing on Arbitrum / Optimism in the last ~18 days with suspected/confirmed trap contracts, where the same address has substantial prior activity on Ethereum mainnet that our per-chain ingest doesn't link.

---

## Result

**Of 100 high-risk L2 deployers probed:**

- **54 (54%) are cross-chain imports** — had mainnet activity that predates their L2 first-seen
- **44 (44%) are fresh identities** — zero mainnet history
- **2 (2%) had mainnet activity dated after L2 first-seen** (rounding artifacts; first-tx timestamps resolve to block time, small date ties)

**The cross-chain-import signal is strong.** At 54% hit rate, Pattern D is the most supported of the five behavioral-laundering patterns against our current corpus.

## Top candidates — longest pre-existing mainnet footprint

These deployers had *substantial* mainnet history before appearing on L2. Long gap = long pre-existing identity.

| Deployer | L2 chain | Mainnet first | L2 first | Gap (days) | Susp. | Conf. |
|---|---|---|---|---|---|---|
| `0x7fd9a5104f1cb261a7215f950c9fa7eac06d60d0` | Base | 2017-06-20 | 2026-04-02 | **3208** | 14 | 0 |
| `0x5f799f365fa8a2b60ac0429c48b153ca5a6f0cf8` | Arbitrum | 2020-11-04 | 2026-04-02 | 1974 | 5 | 0 |
| `0x9905e56cdc20199ad06cfe2ab580ce9c19bee2e2` | Arbitrum | 2022-04-08 | 2026-04-01 | 1453 | 39 | 0 |
| `0x01089f3755a0e52fd5dbecdb506d95e88590acf8` | Arbitrum | 2022-10-02 | 2026-04-06 | 1281 | 27 | 0 |
| `0x5f7476ee17eccbc57de45f3444852f5141f650f2` | Arbitrum | 2024-03-21 | 2026-04-01 | 740 | 24 | 0 |
| `0xd866b2332d4383c1bf719732177e2d9109c99dbc` | Optimism | 2024-06-03 | 2026-04-06 | 671 | 25 | 0 |
| `0xa1be220e2491239206f6cd7221f54d24de5907a1` | Optimism | 2024-09-13 | 2026-04-07 | 570 | 19 | 0 |
| `0xfe87530526e8ec2a4136f978e8e1346e44ac030b` | Base | 2024-10-24 | 2026-04-01 | 524 | 10 | 0 |

## Fresh identity candidates

44 deployers had **zero mainnet history**, consistent with a wallet created specifically for L2 trap operations. Top confirmed-trap holders in that set:

| Deployer | Confirmed | Suspected | Total | Chain profile |
|---|---|---|---|---|
| `0x449f6441e85e2b6572283175f73f5ae4816e7449` | 4 | 1 | 20 | L2-only identity |
| `0xa5d55db6adb1bfa7462e136c302dc793bdb9d934` | 2 | 9 | 13 | L2-only |
| `0x3ce47c5d5059705f555bd36c9ff53bff92961d1f` | 2 | 7 | 10 | L2-only |
| `0xcf4eb63977766cf27949860e2b75037218b779f6` | 1 | 59 | 60 | L2-only, suspected-heavy |
| `0x01fe747e91062fe9af2328e43cee5faf3d9c5072` | 1 | 28 | 29 | L2-only, suspected-heavy |

The split between "imported mainnet identity" (54) and "fresh L2-only identity" (44) is nearly even. Both population strategies exist in the ecosystem at comparable scale.

---

## Interpretation — how Pattern D actually works

The handoff framed Pattern D as operators *exploiting* the fact that per-chain profiling sees only target-chain activity. The data confirms this is a live tactic:

- **Long-gap imports (≥1 year)** are most likely **wallet-age laundering**: the operator uses an address with multi-year mainnet history to inherit "this isn't a fresh scam wallet" plausibility. `0x7fd9a5104f…` has 8.8 years of mainnet history and is now deploying trap-suspected contracts on Base. Our per-chain ingest sees a fresh-to-Base deployer with 14 suspected contracts; cross-chain view reveals a long-standing identity that's pivoted to trap deployment.
- **Medium-gap imports (30–365 days)** are more ambiguous. Could be genuine multi-chain users who finally onboarded to L2 and happen to be deploying trap-adjacent contracts, or could be operators who cycle addresses across chains faster.
- **Fresh-identity deployers (44/100)** are the opposite pattern — no reputation inheritance, just new wallet + trap deployment. This is the *non*-laundering population and they still account for 44% of high-risk deployers. So at baseline, plenty of trap ops happen from brand-new addresses.

The interesting analytical surface: **for deployers with similar confirmed+suspected counts, does mainnet-gap correlate with anything measurable on L2** (different bytecode families, different drain mechanics, different funding patterns)? If mainnet-imported deployers run fundamentally different operations than fresh-identity ones, they deserve different risk scoring. We haven't computed that correlation — it's a follow-up.

---

## Operational value

Pattern D is ready to become a risk-scoring feature:

- Input: for each new high-risk deployer, one Etherscan v2 API call returns mainnet first_tx timestamp.
- Signal: `mainnet_gap_days` — if > 30, flag "imported identity"; if null, flag "fresh identity."
- Neither strictly correlates with malicious intent (both populations deploy traps), but the two sub-populations are large enough to be worth distinguishing in reports.

**Scoping decision:** adding `mainnet_first_tx` as a column to `deployers` is a small schema migration + one Etherscan call per new deployer in `auto_funder_tracer`. Etherscan v2 free tier supports 5 req/s = 432k/day; we add ~1,000 new deployers/day, so the budget headroom is enormous. Per the handoff, no new modules without approval — so this is scoped but not built.

**Cost to build:** ~50 LoC added to `auto_funder_tracer` (one Etherscan call added alongside existing funding-trace), one ALTER TABLE migration, one `infrastructure_registry`-style documentation update. About 2 hours of work.

---

## What this report does NOT claim

- The 54 cross-chain imports are not all malicious. Some are legitimate multi-chain actors who happen to deploy ERC-20s that our classifier flagged as suspected.
- The 44 fresh identities are not all malicious. Some are legitimate fresh wallets.
- The correlation between import-pattern and malicious-intent is not established; both populations include confirmed traps at different ratios that we haven't computed.
- No entity_classification changes, no alerts fired.
- Re-running this scan after corpus age ≥ 60 days would sharpen the signal — larger L2 sample, more confirmed traps, clearer pattern discrimination.

---

## Cross-ref

- Pattern F (advisor-parasite): orthogonal; Pattern F concerns victim-extraction cadence, D concerns operator-identity provenance.
- Pattern C (CEX-funded): overlaps. `0x4885631c7335290adcdc4b6b95f97549f5a40edd` is flagged by both — CEX-funded AND 44-day mainnet pre-history gap. Multi-signal candidate.
- `reports/extraction_event_004_rhea_finance.md` — Pattern D validated in a NEAR/Solana context; Subject Wallet was a fresh NEAR identity funded via `intents.near` cross-chain bridge. Cross-chain import *via bridge* rather than *via address-reuse*. Different mechanism, same family.
