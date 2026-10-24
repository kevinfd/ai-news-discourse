---
id: "5234a9024be8a458"
title: "Gyro quants looks like EXL3 but kinda closed source. please explain why we need this."
url: "https://reddit.com/r/LocalLLaMA/comments/1xe41qe/gyro_quants_looks_like_exl3_but_kinda_closed"
link: "https://reddit.com/r/LocalLLaMA/comments/1xe41qe/gyro_quants_looks_like_exl3_but_kinda_closed"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T09:17:15Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["nasone32"]
language: "en"
summary: "Recently this new quant has popped up called Gyro. It is gaining popularity because it's being inserted into many different engines, especially the recently popular Strata. So i took a dive into the code to see the differences between Gyro and EXL3, to me it looks like simply a different flavor of EXL3 quantization, but it's not interoperable and the recipe to make it is closed source for now.…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: []
content_source: "post"
word_count: 202
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xe41qe/gyro_quants_looks_like_exl3_but_kinda_closed/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Gyro quants looks like EXL3 but kinda closed source. please explain why we need this.

Reddit · nasone32 · 2026-10-24

Recently this new quant has popped up called Gyro. It is gaining popularity because it's being inserted into many different engines, especially the recently popular Strata. So i took a dive into the code to see the differences between Gyro and EXL3, to me it looks like simply a different flavor of EXL3 quantization, but it's not interoperable and the recipe to make it is closed source for now. Property Gyro-S / Gyro-M EXL3 Quantization family QTIP / Trellis-coded quantization QTIP / Trellis-coded quantization Hadamard rotations Yes Yes Trellis state size 15 bits 16 bits Encoding unit 128-weight blocks 256-weight tiles (standard path) Codebook Explicit LUT with 2,048 2D points Procedural codebook Weight reconstruction State hashing + lookup table Procedural value generation Bit packing format TQ2_T , TQK6 , TQK7 EXL3-specific packing Direct interoperability Not demonstrated Not demonstrated I did not find any published evidence that it's better than EXL3 on either decode speed, or perplexity/KLD/top 1%. I'm not dunking on Agentionai but I kinda hate how this only makes the community more fragmented without providing any benefit. EXL3 is not very publicized while this Gyro is gaining popularity with aggressive brading (socials and stuff). " Agention Precision Rotor "... please, proof....
