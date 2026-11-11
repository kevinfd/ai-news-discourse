---
id: "395ee1dfce4e22c2"
title: "Anyone willing to benchmark my MoE runtime on their M-series Mac?"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsyges/anyone_willing_to_benchmark_my_moe_runtime_on"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsyges/anyone_willing_to_benchmark_my_moe_runtime_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T20:57:02Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["dave-tro"]
language: "en"
summary: "I've built an inference backend optimized for M-series Macs that makes it possible to run larger MoE models on machines without eating up all the RAM (for example, it can run Qwen 3.8 Flash Next on a 24GB Mac) using SSD offloading along with architecture-specific optimizations for Apple Silicon. I've only been able to test a limited number of configurations so far, including my own machine and a…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Apple"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 268
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsyges/anyone_willing_to_benchmark_my_moe_runtime_on/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Anyone willing to benchmark my MoE runtime on their M-series Mac?

Reddit · dave-tro · 2026-11-10

I've built an inference backend optimized for M-series Macs that makes it possible to run larger MoE models on machines without eating up all the RAM (for example, it can run Qwen 3.8 Flash Next on a 24GB Mac) using SSD offloading along with architecture-specific optimizations for Apple Silicon. I've only been able to test a limited number of configurations so far, including my own machine and a couple of independent benchmarks. I've shared some results in the repo already. Now I'd like to put together a benchmark list across different M-series chips, RAM and workloads. I'm particularly interested in older Macs and how well it holds up with longer prompts. If anyone wants to give it a shot, I'd love to see the results, good or bad. How to run it: Clone the repo and install MoEShift Run python ./benchmarks/run.py that runs 3 requests for both a short and a long prompt, then saves the results to (it takes a few minutes to run end-to-end). Open a new benchmark issue in GitHub using the benchmark template, fill your system info and conditions during the test and upload the benchmark-results.json file. You will need roughly 120GB free disk space to test Qwen 3.8 Flash Next IQ3 XXS and 61GB for Qwen 3.6 35B A3B. You can also test other quants or other models that share the same architecture, just configure them in your config.json. I'd really appreciate anyone willing to test it. The more different Macs we can cover, the more useful the results will be for the community. Repo, setup instructions and benchmark details here . Thanks!
