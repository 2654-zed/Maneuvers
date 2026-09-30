<!-- EVIDENCE FILE. Provenance: fact-checking subagent run by the auditing model (Claude Fable 5.1) on 2026-09-28. Model-generated research output; every figure is a pointer to the cited URL. Direct JSON-RPC / Blockscout on-chain checks were run for the Wasabi CREATE2 claim and the 0xF7CFFC27 wallet. Quotes are ≤15 words, one per source. -->

# Fact-check report: May-2026 corpus claims (14 items)

Verification date: 2026-09-28. Primary sources: THORChain official Exploit Reports #1/#2, THORNode GitLab (commit + MR 4820), V12 Security PoC repo, Rekt, BlockSec, Verichains, Halborn, DarkNavy, SlowMist, TRM, Vercel KB bulletin, DefiLlama hacks API, plus direct on-chain checks.

Scorecard: 1 VERIFIED (Sui key compromise), 2 VERIFIED (CREATE2 claim wrong), 3 PARTIALLY (identified, mechanism wrong), 4 CONTRADICTED (mechanism wrong), 5 VERIFIED, 6 CONTRADICTED on mechanism (official cause is GG20 TSS key leakage; the ObservedTx "bit-flip" bug is a real, separately-disclosed, patched bug that THORChain says is unrelated), 7 VERIFIED, 8 VERIFIED incl. same-operator claim (attributed to Blockaid), 9 PARTIALLY (root cause is uninitialized facet, not "diamondCut injection" as entry point), 10 PARTIALLY (event real; "5+/49+ wallets", "3.5-minute burst", and "Permit2" are wrong), 11 VERIFIED ("SSO" is an embellishment), 12 NOT FOUND, 13 NOT FOUND in public reporting but on-chain trace shows a plausible small-scale match, 14 NOT FOUND.

---

## 1. Volo Protocol — 2026-04-21, ~$3.5M — VERIFIED

