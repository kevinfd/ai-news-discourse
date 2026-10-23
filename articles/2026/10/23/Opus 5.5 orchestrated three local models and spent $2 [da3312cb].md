---
id: "da3312cb84595101"
title: "Opus 5.5 orchestrated three local models and spent $2"
url: "https://reddit.com/r/ClaudeAI/comments/1xczls1/opus_55_orchestrated_three_local_models_and_spent"
link: "https://reddit.com/r/ClaudeAI/comments/1xczls1/opus_55_orchestrated_three_local_models_and_spent"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T00:33:48Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["GapNew4766"]
language: "en"
summary: "I wanted to see how much Opus 5.5 actually does when it runs as a planner over local models. In Fusion mode Opus plans and reviews, and three workers on a local model write the code in parallel. I ran the same task three times and only swapped the local model. Same prompt, same Opus, same settings. The task was one prompt: a 20 s Halloween chain reaction in Three.js (flint strikes steel → spark…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["models & research", "jobs & society", "agents & coding"]
content_source: "post"
word_count: 425
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xczls1/opus_55_orchestrated_three_local_models_and_spent/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Opus 5.5 orchestrated three local models and spent $2

Reddit · GapNew4766 · 2026-10-23

I wanted to see how much Opus 5.5 actually does when it runs as a planner over local models. In Fusion mode Opus plans and reviews, and three workers on a local model write the code in parallel. I ran the same task three times and only swapped the local model. Same prompt, same Opus, same settings. The task was one prompt: a 20 s Halloween chain reaction in Three.js (flint strikes steel → spark lights a fuse → fuse fires a rocket → rocket knocks a marble down a spiral → marble tips a match into a jack-o'-lantern), follow camera, seamless rewind loop. About 1,000 to 1,700 lines across 6 to 9 files. Setup Agent: Atomic Agent v0.6.10, one turn, no human in the loop Planner: Opus 5.5 via OpenRouter. Workers: 3 in parallel on the local model Models: all Q8_0 GGUF, llama.cpp b11803, one RTX PRO 6000 Blackwell 96 GB per model What Opus did Metric Flint 40B-A2.5B Ornith 1.5 35B-A3B Nemotron 3.5 Lightning 30B-A3B Opus in / out 155K / 3.0K 200K / 4.2K 478K / 6.3K Opus calls 10 12 21 Planning waves 3 3 6 Opus spend $0.41 $0.49 $0.95 Wall time 7:36 9:04 30:32 Fixes needed to run 6 14 16 What stood out Opus barely writes. It read 48-76x more than it wrote (155K in, 3K out on the Flint run). All the code came from the local models. What you pay Opus for is reading their output and deciding what to send back. The local model sets the Opus bill. Same Opus, same prompt, spend went from $0.41 to $0.95 just by swapping the worker. Every broken piece is another review round on Opus. Fastest local model, most Opus work. Nemotron had the best tok/s, but its edits failed ~83% of the time (23 ok vs 109 failed). Opus sent it back six times instead of three and read 3x more tokens than with Flint. Opus can't trust a worker's "ok". One Ornith worker overwrote its own 367-line file with a literal ... and reported "ok". The task still passed because the other two workers covered it. Caveats One run per model, variance not measured. These are time/token numbers. Output quality is a separate writeup. None of the three delivered a fully working scene first pass; after minimal fixes Flint came out cleanest. Anyone else running Opus over local or cheaper sub-agents? What does your in/out ratio look like? Disclosure: I work on Atomic Agent , the open source agent this ran in so ask me anything!
