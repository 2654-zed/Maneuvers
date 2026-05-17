# Layer 3 Corrections Log

A living record of claims made, errors found, and how they were fixed. Every entry includes discovery date, discovery method, what was wrong, what was actually true, and the commit or report where the fix landed.

**Purpose:** Make the project defensible under scrutiny. Customers and reviewers can reconstruct "what did Layer 3 claim on date X and was it true?" by reading this file chronologically.

**Format for each entry:**
```
## [YYYY-MM-DD] Short title
- **Claim:** what was asserted
- **Reality:** what the data actually shows
- **Discovery:** how it was caught
- **Fix:** commit/report where it was corrected
- **Severity:** HIGH / MEDIUM / LOW — impact if a customer had acted on the wrong claim
```

---

## Quick Retirement Index

**Do not cite any of the following as live. See the dated entry below for the corrected form and methodology context.**

| Retired claim | Retired on | Use instead | Detailed entry |
|---|---|---|---|
| Trust amplification factor 14.2× (`0xd4624228`) | 2026-04-02 | `router_percentage` and per-contract `amplification_factor` from current `trust_amplification` table. The 14.2× multiplier specifically was computed against the `T2-eaef6a5d` family baseline that Correction #3 dissolved; not currently reproducible. The 2,910 victims and 96.6–98.7% router-delivered traffic remain Tier A. | "Trust amplification factor of 14.2x" (2026-04-02); lexicon Trust Amplification Factor entry methodological caveat (2026-04-25); Correction #17 |
| org_001 has 899 deployers and 2,042 contracts | 2026-04-02 | 308 deployers / 1,856 contracts via `funding_chain` method, with explicit `methodology_note` on which attribution method is used. Conservative count via `entity_classification` is 16/462. Always state the method. | "org_001 has 899 deployers and 2,042 contracts" (2026-04-02) |
| GoPlus detects 0 of top 50 | 2026-04-02 | 50 GoPlus results now stored in `goplus_results`. Reframe as L3_ONLY match counts (contracts Layer 3 catches that GoPlus did not flag or did not have data on). Do not use "100% detection gap" wording. | "GoPlus detects 0 of the top 50 contracts" (2026-04-02) |
| Camouflage ratio 68% | 2026-04-02 | 70–79% range, stable across chains and time windows. Recompute from `transaction_events` for the citation date — do not pull from the older `camouflage_metrics` table. | "Camouflage ratio 68%" (2026-04-02) |
| 832 wallet rotations / 302 high-confidence | 2026-04-02 | 274 with temporal succession filter (similarity ≥ 0.85 AND one deployer's `last_seen` < other's `first_seen`). State the criteria. | "832 wallet rotations, 302 high-confidence" (2026-04-02) |
| 49 victim-to-predator conversions | 2026-04-02 | 2 with strict 24h filter. Narrative effectively collapsed — do not use "victim-to-predator pipeline" as a corpus-supported claim without explicit Tier B framing and the corrected count. | "49 victim-to-predator conversions" (2026-04-02) |
| Anti-forensic implementation destruction behind `0x08b8b941` proxy slot 1 | 2026-04-05 | `0x93614117…` is an EOA (nonce > 0, actively transacting on Aave V3 / Uniswap V3 / ParaSwap). Not a destroyed contract. Closed-loop infrastructure ecosystem is confirmed; evidence of extraction is inconclusive. | "Destroyed Implementation → EOA" (2026-04-05) |
| Coffee fleet size 55 | 2026-04-08 | 56 (production). Local DB had stale 209 superset. Case file rewrite pending. | "Coffee fleet size 55" entry in summary table (2026-04-08) |
| 0x785ce546 is a $256K victim of E3B2 | 2026-04-13 | Controlled intermediary funded by E717 with 1,406 ETH, distributing $9.8M to address-poisoning collectors. Not a victim. | "0x785c: $256K victim of E3B2" entry in summary table (2026-04-13) |
| 6 rogue facilitators | 2026-04-13 | 7 confirmed: CE5E, E717, A7B9, E3B2, D270, 881E, F71C. | "6 rogue facilitators" entry in summary table (2026-04-13) |
| $3.9M drain volume | 2026-04-15 | ~$2.3M real victim extraction + ~$1.6M pass-through laundering. 42% of top-value events are drainer cycling own funds through compromised wallets. Real pass-through fraction likely higher than 42% (see 2026-04-16 follow-up). | "$3.9M drain volume" entry in summary table (2026-04-15) |
| $3.1 quadrillion OP drain (DRAINER-D270) | 2026-04-12 | Token decimals normalization bug: amount divided by 10^6 (USDC default) instead of 10^18 (OP). Real drain ~3,100 OP (~$4,650–$6,200). Alert pipeline's token decimals lookup needs generalizing — not yet patched. | "Token Decimals Normalization Bug — OP Drain Amount Off by 10^12" (2026-04-12) |
| "Anti-forensic confirmed" / "infrastructure-layer extraction confirmed" | 2026-04-05 | "Architecturally valid, unconfirmed." Do not use "confirmed" wording for the infrastructure-layer extraction hypothesis. | "Destroyed Implementation → EOA" (2026-04-05); summary table entry |
| "Pipeline is down" (2026-04-07) | 2026-04-08 | Pipeline was healthy. Local DB was stale. Fixed via sync 2026-04-07. | Summary table entry |
| 4,015 stale deployer counts (2026-04-07) | 2026-04-08 | Local artifact only. Production had 3 stale, all -1 deltas. Corrected via `railway ssh refresh`. | Summary table entry |

**Propagation watch-list (cleanup pending):**

Retired claims that the audit has identified as still appearing in downstream files. These do not change the retirement — they are cleanup tasks. Do not cite the retired form from any of these locations.

| Retired claim | Still appears in | Required cleanup |
|---|---|---|
| 14.2× trust amplification | `docs/lexicon.md` line ~943 (Bug-Bounty Structural Gap empirical grounding); two case files: `PARASITE_ARCHITECTURE_0xd4624228.md` and `TRUST_LAYER_EXPLOITATION_20260324.md`; deck `Layer3_Intelligence_Platform_1.pptx` slide 5 | Rewrite each citation to use `router_percentage` + `amplification_factor` per the lexicon's Trust Amplification Factor entry methodological caveat. Surface the Cantina rejection quote separately from the multiplier figure. |
| Bot anchor `0x84792c2a` (Tuition Extraction Markets lexicon entry) | `docs/lexicon.md` Tuition Extraction Markets entry | Bot has zero corpus entries per Epistemic Test #2 A12. Either re-source the anchor or relabel the entry to remove the specific address. |
| "Cross-Domain Compositional Harm" lexicon entry empirical grounding | `docs/lexicon.md` | Vercel and Bancor case files referenced do not exist. Either create the case files or revise the entry to cite conversation-level evidence with explicit framing. |

---

## How to use this index

**At session start:** scan the Retired Claim column and the Use Instead column. Note any item your task is likely to touch.

**Before citing any number:** check if the number, its anchor (an address role, a percentage, a count), or its named claim appears in the retired list. If yes, use the corrected form and do not cite the retired form — even if it appears in a non-CORRECTIONS file.

**When adding a new retirement:**

1. Append the full dated entry to the body of CORRECTIONS.md (existing format).
2. Add a row to the Quick Retirement Index table above.
3. If the retired claim is known to appear in downstream files (lexicon, case files, decks, INDEX.md), add a row to the Propagation watch-list.
4. Update the relevant lexicon entry if the retirement changes a definition or methodological grounding.
5. Add a numbered entry to `reports/correction_log.md` if the retirement is also a methodology correction.

