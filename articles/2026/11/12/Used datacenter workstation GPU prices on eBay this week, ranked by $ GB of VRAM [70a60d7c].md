---
id: "70a60d7cd198d3ff"
title: "Used datacenter/workstation GPU prices on eBay this week, ranked by $/GB of VRAM"
url: "https://reddit.com/r/LocalLLaMA/comments/1xur9ud/used_datacenterworkstation_gpu_prices_on_ebay"
link: "https://reddit.com/r/LocalLLaMA/comments/1xur9ud/used_datacenterworkstation_gpu_prices_on_ebay"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T22:49:43Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["MzCWzL"]
language: "en"
summary: "edit: I am a moron with reddit formatting hang tight I've been tracking ebay listings that ship to the US for the GPUs people here actually buy, ranked by $/GB of VRAM. here's today's snapshot: Card Low end US-only low end Low-end $/GB Bandwidth $ per GB/s Tesla P100 16GB $174 $159 $10.88 732 GB/s $0.24 Tesla P40 24GB $280 - (7 US) $11.67 346 GB/s $0.81 Tesla V100 16GB (mostly SXM2) $220 $238…"
tags: ["r/LocalLLaMA"]
orgs: ["Tesla"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 629
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xur9ud/used_datacenterworkstation_gpu_prices_on_ebay/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Used datacenter/workstation GPU prices on eBay this week, ranked by $/GB of VRAM

Reddit · MzCWzL · 2026-11-12

edit: I am a moron with reddit formatting hang tight I've been tracking ebay listings that ship to the US for the GPUs people here actually buy, ranked by $/GB of VRAM. here's today's snapshot: Card Low end US-only low end Low-end $/GB Bandwidth $ per GB/s Tesla P100 16GB $174 $159 $10.88 732 GB/s $0.24 Tesla P40 24GB $280 - (7 US) $11.67 346 GB/s $0.81 Tesla V100 16GB (mostly SXM2) $220 $238 $13.75 900 GB/s $0.24 Instinct MI50 16GB $268 - (3 US) $16.75 1,024 GB/s $0.26 Instinct MI50 32GB $702 - (2 US) $21.93 1,024 GB/s $0.69 Tesla V100 32GB $949 $807 $29.66 900 GB/s $1.05 Quadro RTX 8000 48GB $2,111 $2,000 $43.99 672 GB/s $3.14 Instinct MI100 32GB $1,490 - (6 US) $46.56 1,229 GB/s $1.21 RTX 3090 24GB $1,790 $1,737 $74.58 936 GB/s $1.91 RTX A6000 48GB $4,600 $4,400 $95.83 768 GB/s $5.99 RTX 4090 48GB (modded) $5,390 — (1 US) $112.29 1,008 GB/s $5.35 A100 40GB $4,799 $6,020 $119.98 1,555 GB/s $3.09 A100 80GB $13,995 $13,995 $174.94 1,935 GB/s $7.23 CMP 170HX 40GB (10GB card, unlocked) $2,950 — (6 US) $73.75 1,555 GB/s $1.90 CMP 170HX 64GB (8GB card, unlocked) $4,510 — (7 US) $70.46 1,493 GB/s $3.02 Radeon AI Pro R9700 32GB $2,430 $2,250 $75.94 640 GB/s $3.80 all asking prices, single cards, fixed-price, not for-parts. "low end" is the 10th % of credible listings i.e. what a patient buyer can actually land, not a too-good-to-be-true outlier. "-" in the US-only column means fewer than 10 US listings. $/GB/s is just the low end divided by bandwidth. I had been eyeing the MI100 myself for a while at the $1100 ish it hovered at for ages... looks like even that is going up. I did end up buying a 8x V100 32GB server for $5400 in early Sept. those prices are long gone, equivalent server is now $11k for an OG DGX Station (no memory). the exact inspur server is now $13k for 8x 9 year old GPUs. insanity. I hope prices come back down to earth soon but don't think that's actually gonna happen. some notes: - P100, V100 16GB and MI50 16GB all work out to about $0.25 per GB/s. the P40 looks cheap per GB of VRAM but costs over 3x as much per GB/s, since its only got about a third of a V100's bandwidth. people are having opus 5.5 write megakernels for these cards that are working surprisingly well. - V100 16GB at ~$14/GB looks like the best deal in the table, but 38 of the 40 cheapest are SXM2 modules, so budget for an adapter or an SXM2 server. the cheapest 32GB V100s are SXM3 (DGX-2) modules, which aren't drop-in either. - MI50 32GB is under a third of a 3090's $/GB at similar bandwith, assuming ROCm cooperates. - if you want 48GB on one card, a Quadro RTX 8000 is less than half the price of an A6000 or a modded 4090 48GB. - of the consumer and workstation cards, the 3090 is the cheapest per GB/s by a wide margin. an A100 40GB costs about the same per GB/s as an RTX 8000. - for what it's worth, buying from a US seller usually doesn't cost more: the US-only low end is at or below the global one for the P100, V100 32GB, RTX 8000, 3090 and A6000. it's about $20 more for the V100 16GB and $1,200 more for the A100 40GB, and the P40 and MI50 barely exist in the US. full data and per-card listings, with a US-only filter: https://rackbites.com . prices are asking, not sold - ebay's sold-data API is super restricted. edit: added CMP 170HX edit2: added R9700 edit3: full builds here https://rackbites.com/builds with benchmarks and other useful/relevant info
