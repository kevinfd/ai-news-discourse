---
id: "c9786f91a0400498"
title: "capy-flash: Qwen3.8-Flash-Next (125B MoE) in full NVFP4 on two 16 GB consumer GPUs"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6wh1z/capyflash_qwen38flashnext_125b_moe_in_full_nvfp4"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6wh1z/capyflash_qwen38flashnext_125b_moe_in_full_nvfp4"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T20:20:40Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["FeydRowan"]
language: "en"
summary: "First, kudos to Strata . It inspired this project, and while I was building it Strata got much faster and added NVFP4 support, which was my main reason for starting. By then I was too far in to stop, so I finished it. capy-flash is the evolution of my ninfer-tp2 engine. It still runs Qwen3.8-27B as before, and now also Qwen3.8-Flash-Next 125B-A6B with the experts offloaded to RAM. It uses…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "agents & coding", "models & research"]
content_source: "post"
word_count: 291
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6wh1z/capyflash_qwen38flashnext_125b_moe_in_full_nvfp4/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# capy-flash: Qwen3.8-Flash-Next (125B MoE) in full NVFP4 on two 16 GB consumer GPUs

Reddit · FeydRowan · 2026-10-15

First, kudos to Strata . It inspired this project, and while I was building it Strata got much faster and added NVFP4 support, which was my main reason for starting. By then I was too far in to stop, so I finished it. capy-flash is the evolution of my ninfer-tp2 engine. It still runs Qwen3.8-27B as before, and now also Qwen3.8-Flash-Next 125B-A6B with the experts offloaded to RAM. It uses NVIDIA's official NVFP4 checkpoint as-is and runs both GPUs in tensor parallel. Switching between the two models is one flag. On my machine (2× RTX 5070 Ti 16 GB, Ryzen 9 9900X, 96 GB DDR5), with the same NVFP4 weights, it does ~100 tok/s generation vs 78 for Strata, and ~3.4k tok/s prefill on a 15k prompt vs 2.7k. Strata's 3-bit IQ3_S build is still faster at generation; full comparison in the image. Quality is checked against a datacenter NVFP4 reference (GSM8K, MMLU-Pro, agentic coding tasks). A side finding for any tensor-parallel engine. With TP, each GPU rounds its partial sum to BF16 before the all-reduce, so TP=2 rounds twice where one GPU rounds once. Where the two halves cancel, the error blows up: on Qwen3 at TP=2, large errors happen ~5× as often as on one GPU. Writing the partial sums in FP16 (same bytes, 8× finer) brings them back to single-GPU level, at no real speed cost. The effect on benchmarks is small, so think of it as free numerical parity rather than a quality boost. But it should reduce some rare weirdness and keep the agentic loop cleaner. Limits: Linux, RTX 50 series (sm_120) only for now. Repo: https://github.com/ValerioDolci/capy-flash Weights: https://huggingface.co/Feyd89/Qwen3.8-Flash-Next-NVFP4-capy-flash Built on NInfer (Neroued), Strata, ninfer-ext, FreeToken, sybrix and qf_moe. Numbers from other hardware are very welcome.
