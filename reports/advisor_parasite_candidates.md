# Advisor-Parasite Pattern Scan — Candidates Report

**Date:** 2026-04-18
**Scope:** One-shot investigation. Query the corpus for hub-and-spoke approval patterns with temporal signatures that distinguish **advisor-parasite** (slow extraction over months, victims retain balance) from **phishing drainer** (one-shot sweep, victims go to zero).
**Epistemic:** all findings below are Tier B (inferential); the core answer is negative — *no confirmed advisor-parasite candidates in the current corpus*.

---

## Honest top-line finding

**We cannot confirm an advisor-parasite in our 30-day corpus from approval data alone.** The 16 high-diversity approval spenders that match the basic hub-and-spoke shape are almost entirely legitimate DeFi infrastructure (routers, aggregators, bridges). The advisor-parasite signature requires data we don't currently index.

Why the scan is negative:

1. **Corpus age.** Advisor-parasite extraction runs for months. Our ingest started 2026-03-17 (~30 days). Any "advisor" pattern in the data is time-compressed to multi-week — indistinguishable from normal protocol traffic.
2. **Retention metric doesn't discriminate at our scale.** The X402_AGENT_DRAIN victim set is 128 addresses total. The 16 candidate spenders each have 50–1,933 unique approvers. Statistical overlap is tiny regardless of whether a spender is an advisor-parasite or a router — all candidates return `retention_rate = 1.000`.
3. **Our `contracts` table is trap-biased.** We only deeply profile bytecode that looks trap-adjacent at deploy time. Legitimate advisor-parasite contracts (or legitimate protocol contracts) don't have trap signatures, so they're absent from `contracts`. We see them only via `approval_events.spender`.
4. **No Transfer-event indexing.** The advisor-parasite fingerprint requires showing victims make *regular small outbound transfers* to the hub over time. We index approvals to flagged contracts and transactions *with* our monitored contracts, not general ERC-20 Transfer flows.

---

## What the scan found (candidates + disposition)

Query: spenders with ≥50 unique approvers over ≥14-day window in `approval_events`, excluding known infrastructure and classified rogue drainers.

| Score | Spender | Approvers | Days | Chain(s) | Disposition |
|---|---|---|---|---|---|
| 133 | `0x57df6092…114e` | 892 | 19.6 | Base | Likely router/DEX (high per-user approval counts) |
| 116 | `0x4752ba5d…ad24` | 1933 | 15.3 | Base (+6 Arb) | **Almost certainly Base Uniswap Universal Router** — top approvers have 72–82 approvals each in 16 days = ~5/day = heavy swap traffic |
| 106 | `0xccc88a9d…315be` | 259 | 19.1 | Base (+Arb) | Medium-traffic protocol; per-user approval counts don't fit advisor-parasite |
| 105 | `0x11111112…2a65` | 246 | 19.1 | Base | **1inch Router v6** (canonical `0x1inch…` vanity) |
| 105 | `0x00000000…2734` | 315 | 18.2 | Base | Near-null vanity prefix → public infra pattern |
| 91 | `0xd8ba9d1a…a4e2` | 127 | 18.8 | Base | One approver has 120 approvals in a single day — script-driven, not advisor |
| 89 | `0x9dda6ef3…e8e6` | 210 | 16.6 | Base | Long tail, small per-user counts — looks like a protocol |
| 86 | `0x6131b5fa…37b5` | 123 | 17.9 | Base | Not identified; no notable signal |
| 80 | `0xec3576c5…06cd` | 193 | 15.2 | Base | Not identified |
| 79 | `0xac4c6e21…0b75` | 88 | 17.7 | Base | Not identified |
| 78 | `0x91a65ef6…168c` | 61 | 19.0 | Base | **Already CONFIRMED trap in `contracts`** — caught by behavioral trigger. Not advisor; it's a honeypot. |
| 78 | `0x1231deb6…4eae` | 63 | 18.8 | Base | **LI.FI Diamond** — cross-chain bridge aggregator |
| 78 | `0x337685fd…c3e2` | 93 | 17.1 | Base | Not identified |
| 75 | `0xb3000000…028d` | 51 | 19.2 | Base | Vanity prefix → public protocol |
| 73 | `0x07964f13…0000` | 61 | 17.8 | Base | Trailing-zeros vanity → public protocol |
| 66 | `0x1b02da8c…7506` | 101 | 14.2 | Base | Not identified |

**Six candidates I can't map to known infrastructure by name**: `0x57df6092…`, `0xccc88a9d…`, `0xd8ba9d1a…`, `0x9dda6ef3…`, `0x6131b5fa…`, `0xec3576c5…`, `0xac4c6e21…`, `0x337685fd…`, `0x1b02da8c…`. All concentrated on Base. Only `0x91a65ef6…` is already flagged (confirmed trap — different class entirely).

