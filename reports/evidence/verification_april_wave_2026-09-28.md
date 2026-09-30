<!-- EVIDENCE FILE. Provenance: fact-checking subagent run by the auditing model (Claude Fable 5.1) on 2026-09-28. Model-generated research output; every figure is a pointer to the cited URL. Direct on-chain checks were run against NearBlocks (NEAR) and the DefiLlama hacks API. BSC explorer access was unavailable from the sandbox. Quotes are ≤15 words, one per source. -->

# Fact-check report: April-2026 DeFi incident corpus (verified 2026-09-28)

Legend: **VERIFIED** / **PARTIALLY VERIFIED** / **CONTRADICTED** / **NOT FOUND**.

---

## 1. Drift Protocol (Solana) — PARTIALLY VERIFIED (mechanism verified; recovery claims partly wrong)

**Verdict by sub-claim**
- Date/time 2026-04-01 ~16:05 UTC — VERIFIED (BlockSec, Chainalysis, Blockaid).
- ~$285M — VERIFIED as the widely cited figure (BlockSec $285,279,417.69; QuillAudits $285.26M). Drift's own recovery plan (May 5) states total exploit losses of **$295,426,725.97**; early disclosures said $200M+, then ~$270–280M.
- Pre-acquired durable-nonce signatures from Security Council signers via social engineering — VERIFIED. Four durable-nonce accounts created March 23 (two controlled by SC members, two attacker-controlled); signatures collected March 23–30, re-collected against the migrated multisig by March 30/31. Drift's own April 1 X statement calls it "a novel attack involving durable nonces."
- 2026-03-27 migration to 2-of-5 with zero timelock — VERIFIED (BlockSec, Blockaid, Hypernative, Nexus Mutual, QuillAudits; Chainalysis says March 26).
- "Threshold reduced 3/5 → 2/5 and a timelock removed" — PARTIALLY VERIFIED / weakly sourced. Only Rekt states the prior threshold ("lowering the signing threshold from 3-of-5 to 2-of-5", citing an Andrew Hong gist). BlockSec, Blockaid, Hypernative, Chainalysis, Squads' statement and Drift's April 6 post-mortem describe only the post-migration 2/5, 0-timelock state. On the timelock, Nexus Mutual and Halborn say it was removed/eliminated at migration; Rekt says no timelock existed before either. Treat "3/5→2/5" and "timelock removed" as unconfirmed by primary sources.
- Fake "CVT" (CarbonVote Token) wash-traded to ~$1 on Raydium and accepted as collateral — VERIFIED. 750M minted (March 11/12), ~80% attacker-held, Raydium pool seeded with ~$500 (Chainalysis/Blockaid/Rekt; TRM/Halborn say "a few thousand dollars"), 500M CVT deposited as collateral.
- Two transactions four slots apart — VERIFIED (BlockSec, Blockaid, Hypernative, Rekt; QuillAudits gives slots 410344005 and 410344009, ~1 second apart). 31–33 withdrawal txs in ~12 minutes; full drain over ~2.5 hours.

**Best-source facts:** Solana; Squads V4 multisig; drained JLP ~$155–159M, USDC ~$60–71M, cbBTC $11.3M plus USDT/WETH/dSOL/WBTC/JTO/others; ~$230–232M USDC bridged to Ethereum via Circle CCTP over ~6 hours.

