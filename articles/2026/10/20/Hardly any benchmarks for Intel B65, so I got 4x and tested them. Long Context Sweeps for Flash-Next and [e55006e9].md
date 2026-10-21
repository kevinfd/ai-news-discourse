---
id: "e55006e93a41c0b5"
title: "Hardly any benchmarks for Intel B65, so I got 4x and tested them. Long Context Sweeps for Flash-Next and other models"
url: "https://reddit.com/r/LocalLLaMA/comments/1xavy8t/hardly_any_benchmarks_for_intel_b65_so_i_got_4x"
link: "https://reddit.com/r/LocalLLaMA/comments/1xavy8t/hardly_any_benchmarks_for_intel_b65_so_i_got_4x"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T15:57:27Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["SamSausages"]
language: "en"
summary: "EDIT: Note that I built off the official vllm documentation and I just got done validating the system. This is now my control. That means this is a slow and stable config. Now that i have a baseline control I’m going to begin tweaking settings for performance runs. I’ll make posts as I find settings that improve performance. For example, I already know that I can cut prefill times by increasing…"
tags: ["r/LocalLLaMA"]
orgs: ["Intel"]
topics: ["models & research"]
content_source: "post"
word_count: 603
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xavy8t/hardly_any_benchmarks_for_intel_b65_so_i_got_4x/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Hardly any benchmarks for Intel B65, so I got 4x and tested them. Long Context Sweeps for Flash-Next and other models

Reddit · SamSausages · 2026-10-20

EDIT: Note that I built off the official vllm documentation and I just got done validating the system. This is now my control. That means this is a slow and stable config. Now that i have a baseline control I’m going to begin tweaking settings for performance runs. I’ll make posts as I find settings that improve performance. For example, I already know that I can cut prefill times by increasing chunk size. Howdy Folks! New batch of tests from my 4x B65 rig I built, because I was curious to test how the high memory bandwidth works out in reality. This time doing long context sweeps for our most popular models! If there are specific tests that you want to see, hit me up and I'll see if I can fit them in. I'm also starting offload tests, where I put some of the layers into system RAM. So far only doing it with flash-next, but interesting results in the "by model" section of my site for flash-next. Some Examples below, full context sweep list of all the models I tested: https://b65.thekaiser.us/matrices/ AI Generated table from my data: Qwen3.8 Flash-Next and 27B — Intel Arc Pro B65 context sweeps All numbers are overall output throughput in tokens/sec , measured across repeated requests during each 30-second test. This includes waits between requests; it is not prompt-processing speed. Columns show requested simultaneous requests. Context lengths use K = 1,024 tokens. * = requests queued/capacity-limited. — = skipped as over capacity. Flash-Next W4A16 — 4× B65 — MTP-3 enabled vLLM 0.30.0 · October 18, 2026 Context 1 request 2 requests 4 requests 0 84.5 145.6 243.2* 16K 73.4 115.4* 166.4* 32K 71.0 105.7* 137.3* 64K 68.6 109.3* 143.7* 128K 55.0 72.3* — 200K 45.8 66.2* — Full results Flash-Next W4A16 — 4× B65 — MTP disabled vLLM 0.30.0 · October 18, 2026 Context 1 request 2 requests 4 requests 0 42.7 85.1 159.2 16K 40.8 79.4 141.9* 32K 39.3 75.2* 127.3* 64K 38.6 73.5 127.6 128K 34.5 61.2* 101.7* 200K 31.5 57.0* — Full results Qwen3.8-27B INT4 — 1× B65 vLLM 0.31.0+xpu.llmscaler · October 19, 2026 Context 1 request 2 requests 4 requests 8 requests 16 requests 0 20.2 59.9 115.1 204.3 159.3 8K 19.8 57.4 106.6 184.5 144.8 32K 18.2 48.2* 84.0 — — 64K 16.7 42.1* — — — 128K 14.6 — — — — Full results Qwen3.8-27B INT4 — 4× B65 vLLM 0.31.0+xpu.llmscaler · October 19, 2026 Context 1 request 2 requests 4 requests 8 requests 16 requests 0 50.4 129.8 253.4 468.2 458.1 8K 49.4 125.9 239.6 417.1 422.8 32K 46.2 108.7* 197.7* 310.6* 332.8 64K 43.5 96.3* 172.2 270.9* 286.2 128K 37.8 76.0* 121.8* 181.8* — 200K 33.8 63.3* 97.9* — — Full results Qwen3.8-27B FP8 — 4× B65 vLLM 0.32.0 · October 19, 2026 Context 1 request 2 requests 4 requests 8 requests 16 requests 0 30.5 59.7 116.2 222.8 404.2 8K 30.0 58.6 111.6 205.8 354.5 32K 28.7 54.4 98.5 177.4 269.7 64K 27.9 52.3 94.0* 164.3* 242.3* 128K 25.3 46.3 78.9* 117.2* — 200K 23.2 41.3 66.9* — — Full results Qwen3.8-27B BF16 — 4× B65 vLLM 0.32.0 · October 19, 2026 Context 1 request 2 requests 4 requests 8 requests 16 requests 0 28.6 56.2 110.0 211.0 389.5 8K 28.1 55.2 106.2 197.9 357.6 32K 27.1 52.1 96.5* 176.9 287.0 64K 26.0 49.5* 91.3 159.1* — 128K 24.0 45.1 79.3* — — 200K 22.7 40.3 67.7* — — Full results These are throughput measurements, not model-quality scores. Engine versions differ between configurations. Starred results include queueing and should not be interpreted as fully sustained requested concurrency.
