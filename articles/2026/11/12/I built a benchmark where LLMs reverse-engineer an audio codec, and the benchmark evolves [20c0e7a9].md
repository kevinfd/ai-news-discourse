---
id: "20c0e7a9e7900d95"
title: "I built a benchmark where LLMs reverse-engineer an audio codec, and the benchmark evolves"
url: "https://reddit.com/r/LocalLLaMA/comments/1xupf99/i_built_a_benchmark_where_llms_reverseengineer_an"
link: "https://reddit.com/r/LocalLLaMA/comments/1xupf99/i_built_a_benchmark_where_llms_reverseengineer_an"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T21:34:05Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Character-Result-281"]
language: "en"
summary: "Most coding benchmarks feel like textbook coding tasks or black boxes — either easy to benchmaxx or full of hidden tasks with unclear evaluation criteria. And most of them get irrelevant with each new model generation because all of the new models hit the ceiling. So I made one that has a moving target. It's a benchmark where the model gets a mystery compressed audio file, has to figure out the…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Anthropic"]
topics: ["models & research", "agents & coding", "jobs & society"]
content_source: "post"
word_count: 410
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xupf99/i_built_a_benchmark_where_llms_reverseengineer_an/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I built a benchmark where LLMs reverse-engineer an audio codec, and the benchmark evolves

Reddit · Character-Result-281 · 2026-11-12

Most coding benchmarks feel like textbook coding tasks or black boxes — either easy to benchmaxx or full of hidden tasks with unclear evaluation criteria. And most of them get irrelevant with each new model generation because all of the new models hit the ceiling. So I made one that has a moving target. It's a benchmark where the model gets a mystery compressed audio file, has to figure out the format, write a decoder, and then build an encoder that beats the original. No ffmpeg, no Opus, no importing a library that already does the job. Just Python and numpy, running locally through OpenCode Scoring: 100 = decode the reference in stage one. Build a better encoder in quality or compression rate with equal or better SNR for additional points. There are 4 stages: 1. is the most difficult: just a compressed audio file. 2. if the model failes the first stage, it gets the uncompressed audio as a reference. Each new stage decreases the points up for graps. 3. if it fails stage 2 it gets additional information on the codec 4. if it fails stage 3 it gets an oracle tool where it can USE the codec to figure it out. Current Leaderboard, we are in Evolve 2 (Deepseek cracked the codec of evolve 1 in 13min): Model Score 1 Claude Fable Latest (stage 1) 127 2 DeepSeek V4.1 Flash 1017 (stage 3) 81 3 Qwen3.8-Flash-Next NVFP4 (stage 3) 67 4 Qwen3.8-Flash-Next Q3_S (stage 4) 56 5 Qwen3.8-Flash-Next IQ3_XXS (stage 4) 44 The fun part: it evolves. If a model finishes stage 1 and its encoder beats the current codec, that codec becomes the next baseline. So the benchmark levels up instead of staying at the same difficulty forever. Pokémon rules, except the final boss is a bitstream. DeepSeek did it first and became Evolve 2. Fable just finished stage 1 with Compress 190, so its codec is the Evolve 3 baseline. The next runs should use it. A better encoder in stage 3 doesn't count for an evolve, by the way. Only a stage-1 finish does. That's the rule. It's manual for now: you run it on your own hardware, post the result, and set the evolve stage. It's mean. Most models don't finish stage 1. But that's kind of the point. Leaderboard: https://andreasknopke.github.io/codec-reverse-bench-leaderboard/ — ping me if you want to run it (the repo is private to prevent the models from simply copying the solution.
