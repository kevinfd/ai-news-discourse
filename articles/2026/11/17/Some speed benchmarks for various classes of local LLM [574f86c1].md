---
id: "574f86c1b59aa49a"
title: "Some speed benchmarks for various classes of local LLM"
url: "https://reddit.com/r/LocalLLaMA/comments/1xy5yn4/some_speed_benchmarks_for_various_classes_of"
link: "https://reddit.com/r/LocalLLaMA/comments/1xy5yn4/some_speed_benchmarks_for_various_classes_of"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T00:20:35Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Icaruswept"]
language: "en"
summary: "Model Active config 4080 decode (tok/s) 4080+3080 decode (tok/s) 4080 prefill (tok/s) 4080+3080 prefill (tok/s) LFM2.5-24B-A2B UD-Q4_K_XL 4080+3080 249 250 5,530 7,930 MiniCPM-V 4.7 35B-A3B Q4_K_M 4080+3080 177 165 1,305 2,500 Flint 40B-A2.5B UD-Q4_K_XL 4080+3080 119 138 1,563 1,380 Swift 1.5 (Qwen3.8-Flash-Next) IQ2_XS 4080 117 116 1,070 679 Qwen3.8-Flash-Next IQ3_S 4080 79 87 730 465 GLM 5.3…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "DeepSeek", "Anthropic", "Alibaba", "AMD"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 372
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xy5yn4/some_speed_benchmarks_for_various_classes_of/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Some speed benchmarks for various classes of local LLM

Reddit · Icaruswept · 2026-11-17

Model Active config 4080 decode (tok/s) 4080+3080 decode (tok/s) 4080 prefill (tok/s) 4080+3080 prefill (tok/s) LFM2.5-24B-A2B UD-Q4_K_XL 4080+3080 249 250 5,530 7,930 MiniCPM-V 4.7 35B-A3B Q4_K_M 4080+3080 177 165 1,305 2,500 Flint 40B-A2.5B UD-Q4_K_XL 4080+3080 119 138 1,563 1,380 Swift 1.5 (Qwen3.8-Flash-Next) IQ2_XS 4080 117 116 1,070 679 Qwen3.8-Flash-Next IQ3_S 4080 79 87 730 465 GLM 5.3 Flash Maya-S24 IQ2_XXS_S 4080+3080 6.8 8.8 79 42 DeepSeek V4 Flash UD-IQ2_XXS 4080+3080 15.9 18.2 38 53 Decode: the second of two 300-token runs, with the expert cache warm (the first request after loading is often slower) Prefill: the average of two runs on a prompt of about 1,400 tokens Bold: the better config for that column. Morning, everyone. I've seen a lot of posts wondering about what can be run with what, so I made this table of the models on my system. Specifically because of the unorthodox results when it comes to Qwen Flash-Next, where one 16 GB card (the 4080 Super) significantly outperforms two in prefill. My hardware is as follows: CPU AMD Ryzen 7 5800X3D @ 3.40 GHz GPU NVIDIA GeForce RTX 4080 SUPER [Discrete] GPU NVIDIA GeForce RTX 3080 [Discrete] (got it secondhand for cheap, so why not) RAM 62.72 GB at 3200 Mhz I'm running these models on PolyStrata. I used to have a combination of Maya and Strata, but got tired of running different things all derived from the same fork (plus Strata seems to be getting increasingly unintuitive), and so moved everything to PS. Now: why Q3? It's a generally held opinion that anything below Q4 is crap, which was true of most earlier generation models. However, benchmarks measure deviation from the base, and not necessarily task fitness. In actual use, the only real way to know is to test it yourself. The Swift finetune of QWN at Q2, for example, is fast and excellent at data extraction, search, and piloting scripts written by more competent models. The IQ3 is a decent coder, roughly on par with Haiku for the use cases I've tried. The GLM and Deepseek Q2 variants are a bit better - verging on older Sonnet territory, I'd say, and do very well as subagents for Claude. YMMV. Hope this data is useful. Enjoy!