**Authority:** This index is supreme over any other file containing the same claim. If lexicon, INDEX.md, a case file, a deck, or claude.md cites a retired claim as live, the file is wrong — not this index.

---

## 2026-04-02 Epistemic Integrity Audit — 6 Corrections

### "GoPlus detects 0 of the top 50 contracts"
- **Claim:** 100% detection gap vs GoPlus across 50 contracts
- **Reality:** GoPlus API was unreachable during testing (TLS SSL error). The "0/50" figure was from a prior session that never successfully queried GoPlus. At audit time, there was no GoPlus data in the database.
- **Discovery:** Section A1 of epistemic integrity test. Searched all 54 tables for GoPlus data, found none.
- **Fix:** Removed GoPlus claims from API responses. Added TODO to rerun benchmark when API accessible. Later discovered `goplus_results` table DID contain 50 prior benchmark results — now exposed in `/risk` endpoint as of commit 14bc4f8.
- **Severity:** HIGH — this was a central pitch claim with no verifiable backing.

### "org_001 has 899 deployers and 2,042 contracts"
- **Claim:** Specific headcount for org_001
- **Reality:** Actual numbers depend entirely on attribution method. `entity_classification`: 16 deployers / 462 contracts. `deployer_profiles.org_link`: 26 deployers. `funding_trail` JSON: 308 deployers / 1,856 contracts. Union of all methods: 324 deployers / 1,875 contracts. The "899" figure matched no clean query.
- **Discovery:** Section A2 of epistemic test. Ran three independent counts and compared.
- **Fix:** `/org/{org_id}` endpoint now returns `attribution_method: "funding_chain"` and a `methodology_note` showing the conservative count alongside. Commit d3ee103.
- **Severity:** HIGH — numbers were off by up to 20x depending on method.

### "Trust amplification factor of 14.2x"
- **Claim:** Router parasite operates at 14.2x the normal bytecode family rate
- **Reality:** No trust amplification table existed in the DB at audit time. The number came from an ad-hoc analysis that was never persisted. *Later update:* the table now has 32 rows with real data, including the `0xd4624228` parasite at router_percentage=96.6%. The original "14.2x" still cannot be reproduced from stored data.
- **Discovery:** Section C2 of epistemic test.
- **Fix:** Removed from API responses. Now re-exposed with verified fields (`total_callers`, `router_percentage`, `amplification_factor`) from the populated table. Commits d3ee103 (remove) and 14bc4f8 (re-add with real data).
- **Severity:** HIGH — key pitch number with no backing.

### "Camouflage ratio 68%"
- **Claim:** 68% of active contracts have <10% revert rate
- **Reality:** Actual ratio is 79.2% (computed fresh from transaction_events on contracts with 10+ interactions). Off by 11 percentage points.
- **Discovery:** Section A3 of epistemic test. Recomputed from raw data.
- **Fix:** API `/ecosystem/stats` now computes live from `transaction_events` instead of reading stale `camouflage_metrics` table. Commit d3ee103. The "stable across chains/weeks" claim still holds — spread is <15pp.
- **Severity:** MEDIUM — directionally correct, magnitude wrong.

### "832 wallet rotations, 302 high-confidence"
- **Claim:** 832 rotations detected, 302 high-confidence
- **Reality:** `deployer_similarity` has 4,879 pairs total. Thresholds produce 4,879 (≥0.70), 1,236 (≥0.80), 348 (≥0.85), 27 (≥0.90). None match "832" or "302" cleanly. With the temporal succession filter (≥0.85 AND one deployer's last_seen < other's first_seen), the count is **274**.
- **Discovery:** Section A4 of epistemic test.
- **Fix:** API `/ecosystem/stats` now reports 274 with explicit criteria: `rotation_criteria: "similarity >= 0.85 with temporal succession"`. Commit d3ee103.
- **Severity:** MEDIUM — wrong number but the underlying capability is real.

### "49 victim-to-predator conversions"
- **Claim:** 49 addresses were trap victims before becoming trap deployers
- **Reality:** The original query found 84 addresses that appear in both `transaction_events` (as reverted caller) AND `deployers` table. With a 24-hour filter requiring the first revert to precede first deployment by at least a day (to exclude operators who got reverted while probing), the count drops to **2**. Most of the original 84 were deployer-first operators, not victims-turned-predators.
- **Discovery:** Section A5 of epistemic test. Re-ran with stricter temporal filter.
- **Fix:** Number removed from external materials. The victim-to-predator narrative is essentially dead with the corrected filter.
- **Severity:** MEDIUM — narrative collapsed from "49 confirmed" to "2 with strict filter".

---

## 2026-04-05 Destroyed Implementation → EOA

- **Claim:** `0x93614117...` stored in `0x08b8b941`'s proxy slot 1 was a self-destructed implementation contract, indicating anti-forensic behavior. This was flagged as the "strongest evidence of anti-forensic behavior in our corpus" and as a potential infrastructure-layer extraction confirmation.
- **Reality:** `0x93614117...` is an EOA (externally owned account), not a destroyed contract. It has nonce > 0, is actively transacting on Aave V3, Uniswap V3, and ParaSwap. Zero bytes from `get_code` is normal for an EOA — not evidence of SELFDESTRUCT.
- **Discovery:** Blockscout API returned `is_contract: false`. Confirmed by checking the address's current transaction activity — actively doing DeFi operations from March 31 to April 5.
- **Fix:** Proxy watcher updated (commit a259755) to check nonce > 0 before flagging zero-code address as destroyed. Infrastructure layer report corrected to note: "Initial analysis flagged a potential anti-forensic implementation destruction. Verification revealed the address is an EOA, not a destroyed contract. The closed-loop infrastructure ecosystem is confirmed but evidence of extraction is inconclusive."
- **Severity:** HIGH — the wrong interpretation was used to support an infrastructure-layer extraction hypothesis. Correction prevents false "anti-forensic" confirmations in future proxy checks.

## 2026-04-05 Drain TX Hashes Don't Match On-Chain Events

- **Claim:** We can recover dollar values from the 963 documented drain events by fetching transaction receipts and parsing Transfer event logs.
- **Reality:** The drain transactions call a custom function (`e37136db`, unknown ASCII) that emits **zero log events**. Successful transactions with empty logs mean the extraction mechanism doesn't use standard ERC-20 Transfer events. Receipt parsing finds nothing.
- **Discovery:** Built drain_value_scanner.py, ran it on 500 drain receipts, found 0 transfer events. Debugged by fetching individual receipts and inspecting logs directly.
- **Fix:** Pivoted to checking current balances on trap contracts and their deployers. Result: ~$194 total across top 20 drain contracts. Most extracted value has already been moved out via the laundry pipeline. True drain amounts require `debug_traceTransaction` (trace-enabled RPC, not available).
- **Severity:** MEDIUM — the "we can value drains" claim was wrong, but we now know the extraction mechanism is invisible at the event log level. This is itself a finding about the anti-forensic design of these traps.

## 2026-04-05 Infrastructure-Layer Extraction Hypothesis Deflated

