---
id: "92fbfd226b6f8f2f"
title: "LLM Drives Car"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xv41ma/llm_drives_car"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xv41ma/llm_drives_car"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T10:05:55Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["No-Dragonfly6246"]
language: "en"
summary: "NVIDIA's Alpamayo 2 Edge is a vision-language-action model: it looks at a car's cameras, says what it's about to do and why, then plans the path. The model is trained in an RL loop (!) and takes in 6 cameras and the recent motion. Out of the box on a Jetson AGX Thor, the released PyTorch version takes ~0.6–0.8 s per plan, so a 20 Hz camera gets a new plan about once a second. We optimized it to…"
tags: ["r/ArtificialInteligence"]
orgs: ["Nvidia"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 114
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xv41ma/llm_drives_car/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# LLM Drives Car

Reddit · No-Dragonfly6246 · 2026-11-13

NVIDIA's Alpamayo 2 Edge is a vision-language-action model: it looks at a car's cameras, says what it's about to do and why, then plans the path. The model is trained in an RL loop (!) and takes in 6 cameras and the recent motion. Out of the box on a Jetson AGX Thor, the released PyTorch version takes ~0.6–0.8 s per plan, so a 20 Hz camera gets a new plan about once a second. We optimized it to 45 ms per plan, 20 decisions/s on the same board, so the plan and the reasoning keep up with the camera. Numbers, methodology, and a live run on a real Thor in your browser: https://embedl.com/nvidia/alpamayo2-edge/thor
