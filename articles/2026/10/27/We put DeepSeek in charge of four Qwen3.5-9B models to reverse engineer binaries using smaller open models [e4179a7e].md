---
id: "e4179a7e31d7317b"
title: "We put DeepSeek in charge of four Qwen3.5-9B models to reverse engineer binaries using smaller open models."
url: "https://reddit.com/r/LocalLLaMA/comments/1xgoxvu/we_put_deepseek_in_charge_of_four_qwen359b_models"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgoxvu/we_put_deepseek_in_charge_of_four_qwen359b_models"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T10:32:27Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["HauntingMoment"]
language: "en"
summary: "Reverse Engineer Anything blew up recently but, every impressive reverse engineering result we’ve seen uses (closed) frontier models. We wanted to know whether small local models can do useful work here if a bigger model organizes them, hopefully cutting cost and allowing a broder range of people to Reverse Engineer Anything :) Setup Lead: DeepSeek-V4.1-Flash. It disassembles the binary, names…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Oracle", "Anthropic"]
topics: ["jobs & society", "models & research"]
content_source: "post"
word_count: 419
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgoxvu/we_put_deepseek_in_charge_of_four_qwen359b_models/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# We put DeepSeek in charge of four Qwen3.5-9B models to reverse engineer binaries using smaller open models.

Reddit · HauntingMoment · 2026-10-27

Reverse Engineer Anything blew up recently but, every impressive reverse engineering result we’ve seen uses (closed) frontier models. We wanted to know whether small local models can do useful work here if a bigger model organizes them, hopefully cutting cost and allowing a broder range of people to Reverse Engineer Anything :) Setup Lead: DeepSeek-V4.1-Flash. It disassembles the binary, names the functions, recovers signatures and memory layout, and posts tasks with hints to a shared board. Workers: 4× Qwen3.5-9B. Each picks up a task and rewrites one function in Python. Oracle ( diff_test ): runs ~600 cases through both the original binary function and the Python rewrite, comparing the return value and every byte of state. Workers only submit at 100%. Harness: a minimal ipython-based harness. The lead is allowed to modify the workers’ harness (prompts, tools) if it thinks that will help. (this ends up being the most interesting part) To begin with a proof of concept, the targets were two small C programs we generated with Claude Code and compiled. The team only ever saw the binaries. As a baseline, we also ran DeepSeek (the lead) alone on each tasks. Task Run Functions Escalated Cost Time HF logo animation Team 38/38 15 $2.97 86 min HF logo animation Solo 38/38 — $0.87 14 min Space shooter Team 56/56 20 $3.60 100 min Space shooter Solo 56/56 — $3.28 54 min (4 launches) The team work is pure overhead on smaller jobs, the lead has to organize and fix the smaller models, taking more time than if it had just worked alone. The most interesting part For the shooter game, the lead ended up changing the instructions of the smaller models 3 times. House rules. The workers were inventing helper function names, ignoring signed/unsigned distinctions and not using the recorded memory layout. Workers were reading b.ls as < instead of unsigned <= , calling functions with the wrong number of arguments, and computing field offsets by hand (and getting them wrong). The lead added instructions for this. A lookup tool: written by the lead so workers could query function signatures and field offsets instead of re-deriving them. Caveats The binaries weren’t stripped. Function names make the lead’s mapping job much easier, and most real software ships without them. These were small, clean, AI-generated programs, not optimized real-world code. Two data points. The trend with task size is suggestive, not proven. About 40% of functions still went back to the lead. You can find the full write-up here: https://huggingface.co/blog/ybelkada/reverse-engineering-anything-with-small-local-mode
