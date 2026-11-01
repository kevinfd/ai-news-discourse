---
id: "3913112760390add"
title: "Rented some server time and wanted to share some learnings from benching using RAM heavier servers with some decent GPU: AMD EPYC and ROME motherboards really *ARE* worth it: Qwen 3.8 Flash Next Unsloth Q8 at 94 tok/s c=1, 456 tok/s c=8 ."
url: "https://reddit.com/r/LocalLLaMA/comments/1xkvp10/rented_some_server_time_and_wanted_to_share_some"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkvp10/rented_some_server_time_and_wanted_to_share_some"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T06:09:18Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["sleight42"]
language: "en"
summary: "Raw data in the comments, if you go for that sort of thing. The TL;DR This build generates a nearly linear performance per stream up to at least 8 streams using a context window of 124k. I didn't test beyond that. Abstract Until today, I considered Strata a toy. I don't anymore. Rented a few instances on vast.ai to do some benching. Blew about $40 in all on the benchmarking. Tested against 2x…"
tags: ["r/LocalLLaMA"]
orgs: ["AMD", "Alibaba"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 328
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkvp10/rented_some_server_time_and_wanted_to_share_some/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Rented some server time and wanted to share some learnings from benching using RAM heavier servers with some decent GPU: AMD EPYC and ROME motherboards really *ARE* worth it: Qwen 3.8 Flash Next Unsloth Q8 at 94 tok/s c=1, 456 tok/s c=8 .

Reddit · sleight42 · 2026-11-01

Raw data in the comments, if you go for that sort of thing. The TL;DR This build generates a nearly linear performance per stream up to at least 8 streams using a context window of 124k. I didn't test beyond that. Abstract Until today, I considered Strata a toy. I don't anymore. Rented a few instances on vast.ai to do some benching. Blew about $40 in all on the benchmarking. Tested against 2x AMD EPYC 7642 on ROME2D32GM-2T motherboard with 251GB and 504GB DDR4 respectively with 2x 3090 (one actually had 4x but only 2x were used). The runtimes and models Using Strata (up to unsloth Q8) and Maya (GLM 5.3F and DSV4.1F) at various model sizes. The Results Don't even consider > C=1 for Maya. Strata? From > 100 tok/s down to just over 50 tok/s (at Q_8). The part that blew my mind and made me want to post: You can get almost linear concurrent stream performance scaling up to at least 8 streams on QFN 3.8 Q8 with this build. Workstation and server builds are worth it: you don't have to fight so much for VRAM; a couple of decent GPUs and you're off to the races. Instead it's DRAM (which sucks a whole lot less to buy--even though it still sucks) and CPUs (which aren't too bad at all) GLM and DSV: they'd likely benefit from more VRAM. But, again, 1.5k+ for a 3090, paying at least what they sold for 6-7 years ago? It's insulting. See comments for the boring as hell raw data. DISCLAIMER: Totally not an advertisement. Like buying a car, if I can, I want to take it for a spin before I buy. Vast.ai is amazing this way. If you can find a machine spec that you're even the least bit curious about, you lease some time on it (paying a bit extra for storage), download the runtime and models you want to test, and fire up the benches.
