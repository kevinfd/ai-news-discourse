---
id: "5c1d88de1b77252a"
title: "Kokon 0.10: the Qwen-Image 2.1 text encoder now writes your prompts too (no extra model), plus your own LoRAs (beta)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xazqxz/kokon_010_the_qwenimage_21_text_encoder_now"
link: "https://reddit.com/r/LocalLLaMA/comments/1xazqxz/kokon_010_the_qwenimage_21_text_encoder_now"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T18:16:33Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Ok-Director4174"]
language: "en"
summary: "Kokon 0.10: Prompt+ and your own LoRAs A week ago I posted Kokon here , a no-settings desktop editor for Qwen-Image 2.1. 0.10 is out with the two things people asked for most. Prompt+. Type a short idea, in any language, and Kokon writes a detailed prompt from it before making the image. For edits it looks at your photo first. You watch the prompt being written, and the result keeps both your…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Nvidia"]
topics: ["models & research"]
content_source: "post"
word_count: 440
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xazqxz/kokon_010_the_qwenimage_21_text_encoder_now/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Kokon 0.10: the Qwen-Image 2.1 text encoder now writes your prompts too (no extra model), plus your own LoRAs (beta)

Reddit · Ok-Director4174 · 2026-10-20

Kokon 0.10: Prompt+ and your own LoRAs A week ago I posted Kokon here , a no-settings desktop editor for Qwen-Image 2.1. 0.10 is out with the two things people asked for most. Prompt+. Type a short idea, in any language, and Kokon writes a detailed prompt from it before making the image. For edits it looks at your photo first. You watch the prompt being written, and the result keeps both your words and the written prompt, so you can reuse either. It's off by default, one click next to Quality. Both system prompts are editable in Settings. The prompt is written by Qwen3-VL 8B, which is the text encoder Qwen-Image 2.1 already loads. So there's no second model to download and nothing extra in memory. It adds about 2 s per image on an RTX 5070 Ti and about 13 s on an M2 Pro, and it works on 8 GB cards. Your own LoRAs (beta). Load a Qwen-Image 2.1 LoRA in Settings, set its strength and trigger words, then turn it on per project with one click, up to 3 at once. Kokon checks each file and works on its own copy, so your file isn't changed. LoRAs for older Qwen-Image versions (1.0, 2512, Edit 2509/2511) are refused, because they don't work on 2.1. So far it's tested on Windows with NVIDIA only. If you try it on Mac or Linux, please tell me how it goes. An honest note: I said there would be a curated LoRA list. I tested the popular 2.1 LoRAs on the Turbo model Kokon runs, and today they don't beat what Turbo does with a good prompt. So there's no catalog for now, and it comes when a LoRA earns its place. Under the hood. Kokon now runs its own build of stable-diffusion.cpp on Windows, macOS and Linux. It's upstream plus text generation on the already-loaded text encoder: about 127 tokens/s on a 5070 Ti, the same tokens llama.cpp gives. The image side is upstream's code and makes bit-identical images. Upstream prefers to leave text generation to llama.cpp ( #2155 ), which is fair, so it lives in a fork that I keep close to upstream. Also new: a new look, deleting several projects at once, and fixes for Linux/macOS engine crashes, Windows reserved ports and 8 GB cards. Updating from 0.9.x keeps your images and models. The new engine is a one-time download, 29–352 MB depending on your platform. Free and open source (AGPL), Windows, macOS 15+ and Linux: GitHub · kokon.app Still not there: other models, a server/browser mode for Linux boxes, code signing. (Weights: Qwen Research License, non-commercial.)
