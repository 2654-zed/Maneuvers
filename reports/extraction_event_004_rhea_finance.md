# Extraction Event 004 — Rhea Finance (NEAR Protocol)

**Date:** 2026-04-18
**Event date:** 2026-04-16, 08:22–09:42 UTC
**Chain:** NEAR Protocol (OFF our monitored chains — Base/Arbitrum/Optimism)
**Purpose:** Corpus expansion, not correction. Validates compositional harm thesis with a non-EVM case study.
**Status:** Draft INSERT + draft migration. Nothing executed. Paired with `circle_bridge_infrastructure.md` for review.

---

## Schema check outcome

The live `extraction_events` schema:

```sql
CREATE TABLE extraction_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT NOT NULL,
    event_type TEXT NOT NULL,
    observed_at TEXT NOT NULL,
    documented_at TEXT NOT NULL,
    summary TEXT NOT NULL,
    raw_transactions TEXT,
    total_usd_moved REAL,
    nodes_active INTEGER,
    notes TEXT
)
```

**There is no chain column.** Existing rows (EXTRACTION_001, 002, 003) are all on-chain events on our monitored chains (Base/Arb/Optimism/Ethereum-adjacent), and chain information is only mentioned in `summary` / `notes` prose. Every consumer of this table implicitly assumes monitored-chain context.

Inserting Rhea as-is would be **silently incorrect**: a future query like `SELECT SUM(total_usd_moved) FROM extraction_events WHERE observed_at >= '2026-04-01'` would roll up NEAR dollars with L2 dollars without distinction. Per the framework's ground-truth discipline, this is the shape of bug we publish corrections about.

**Proposed migration:** add two columns — `chain` to identify the chain, `monitored_chain` as a boolean flag so existing queries can filter with `WHERE monitored_chain = 1` without breaking. Backfill existing rows with `chain='ethereum_l2_mixed'` + `monitored_chain=1` (the existing three events span our monitored set). Set Rhea to `chain='near'` + `monitored_chain=0`.

---

## Draft migration

Not executed. Follows the existing migration pattern in `db.py` (lines 48–63, 88–113, etc.).

```sql
-- Migration: extraction_events chain tagging
-- Purpose: distinguish events on monitored chains (primary analysis corpus)
-- from off-chain reference events (e.g. Rhea Finance on NEAR) that inform
-- methodology but should not roll up into monitored-chain metrics.

ALTER TABLE extraction_events ADD COLUMN chain TEXT DEFAULT NULL;
ALTER TABLE extraction_events ADD COLUMN monitored_chain INTEGER NOT NULL DEFAULT 1;

-- Backfill existing rows (EXTRACTION_001-003 are all on monitored chains).
-- 'ethereum_l2_mixed' rather than a single chain value because these events
-- involve addresses/flow across multiple L2s; preserves the fact that we
-- didn't encode a specific chain at observation time.
UPDATE extraction_events
   SET chain = 'ethereum_l2_mixed',
       monitored_chain = 1
 WHERE chain IS NULL;

CREATE INDEX IF NOT EXISTS idx_extraction_events_chain
    ON extraction_events(chain, monitored_chain);
```

Migration hook in `db.py`: gate on `"ALTER TABLE"` attempt with try/except for the "duplicate column" error, same shape as the existing per-column migrations in `db.py` around lines 170–185 (`funding_trail`, `entity_type`, `selector_cluster`).

---

## Draft INSERT — EXTRACTION_004

Not executed. Values transcribed from the handoff data block. Every figure either traces to the provided Tier A claims (explicit on-chain evidence cited in the handoff) or is encoded in `notes` as Tier B interpretation.

