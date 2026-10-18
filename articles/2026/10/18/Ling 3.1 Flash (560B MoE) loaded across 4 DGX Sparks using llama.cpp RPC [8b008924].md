---
id: "8b008924045b8661"
title: "Ling 3.1 Flash (560B MoE) loaded across 4 DGX Sparks using llama.cpp RPC"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8v7cp/ling_31_flash_560b_moe_loaded_across_4_dgx_sparks"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8v7cp/ling_31_flash_560b_moe_loaded_across_4_dgx_sparks"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T05:37:02Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["BerryBlush_Rogers691"]
language: "en"
summary: "sudoing posted that he's loaded Ling 3.1 Flash across four DGX Sparks. It's a 560B MoE with 25B active parameters per token. He'd enjoyed the earlier Ling models and wanted to test this one, but it wouldn't fit on his two Sparks with the setup he was trying. someone in Germany gave him access to a four-Spark setup. He's using Atomic Chat's day-one Q4 GGUF, distributed across all four machines…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 168
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8v7cp/ling_31_flash_560b_moe_loaded_across_4_dgx_sparks/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Ling 3.1 Flash (560B MoE) loaded across 4 DGX Sparks using llama.cpp RPC

Reddit · BerryBlush_Rogers691 · 2026-10-18

sudoing posted that he's loaded Ling 3.1 Flash across four DGX Sparks. It's a 560B MoE with 25B active parameters per token. He'd enjoyed the earlier Ling models and wanted to test this one, but it wouldn't fit on his two Sparks with the setup he was trying. someone in Germany gave him access to a four-Spark setup. He's using Atomic Chat's day-one Q4 GGUF, distributed across all four machines through llama.cpp RPC. According to his post, there wasn't an official FP4 build for vLLM available at the time, which is why he went with this route. No performance numbers in the screenshot yet. He expects bandwidth and speed to be painful, but wants to see how it compares with the 124B Ling 3.0 Flash. That's the comparison I'm interested in too: how much the larger model changes answer quality, and what the waiting time looks like in actual use. Links for anyone following along: Atomic Chat's Ling 3.1 Flash GGUF repository llama.cpp Official Ling 3.1 Flash model
