---
id: "ef7c18df0b5b38b4"
title: "We turned 10 years of ML papers into one page per topic: benchmark records, what got tried, what reviewers expect [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xmk8rx/we_turned_10_years_of_ml_papers_into_one_page_per"
link: "https://reddit.com/r/MachineLearning/comments/1xmk8rx/we_turned_10_years_of_ml_papers_into_one_page_per"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T05:09:18Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["latenticlabs"]
language: "en"
summary: "We've been working on this for a while and shipped it today. We took every accepted paper from ICML, NeurIPS, ICLR, CVPR and AAAI since 2016 (about 109k), grouped them into ~1,260 topics, and pulled the results tables and ablations out of the full text of 79k of them. The research map just shows the grouping, but each topic page shows what the papers actually report. Here's the one for…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 258
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xmk8rx/we_turned_10_years_of_ml_papers_into_one_page_per/"
score: null
comments: null
community: "r/MachineLearning"
---

# We turned 10 years of ML papers into one page per topic: benchmark records, what got tried, what reviewers expect [P]

Reddit · latenticlabs · 2026-11-03

We've been working on this for a while and shipped it today. We took every accepted paper from ICML, NeurIPS, ICLR, CVPR and AAAI since 2016 (about 109k), grouped them into ~1,260 topics, and pulled the results tables and ablations out of the full text of 79k of them. The research map just shows the grouping, but each topic page shows what the papers actually report. Here's the one for compact/efficient Gaussian splatting: https://atlas.scime.ai/research/3d-vision/gaussian-splatting/compact-and-efficient-gaussian-splatting A few things it shows: - the topic went from 29 papers in 2023-24 to 240 in 2025-26 - best reported numbers per benchmark over time, with the paper that set each one. Deep Blending PSNR, for example, has barely moved (30.42 → 30.45) - ablations from recent papers, including the ones that hurt - what recent papers compare against: 38 of 113 use 3DGS as a baseline, then 2DGS, Scaffold-GS, Mip-Splatting - recent arXiv preprints on the topic and a BibTeX file of the key papers The pages are computed from the extracted numbers, and every number links to its paper. Extraction isn't perfect and numbers from different papers aren't always comparable, so treat it as a starting point, not a leaderboard. Free, no signup. All topics: https://atlas.scime.ai/research If you know a topic well and something's off, please tell us. That's the most useful feedback right now. Note: Benchmark numbers and ablations from 2026 papers aren't in yet. We're working on them now, so for now the records on topic pages mostly reflect papers up to 2025. We'll update here when they're ready.
