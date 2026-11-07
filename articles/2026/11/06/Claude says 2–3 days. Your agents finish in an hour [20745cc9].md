---
id: "20745cc9e3f9d1e5"
title: "Claude says \"2–3 days.\" Your agents finish in an hour."
url: "https://reddit.com/r/ClaudeAI/comments/1xpkjqd/claude_says_23_days_your_agents_finish_in_an_hour"
link: "https://reddit.com/r/ClaudeAI/comments/1xpkjqd/claude_says_23_days_your_agents_finish_in_an_hour"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T18:39:46Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Current-Zebra-2039"]
language: "en"
summary: "Ask Claude \"how long will this take?\" and you get a human developer's estimate, as if someone types every line. With Claude Code and subagents, typing is nearly free. In my builds the time goes to: waiting on me (questions, approvals, manual testing) review and test loops after every task tasks that have to run in order rework So I built agent-eta , a Claude Code plugin. You run /agent-eta:eta…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 388
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpkjqd/claude_says_23_days_your_agents_finish_in_an_hour/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude says "2–3 days." Your agents finish in an hour.

Reddit · Current-Zebra-2039 · 2026-11-06

Ask Claude "how long will this take?" and you get a human developer's estimate, as if someone types every line. With Claude Code and subagents, typing is nearly free. In my builds the time goes to: waiting on me (questions, approvals, manual testing) review and test loops after every task tasks that have to run in order rework So I built agent-eta , a Claude Code plugin. You run /agent-eta:eta add Stripe billing (or point it at a plan file) and get: Total: 2h 25m – 4h 29m (wall clock) Agents working: ~2h 11m (you can walk away) You needed: ~30 min (5 questions, 2 approvals, 1 manual test) Waiting on you: ~10 min (Claude idle until you reply) Biggest risk: Task 4 — Pricing page (+1h 08m if it goes badly) Speed-ups (−35 min): • Tasks 2 & 4 are independent → run them in parallel, each in its own git worktree (−28 min) • 7 questions/approvals before the build → answer them in one go (−7 min) • Task 1 is mechanical → use a cheaper model (lower cost, ~same time) How it works Claude splits the work into tasks, and a Haiku subagent tags each one (size, kind, flags). A plain Node script does all the maths with no AI involved, so the same tasks always give the same number. I ran it 3 times on the same feature and the results landed within 6% of each other. It learns from you After the build, /agent-eta:eta-done measures the real time from your local Claude Code transcripts. Each result moves your personal numbers 30% toward reality. They switch on after 3 confirmed builds. Everything stays local, and no message text is saved. Honest status: v0.1 The default numbers come from my own ~670 subagent runs, so they're tuned to one person. My first real measurement was way off: predicted 1h 10m, actual 26 min, because I ran agents in parallel. That's exactly why it learns. I'd love to know how far off it is for you. Zero dependencies, MIT licensed. It works with or without the superpowers plugin, and reads superpowers plan files directly. Install: /plugin marketplace add MuhammadTalhaMT/agent-eta /plugin install agent-eta@agent-eta Repo: https://github.com/MuhammadTalhaMT/agent-eta If you try it, I'd really like your /agent-eta:eta-stats output after a few builds. That's how the defaults get better for everyone.