```sql
INSERT INTO extraction_events (
    event_id, event_type, observed_at, documented_at,
    summary, raw_transactions, total_usd_moved, nodes_active, notes,
    chain, monitored_chain
) VALUES (
    'EXTRACTION_004',
    'oracle_manipulation_lending_exploit',
    '2026-04-16T08:22:00+00:00',
    '2026-04-18T00:00:00+00:00',
    -- summary (Tier A facts only; interpretation goes in notes)
    'Rhea Finance (formerly Burrow Finance) on NEAR Protocol. $18.4M drained 2026-04-16 08:22-09:42 UTC via margin-trading slippage aggregation bug combined with fake-token oracle manipulation. Subject Wallet funded via cross-chain onboarding (intents.near). 423+ implicit accounts used as distribution infrastructure. 55 intermediary accounts deleted across 3 coordinated waves with Subject Wallet as sole beneficiary. ~45% recovery: $3.29M USDT frozen by Tether in attacker wallet + $1.05M USDT frozen in NEAR Intents + $3.36M USDC + $1.56M NEAR voluntarily returned ($8.26M total). Attack tx: 44tWhQmmkTJgchgFVkYpPrgyKvaH7wRLu1jZWXD3Du1x.',
    -- raw_transactions (JSON)
    '{"attack_tx": "44tWhQmmkTJgchgFVkYpPrgyKvaH7wRLu1jZWXD3Du1x", "subject_wallet_creation": "2026-04-15T06:53:00+00:00", "subject_wallet_funding_source": "intents.near", "intermediary_accounts_total": "423+", "intermediary_accounts_deleted": 55, "mca_infrastructure": ["rhea000453.multica.near", "rhea000462.multica.near", "rhea000505.multica.near"], "first_mca_activation": "rhea000453 storage_deposit on lst.rhealab.near @ 2026-04-14T03:49:00+00:00", "main_exploit_window": "2026-04-16T08:22/09:42 UTC", "fake_token_pool_ids_ref_finance": [8528, 8538], "affected_code": "burrowland/margin_trading.rs#L102", "recovery": {"tether_freeze_attacker_wallet_usdt": 3291000, "tether_freeze_near_intents_usdt": 1053000, "voluntary_return_usdc": 3359000, "voluntary_return_near": 1564000, "total_recovered_usd_approx": 8257000}}',
    18400000.0,
    423,
    -- notes (Tier A + Tier B, explicitly labeled)
    'ATTACK CATEGORY (Tier B interpretation): Compositional harm via oracle manipulation. Primary mechanism: fake token price manipulation via controlled liquidity pools. Secondary mechanism: slippage protection aggregation bug in margin trading. Parent pattern: oracle manipulation + lending protocol exploit (Drift copycat family).

ROOT CAUSE (Tier A from handoff): Burrow Protocol margin trading aggregated min_amount_out values across swap actions without accounting for intermediary token reuse between steps. Each individual min_amount_out was correctly implemented. Aggregation logic was correctly implemented. Swap execution was correctly implemented. The vulnerability was in the semantic gap between what the code computed (sum of step-level slippage tolerances) and what the protocol designers intended it to bound (end-to-end output quantity). Affected code: burrowland/margin_trading.rs#L102.

CROSS-CHAIN CORRELATION (Tier B): 15 days after Drift Protocol exploit ($285M, 2026-04-01, Solana). Same attack family: fake token + manipulated oracle + lending protocol drain. Different chain (NEAR vs Solana). Different trigger (code aggregation bug vs compromised admin key). Confirms Strategy Lifecycle prediction: EARLY -> ARMS_RACE transition within 15 days of public demonstration.

METHODOLOGY NOTES (Tier B, framework implications):
- NEAR account deletion pattern: 55 intermediary accounts deleted with asset transfer to hub. NEAR-specific architectural capability enabling ephemeral organizational infrastructure. Layer 3 persistent-wallet assumption breaks on NEAR; methodology adaptation required if NEAR expansion is considered.
- Cross-chain identity laundering (Pattern D validation): Subject Wallet funded from intents.near, creating no direct on-chain link to attacker pre-NEAR identity. Confirms Pattern D from behavioral laundering framework.
- Sybil infrastructure at scale: 423+ counterparty addresses used as operational wallets. Distribution from single hub wallet, deletion after use. auto_funder_tracer would identify hub on EVM chains; on NEAR, deletion removes evidence.
- Bytecode-equivalent detection gap: Fake tokens lacking NEP-141 metadata methods = NEAR equivalent of "token without standard ERC-20 interface" — detection pattern EVM classifier catches but isn''t portable to NEAR Wasm.

RECOVERY COMPARISON (Tier B): Drift: $147M institutional + $100M credit facility vs $295M loss (~50% coverage). Rhea: $8.2M recovery vs $18.4M loss (~45% coverage). Pattern: ~45-50% recovery when centralized stablecoin issuer intervenes combined with voluntary return. Still represents significant unrecovered loss.

TIER A (DEDUCTIVE) claims preserved from handoff:
- Attack transaction hash verified: 44tWhQmmkTJgchgFVkYpPrgyKvaH7wRLu1jZWXD3Du1x
- Affected code path: burrowland/margin_trading.rs#L102
- Tether froze specific USDT amounts (verifiable on-chain)
- Account deletion pattern confirmed via NEAR explorer (55 accounts deleted)
- Fake tokens deployed on implicit account addresses (verifiable)

TIER B (INFERENTIAL) claims labeled as such:
- Attack methodology interpretation
- Connection to Drift attack family (pattern similarity, not provenance)
- Strategy lifecycle classification (ARMS_RACE)
- Attribution of coordinated behavior across 423 counterparty addresses to single operator',
    'near',
    0  -- monitored_chain = FALSE; NEAR is outside our ingest scope
);
```

