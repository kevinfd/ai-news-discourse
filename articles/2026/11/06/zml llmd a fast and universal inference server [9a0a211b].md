---
id: "9a0a211bfbcb5eee"
title: "zml/llmd: a fast and universal inference server"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpppfl/zmlllmd_a_fast_and_universal_inference_server"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpppfl/zmlllmd_a_fast_and_universal_inference_server"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T22:10:22Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["siwu"]
language: "en"
summary: "Hey all, I wanted to share that we're working on zml/llmd, a fast (we believe the fastest) inference engine that currently runs on NVIDIA, AMD, Intel, TPU and Metal. It has all the features of a modern LLM server: continuous batching, prefix-caching, speculative decoding (DFlash, DFlash2 and DSpark), tool calling, tensor and experts parallel automatic sharding, native VFS with s3:// and hf://…"
tags: ["r/LocalLLaMA"]
orgs: ["Mistral", "Nvidia", "Alibaba", "Intel", "AMD", "DeepSeek"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 184
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpppfl/zmlllmd_a_fast_and_universal_inference_server/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# zml/llmd: a fast and universal inference server

Reddit · siwu · 2026-11-06

Hey all, I wanted to share that we're working on zml/llmd, a fast (we believe the fastest) inference engine that currently runs on NVIDIA, AMD, Intel, TPU and Metal. It has all the features of a modern LLM server: continuous batching, prefix-caching, speculative decoding (DFlash, DFlash2 and DSpark), tool calling, tensor and experts parallel automatic sharding, native VFS with s3:// and hf:// support streaming straight to GPU. The currently supported models are: Qwen 2, 3, 3.5, 3.6 and 3.8 series (dense and MoE) Gemma 3 and 4 series (dense and MoE) LFM2.5 series Mistral 3 and Ministral series LLaMa 2 and 3 series Poolside's Laguna S 2.1 DeepSeek 4.1 Flash Muse Glimmer Qwen3.8 Flash Next Xiaomi MiMo V2.6 Mistral Large 4 GLM 5.2 GLM 5.3 LFM 3 Beam 1.0 Ripple 65B Our images are a lot smaller than alternatives: Platform Image Size CUDA zmlai/llmd:cuda 1.96 GB ROCm zmlai/llmd:rocm 4.77 GB TPU zmlai/llmd:tpu 272 MB OneAPI zmlai/llmd:oneapi 454 MB Metal brew install zml/zml/llmd 142 MB We just came out with a new release today: zml/llmd llmd-20261106.0 and we'd love to get your feedback on it!