- **Claim:** `0x08b8b941` is an infrastructure operator extracting value from its own funded deployers, confirmed via the destroyed implementation and post-deployment callback pattern.
- **Reality:** The "destroyed implementation" was an EOA. Broader search across the corpus found **zero additional closed-loop operators**. The pattern (fund deployers + deploy service contracts + receive callbacks from funded deployers) is unique to this one address and the evidence of extraction is inconclusive. The funded deployers call the hub AFTER deploying (not before), which is suspicious but not diagnostic.
- **Discovery:** Phase 3 broader search ran against all 50 top funders, returned zero additional matches. Post-deployment call pattern is explainable as shared infrastructure usage, not necessarily extraction.
- **Fix:** Infrastructure layer report updated with honest assessment: "The infrastructure-layer threat model remains architecturally valid but lacks a confirmed instance in this corpus." Commit a259755.
- **Severity:** MEDIUM — the hypothesis is still valid as a concept but should not be claimed as confirmed.

## 2026-04-04 "Serial Victim Trapped 6x in 15 Minutes" Misread

- **Claim:** Bot `0x5901663c...` was trapped 6 times in 15 minutes across different contracts.
- **Reality:** The bot has 9 total trap events spread across Apr 3-4 (not 15 minutes). The "6 in 15 minutes" mental model conflated separate sessions. Actual pattern: 6 traps in 1 hour on Apr 3 (13:26-14:10), then 3 more traps in 15 minutes on Apr 4 (05:05-05:19). Still notable behavior but initial framing was imprecise.
- **Discovery:** Full timeline dump during April 5 investigation.
- **Fix:** Corrected in April 5 trap analysis. Updated framing to "9 traps across 2 days, clustered in rapid-fire sessions."
- **Severity:** LOW — the underlying observation (bot repeatedly hits traps without learning) holds, just the time window was wrong.

## 2026-04-05 Seven Optimism Trap Fires — Actually Three Chains Active

- **Claim:** "First Optimism trap fire" on April 4.
- **Reality:** Three Optimism trap fires had already occurred: April 3 00:00:29, April 3 10:35:13, April 4 12:34:43. The April 4 was the third, not the first. Missed in the daily summary because earlier detections were pre-sync.
- **Discovery:** Queried all trap events directly from Railway.
- **Fix:** Updated April 5 analysis to note Optimism trapping started April 3.
- **Severity:** LOW — chronology was wrong by a day.

---

## Infrastructure Corrections (Non-Data)

### 2026-03-31 WAL Bloat — 4.5GB Volume Fill
- **Problem:** SQLite WAL file grew unbounded, filling 5GB Railway volume in days.
- **Root cause sequence:**
  1. Initial: per-event commits generated massive WAL traffic. Fixed with batch commits per-block.
  2. Still growing: WAL checkpoint thread couldn't get exclusive access while monitors held connections. Fixed with aggressive PASSIVE checkpoints.
  3. Still growing: PASSIVE only moves pages, doesn't truncate. Fixed with connection cycling (close + reopen to allow TRUNCATE).
  4. Still growing: architectural — SQLite not designed for multi-process writers. Fixed with single-writer architecture (multiprocessing.Queue + dedicated writer process). Commit 0be703e.
- **Result:** WAL now stays under 100MB. DB grows only from real data.

### 2026-04-05 Railway Deploy Failures — Pre-Deploy Command
- **Problem:** Railway deploys failing repeatedly with "no such table: contracts" errors during startup.
- **Root cause:** The Railway agent had added `python -m surveillance.backfill_timelocks` as a pre-deploy command. The backfill script tries to read from the contracts table before the volume is mounted, causing it to fail and block deployment.
- **Fix:** Remove pre-deploy command entirely. Backfill is a one-shot admin script, not a deploy hook.
- **Severity:** HIGH — service was down through multiple deploy cycles.

### 2026-04-05 Multiprocessing Spawn Loop
- **Problem:** After switching from `fork` to `spawn` start method, child processes re-imported `run_surveillance.py` at module level, which re-executed the HTTP server start, DB cleanup, and writer spawn code — causing infinite process creation.
- **Fix:** Reverted to `fork` start method. Linux (Railway) supports fork, which inherits parent memory without re-executing module-level code. The original reason for switching to spawn (fd inheritance) was theoretical and not observed in practice.
- **Severity:** HIGH — crashed Railway deploy loop.

---

## 2026-04-07 Pipeline-Down Misread

- **Claim:** "Surveillance pipeline is down — last heartbeat 2026-04-06 20:23 UTC, ~13 hours stale"
- **Reality:** The Railway production pipeline was healthy and writing the entire time. The local SQLite at `surveillance/data/surveillance.db` was a stale dev checkout that hadn't been synced. The user's logs from Railway showed continuous activity through 2026-04-07 20:39+ that I had no visibility into until I ran `sync_railway_db.py`.
- **Discovery:** User pasted Railway logs showing live monitor activity on the same date my local query said "no rows".
- **Fix:** Ran `sync_railway_db.py` to pull production state. All future analysis sessions should begin with a sync (or query the live `/dump` endpoint directly) before claiming the pipeline is down.
- **Severity:** HIGH — would have triggered an unnecessary "restart Railway" intervention if the user had acted on it.

## 2026-04-07 Coffee Fleet Size Off By 4x

- **Claim:** Coffee fleet `0xc0ffeefeed8b9d27` has fleet size 55 (from `dormant_activations.fleet_size` and `deployers.total_contracts_deployed`)
- **Reality:** The actual contracts table shows **209 contracts** under that deployer. The `deployers.total_contracts_deployed` field is **stale** — it was last updated on 2026-03-30 when the deployer first crossed an alert threshold and hasn't been refreshed since. 60 of the 209 are confirmed (with on-chain victim evidence).
- **Discovery:** Joining `contracts WHERE deployer_address=?` while writing the case file. Counted directly instead of trusting the deployer record's stale field.
- **Fix:** Case file `surveillance/data/cases/CASE_COFFEE_FLEET_0xc0ffeefeed8b.md` documents the correct number. Need a periodic background job to refresh `deployers.total_contracts_deployed` from the contracts table — currently only gets updated at deployer-creation time.
- **Severity:** MEDIUM — under-counted the largest single trap fleet in the corpus by 4x in any report that referenced the deployer record.
- **LATER UPDATE (2026-04-08):** See next entry — the 209 figure itself was a local-only artifact and production actually had ~56 the whole time. The original "55" was essentially correct for production. This entry is kept as-is for audit purposes but is superseded below.

## 2026-04-08 Correction-of-the-Correction: Coffee Fleet Was Never 209

