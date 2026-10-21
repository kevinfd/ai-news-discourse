---
id: "f481f6e44d7a6a7e"
title: "KFlash: Benchmarks of newly released versions of Apple Silicon optimized engines: 1.4.0 Splash (DFlash2 ~ 50 tok/s) vs 0.2 Kapitsa (KFlash ~65 tok/s), MLX(MTP) & more on Qwen 3.8 27b/4b/35b 4Q on Macbook Pro M4 Pro 48 GB 2024, 48GB & Macbook Pro M1 Pro 16GB 2021"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbdxg3/kflash_benchmarks_of_newly_released_versions_of"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbdxg3/kflash_benchmarks_of_newly_released_versions_of"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T04:47:12Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["DotaMate"]
language: "en"
summary: "hey folks, its Ye, I work on an open source project called Kapitsa : its a fast Apple Silicon optimized inference engine built for Qwen and Nemotron models. this week two new releases landed in local inference: Inco shipped Splash 1.4.0 yesterday, and we shipped Kapitsa 0.2 today with a new speculative decoding method we call KFlash. so we put the newest versions next to the other engines people…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Apple", "Anthropic", "OpenAI", "Nvidia", "DeepSeek"]
topics: ["models & research", "products & launches", "chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 555
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbdxg3/kflash_benchmarks_of_newly_released_versions_of/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# KFlash: Benchmarks of newly released versions of Apple Silicon optimized engines: 1.4.0 Splash (DFlash2 ~ 50 tok/s) vs 0.2 Kapitsa (KFlash ~65 tok/s), MLX(MTP) & more on Qwen 3.8 27b/4b/35b 4Q on Macbook Pro M4 Pro 48 GB 2024, 48GB & Macbook Pro M1 Pro 16GB 2021

Reddit · DotaMate · 2026-10-21

hey folks, its Ye, I work on an open source project called Kapitsa : its a fast Apple Silicon optimized inference engine built for Qwen and Nemotron models. this week two new releases landed in local inference: Inco shipped Splash 1.4.0 yesterday, and we shipped Kapitsa 0.2 today with a new speculative decoding method we call KFlash. so we put the newest versions next to the other engines people here run, on a couple of macs people actuall yuse not some 128gb M5 Ultra xd, same opencode like harness. https://github.com/nace-ai/kapitsa whats KFlash: most fast engines now use a small draft model that guesses the next ~7 tokens, and the big model checks them in one pass. DFlash2 as published checks one chain of guesses and stops at the first wrong one. KFlash checks a best-first tree of the drafter's candidates in that same pass, so when the drafter hesitates its runnerup guesses get checked. more details here https://github.com/nace-ai/kapitsa/blob/main/docs/kflash.md the numbers (i dont trust benchmarks myself, neither should you, run kapitsa bench on your own Mac, it will allow you to submit your bench to our repo so we all could see the performance of kapitsa from across different machines. decode tok/s of a 512-token coding answer, T 0.6, median of 5 runs, 4-bit weights, each engine in its fastest setup: MacBook Pro M4 Pro (2024), 48GB: engine version Qwen3.8 27B Qwen3.6 35B-A3B Qwen3.5 4B Kapitsa 0.2 63 tok/s KFlash 161 tok/s KFlash 201 tok/s KFlash Splash 1.4.0 53 DFlash2 135 DFlash2 ✗ mlx-serve 26.10.2 54 DFlash2 124 MTP 137 MTP oMLX 0.7.1rc1 45 DFlash2 127 DFlash2 102 MTP Ollama 0.40.5 / 0.40.6 32 MTP 89 MTP 109 MTP MTPLX 2.12.2 36 MTP 80 MTP 104 MTP MLX (mlx-vlm 0.7.8) 28 MTP 86 DFlash2 88 MTP llama.cpp b11669 18 MTP 69 MTP 70 MTP LM Studio MLX runtime 1.13.1 15 no spec 86 no spec 81 no spec MacBook Pro M1 Pro (2021), 16GB: Qwen3.5 4B (the 27B is ~15GB of weights and the 35B ~19GB, they don't fit 16GB) engine version Qwen3.5 4B Kapitsa 0.2 95 KFlash mlx-serve 26.10.2 62 MTP oMLX 0.7.1rc1 55 MTP Ollama 0.40.6 55 MTP LM Studio MLX runtime 1.13.1 47 no spec MLX (mlx-lm) 0.32.2 46 no spec MTPLX 2.12.2 42 MTP llama.cpp b11669 38 MTP Splash 1.4.0 ✗ (needs an M3 or newer) quickstart. Kapitsa serves OpenAI Anthropic compatable API along with a really simple CLI that allows it to run Kapitsa w Opencode/Pi/Claude etc. brew install nace-ai/tap/kapitsa # or: curl -fsSL https://raw.githubusercontent.com/nace-ai/kapitsa/main/install.sh | bash kapitsa claude --model 27b # or kapitsa claude, kapitsa codex, etc kapitsa bench runs this same benchmark on your Mac, and kapitsa bench --submit adds it to the community results (shows the JSON and asks first). M2/M3 Macs and 16-36GB ones are the results we want most things to mention Splash runs the 27B and 35B (and Flash-Next GGUFs) and needs an M3 or newer, Kapitsa works on all M chips M1 to M6 vibecode, expect bugs. issues/PRs welcome \ ^) credits DeepSeek (DSpark), Inco(DFlash2) (a really solid engine, go compare it), z-lab (DFlash), NVIDIA (LiLiCorr and the Nemotron checkpoints), Qwen (MTP heads), MLX, mlx-serve, oMLX, MTPLX, Ollama, llama.cpp and LM Studio folks. Fable 5.1, Opus 5.5 and Nace.AI coding models asks try it, bench it, break it, upload your benches please \ ^)