---

## Why this event matters to the corpus

Three methodological contributions, in order of importance:

1. **Validates Pattern D (cross-chain reputation import) from the behavioral laundering framework.** The Subject Wallet had zero prior history on NEAR; funding arrived via `intents.near` (cross-chain bridge). Any per-chain profiling system — including our EVM-native methodology — would see a fresh wallet with one inbound transfer and classify it as UNKNOWN / benign. Rhea is the empirical confirmation that this evasion strategy works against per-chain detection at scale.

2. **Demonstrates the "ephemeral infrastructure" gap that NEAR's architecture enables.** EVM-style auto_funder_tracer works because addresses are persistent; the funding graph is reconstructable from balance changes. NEAR accounts can be *deleted*, with asset transfer to the hub, which removes the evidence trail from the on-chain state. 55 deletions across 3 coordinated waves is a feature of the attack, not an accident — the attacker exploited the architectural affordance. Layer 3 methodology assumes persistent wallets; NEAR expansion (if considered) would require adapting the funder trace to consume NEAR historical state, not current state.

3. **Confirms Strategy Lifecycle ARMS_RACE transition in 15 days.** This is the second public demonstration in the "oracle manipulation + lending protocol drain" family within two weeks of Drift ($285M, 2026-04-01). The corpus now has two datapoints on the EARLY → ARMS_RACE timing: fast. Expect further copies within 30 days per the strategy_lifecycle model.

---

## Cross-linkage to existing corpus

- **Parent event:** Drift Protocol exploit (2026-04-01). I did not find an `EXTRACTION_*` row for Drift — only EXTRACTION_001/002/003 exist. Drift is documented in `reports/drift_simulation.md`, `reports/drift_prehindsight_simulation.md`, `reports/post_drift_impact.md`, and is referenced throughout `claude.md` and the deck library. **Consider a separate EXTRACTION_005 for Drift itself**; it's the larger parent case study and deserves the same structured row. Not in scope for this draft; flagged as follow-up.
- **Pattern siblings:** EXTRACTION_003 (infrastructure parasitism, $211K) and the two org_001 rows (001, 002) are EVM-native; EXTRACTION_004 is the first off-chain reference event and the first of the "oracle manipulation + lending" family. Keep in a distinct `event_type` value — proposed `'oracle_manipulation_lending_exploit'` vs. the existing `'full_pipeline_cycle'` / `'infrastructure_parasite'`.
- **No correction log entry** per your instruction. This is corpus expansion.

---

## Deferred / open

- **Missing EXTRACTION_005 for Drift.** Noted above. If you want it, same pattern: draft INSERT + draft row and review before execution. Not in this scope.
- **NEAR-specific analysis extensions.** If Layer 3 is ever considered for NEAR expansion, three modules need architectural review: `auto_funder_tracer` (persistent-wallet assumption), `bytecode_classifier` (EVM-specific patterns not portable to Wasm), `deployer_profiler` (account-lifecycle assumption). None of this is asked-for today; flagging so future discussions don't restart from zero.
- **Strategy Lifecycle scoring.** The `strategy_lifecycle` table (8 rows, 22 days stale as of Wave 2 audit) would benefit from recording "Drift family ARMS_RACE: 15 days, n=2". Not in scope; the producer scheduler (Correction #7) will regenerate that table at its next run.

---

## What was not built

- No ALTER TABLE executed. Current schema unchanged.
- No INSERT executed. `extraction_events` still has 3 rows.
- No correction log entry (per your explicit instruction).
- No changes to `strategy_lifecycle`, `org_cycles`, or other analysis tables.
- No cross-link to behavioral laundering report files — that work is queued for Part 2.

Pause here. On approval: execute migration + INSERT on local, verify, mirror to Railway.
