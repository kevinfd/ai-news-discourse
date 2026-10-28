---
id: "1f02f6890ddac42d"
title: "Self-distillation with an EMA teacher at scale: ZeRO-3 + PEFT [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xh083s/selfdistillation_with_an_ema_teacher_at_scale"
link: "https://reddit.com/r/MachineLearning/comments/1xh083s/selfdistillation_with_an_ema_teacher_at_scale"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T18:16:08Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["ifaposto"]
language: "en"
summary: "Self-distillation methods usually rely on an Exponential Moving Average (EMA) teachers to get synced and stable critics. However, this doesn't scale well for large models since holding both teacher and student (trained) on GPU increases latency, zero3 communication, etc. We can mitigate this with LoRA finetuning: the backbone is shared & frozen, and we need to maintain two light adapters: one…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["jobs & society", "chips & infrastructure"]
content_source: "post"
word_count: 149
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xh083s/selfdistillation_with_an_ema_teacher_at_scale/"
score: null
comments: null
community: "r/MachineLearning"
---

# Self-distillation with an EMA teacher at scale: ZeRO-3 + PEFT [P]

Reddit · ifaposto · 2026-10-27

Self-distillation methods usually rely on an Exponential Moving Average (EMA) teachers to get synced and stable critics. However, this doesn't scale well for large models since holding both teacher and student (trained) on GPU increases latency, zero3 communication, etc. We can mitigate this with LoRA finetuning: the backbone is shared & frozen, and we need to maintain two light adapters: one for the student (trained) and one for the teacher (EMA of the student adapter). Getting this to work cleanly under TRL and ZeRO-3 took some fixes, so I packaged it as a plug-and-play repo. It supports: -> robust SDFT implementation that runs under ZeRO-3 -> ZeRO-3 + LoRA integration with adapter switching for teacher/student passes -> Saving and resuming EMA teacher checkpoint -> working deepspeed configs that fix memory spikes when GPU memory is tight I tested on Qwen3.5 and ToolAlpaca. Repo: https://github.com/ifiaposto/sdft_zero3 Feedback/ more examples/ issues welcome!
