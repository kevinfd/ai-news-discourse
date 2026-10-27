---
id: "ea2b6fa55e931bf8"
title: "A small visual Q&A benchmark for models that fit into 48GB VRAM + 128GB RAM and smaller"
url: "https://reddit.com/r/LocalLLaMA/comments/1xg2d25/a_small_visual_qa_benchmark_for_models_that_fit"
link: "https://reddit.com/r/LocalLLaMA/comments/1xg2d25/a_small_visual_qa_benchmark_for_models_that_fit"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T16:52:52Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["EmilPi"]
language: "en"
summary: "Every model is SOTA in its the technical report. But custom benchmarks shatter such claims. In this particular benchmark, Qwen3.8-Flash-Next wins so far (the benchmark will grow). Source: https://beta.locallm.top/home?question=10 Limitations: there are Lithuanian and Russian OCR questions included, so results are biased towards models which work better with those; there is limited number of…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Meta"]
topics: ["models & research"]
content_source: "post"
word_count: 295
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xg2d25/a_small_visual_qa_benchmark_for_models_that_fit/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# A small visual Q&A benchmark for models that fit into 48GB VRAM + 128GB RAM and smaller

Reddit · EmilPi · 2026-10-26

Every model is SOTA in its the technical report. But custom benchmarks shatter such claims. In this particular benchmark, Qwen3.8-Flash-Next wins so far (the benchmark will grow). Source: https://beta.locallm.top/home?question=10 Limitations: there are Lithuanian and Russian OCR questions included, so results are biased towards models which work better with those; there is limited number of tasks yet. Some additional benchmark info is at https://beta.locallm.top/benchmark/2b2aa60b-7eaa-49da-8660-b650a53412b4 : runs can be inspected by registered users (done against scraping). Some things I see from this chart: There is a group of models in the top league. Qwen3.8-27B was damaged compared to Qwen3.6-27B (and even 3.5) while improving its agentic/STEM capabilities, and 3.8 uncensored took additional (but small) damage compared even to that. I didn't expect: Muse-Glimmer-30B scoring high, but it was superb in some details recognition, which I attribute for Meta work in computer vision, e.g. SAM3. GLM-5.3-Flash scoring high even at low quant DeepSeek-V4-Flash-Vision-Exp be the last, but it was first experimental DeepSeek truly multimodal LLM, so in hindsight... A few examples from the benchmark: Below, common errors was not to format generated markdown correctly, and some models outright hallucinated generic management stuff. Still, some models did perfectly. Prompt: \"Write me the markdown version of the note.\" Here below Neowise comet is visible in the center of the sky. Common errors was characterising the building as made of yellow bricks (although it is overexposure saturation from sodium lamps, of course). Some models identified the comet as meteor or satellite - they got a bonus for this, the score did not rely on that faint comet tail discovery only. Prompt: \"What is in the image?\" If you want to participate in the custom benchmarks creation, please write me here or DM, or just register on the website and start creating!
