---
id: "5c8d4ff3b98433a6"
title: "DeepSeek V4.1 Flash 1017 on 2x DGX Spark: 57 tok/s text, 92 tok/s code with TensorFold (2.1-2.3x the vLLM kit)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8q6t6/deepseek_v41_flash_1017_on_2x_dgx_spark_57_toks"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8q6t6/deepseek_v41_flash_1017_on_2x_dgx_spark_57_toks"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T01:00:38Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["shayanx45"]
language: "en"
summary: "**TL;DR:** DeepSeek-V4.1-Flash-1017 (EXL3 2.9bpw, 1M context) on 2x DGX Spark, TP=2 over the CX7 cable. TensorFold is 2.1-2.3x faster than the vLLM kit on the same pair, same weights, same prompts, same day. vLLM kit TensorFold Decode, text 27.0 tok/s **56.8 tok/s** Decode, code 39.9 tok/s **92.2 tok/s** Needle in 64K 80.4 s **35.9 s** 4 requests, code, total 1 at a time **140 tok/s** Cold…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["models & research"]
content_source: "post"
word_count: 233
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8q6t6/deepseek_v41_flash_1017_on_2x_dgx_spark_57_toks/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# DeepSeek V4.1 Flash 1017 on 2x DGX Spark: 57 tok/s text, 92 tok/s code with TensorFold (2.1-2.3x the vLLM kit)

Reddit · shayanx45 · 2026-10-18

**TL;DR:** DeepSeek-V4.1-Flash-1017 (EXL3 2.9bpw, 1M context) on 2x DGX Spark, TP=2 over the CX7 cable. TensorFold is 2.1-2.3x faster than the vLLM kit on the same pair, same weights, same prompts, same day. vLLM kit TensorFold Decode, text 27.0 tok/s **56.8 tok/s** Decode, code 39.9 tok/s **92.2 tok/s** Needle in 64K 80.4 s **35.9 s** 4 requests, code, total 1 at a time **140 tok/s** Cold prefill (random-word prompts, no cache hit, bertholomus's kit_bench client), measured tonight: Prompt vLLM kit TensorFold 8K 789 tok/s **~2,075 tok/s** 32K 925 tok/s **2,080-2,185 tok/s** 64K ~800 tok/s **2,010-2,040 tok/s** 128K n/a **~1,900 tok/s** 1M (1,034,753 tokens) n/a **1,246 tok/s** (needle found) So roughly 2.2-2.4x vLLM on prefill too. A second question on the same 24K doc starts in ~1.1 s (prompt cache). Some of these come from host tuning I found tonight (swap off for the engine, less kernel compaction). It lands in the repo in the next update. bertholomus's engine publishes ~2,400 at 32K, and I'm still closing that gap. forced tool calls (`tool_choice` required / named) * json_schema / regex / choice output, 4 requests at once * one bad request no longer takes down the server **Also:** the prompt cache survives a restart (an 18K-token conversation resumes in 2.7 s instead of 16.8 s). [Recipe on GitHub]( https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark ) [HF card]( https://huggingface.co/Elevatormusic/DeepSeek-V4.1-Flash-1017-2x-DGX-Spark-TensorFold-2x-Faster ) **Credit:** the fast engine is [bertholomus's V4.1 port]( https://github.com/bertholomus/deepseek-v4.1-tensorfold-tp2-2xgb10 ).
