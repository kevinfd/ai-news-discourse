---
id: "9b9d41450cd6db7c"
title: "[Guide] Ternary Bonsai 2 is finally 100% working on ik_llama.cpp (Native CUDA offload + Fast CPU -rtr)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkcg2y/guide_ternary_bonsai_2_is_finally_100_working_on"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkcg2y/guide_ternary_bonsai_2_is_finally_100_working_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T15:01:18Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Any_Bus9205"]
language: "en"
summary: "Hey folks, Quick heads up for anyone playing around with PrismML's Ternary Bonsai 2! Until very recently, running it outside of Prism's own fork was a bit of a pain. Upstream llama.cpp uses a block size of QK=256 (TQ2_0), while Prism uses QK=128 (PQ2_0), and trying to offload layers to CUDA on other forks would bottleneck or break due to Hadamard sign tensor handling. With the latest commits…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel", "Nvidia", "Perplexity"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 418
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkcg2y/guide_ternary_bonsai_2_is_finally_100_working_on/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Guide] Ternary Bonsai 2 is finally 100% working on ik_llama.cpp (Native CUDA offload + Fast CPU -rtr)

Reddit · Any_Bus9205 · 2026-10-31

Hey folks, Quick heads up for anyone playing around with PrismML's Ternary Bonsai 2! Until very recently, running it outside of Prism's own fork was a bit of a pain. Upstream llama.cpp uses a block size of QK=256 (TQ2_0), while Prism uses QK=128 (PQ2_0), and trying to offload layers to CUDA on other forks would bottleneck or break due to Hadamard sign tensor handling. With the latest commits landed in ik_llama.cpp, we finally have complete, native support across both CUDA and CPU. 📊 Benchmark & Speedup: Ternary-Bonsai-2-27B on CPU Tested on an Intel Core i5-13420H (4 P-cores pinned via taskset, AVX2, mimalloc, --no-mmap): Format Metric Base (t/s) R8 / -rtr (t/s) Speedup PQ2_0 Prompt Eval (pp256) 1.93 11.45 ~5.93x (+493%) PQ2_0 Generation (tg32) 3.30 5.04 ~1.53x (+53%) PTQ1_0 Prompt Eval (pp256) 1.80 8.43 ~4.68x (+368%) PTQ1_0 Generation (tg32) 0.77 2.61 ~3.39x (+239%) Perplexity check (n_ctx=256, 1 chunk): Runtime Tip: You don't even need to mess with offline repack scripts if you want a quick spin: simply pass --run-time-repack 1 (or -rtr 1) at launch, and the engine automatically applies the 8-row interleaved layout on the fly via the IQK kernels. 1. Convert upstream weights losslessly (PR #2694) If you already have a native PQ2_0 GGUF downloaded from Prism, you can skip this. If you downloaded upstream TQ2_0 or TQ1_0 files, ik_llama.cpp now ships with a script that losslessly repacks them to PQ2_0 in just a few seconds (exact trits preserved, no requantization needed): python3 scripts/repack_ternary_to_prism.py Bonsai-2-27B-TQ2_0.gguf Bonsai-2-27B-PQ2_0.gguf 2. Native CUDA Full Offload (PR #2691 & PR #2747) Native CUDA kernels for PQ2_0 are now merged. You can offload everything to your Nvidia GPU without token corruption or falling back to heavy k-quants: ./build/bin/llama-cli -m Bonsai-2-27B-PQ2_0.gguf -ngl 99 -p "Explain the theory of relativity in simple terms." --temp 0.7 --top-p 0.95 --top-k 20 3. CPU Inference with fast prompt ingestion (-rtr 1) If you're testing on CPU, ik_llama.cpp uses an 8-row interleaved format (PQ2_0_R8) backed by iqk_mul_mat kernels. Remember to pass -rtr 1 (runtime repack) to drastically accelerate prompt processing: ./build/bin/llama-cli -m Bonsai-2-27B-PQ2_0.gguf -rtr 1 -t 8 -p "Explain the theory of relativity in simple terms." --temp 0.7 --top-p 0.95 --top-k 20 TL;DR No more sign tensor bottlenecks on GPU. PR #2747 brings native CUDA kernels, PR #2694 gives us instant lossless repack from upstream weights, and CPU prompt ingestion with -rtr 1 jumps from 1.93 to 11.45 t/s (+493% speedup) with zero perplexity degradation. Big shoutout to Iwan Kawrakow and the contributors for getting ternary models working natively!
