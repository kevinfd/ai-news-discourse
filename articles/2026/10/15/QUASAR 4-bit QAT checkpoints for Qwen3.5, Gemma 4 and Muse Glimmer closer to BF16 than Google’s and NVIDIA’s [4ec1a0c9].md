---
id: "4ec1a0c953f735d0"
title: "QUASAR 4-bit QAT checkpoints for Qwen3.5, Gemma 4 and Muse Glimmer: closer to BF16 than Google’s and NVIDIA’s 4-bit releases"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6u8pi/quasar_4bit_qat_checkpoints_for_qwen35_gemma_4"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6u8pi/quasar_4bit_qat_checkpoints_for_qwen35_gemma_4"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T18:55:28Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Mindless_Ad_407"]
language: "en"
summary: "Two months ago we released a fully quantized NVFP4 Qwen3.8-27B trained with QUASAR. We've since trained QUASAR checkpoints for a bunch of other recent models: Qwen3.5-4B, Gemma 4 E4B and 12B, and Muse Glimmer 30B, in NVFP4 for vLLM and Q4_0 GGUF for llama.cpp / Ollama / LM Studio. The code and a project page are now public too. Every checkpoint is trained with quantization-aware distillation:…"
tags: ["r/LocalLLaMA"]
orgs: ["Google", "Nvidia", "Meta"]
topics: ["models & research", "jobs & society", "chips & infrastructure"]
content_source: "post"
word_count: 328
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6u8pi/quasar_4bit_qat_checkpoints_for_qwen35_gemma_4/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# QUASAR 4-bit QAT checkpoints for Qwen3.5, Gemma 4 and Muse Glimmer: closer to BF16 than Google’s and NVIDIA’s 4-bit releases

Reddit · Mindless_Ad_407 · 2026-10-15

Two months ago we released a fully quantized NVFP4 Qwen3.8-27B trained with QUASAR. We've since trained QUASAR checkpoints for a bunch of other recent models: Qwen3.5-4B, Gemma 4 E4B and 12B, and Muse Glimmer 30B, in NVFP4 for vLLM and Q4_0 GGUF for llama.cpp / Ollama / LM Studio. The code and a project page are now public too. Every checkpoint is trained with quantization-aware distillation: the original BF16 model is the teacher, and the quantized model is distilled (healed) on the teacher's own responses. The exports are standard formats (so no custom kernels and/or conversion step). KL to the BF16 model on held-out prompts (lower=better): Model Format QUASAR Reference Muse Glimmer 30B NVFP4 (vLLM) 0.0183 0.0300 (NVIDIA NVFP4) Muse Glimmer 30B NVFP4 W4A4 (Blackwell) 0.0530 0.0664 (Red Hat NVFP4) Muse Glimmer 30B Q4_0 GGUF 0.0213 0.0228 (Meta Q4_K_M) Gemma 4 12B W4A16 (vLLM) 0.034 0.044 (Google QAT) Gemma 4 12B Q4_0 GGUF 0.048 0.069 (Google QAT) Gemma 4 E4B W4A16 (vLLM) 0.022 0.064 (Google QAT) Gemma 4 E4B Q4_0 GGUF 0.044 0.088 (Google QAT) Qwen3.5-4B NVFP4 (vLLM) 0.0181 0.0419 (cyankiwi AWQ) Qwen3.5-4B NVFP4 W4A4 (Blackwell) 0.046 0.075 (cosmicproc NVFP4) Qwen3.5-4B Q4_0 GGUF 0.235 0.284 (bartowski Q4_0) On benchmarks: Muse Glimmer 30B NVFP4: at or above BF16 on GPQA-Diamond (63.6 vs 62.1), MMLU-Pro (83.3 vs 83.1) and AIME'25 (90.0 vs 86.7), and the only 4-bit build at BF16 performance on RULER at 32K, 64K and 128K. Qwen3.5-4B NVFP4: best AIME'25 (74.2) and GPQA-Diamond (77.9) among the 4-bit builds we tested. Gemma 4 E4B / 12B: higher than Google's QAT on every downstream benchmark we ran. On H100, E4B also gets +36% batched throughput (group-64 quant uses vLLM's Machete kernel, the faster one). Qwen3.8-27B NVFP4: all 496 linears in NVFP4 (W4A4), 90.9 GPQA-Diamond vs 91.4 BF16, at 19.7 GB. Run it: vllm serve QUASAR-QAT/Qwen3.5-4B-QUASAR-NVFP4 --max-model-len 262144 --reasoning-parser qwen3 ollama run hf.co/QUASAR-QAT/gemma-4-12B-it-QUASAR-Q4_0-GGUF Collection: https://huggingface.co/collections/QUASAR-QAT/all-quasar-models-6aab09fd2913ec22df0d5f15 Paper: https://arxiv.org/abs/2608.13966 Code: https://github.com/vincentcounathe/quasar-qat Project page: https://quasar-qat.github.io/ We'd love to hear your feedback on these checkpoints!