**Recovery/aftermath**
- **"Tether froze $127.5M" — CONTRADICTED.** Tether froze nothing in this incident. Tether committed *support capital*: "Tether is proposed to contribute up to $127.5 million" (Drift, April 16), structured as a **$100M revenue-linked credit facility** plus an ecosystem grant and market-maker loans, with ~$20M from "other partners." Total package ~$147.5–150M.
- Only freeze on record: "Three transfers via Circle's CCTP have been successfully frozen, totaling approximately 3.36M USDC." (Drift, May 5). Circle declined to freeze the ~$230M flow in real time (Allaire: acts only on law-enforcement/court direction), which drove Drift's switch from USDC to USDT settlement.
- "Solana Foundation contributed $20M" — NOT CONFIRMED by primary source. Drift's April 16, May 5 and June 3 updates say "other/strategic partners" up to $20M, unnamed. CryptoBriefing/Tekedia headlines attribute the plan to "Tether and Solana Foundation," but no Drift or Foundation document names a Foundation contribution. The Foundation's April 7 announcement was the STRIDE evaluation program and SIRN incident network, not a Drift grant.
- $100M revenue-linked credit facility — VERIFIED (Drift April 16).
- Mechanism for users: transferable SPL "recovery token," 1 token = $1 verified loss, redeemable pro-rata as the pool fills; pool seeded with ~$3.8M; relaunch as USDT-settled perps exchange targeted Q2 2026; 10% bounty on recovered assets (Arkham/Bybit supported). ~130,259 ETH (~$293M) sat in four monitored attacker wallets as of May 5.
- **Attribution:** TRM (initial: likely DPRK; CVT deployed ~09:30 Pyongyang time) and Elliptic (DPRK tradecraft) — VERIFIED. Drift's April 6 post-mortem: UNC4736 (AppleJeus/Citrine Sleet), medium-high confidence, six-month in-person operation posing as a quant firm, malicious repo + TestFlight wallet + VSCode/Cursor exploit. Note a designator change: Drift's June 3 update says "Mandiant's investigation conclusively attributed the attack to UNC6862." Flag this inconsistency (UNC4736 vs UNC6862) in the corpus.

**Contradictions:** the $127.5M "freeze"; the $20M attributed specifically to Solana Foundation; 3/5→2/5 unsupported by primary sources.

---

## 2. Silo Finance (2026-04-03) — PARTIALLY VERIFIED; "same family as Drift" is a stretch

- DefiLlama hacks record: 2026-04-03, "Silo V2," **Arbitrum**, **$359,000**, classification Oracle Manipulation / **Oracle Misconfiguration**. Press (CoinMarketCap, FinanceFeeds, dev.to) cites **~$392K** and a "misconfigured oracle exploit."
- Mechanism: a misconfigured price feed for one isolated market, not a governance takeover or a wash-traded fake collateral token. So it is an oracle-pricing failure, loosely analogous to Drift's CVT pricing, but not the same attack family (Drift's root cause was signer compromise via durable nonces).
- **No Silo primary post-mortem located.** Do not conflate with the June 2025 Silo incident ($545K, Arbitrum, logic error) or the July 2023 RAM-SEC whitehat rescue.

---

## 3. Aethir OFTAdapter (BNB Chain, 2026-04-09) — PARTIALLY VERIFIED; owner/root-cause claims NOT FOUND

- Date April 9, 2026; contract AethirOFTAdapter on BNB Chain; ~$400K+ gross (~423K ATH per PeckShield; DefiLlama $400K); Aethir: user losses under $90,000 after disconnecting contracts and blacklisting wallets with exchanges — VERIFIED (PeckShieldAlert; Aethir X "ATH Security Notice"; Cointelegraph). Main ATH supply on Ethereum unaffected; compensation plan promised.
- Laundering BNB Chain → TRON via Symbiosis — VERIFIED; PeckShield: "bridged the stolen funds from #Bnbchain to #TRON via symbiosis[.]finance".
- "Single EOA owner, no multisig/timelock" and "private-key compromise" — **NOT FOUND.** Aethir never published a public root cause. The dev.to post-mortem exists (dev.to/cryip, April 10) but is a third-party write-up, not Aethir's. It frames the cause as an unauthorized `transferOwnership` call via "missing or bypassed onlyOwner modifier" (access control), gives no tx hash, and never states the owner was a single EOA. DefiLlama classifies it "Access Control / Improper Access Control." The corpus's "private-key compromise" framing therefore conflicts with the only detailed write-up and is unconfirmed either way. BSC state could not be read from this sandbox.

---

## 4. Zerion (~$100K, DPRK social engineering) — VERIFIED with date caveat

