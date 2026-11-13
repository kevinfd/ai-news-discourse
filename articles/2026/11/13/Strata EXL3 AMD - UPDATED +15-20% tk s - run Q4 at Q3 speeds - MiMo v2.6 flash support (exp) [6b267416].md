---
id: "6b2674167bde68af"
title: "Strata EXL3 AMD - UPDATED +15-20% tk/s - run Q4 at Q3 speeds - MiMo v2.6 flash support (exp)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xv282p/strata_exl3_amd_updated_1520_tks_run_q4_at_q3"
link: "https://reddit.com/r/LocalLLaMA/comments/1xv282p/strata_exl3_amd_updated_1520_tks_run_q4_at_q3"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T08:10:02Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["nasone32"]
language: "en"
summary: "A quick update on my Strata EXL3 fork for AMD. I've been working on the HIP kernels and memory management, and decode performance is now roughly 10-20% higher than the previous version, depending on the quant and workload. Some cases improved by almost 24%. The other news is that I managed to get MiMo V2.6 Flash running at around 25-30 tokens/s with 2 cards. . More on that below. First, why…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD", "Baidu"]
topics: ["chips & infrastructure", "products & launches", "agents & coding", "models & research"]
content_source: "post"
word_count: 813
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xv282p/strata_exl3_amd_updated_1520_tks_run_q4_at_q3/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strata EXL3 AMD - UPDATED +15-20% tk/s - run Q4 at Q3 speeds - MiMo v2.6 flash support (exp)

Reddit · nasone32 · 2026-11-13

A quick update on my Strata EXL3 fork for AMD. I've been working on the HIP kernels and memory management, and decode performance is now roughly 10-20% higher than the previous version, depending on the quant and workload. Some cases improved by almost 24%. The other news is that I managed to get MiMo V2.6 Flash running at around 25-30 tokens/s with 2 cards. . More on that below. First, why EXL3? I think this is worth repeating because people tend to compare quantizations just by looking at the number of bits. EXL3 is NOT equivalent to regular GGUF quants at the same bpw. For example, 3.05 bpw EXL3 is roughly in the same quality range as a regular 4-bit quant (like IQ4_XS) . 3.05 bpw quant: https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/3.05bpw_h5_ng5 4.05 bpw quant: https://huggingface.co/turboderp/Qwen3.8-Flash-Next-exl3/tree/4.05bpw_h6_ng6 So the interesting part is that you can get something close to 4-bit quality, while running at speeds closer to what you'd expect from a 3-bit quant. And with the latest optimizations, I think this fork is becoming VERY competitive. The 4.05 bpw version is also pretty fast now, even on a single GPU. WHAT'S NEW: Faster HIP kernels and better memory management: around 10-20% faster decode on average compared to the previous version. Optional local expert repacking: you can now repack the quantized expert weights into a layout that is more efficient for CPU access from system RAM. This helps when using CPU assistance for inference, since the CPU can process experts more efficiently without having to deal with the original GPU-oriented layout. It doesn't change the quantization itself. The repacking is optional , and CPU assistance is not always beneficial. It depends on your hardware and GPU configuration. With two GPUs, for example, you're generally better off without it. Please read the README before enabling it. Experimental MiMo V2.6 Flash support: currently running at around 25-30 tok/s using the 2.20 bpw MOPD quant. This is still experimental, so don't expect everything to work perfectly yet. NOTES ON REPACKING: Repacking can be done in two ways: by creating a file on disk once, that will be used to load the model, or directly to RAM everytime. directly to RAM adds a couple of minutes to the launch but uses no extra space. your choice. BENCHMARKS: My hardware is the same as in the previous post: Ryzen 9 7950X, 96GB RAM, 2x Radeon RX 7900 XTX 24GB Linux, HIP/ROCm core-7.14 Qwen3.8-Flash-Next, MTP drafter, spec 4, 64K context BENCHMARKS: Results with one or two RX 7900 XTX GPUs, using warm decode runs: EXL3 quant GGUF equivalent quality GPUs CPU assistance Test Previous Updated Improvement 3.05 bpw ≈ IQ4_K_XS 2 No CODE 78.27 87.33 +11.6% 3.05 bpw ≈ IQ4_K_XS 2 No PROSE 66.01 70.35 +6.6% 4.05 bpw ≈ Q5_K_M 2 No CODE 61.88 76.67 +23.9% 4.05 bpw ≈ Q5_K_M 2 No PROSE 57.78 67.57 +16.9% 4.05 bpw ≈ Q5_K_M 1 No → Yes CODE 54.80 59.30 +8.2% 4.05 bpw ≈ Q5_K_M 1 No → Yes PROSE 44.80 51.60 +15.2% All speeds are in tokens/s, GGUF quality equivalents are approximate... dont' hate me :) 32K prefill is basically unchanged: around 1,500 tok/s with two GPUs and 1,360 tok/s with one GPU. I think the single-GPU results are particularly interesting. We're getting 55-60 tok/s in CODE with 4.05 bpw EXL3, at roughly Q5_K_M quality, on a single 7900 XTX with CPU assistance. And the 3.05 bpw quant is now reaching 87 tok/s with two GPUs, while offering considerably better quality than you'd normally expect from a 3-bit quant. ABOUT MiMo: In my previous post I mentioned that I wanted to support larger models, particularly the 300B class models. Well, MiMo V2.6 Flash is now running :) I'm waiting for that ERNIE 5.5 to drop.I'm getting around 25-30 tok/s with the EXL3 2.20 bpw MOPD quant.It's still experimental and currently only tested with that specific quant. CPU assistance is recommended for MiMo, even with two GPUs.I'll probably spend some more time optimizing it, but the fact that it's already running at usable speeds on consumer AMD hardware is pretty interesting. this is the quant: https://huggingface.co/vcruz305/MiMo-V2.6-Flash-MOPD-EXL3/tree/main/2.20bpw REPO: https://github.com/nasone32/Strata-EXL3-fork If you're setting it up with an AI agent, point it to docs/AI_SETUP_EXL3_AMD.md . The README has the benchmarks, configuration options and instructions for CPU repacking.As before, this is developed and tested on RDNA3 / Linux / ROCm. Other AMD architectures need community testing. And the long-term goal is still to get this merged upstream into Strata, if the maintainers are interested. Credits to the original Strata developers, Ryutaku for the EXL3 integration, and Turboderp/ExLlamaV3 for the quantization and code I've been porting. If anyone tests this on different AMD hardware, please report your results. Especially interested in seeing how it behaves on RDNA4. I have only two 7900 xtx so if you have different hardware get an agent to help you, and open a PR if you want.
