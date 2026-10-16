---
id: "ff08a8815cebb1b5"
title: "**DeepSeek-V4-Flash-0731 on 4x Radeon AI PRO R9700 with affinity: the \"refused\" 4-card config works, ~79 tok/s on real cards**"
url: "https://reddit.com/r/LocalLLaMA/comments/1x70e5r/deepseekv4flash0731_on_4x_radeon_ai_pro_r9700"
link: "https://reddit.com/r/LocalLLaMA/comments/1x70e5r/deepseekv4flash0731_on_4x_radeon_ai_pro_r9700"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T23:06:40Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["brainchillzZ"]
language: "en"
summary: "Follow-up to u/neuromacmd 's post from a few weeks back ( https://www.reddit.com/r/LocalLLaMA/comments/1wod07t/ ). The affinity engine ( https://codeberg.org/StillDeadcode/affinity ) refuses to start on more than two cards because the author only had two, simulated four ranks on them, and got repeated-token garbage they couldn't explain. Nobody had tried it on four real R9700s. I have four, so…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: []
content_source: "post"
word_count: 383
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x70e5r/deepseekv4flash0731_on_4x_radeon_ai_pro_r9700/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# **DeepSeek-V4-Flash-0731 on 4x Radeon AI PRO R9700 with affinity: the "refused" 4-card config works, ~79 tok/s on real cards**

Reddit · brainchillzZ · 2026-10-15

Follow-up to u/neuromacmd 's post from a few weeks back ( https://www.reddit.com/r/LocalLLaMA/comments/1wod07t/ ). The affinity engine ( https://codeberg.org/StillDeadcode/affinity ) refuses to start on more than two cards because the author only had two, simulated four ranks on them, and got repeated-token garbage they couldn't explain. Nobody had tried it on four real R9700s. I have four, so tonight I did. Short version: it just works. Setup: Threadripper PRO 9955WX, 128 GB RAM, four R9700s all on CPU lanes with P2P between every pair. I built the fork with the stability fixes ( https://github.com/neuromaniacMD/affinity , branch v4-fixes) and used the prebuilt 2.875 bpw quant ( https://huggingface.co/neuromaniacmd/DeepSeek-V4-Flash-0731-affinity-2.875bpw ), so no 149 GB download or 2.5 hour quantize. Then AFF_ALLOW_NRANK=1 --gpus 4. Results, same box, same prompts: 2 cards: 36 tok/s decode. 45% of the experts fit in VRAM, the rest stream from a 51 GB pinned host pool, and the profiler shows 82% of every token waiting on that stream. 4 cards: 79 tok/s greedy, 63 at temp 1.0, about 90 on a chat answer with thinking on. All 11,008 experts resident, host pool not even allocated. Five runs, greedy and sampled, plus a chat server test. No degenerate output. The engine's own cross-rank check (it compares the cards against each other every few samples) passed every time. So the bug the author hit lives in the 4-on-2 simulation, not in 4-rank execution. u/neuromacmd already suspected this. Two things to know if you try it: The default heat placement strategy aborts on 4 cards with "needs the registered host pool", because there is nothing left to demote. Pass --placement-strategy static. Nothing needs to move anyway when everything is resident. Load is about a minute, 42 seconds of which is pushing 96 GB of experts onto the cards. Also correcting my own earlier comment in that thread: I assumed affinity's cap was a 2-rank-only all-reduce like Radiance had before my patch ( https://github.com/brainchillz/r9700-tp4-allreduce , https://github.com/jdrews/vllm-mxfp4/pull/2 ). Wrong. Affinity's collective is already written for N ranks and tested at 3, 4 and 8. The cap was purely the unexplained garbage, which real hardware doesn't produce. I'm going to leave this up for a while so I'm happy to run anything else on this box if the author or anyone wants more data. Logs are available if useful.
