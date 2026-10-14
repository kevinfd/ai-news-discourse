---
id: "63ac67d713c89c14"
title: "What’s possible with 2x5090 + 64GB RAM?"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5i6dt/whats_possible_with_2x5090_64gb_ram"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T04:38:48Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["nok01101011a"]
language: "en"
summary: "Hey there, coming from the 3D rendering sector, I happen to have a somewhat potent system that I thought I may exploit for local LLM generations (app development). I’ve experimented now for about three weeks, but feel stuck regarding usability and speed. First of all, where do you guys acquire the latest knowledge without reading every custom commits ever released? As for usability, I’ve tried…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["products & launches", "business & funding", "agents & coding"]
content_source: "post"
word_count: 290
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5i6dt/whats_possible_with_2x5090_64gb_ram/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# What’s possible with 2x5090 + 64GB RAM?

Reddit · nok01101011a · 2026-10-14

Hey there, coming from the 3D rendering sector, I happen to have a somewhat potent system that I thought I may exploit for local LLM generations (app development). I’ve experimented now for about three weeks, but feel stuck regarding usability and speed. First of all, where do you guys acquire the latest knowledge without reading every custom commits ever released? As for usability, I’ve tried many webuis, apps and inference engines only to end up (due to my unqualified knowledge) with LM Studio Bionic. It’s not that I need a simplified app, but the agents just do their work compared to Unsloth Desktop. The main reason for not sticking with Unsloth was, that truncating (over LAN (server - client) the chat wasn’t possible (or very unreliable) and I was just wondering how do people develop apps at all with having the chat stop after reaching context limit. I use around 210k ontext size with Qwen Next GSQ RCO IQ3XXS + MTP and I need maybe 10-20 loops or so to get an app working solid. Is this something everyone struggles with or do I just use it wrong? However, I feel LM Studio does decent truncating, so I stick with it, however the speeds sticking with standard llama builds is from 80-30t/s (mostly running in the 40s). Using custom llama with Unsloth, I’ve got it to around 100-40t/s, but that’s it. Following this sub, made me realise that my GPUs are pretty underperforming compared to others results with much weaker hardware. So, I’d like to know from people with similar systems what speeds they achieve with what engine and how a proper development environment should look and be used like? What am I doing wrong? Any help is appreciated, thanks!