- Zerion disclosed on April 14, 2026 (coverage April 15 says the attack "took place last week"); DefiLlama dates it April 14. The corpus's April 10 is plausible but not confirmed by any primary statement.
- Mechanism: multi-week, low-pressure social engineering (Telegram/LinkedIn/Slack) with AI-edited images/video; one team member's device compromised; attacker obtained logged-in sessions, credentials and private keys to internal test/hot wallets; ~$100K taken from company wallets; no user funds, apps or infrastructure affected; web app taken down for ~48h as precaution.
- Attribution: Zerion called it a DPRK-linked actor; coverage links it to UNC1069.

---

## 5. Hyperbridge Token Gateway (2026-04-13) — VERIFIED

- Time: April 13, 2026, 03:39–05:08 UTC (Verichains); forged PostRequest at 03:55:23 UTC (DarkNavy). DefiLlama lists April 12 (day-bucketing artifact).
- Bug: MMR proof verification in `MerkleMountainRange` lacked a `leaf_index < leafCount` bounds check; with leafCount = 1 and an out-of-bounds leaf index, `CalculateRoot` returned `proof[0]` unmodified, so any supplied node equal to the stored root verified. Reached through `HandlerV1.handlePostRequests(...)`, delivering a forged `ChangeAssetAdmin` to TokenGateway, then minting ~1B bridged DOT (also ARGN, MANTA, CERE). Hyperbridge's own blog: "proof forgery due to missing input validation" in VerifyProof. Aggravators (dev.to): no cryptographic binding between proof and request body; challengePeriod 0.
- Phases: Hyperbridge: "roughly 245 ETH from TokenGateway preceded the main event by approximately one hour," then the 1B DOT mint and dump. The ~108.2 ETH (~$237K) figure in Verichains/DarkNavy is the Ethereum DOT-dump proceeds, which is why the initial loss was reported as ~$237K.
- Revised loss: **~$2.5M** (April 16), across DOT pools on **Ethereum, Base, BNB Chain, Arbitrum**; user incentive-pool deposits were hit. DefiLlama: $2.5M.
- Aftermath: Token Gateway paused pending patch, independent audit and new safeguards; funds traced, "significant portion routed to Binance," Binance compliance + law enforcement engaged; if recovery fails, BRIDGE tokens to cover residual losses, structured from one year after April 13, 2026; 14-day return window for users who over-withdrew. Attacker EOA 0xC513E4…F8E7; key tx 0x240aeb9a…1109. No attribution.

---

## 6. "Dango" (2026-04-13) — IDENTIFIED / VERIFIED

- Dango is a Hack VC-backed Layer-1 with a perpetuals DEX. On April 13, 2026 a flaw in the insurance-fund donation logic (donation amount not validated as positive; DefiLlama: Input Validation / Missing Input Validation) let an exploiter extract ~**$1.9M USDC**; **$410,010 USDC** was bridged to Ethereum before bridge rate limits bit; ~$1.49M stayed on-chain and was recovered. On April 14 the exploiter returned everything as a white hat and received a bug bounty; users unaffected; chain restarted with fix.
- Unrelated to the exploit: Dango announced a wind-down — trading halts July 29, 2026 12:00 UTC, L1 shuts August 13, 2026.

---

## 7. Rhea Finance / Burrow (NEAR, 2026-04-16) — VERIFIED (on-chain confirmed), with small corrections