- **Previous claim:** "Coffee fleet actually has 209 contracts, not 55 — the deployers table was stale" (entry dated 2026-04-07, above)
- **Reality:** The 209 count was from the **local** SQLite file, not production. When `surveillance.refresh_deployer_counts` was run against Railway production via `railway ssh`, it reported only **3 stale deployer records** fleet-wide — and those 3 were *-1 deltas* (counts overstated by 1). Production coffee fleet was 55 and is now 56, essentially matching the deployer record. Local contract count for the same deployer was 209, ~3.7x higher than production, because the local DB accumulated contracts from multiple sync sessions across earlier Railway states that have since been pruned or lost in Railway resets.
- **Root cause:** `sync_railway_db.py` uses `INSERT OR REPLACE`/`INSERT OR IGNORE` to pull rows from Railway's `/dump` endpoint. Rows that exist locally but no longer exist on Railway (because Railway was reset at some point, which I know happened at least once during the multiprocessing/spawn debugging period) are never removed from local. So the local DB is a *superset* of production state, not a mirror.
- **Discovery:** Running `refresh_deployer_counts` on Railway via `railway ssh` on 2026-04-08 and seeing only 3 stale records instead of the ~4,015 seen locally. Cross-checked with a direct `SELECT COUNT(*) FROM contracts WHERE deployer_address=?` on production which returned 56.
- **Fix:** Kept the refresh module (it's a cheap safety net that executed in <1s against 17,954 production deployers). Added this correction entry. **The case file `CASE_COFFEE_FLEET_0xc0ffeefeed8b.md` still reflects the 209 number and is wrong for production** — it should be re-written with production data, or explicitly marked as a local-only historical snapshot. For now, noting here: coffee fleet on production is currently ~56 contracts deployed by `0xc0ffeefeed8b9d271445cf5d1d24d74d2ca4235e`, first_block 44019865, last_block 44404815.
- **Severity:** MEDIUM — entire yesterday's case file conclusion ("largest single-deployer trap fleet in the corpus") is potentially invalidated. Production may well have a larger fleet-by-single-deployer than 56; haven't checked. The "all 84 victims are coffee-fleet vanities" finding needs re-verification against production data.
- **Process lesson:** Before writing any case file or correction entry again, verify the data source is production, not the local sync cache. Either sync fresh or query the Railway API directly.

## 2026-04-08 Three Investigation Findings

### INV 1: `0xf30ba13e` is a major CEX hot wallet (L1)

- **Context:** The `withdrawTo` decoder bug fix (commit 5a82c94) revealed that the 2,364 ETH tx from org_001 gas station `0xbefa750ed568cc` on base bridged to L1 recipient `0xf30ba13e4b04ce5dc4d254ae5fa95477800f0eb0` — a cross-recipient withdraw, not same-EOA.
- **Finding:** `0xf30ba13e` on L1 Ethereum is an EOA with nonce **813,076** and current balance **155,492 ETH (~$466M)**. It holds diverse ERC-20 positions (ENJ 16.3M, MTA 1.35M, SHIB 300k, IMX, ANT, INJ, RENDER, USDT) — a custody pattern only consistent with a **centralized exchange hot wallet**. Address-poisoning neighbors (0x9461...0421 variants) confirm it's a well-known target.
- **Implication:** org_001 has **active CEX cashout infrastructure**. The 2,364 ETH withdraw is not a laundering hop — it's a direct deposit to a CEX. First concrete evidence of org_001 funds exiting the monitored ecosystem via centralized exchange on-ramps. This shifts the threat model from "on-chain laundering" to "active off-chain liquidation."
- **Follow-up needed:** Match `0xf30ba13e` against public CEX address databases (Etherscan tags, Arkham, Chainalysis) to identify which exchange.

### INV 2: $90M USDC observability gap closed (partially)

- **Claim:** `0xe69f81b8` had $90M in USDC flow invisible to our trackers.
- **Reality, after deeper trace:** Of the 52 canonical USDC transfers from this EOA, **11 go DIRECTLY to the USDC contract `0x833589fcd6edb6e08f4c7c32d4f71b54bda02913`** (direct `transfer()` calls), and **19/30 sampled go through an intermediary router contract `0x28b5a0e9c621a5badaa536219b3a228c8168cf5d`** that calls USDC internally. The 0x28b5a0e9 router is a 2,175-byte contract of unknown purpose (possibly a CEX deposit contract or aggregator) that uses a non-standard selector `0x8e0250ee`.
- **Fix:** Added ERC-20 calldata scanning to `surveillance/event_monitors.py`:
  - New `ERC20_TOKENS` registry for USDC/WETH/USDT/cbBTC across base/arbitrum/optimism
  - New `_decode_erc20_transfer` helper for `transfer`/`transferFrom` calldata
  - New `_handle_org_erc20_transfer` writer that populates the new `token_contract`/`token_symbol`/`token_value` columns in `org_transfer_events`
  - Idempotent `ALTER TABLE` adds the 3 new columns on existing DBs
  - `process_block` branches to the ERC-20 path when an org wallet calls a registered token contract with a transfer selector
- **Coverage**: This catches direct ERC-20 transfers (~36% of the 0xe69f81b8 USDC flow based on sampling). The remaining ~64% going through router `0x28b5a0e9` requires log-based parsing (fetching tx receipts and parsing Transfer event logs), which is a larger architectural change not included in this fix.
- **Verified:** End-to-end test against a real direct USDC `transfer()` from 0xe69f81b8 decoded the recipient and amount correctly and wrote a populated row to `org_transfer_events`.
- **Severity:** MEDIUM — half the problem is solved; full coverage needs log scanning.

### INV 3: `0x51c72848` MEV bot — $682M operational capital, 227k ETH throughput

- **Context:** This address was previously assumed to be a laundering sink. Yesterday's trace showed it's actually a 23KB-bytecode **contract** running ERC-20 trading with zero direct ETH outflow.
- **Full inbound picture (all time):** 227,341 ETH received from 13 unique sources. Top funders:
  - `0x3304e22ddaa22bcdc5fca2269b418046ae7b566a`: 181,679 ETH across 361 events (org_001 primary gas station)
  - `0x26b610a059de2488ebe3e0eda02ae17907917419`: 20,366 ETH across 37 events
  - `0xcf748f1bd1e2a1e2a1cef35a480acfd5220c9e7d`: 8,600 ETH
  - `0xbefa750ed568cc84970eb4fd506af4ff599c42d0`: 6,005 ETH (the same address that bridged 2,364 ETH to the CEX hot wallet)
- **Current balance:** 0.0000 ETH — contract is exhausted after each trading cycle
- **Total operational capital moved:** ~$682M at $3k/ETH
- **Outflow concentration on ZORA:** 692,522 ZORA across 21 outbound transfers, but **68.6% goes to a single recipient `0xedc625b74537ee3a10874f53d170e9c17a906b9c`** (475k ZORA, 8 txs) and **21.4% to `0x3f53f1fd5b7723ddf38d93a584d280b9b94c3111`** (148k ZORA, 7 txs). 90% of ZORA flow → 2 addresses. Extremely concentrated — these are likely specific DEX pools or aggregator contracts used as arb endpoints.
- **AIXBT even more concentrated:** only 2 recipients total, 63/37 split.
- **USDC/cbBTC distributed:** 20+ recipients each, smaller per-recipient amounts, consistent with DEX swap counterparties.
- **Interpretation:** Multi-venue arb bot with per-token strategies. ZORA and AIXBT have dedicated pool targets (likely single-venue arb), while USDC/cbBTC are traded across many venues (multi-DEX routing). Updated the `0x51c72848` entry in working notes: not a sink, a trading contract. org_001 is clearly running an active MEV operation as part of its infrastructure, not just on-chain laundering.
- **Severity note:** This is a reclassification, not an error. No CORRECTIONS.md-tracked claim was broken — the `0x51c72848` description was first published in an analysis report on 2026-04-07 and updated here on 2026-04-08 as more data came in.

## 2026-04-09 Two Permit2 "Self-Settlements" Were Confirmed Drains

- **Earlier claim (Phase 4 final report, 2026-04-09):** "2 Permit2 transferFrom events where facilitator is also payee — could be legitimate batch-settlement or a drain, inconclusive."
- **Reality:** Forensic investigation confirmed both events and 4 more are **confirmed stablecoin drains** by 4 rogue facilitator EOAs. None of the 4 are in `facilitators.x402.watch`. All spot-checked victims have unlimited never-expiring Permit2 allowances (`amount=MAX_UINT160, expiration=MAX_UINT48`) and zero current token balance.
- **Discovery:** Read `Permit2.allowance(owner, token, spender)` directly via eth_call on both chains for each sender, then measured total stablecoin inflow per facilitator via alchemy_getAssetTransfers.
- **Scale:** 4 rogue facilitators, **$3,885,831 in USD stablecoin inflows** across **1,955 distinct senders** in recent 1000-tx windows per facilitator. Individual victim losses up to **$256,321** confirmed. Lifetime total is larger because RPC queries are capped at 1000 events each; A7B9 and E717 have nonces 96k and 80k respectively indicating weeks of operation at industrial scale.
- **Fix applied to production:**
  - Reclassified the 4 drainers as `classification='rogue'` in `x402_facilitators`
  - Inserted 6 `X402_AGENT_DRAIN` alerts for the monitor-captured Permit2.transferFrom events (previously they only fired the weaker `X402_FACILITATOR_UNKNOWN` alert)
  - Created `surveillance/data/cases/CASE_X402_DRAINER_OPERATION.md` documenting the full forensic trail
- **Detector gap (logged, not yet fixed):** `X402_AGENT_DRAIN` fires only when the payer is in `x402_permit2_exposure`, which is scoped to Permit2 approvals on trap tokens. These 6 drains targeted canonical USDC/USDT, not trap tokens, so the payers were never tracked and the drain alert never fired live. The fix is to widen the drain trigger to include any Permit2.transferFrom where facilitator == payee AND amount >= threshold AND post-state balance is zero. Filed as follow-up.
- **Severity:** CRITICAL — the "inconclusive" framing in Phase 4 understated an active multi-million-dollar drain operation that our monitor had captured but failed to classify correctly.

## 2026-04-08 Railway Production Runs

Three maintenance scripts ran successfully against Railway production via `railway ssh`:

1. **`refresh_deployer_counts`** — 17,954 deployers evaluated, 3 stale counts fixed (all -1 deltas), 7 stale last_seen fixed. Production counts were essentially correct.

2. **`backfill_self_loops`** — 67 contracts promoted across 14 unique dual-role operators. Production confirmed tier went from 191 → 258. Top operator `0xc0dec76000f6c2d3` promoted 27 contracts. 67 `BACKFILL: Self-loop` rows now live on production.

3. **Bridge scanner schema migration + live backfill** — `bridge_events` table extended with 5 new columns via the idempotent `ALTER TABLE` block in `_ensure_tables`. Expanded `_org_wallets` set verified at 258 addresses on production (the 19k ETH recipient `0xe69f81b8...` is now in the set). Real-world 19k ETH case backfilled into production via direct `_handle_bridge` call; production `bridge_events` has 1 row with correctly decoded selector, function name, value_eth, L1 recipient, and bridge name, plus 1 corresponding `BRIDGE_WITHDRAWAL` alert at critical level.

EventMonitors live on production as of 2026-04-08 05:18 UTC heartbeat. Bridge scanner is now active and any org-wallet → bridge call ≥10 ETH will auto-populate `bridge_events` and `alerts`.

## 2026-04-07 Self-Loop Trap Operator Was Logged But Never Promoted

- **Claim:** Implicit — that BOT+DEPLOYER warnings logged by the revert detector were sufficient to flag self-deploying trap operators
- **Reality:** The warning was a `logger.warning()` only — no contracts ever got promoted, no entity_type ever changed. `0x0e4c51936a3f74b4` had been hammering its own trap `0x55ab3b8397...` with selector `9aa6e55a` 2,015 times across 7 days (and selector `042ff559` 5,135 times against other targets) and the system kept logging "possible self-deploying trap operator" without acting on it. The trap stayed `suspected` until manually promoted on 2026-04-07.
- **Discovery:** While decoding the heaviest revert source in the live log capture from the user.
- **Fix:** `surveillance/revert_cluster_detector.py` now captures the `to` address of every reverted tx in `process_block`, and `_check_self_loop` queries the contracts table for any addresses the deployer is calling that they themselves deployed. Self-call → automatic promotion to `confirmed` with reason `"Self-loop: deployer X called own contract..."`. Commit `552baab`.
- **Severity:** HIGH — the system had the data and the warning but never closed the loop. There are likely other dual-role addresses still sitting at `suspected` that the new rule will catch on next encounter.

## 2026-04-07 19,000 ETH Trace Coverage Gap (closed via direct block scan)

- **Claim:** Initially "the 18,994 ETH already drained off" without saying where
- **Reality:** The 19k ETH was bridged to Ethereum L1 via the canonical Base bridge `0x4200000000000000000000000000000000000010` in tx `0x675afa1eb19e72ff3b453563a2b270e76d25b727292a331db633e918b2aad720` at block 44386396 (93 blocks / ~3 minutes after arrival). The recipient `0xe69f81b8...` called `withdraw()` (not `withdrawTo`) so the L1 destination is the **same address** on Ethereum mainnet, pending 7-day challenge period for finalization. `org_transfer_events` did not capture this because the bridge call is a direct contract call to a system precompile, not a top-level value transfer pattern that the org_transfer scanner watches.
- **Discovery:** Alchemy `alchemy_getAssetTransfers` returned 0 results for both inbound and outbound (Base support gap). Found the tx via brute-force `eth_getBlockByNumber` scan over blocks 44386300 → 44386450 looking for `tx.from == recipient`.
- **Fix:** Need to add a scanner that watches outbound calls from gas-station-class addresses to the Base/Optimism L2StandardBridge addresses (`0x4200000000000000000000000000000000000010`) and decodes the `withdraw`/`withdrawTo` calldata. Filed as follow-up.
- **Severity:** MEDIUM — we're missing org-level fund movements when the destination is L1 mainnet via the canonical bridge. For org_001 specifically this is a significant blind spot since the largest single tx of 2026-04-07 ($57M+ at $3K/ETH) used this exact path.

## 2026-04-07 Cross-Chain Rotation Misattribution

- **Claim:** "0x09d6f2c4b854 was funded by org_001 across all 3 chains within 90 seconds — cross-chain rotation"
- **Reality:** The deployer `0x09d6f2c4b854c5ec4e552e3754d38973ac83bbdd` only exists on optimism (1 contract). The 3 different `ORG LINK: deployer 0x09d6f2c4b854 funded by 0x8c826f795466 (org_001:gas_station)` log lines weren't 3 separate cross-chain deployments — they were the `auto_funder` running on each chain (base, arbitrum, optimism) and observing the same arbitrum-side funding tx. The funding tx is on arbitrum (block 450105987); the deployer first appears on optimism 8 minutes later. So the EOA *did* cross-chain (funded on arbitrum, deployed on optimism), but it's a single cross-chain hop, not a 3-way fan-out.
- **Discovery:** Looking at the actual deployer record in the synced DB and seeing `chain=optimism` only, then checking `funding_trail` JSON and finding the arbitrum tx.
- **Fix:** Updated investigation report. Real pattern is 1-hop chain rotation, not multi-chain simultaneous deployment. Still a valid Attack 5 instance but smaller in scope than originally reported.
- **Severity:** LOW — direction was right, magnitude was overstated.

## 2026-04-12 org_001 Is Targeted by External Address Poisoners (Not Just a Practitioner)

- **Context:** org_001's own vanity address spoofing was documented on 2026-04-11 as an intelligence-layer anti-forensic capability — they generate look-alike addresses to confuse analysts and monitoring systems.
- **New finding:** Three external address poisoner EOAs are actively targeting org_001's Treasury on Arbitrum. These are **not org_001 infrastructure** — they are third-party attackers using transaction-layer address poisoning (fake token transfers, zero-value ETH spam, dust token spam) to trick org_001 operators into copying the wrong address from transaction history.
- **Addresses:**
  - `0xe93d2a52f549b9726f2914ab4c2ff0f25c6e7f86` — Operator spoof, fake Unicode USDC, nonce=2
  - `0x360ed34d03353bcc229bf4660e9f48a66db9fb32` — Vault spoof #1, zero-value ETH spam, nonce=2,622
  - `0x360ee8653c848ca03172e65f5c95bde66db9fb32` — Vault spoof #2, dust USDC/USDT spam, nonce=4,069
- **Key distinction:** org_001's own vanity spoofing operates at the intelligence layer (targeting analysts/monitoring systems). These external poisoners operate at the transaction layer (targeting org_001's own operators via tx history pollution). Different phenomenon, different actors, different layer.
- **Implication:** org_001 is both a **practitioner** of vanity spoofing and a **target** of address poisoning. The combined poisoner nonce of 6,693 indicates a sustained, automated campaign against org_001 — confirming org_001 is a high-value target recognized by other actors in the ecosystem.
- **Fix:** All 3 addresses added to production watchlist (`/admin/flag-address`) and local watchlist DB. Classified as `address_poisoner_targeting_org_001` — explicitly separated from org_001's own infrastructure. Documented in CASE_ORG_001_INFRASTRUCTURE.md under new "Address Poisoning Attacks Against org_001" section.
- **Severity:** LOW — this is a new finding, not a correction of a prior claim. Logged here because it adds important context to the 2026-04-11 vanity spoofing discovery: the anti-forensic capability discussion should not be conflated with the fact that org_001 is simultaneously a victim of similar (but distinct) techniques from external actors.

