---
id: "5412cb37c9448e86"
title: "Show HN: Daily GPU Rental Prices Across AWS, Azure, RunPod and Vast.ai"
url: "https://taipeiledger.com/gpu"
link: "https://taipeiledger.com/gpu"
source: "taipeiledger.com"
domain: "taipeiledger.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-11T02:50:01Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["khoonie"]
language: "en"
summary: "What one GPU-hour costs to rent, in US dollars, by GPU model and provider. Prices of 11 November 2026.\nCompute only: storage and data transfer cost extra (for Vast.ai, see below). Hover a price for the instance it comes from. * = source not updated today; last price shown.\nData transfer and disk on Vast.ai\nEach Vast.ai host sets its own charge for data sent to and from the machine, billed per GB…"
tags: []
orgs: ["Amazon", "Microsoft"]
topics: ["chips & infrastructure", "models & research"]
content_source: "fulltext"
word_count: 311
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50449232"
score: 11
comments: 2
community: "Hacker News"
---

# Show HN: Daily GPU Rental Prices Across AWS, Azure, RunPod and Vast.ai

taipeiledger.com · khoonie · 2026-11-11

What one GPU-hour costs to rent, in US dollars, by GPU model and provider. Prices of 11 November 2026.
Compute only: storage and data transfer cost extra (for Vast.ai, see below). Hover a price for the instance it comes from. * = source not updated today; last price shown.
Data transfer and disk on Vast.ai
Each Vast.ai host sets its own charge for data sent to and from the machine, billed per GB on top of the
hourly price. Most charge little, but some charge US$30 or more per TB in each direction, which can outweigh a lower
hourly price when large datasets or model weights are moved. Charges of the same day's offers, in US$ per TB
(1 TB = 1,000 GB).
Highest and US$30+ count the dearer direction of each offer. The hourly
price includes a small default disk; more disk is charged per GB-month. AWS and Azure charge for data sent out to the
internet: see AWS data transfer and
Azure bandwidth pricing.
Price history
Daily since 02 November 2026.
How these prices are measured
Per GPU-hour. Clouds rent whole machines, so a machine's hourly price is divided by the GPUs in it (for example AWS p5.48xlarge, 8 × H100, ÷ 8). Compute only: storage, data transfer and support are extra and differ by provider.
List prices. AWS (US East, N. Virginia) and Azure (East US) on-demand Linux prices; RunPod Secure Cloud (its own data centres) and Community Cloud (third-party hosts). Committed-use and reserved prices are usually lower and are not shown.
Marketplace. Vast.ai lists machines offered by many independent hosts worldwide; the median and the lowest per-GPU price of the rentable on-demand offers that day, with the number of offers. Few offers means the figure can swing.
Checks. A list price that moves more than 50% in a day is held at the previous value until checked.
