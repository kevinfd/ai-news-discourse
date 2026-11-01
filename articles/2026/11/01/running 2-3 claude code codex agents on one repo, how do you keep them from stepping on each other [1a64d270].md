---
id: "1a64d2708367ae57"
title: "running 2-3 claude code / codex agents on one repo, how do you keep them from stepping on each other"
url: "https://reddit.com/r/ClaudeAI/comments/1xkvmve/running_23_claude_code_codex_agents_on_one_repo"
link: "https://reddit.com/r/ClaudeAI/comments/1xkvmve/running_23_claude_code_codex_agents_on_one_repo"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T06:05:25Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Axlonri"]
language: "en"
summary: "the way i think about it there's level 1 (ai helps you write, cursor/antigravity), level 2 (you don't write the code but you read it and run it, claude code/codex) and level 3 (you never see the code, lovable/bolt) on level 2 one agent is fine, but once i start a second one in another terminal for a different task and then a third, they start messing with each other. two of them edit the same…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 276
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkvmve/running_23_claude_code_codex_agents_on_one_repo/"
score: null
comments: null
community: "r/ClaudeAI"
---

# running 2-3 claude code / codex agents on one repo, how do you keep them from stepping on each other

Reddit · Axlonri · 2026-11-01

the way i think about it there's level 1 (ai helps you write, cursor/antigravity), level 2 (you don't write the code but you read it and run it, claude code/codex) and level 3 (you never see the code, lovable/bolt) on level 2 one agent is fine, but once i start a second one in another terminal for a different task and then a third, they start messing with each other. two of them edit the same config, or one keeps working off a file the other already changed, and i only find out when merging last time this bit me was a judging platform we built for a big tech conference, we were coding it pretty much the night before and the judges were going to be actual ministers and a couple of unicorn founders, so i had three agents going at once and two of them ended up editing the scoring logic in parallel, one renamed a field the other was still reading from, and we caught it at like 4am when the merged version showed half the scores as empty anthropic's agent teams docs say two teammates editing the same file "leads to overwrites" and suggest splitting file ownership by hand, which works until the task needs the shared file. there's also a paper (agenticflict) that looked at 107k+ agent PRs and 27.67% of them hit a merge conflict with the base branch so how are you all splitting work when you run more than one? worktrees, separate clones, some plan file, or just hoping for the best? and has anyone tried claude code + codex on the same repo at the same time
