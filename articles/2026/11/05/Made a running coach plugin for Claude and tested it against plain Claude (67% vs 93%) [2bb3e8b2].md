---
id: "2bb3e8b240cc568a"
title: "Made a running coach plugin for Claude and tested it against plain Claude (67% vs 93%)"
url: "https://reddit.com/r/ClaudeAI/comments/1xoso2l/made_a_running_coach_plugin_for_claude_and_tested"
link: "https://reddit.com/r/ClaudeAI/comments/1xoso2l/made_a_running_coach_plugin_for_claude_and_tested"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T20:01:08Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["slinto"]
language: "en"
summary: "I've been running for a few years and trained with a coach for part of that time, so I have a fair idea of what a good plan looks like. Now I coach myself, and plain Claude was fine for chatting about training but not great at the actual plan. It agreed with whatever goal I gave it, and the numbers changed every time I asked. So I wrote a plugin for it. It works in Claude Code, the desktop app…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 353
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xoso2l/made_a_running_coach_plugin_for_claude_and_tested/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Made a running coach plugin for Claude and tested it against plain Claude (67% vs 93%)

Reddit · slinto · 2026-11-05

I've been running for a few years and trained with a coach for part of that time, so I have a fair idea of what a good plan looks like. Now I coach myself, and plain Claude was fine for chatting about training but not great at the actual plan. It agreed with whatever goal I gave it, and the numbers changed every time I asked. So I wrote a plugin for it. It works in Claude Code, the desktop app and claude.ai (as a ZIP). You just ask things like "should I run today?" or "race plan for Sunday's half". If you connect TrainingPeaks it reads HRV, sleep and workouts and can put sessions on your watch (after you confirm). Strava works too, or no data at all. The trick is that the model doesn't calculate anything. Paces, zones, load checks, predictions and race splits come from Python scripts the skill runs. The rules are backed by research, 63 sources, each with how solid the evidence is. I tested it with claude plugin eval: 39 cases in English and Slovak, each run with and without the plugin. On the 8 questions in both languages plain Claude got 67/66% and the plugin 93/95%. One example from the evals: a race plan for a hilly half at 21 °C with a 1:35 goal. Plain Claude kept the goal and the fuelling didn't add up to what the runner had handled in training. The plugin slowed the goal by about 2.4% for the heat, slowed the splits on the climb, and planned 45 g of carbs an hour, the runner's tested rate. I'm using it for my own spring. Last May I ran the Prague Marathon, held 4:38/km for 30 km, then slowed down over the last 12 and finished in 3:22:47. In April I want the Prague half under 1:30 (this year I missed it by 27 seconds), and in May the marathon in 3:15. So I'll find out the hard way if it's wrong. It's free and MIT: https://github.com/tomasstankovic/running-coach If you run, I'd like to know where it coaches badly. Processing img 7q34dafyouzh1...
