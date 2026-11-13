---
id: "75348ee9bdbcfb74"
title: "What does Qwen3.6-35B-A3B look like at Q8_0 and BF16 on datacenter GPUs?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xuon4m/what_does_qwen3635ba3b_look_like_at_q8_0_and_bf16"
link: "https://reddit.com/r/LocalLLaMA/comments/1xuon4m/what_does_qwen3635ba3b_look_like_at_q8_0_and_bf16"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T21:03:04Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Serious_Scarcity7818"]
language: "en"
summary: "RustingStrata is a pure-Rust inference engine for Qwen, DeepSeek and GLM GGUFs. CUDA kernels are compiled at run time with NVRTC, the same kernels run on Vulkan, and there is no ggml and no C++ build step. I wanted the high-quant numbers, so these runs use Q8_0 (37.8 GB) and unquantized BF16 (71.1 GB), with the whole model in VRAM, on A100, L40S and H100: GPU Quant Prefill, 4K prompt Decode…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Alibaba"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 468
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xuon4m/what_does_qwen3635ba3b_look_like_at_q8_0_and_bf16/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# What does Qwen3.6-35B-A3B look like at Q8_0 and BF16 on datacenter GPUs?

Reddit · Serious_Scarcity7818 · 2026-11-12

RustingStrata is a pure-Rust inference engine for Qwen, DeepSeek and GLM GGUFs. CUDA kernels are compiled at run time with NVRTC, the same kernels run on Vulkan, and there is no ggml and no C++ build step. I wanted the high-quant numbers, so these runs use Q8_0 (37.8 GB) and unquantized BF16 (71.1 GB), with the whole model in VRAM, on A100, L40S and H100: GPU Quant Prefill, 4K prompt Decode Decode with MTP H100 80 GB HBM3 Q8_0 11,486 tok/s 290 tok/s 508 tok/s H100 NVL BF16 8,691 tok/s 230 tok/s 324 tok/s A100 80 GB Q8_0 6,507 tok/s 193 tok/s 288 tok/s A100 80 GB BF16 5,625 tok/s 171 tok/s 238 tok/s L40S 48 GB Q8_0 9,542 tok/s 165 tok/s 270 tok/s MTP is speculative decoding with the model's own draft head; calibrate picked the draft count on each card. Higher quants are not automatically slower. On the A100 80 GB and H100, Q8_0 decodes faster than Q2_K_XL (193 vs 174, 290 vs 265 tok/s after 4K). On the L40S it is slower (165 vs 214), so the ranking depends on the card. BF16 is practical. 71 GB of unquantized weights decode at 171-230 tok/s on one card. MTP helps less as the quant grows. Gains are 1.4-1.9x on Q2_K_XL and Q8_0, and 1.2-1.4x on BF16. When the model does not fit, it degrades but runs. Q8_0 on a 24 GB A30 (63% of experts resident) still decodes at 130 tok/s, 200 with MTP. BF16 on the same card (31% resident) only reaches about 12.5 tok/s. The same code runs on Vulkan, and on the Q2_K_XL runs on the 3060 and the Ampere cards prefill lands close to CUDA. At Q8_0 on the big cards the gap can be large: H100 prefill is 6,883 tok/s on Vulkan against 11,486 on CUDA. All table numbers are CUDA. These are different nodes of one cluster, so the host CPUs differ. Compare within a row, not across rows. MTP costs 4-11% prefill in these runs. Quality: I do not have a llama.cpp perplexity/KLD run on these exact Q8_0/BF16 files yet, so this is a hardware roundup, not an accuracy comparison. The last check was UD-Q3_K_M on the 3060 over 9,180 tokens of repo docs prose: perplexity 9.0714 vs 9.0587 for llama.cpp, mean KLD 0.0055, same top token 96.3%. Why I find it kinda interesting, is bc when I was searching for models in OpenRouter, I saw that Qwen3.6:35b-a3b for some reason is pretty slow, like 50-110t/s on almost all providers, why like that? Do people already use other Strata like project for LLM inference to be in top of providers? I am thinking about it, but I think something is wrong and not so easy as I expect, if anyone knows I would be happy to hear Repo: RustingStrata