**On-chain (NearBlocks API, checked directly):**
- Attack account `5a7695e3…343040` (implicit account) created **08:23:14 UTC** April 16 with 15 NEAR from parent `31ac7a27…a540`; contract deployed 08:51:12; Ref pools created from 08:52:45; 13 `open_position` margin calls 08:55:34–09:21:30; last outbound transfers 09:52:29; **DELETE_ACCOUNT at 09:54:44 UTC**. The corpus's 08:22–09:42 window is close but the account activity ran to ~09:54.
- Parent `31ac7a27…` was created April 15 06:53 UTC (100 yocto from team.herewallet.near) and received **74 NEAR from `intents.near` at 07:12:49 UTC April 15**, then wrapped NEAR and fan-out-funded dozens of worker accounts (10–15 NEAR each). "Funded via intents.near" — VERIFIED.
- Tx `44tWhQmmkTJgchgFVkYpPrgyKvaH7wRLu1jZWXD3Du1x` — VERIFIED as real: an `open_position` call at 09:47:12 UTC by the attack account (95 ZEC moved burrow→ref). It is one of 13 margin opens, not the sole/first attack tx (first open_position was 08:55:34).
- Fake tokens on implicit accounts paired with USDC on Ref: VERIFIED.

**Documented facts:**
- Loss **$18.4M** (initial estimate $7.6M) — VERIFIED (Rhea post-mortem thread; The Block; AMBCrypto).
- Root cause: `get_token_out()` in burrowland `contracts/contract/src/margin_trading.rs` (L101–113) summed intermediate minimums across the route so attacker tokens counted as final output — VERIFIED.
- Pool range: Rekt/Defi_Nerd cite **25 consecutive pools 8514–8538**; the corpus's 8528–8538 is a subset. 123 fake token contracts (Rekt). Rehearsal began April 13.
- "55 intermediary accounts deleted" — VERIFIED via TechFlow's report of Rhea's disclosure. (Coinedition separately reports 423 intermediary wallets created.)
- Recovery: voluntary returns **3.359M USDC + 1.564M NEAR** — VERIFIED. Frozen USDT **4.34M total** — VERIFIED, but per Rhea/TechFlow the split is **3.291M frozen by Tether and 1.053M frozen by NEAR Intents**, not two Tether freezes. Total recovered ≈ $8.3M. Outstanding ~$5.6M (The Block); ~$4M went to Zcash shielded pools; ~$3.4M sits as aUSDC on Aave Ethereum. No attribution.

---

## 8. KelpDAO rsETH / LayerZero (2026-04-18) — VERIFIED, with number ranges

**Core facts:** April 18, 2026, 17:35 UTC; **116,500 rsETH ≈ $292M** (DefiLlama $293M); forged Unichain→Ethereum OFT packet; LayerZero Labs DVN `0x589dEDbD…236b` was the **sole required DVN (1-of-1, zero optional)**; the Ethereum adapter is a lock-and-release custody pool, so real user deposits were released. PoC README: "no transaction was ever sent on Unichain" (source nonce never advanced past 307; forged nonces 308 and 309). Attack tx 0x1ae232da…db4222, block 24,908,285. A second forged packet (40,000 rsETH ≈ $95M) was blocked ~46 minutes later by blacklisting.

**DVN compromised vs colluding — resolved: compromised, via RPC poisoning; signer keys not stolen.** LayerZero Labs' May 18, 2026 incident report (Mandiant + CrowdStrike): breach began **March 6, 2026** when a LayerZero RPC-team developer was socially engineered into cloning a malicious GitHub repo that dropped macOS backdoors; session keys harvested; March 30–April 16 recon/persistence in GCP and GitHub; April 16–18 lateral movement into GKE and in-memory patching of op-geth on two clusters that fed forged responses only to the DVN signing path; April 18 16:30 UTC DoS on external RPC providers forced failover onto the poisoned internal nodes; 17:35 forged attestation signed by legitimately held keys. Forensics found no key exfiltration.

**2-of-2 → 1-of-1:** LayerZero's report: "a previous 2-of-2 configuration had been modified by the application owner to a 1-of-1" (delegate EOA 0x1f7A03b7…769b). Kelp's position (lawsuit): LayerZero told it there was "no problem" with the default DVN setup on Feb 2, 2024 and on March 21, 2024 directed Kelp to mirror another bridge's 1-of-1 config.

