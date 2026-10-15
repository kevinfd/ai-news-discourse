---
id: "bd1bdffa0eba9b4d"
title: "GPT-Image-style photo editing on your own GPU (12 GB+): I built a zero-setup app for Qwen-Image 2.1 on stable-diffusion.cpp"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5wyii/gptimagestyle_photo_editing_on_your_own_gpu_12_gb"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T17:10:15Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Ok-Director4174"]
language: "en"
summary: "Every local setup I tried for Qwen-Image 2.1 meant a Python env, a node graph and an evening of picking quantization, offloading and resolution for my card. Kokon is a free, open-source desktop app that does all of that for you and gives you a plain photo editor on top. Zero setup: first run detects your GPU and memory and downloads the matching GGUFs (Qwen-Image 2.1 Turbo Q4_K + Qwen3-VL 8B…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Nvidia", "Apple", "Intel", "AMD"]
topics: ["models & research", "chips & infrastructure", "agents & coding", "products & launches"]
content_source: "post"
word_count: 278
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5wyii/gptimagestyle_photo_editing_on_your_own_gpu_12_gb/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# GPT-Image-style photo editing on your own GPU (12 GB+): I built a zero-setup app for Qwen-Image 2.1 on stable-diffusion.cpp

Reddit · Ok-Director4174 · 2026-10-14

Every local setup I tried for Qwen-Image 2.1 meant a Python env, a node graph and an evening of picking quantization, offloading and resolution for my card. Kokon is a free, open-source desktop app that does all of that for you and gives you a plain photo editor on top. Zero setup: first run detects your GPU and memory and downloads the matching GGUFs (Qwen-Image 2.1 Turbo Q4_K + Qwen3-VL 8B text encoder, ~12 GB, checksummed). Each job is sized automatically: working resolution, VRAM/RAM split, tiled VAE, retry if it runs out of memory. Engine: stable-diffusion.cpp (ggml), so no Python, no PyTorch. CUDA, Vulkan and Metal builds. An editor, not a workflow: type the change, or brush an area with Change / Remove / Replace / Add. The brushed area is marked on a second reference image, so the model actually sees it. Versions with undo, before/after, upscaler comparison. Hardware: NVIDIA 12 GB+ (CUDA). Apple Silicon (Metal, beta, slow: ~4 min per image on a 16 GB M2 Pro). AMD / Intel Arc 12 GB+ via Vulkan (beta, only tested on NVIDIA so far, reports very welcome). Speed: 5070 Ti 16 GB: ~24 s per edit at 1.5K, ~40 s for a native 2K edit. Agents: built-in MCP server ( generate_image , edit_image , inpaint_image , outpaint_image , upscale_image …) and a local HTTP API: npx -y kokon-mcp , also in the official MCP Registry. Not yet: Linux; code signing (SmartScreen warns on first run); reusing model files you already have is a manual workaround for now ( #14 ). Repo: https://github.com/GabrieleLozupone/kokon · Site: https://kokon.app Code is AGPL-3.0; the Qwen weights are under the Qwen Research License (non-commercial).
