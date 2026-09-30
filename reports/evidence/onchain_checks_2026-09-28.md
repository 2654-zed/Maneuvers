# On-chain verification record — 2026-09-28

Direct checks run by the auditing model against Ethereum mainnet (via Blockscout MCP and a JSON-RPC bridge) and the Arbitrum Blockscout REST API. These are primary-source checks of the historical corpus's most load-bearing Tier A claims. Nothing here is inferred from press coverage.

## 1. KelpDAO attack transaction (corpus: `reports/kelp_retrospective_replay.md`, `reports/extraction_event_008_kelp.md`)

Query: `get_transaction_info(chain_id=1, 0x1ae232da212c45f35c1525f851e4c41d529bf18af862d9ce9fd40bf709db4222)`

| Field | Corpus claim | Observed | Match |
|---|---|---|---|
| Block | 24,908,285 | 24,908,285 | yes |
| Timestamp | 2026-04-18 17:35:35 UTC | 2026-04-18T17:35:35Z | yes |
| Method | `EndpointV2.lzReceive` | `lzReceive((uint32,bytes32,uint64),address,bytes32,bytes,bytes)` to `0x1a44076050125825900e736c501f859c50fE728c` | yes |
| Source eid / nonce | srcEid 30320, nonce 308 | `_origin = (30320, 0x…c3eacf0612346366db554c991d7858716db09f58, 308)` | yes |
| Token movement | 116,500 rsETH from OFTAdapter `0x85d4…8ef3` to `0x8B1b…0D3b` | ERC-20 transfer of 116,500.000 RSETH from `0x85d456B2DfF1fd8245387C0BfB64Dfb700e98Ef3` to `0x8B1b6c9A6DB1304000412dd21Ae6A70a82d60D3b` | yes |
| Gas used | 94,456 | 94,456 | yes |
| tx.from | "Executor EOA" | `0x4966260619701a80637cDbdAc6A6cE0131f8575E` | consistent |

Verdict: the corpus's Tier A description of the attack transaction is exact.

## 2. Historical DVN configuration at block 24,500,000 (corpus Phase 3 replay)

Query: `eth_call` at block `0x175d720` (24,500,000) to `EndpointV2.getConfig(0x85d456B2DfF1fd8245387C0BfB64Dfb700e98Ef3, 0xc02Ab410f0734EFa3F14628780e6e695156024C2 /*ReceiveUln302*/, 30320, 2)`.

Decoded UlnConfig: `confirmations = 42`, `requiredDVNCount = 1`, `optionalDVNCount = 0`, `optionalDVNThreshold = 0`, `requiredDVNs = [0x589dedbd617e0cbcb916a9223f4d1300c294236b]`, `optionalDVNs = []`.

