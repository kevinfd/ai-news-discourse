---
id: "b9f75c115a3710bb"
title: "64GB isn't the dead zone anymore if you run agents"
url: "https://reddit.com/r/LocalLLaMA/comments/1xksj75/64gb_isnt_the_dead_zone_anymore_if_you_run_agents"
link: "https://reddit.com/r/LocalLLaMA/comments/1xksj75/64gb_isnt_the_dead_zone_anymore_if_you_run_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T03:02:34Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["M5_Maxxx"]
language: "en"
summary: "https://preview.redd.it/hboxdgjh2xyh1.png?width=1230&format=png&auto=webp&s=cca6b2b7b08807a334ff5280e19d96133667fbb0 The usual advice was that 64GB is a dead zone for local LLMs: too small for a 70B with real context, and more than a 30B needs. After running a 27B for agentic coding on a 64GB M4 Max for the last ten days, I think that has flipped. My memory usage is in the 50 GB as the context…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 348
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xksj75/64gb_isnt_the_dead_zone_anymore_if_you_run_agents/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 64GB isn't the dead zone anymore if you run agents

Reddit · M5_Maxxx · 2026-11-01

https://preview.redd.it/hboxdgjh2xyh1.png?width=1230&format=png&auto=webp&s=cca6b2b7b08807a334ff5280e19d96133667fbb0 The usual advice was that 64GB is a dead zone for local LLMs: too small for a 70B with real context, and more than a 30B needs. After running a 27B for agentic coding on a 64GB M4 Max for the last ten days, I think that has flipped. My memory usage is in the 50 GB as the context starts building up. Setup: Qwen3.8 27B (16 GB MLX quant) in LM Studio, 256k context, coding agent sessions that sit at 100-200k tokens. At 164k tokens, LM Studio's engine process is using 48 GB, 46 GB of it GPU memory. Roughly: - 16 GB weights - ~11 GB KV cache (~64 KB/token, only 16 of the 64 layers are full attention) - what looks like a second copy of the context for the prompt cache, plus the linear attention checkpoints - MLX holding on to scratch memory from prefill The prompt cache is what makes it usable. It's hitting 93%, so a turn processes about 1k new tokens instead of 160k. When it misses, a full prefill takes about 20 minutes. Why not quantize the KV cache like people do on a 24GB card? LM Studio's MLX vision path refuses KV quantization for this model. The text-only path allows it, but skips the cache checkpoints when the cache is quantized, and on a hybrid model that means a lot more full reprocessing. So on 48GB this doesn't fit unless you drop to ~128k context or move to llama.cpp with q8 KV (should be ~25-30 GB at 256k, with slower prefill). On 64GB it fits with nothing to spare. Free memory is about 150 MB right now. The dead zone argument was about weights. With agents, context costs about as much as the model, and 27B models are now good enough for real work. That puts 64GB right in the sweet spot. Bigger MoE models or two models loaded at once still want 128GB. Anyone else on 64GB seeing the same? And is anyone running long context on llama.cpp on a Mac with prefill speeds they're happy with?