**Aave:** attacker supplied ~89,567 rsETH to Aave V3 (Ethereum + Arbitrum) and borrowed WETH — VERIFIED. "$236M WETH" matches the KuCoin blog (126,000 ETH); Rekt: ~82,650 WETH borrowed on Ethereum plus ~$72M moved to Arbitrum; CoinDesk/OpenZeppelin: ~$190M borrowed. Bad-debt estimates ranged $123.7M (socialized) to $230.1M (L2-isolated); Aave ARFC: original shortfall **~163,183 ETH**. WETH reserves hit 100% utilization; Aave TVL fell ~$10B.

**Arbitrum freeze:** Security Council (9-of-12 emergency vote) froze **30,766 ETH (~$71M)** on April 20, 2026 11:26 pm ET; Arbitrum said it "acted with input from law enforcement as to the exploiter's identity" — VERIFIED.

**PoC repo** github.com/DK27ss/KelpDAO-294m-PoC — VERIFIED.

**Aftermath through Sept 2026**
- LayerZero (April 19/20 statement, May 18 report): DVN now refuses to be sole required attestor on any channel; multi-source RPC quorum with provider/geo diversity; second Rust client; cloud environment rebuilt; protocol defaults moving to no less than 3-of-3.
- Attribution: Mandiant and CrowdStrike — DPRK high confidence, **UNC4899 (TraderTraitor / Jade Sleet)** medium confidence; Chainalysis: Lazarus/TraderTraitor. Same cluster the FBI named for Bybit.
- Laundering: ~75,701 ETH converted to BTC within ~36 hours mainly via THORChain.
- DeFi United (Aave-led, April 23–28): >$300M ETH pledged (ConsenSys 30,000 ETH; Mantle credit facility up to 30,000 ETH; EtherFi 5,000; Stani Kulechov 5,000; Lido up to 2,500 stETH; group 14,570 ETH; Aave DAO treasury request 25,000 ETH). ARFC accounting: recoveries ~87,955 ETH (54%) = Kelp froze 40,373 rsETH (~43,168 ETH) + Arbitrum 30,766 ETH + Aave liquidation up to 12,323 WETH + Compound 1,845 WETH; residual gap ~75,081 ETH. Final tranche 20,373.72 rsETH delivered May 25, 2026; rsETH operations resumed ~May 25–26; Kelp migrated rsETH bridging to Chainlink CCIP; >$650M withdrawn by Kelp users post-exploit.
- Frozen-ETH litigation: North Korea terrorism-judgment creditors served a restraining notice in SDNY claiming the ETH as DPRK property. Arbitrum DAO voted May 8 (~91%) to send the ETH to an Aave-controlled wallet; Judge Margaret Garnett on May 9 modified the notice to allow the transfer, with Aave remaining bound by the freeze pending a merits ruling; further hearing set for June 5, 2026. No post-June ruling found.
- **Sept 25, 2026:** KelpDAO sued LayerZero Labs and CEO Bryan Pellegrino in the Supreme Court of British Columbia, alleging LayerZero reviewed and endorsed the 1-of-1 configuration; Pellegrino: "The claim continues to be meritless." Case pending.

---

## 9. Bybit ($1.5B, Feb 2025) — VERIFIED as operational-layer / Safe{Wallet} supply-chain compromise

- Feb 21, 2025; ~$1.46–1.5B. Sygnia: the malicious code "originated directly from Safe{Wallet}'s AWS Infrastructure" — not Bybit's systems. Safe{Wallet} developer macOS workstation compromised Feb 4, 2025 via a malicious Docker project; AWS session tokens hijacked; app.safe.global JavaScript replaced Feb 19 with code that activated only for Bybit's Safe; executed Feb 21. FBI attribution: TraderTraitor (UNC4899/Jade Sleet).

---

## 10. Blockaid "January 2026 prediction" about "operational layers around key management" — NOT FOUND