**None of them behave like advisor-parasites.** The per-user approval counts are either:
- Very high (70+ per user → power-DeFi-user hitting a router repeatedly), or
- Very low with moderate diversity (2–4 per user → users interacting with a protocol occasionally, like a niche swap venue)

Neither matches the advisor pattern, which would be **steady moderate per-user approval cadence** (say 1–3 approvals per user per month, consistently, across many users) paired with **ongoing balance** in the victim wallet.

---

## What advisor-parasite would actually look like in our data

Revised fingerprint, informed by what we can and can't see:

**Observable (current schema):**
1. Spender with 50–300 unique approvers (too small = niche phishing; too many = public protocol)
2. Approvers contribute 1–5 approvals each over weeks (not 80+, not 1)
3. Approvers are NOT in drain victim set (retention = 1.0) — but this is weak given our small drain-victim count
4. Spender is a contract NOT in `contracts` table (bytecode didn't trigger trap classifier at deploy time → pre-corpus or benign-looking)
5. Chain concentration on one chain (advisor community is usually one ecosystem)

**Not observable without new indexing:**
6. Outbound transfers from approvers to spender *beyond the approval event itself* — the actual small extractions
7. Approver account-age: were these wallets new-to-crypto when they approved? Advisor-fraud targets less-experienced users.
8. Affinity signals: shared funding source (CEX deposit from same origin), similar gas price cohort, similar tx timing clusters.

**The six unknown candidates above fit the OBSERVABLE profile weakly.** Without the additional signals (especially #6 — actual outbound extraction flows from approver to spender), I cannot promote any of them to "suspected advisor-parasite." Their structural shape matches the hypothesis *and* matches "niche DeFi protocol we haven't labeled." The hypothesis is not falsified; it's unprovable with the current data.

---

## What it would take to actually detect this

Three work items, ordered by leverage:

1. **Outbound Transfer-event indexing for approvers of candidate spenders** — build a narrow ERC-20 Transfer event indexer scoped to the top-50 approval spenders' approver cohorts. For each approver, track outbound ERC-20 flows to the spender (or to addresses downstream of the spender). Advisor-parasite shows: small, regular, cumulative outflow over time. Phishing shows: nothing, then full sweep. Legitimate protocol use: irregular, tied to swap events.
   - Cost: moderate — new indexer module, ~200 LoC, runs from existing WebSocket. Scoped to a few hundred addresses = low volume.
   - Blocks on: your approval to scope the new module (per Part 2 discipline in the behavioral-laundering handoff: no new modules without explicit approval).

2. **Approver account-age enrichment** — one-time `eth_getTransactionCount(addr, 0)` lookup for each approver against the earliest mainnet block where they appear. Distinguishes "first-time crypto user who just funded from Coinbase" (classic advisor victim profile) from "longtime DeFi user who swaps regularly" (legitimate user of a niche protocol).
   - Cost: 1 RPC call per approver; for the top 16 spenders' ~5,000 total approvers that's 5,000 calls. Over the 200-call Alchemy budget. Would need separate approval.

3. **Corpus time extension** — run for another 60–90 days before re-scanning. Advisor-parasite requires the patience that only time exposes. No work today; just don't close the hypothesis.

---

## Cross-ref to existing drainer operations

None of today's drain facilitators (CE5E, A7B9, E3B2, E717, D270) match the advisor-parasite hypothesis. Confirmed:

- **CE5E today:** 67 unique victims over 6.8 days, all drained to zero balance. Each victim = one approval + one sweep. No per-victim-retention.
- **A7B9:** similar pattern on Base.
- **The pattern is "one-shot phishing drain via approval,"** not "extended trust relationship with many small extractions."

This is useful as confirmation: **the handoff's framing — that some "drainers" might actually be advisor-parasites — is not supported by our current data.** The drainers we've identified are operating the classical one-shot phishing pattern, not the advisor model.

This is not the same as saying advisor-parasites don't exist in the ecosystem. It's saying: **they're not the 7 rogue facilitators we've profiled.** If advisor-parasite operators exist, they're a separate population, and our current ingest doesn't surface them because their contracts look benign at deploy time and their extraction rhythm is too slow for our 30-day window.

---

## What this file does NOT claim

- No spender address is labeled as advisor-parasite. Six unknowns flagged for follow-up; none promoted.
- No new `entity_classification` rows written.
- No alerts fired for any candidate.
- No ALTER TABLE, no new module, no schema changes.
- No criminal attribution. The ecosystem fact that "advisor-parasite extraction exists" is not the same as "we've found one."

---

## Recommended next step

Stand down this specific scan until either (a) corpus age reaches 90+ days, or (b) the Transfer-event indexer work item above gets scoped and approved. The hypothesis has been memorialized as **Pattern F** in `reports/behavioral_laundering_detection_scope.md` (2026-04-18) — see that doc for the re-scan trigger conditions and full detection-gap analysis alongside Patterns A–E.