Matches the corpus table row for block 24,500,000 field-for-field. The "≥56.7 days of publicly readable 1-of-1 configuration" claim is independently reproduced. (LayerZero's May 18, 2026 incident report adds that the application owner had earlier downgraded a 2-of-2 configuration to 1-of-1; the window was therefore longer than the corpus measured, and a configuration *change* event existed that the corpus did not detect.)

## 3. Current DVN configuration (post-exploit defender adaptation)

Same call at `latest` (2026-09-28): `confirmations = 64`, `requiredDVNCount = 4`, `optionalDVNCount = 0`, `requiredDVNs = [0x380275805876ff19055ea900cdb2b46a94ecf20d, 0x589dedbd617e0cbcb916a9223f4d1300c294236b, 0xa4fe5a5b9a846458a70cd0748228aed3bf65c2cd, 0xa59ba433ac34d2927232918ef5b2eaafcf130ba5]`.

Kelp's Ethereum receive path for the Unichain channel now requires 4-of-4 DVNs with 64 confirmations. The corpus's central detection hook (`requiredDVNCount < 2`) would no longer flag this OApp.

## 4. Tornado Cash funding of the attack recipient (corpus Phase 4)

Query: `eth_getLogs(address=0x12D66f87A04A9E220743712cE6d9bB1B5616B8Fc /*Tornado 0.1 ETH pool*/, blocks 0x17c0a64–0x17c0a68)`.

One `Withdrawal` event at block 24,906,342 (`0x17c0a66`), tx `0xcb2ee450d6e770216dc3061750b4ac5b5fa494666bcf7eaa936411733e2ef7ee`, recipient `0x8b1b6c9a6db1304000412dd21ae6a70a82d60d3b`, relayer `0xee4c45cc5eaa535cb8a8ffdc92f2839a601fe226`, fee `0x7a6625c0c7260` wei (≈0.0021533 ETH → net ≈0.0978 ETH, matching the corpus's 0.0978467). Block timestamp `0x69e3657f` = 2026-04-18 11:05:35 UTC. Gap to exploit: 6 h 30 min. Corpus claim reproduced exactly.

## 5. CE5E "rogue x402 facilitator" (corpus: `reports/case_CE5E_drainer_operation.md`) — Arbitrum

Queries: Arbitrum Blockscout REST `/api/v2/addresses/0xce5ec7336f863931fda2ee3e4b9dad99fcc53c91/{counters,transactions?filter=from,token-transfers?type=ERC-20&filter=to}`.

- Counters: 214 transactions, 518 token transfers lifetime (as indexed).
- The address is **still active on 2026-09-28**: outbound `USDC.transfer` and `USDT0.transfer` calls at 13:42–17:56 UTC.
- Inbound page (most recent 50): on 2026-09-26 14:28:22 UTC a single-second batch of ~34 `transferFrom` pulls into CE5E from distinct addresses, amounts overwhelmingly round ($350, $1,800, $3,550, $10,010, $20,050, $72,032 USDC), plus recurring small `transfer` inflows ($0.000023–$3.39) from four addresses at regular intervals, and `0xb61d27f6`/`0x34fcd5be` (smart-account `execute`-style) inflows of ~$806–$1,999 from `0xEe7aE85f…4055`.
- `0xA3a1D7a54269be09C34aCCfeB4b08Adc21a51738` — the address the corpus reclassified on 2026-04-15 as a controlled pass-through intermediary — again sent $72,032 via `transferFrom` on 2026-09-26.

Interpretation for the audit: the corpus's *observation* (self-settlement `transferFrom` pulls into a facilitator EOA from many payers) is real and persists five months later. The corpus's *classification* (phishing drain of victims) is not established by this shape: single-second batch settlement of round-number amounts, repeat "victims" that keep paying over months, and the absence of any public victim report over five months are at least as consistent with a payment/settlement processor (legitimate or laundering) as with a phishing operation. See `V4/COMPETING_EXPLANATIONS.md` §1.

## 6. Aethir dev.to post-mortem quotations (corpus: lexicon "Operational Layer Attack", "Participatory Asymmetry")

Fetched `https://dev.to/cryip/aethir-adapter-exploit-complete-technical-postmortem-report-1001`. The post attributes root cause to a direct `transferOwnership()` call with "missing or bypassed onlyOwner modifier and weak ownership validation"; it names owner `0xd5fa8ac45d6a0984d14f3b301b18910948deb11a`; it gives no transaction hash. It does **not** contain the sentences the corpus quotes ("The legitimate owner was just an eoa…"; "The protocol had no multisig. They had no time wait mechanism…"). Those quotations could not be located in any source; the web-search budget was exhausted before an exhaustive search of other dev.to posts could be completed, so this is recorded as NOT FOUND rather than fabricated.

## Method notes

- Blockscout MCP free-session budget (8 calls) was consumed after the first transaction lookup; subsequent Ethereum reads used a JSON-RPC bridge (`eth_call`, `eth_getLogs`), and Arbitrum reads used the public Blockscout REST API via HTTP fetch.
- Selector for `getConfig(address,address,uint32,uint32)` computed locally as `0x2b3197b9` (keccak-256).
- No writes, no interaction with any flagged contract.