- No Blockaid publication from January 2026 with that wording could be located. Blockaid's blog lists no January 2026 posts. The one Blockaid document dated January 2026 is its SEC Crypto Task Force submission (Jan 5, 2026): it argues for pre-execution prevention and multisig co-signing controls but contains no "operational layers" or "key management" prediction language.
- Closest genuine Blockaid wording is retrospective: the April 19, 2026 KelpDAO post states the attack surface is now "the off-chain infrastructure, key management, and trust assumptions". Blockaid's H1 2026 report (July 28, 2026) and Sept 10, 2026 press release state "74% of stolen crypto value in H1 2026 came from operational and infrastructure compromises."
- Recommendation: cite the April 2026 KelpDAO post as a contemporaneous framing, or drop the "January 2026 prediction" attribution.

---

## Cross-cutting notes
- Dates/amounts largely hold; the corpus's weakest claims are (1) Drift "Tether froze $127.5M" (wrong), (2) Drift "$20M from Solana Foundation" (unconfirmed), (3) Drift 3/5→2/5 (single secondary source), (4) Aethir single-EOA/private-key root cause (no source; contradicted in framing by the only write-up), (5) Blockaid January prediction (not found), (6) Rhea's second $1.05M USDT freeze was by NEAR Intents, not Tether, (7) Zerion's April 10 date (disclosed April 14).
- DPRK attribution consensus: Drift (UNC4736 per Drift April 6; UNC6862 per Drift June 3 citing Mandiant), Zerion (UNC1069), KelpDAO (UNC4899/TraderTraitor, same as Bybit). Rhea, Hyperbridge, Dango, Silo, Aethir: no state attribution.

