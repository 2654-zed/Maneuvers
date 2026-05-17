# Case File — CE5E Drainer Operation (Arbitrum)

**Date:** 2026-04-18
**Status:** Active. 68 drain events over 6.8 days; pace unchanged today (11 drains, $135,400).
**Facilitator under review:** `0xce5ec7336f863931fda2ee3e4b9dad99fcc53c91` ("CE5E")
**Classification:** Rogue x402 facilitator (confirmed via `rogue_facilitator_self_settlement` detection path — `tx.from == decoded.to` on Permit2.transferFrom with facilitator in our rogue set).
**Purpose of this file:** Summarize surveillance evidence in a shape suitable for intelligence sharing, internal review, or recovery-coordination conversations. Every figure carries an explicit Tier A (deductive) or Tier B (inferential) label.

---

## Tier A — verifiable facts from our corpus

### Lifetime footprint
- **68 X402_AGENT_DRAIN events** attributed to CE5E as facilitator
- **67 unique victim addresses** (one repeat: `0xa3a1d7a54269be09c34accfeb4b08adc21a51738` hit twice)
- **$929,628.55 USDC drained** (6-decimal normalized; all 68 events targeted USDC on Arbitrum — the decimal normalization is safe for this operator per Correction #8)
- **Chain: Arbitrum only** (`0xaf88d065…5831`)
- **First seen:** 2026-04-12 01:44:04 UTC
- **Last seen:** 2026-04-18 21:08:42 UTC
- **Operational window:** 6 days, 19 hours
- **Daily average:** ~$137K / day (today's $135K is at baseline, not a spike)

### Today's 11 drain events (2026-04-18)

| Time UTC | Victim | USDC | Arbitrum tx hash |
|---|---|---|---|
| 01:19:15 | `0x96ec2c15…2b08` | $10,400 | `0xc6a2abea…72a94` |
| 01:38:15 | `0x95be5368…22ba7` | $10,050 | `0x542ffe6d…10bf` |
| 03:28:15 | `0xe8125614…9f194` | $10,000 | `0x40919e04…9695` |
| 07:14:02 | `0xa9283155…ea42` | $6,850 | `0xc50e1ef7…9e0b` |
| 08:21:33 | `0xc0b7e765…4ce2` | $16,500 | `0x44394cbc…e6eb` |
| 08:42:32 | `0x14aa42c5…172b` | $16,850 | `0x7a0bc450…82eb2` |
| 09:20:03 | `0x9a0bf937…6af7` | $10,400 | `0xc004c78a…5256` |
| 09:31:13 | `0xc3fc8855…4b68` | $20,000 | `0x49d7184e…ce14` |
| 10:42:53 | `0x554dc768…4297` | $20,050 | `0x58296ba8…1aaa` |
| 12:37:24 | `0x95e43c73…24ab` | $3,900 | `0xd0193f46…67d5` |
| 21:08:42 | `0x88e9557d…9d2a` | $10,400 | `0x22ea309e…0c2c` |

Each row: Permit2.transferFrom called with CE5E as both caller and destination; target token is Arbitrum USDC; victim had previously signed an unlimited, never-expiring Permit2 allowance to CE5E.

### Victim profile
- **0 of 11 victims had prior alerts** in our system — fresh wallets from the phishing funnel, not repeat marks
- **7 of 11 victims had prior `x402_permit2_exposure` rows** — meaning we tracked their Permit2 allowance *before* the drain fired. The gap between exposure-detection and drain-execution is the relevant observation window; the shortest was ~3 hours between signing and draining.
- **4 of 11 had no exposure trail** — our Permit2 exposure tracker missed their approval before the drain; only caught the sweep.

### CE5E operator wallet state (queried 2026-04-18 ~22:00 UTC via Alchemy Arbitrum)
- ETH balance: **2.37 ETH** on Arbitrum
- USDC balance: **$10,788.26** (consistent with the most recent $10,400 drain + gas reserve; operator moves funds out after each batch)
- The operator is NOT accumulating — $929K cumulative drain vs $11K current balance means ~$918K has been forwarded to destination wallet(s) outside our corpus

---

## Tier B — interpretations and open gaps

### Outflow destination: **unknown in our corpus**
The Permit2 Drain Case Study deck (`l3-narrative/Permit2_Drain_Case_Study.pptx` slide 6) claims CE5E proceeds concentrate in a vanity sink `0xbec87a77…d22` holding $3.63M. **We could not verify this from surveillance data today.** Cross-referenced every 0xbec8-prefix address in our DB across contracts, deployers, entity_classification, transaction_events, approval_events — no `0xbec87a77*` match. The deck's claim came from a different data source (likely manual Etherscan enumeration at the time the deck was drafted); the operation has continued since, and we don't index the sink's activity directly because:

- Sinks are EOAs that only receive USDC from CE5E; they don't deploy contracts (not in `contracts` table)
- We don't track arbitrary USDC inbound transfers — only Permit2 calls via our monitors
- Cross-chain moves out of the sink are invisible unless we build a dedicated outbound tracer

**Practical implication:** we can attest to the drains themselves with Tier A confidence, but we can't currently say where the $918K went. The $3.63M figure from the deck either referred to a now-cleared wallet or an address we never indexed. Either way, **do not cite the $3.63M concentration figure in new outreach without an independent lookup**.

### Funnel shape (inference)
- Median drain size: ~$10,400 — clustered around $10K and $20K
- Today's amounts are rounded (10,000 / 10,400 / 20,050) consistent with a phishing site that presents round numbers to victims
- 1.4-hour average interval between drains ⟹ automated processor, not manual operator
- 0 repeat-victim concentration (1 of 67 hit twice) suggests the phishing campaign is consuming fresh traffic at a rate that matches the drain rate — the bottleneck is fresh-victim acquisition, not execution

### Relation to broader operation
- Today's activity includes **1 drain via A7B9** on Base (non-stablecoin token; display value unreliable per Correction #8). Both CE5E (Arbitrum) and A7B9 (Base) firing today means the four-facilitator operation documented in the deck is at least two-facilitator-active right now. Worth re-running enumeration for E3B2 + E717 to confirm all four are still live.

---

## Actionable items — ranked by tractability

### 1. Tether freeze candidate (highest leverage)
**The CE5E operator wallet itself:** `0xce5ec7336f863931fda2ee3e4b9dad99fcc53c91`
Holds $10,788 USDC on Arbitrum at pull time. Tether/Circle policy is typically to freeze drainer wallets on verified incident reports. This is a small freeze target relative to the cumulative damage, but it's the one wallet we can point to with Tier A confidence. Larger freeze targets (the downstream sink) require separate discovery work.

### 2. Victim notification
11 victims today. 7 had prior Permit2 exposure that we were tracking. If there's a mechanism to notify these wallets before the next drain (via ENS / wallet-integrated warning / on-chain message), it would be a demonstration of predictive intelligence — Permit2 exposure tracked today means a future drain signal tomorrow. **Our system caught the signing events but took no action before the drain.** That's the category of Tier C predictive intelligence the decks describe; it would need a delivery mechanism.

### 3. Outflow tracer (scoped, not built)
Adding a one-shot outflow tracer for CE5E would reveal the current sink. ~5–10 Alchemy calls per drain event (trace the USDC outbound from CE5E after each inbound drain) × 68 events = ~500 calls. Over the 200-call budget you authorized for Part 2 Phase 3. Would require separate approval. Alternative: periodic Etherscan API lookup of CE5E's transaction history (free, rate-limited), one-shot.

### 4. Additional facilitator confirmation
The deck names E3B2 and E717 as CE5E-sibling drainers. Today's activity confirmed A7B9 is live on Base. We haven't probed E3B2 or E717's recent activity in this pull. If you want a full four-facilitator freshness check, that's a quick query (~1 min).

---

## Cross-references

- Methodology: `reports/circle_bridge_infrastructure.md` (adjacent — Circle's stablecoin ecosystem; the drainer operation exploits the same USDC payment surface the bridge operates on)
- Extraction context: `extraction_events` table (EXTRACTION_005 Drift, EXTRACTION_004 Rhea) — separate attack families; CE5E is not an oracle-manipulation-lending-drain case, it's a Permit2-phishing-drain pattern
- Deck narrative: `l3-narrative/Permit2_Drain_Case_Study.pptx` — note that deck's outflow claims require re-verification against current state before reuse in customer outreach
- Corrections: #5 (bytecode cache hygiene, unrelated to drain detection), #7 (scheduler; ensures future producer metrics stay current), #8 (decimal normalization; relevant because A7B9's Base drain displayed wrong — CE5E's Arbitrum drains display correct because USDC is on the allowlist)

---

## What this file explicitly does NOT claim

- **No attribution to a named operator, organization, or nation-state.** The Drift-Heist deck attributes that event to DPRK via Elliptic/TRM; we have no equivalent attribution evidence for CE5E. CE5E is "an operator running industrial-pace Permit2 draining on Arbitrum." Full stop.
- **No claim about the phishing infrastructure.** We see the on-chain drain. The phishing site delivering the signatures is off-chain and outside our observation surface (cf. `l3-narrative/The_Boundary.pptx`).
- **No $3.63M sink claim.** Legacy figure from prior documentation; not verifiable today.
- **No bounty-eligibility.** Per cross-session context: Permit2 isn't broken, Arbitrum isn't broken, USDC isn't broken; the drains are stored-potential discharge of user-authorized approvals. Cantina-class bounties don't apply. Intelligence-vendor framing only.
