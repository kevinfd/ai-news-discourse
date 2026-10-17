---
id: "e74466f7ff446a8e"
title: "vLLM finally working on 4 x Intel B70, QFN 3.8 FP8"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7yxxl/vllm_finally_working_on_4_x_intel_b70_qfn_38_fp8"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7yxxl/vllm_finally_working_on_4_x_intel_b70_qfn_38_fp8"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T02:33:05Z"
published_date: "2026-10-17"
collected_at: "2026-10-17T12:05:45Z"
authors: ["38andstillgoing"]
language: "en"
summary: "I think it's all working. I asked various models to make it all work for me, with the bulk being GLM 5.3 flash. Its not as fast as some of the benchmarks I've found but getting them working apparently requires even more surgery. I wanted a simple \"Qwen 3.8 Flash Next FP8 MTP 256k context, 128GB VRAM in 4x Intel B70, 128GB RAM, vLLM in a container. Fully reproducable.\" According to the LLM tests:…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel", "Alibaba"]
topics: []
content_source: "post"
word_count: 129
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7yxxl/vllm_finally_working_on_4_x_intel_b70_qfn_38_fp8/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# vLLM finally working on 4 x Intel B70, QFN 3.8 FP8

Reddit · 38andstillgoing · 2026-10-17

I think it's all working. I asked various models to make it all work for me, with the bulk being GLM 5.3 flash. Its not as fast as some of the benchmarks I've found but getting them working apparently requires even more surgery. I wanted a simple "Qwen 3.8 Flash Next FP8 MTP 256k context, 128GB VRAM in 4x Intel B70, 128GB RAM, vLLM in a container. Fully reproducable." According to the LLM tests: 450 t/s prefill, 20 t/s generation. The LLM found and made or backported fixes for several 2 32 overflows causing random weird crashes and it all seems stable now.... maybe. Edit: Added context. https://github.com/wormley/B70_Quad/tree/master/qfn-38-fp8-4xb70-mtp Before this all my manual vLLM testing ended in crashes for almost every model trying to run on multiple B70 cards.
