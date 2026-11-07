---
id: "e39c6f996a8f2274"
title: "How I orchestrate test runs from multiple Claude Code agents across a cluster of mac mini's"
url: "https://reddit.com/r/ClaudeAI/comments/1xpgkrp/how_i_orchestrate_test_runs_from_multiple_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xpgkrp/how_i_orchestrate_test_runs_from_multiple_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T16:06:57Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["No_Paramedic_4881"]
language: "en"
summary: "When working with multiple coding agents, or dispatching multiple subagents to complete a task faster, the bottleneck started to become my laptop itself. Agents dont coordinate when they kick off test runs, so they would run tests at the same time which would bog down my laptop and cause flakey failures from test suites running on top of each other. I have a few mac minis laying around, so I…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 277
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpgkrp/how_i_orchestrate_test_runs_from_multiple_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How I orchestrate test runs from multiple Claude Code agents across a cluster of mac mini's

Reddit · No_Paramedic_4881 · 2026-11-06

When working with multiple coding agents, or dispatching multiple subagents to complete a task faster, the bottleneck started to become my laptop itself. Agents dont coordinate when they kick off test runs, so they would run tests at the same time which would bog down my laptop and cause flakey failures from test suites running on top of each other. I have a few mac minis laying around, so I coded up a CLI (with Claude) to orchestrate queuing test runs, syncing code to the mac mini's, and running commands across the cluster. The boundary is so seamless now that it almost feels like I bolted 3 mac mini's onto my laptop. It even has the ability to sync over LAN first, and fallback to tailscale when I am working from a coffeeshop. Tests run almost 3x faster, and agents no longer collide test runs at the same time, which has improved the signal coding agents need when they are working. Something this process has taught me is how to work with agents like they are your end uses. This CLI was built for Claude, by Claude, and it's interface was designed for agents as it's main user. It's an interesting way to build things, since historically a person (developer) or system is the user of something like a CLI. When building a given tool, I would have Claude use it and give feedback on how it would want the interface or output changed. I've found this CLI to significantly improve my agentic coding productivity, so I open sourced it. If you happen to have some extra hardware laying around, you might give it a try: https://github.com/rileyhilliard/rr
