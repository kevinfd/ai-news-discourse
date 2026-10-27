---
id: "78e419ca70cc1c6e"
title: "Benchmark task for testing local AI"
url: "https://reddit.com/r/LocalLLaMA/comments/1xgm6nu/benchmark_task_for_testing_local_ai"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgm6nu/benchmark_task_for_testing_local_ai"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T07:38:59Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["prusswan"]
language: "en"
summary: "Just want to share a task I used to evaluate the capability of Qwen 3.8 FN. The goal is to port a old screensaver (can find it on Wayback Machine) to Python OpenGL, maintaining full visual fidelity. Tooling: Claude Code (harness) + Qwen 3.8 FN Q4_K_XL via gufo + Strix Halo + Ubuntu 26.04 Run command: export MODEL=Qwen3.8-Flash-Next-UD-Q4_K_XL-00001-of-00004.gguf export…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "Anthropic"]
topics: ["models & research", "search & media"]
content_source: "post"
word_count: 167
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgm6nu/benchmark_task_for_testing_local_ai/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Benchmark task for testing local AI

Reddit · prusswan · 2026-10-27

Just want to share a task I used to evaluate the capability of Qwen 3.8 FN. The goal is to port a old screensaver (can find it on Wayback Machine) to Python OpenGL, maintaining full visual fidelity. Tooling: Claude Code (harness) + Qwen 3.8 FN Q4_K_XL via gufo + Strix Halo + Ubuntu 26.04 Run command: export MODEL=Qwen3.8-Flash-Next-UD-Q4_K_XL-00001-of-00004.gguf export MTP=/run/media/user/DATA/models/huggingface/mtp-Qwen3.8-Flash-Next-shared-Q8_0.gguf export MMPROJ=/run/media/user/DATA/models/huggingface/mmproj-Qwen3.8-Flash-Next-BF16.gguf #./result/bin/gufo chat --model "$MODEL" ./result/bin/gufo serve llm --model "$MODEL" --speculative mtp \ --mtp-model "$MTP" \ --mmproj "$MMPROJ" \ --sessions 1 \ --context 133760 \ --max-tokens 32768 \ --prefill-chunk 4096 \ --served-model-name qwen3.8-flash-next \ --max-pending-per-client 2 Assessment: Some parts are quite challenging with the 128K context window. Also, be mindful that graphics-related tasks (apart from running the model) may produce inconsistent results, and thus require specific measures, To keep this benchmark useful for others, I won't go into the details of the approach adopted by the AI, except to share that the task is tractable given a comparable setup. But feel free to ask by PM.