## Sources
- DefiLlama hacks API: https://api.llama.fi/hacks
- Drift: https://www.drift.trade/updates/incident-recovery-update-april-16-2026-now ; https://www.drift.trade/updates/recovery-plan-for-affected-users ; https://www.drift.trade/updates/drift-recovery-update-june-3-2026 ; https://www.trmlabs.com/resources/blog/north-korean-hackers-attack-drift-protocol-in-285-million-heist ; https://www.chainalysis.com/blog/lessons-from-the-drift-hack/ ; https://blocksec.com/blog/drift-protocol-incident-multisig-governance-compromise-via-durable-nonce-exploitation ; https://blockaid.io/blog/285m-gone-how-blockaids-cosigner-could-have-protected-drift-protocol ; https://www.hypernative.io/blog/the-drift-exploit-when-privileged-access-has-no-limits ; https://nexusmutual.io/blog/drift-protocol-incident-report ; https://rekt.news/drift-protocol-rekt ; https://www.quillaudits.com/blog/hack-analysis/drift-protocol-multisig-exploit ; https://www.halborn.com/blog/post/explained-the-drift-hack-april-2026 ; https://www.coindesk.com/business/2026/04/16/drift-gets-usd148-million-funding-from-tether-and-partners-as-it-replaces-circle-stablecoin-with-usdt-after-massive-exploit ; https://www.coindesk.com/business/2026/05/05/drift-outlines-a-recovery-plan-for-users-after-usd295-million-dprk-linked-exploit ; https://www.coindesk.com/tech/2026/04/07/solana-foundation-unveils-security-overhaul-days-after-usd270-million-drift-exploit ; https://fortune.com/2026/04/17/tether-127-5-million-drift-circle-freeze-hacked-funds/ ; https://www.bleepingcomputer.com/news/security/drift-280m-crypto-theft-linked-to-6-month-in-person-operation/
- Silo: https://dev.to/pavelespitia/oracle-manipulation-how-a-392k-silo-finance-loss-happened-in-2026-2051 ; https://coinmarketcap.com/academy/article/12-crypto-protocols-attacked-in-two-weeks-after-drift-exploit
- Aethir: https://x.com/PeckShieldAlert/status/2042441698559868970 ; https://x.com/AethirCloud/status/2042492153079939191 ; https://cointelegraph.com/news/aethir-bridge-exploit-halt-user-compensation-90k-loss ; https://dev.to/cryip/aethir-adapter-exploit-complete-technical-postmortem-report-1001
- Zerion: https://ambcrypto.com/zerion-claims-no-user-funds-were-affected-as-employee-loses-100k-in-social-engineering-attack/ ; https://www.cryptotimes.io/2026/04/15/north-korean-hackers-target-zerion-in-ai-driven-attack-steal-100k/
- Hyperbridge: https://blog.hyperbridge.network/security-update-forged-proofs/ ; https://blog.hyperbridge.network/recovery-and-next-steps/ ; https://blog.verichains.io/p/how-a-missing-bounds-check-led-to ; https://www.darknavy.org/web3/exploits/hyperbridge-ismp-forged-proof-dot-mint/ ; https://www.theblock.co/news/defi/2026-04-16-polkadot-hyperbridge-exploit-losses-2-5-million-ten-times-initial-estimate-397773
- Dango: https://ourcryptotalk.com/news/dango-perp-dex-exploit-insurance-fund-bug ; https://ambcrypto.com/dango-exploit-resolved-after-white-hat-returns-funds-users-unaffected/ ; https://thedefiant.io/news/defi/perp-dex-dango-to-wind-down-will-halt-trading-july-29
- Rhea: NearBlocks API (https://api.nearblocks.io/v1/txns/44tWhQmmkTJgchgFVkYpPrgyKvaH7wRLu1jZWXD3Du1x) ; https://rekt.news/rhea-finance-rekt ; https://x.com/rhea_finance/status/2045203607856042118 ; https://www.theblock.co/post/397961/rhea-finance-post-mortem-exploit-losses-18-4-million-double-initial-estimates ; https://www.techflowpost.com/en-US/newsletter/120176 ; https://www.halborn.com/blog/post/explained-the-rhea-finance-hack-april-2026
- KelpDAO: https://layerzero.network/publications/kelpdao-incident-report.pdf ; https://layerzero.network/blog/layerzero-labs-kelpdao-incident-report ; https://layerzero.network/blog/kelpdao-incident-statement ; https://blockaid.io/blog/how-a-single-layerzero-dvn-compromise-drained-292m-from-kelpdao ; https://www.chainalysis.com/blog/kelpdao-bridge-exploit-april-2026/ ; https://www.openzeppelin.com/news/lessons-from-kelpdao-hack ; https://rekt.news/kelpdao-rekt ; https://raw.githubusercontent.com/DK27ss/KelpDAO-294m-PoC/main/README.md ; https://x.com/arbitrum/status/2046435443680346189 ; https://www.coindesk.com/markets/2026/04/21/arbitrum-freezes-usd71-million-in-ether-tied-to-kelp-dao-exploit ; https://www.coindesk.com/business/2026/04/23/aave-rallies-defi-partners-to-contain-fallout-from-usd292-million-kelpdao-hack ; https://governance.aave.com/t/arfc-rseth-incident-funding-update/24740 ; https://www.theblock.co/post/400642/arbitrums-71-million-in-eth-cleared-for-aave-transfer-as-north-korea-terrorism-creditors-retain-legal-claim ; https://www.theblock.co/news/regulation/2026-09-25-kelpdao-sues-layerzero-claims-it-endorsed-setup-used-in-292-million-rseth-exploit-416361 ; https://thedefiant.io/news/hacks/layerzero-s-incident-report-says-kelp-downgraded-from-2-of-2-to-1-of-1-before-usd292m-exploit
- Bybit: https://www.sygnia.co/blog/sygnia-investigation-bybit-hack/ ; https://thehackernews.com/2025/02/bybit-hack-traced-to-safewallet-supply.html
- Blockaid: https://www.blockaid.io/blog ; https://blockaid.io/h1-report-2026 ; https://www.sec.gov/files/ctf-written-blockaid-submission-01-05-2026.pdf ; https://www.prnewswire.com/news-releases/blockaid-expands-onchain-monitoring-as-infrastructure-failures-drive-74-of-crypto-losses-302874819.html ; https://www.theblock.co/post/409944/crypto-hacks-hit-record-high-in-h1-2026-as-losses-top-1-billion-blockaid-says
