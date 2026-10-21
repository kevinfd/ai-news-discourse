---
id: "605c04bdee239596"
title: "Qwen3.8-Flash-Next vs Opus 5.5: Six-way benchmark on a real Rust feature with Claude Code and Pi"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbipsl/qwen38flashnext_vs_opus_55_sixway_benchmark_on_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbipsl/qwen38flashnext_vs_opus_55_sixway_benchmark_on_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T09:41:48Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["deepu105"]
language: "en"
summary: "Reposting again since original post got removed by Reddit for some reason (I have no idea why) A few of you pointed out in my last post that comparing Flash-Next and Opus with different harnesses and effort levels wasn't fair. So here is a more controlled comparison. Same task for every run: a real feature from the LlamaStash roadmap (save llama-server's KV cache before an unload and restore it…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 505
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbipsl/qwen38flashnext_vs_opus_55_sixway_benchmark_on_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Qwen3.8-Flash-Next vs Opus 5.5: Six-way benchmark on a real Rust feature with Claude Code and Pi

Reddit · deepu105 · 2026-10-21

Reposting again since original post got removed by Reddit for some reason (I have no idea why) A few of you pointed out in my last post that comparing Flash-Next and Opus with different harnesses and effort levels wasn't fair. So here is a more controlled comparison. Same task for every run: a real feature from the LlamaStash roadmap (save llama-server's KV cache before an unload and restore it when the model comes back). Six combinations, each run twice, so 12 PRs. Flash-Next ran locally on my Strix Halo laptop (Flow Z13) via Halogen (~Q4 quant). Opus 5.5, Flash-Next, and Kimi K3 scored every PR on seven review questions plus CI. Combination Score (of 8) Time API cost Tokens (in / cached / out) Claude Code + Opus 5.5, xhigh 6.94 (87%) 43.5 min $17.78 507k / 48.3M / 203k Claude Code + Opus 5.5, medium 6.25 (78%) 23.4 min $6.52 242k / 13.4M / 95k Claude Code + Flash-Next, medium 5.5 (69%) 45.3 min $0.32 445k / 13.5M / 82k Pi + Flash-Next, xhigh 5.44 (68%) 63.8 min $0.67 316k / 35.0M / 134k Claude Code + Flash-Next, xhigh 5.38 (67%) 49.5 min $0.39 269k / 18.9M / 99k Pi + Flash-Next, medium 5.06 (63%) 48.1 min $0.56 242k / 29.1M / 117k Scores are the average of both runs. Time, cost and tokens are from the second run, where the 100k-token benchmark numbers were given in the prompt. Flash-Next cost is at the QwenCloud price for Qwen3.8-Flash; I ran it locally, so it cost me only electricity. TL;DR All 12 runs finished and all 12 PRs pass the end-to-end test. Opus wrote better code, 82% on average against 68% for Claude Code + Flash-Next and 66% for Pi + Flash-Next. The difference is in edge cases, tests and docs. The core feature works fine. The gap between Opus and Qwen is not that wide. Flash-Next took 1.1x to 2.1x as long as Opus at the same effort. With Flash-Next, Claude Code and Pi scored the same on the review questions. CI passed on 4 of 4 Claude Code PRs and 1 of 4 Pi PRs. xhigh helped Opus a bit at 2.7x the cost. For Flash-Next, medium and xhigh scored about the same, and medium was faster in all 4 pairs. Opus is still ahead, but Flash-Next was right behind, on my laptop, for the cost of electricity. Also note that the models are not on the same league. Opus is a frontier model run at FP16 or atleast FP8. I ran Flash-Next on my laptop at 4.16 bpw . Flash-Next at FP8 should show a bit more quality. The machine running Flash-Next ran at 70W TDP ceiling for the entire duration. I could have run it at 90W for slightly better speed but the fan noise and thermal stress was not worth it. Full write-up with the detailed methodology and the per-run results and what each model missed: https://deepu.tech/qwen3.8-flash-next-vs-claude-opus-showdown All 12 PRs are public if you want to read the code: https://github.com/deepu105/llamastash-b4r2/pulls
