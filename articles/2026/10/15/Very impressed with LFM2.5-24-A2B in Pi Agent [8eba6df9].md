---
id: "8eba6df90126f465"
title: "Very impressed with LFM2.5-24-A2B in Pi Agent"
url: "https://reddit.com/r/LocalLLaMA/comments/1x68qma/very_impressed_with_lfm2524a2b_in_pi_agent"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T01:22:04Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Thrumpwart"]
language: "en"
summary: "Just downloaded the new LFm2.5-24B-A2B LiquidAI model for testing. They claimed some pretty good performance, and I've had good experiences with their prior releases. Some context - I use Ornith 1.5-35B pretty regularly in multiple workflows - sometimes on it's own, and sometimes as part of an AI-Council in Pi Agent. It's been very reliable, provides surprising insight \"smarter\" models miss, and…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "post"
word_count: 241
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x68qma/very_impressed_with_lfm2524a2b_in_pi_agent/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Very impressed with LFM2.5-24-A2B in Pi Agent

Reddit · Thrumpwart · 2026-10-15

Just downloaded the new LFm2.5-24B-A2B LiquidAI model for testing. They claimed some pretty good performance, and I've had good experiences with their prior releases. Some context - I use Ornith 1.5-35B pretty regularly in multiple workflows - sometimes on it's own, and sometimes as part of an AI-Council in Pi Agent. It's been very reliable, provides surprising insight "smarter" models miss, and is a great workhorse in Pi. I swapped LFM 24B in to replace Ornith in a few of my workflows - it is holding up REALLY well. It's very fast (~95 tps sustained in llama.cpp using ROCM on an AMD W7900 - latest llama.cpp build). The Q8 takes up 30GB vram with full 128k context. It hasn't failed me yet in my mechanical tasks - it just keeps going and going and going and seems to tick all the boxes for a "little" model I run alongside a larger or smarter model on my other GPU. For "insight" I'll have to test it longer in my council-mode workflow but I will report back. Just wanted to give my $0.02 (CAD) on this model - it is very competent with Pi and worth your time to check out. The speed alone is a nice upgrade, and for my more basic tasks, even long running recursive tasks, it is holding up very nicely. Kudos to the LiquidAI team, this one is going to get alot of use on my chonky boi.
