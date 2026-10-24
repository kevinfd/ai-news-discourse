---
id: "db7b7082866df83f"
title: "Once cached, CyberTiel loads fully in 5.6s (vs. 13.7s on the first disk-bound load, lease included)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdt07p/once_cached_cybertiel_loads_fully_in_56s_vs_137s"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdt07p/once_cached_cybertiel_loads_fully_in_56s_vs_137s"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T23:11:55Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Distinct-Pie2389"]
language: "en"
summary: "Park in RAM. An engine that can offload itself (ComfyUI, vLLM, SGLang, or any engine that serves the park protocol ) moves its weights to system memory on a drain and resumes from there instead of reloading from disk. Berth parks only when the RAM it measures covers the engine plus a floor, and stops parked engines first when memory runs short. Swap numbers On the reference RTX 4090 with 64 GiB…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 130
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdt07p/once_cached_cybertiel_loads_fully_in_56s_vs_137s/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Once cached, CyberTiel loads fully in 5.6s (vs. 13.7s on the first disk-bound load, lease included)

Reddit · Distinct-Pie2389 · 2026-10-23

Park in RAM. An engine that can offload itself (ComfyUI, vLLM, SGLang, or any engine that serves the park protocol ) moves its weights to system memory on a drain and resumes from there instead of reloading from disk. Berth parks only when the RAM it measures covers the engine plus a floor, and stops parked engines first when memory runs short. Swap numbers On the reference RTX 4090 with 64 GiB of RAM, one chat request through llama-swap, from the request to the reply, lease included (2026-10-23): Switch | Time A 21 GB chat model, file in the page cache |5.6 s ComfyUI parks in RAM |under 1 s ComfyUI to a 27B chat model |13.6 to 16.3 s Strata's numbers and the method are in Benchmarks Repo: Berth
