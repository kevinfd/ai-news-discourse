---
id: "2df0c952ba0091bc"
title: "XeMaya, an Intel Arc inference engine to run DeepSeek V4.1 and GLM 5.3"
url: "https://reddit.com/r/LocalLLaMA/comments/1xt2mjk/xemaya_an_intel_arc_inference_engine_to_run"
link: "https://reddit.com/r/LocalLLaMA/comments/1xt2mjk/xemaya_an_intel_arc_inference_engine_to_run"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T23:50:54Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Jumbomuffin1312"]
language: "en"
summary: "I've been trying to get some of the newer MoE models running on my Intel Arc GPUs, mainly DeepSeek V4.1 Flash and GLM 5.3 Flash. Intel support for these models is still pretty limited, and while I could get some things working through patched llama.cpp builds, performance wasn't exactly great. fable 5.2 ended up making XeMaya, a fork of XeStrata focused on getting these models running natively…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel", "DeepSeek", "Alibaba"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 380
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xt2mjk/xemaya_an_intel_arc_inference_engine_to_run/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# XeMaya, an Intel Arc inference engine to run DeepSeek V4.1 and GLM 5.3

Reddit · Jumbomuffin1312 · 2026-11-10

I've been trying to get some of the newer MoE models running on my Intel Arc GPUs, mainly DeepSeek V4.1 Flash and GLM 5.3 Flash. Intel support for these models is still pretty limited, and while I could get some things working through patched llama.cpp builds, performance wasn't exactly great. fable 5.2 ended up making XeMaya, a fork of XeStrata focused on getting these models running natively on Intel Arc through SYCL and Level Zero. The idea is basically to bring the kind of model support Project Maya has to Intel GPUs. I've been testing it on my Ubuntu server with a B70 32GB, B65 32GB, B60 24GB, Ryzen 9950X, and 128GB RAM. Here are some of the results so far. All speeds are prefill / generation in tok/s. GLM 5.3 Flash Stock llama.cpp SYCL: 68.3 / 13.6 Experimental grouped-matmul SYCL: 108.9 / 14.0 XeMaya: 152–161 / 17.4 (around 20 generation with MTP) DeepSeek V4.1 Flash Coder First XeMaya implementation: 48.5 / 16.3 After optimization: 224.8 / 21.7 DeepSeek V4.1 Flash (regular 384-expert model) Previous patched llama.cpp setup: 45.6 / 10.9 XeMaya on B70 + B65: 11.4 / 14.56 XeMaya on all three GPUs: 11.2 / 11.58 Prefill on the regular model still needs a lot of work. Also found out that using two GPUs is actually faster than three for this model because my B60 is connected through a slower chipset link. Qwen3.8 Flash-Next Strata: 2,211 / 78.3 XeMaya: 1,842–1,884 / 76.6 Strata is still slightly faster for Qwen, which makes sense since that's not really where I've been focusing my time. These aren't all perfectly controlled comparisons. Different model files, prompts, and GPU configurations were used during development, so I wouldn't treat them as definitive benchmarks. It's still an early alpha, but I've gotten DeepSeek V4.1 Flash, Coder, GLM 5.3 Flash, and Qwen3.8 Flash-Next running. There's plenty left to fix and optimize. Also, I want to credit MistVVK (XeStrata), Niko1221 (Strata), and mw00 (Project Maya) . XeMaya wouldn't exist without their work. The llama.cpp contributors have also been a huge help through their reference implementations. Figured I'd share it here since I'm sure there are others trying to run these models on Intel hardware. Would be interested to hear how it runs on other Arc cards. GitHub: https://github.com/Jumbomuffin777/XeMaya
