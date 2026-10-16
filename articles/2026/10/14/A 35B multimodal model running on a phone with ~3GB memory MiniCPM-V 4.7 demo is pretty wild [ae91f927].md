---
id: "ae91f927c146036b"
title: "A 35B multimodal model running on a phone with ~3GB memory? MiniCPM-V 4.7 demo is pretty wild"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5uwnd/a_35b_multimodal_model_running_on_a_phone_with"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5uwnd/a_35b_multimodal_model_running_on_a_phone_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T15:53:48Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Equivalent-Grass-527"]
language: "en"
summary: "Just saw this demo from OpenBMB for MiniCPM-V 4.7 , and the on-device capability is pretty impressive. A 35B-A3B MoE vision-language model running locally on mobile devices is already interesting, but the use cases are what caught my attention: 📷 Reading real-world signs 📄 Understanding complex documents 🧠 Reasoning over visual information 🗺️ Planning with real-world constraints The key piece…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research"]
content_source: "post"
word_count: 156
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5uwnd/a_35b_multimodal_model_running_on_a_phone_with/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# A 35B multimodal model running on a phone with ~3GB memory? MiniCPM-V 4.7 demo is pretty wild

Reddit · Equivalent-Grass-527 · 2026-10-14

Just saw this demo from OpenBMB for MiniCPM-V 4.7 , and the on-device capability is pretty impressive. A 35B-A3B MoE vision-language model running locally on mobile devices is already interesting, but the use cases are what caught my attention: 📷 Reading real-world signs 📄 Understanding complex documents 🧠 Reasoning over visual information 🗺️ Planning with real-world constraints The key piece seems to be LES (Lookahead Expert Scheduling) — instead of just making the model smaller, they optimize MoE inference by predicting and preloading experts to reduce bottlenecks. They also released a smaller MiniCPM-V 4.7 1B model for more resource-constrained devices. Another interesting addition is Self-Replay Fine-Tuning (SRFT) , which aims to let developers customize the model for specific tasks while keeping general capabilities. The direction is interesting: instead of sending every image/question to the cloud, we're getting closer to having capable multimodal assistants running directly on phones. Links: GitHub: https://github.com/OpenBMB/MiniCPM-V Hugging Face: https://huggingface.co/collections/openbmb SRFT details: https://openbmb.cn/en/blog/self-replay-fine-tuning
