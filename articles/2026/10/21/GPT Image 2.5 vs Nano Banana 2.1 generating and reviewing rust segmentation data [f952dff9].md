---
id: "f952dff9e496e0b0"
title: "GPT Image 2.5 vs Nano Banana 2.1: generating and reviewing rust segmentation data"
url: "https://reddit.com/r/artificial/comments/1xbjkfu/gpt_image_25_vs_nano_banana_21_generating_and"
link: "https://reddit.com/r/artificial/comments/1xbjkfu/gpt_image_25_vs_nano_banana_21_generating_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T10:31:53Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Gloomy_Recognition_4"]
language: "en"
summary: "Same prompt. Different rust-mask errors. I compared GPT Image 2.5 Sunburst and Nano Banana 2.1 on eight identical prompts to explore synthetic training data for rust segmentation. Both generated promising samples and masks with missing rust, shifted boundaries or false positives. I then expanded the work to 502 image mask pairs, including the pilot. After visual screening, 400 remained and 102…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 141
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xbjkfu/gpt_image_25_vs_nano_banana_21_generating_and/"
score: null
comments: null
community: "r/artificial"
---

# GPT Image 2.5 vs Nano Banana 2.1: generating and reviewing rust segmentation data

Reddit · Gloomy_Recognition_4 · 2026-10-21

Same prompt. Different rust-mask errors. I compared GPT Image 2.5 Sunburst and Nano Banana 2.1 on eight identical prompts to explore synthetic training data for rust segmentation. Both generated promising samples and masks with missing rust, shifted boundaries or false positives. I then expanded the work to 502 image mask pairs, including the pilot. After visual screening, 400 remained and 102 were excluded: a 79.7% retention rate. That is an encouraging starting set for training, with room to expand it further. Two engineering notes document the comparison and the larger review, with interactive mask overlays. RF-DETR training and real-image evaluation come next. Part 1 — 14 October 2026: GPT Image vs Nano Banana, eight prompts and interactive mask comparisons. https://www.antal.ai/blog/synthetic-rust-masks-gpt-image-vs-nano-banana.html?utm_source=reddit&utm_medium=social&utm_campaign=rust_segmentation_2026_10&utm_content=pilot Part 2 — 16 October 2026: generation and dataset review — 502 inspected, 400 retained, 102 excluded. https://www.antal.ai/blog/synthetic-rust-dataset-generation-review.html?utm_source=reddit&utm_medium=social&utm_campaign=rust_segmentation_2026_10&utm_content=review #ComputerVision #SyntheticData #ImageSegmentation
