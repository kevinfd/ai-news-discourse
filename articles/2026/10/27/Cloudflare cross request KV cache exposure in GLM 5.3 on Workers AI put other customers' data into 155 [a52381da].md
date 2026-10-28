---
id: "a52381da3bc8fdfa"
title: "Cloudflare: cross request KV cache exposure in GLM 5.3 on Workers AI put other customers' data into 155 responses"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xgr6zx/cloudflare_cross_request_kv_cache_exposure_in_glm"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xgr6zx/cloudflare_cross_request_kv_cache_exposure_in_glm"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T12:28:59Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["djcroman"]
language: "en"
summary: "Primary source (Cloudflare incident report): https://blog.cloudflare.com/kv-cache-exposure-remediation/ Cloudflare published a pretty candid write up yesterday. From Aug 27 to Sep 9, GLM 5.3 on Workers AI returned 155 responses that contained data from other customers' requests. All of them were answers to prompts longer than 681,280 tokens. Two things stacked up. The model was advertised with a…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research", "chips & infrastructure", "jobs & society", "search & media"]
content_source: "post"
word_count: 270
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xgr6zx/cloudflare_cross_request_kv_cache_exposure_in_glm/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Cloudflare: cross request KV cache exposure in GLM 5.3 on Workers AI put other customers' data into 155 responses

Reddit · djcroman · 2026-10-27

Primary source (Cloudflare incident report): https://blog.cloudflare.com/kv-cache-exposure-remediation/ Cloudflare published a pretty candid write up yesterday. From Aug 27 to Sep 9, GLM 5.3 on Workers AI returned 155 responses that contained data from other customers' requests. All of them were answers to prompts longer than 681,280 tokens. Two things stacked up. The model was advertised with a 1,048,576 token context window, but the KV cache pool on the prefill GPUs only fit 681,280 tokens. Cloudflare knew that and assumed SGLang would just reject anything too big. It did mark those requests as rejected, but in disaggregated prefill/decode mode the rejected request still looked alive. Prefill wrote a single placeholder page, said the transfer was done, and decode read all the reserved pages anyway, most of which still held earlier users' prompts. The client got a normal HTTP 200 and a coherent answer. What gets me is that nothing looked broken. No error, no garbage output, just an answer built partly on someone else's memory. Their own long context tests passed because they only checked status codes. Credit where it's due: Gadi Evron reported it via HackerOne, the model was pulled within about 40 minutes of the incident being declared and fixed the same day, and they found no sign of deliberate exploitation. The same SGLang bug had already been filed upstream on July 6 though. Fixes are in SGLang v0.5.20 to v0.5.22. Has anyone here actually asked their inference provider how they isolate tenants in GPU memory? Feels like a question that should be in every vendor review now. I also wrote a longer breakdown with diagrams (my own site): https://go.djcroman.com/cloudflare-kv-leak?p=reddit
