---
id: "08abc03215360f9e"
title: "Intel Arc Vulkan prefill got a dedicated FA kernel in llama.cpp master"
url: "https://reddit.com/r/LocalLLaMA/comments/1xumdj4/intel_arc_vulkan_prefill_got_a_dedicated_fa"
link: "https://reddit.com/r/LocalLLaMA/comments/1xumdj4/intel_arc_vulkan_prefill_got_a_dedicated_fa"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T19:35:39Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Polaris_debi5"]
language: "en"
summary: "We have a new dedicated Vulkan Flash Attention prefill kernel for Intel Arc and Xe, delivering massive prefill acceleration on supported platforms like ARL-H and Xe2/Xe3. This implementation leverages customized shaders to utilize Intel's native matrix core shapes and SLM architecture, including m16n16k16/SIMD32 support. To ensure stability, the kernel is currently enabled for these specific…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel", "Meta", "DeepSeek"]
topics: ["models & research"]
content_source: "post"
word_count: 340
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xumdj4/intel_arc_vulkan_prefill_got_a_dedicated_fa/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Intel Arc Vulkan prefill got a dedicated FA kernel in llama.cpp master

Reddit · Polaris_debi5 · 2026-11-12

We have a new dedicated Vulkan Flash Attention prefill kernel for Intel Arc and Xe, delivering massive prefill acceleration on supported platforms like ARL-H and Xe2/Xe3. This implementation leverages customized shaders to utilize Intel's native matrix core shapes and SLM architecture, including m16n16k16/SIMD32 support. To ensure stability, the kernel is currently enabled for these specific architectures while remaining disabled for others, like the A770, due to inconsistent test results. Additionally, backend refinements now extend these benefits to single-KV-head models like MQA and MLA. Platform Prefill Performance Comparison (pp8192) Platform Model Baseline (t/s) PR (t/s) ARL-H Windows qwen3 8B Q4_K 126.58 ± 0.48 415.31 ± 1.04 qwen35 27B Q4_K 83.38 ± 0.22 119.95 ± 0.07 qwen35moe 35B.A3B Q4_K 247.82 ± 0.65 394.44 ± 0.89 gpt-oss 20B Q4_K 478.14 ± 0.17 639.02 ± 0.70 PTL-H Windows qwen3 8B Q4_K 234.92 ± 0.39 911.60 ± 14.56 qwen35 27B Q4_K 194.93 ± 0.59 264.39 ± 0.38 qwen35moe 35B.A3B Q4_K 632.12 ± 17.56 914.80 ± 67.39 gpt-oss 20B Q4_K 804.70 ± 84.56 1357.34 ± 125.30 B70 Pro Windows qwen3 8B Q4_K 1064.67 ± 4.37 2955.83 ± 1.87 qwen35 27B Q4_K 659.10 ± 0.11 932.13 ± 0.63 qwen35moe 35B.A3B Q4_K 2088.50 ± 3.32 3005.11 ± 4.24 gpt-oss 20B Q4_K 2311.37 ± 2.56 3967.29 ± 6.77 B70 Pro Linux qwen3 8B Q4_K 783.67 ± 0.20 1518.19 ± 1.05 qwen35 27B Q4_K 497.22 ± 1.17 647.78 ± 2.44 qwen35moe 35B.A3B Q4_K 1060.55 ± 5.09 1311.62 ± 7.55 gpt-oss 20B Q4_K 1237.51 ± 2.16 1841.35 ± 3.78 Intel Arc B580: Detailed Model Benchmarks (FA1) Comparison of f16 Prefill (pp16384) performance Model Baseline $rightarrow$ PR $Delta$% Gemma4 E4B Q4_K_M 115.98 -» 1156.62 +897.3% Phi-3.5-mini Q4_K_M 384.45 -» 932.90 +142.7% Granite 4.2 8B Q4_K_M 282.67 -» 520.98 +84.3% DeepSeek-R1-Qwen3-8B Q5_K_M 306.88 -» 559.34 +82.3% Llama 3.1 8B Q4_K_M 347.79 -» 633.73 +82.2% Ministral-3-8B Q5_K_M 324.17 -» 590.91 +82.3% Qwen3.5-9B Q6_K 687.50 -» 979.49 +42.5% Gemma3 4B Q4_1 1414.61 -» 1948.23 +37.7% Granite 4.0-h-tiny Q4_K_M 2503.03 -» 2927.33 +16.95% Ling-3.0-tiny (hkv=1) 76 -» 1239 +1530.3% Gemma4 12B (hkv=1) 52 -» 649 +1144.2%
