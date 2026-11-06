---
id: "08e7e63415aa0842"
title: "Strata for all Qwen models from little to big"
url: "https://reddit.com/r/LocalLLaMA/comments/1xottw2/strata_for_all_qwen_models_from_little_to_big"
link: "https://reddit.com/r/LocalLLaMA/comments/1xottw2/strata_for_all_qwen_models_from_little_to_big"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T20:47:30Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Serious_Scarcity7818"]
language: "en"
summary: "Ran every Qwen GGUF on my disk through RustingStrata and llama.cpp, same PC, same file, back to back. PC: RTX 3060 12 GB, Ryzen 5 7600X, 32 GB RAM. CUDA. Normal desktop open (browser, Discord), no tuning, so numbers are lower than in the README. Model Quant Size Prefill 4K, RustingStrata Prefill 4K, llama.cpp Decode after 4K, RustingStrata Decode after 4K, llama.cpp Qwen3.5-2B Q8_0 1.9 GB 3859…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 262
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xottw2/strata_for_all_qwen_models_from_little_to_big/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strata for all Qwen models from little to big

Reddit · Serious_Scarcity7818 · 2026-11-05

Ran every Qwen GGUF on my disk through RustingStrata and llama.cpp, same PC, same file, back to back. PC: RTX 3060 12 GB, Ryzen 5 7600X, 32 GB RAM. CUDA. Normal desktop open (browser, Discord), no tuning, so numbers are lower than in the README. Model Quant Size Prefill 4K, RustingStrata Prefill 4K, llama.cpp Decode after 4K, RustingStrata Decode after 4K, llama.cpp Qwen3.5-2B Q8_0 1.9 GB 3859 6080 96.1 89.8 Qwen3-4B-Instruct-2507 Q4_K_M 2.3 GB 1433 2482 57.4 59.7 Qwen3.8-27B (Swift-1.5) IQ2_XXS 8.3 GB 283 459 16.5 14.7 Qwen3-30B-A3B-Instruct-2507 UD-Q2_K_XL 11 GB 1236 1545 63.6 52.9 Qwen3.6-35B-A3B UD-Q2_K_XL 11.7 GB 1539 1029 71.5 39.6 Qwen3-Next-80B-A3B-Instruct UD-IQ1_S 21 GB 1154 739 63.7 33.3 Qwen3.8-Flash-Next (177B) IQ2_XS 63 GB 305 193 21.3 18.1 All numbers tok/s, mean of 2 runs. Short version: small dense models, llama.cpp still prefills faster. Once the model is bigger than VRAM (35B, 80B, 177B on a 12 GB card), Strata is ~1.5x on prefill and up to ~2x on decode. 80B at 64 tok/s and a 177B model at 21 tok/s on a 3060 with 32 GB RAM. Commands: - Strata: strata bench --model X --gpu --mtp 0 --pp 4096 --tg 128 --reps 2 - llama.cpp (build 12119): llama-bench -m X -p 4096 -n 128 -d 4096 -fa on -ub 2048 -b 2048 -fitt 512 (its auto-fit to VRAM) MTP is off here. With MTP on, 35B goes up to ~160 tok/s decode. Hand-tuned llama.cpp ( -ncmoe 12 ) on a quiet machine does better on 35B (~2236 prefill / 68 decode), see the README for that comparison. Repo: RustingStrata
