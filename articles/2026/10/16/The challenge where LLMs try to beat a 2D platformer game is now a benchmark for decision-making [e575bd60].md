---
id: "e575bd609ea890cb"
title: "The challenge where LLMs try to beat a 2D platformer game is now a benchmark for decision-making"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7k7vm/the_challenge_where_llms_try_to_beat_a_2d"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7k7vm/the_challenge_where_llms_try_to_beat_a_2d"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T16:04:35Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Felladrin"]
language: "en"
summary: "The project I posted here a week ago ( https://www.reddit.com/r/LocalLLaMA/comments/1x17ou5/decisions_in_a_js13kgame ) is now a benchmark: anyone can run their model on it and contribute reproducible results to a leaderboard of models that are good at 2D spatial decisions! At each decision, the model reads a text description of the game and answers two multiple-choice questions (which objective…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 140
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7k7vm/the_challenge_where_llms_try_to_beat_a_2d/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# The challenge where LLMs try to beat a 2D platformer game is now a benchmark for decision-making

Reddit · Felladrin · 2026-10-16

The project I posted here a week ago ( https://www.reddit.com/r/LocalLLaMA/comments/1x17ou5/decisions_in_a_js13kgame ) is now a benchmark: anyone can run their model on it and contribute reproducible results to a leaderboard of models that are good at 2D spatial decisions! At each decision, the model reads a text description of the game and answers two multiple-choice questions (which objective to go for, and which key to press). So any model that gives a probability per answer can play it. The top model is the only one so far to clear all 14 levels on all 5 seeds! I'm testing other models and will post the results when they finish. Large ones (27B) take 16 hours to finish the trial (5 seeds, with a cap of 100 deaths on each of the 14 levels). The code and the leaderboard are on GitHub: https://github.com/felladrin/cat-goric-game-benchmark