---

## 2026-04-11 Vanity-Spoofed Shadow Wallets Discovered in org_001 Infrastructure

- **Claim (implicit):** All wallets with org_001-associated prefixes in the deployers table are genuine org_001 infrastructure — specifically `0x96daa0b8...` (classified as `lp_staging`) and `0x01989c93...` (classified as `cex_deposit`).
- **Reality:** Both addresses are **vanity-spoofed shadow wallets**. They share the first 6-8 hex characters of real org_001 infrastructure wallets but differ in the suffix. This is a deliberate address-generation technique (vanity address mining) to create lookalike addresses that pass casual visual inspection. These two wallets routed ~$2M+ each during the April 8-11 data gap period, exploiting the monitoring blind spot.
- **Reclassification (2026-04-12):** Vanity address spoofing has been reclassified from an "OPSEC technique" to a formal **anti-forensic capability (intelligence layer)** in the diamond model framework. This is the highest counter-intelligence sophistication observed in the corpus. The three-tier anti-forensic model for org_001: transaction layer (custom selector drains evade log-based detection), victim layer (Unicode WETH impersonation evades human token inspection), intelligence layer (vanity address spoofing evades organizational monitoring and chain analysis). Evidence: 7-char prefix matching, proxy contract funding chains, vanity suffix patterns on downstream wallets.
  - `0x96daa0b8a5499ea9323421ed0cda06b345caab73` — mimics LP Staging wallet `0x96daa0e1...` (prefix match `0x96daa0`, suffix diverges)
  - `0x01989c93890aed05a63d179b03424997075b6acf` — mimics CEX Exit wallet (prefix match `0x01989c`, suffix diverges)
