---
id: "b1b1271dc03a1458"
title: "Calling all GPUs: help us benchmark SonicBoom v0.0.3 — a compiler-first AI runtime that beats llama.cpp on decode"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9mitw/calling_all_gpus_help_us_benchmark_sonicboom_v003"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9mitw/calling_all_gpus_help_us_benchmark_sonicboom_v003"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T03:40:00Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["nalaginrut"]
language: "en"
summary: "Hi folks! We are HardenedLinux, an old-school free software community. SonicBoom is our open-source (GPLv3) inference runtime: a compiler-first alternative to the usual Python stack. No Python at build or run time — one shared library, a C ABI, and Guile Scheme as the first-class language. What v0.0.3 does on a desktop RTX 3050 8 GB (same session, same GGUF, vs llama.cpp -ngl 99): model decode…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "Alibaba"]
topics: ["models & research", "chips & infrastructure", "jobs & society", "agents & coding"]
content_source: "post"
word_count: 239
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9mitw/calling_all_gpus_help_us_benchmark_sonicboom_v003/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Calling all GPUs: help us benchmark SonicBoom v0.0.3 — a compiler-first AI runtime that beats llama.cpp on decode

Reddit · nalaginrut · 2026-10-19

Hi folks! We are HardenedLinux, an old-school free software community. SonicBoom is our open-source (GPLv3) inference runtime: a compiler-first alternative to the usual Python stack. No Python at build or run time — one shared library, a C ABI, and Guile Scheme as the first-class language. What v0.0.3 does on a desktop RTX 3050 8 GB (same session, same GGUF, vs llama.cpp -ngl 99): model decode (tg64) prefill (pp512) Gemma 4 E4B Q3_K_M 1.18× 1.00× Qwen2.5-0.5B Q4_K_M 1.12× 1.09× On real multi-turn agent workloads, time-to-first-token dropped several-fold since v0.0.2 (prefix reuse + plan caching). Output tokens are bit-identical to our golden runs, and prefix reuse is bitwise identical to a full prefill. How: all graph optimization and kernel generation happen on Boom IR, an MLIR dialect; hot quantized matmuls run as attributed ggml-derived kernels. Every optimization has a switch and an ablation number, so you can see what each one buys. Where we are honest about gaps: Qwen decode at depth 512 is 0.98×, and we have only one GPU. That is exactly why we need you. The invitation: every release gets one benchmark issue. If you have an NVIDIA GPU (any generation — Ada, Hopper, Blackwell especially welcome), one command produces a report you can paste. Everyone whose results we publish is credited in the README. → v0.0.3 benchmark issue: https://github.com/hardenedlinux/SonicBoom/issues/2 Please post results and problems in the issue rather than here, so everything stays in one place.
