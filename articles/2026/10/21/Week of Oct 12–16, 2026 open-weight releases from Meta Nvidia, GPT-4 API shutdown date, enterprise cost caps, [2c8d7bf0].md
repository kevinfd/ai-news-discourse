---
id: "2c8d7bf002a63045"
title: "Week of Oct 12–16, 2026: open-weight releases from Meta/Nvidia, GPT-4 API shutdown date, enterprise cost caps, and regulatory probes"
url: "https://reddit.com/r/artificial/comments/1xbkezt/week_of_oct_1216_2026_openweight_releases_from"
link: "https://reddit.com/r/artificial/comments/1xbkezt/week_of_oct_1216_2026_openweight_releases_from"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T11:18:48Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["ksraj1001"]
language: "en"
summary: "Roundup of what I found this week. Caveat: much of this is via news aggregators citing Reuters/Bloomberg/The Information, so some items are second-hand. Open weights Meta's Muse Spark Open: MoE, 816B total / 42B active, 1M context; reportedly runs on 2–4 M5 Ultra Mac Studios via MLX. Nvidia Nemotron 3.5 Super VL: 120B total / 12B active, 1M context, claims up to 5x throughput (vendor claim).…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Meta", "Nvidia", "Anthropic", "Microsoft", "US government"]
topics: ["models & research", "policy & regulation", "chips & infrastructure", "products & launches"]
content_source: "post"
word_count: 236
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xbkezt/week_of_oct_1216_2026_openweight_releases_from/"
score: null
comments: null
community: "r/artificial"
---

# Week of Oct 12–16, 2026: open-weight releases from Meta/Nvidia, GPT-4 API shutdown date, enterprise cost caps, and regulatory probes

Reddit · ksraj1001 · 2026-10-21

Roundup of what I found this week. Caveat: much of this is via news aggregators citing Reuters/Bloomberg/The Information, so some items are second-hand. Open weights Meta's Muse Spark Open: MoE, 816B total / 42B active, 1M context; reportedly runs on 2–4 M5 Ultra Mac Studios via MLX. Nvidia Nemotron 3.5 Super VL: 120B total / 12B active, 1M context, claims up to 5x throughput (vendor claim). Black Forest Labs FLUX 3 Image Klein: 5.6B, free commercial use under $5M revenue. Microsoft's MAI-Base-2 (2.8T/80B active) is not open; trusted partners via Foundry. Cost / platform Accenture reportedly capped centrally funded Claude at $29/month/employee after some spent $500–$1,000. OpenAI: GPT-4o, 4o mini, 4.1, 4.1 mini removed from the API Jan 14, 2027 (per OpenAI release notes as aggregated by Releasebot). Policy FTC civil investigative demands to OpenAI and Anthropic over safety incidents (Axios, via aggregator); EU AI Office's first AI Act probes. My take as someone building on top of these APIs: the deprecation timeline is the thing that actually costs me engineering time. Six months is fine if you have evals; painful if you don't. I'm also skeptical of "runs on a Mac Studio" headlines until I see sustained throughput numbers at long context. Open weights are attractive for data-sensitive clients, but I'd want to see real total cost including ops before calling it cheaper. Curious what others are seeing on migration effort off the GPT-4 family.