- **Discovery:** Data gap investigation on 2026-04-11. During the Apr 8-11 monitoring gap, these addresses showed anomalous volume that did not match the behavioral baseline of the real wallets they impersonate. Suffix comparison against known org_001 wallets confirmed vanity spoofing.
- **Fix:**
  - Both flagged on production watchlist via `/admin/flag-address` with `priority: CRITICAL` and `entity_type: org_001_shadow`
  - Local `entity_classification` updated: subtype reclassified from `lp_staging`/`cex_deposit` to `org_001_shadow_lp_staging`/`org_001_shadow_cex_exit`, confidence upgraded to `CONFIRMED`
  - Local `deployers` table updated: `entity_type` set to `org_001_shadow` with vanity-spoof documentation in `deployment_pattern_notes`
  - Both added to local `watchlist` table at `CRITICAL` priority
- **Severity:** HIGH — these wallets were previously trusted as genuine org_001 infrastructure. Any analysis that routed through or attributed funds to them as legitimate org_001 operations during the data gap was contaminated. The vanity-spoofing technique is now classified as a formal anti-forensic capability at the intelligence layer of the diamond model — the highest counter-intelligence tier observed in the corpus.
- **Anti-forensic capability documented:** Vanity address spoofing — generating addresses with matching 7-character prefixes to impersonate known wallets. This targets organizational monitoring systems and analyst workflows that truncate addresses, not victims or automated tools. Mitigation: future wallet attribution must compare full addresses, not prefix substrings. Watchlist matching should flag any new address sharing a 6+ hex prefix with a known org_001 wallet for manual review.

---

## 2026-04-16 Pass-Through Classifier Blind to EOA Victims — $200K Drain Missed Today

- **Claim (implicit):** The pass-through classifier that shipped 2026-04-15 correctly labels drain events against drainer infrastructure (documented laundering hops) as PASS_THROUGH instead of REAL_DRAIN.
- **Reality:** The classifier misclassified a $200,615 drain against `0x785ce546` (the documented controlled intermediary) as REAL_DRAIN at 2026-04-16 00:16 UTC. Also missed similar prior events against `0xa3a1d7a5` (documented CE5E laundering hop).
- **Discovery:** Production query during Apr 16 data analysis. Filtered drains by amount; the top hit was 0x785c being drained by E3B2 for $200K, labeled `event_class=REAL_DRAIN path=rogue_facilitator_self_settlement`. 0x785c is explicitly in our `_DRAINER_ADDRESSES` hardcoded set — should have been caught.
- **Root cause:** The `_check_deposit_source()` function queried two sources:
  1. `transaction_events WHERE contract_address = payer` — only populates for contracts, not EOAs
  2. `org_transfer_events WHERE to_address = payer` — only populates for org wallets

  The victim in this case (0x785c) is an EOA that isn't an org wallet, so both queries returned empty. The check structurally cannot see EOA-to-EOA drainer deposits without live Alchemy calls. It never checked the simplest case: **is the payer itself in the known drainer set?**
- **Fix (2026-04-16):** `surveillance/x402_monitor.py::_check_deposit_source` now has a three-path check in order of specificity:
  1. Payer is itself in `_DRAINER_ADDRESSES` → `self:<addr>` (catches all documented intermediaries)
  2. Payer matches a drainer vanity prefix → `vanity_prefix:<prefix>` (catches undocumented addresses in the vanity family)
  3. Original deposit-source check (unchanged, still only works for contracts/org wallets)

  Also added `0xa3a1d7a5` to the hardcoded drainer set — it was documented in the Apr 15 audit but only added to `audit_passthrough.py`, not to the monitor.
- **Implication for Apr 15 numbers:** The `~$2.3M real victim extraction / ~$1.6M pass-through` split from 2026-04-15 is likely an **underestimate of pass-through volume** because the live classifier couldn't fire on EOA victims that are actually drainer infrastructure. A full corpus re-audit with the fixed classifier is needed to produce accurate totals.
- **Severity:** HIGH — a documented laundering wallet was presented as a victim of a $200K drain. If this had appeared in a customer feed or law-enforcement brief, the "victim" would have been the drain operator themselves. The same pattern likely occurred dozens of times historically; the Apr 15 audit only sampled the 4 largest events.

