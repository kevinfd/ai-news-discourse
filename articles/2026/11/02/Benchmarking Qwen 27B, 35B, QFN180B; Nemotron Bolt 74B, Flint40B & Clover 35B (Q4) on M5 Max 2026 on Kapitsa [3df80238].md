---
id: "3df8023857a5dab0"
title: "Benchmarking: Qwen 27B, 35B, QFN180B; Nemotron Bolt 74B, Flint40B & Clover 35B (Q4) on M5 Max 2026 on Kapitsa with KFlash [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xljter/benchmarking_qwen_27b_35b_qfn180b_nemotron_bolt"
link: "https://reddit.com/r/MachineLearning/comments/1xljter/benchmarking_qwen_27b_35b_qfn180b_nemotron_bolt"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T01:05:33Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["DotaMate"]
language: "en"
summary: "https://preview.redd.it/260fkihtk3zh1.png?width=2400&format=png&auto=webp&s=a80b6861abdeee3c9a4e705b6ad9b337be005722 hey folks, I'm Ye, one of the contributors to Kapitsa, an open-source inference engine optimized specifically for Apple Silicon to run Qwen, Nemotron, Flint and Clover models locally. Our custom-written Metal kernels let us tune for each chip and each model.…"
tags: ["r/MachineLearning"]
orgs: ["Apple", "Alibaba", "OpenAI", "Anthropic"]
topics: ["models & research", "chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 662
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xljter/benchmarking_qwen_27b_35b_qfn180b_nemotron_bolt/"
score: null
comments: null
community: "r/MachineLearning"
---

# Benchmarking: Qwen 27B, 35B, QFN180B; Nemotron Bolt 74B, Flint40B & Clover 35B (Q4) on M5 Max 2026 on Kapitsa with KFlash [P]

Reddit · DotaMate · 2026-11-02

https://preview.redd.it/260fkihtk3zh1.png?width=2400&format=png&auto=webp&s=a80b6861abdeee3c9a4e705b6ad9b337be005722 hey folks, I'm Ye, one of the contributors to Kapitsa, an open-source inference engine optimized specifically for Apple Silicon to run Qwen, Nemotron, Flint and Clover models locally. Our custom-written Metal kernels let us tune for each chip and each model. https://github.com/nace-ai/kapitsa/ The latest update, 0.2.26, is out. Since our last M5 Max numbers, Flash-Next 180B reads prompts 46% faster and the 27B writes 8% faster, and DiffuSpace's Clover 35B joins the catalog. Kapitsa also runs Qwen Flash-Next 180B with SSD offloading : on a Mac that can't hold it, the experts that don't fit in RAM stream from the SSD, so it runs on a 48 GB MacBook Pro at 61 tok/s. Here are the end-to-end numbers on a 2026 MacBook Pro 16 with an M5 Max and 128 GB: six targets (dense, MoE, hybrid Mamba-2 MoE and a block-diffusion MoE), from 1K context up to 32K, against the next-fastest engine for each. Try it (any Apple Silicon Mac; models in this post: 35b , 27b , flash-next , bolt , flint , clover ): brew install nace-ai/tap/kapitsa kapitsa serve --model 35b # OpenAI and Anthropic APIs on localhost kapitsa opencode --model 35b # or claude, codex, pi kapitsa bench # benchmark your own Mac Results Decode is a 512-token coding answer, prefill a 4K prompt, median of 3 runs: Model Decode, tok/s Prefill, tok/s Qwen3.6 35B-A3B 346 6,036 Clover 35B-A3B 304 5,981 Flint 40B 265 5,770 Nemotron Bolt 74B 154 1,075 Qwen3.8 27B 143 904 Qwen Flash-Next 180B 108 1,701 https://preview.redd.it/r1t8d4jtk3zh1.png?width=2400&format=png&auto=webp&s=6f707ed68fe883ddf206de9e30e5f94cef4bd738 From 1K context all the way up to 32K. At 32K the 35B still writes 175 tok/s, and Flash-Next barely drops (90 to 78): https://preview.redd.it/hxod2sktk3zh1.png?width=2400&format=png&auto=webp&s=9703ef7d4356cac43d685cf5e284a60a51764786 https://preview.redd.it/b2wqfimtk3zh1.png?width=2400&format=png&auto=webp&s=fd2da7b94e354af519fde41fbdaede61aa6df883 Against the other engines Against the next-fastest engine for each model on the same Mac: 1.23x Splash on the 35B, 2.2x oMLX on Bolt, 1.18x rec on Flint and 1.12x mlx-serve on the 27B. Flash-Next is a tie with mlx-serve, Splash still reads prompts faster on the two Qwens, and nothing else runs Clover on a Mac. https://preview.redd.it/zpjhe6otk3zh1.png?width=2400&format=png&auto=webp&s=2bf9bbc25c8231fcc1376e9f9efcf8d024914cea Every cell with versions and flags: benchmarks . Raw runs: results . Why it's fast: KFlash Other engines verify the drafter's guesses as one chain and stop at the first miss. KFlash verifies a best-first tree of the drafter's candidates in the same 8-row pass and keeps the longest branch the target agrees with. https://preview.redd.it/sle8vzptk3zh1.png?width=1200&format=png&auto=webp&s=c2e4afec6cad457c34108beab8824353c0123514 Three details make it fit Apple silicon: Nearly free rows. Apple GPUs work in 8-row tiles, so on dense models an 8-row verify costs about 1.1-1.25x one decode step. Sized per Mac. Each tree is sized cycle by cycle from a budget measured on that Mac: GPU time per row count, plus a per-position calibration of the drafter against its own acceptances. Seed-exact. A guess is accepted only if it equals the token the target itself samples with plain decoding's random number, so a sampled reply is the one plain sampling writes with the same seed. Write-up and measurements Send us your benchmarks Run the same test on your Mac and add it to the community results . It takes 3-15 minutes: brew install nace-ai/tap/kapitsa brew install gh && gh auth login # results are sent as a GitHub pull request kapitsa bench --submit # pick a model; it asks before sending anything Plug in and close heavy apps while it runs. At the end it asks once: Enter sends the result as a pull request from your GitHub fork, and n keeps it on your Mac. What it sends is about 2 KB: your Mac's model, chip, RAM, macOS version and the numbers, with no serial number, user name or paths (add --dry-run to see exactly what it would send). No GitHub? Paste the numbers it prints in a comment here. One more ask Do you know prior work where tree-verified sampling matches plain sampling token for token under the same seed? Please point me to it so we credit it. We cite SpecInfer, Medusa, EAGLE-2 and Sequoia.
