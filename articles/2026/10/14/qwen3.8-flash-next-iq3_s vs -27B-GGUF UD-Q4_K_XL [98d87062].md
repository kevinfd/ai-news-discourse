---
id: "98d87062d63bbd59"
title: "qwen3.8-flash-next-iq3_s vs -27B-GGUF:UD-Q4_K_XL"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5vfs2/qwen38flashnextiq3_s_vs_27bggufudq4_k_xl"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T16:13:14Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["politerate"]
language: "en"
summary: "Sampling: temp 1.0, top_p 0.95, top_k 20 for both. Run with evalscope over the OpenAI-compatible API: Qwen3.8-Next on Strata (MI50 32GB), Qwen3.8-27B on llama.cpp (RX 7900 XTX 24GB). Caveat: These are only a portion of the full sets, since they take days. Edit1: Strata started with --kv fp16 and llama's default f16. Results Benchmark Next IQ3_S 27B UD-Q4_K_XL Only Next solved Only 27B solved…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 259
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5vfs2/qwen38flashnextiq3_s_vs_27bggufudq4_k_xl/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# qwen3.8-flash-next-iq3_s vs -27B-GGUF:UD-Q4_K_XL

Reddit · politerate · 2026-10-14

Sampling: temp 1.0, top_p 0.95, top_k 20 for both. Run with evalscope over the OpenAI-compatible API: Qwen3.8-Next on Strata (MI50 32GB), Qwen3.8-27B on llama.cpp (RX 7900 XTX 24GB). Caveat: These are only a portion of the full sets, since they take days. Edit1: Strata started with --kv fp16 and llama's default f16. Results Benchmark Next IQ3_S 27B UD-Q4_K_XL Only Next solved Only 27B solved AIME26 (30) 28 27 2 1 IFEval (50, prompt strict) 48 (0.960) 46 (0.920) 2 0 BFCL v4 (56) 49 (0.875) 47 (0.839) 4 2 LiveCodeBench v6 (30) 26 (0.867) 25 (0.833) 2 1 Total (166) 151 145 10 4 Sign test on the 14 problems only one model solved (10 vs 4): two-sided p = 0.18, so a lean toward Next rather than proof. Token limits Benchmark max_tokens AIME26 65,536 IFEval 16,384 BFCL v4 16,384 LiveCodeBench v6 63,488 Failures: wrong answer vs out of tokens Benchmark Next wrong Next out of tokens 27B wrong 27B out of tokens AIME26 0 2 1 2 IFEval 2 0 4 0 BFCL v4 7 0 9 0 LiveCodeBench v6 0 4 0 5 Total 9 6 14 7 BFCL v4 by category (7 per category) Category Next IQ3_S 27B UD-Q4_K_XL simple_python 1.000 1.000 multiple 1.000 0.857 parallel 0.857 0.857 parallel_multiple 0.714 0.857 irrelevance 1.000 1.000 live_simple 1.000 1.000 live_multiple 0.857 0.571 multi_turn_base 0.571 0.571 Speed (AIME + LiveCodeBench generation) 27B UD-Q4_K_XL Next IQ3_S Output tokens 1.34M 1.39M Generation time 7.8 h 10.5 h Speed 47.9 tok/s 36.8 tok/s Hardware RX 7900 XTX 24GB (llama.cpp) MI50 32GB (Strata)
