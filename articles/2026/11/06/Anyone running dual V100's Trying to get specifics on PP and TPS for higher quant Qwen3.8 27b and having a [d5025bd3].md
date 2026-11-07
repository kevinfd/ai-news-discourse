---
id: "d5025bd3e5622629"
title: "Anyone running dual V100's? Trying to get *specifics* on PP and TPS for higher quant Qwen3.8 27b and having a tough time"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpfjua/anyone_running_dual_v100s_trying_to_get_specifics"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpfjua/anyone_running_dual_v100s_trying_to_get_specifics"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T15:26:07Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["FantasyMaster85"]
language: "en"
summary: "So I'm thinking of switching from my 32gb AMD MI60 to dual V100's (64gb VRAM total) and I've got 96gb of DDR5. My problem is I'm having a terrible time finding \"hard data\" on PP and TPS speeds on higher quants (q6 and q8 specifically) with large context windows (150-200k). I know that it will outperform my MI60, but I'm not just looking for \"yeah, it'll be faster\" I'm specifically looking to see…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD"]
topics: []
content_source: "post"
word_count: 209
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpfjua/anyone_running_dual_v100s_trying_to_get_specifics/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Anyone running dual V100's? Trying to get *specifics* on PP and TPS for higher quant Qwen3.8 27b and having a tough time

Reddit · FantasyMaster85 · 2026-11-06

So I'm thinking of switching from my 32gb AMD MI60 to dual V100's (64gb VRAM total) and I've got 96gb of DDR5. My problem is I'm having a terrible time finding "hard data" on PP and TPS speeds on higher quants (q6 and q8 specifically) with large context windows (150-200k). I know that it will outperform my MI60, but I'm not just looking for "yeah, it'll be faster" I'm specifically looking to see how much faster, because a 10% bump isn't worth it for me. I'm also looking to see from you experts if it's silly because of what I've read about support for CUDA being EoL for the card soon (or already did?). Hopefully I'm not beating a dead horse here, as I did go through other posts (lots of them) but it's just so difficult going through post after post where specifics aren't included "I'm getting 200tps on qwen3.8 27b" ...at what quant? at what context? using what KV settings? Lastly, if it is significantly faster, do those speedups (generally speaking) transfer to other models or is it only because of specific forks of llama.cpp were built out with this model and that card in mind? EDIT: forgot to add I’d be going with sxm2 not PCIe.