Chain: **Sui** (Volo Vaults, NAVI's liquid-staking arm). Loss ~$3.5M from three vaults (~19.6 WBTC, XAUm tokenized gold, USDC; sources disagree on split). Root cause: **compromised privileged operator/admin private key** (SlowMist "Private Key Leakage"; BlockSec "Operator private key leaked"). No contract bug; attacker executed the legitimate operator withdrawal path. DefiLlama: Key Compromise, Sui, $3.5M. Aftermath: USDC bridged via CCTP within ~80 min; WBTC bridge attempt blocked on LayerZero; ~$500K frozen within 30 min; Recovery Update #5 (Apr 28): ~98% recovered, net loss ~$60K covered by treasury. Note: a **Move/Sui** key compromise, not an EVM proxy-upgrade pattern.

Sources: rekt.news/volo-rekt; blocksec.com/blog/weekly-web3-security-roundup-2026-04-26; coindesk.com/markets/2026/04/22/another-defi-protocol-loses-millions-in-hack-days-after-kelpdao-breach; api.llama.fi/hacks.

## 2. Wasabi Protocol — 2026-04-30 — VERIFIED (CREATE2 claim wrong)

Date 2026-04-30 ~07:46–09:07 UTC. Deployer EOA `0x5c629f8c0b5368f523c85bfe79d2a8efb64fb0c8` (wasabideployer.eth), sole ADMIN_ROLE holder; timelock supported but set to zero (Halborn). Attacker EOA `0x02228b0afcdbEdf8180D96Fc181Da3AF5DD1d1ab`; helper `0x878E94142409DAFCC5CC83D5cD2e9DA2Bf0BF3bF`. Sequence: `grantRole()` with delay=0 → UUPS `upgradeTo` on WasabiVault/LongPool → `strategyDeposit()` to fake strategy → `drain()` → swaps to ETH → 5 wallets → 4 via Tornado. Amount: Blockaid initial $4.55M (ETH+Base); Rekt total **$5.9M** (~$2M ETH, ~$2.5M Base, remainder Berachain+Blast); DefiLlama $5.5M, chains **Ethereum, Base, Berachain, Blast**. Blockaid's wording: "on-going admin-key compromise exploit".

**On-chain check:** Helper `0x878E…F3bF` has identical bytecode on Ethereum, Base, and Berachain; on Blast `eth_getCode` returns `0x`. Creation tx on Ethereum has `to: null`, `nonce: 0` from the attacker EOA — **plain CREATE at nonce 0, not CREATE2**. The address is the same on each chain because a fresh EOA's first deployment yields the same address everywhere.

Aftermath: SEAL 911 + Blockaid engaged; FBI notified; no post-mortem or compensation plan as of May 9; key-compromise vector never disclosed; no attribution by TRM.

Sources: rekt.news/wasabi-protocol-rekt; halborn.com/blog/post/explained-the-wasabi-protocol-hack-april-2026; coindesk.com/tech/2026/04/30/wasabi-protocol-drained-for-usd4-5-million-in-apparent-admin-key-compromise; banklesstimes.com/articles/2026/04/30/blockaid-flags-live-admin-key-exploit-hitting-wasabi-protocol-on-ethereum-and-base/; on-chain via ethereum-rpc.publicnode.com, mainnet.base.org, rpc.berachain.com, rpc.blast.io, eth.blockscout.com.

## 3. Juicebox V3 — 2026-04-20 — PARTIALLY VERIFIED (mechanism wrong)

Ethereum, **~$50.7K–$52K** (~21.77 ETH). Component: **REVLoans** (Revnet loans on the Juicebox V3/V5 stack). Root cause (BlockSec): `borrowFrom()` accepted caller-supplied `(terminal, token)` pairs without checking registration; attacker forged a 36-decimal accounting context to bypass price oracles and inflate `totalBorrowed`. DefiLlama: Input Validation / Missing Input Validation. **Not an access-control/admin pattern.**

Sources: blocksec.com/blog/weekly-web3-security-roundup-2026-04-26; academy.teleswap.xyz/defi-protocol-hacks-april-2026-exploits-analyzed; api.llama.fi/hacks.

## 4. Thetanuts Finance — 2026-04-20 — CONTRADICTED on mechanism

Ethereum, **~$50K**, DefiLlama: Token & Share Accounting / **First Depositor Attack**. Single chain, no admin key. A separate, larger Thetanuts incident on **2026-06-15** (~$2.1M, deprecated legacy vault, redemption-formula rounding flaw; most option tokens whitehat-recovered) is outside the corpus window.

Sources: api.llama.fi/hacks; academy.teleswap.xyz/…; cryptopolitan.com/hack-deprecated-thetanuts-vault.

## 5. Renegade Finance (Arbitrum) — 2026-05-10 — VERIFIED

Exploit tx `0x0e494685ace16d372066c5b4db959b58ebac6d88166c2d9d618e0e421dc0c77e`, **2026-05-10 08:27:23 UTC** (some outlets say May 11). Proxy `0x30bd8eab29181f790d7e495786d4b96d7afdc518` (legacy **V1 Arbitrum** dark pool). Attacker EOA `0x777253f28adc29645152b7b41be5c772a9657777`. Mechanism: called `initialize(...)` on the proxy with attacker-controlled addresses → became admin → delegatecalled malicious logic → swept ERC-20s. Token count: Blockaid "27 ERC-20s"; DarkNavy counts 26. ~$209K. Blockaid's alert text: "An unprotected initializer on the Dark Pool proxy…". Aftermath: ~$190K returned; **90/10 split**; V1 Arbitrum suspended; users compensated.

Sources: x.com/blockaid_/status/2053395937708384587; darknavy.org/web3/exploits/renegade-dark-pool-unprotected-initializer; cryptobriefing.com/renegade-recovers-190k-hacker-returns-funds; hacked.slowmist.io/?c=Arbitrum.

## 6. THORChain — 2026-05-15 — CONTRADICTED on root cause

**Official mechanism (THORChain Exploit Report #1, May 2026; Report #2, July 3 2026):** A **GG20 TSS cryptographic attack**, not observation forgery.
- Attacker (Discord "Dinosauruss", joined dev Discord May 1) churned in a validator on **May 13** (node `thor16ucjv3v695mq283me7esh0wdhajjalengcn84q`, ~635K RUNE bond), randomly assigned to one of five Asgard vaults.
- Planted a malformed **multi-prime Paillier modulus** in its own key material; deliberately failed the MtA/round-2 step **864 times over ~2.5 days**, each failure leaking a fragment of other validators' key shares.
- Three inherited weaknesses in THORChain's fork of Binance tss-lib v0.1.6: (1) no biprime verification of Paillier moduli, (2) range proofs verified in halves and never bound together, (3) blinding term drawn from too-small a range. Upstream fixes existed in tss-lib v2.0.0 (Aug 2023) and v3.0.0 (2024).
- Once the full vault key was reconstructed, attacker "sign[ed] and broadcast outbound transactions directly, bypassing the GG20 signing ceremony entirely" — **the attacker had the whole key**. This directly contradicts the corpus claim that "TSS signed real outbounds."
- EdDSA chains (SOL) unaffected; four other vaults untouched.

**Loss/chains:** $10.7M official (initial $7.4M). Assets: ~3,443 ETH, 36.85 BTC, 96.6 BNB, plus ~798K USDC early reports. Chains: BTC, ETH, BSC, Base (DefiLlama); TRM says at least nine chains ($11M+).

**Halt:** Automatic solvency-checker halts (>1% vault imbalance) within ~52 min; node operators stacked 720-block pauses from 09:08 UTC; Mimir votes: HALTTRADING, HALTSIGNING, HALTCHAINGLOBAL, HALTCHURNING. Corpus "Mimir used to set HALTTRADING and freeze" — **VERIFIED**.

**"3,156 ETH cold wallet":** PeckShield/Arkham reported 3,156 ETH moved to one address on the day. Both EVM attacker addresses are near-empty (0.001 and 0.21 ETH by RPC check on 2026-09-28) — funds were moved on.

**The ObservedTx bug is real but separate:** V12 Security reported on **2026-04-28** that `ObservedTx.GetSignablePayload()` signed only `Tx.Marshal()`, so `FinaliseHeight`/`BlockHeight` (and per MR 4820, the inbound/outbound bit) were unsigned; a CometBFT proposer could flip them in `PrepareProposal`. THORChain patched it: commit `af46db22` "fix(common): sign full ObservedTx wrapper to prevent proposer forgery" (authored 2026-05-06, tag `v3.18.0-disclosed` 2026-05-08); MR !4820 (created May 12, merged May 25). THORChain "maintains that the bug reported by V12 is unrelated to the May 15 incident." One outlet (cryip) and a dev.to post assert the proposer-forgery bug was the exploit — **neither is corroborated by THORChain, TRM, Chainalysis, or PeckShield**. The corpus's mechanism almost certainly conflates the V12 disclosure/patch with the actual exploit.

**Aftermath:** Patch v3.18.1 (May 19), v3.19.0 (June 5), v3.19.1 (June 16); trading resumed **June 23** after ~5-week halt. $10M treasury-funded refund pool + recovery portal (12,847 wallets). ADR-028 governance on recovery (bond slash of ~635K RUNE). Planned: migrate GG20 → DKLS (Silence Labs) / Schnorr (FROST), validator minimum age, per-validator keysign-failure monitoring, keyshare at-rest encryption. Bug bounty had been retired March 31, 2026.

Sources: blog.thorchain.org/thorchain-exploit-report-1; blog.thorchain.org/thorchain-exploit-report-2; gitlab.com/thorchain/thornode/-/merge_requests/4820; gitlab.com/thorchain/thornode/-/commit/af46db22bdfe0c6ce9ec5ee9f4178442318d8eff; github.com/v12-security/pocs/tree/main/thorchain/20260602; trmlabs.com/resources/blog/thorchain-exploit-drains-usd-11m-across-at-least-nine-chains-what-trm-knows-now; coindesk.com/tech/2026/05/15/thorchain-halts-trading-after-usd10-million-cross-chain-exploit-rune-token-drops-12; thedefiant.io/news/hacks/v12-says-thorchain-silently-patched-its-critical-bug-then-told-researchers-the-bounty-is; thedefiant.io/news/defi/thorchain-resumes-trading-after-month-long-halt-107m-exploit.

## 7. Grok/Bankr — 2026-05-04 — VERIFIED

May 4, 2026, Base. Wallet was a Bankr-operated "Grok wallet" (not xAI-controlled). Attacker first sent a **Bankr Club Membership NFT** which activated agentic permissions, then posted a **Morse-code** reply Grok decoded to a withdraw command; @bankrbot treated Grok's public reply as a command. ~3B DRB (~$150–204K; $175K commonly cited). SlowMist: "AI agent permission chain abuse". A **separate** Bankr incident on **May 19** (~$170K/14 wallets, "Session Key Compromised") and a Jul 2026 Bankr X-account takeover (~$480K). Recovery ~80–88%. "Deleted within minutes" partially sourced.

Sources: slowmist.medium.com/behind-the-grok-exploitation-an-analysis-of-ai-agent-permission-chain-abuse-4d832d1bfc73; cryptotimes.io/2026/05/04/xais-grok-ai-loses-175k-in-crypto-heist-via-clever-prompt-injection-then-gets-it-all-back/; beincrypto.com/grok-wallet-bankr-drb-prompt-injection; oecd.ai/en/incidents/2026-05-04-4a73.

## 8. TrustedVolumes / 1inch RFQ proxy — 2026-05-06 — VERIFIED

Blockaid flagged May 6, 2026 (Rekt/DefiLlama date May 7). Asset breakdown as corpus: 1,291.16 WETH, 206,282 USDT, 16.939 WBTC, 1,268,771 USDC = $5.87M (TrustedVolumes' own figure ~$6.7M). RFQ proxy `0xeEeEEe53033F7227d488ae83a27Bc9A9D5051756`; exploiter `0xC3EBDdEa4f69df717a8f5c89e7cF20C1c0389100`. Mechanism (Rekt/Verichains): (1) permissionless `registerAllowedOrderSigner()`; (2) signature validation keyed on the taker rather than the order maker; (3) broken replay protection. Rekt: "The contract verified who signed an order, but never once asked whether the signer had any right to spend the funds being moved." Not a 1inch protocol bug. **Same-operator claim:** Cointelegraph/The Block/Decrypt attribute it to Blockaid and researcher Vladimir Sobolev; no public address-linkage evidence published. Aftermath: July 18, 2026 attacker returned 1,122 ETH (~$2M), self-declared a $2M "bounty".

Sources: rekt.news/trustedvolumes-rekt; theblock.co/post/400332/1inch-trustedvolumes-exploit; cointelegraph.com/news/1inch-fusion-resolver-trusted-volumes-floats-bounty-after-67m-exploit; crypto.news/trustedvolumes-attacker-returns-2m-keeps-2m-bounty.

## 9. Aurellion Labs — 2026-05-12 — PARTIALLY VERIFIED (entry point mischaracterized)

Arbitrum One. Diamond `0x0adc63e71b035d5c7fdb1b4593999fa1f296f1b2`. Attacker EOA `0x9F49591a3bf95B49cD8d9477b4481Ce9da68d5Ca`; exploit tx `0x19cbafae517791e7e73403313d70440abf60558350e419df05c04f816998fe0a`. Root cause (Verichains): the protocol owner added a **SafeOwnable facet with `initialize(address)` but omitted the post-cut initializer call**, leaving OZ `_initialized` at zero → anyone could call `initialize()` and claim ownership. **Then** the attacker used ownership to `diamondCut` in a malicious facet exposing `pullERC20` (arbitrary `transferFrom` using existing user USDC allowances). Total 456,442.53 USDC: 450,999.72 from one victim. DefiLlama: "Uninitialized Proxy". **Same class as Renegade.**

Sources: blog.verichains.io/p/aurellion-labs-hack-analysis-diamond; hacked.slowmist.io/?c=Arbitrum; cryptotimes.io/2026/05/12/aurellion-labs-drained-of-455k-usdc-in-diamond-proxy-exploit/.

## 10. "Mass dormant-wallet drain" — 2026-04-30 — PARTIALLY VERIFIED (scale, duration, Permit2 wrong)

April 29–30, 2026, Ethereum mainnet. Hub `0xA707034429c8E4E01df056C0CbCf478F0FBeFAd7` (Etherscan label "Fake_Phishing2831105"). **500–570+ wallets**, ~591–596 transactions, ~261–326 ETH (~$600–800K). Duration **~12–13 hours**, peak 244 wallets in one hour. Wallet ages mostly 4–8 years dormant. Mechanism: **direct private-key compromise** — attacker signed native-ETH transfers itself; "unlike typical drainer-as-a-service scams… this operation pulled almost exclusively native ETH." **No Permit2 / no approvals involved.** Root cause unresolved (LastPass-2022 vault cracking, weak-entropy legacy generators, trading-bot key entry, supply chain are the leading theories). Laundered ~324.74 ETH via THORChain. No formal SlowMist/PeckShield analysis; no attribution.

Sources: cryptoslate.com/someone-drained-long-forgotten-ethereum-wallets-and-the-cause-may-trace-back-years/; cryptotimes.io/2026/05/01/mysterious-wallet-drains-326-eth-from-over-570-ethereum-addresses/; cryptopolitan.com/hundreds-of-ethereum-wallets-drained-after-years-of-no-activity/; recoveris.io/weekly-incident-report-april-27-may-3-2026.

## 11. Vercel / Context.ai breach — disclosed 2026-04-19 — VERIFIED (one embellishment)

Vercel KB bulletin first posted **April 19, 2026**. Chain: Feb 2026 — a Context.ai employee downloaded Roblox exploit scripts → **Lumma Stealer** → harvested Google Workspace creds/session tokens → Mar 2026 Context.ai found unauthorized **AWS** access and compromised **OAuth tokens** for AI Office Suite users → a Vercel employee had authorized Context.ai's Office Suite with broad Google Workspace scope → attacker used that token to take over the employee's Vercel Google Workspace account → their Vercel account → "enumerated and decrypted non-sensitive environment variables"; "sensitive"-flagged vars not read → limited subset of customers notified. Rauch: attacker "highly sophisticated based on their operational velocity" and "I strongly suspect, significantly accelerated by AI" (CyberScoop). Vercel never describes "SSO into internal systems"; the pivot was Google Workspace account takeover → the employee's Vercel account.

Sources: vercel.com/kb/bulletin/vercel-april-2026-security-incident; thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html; cyberscoop.com/vercel-security-breach-third-party-attack-context-ai-lumma-stealer; blog.gitguardian.com/vercel-april-2026-incident-non-sensitive-environment-variables-need-investigation-too/.

## 12. "x402 facilitator drains" — NOT FOUND

No public reporting of any rogue-facilitator or Permit2-allowance drain tied to x402 in April–May 2026, at any dollar scale. What exists: Coinbase's x402 ERC-20 extension (Mar 18, 2026) uses Permit2 for gasless payments on Base/Polygon; academic papers (arXiv 2605.30998; arXiv 2607.19545) document logic flaws and a controlled PoC that "stole no funds"; **402bridge** (Oct 28, 2025, ~$17.7K USDC, admin key leak) is the only x402-adjacent user drain on record. No DefiLlama entry, not in MetaMask's May 2026 report, Recoveris weekly reports, or SlowMist's Arbitrum archive. The $3.9M/$2.3M figures have no traceable public origin.

Sources: coinbase.com/developer-platform/discover/launches/x402-ERC20; arxiv.org/html/2605.30998v1; crypto.news/402bridge-hack-leads-to-over-200-users-drained-of-usdc; api.llama.fi/hacks.

## 13. "Private key drain" — 2026-05-11, 0xF7CFFC27 — NOT FOUND publicly; on-chain real but tiny

On-chain (eth.blockscout.com + public RPC, 2026-09-28): `0xF7cFFC27732a5C9c4E2D592F3E33435F8dDb019A` (nonce 7). On 2026-05-11 00:53–01:19 UTC: received 5.8 ETH and 157,340.65 `sat1` tokens from `0x62acE10c7f2Aa0e9B5a8e09CbF5D18d0f8a1EE8A`; sent 0.02 ETH back; approved sat1 to KyberSwap and swapped for ~4.3 ETH. The "victim" `0x62acE10c…EE8A` also received dust from multiple lookalike vanity addresses and sent fake "ETH" tokens to lookalikes — a classic address-poisoning/vanity-mimic cluster. Real value ≈ 5.8 ETH + a low-cap token (likely <$20K). The "key compromise" framing is not established (the victim sent funds itself; poisoning fits better). Not a notable public event.

## 14. Immunefi community response, April 18, 2026 — NOT FOUND

No Immunefi post, thread, blog, or press coverage dated April 18, 2026 about compositional/configuration findings and bounty scope. Immunefi's exclusion lists carry no April-2026 dated change. Nearest real events: the KelpDAO/LayerZero blame dispute (LayerZero statement Apr 19; Kelp rebuttals Apr 20 / May 5); Immunefi CEO Mitchell Amador's June 11, 2026 "vulnerability apocalypse" comments; THORChain retiring its own bounty (Mar 31, 2026).

Sources: immunefi.com/common-vulnerabilities-to-exclude; layerzero.network/blog/kelpdao-incident-statement; cointelegraph.com/news/frontier-ai-models-vulnerability-apocalypse-crypto-security-immunefi-ceo.

---

## Cross-cutting notes
1. **Biggest correction: THORChain.** Replace "consensus forgery / ObservedTx inbound-outbound bit" with GG20 TSS key-material leakage via malformed Paillier modulus + 864 deliberate MtA failures by a freshly churned validator; attacker reconstructed the full vault key and signed outbounds directly.
2. Volo (Sui key compromise), Wasabi (EVM deployer key → UUPS) are admin-key events. Juicebox (input validation), Thetanuts (first depositor) are not. Renegade and Aurellion are both uninitialized-proxy/facet takeovers.
3. Wasabi: same address from CREATE at nonce 0, not CREATE2; helper absent on Blast.
4. Dormant drain: hundreds of wallets over ~13h, native ETH via stolen keys, no Permit2.
5. Items 12–14 have no public footprint; item 13 is on-chain-real but trivial.
