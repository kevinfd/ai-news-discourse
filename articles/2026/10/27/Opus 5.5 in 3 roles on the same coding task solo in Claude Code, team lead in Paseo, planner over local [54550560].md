---
id: "54550560ed4cf55c"
title: "Opus 5.5 in 3 roles on the same coding task: solo in Claude Code, team lead in Paseo, planner over local workers"
url: "https://reddit.com/r/ClaudeAI/comments/1xh6950/opus_55_in_3_roles_on_the_same_coding_task_solo"
link: "https://reddit.com/r/ClaudeAI/comments/1xh6950/opus_55_in_3_roles_on_the_same_coding_task_solo"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T22:02:27Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["latent_lurker8587"]
language: "en"
summary: "A few days ago I asked in a different subreddit whether people use multi-agent orchestration or stick with a single agent ( original thread ). It got 84K views and 60+ comments, and the answers were all over the place. Everyone was arguing from experience and nobody had numbers on the same task. So I took four setups straight from the comments and gave them the exact same job. The four setups…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Alibaba", "OpenAI"]
topics: ["agents & coding", "jobs & society", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 589
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xh6950/opus_55_in_3_roles_on_the_same_coding_task_solo/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Opus 5.5 in 3 roles on the same coding task: solo in Claude Code, team lead in Paseo, planner over local workers

Reddit · latent_lurker8587 · 2026-10-27

A few days ago I asked in a different subreddit whether people use multi-agent orchestration or stick with a single agent ( original thread ). It got 84K views and 60+ comments, and the answers were all over the place. Everyone was arguing from experience and nobody had numbers on the same task. So I took four setups straight from the comments and gave them the exact same job. The four setups Claude Code, single agent. Anthropic’s coding agent running Opus 5.5 on its own, start to finish, no subagents. Codex CLI, single agent. Also one agent working alone, but from OpenAI. It ran GPT 5.5 on its own, with the same instructions. A Paseo agent team, set up exactly like u/c-digs described. An expensive lead model that hands work to cheaper worker agents, with a structured handoff prompt. I used his published team prompt and agent profiles as is. Big thanks to him for making this testable. Atomic Agent in Fusion mode. Fusion mode in Atomic Agent is where a cloud model plans while smaller local models do the work. Here the planner was Claude Opus 5.5 and the workers were Qwen 3.8 27B running locally on the same Mac. The task One small Python app, an expense tracker in 5 parts: storage, an importer for a deliberately messy bank CSV, a JSON API, a CLI and an HTML monthly report, all sharing one config file. Same one-line prompt and spec for every setup. Grading was 38 hidden tests the agents never saw. M5 Max with 64 GB, October 26, one run per setup, cloud models through OpenRouter. Results Setup Models Time Hidden tests API cost Codex GPT 5.5 5m 38s 38/38 $1.32 Claude Code Opus 5.5 6m 57s 38/38 $1.27 Paseo team (c-digs setup) Opus 5.5 lead 5m 25s 38/38 $1.13 Atomic Agent, Fusion mode Opus 5.5 plans, local Qwen 3.8 27B Q4 builds 3m 11s 38/38 $0.40 The Claude part Opus 5.5 ended up in three of the four setups, each time in a different role: Solo in Claude Code: did the whole job alone. 6m 57s, 38/38, $1.27. Lead of the Paseo team: was supposed to hand work to cheaper workers, judged the job small enough and did it all itself, exactly as c-digs said his setup does ("simple tasks: it does it directly"). 38/38, $1.13. Planner in Atomic Agent's Fusion mode: only planned and checked while local Qwen workers wrote the code. When one worker stalled, Opus noticed and handed its part to another one. $0.40, the lowest bill of the four. What I learned Orchestration is worth it, just not for the reason most people argue about. It lets an expensive model do only the thinking while cheap or local models do the bulk, and it keeps someone watching the work when a piece fails. The bigger the job, the more that matters, and this one was about as small as a real task gets. Round 2 should be a job big enough that splitting it is the obvious move. If you have a task in mind that is fair to test, drop it below. What’s the biggest job you’ve handed to a multi-agent setup, and did the planner live up to its expectations? Sources Costs: OpenRouter billing per request (Codex's cost computed from its token counts) Times and test results: run logs and the hidden test suite from each run Versions: Claude Code 2.1.310, Codex 0.147.0, Paseo 0.13.2, Atomic Agent 0.6.11 Links to all tools and c-digs's setup in the first comment
