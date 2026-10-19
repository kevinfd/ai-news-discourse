---
id: "533e6a680dd2e1e8"
title: "Don't sleep on Nemotron 3.5 Super VL"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9mwmz/dont_sleep_on_nemotron_35_super_vl"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9mwmz/dont_sleep_on_nemotron_35_super_vl"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T04:01:26Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Kahvana"]
language: "en"
summary: "Hey everyone, One of the benchmarks I run for myself is to check obscure knowledge, like game rules from Anno 1602 (a game from 1998) and it's (many confusing) editions. Websearch is not permitted. So far, it has come the closest for me in niche information. Ranking order (1 highest, 6 lowest): Nemotron 3.5 Super VL 120B-A12B: Hallucionated salt for citizen to merchant, left out church for…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Nvidia"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 236
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9mwmz/dont_sleep_on_nemotron_35_super_vl/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Don't sleep on Nemotron 3.5 Super VL

Reddit · Kahvana · 2026-10-19

Hey everyone, One of the benchmarks I run for myself is to check obscure knowledge, like game rules from Anno 1602 (a game from 1998) and it's (many confusing) editions. Websearch is not permitted. So far, it has come the closest for me in niche information. Ranking order (1 highest, 6 lowest): Nemotron 3.5 Super VL 120B-A12B: Hallucionated salt for citizen to merchant, left out church for settlers, left out required landmarks for merchant and aristocrat Gemma 4 31B IT QAT: Omitted too many parts of the upgrade requirements DeepSeek v4 Flash Vision Exp: Hallucionated different upgrade requirements Qwen3.5-122B-A12B: Hallucionated game editions and upgrade requirements Qwen3.8-flash-next: Hallucionated game editions and upgrade requirements GPT-OSS 120B: Hallucionated game editions and upgrade requirements Compared to the other models, that's a huge improvement! Basically from totally inaccurate to only minor mistakes. The model itself (unsloth's quants, NVFP4) runs at ~8-10 t/s generation and ~150-170 t/s processing on dual RTX 5060 Ti 16GB with dual 48GB DDR5-6000MHz, no MTP, layer split, vulkan. Seems like it's a good model to keep. Also crazy how capable Germma 4 31B IT QAT is. [EDIT] inference engine and models used: llama.cpp 0.7.0, used with models: https://github.com/ggml-org/llama.cpp/releases?page=4#release-b11669 MXFP4 for GPT-OSS-120B: https://huggingface.co/bartowski/openai_gpt-oss-20b-GGUF Q4_K_S for Qwen3.5-122B-A10B: https://huggingface.co/unsloth/Qwen3.5-122B-A10B-MTP-GGUF Q4_K_XL for Qwen3.8-flash-next: https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF Q2_K_XL for DeepSeek v4 Flash Vision Exp: https://huggingface.co/unsloth/DeepSeek-V4-Flash-Vision-Exp-GGUF QAT + MTP (Q4_0) for Gemma 4 31B IT QAT: https://huggingface.co/unsloth/gemma-4-31B-it-qat-GGUF NVFP4 for Nemotron 3.5 Super VL 120B-A12B: https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF
