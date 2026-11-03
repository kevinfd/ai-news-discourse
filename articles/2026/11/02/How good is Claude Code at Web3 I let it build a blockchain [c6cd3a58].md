---
id: "c6cd3a5813c12380"
title: "How good is Claude Code at Web3? I let it build a blockchain"
url: "https://reddit.com/r/ClaudeAI/comments/1xm3d66/how_good_is_claude_code_at_web3_i_let_it_build_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xm3d66/how_good_is_claude_code_at_web3_i_let_it_build_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T17:23:01Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["regressiveparty"]
language: "en"
summary: "Every meme gets its own block. That was the one-line brief I gave Claude Code, and about three weeks later memechain is live. It’s free to try in your browser, no signup or installation needed. Live: https://larajeftic.github.io/memechain/ Source (MIT): https://github.com/larajeftic/memechain What it is A small Bitcoin-style chain where a meme is an inscription: the picture’s SHA-256 goes into a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 448
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xm3d66/how_good_is_claude_code_at_web3_i_let_it_build_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How good is Claude Code at Web3? I let it build a blockchain

Reddit · regressiveparty · 2026-11-02

Every meme gets its own block. That was the one-line brief I gave Claude Code, and about three weeks later memechain is live. It’s free to try in your browser, no signup or installation needed. Live: https://larajeftic.github.io/memechain/ Source (MIT): https://github.com/larajeftic/memechain What it is A small Bitcoin-style chain where a meme is an inscription: the picture’s SHA-256 goes into a signed transaction, a miner puts it into a block, and from then on the meme has one owner who can list it and sell it. Double SHA-256 proof of work, difficulty retarget every 10 blocks, 50 MEME per block with halving, secp256k1 wallets with RFC 6979 signatures. No gas, no real token, no money anywhere: MEME is a test token that is not sold and cannot be bought. I wanted to understand how an on-chain market actually works, not to launch a coin. The part I’m proud of The same consensus rules run twice. node.py (Python) runs the public testnet, and docs/chain.js runs the identical rules in your browser. You can create wallets, mine blocks, inscribe a picture, list it, let a test buyer mine for MEME and buy it, move 75% to a cold vault, and then replay your whole chain from genesis, checking every hash and signature. Export it as chain.json and the Python node validates it. npm test cross-checks that JS and Python agree on every hash. The public testnet runs without an always-on server. A GitHub Actions job runs the node every 20 minutes, mines a few blocks, inscribes memes from a public pool folder and pushes the export to a testnet branch. The static site reads it from there. Every 10th block hash is timestamped in Bitcoin using OpenTimestamps. Add a meme to the pool with a pull request and the bot inscribes it. How Claude was used All of it was written with Claude Code in the terminal, with me reviewing, testing and deciding. Things that worked well: Writing the Python node first, then asking for a line-by-line JS port with a cross-validation test, so every later change had to pass both Letting Claude run Playwright against the local page and look at the screenshots, then critique its own layout. Two design passes were thrown away The no-server testnet: Claude proposed the Actions-plus-branch trick when I said I didn’t want to run a server Things that didn’t work on the first try: the browser miner froze the UI until it moved to batched nonce loops, and the first block-time retarget overshot wildly on the 1-second browser chain until the clamp was added. Feedback welcome, especially on the consensus rules. And if you have a meme that deserves its own block, open a PR.
