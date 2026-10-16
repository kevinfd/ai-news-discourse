---
id: "98e27055923b345a"
title: "Show HN: Jevman – AI decision models play Pac-Man"
url: "https://opper.ai/jevman-benchmark"
link: "https://opper.ai/jevman-benchmark"
source: "Opper AI"
domain: "opper.ai"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T16:34:13Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["felix089"]
language: "en"
summary: "Openai just launched their decisions endpoint, cloudflare launched clef the other week, and many more jev alternatives are out there. We wanted to put the popular ones to the test and thought Pac-Man is a good benchmark for simple and fast decision making. So we let jev 1.13, kev, clef, clef flash, GPT-6 Luna and Laya play Pac-Man against bot ghosts. The low latency of these models allows for…"
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 433
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50007993"
score: 81
comments: 23
community: "Hacker News"
---

# Show HN: Jevman – AI decision models play Pac-Man

Opper AI · felix089 · 2026-10-08

jevman: the Pac-Man benchmark for AI decision models
Every model plays 100 real-time games against the classic arcade ghosts, and you can play against them.
Leaderboard
100 games per model against the classic ghosts.
=1 means tied: those scores are within each other's margin of error. Run by @opper-ai means we played the games through Opper. Community models were benchmarked by whoever submitted them, named under Run by: CI replayed every game they sent in to check its score, and the latency and cost are as they reported. Only decision models are ranked: they answer with odds for every option in one pass, without writing text. Chat models, regular LLMs that write their answer, and rules that use no model at all show at their score for reference, marked Chat or Base (baseline) instead of a rank. Claude Haiku 5.5, which we ran ourselves, was too slow to show: two thirds of its answers came too late, so backup moves played instead.
Benchmark your own model
jevman is open source, and any model behind an HTTP endpoint can play it: a hosted model, a fine-tune or one running on your laptop.
- 
            01
            Put your model behind an endpoint At every junction the game sends the maze as JSON and asks for a direction, with odds if your model has them. The repo has a 34-line example endpoint to start from.
- 
            02
            Run the benchmark One command plays the games under the leaderboard's rules: real time, 2 seconds per answer, the classic ghosts, three lives or 5 minutes.
- 
            03
            Send a pull request CI replays every game you submit and checks its score. Your model then joins the leaderboard as a community model.
Method
- Games
- Each model played 100 games against the classic scripted ghosts, each until it lost all three lives. Games are capped at 5 minutes so every run ends, but none came close: the longest lasted 2 minutes 24 seconds.
- Decisions
- At every junction the game asks the model one question, with the maze, pellets and ghosts as state. The model returns a probability per direction, and Pac-Man takes its pick.
- Deadline
- An answer that takes longer than 2 seconds is replaced by a simple backup rule, counted under backup moves.
- Scores
- The ranking uses the mean score with a 95% margin of error (±2 standard errors), and models within each other's margin are tied. The high score is a model's best single game.
- Checks
- Every game is recorded and replays exactly, so any result can be checked.
