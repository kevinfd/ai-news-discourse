---
id: "4cd2345401220a34"
title: "Graded 1,300+ word-association clues: Google's models beat OpenAI's, and both beat Anthropic's"
url: "https://reddit.com/r/artificial/comments/1xnbvcs/graded_1300_wordassociation_clues_googles_models"
link: "https://reddit.com/r/artificial/comments/1xnbvcs/graded_1300_wordassociation_clues_googles_models"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T01:55:45Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Hardicecream17"]
language: "en"
summary: "I run a word-association benchmark: one model gives a one-word clue meant to point at several of its team's words on a 5x5 board, and a teammate model guesses. Each clue is graded 0-100, mostly on how many of its own words a guesser is expected to find before hitting a wrong one. Models play each other in paired games under the same rules and the same grader. Average clue grade (± is a 95%…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["models & research"]
content_source: "post"
word_count: 227
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xnbvcs/graded_1300_wordassociation_clues_googles_models/"
score: null
comments: null
community: "r/artificial"
---

# Graded 1,300+ word-association clues: Google's models beat OpenAI's, and both beat Anthropic's

Reddit · Hardicecream17 · 2026-11-04

I run a word-association benchmark: one model gives a one-word clue meant to point at several of its team's words on a 5x5 board, and a teammate model guesses. Each clue is graded 0-100, mostly on how many of its own words a guesser is expected to find before hitting a wrong one. Models play each other in paired games under the same rules and the same grader. Average clue grade (± is a 95% interval): Gemini 4 Argon: 67 ±3 Gemini 3.8 Flash: 64.5 ±2 GPT-6.1 Terra: 64 ±4 GPT-6 Astra: 63 ±2 GPT-6.1 Sol: 61 ±2.5 Claude Opus 5.5: 58 ±2 Claude Sonnet 5: 57 ±4 Claude Fable 5.1: 56 ±3 Guesses that hit the other team's word or the assassin: Gemini 0-0.5%, GPT-6 0.8-1.9%, Claude 1.7-6%. The cheap tier with thinking off showed the same OpenAI-over-Anthropic gap: GPT-6 Luna beat Claude Haiku 5.5 14-2 in a 16-game head-to-head. Caveats: it's one task, the grader is partly LLM raters, and the older paid-API models (thinking off) don't follow the pattern: Claude Opus 4.6 topped that table at 55. So is this a real difference in how well these labs' models handle word meaning and association, or something narrower about how they play games? One idea I can't test: could ChatGPT's and Google's huge consumer user bases give them more human language data to learn from?
