---
id: "a4761cd5ecfd623f"
title: "🌋 Pushing PCIe x1 to the limit: lvgale concurrently serving 27B, 9B, and 2B LLMs on a hardware abomination 📈"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdq2cj/pushing_pcie_x1_to_the_limit_lvgale_concurrently"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdq2cj/pushing_pcie_x1_to_the_limit_lvgale_concurrently"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T21:05:21Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["FieldMouse-AI"]
language: "en"
summary: "Everyone loves a clean, unified server rack, but my standby node ( lvgale ) is an absolute physical abomination. It is a Frankenstein collection of mismatched parts and bolted-together VRAM that has no business running efficiently. The Hardware Setup (lvgale) CPU: Intel Core i7-6700K. GPUs: AMD RX 580 8GB VRAM (PCIe x16) AMD RX 570 8GB VRAM (PCIe x1) NVIDIA GTX 1660 Super 6GB VRAM (PCIe x2)…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "AMD", "Intel"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 194
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdq2cj/pushing_pcie_x1_to_the_limit_lvgale_concurrently/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 🌋 Pushing PCIe x1 to the limit: lvgale concurrently serving 27B, 9B, and 2B LLMs on a hardware abomination 📈

Reddit · FieldMouse-AI · 2026-10-23

Everyone loves a clean, unified server rack, but my standby node ( lvgale ) is an absolute physical abomination. It is a Frankenstein collection of mismatched parts and bolted-together VRAM that has no business running efficiently. The Hardware Setup (lvgale) CPU: Intel Core i7-6700K. GPUs: AMD RX 580 8GB VRAM (PCIe x16) AMD RX 570 8GB VRAM (PCIe x1) NVIDIA GTX 1660 Super 6GB VRAM (PCIe x2) NVIDIA GTX 1070 8GB VRAM (PCIe x1) The Bottleneck: Activations must travel across severely constrained x1 and x2 lanes between entirely different AMD and NVIDIA architectures. The Software Engine The cluster is orchestrated by Slipstream, a custom Nuitka-compiled Python orchestration engine. Here, it utilizes a mixed-vendor Vulkan backend with Flash Attention enabled to maintain stability across the fragmented topology. Concurrent Inference Performance In all cases seamlessly handling OCR and complex vision parsing. Qwen3.8:27b-vision: 3.82 t/s. Qwen3.5:9b-vision: 4.75 t/s. Qwen3.5:2b-vision: 12.47 t/s. While the 2B model runs slightly faster on a modern laptop iGPU due to unified memory, keeping a 27B model stable across this mixed-architecture, low-bandwidth topology without crashing the Vulkan driver is a massive win. For deeper technical architecture details, the engine is documented at slipstream-llm.com.
