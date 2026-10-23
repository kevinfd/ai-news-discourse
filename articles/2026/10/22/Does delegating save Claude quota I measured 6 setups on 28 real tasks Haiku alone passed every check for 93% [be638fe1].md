---
id: "be638fe1b3f7b978"
title: "Does delegating save Claude quota? I measured 6 setups on 28 real tasks: Haiku alone passed every check for 93% less, handing work to cheaper models cost more"
url: "https://reddit.com/r/ClaudeAI/comments/1xclm8k/does_delegating_save_claude_quota_i_measured_6"
link: "https://reddit.com/r/ClaudeAI/comments/1xclm8k/does_delegating_save_claude_quota_i_measured_6"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T15:25:01Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["scomage"]
language: "en"
summary: "I wanted to stretch my quota by having Claude Code hand mechanical coding work to cheaper models, so I measured it before relying on it. Most of what I expected turned out wrong. Sharing the numbers in case they save someone the same experiment. The handoff rows used a small MCP tool I wrote for this. Claude passes it a spec, a cheaper model (local or hosted) does the work in its own git…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "DeepSeek"]
topics: ["agents & coding", "models & research", "jobs & society"]
content_source: "post"
word_count: 562
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xclm8k/does_delegating_save_claude_quota_i_measured_6/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Does delegating save Claude quota? I measured 6 setups on 28 real tasks: Haiku alone passed every check for 93% less, handing work to cheaper models cost more

Reddit · scomage · 2026-10-22

I wanted to stretch my quota by having Claude Code hand mechanical coding work to cheaper models, so I measured it before relying on it. Most of what I expected turned out wrong. Sharing the numbers in case they save someone the same experiment. The handoff rows used a small MCP tool I wrote for this. Claude passes it a spec, a cheaper model (local or hosted) does the work in its own git worktree, and the tool runs the checks before Claude reviews. I've retired it because of these results, so this isn't a pitch. Results (median per run) Setup Checks passed Claude $ / run vs Sonnet alone Sonnet 5.5 alone 84/84 0.113 - Sonnet + Haiku 5.5 subagent 84/84 0.095 +13% (+55% on the 5 harder tasks) Sonnet + MCP tool handing off to DeepSeek V4.1 Flash 84/84 0.113 -6% Sonnet + MCP tool handing off to a local 27B 19/20 0.156 -11% Haiku 5.5 alone 84/84 0.008 +93% Opus 5.5 + Haiku 5.5 subagent (harder tasks only) 15/15 0.303 -2% What surprised me Haiku alone passed everything. It was 86-91% cheaper than Sonnet on every batch. It used more tokens than Sonnet (297k vs 152k median, mostly cache reads) and still cost a fraction, because its tokens are cheaper. Handing work to an outside model cost more, not less. Writing the job, waiting on it and reviewing the branch cost Sonnet about as much as doing the task. The worker's bill was tiny (DeepSeek about 1¢ a run, the local GPU about 1¢ of electricity), so a cheaper worker can't fix that. A subagent is the cheap handoff. It shares the session, skips the spec-and-review round trip, and bills at Haiku's rate. Its savings grew with task size. Opus as the orchestrator cost about what Sonnet alone did. Most of the cost was Opus's own planning and review turns. But is Haiku's code any good? The tests can't tell when everything passes, so I ran a second bench: 10 real backlog items from one of my own projects, one run each, blind-graded by Opus 5.5 against the commit that was actually merged. Setup Score (of 100) Merge as is / minor / major / reject Median $ / run Opus 5.5 alone 99 8 / 2 / 0 / 0 0.417 Haiku 5.5 alone 94 3 / 6 / 1 / 0 0.020 Sonnet + Haiku 5.5 subagent 90 4 / 4 / 1 / 1 0.122 The merged commit (reference) 97 6 / 3 / 1 / 0 - Opus alone was the only setup that never needed a major fix, at about 20x Haiku's cost. Haiku mostly needed small ones. The subagent row's reject came from Claude Code's permission check refusing the subagent's Bash calls, so that's partly a setup problem. Limits: every setup was handed a ready spec, so writing it isn't counted. Python only. 3 runs per task on the first bench and 1 per item on the graded one. The grader is Opus, which may favour Opus's code. I didn't test read-heavy offloading (a cheap model reads a big file and returns a short answer), where other tools report large savings. The tasks, raw results and steps to rerun it all are public if you want to check my numbers or run your own setups: https://github.com/gabrielqfr/skrode . The method is in docs/benchmark.md .
