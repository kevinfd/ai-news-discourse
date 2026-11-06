---
id: "dfcb73025af43ae3"
title: "Getting editable layers out of Qwen-Image 2.1, a model that only edits: what works, what still fails (local, open source) Kokon"
url: "https://reddit.com/r/LocalLLaMA/comments/1xoji3b/getting_editable_layers_out_of_qwenimage_21_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1xoji3b/getting_editable_layers_out_of_qwenimage_21_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T14:06:27Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Ok-Director4174"]
language: "en"
summary: "I'm the developer of Kokon, a local photo editor around Qwen-Image 2.1 Turbo (on stable-diffusion.cpp, and on its own engine on Macs). I posted it here a few weeks ago. 0.12 adds a Layers lab: click objects in any image, get each one on its own layer with the background behind it repainted, then move them around or export a PSD. Qwen-Image 2.1 has no layer output, so this is a pipeline around an…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Nvidia", "Apple", "Intel", "AMD"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 454
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xoji3b/getting_editable_layers_out_of_qwenimage_21_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Getting editable layers out of Qwen-Image 2.1, a model that only edits: what works, what still fails (local, open source) Kokon

Reddit · Ok-Director4174 · 2026-11-05

I'm the developer of Kokon, a local photo editor around Qwen-Image 2.1 Turbo (on stable-diffusion.cpp, and on its own engine on Macs). I posted it here a few weeks ago. 0.12 adds a Layers lab: click objects in any image, get each one on its own layer with the background behind it repainted, then move them around or export a PSD. Qwen-Image 2.1 has no layer output, so this is a pipeline around an edit model: Select : you click, MobileSAM (ONNX, CPU, 44 MB) gives the mask. Click again for a bigger part. Cut out : Fast is a matting model on the CPU (a few seconds per object). Quality asks Qwen to redraw the edge, for hair and fur. Fill : a masked Qwen-Image edit repaints what was behind the object, so the plate has no holes. This is the expensive step: about 15–25 s per object on an RTX 5070 Ti, one to two minutes on an M2 Pro. Blend into scene (optional): after you move things, Kokon reads where each object stands (you can correct it) and one more edit redraws contact shadows and reflections, as a layer you can turn down. What still fails, honestly: the fill sometimes invents a new object where a large one was (remove a big person, get a different person); touching people and crowds get merged or split; the hidden part of an object behind another one is never completed; Blend often doesn't work yet; whole-scene blends work better than per-object ones. An 8-step model only takes so much steering. I'd rather ship it marked experimental and fix what people actually hit than tune it on my own test photos. If you try it, failure cases (image + what you clicked) are the most useful thing you can send. Since my last post here: 0.11, it's a local server now : the app talks to a service on 127.0.0.1; turn on "Other devices" and you can use it from a phone or another PC on your LAN (password, off by default, hashed, rate-limited). Docker image for NVIDIA, kokon-service --persistent --remote for headless Linux. There's also an MCP server (npm kokon-mcp ) so agents can generate and edit through it. Mac engine : I wrote a Qwen-Image 2.1 engine for Apple Silicon in Swift/Metal. M2 Pro: about a minute per 1 MP image, 4x the generic backend. A contributor added paths for the M5's GPU neural accelerators: 37 → 29 s on an M5 Pro. It runs Unsloth's Q4_K_M of the Turbo model. Free, AGPL, Windows / macOS 15+ / Linux, NVIDIA 12 GB (8 GB beta), AMD/Intel via Vulkan (beta). Weights are under Qwen's licence (non-commercial). https://github.com/GabrieleLozupone/kokon · 2 min video of 0.12: https://youtu.be/eGr9yYe7NVc
