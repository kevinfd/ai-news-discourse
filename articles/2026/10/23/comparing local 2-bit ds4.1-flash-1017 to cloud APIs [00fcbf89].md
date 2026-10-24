---
id: "00fcbf8993967891"
title: "comparing local 2-bit ds4.1-flash-1017 to cloud APIs"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdh4xs/comparing_local_2bit_ds41flash1017_to_cloud_apis"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdh4xs/comparing_local_2bit_ds41flash1017_to_cloud_apis"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T15:26:30Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["bakawolf123"]
language: "en"
summary: "Saw this https://x.com/nothingto12/status/2113446055589056718 (in short it compares opencode go ds4.1 and ds4.1 via deepseek API) discussed on opencode reddit and decided to test same prompt myself on 2bit quant locally. it took around 1.5h, ran with 450k context (auto-compaction enabled), didn't have playwright - it tested on headless chrome result on the video above. interestingly the KDL I've…"
tags: ["r/LocalLLaMA"]
orgs: ["Perplexity"]
topics: []
content_source: "post"
word_count: 135
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdh4xs/comparing_local_2bit_ds41flash1017_to_cloud_apis/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# comparing local 2-bit ds4.1-flash-1017 to cloud APIs

Reddit · bakawolf123 · 2026-10-23

Saw this https://x.com/nothingto12/status/2113446055589056718 (in short it compares opencode go ds4.1 and ds4.1 via deepseek API) discussed on opencode reddit and decided to test same prompt myself on 2bit quant locally. it took around 1.5h, ran with 450k context (auto-compaction enabled), didn't have playwright - it tested on headless chrome result on the video above. interestingly the KDL I've measured vs baseline is quite bad: original → oQ2e is 0.4259 nats, original → oQ2.5e is 0.2821. Reverse oQ2.5e → oQ2e is 0.1943 nats. Perplexity: original 3.7315, oQ2.5e 4.1190, oQ2e 4.6333. top-1 agreement is 78.43% for 2 bit one. Really weird to me that this still works like it does: on glm5.3-flash difference between KDLs from baseline for calibrated and non-calibrated quants was 0.12 (~0.24 vs 0.12 oQ4e) and it was very noticeable in quality for me.
