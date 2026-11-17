---
id: "bcf17bff4d1da36c"
title: "Strix Halo int4 cores: Gemma 4 31B at 2.43x llama.cpp, same quality"
url: "https://reddit.com/r/LocalLLaMA/comments/1xygpmv/strix_halo_int4_cores_gemma_4_31b_at_243x"
link: "https://reddit.com/r/LocalLLaMA/comments/1xygpmv/strix_halo_int4_cores_gemma_4_31b_at_243x"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T10:08:06Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["No-Dragonfly6246"]
language: "en"
summary: "The 8060S has an int4 x int4 WMMA instruction at 2x the FP16 rate (we measured 104 TOPS). Nothing in ROCm or llama.cpp uses it. We wrote a GEMM for it and run Gemma 4 with int4 weights and int4 activations. To maintain accuracy we use a combination of rotation and GPTQ, along with selective mixed precision. llama-bench, Gemma 4 31B QAT Q4_0 (llama.cpp b11056 Vulkan, -fa 1). Server benchmark,…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 157
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xygpmv/strix_halo_int4_cores_gemma_4_31b_at_243x/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strix Halo int4 cores: Gemma 4 31B at 2.43x llama.cpp, same quality

Reddit · No-Dragonfly6246 · 2026-11-17

The 8060S has an int4 x int4 WMMA instruction at 2x the FP16 rate (we measured 104 TOPS). Nothing in ROCm or llama.cpp uses it. We wrote a GEMM for it and run Gemma 4 with int4 weights and int4 activations. To maintain accuracy we use a combination of rotation and GPTQ, along with selective mixed precision. llama-bench, Gemma 4 31B QAT Q4_0 (llama.cpp b11056 Vulkan, -fa 1). Server benchmark, 2k-token prompts, greedy, single stream: pp512 pp2048 llama.cpp 287 276 ours 679 724 Full test sets, same settings, 31B: GSM8K IFEval MMLU-Pro llama.cpp 96.2 92.2 85.1 ours 96.4 91.7 85.1 Run it: curl -fsSL https://embedl.com/install.sh | sh && export PATH="$HOME/.local/bin:$PATH" embedl login embedl serve google/gemma-4-31B-it/ryzen-ai-max-395 -d embedl infer google/gemma-4-31B-it/ryzen-ai-max-395 --prompt "Explain mixture-of-experts in one sentence." embedl bench google/gemma-4-31B-it/ryzen-ai-max-395 12B, E4B and E2B are up too (2.80x / 1.58x / 1.39x end to end, in the chart). Swap the name, e.g. google/gemma-4-12B-it/ryzen-ai-max-395 . Model, methodology, and more: https://www.embedl.com/google/gemma-4-31B-it/ryzen-ai-max-395
