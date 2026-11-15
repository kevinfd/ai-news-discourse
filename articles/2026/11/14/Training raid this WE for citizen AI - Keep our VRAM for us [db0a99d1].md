---
id: "db0a99d1895cda39"
title: "Training raid this WE for citizen AI - Keep our VRAM for us"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xw59wv/training_raid_this_we_for_citizen_ai_keep_our"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xw59wv/training_raid_this_we_for_citizen_ai_keep_our"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-14T15:35:26Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["OrganizationTop9026"]
language: "en"
summary: "Why do most folks with an 8 GB or 16 GB desktop GPU sit out distributed LLM runs? It usually comes down to three annoying bottlenecks. Nobody wants to punch holes in their home router. Nobody wants to run untrusted pickle checkpoints off the internet. And nobody wants a background trainer freezing their VRAM when they sit down to play or work. This weekend (November 14-15 CET), I hooked my…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 172
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xw59wv/training_raid_this_we_for_citizen_ai_keep_our/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Training raid this WE for citizen AI - Keep our VRAM for us

Reddit · OrganizationTop9026 · 2026-11-14

Why do most folks with an 8 GB or 16 GB desktop GPU sit out distributed LLM runs? It usually comes down to three annoying bottlenecks. Nobody wants to punch holes in their home router. Nobody wants to run untrusted pickle checkpoints off the internet. And nobody wants a background trainer freezing their VRAM when they sit down to play or work. This weekend (November 14-15 CET), I hooked my HiveMind coordinator up with CrowdGPT (led by Vxtzq) to test a citizen-trained run around Crowd-v1, an open base model with a 658M transformer trunk (roughly 1.01B parameters total with its 151k-vocab CrowdEngram table). Setup takes five minutes. Communication uses plain outbound HTTPS on port 443 with zero inbound listeners, weights move strictly as SHA-256 verified safetensors (no torch.load or pickle anywhere), and updates pass MultiKrum outlier filtering plus held-out loss checks before merging via DiLoCo. Honest caveat first: this is still an experimental PoC, not a polished cloud service, so please do not send private prompts or sensitive keys through volunteer nodes.