---

## 2026-04-15 Drain Volume Inflation: Pass-Through Laundering Counted as Victim Extraction

- **Claim:** The case file documented ~$3.9M in stablecoin drain volume across 1,955 distinct senders, presented as victim extraction. The spot-checked victims table listed $769K (0xa3a1d7a5, CE5E), $256K (0x785ce546, E3B2), $180K (0x303d5773, E717), $29K (0x59f13bc1, A7B9) as the top individual losses.
- **Reality:** Deposit source audit of the 4 highest-value victims shows **42% of the audited volume ($513K of $1.23M) is pass-through laundering, not victim extraction.** The drainer sends its own funds from vanity sinks (0xbec87a77) and other rogue facilitators (0xa7b9) TO the "victim" wallet, then immediately sweeps them via Permit2. The "victim" is a controlled intermediary used as a laundering hop.
  - 0xa3a1d7a5 ($769K): received funds from 0xbec87a77 (CE5E vanity sink) and 0x881e (address poisoner) → **PASS_THROUGH**
  - 0x785ce546 ($256K): received funds from 0xa7b9 (A7B9 rogue facilitator) → **PASS_THROUGH** (already reclassified 2026-04-13)
  - 0x303d5773 ($180K): received from 0xd195e51c (clean, single source, 3 deposits) → **REAL_DRAIN**
  - 0x59f13bc1 ($29K): received from 0x16378049 (clean) → **REAL_DRAIN**
- **Discovery:** Investigation of 0xa3a1d7a54269be09 on 2026-04-15. The wallet received $675K + $94K USDC from CE5E's own vanity sink, then those exact amounts were swept by CE5E via Permit2. The deposit source analysis revealed the pattern.
- **Root cause:** The original methodology counted all Permit2 transferFrom volume per facilitator as "victim drain." It didn't check where the drained tokens came from. The drainer's own infrastructure addresses are in the inbound flow for ~42% of the top-value events. The `distinct senders` metric (1,955) also includes these pass-through wallets alongside real victims.
- **Fix (code):** `surveillance/x402_monitor.py` now classifies every X402_AGENT_DRAIN event as REAL_DRAIN or PASS_THROUGH by checking if the payer received tokens from a known drainer address before being drained. Uses `_DRAINER_ADDRESSES` (15 known addresses) + `_DRAINER_PREFIXES` (8 vanity prefixes) for matching. Committed 2026-04-15.
- **Fix (numbers):** The $3.9M headline needs revision. Based on the 4-victim sample (covering $1.23M of the $3.9M):
  - Real victim extraction: ~58% of audited volume
  - Pass-through laundering: ~42% of audited volume
  - **Estimated real victim extraction: $2.3M** (58% of $3.9M, conservative)
  - **Estimated laundering volume: $1.6M** (42% of $3.9M)
  - The $10-15M combined operation estimate (Permit2 + address poisoning) requires the same split. Full corpus audit is needed.
  - The `distinct senders` count of 1,955 likely includes dozens to hundreds of pass-through intermediaries. Real victim count is lower.
- **Severity:** HIGH — inflated victim extraction numbers by ~42%. If a customer or law enforcement used the $3.9M figure to estimate victim losses, they would be double-counting laundering flow as theft. The real victim theft is substantial (~$2.3M estimated) but the distinction between theft and laundering is legally and operationally material.

---

## 2026-04-13 0x785ce546 Reclassified: "Highest-Value Victim" → Controlled Intermediary

- **Claim:** `0x785ce546ed429559b95895cb4a07874bf8ed329c` was listed as the highest-value drain victim — "$256,321 drained by E3B2" — in the CASE_X402_DRAINER_OPERATION.md spot-checked victims table (opened 2026-04-09). The figure contributed to the $3.9M aggregate and established the upper bound of individual victim exposure.
- **Reality:** `0x785c` is a **controlled intermediary** in the drain operation, not a victim. E717 funded it with 1,406 ETH across 165 transfers. It has nonce 516 and distributed $8.06M in real stablecoins to the primary address-poisoning collector `0x881e7c4c`, plus $1.70M to a secondary collector, plus $30.8M in spoofed Unicode tokens as address-poisoning payloads. The "$256K drain" was an internal fund movement between wallets in the same operation.
- **Discovery:** Deep trace of new rogue facilitator `0x881e7c4c` (nonce 120,983) on 2026-04-13. Following inbound funding to 0x881e led to intermediary `0x785c`, which led back to E717. The funding direction (E717 → 0x785c) is the opposite of what a victim relationship would show.
- **Root cause:** The original spot-check sorted Permit2 transferFrom recipients by inflow volume and assumed top addresses were victims. It verified allowance state (unlimited, never-expiring) and post-drain balance (zero) — both of which matched the victim fingerprint because the operation also uses Permit2 for internal movements and 0x785c had forwarded its balance onward. The check failed to verify: (a) whether the "victim" received ETH from the drainer, (b) whether its nonce indicated operational activity, (c) whether it distributed funds downstream.
- **Fix:** Victim table entry struck through with correction note. Highest confirmed single-victim loss revised from $256K to $179,999 (`0x303d5773`). Full reclassification section added to case file documenting what was claimed, what's true, and why the correction strengthens the finding (reveals dual-vector operation, elevates E717 to financial hub, expands timeline to 22 months).
- **Severity:** HIGH — a controlled intermediary was presented as the worst-hit victim. If a customer or law enforcement had acted on this (e.g., attempting to contact the "victim" for a freeze request), they would have been contacting the operator. The reclassification expands the case from a $6.2M single-vector operation to a $10-15M+ dual-vector operation, so the overall finding is strengthened, not weakened.

---

## 2026-04-13 DELEGATECALL Proxy Honeypots: 21-Day Detection Blind Spot (928 Victims)

- **Claim (implicit):** The surveillance system detects trap contracts in near-real-time. Bytecode classification on day 0, behavioral confirmation within hours/days. Stale data implies coverage we don't have (CLAUDE.md design principle #4).
- **Reality:** 10 contracts in bytecode family T1-2081a9d32218 were deployed on Base on **2026-03-23** (all within a 2-minute window, 19:44–19:46 UTC, by 10 different Sybil deployer wallets). The bytecode classifier correctly flagged them as `suspected` on day 0 for `delegatecall_in_token`. They then sat at `suspected` for **21 days** with zero alerts, zero escalation, while accumulating **928 victims and 2,147+ transactions** — all successful, zero reverts. The first alert fired on **2026-04-13** when the trust amplification heartbeat finally scanned them.
- **Discovery:** Trust amplification batch alert at 17:13:45 UTC on April 13. Investigation revealed the 21-day gap and the architectural blind spot.
- **Root cause — structural, not operational:** The entire confirmation pipeline depends on reverts:
  - Trap confirmation: needs a revert transaction → **blind** (0% revert rate)
  - Self-loop detector: needs deployer calling own contract → **blind** (no self-calls)
  - Revert cluster detector: needs clustered reverts → **blind** (zero reverts)
  - Velocity detector: needs 8+ contracts per deployer → **blind** (10 deployers × 1 contract each)
  - Dormant activation: needs a dormant period → **N/A** (active from day 1)

  The DELEGATECALL proxy design means the trap mechanism isn't in the bytecode we analyze — it's in the implementation contract behind the proxy, which can be swapped at any time. Static bytecode analysis correctly identifies `delegatecall_in_token` but cannot detect `asymmetric_transfer`, `conditional_revert`, or `unusual_fee_structure` because those signatures live in the implementation, not the proxy shell. The 0% revert rate is the camouflage: buys succeed normally, and the sell-block activates later via implementation upgrade.

  The Sybil deployment was specifically structured to evade our detectors: 10 deployers (below velocity threshold of 8 per deployer), identical bytecode (but no cross-deployer family alert), zero self-calls, zero reverts, immediate victim traffic (no dormant phase). Whether this was designed to target Layer 3 specifically or represents general-purpose OPSEC, the effect is the same.

