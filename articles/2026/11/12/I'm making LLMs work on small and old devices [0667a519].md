---
id: "0667a519c65042ee"
title: "I'm making LLMs work on small and old devices"
url: "https://github.com/hyperionaidev/smolmaxxing"
link: "https://github.com/hyperionaidev/smolmaxxing"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-12T15:23:10Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["mrashad74"]
language: "en"
summary: "Run the biggest language model you can on the smallest hardware you own.\nTV boxes, old tablets, single-board computers and routers all have a CPU, some RAM and flash storage that sit idle most of the day. smolmaxxing finds the biggest model each of them can really run, then pushes it further with custom kernels, careful memory use and weights streamed from flash. Every number in this repo was…"
tags: []
orgs: ["Google", "Hugging Face", "Alibaba"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 476
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50468888"
score: 399
comments: 148
community: "Hacker News"
---

# I'm making LLMs work on small and old devices

GitHub · mrashad74 · 2026-11-12

Run the biggest language model you can on the smallest hardware you own.
TV boxes, old tablets, single-board computers and routers all have a CPU, some RAM and flash storage that sit idle most of the day. smolmaxxing finds the biggest model each of them can really run, then pushes it further with custom kernels, careful memory use and weights streamed from flash. Every number in this repo was measured on the device itself.
The TV box and the iPad run 8B and 16B mixture-of-experts models on about 1 GB of RAM, and the phone runs 35B and 80B ones with about 3 GB free. They all keep only part of each model in memory and read the rest from flash as it's needed.
More devices (single-board computers, routers, more phones) are coming. The techniques aren't tied to one box: the 1-bit kernel needs only basic NEON, and the flash streaming works on any Linux or Android device with more model than RAM.
Got a small device? Run a model on it and submit your numbers: we'll add them to the results.
All of it is a patch on llama.cpp. The main ideas:
- Kernels built for the chip. A 1-bit lookup-table kernel, repacked 2-bit and ternary formats for the Cortex-A55, and versions of them for the A7, which has no dot-product instructions.
- Less RAM per model. Most of a small model's vocabulary is rarely used, so we drop those output rows. On the TV, a "headless" mode also stops the launcher and Google services while a model runs.
- Experts paged from flash. A mixture-of-experts model only uses a few experts per token. We keep the popular ones in RAM, read the others from flash on demand and prefetch the next layer's. This is how 8B and 16B models run on 1 GB, and 35B and 80B models on a phone.
- Streaming for dense models bigger than RAM, at the flash's full speed.
docs/how-it-works.md has every technique with its measured gain.
The quickest start is a ready-made model file from Hugging Face. They need the patched llama.cpp: stock llama.cpp can't load them.
- TV box or another ARMv8.2 Android device: docs/tv-box-setup.md
- Jailbroken iPad on iOS 12: ipad-air/README.md
- All model files and how to rebuild them: docs/models.md
Other people running language models on hardware that was never meant for them:
MIT. The llama.cpp patches are derivatives of llama.cpp (MIT). Model weights keep their own licenses, and the evaluation texts are Wikipedia excerpts (CC BY-SA 4.0).
Built on llama.cpp and llama2.c. Models from Qwen, unsloth (GGUFs and importance matrices), PrismML (Bonsai), inclusionAI (Ling-mini-2.0), tablinum (Moon-Beam), bartowski and mradermacher (GGUFs), Google (Gemma) and stories260K. The iPad is jailbroken with Amethyst. The banner uses Archivo (SIL OFL) and is rendered by tools/banner/render.sh. The 🤏 logo is the pinching-hand emoji from Google's Noto Emoji (Apache 2.0).
