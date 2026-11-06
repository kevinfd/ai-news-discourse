---
id: "34b4d91444608a1d"
title: "I was curious how small local models handle Polish grammar – a quick 15-task test on 8 GB VRAM"
url: "https://reddit.com/r/LocalLLaMA/comments/1xomsxq/i_was_curious_how_small_local_models_handle"
link: "https://reddit.com/r/LocalLLaMA/comments/1xomsxq/i_was_curious_how_small_local_models_handle"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T16:17:50Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Full-Travel857"]
language: "en"
summary: "I wanted to know how small local models handle my native language, not just English. I couldn't find a simple way to check a model's Polish in a few minutes, on my own PC, in the quantization I actually run – so I wrote one. That's how \"Zacharski tests\" started: a small task set that runs through Ollama, since that's what I use on my laptop with an RTX 5050 (8 GB). The tasks: Polish (8):…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 420
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xomsxq/i_was_curious_how_small_local_models_handle/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I was curious how small local models handle Polish grammar – a quick 15-task test on 8 GB VRAM

Reddit · Full-Travel857 · 2026-11-05

I wanted to know how small local models handle my native language, not just English. I couldn't find a simple way to check a model's Polish in a few minutes, on my own PC, in the quantization I actually run – so I wrote one. That's how "Zacharski tests" started: a small task set that runs through Ollama, since that's what I use on my laptop with an RTX 5050 (8 GB). The tasks: Polish (8): diacritics, declension, masculine-personal gender, numerals, vocative, verb aspect, genitive – plus one knowledge question (the first recorded Polish sentence, from the 13th-century Book of Henryków). JSON (4) : scored strict and lenient. Python (3): syntax check only. Results so far: | Model | Quant | JSON + code | Polish | | gemma2:9b | Q4_0 | 7/7 | 3/8 | My favourite failure: asked for "22 cats", gemma2 wrote "dwudziesty dwa koty" – roughly "twentieth two cats". The correct form is "dwadzieścia dwa koty". It was perfectly happy producing valid JSON, though. More models are downloading as I write this. Next up: gemma2:9b in Q4_K_M and Q8_0 (does quantization hurt the Polish?), qwen3:8b, llama3.1:8b, gemma3:12b, and two Polish models – Bielik 11B and Bielik-Minitron 7B. Which model would you add? Method and limits – read this before the comments :) 8 Polish tasks (7 grammar + 1 knowledge) and 7 JSON/code tasks. That's a small sample – a quick check on your own PC, in the quantization you actually run, not a ranking. For a proper ranking, see the Open PL LLM Leaderboard by SpeakLeash. One answer per task, temperature 0 (seed 42), context 2k, thinking off. Yes, that means Qwen3 runs without its reasoning mode, which may cost it points – I wanted the same conditions for every model. Graded with regular expressions, strict on purpose: "brzęczały" ("buzzed") instead of "brzmiały" ("sounded") fails, because the task said "change the tense", not "rephrase". [I checked every failed answer by hand.] Some failures are about instruction-following, not language: asked to restore Polish diacritics, one model replied "Read the spelling rules." [(translated)] Generated code is only parsed (Python `ast`), never executed. The questions are in the repo (`data/benchmarks/*.json`) – feel free to add or fix them. The test runs inside a free, open-source tool I've been building (Windows .exe / Python on Linux). Its main job is predicting whether a model fits your VRAM/RAM before you download it. Link in the comments if anyone wants to try it – I'm considering adding tests for other languages.