- **Fix (4 code changes, all executed 2026-04-13):**
  1. **Suspected + high traffic auto-escalation** — contracts at `suspected` tier that accumulate 50+ distinct callers now generate a `SUSPECTED_HIGH_TRAFFIC` WARNING alert. Prevents the 21-day silent accumulation.
  2. **Cross-deployer family velocity alert** — when 3+ contracts with identical bytecode are deployed by different deployers within 1 hour, fire a `COORDINATED_DEPLOYMENT` alert regardless of per-deployer count. Catches the 10-deployer Sybil pattern.
  3. **Trust amplification run frequency** — moved from heartbeat-only (every 360 beats / ~6h) to also run on a daily schedule, ensuring new high-traffic contracts are flagged within 24h of crossing the caller threshold.
  4. **DELEGATECALL implementation tracking** — log the current implementation address (storage slot 0 or EIP-1967 slot) at deployment time. Future: alert if implementation changes post-deployment.
- **Severity:** CRITICAL — 928 victims over 21 days with a system that claims near-real-time detection. This is the longest detection gap in the corpus and the only known case where the entire confirmation pipeline was structurally blind to a live trap operation. The bytecode classifier did its job (day 0 suspected), but the gap between "suspected" and "any alert" had no bridge for non-reverting contracts.
- **Process lesson:** "Suspected" is not coverage. A contract can sit at "suspected" forever if it never produces a revert. The system needs an escalation path for suspected contracts that accumulate real traffic — the absence of reverts is itself a signal when combined with high caller count.

---

## Summary of Wrong Numbers Previously Used in External Materials

| Claim | Correct Number | Status |
|-------|---------------|--------|
| "GoPlus detects 0/50" | 50 GoPlus results stored, most L3_ONLY matches. Not "0/50" but an honest gap of "L3 caught, GoPlus didn't check or rated clean" | FIXED in API |
| "org_001: 899 deployers" | 16-324 depending on method; primary funding_chain = 308 | FIXED in API |
| "Trust amplification 14.2x" | Data now exists (32 rows), actual amplification_factor per contract | FIXED in API |
| "Camouflage 68%" | Actual: 79.2% | FIXED in API |
| "832 wallet rotations" | Actual with temporal filter: 274 | FIXED in API |
| "49 victim-to-predator" | Actual with 24h filter: 2 | REMOVED from narrative |
| "Anti-forensic implementation destruction" | It was an EOA | FIXED in report + proxy watcher |
| "Drain dollar exposure = $211K" (parasite event) | Correct for parasite, but NOT total | Available for specific contracts with extraction_event data |
| "Infrastructure-layer extraction confirmed" | Architecturally valid, unconfirmed | FIXED in report |
| "Coffee fleet size 55" | Local: 209. **Production: 56.** Local was stale-sync superset | CORRECTED 2026-04-08, case file needs rewrite |
| "Pipeline is down" (2026-04-07) | Pipeline was healthy; local DB was stale | FIXED via sync 2026-04-07 |
| "4,015 stale deployer counts" (2026-04-07) | Local artifact. Production had 3 stale, all -1 deltas | CORRECTED 2026-04-08 via `railway ssh refresh` |
| "0x785c: $256K victim of E3B2" | Controlled intermediary funded by E717 with 1,406 ETH. Distributes $9.8M to address-poisoning collectors | CORRECTED 2026-04-13 in case file |
| "6 rogue facilitators" | 7 confirmed: CE5E, E717, A7B9, E3B2, D270, 881E, F71C | UPDATED 2026-04-13 |
| "$3.9M drain volume" | ~$2.3M real victim extraction + ~$1.6M pass-through laundering. 42% of top-value events are drainer cycling own funds through compromised wallets | CORRECTED 2026-04-15 |
| "Pass-through classifier is live" | Shipped 2026-04-15 but structurally blind to EOA victims. Fixed 2026-04-16 (self-check + vanity prefix match). Real pass-through % is likely higher than 42% estimate | CORRECTED 2026-04-16 |

---

## 2026-04-12 Token Decimals Normalization Bug — OP Drain Amount Off by 10^12

- **Claim:** Alert pipeline reported DRAINER-D270 (`0xd27047fe310178316b3acc4746e2a30823bb9186`) on Optimism drained ~$3.1 quadrillion in OP tokens via Permit2.
- **Reality:** The alert normalized the raw token amount using 6 decimals (USDC default), but OP is an 18-decimal token. Dividing by 10^6 instead of 10^18 inflated the display value by 10^12. The actual drain was ~3,100 OP (~$4,650-$6,200 at current OP prices).
- **Discovery:** Manual review of the D270 drain alert during facilitator classification on 2026-04-12. The quadrillion-dollar figure was immediately implausible.
- **Fix:** Corrected amount logged in CASE_X402_DRAINER_OPERATION.md. The alert pipeline's token decimals lookup needs to be generalized beyond the stablecoin assumption (6 decimals) to query actual token decimals on-chain or from a registry. Not yet patched in code.
- **Severity:** HIGH — a customer receiving a $3.1Q alert would either (a) lose trust in the system immediately, or (b) fail to act on what is actually a real drain because the number looks like a bug. Both outcomes are bad.

---

## 2026-04-14 0xe69f81b8 Bridge Withdrawal Running Total — 49,000 ETH (~$147M)

- **Context:** `0xe69f81b825d7dc31ee9becef4dbeab5cf30e3abb` was first documented on 2026-04-07 bridging 19,000 ETH to L1 via the canonical Base bridge (see entry "19,000 ETH Trace Coverage Gap" above). On 2026-04-08, its bridge scanner schema migration added it to the `_org_wallets` monitoring set.
- **New finding (2026-04-14):** An additional **30,000 ETH** bridge withdrawal has been observed, bringing the running total to **49,000 ETH (~$147M at $3K/ETH) bridged to L1 in one week (April 7-14)**. Withdrawals are coordinated during western sleep hours (consistent with prior pattern). L1 nonce is now **36,602**.
- **Scale context:** 49,000 ETH in 7 days from a single EOA is an extraordinarily high withdrawal rate. This address is one of the most active L2-to-L1 bridge users in the Base ecosystem.
- **Action:** Flagged on production watchlist via `/admin/flag-address` with `entity_type: high_value_bridge_user`, `priority: HIGH`.
- **Severity:** MEDIUM — this is a tracking update, not a correction. The 19,000 ETH figure from April 7 was accurate at the time; this entry documents continued activity at accelerating pace.

---

## What This Log Does Not Cover

- Claims made in prior sessions that weren't audited
- Numbers in Week 1/Week 2 reports that predate the epistemic test and weren't retroactively corrected in those documents
- Any number from before March 31 where the underlying data has since changed (the corpus grew from ~29K to 102K contracts, most pre-epistemic-test numbers are now stale by definition)

**The epistemic test is a point-in-time audit, not a running verification.** This log should be updated every time a claim is challenged or found wrong, not just during audits.
