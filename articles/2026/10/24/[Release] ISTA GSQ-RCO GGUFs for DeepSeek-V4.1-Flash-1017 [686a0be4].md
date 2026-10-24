---
id: "686a0be4029ec3b9"
title: "[Release] ISTA GSQ-RCO GGUFs for DeepSeek-V4.1-Flash-1017"
url: "https://reddit.com/r/LocalLLaMA/comments/1xe2wg8/release_ista_gsqrco_ggufs_for_deepseekv41flash1017"
link: "https://reddit.com/r/LocalLLaMA/comments/1xe2wg8/release_ista_gsqrco_ggufs_for_deepseekv41flash1017"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T08:05:17Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Loginhe"]
language: "en"
summary: "We have released DeepSeek-V4.1-Flash-1017 quantized with GSQ and RCO, at 1.75 to 2.25 bits per weight. DeepSeek-V4.1-Flash-1017 is a sparse mixture-of-experts model: 384 routed experts per layer, of which 6 are active per token, 763.2B parameters and a 1M-token context window. It is released with FP8 dense weights and FP4 routed experts. What's inside Three quantized GGUFs: IQ1_M (1.75 bpw),…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "OpenAI", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "search & media"]
content_source: "post"
word_count: 427
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xe2wg8/release_ista_gsqrco_ggufs_for_deepseekv41flash1017/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Release] ISTA GSQ-RCO GGUFs for DeepSeek-V4.1-Flash-1017

Reddit · Loginhe · 2026-10-24

We have released DeepSeek-V4.1-Flash-1017 quantized with GSQ and RCO, at 1.75 to 2.25 bits per weight. DeepSeek-V4.1-Flash-1017 is a sparse mixture-of-experts model: 384 routed experts per layer, of which 6 are active per token, 763.2B parameters and a 1M-token context window. It is released with FP8 dense weights and FP4 routed experts. What's inside Three quantized GGUFs: IQ1_M (1.75 bpw), IQ2_XXS (2.00 bpw) and IQ2_XS (2.25 bpw), with backbones of 120.7 to 155.2 GB. The bit-width is the average over the 551.9B backbone parameters, which is what the search controls. One shared Engram file (110.6 GB): the model's two Engram lookup tables (196.6B parameters) at IQ4_NL. It is identical for every build and needs to be downloaded only once. The tables are read one row per token, so they can stay memory-mapped on disk. Every build runs on a single 12 GB GPU with Strata (see model card, https://github.com/Niko1221/Strata ). GSQ (Gumbel-Softmax Quantization): post-training scalar quantization that jointly learns grid assignments and group scales, closing most of the gap between scalar and vector quantization at low bit-widths while remaining deployable in standard GGUF types. RCO (Riemannian Constrained Optimization): enforces exact budgets by gradient descent on the task loss, without per-constraint tuning. Here it assigns a quantization type to every backbone tensor under the target bit-width, with separate ladders for the dense path (Q5_K to Q8_0) and the routed experts (IQ1_S to IQ3_S). An embedded chat template that reproduces DeepSeek's prompt encoder exactly, including the reasoning effort (1 to 100, or low / high / max). Results At 2.00 bpw the model matches the base model on every benchmark evaluated. All numbers were measured at reasoning effort 50. IQ1_M (1.75 bpw, 120.7 GB backbone): AIME25 100.00, GPQA-Diamond 88.38 against 90.91, LiveCodeBench v6 88.57 against 89.71. Task average 92.32, retaining 98.7%. IQ2_XXS (2.00 bpw, 138.2 GB backbone): AIME25 100.00, GPQA-Diamond 90.91, LiveCodeBench v6 89.71, identical to the base model. Task average 93.54, 100.0% of the base. IQ2_XS (2.25 bpw, 155.2 GB backbone): results to follow. Running it llama.cpp does not support DeepSeek-V4.1 yet, so the GGUFs do not run there for now. They run in Strata, which serves every build on a single NVIDIA GPU with 12 GB of VRAM, with a one-click installer and an OpenAI-compatible endpoint on localhost. Links Quantized models: https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF GSQ: paper https://arxiv.org/abs/2604.18556 | code https://github.com/IST-DASLab/GSQ RCO: paper https://arxiv.org/abs/2605.00649 | code https://github.com/IST-DASLab/RCO The repository ships the complete per-tensor RCO allocation for every build (1008 tensors each). Feedback is welcome. Requests for models to quantize are also welcome. From the ISTA Deep Algorithms and Systems Lab.
