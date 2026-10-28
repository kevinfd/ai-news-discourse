---
id: "d892b1aa5f2273bc"
title: "Lossing my mind over merge times"
url: "https://reddit.com/r/ClaudeAI/comments/1xhgyrx/lossing_my_mind_over_merge_times"
link: "https://reddit.com/r/ClaudeAI/comments/1xhgyrx/lossing_my_mind_over_merge_times"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T06:52:11Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Internal-Departure44"]
language: "en"
summary: "This week is the first time my agents spend about as much time waiting on merges and tests as on the code itself, and on today's branches it's worse. I'm running what I think is a pretty typical setup: coordinators (Claude Code VS Code tabs, each with its own worktree) running subagents, plus vibecoded instrumentation (knowledge base, telemetry, some usage-tracking fanciness). To give some idea…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 555
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xhgyrx/lossing_my_mind_over_merge_times/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Lossing my mind over merge times

Reddit · Internal-Departure44 · 2026-10-28

This week is the first time my agents spend about as much time waiting on merges and tests as on the code itself, and on today's branches it's worse. I'm running what I think is a pretty typical setup: coordinators (Claude Code VS Code tabs, each with its own worktree) running subagents, plus vibecoded instrumentation (knowledge base, telemetry, some usage-tracking fanciness). To give some idea of scale, yesterday I had ~174 subagents across ~70 coordinators, 48 merges and ~260 commits. Mainly Sonnets and Haikus. The issue of course isn't the merge itself (that takes ~4 s), it's the gates on each merge: ~310 tests under coverage, a linter etc. Every time main moves during a merge, the gates run again, and I'm pulling my hair out trying to figure out when it's safe to skip that and when not. Merge conflicts (~1/3 of merges) are handled by a resolver agent and a reviewer agent. From my telemetry and merge logs: Step Time Agent coding 10–15 min Branch gates 6–9.5 min Merge, main unchanged ~4 s Merge, main moved (re-gate) 2.5–4 min Merge with conflict, start to finish 3–13 min If several agents have merges ready, they have to queue, so there's a bunch of waiting for other agents' merges to finish too. And don't forget that each merge moves main, which can prevent reusing the test results an agent already has. One docs-only commit landing mid-gate threw away 9 minutes of gating. Overall my coding vs. blocked ratio went from 80/20 a few days ago to about 55/45 yesterday, and 40/60 on today's branches. Coverage is ~95% of the branch gate time, and it tripled in a day, from a median of 167 s to ~550 s, because parallel agents running tests fight over the CPU (the dev rig is old but ain't bad: 12/24 cores). My main issue is that even if I optimize the heck out of the gates, prevent reruns for docs-only changes etc., the math in the end is this. I have a merge ready every ~10 minutes, and usually 3–5 at the same time, because I tend to start agents on issues at the same time. Branch gates take 6–9 minutes and a re-gate after main moved another 2.5–4, so the other 2–4 agents wait several times that. Main moves in the meantime, so the tests need to be rerun again. It's painful, to put it lightly. What I'm already doing: parallel fail-fast gates; rerunning only the tests that touch the changes; skipping tests when a branch is docs-only; reusing gate results if main hasn't changed; auto-resolving changelog-only conflicts. What I'm thinking about trying: some way to reuse gate results even when main changes, if those changes are docs-only; moving coverage to nightly; centralizing merges on one agent? What's the usual practice? I can't be the only one losing sleep over this. My main worry is that this is a smallish pilot project (~9k lines of Python and ~4k of TypeScript, coded agentically since last Friday). I need to figure out how to handle parallel work on our main codebase, a 15-year-old ERP with ~600k lines of VB.NET. There I'm additionally limited to 3–5 test suites at the same time, by how many MSSQL test databases I can fit on our hardware. Do I drop testing per merge or something?
