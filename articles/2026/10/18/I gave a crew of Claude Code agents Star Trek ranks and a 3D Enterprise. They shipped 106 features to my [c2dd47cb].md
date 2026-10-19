---
id: "c2dd47cb76f5be84"
title: "I gave a crew of Claude Code agents Star Trek ranks and a 3D Enterprise. They shipped 106 features to my journal app last week while I was on vacation."
url: "https://reddit.com/r/ClaudeAI/comments/1x9cq67/i_gave_a_crew_of_claude_code_agents_star_trek"
link: "https://reddit.com/r/ClaudeAI/comments/1x9cq67/i_gave_a_crew_of_claude_code_agents_star_trek"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T19:57:43Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["CatalinMihaiSafta"]
language: "en"
summary: "I've been exploring what software built for exactly one user looks like when AI agents do the building. My journal app (LCARS, Star Trek styled) has a crew: each engineer is a Claude Code session in its own git worktree, running in herdr so it survives me closing the page. A \"Number One\" session (Fable 5.1) writes their orders, reviews their diffs and deploys what passes. Engineers are Opus 5.5.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 206
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9cq67/i_gave_a_crew_of_claude_code_agents_star_trek/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave a crew of Claude Code agents Star Trek ranks and a 3D Enterprise. They shipped 106 features to my journal app last week while I was on vacation.

Reddit · CatalinMihaiSafta · 2026-10-18

I've been exploring what software built for exactly one user looks like when AI agents do the building. My journal app (LCARS, Star Trek styled) has a crew: each engineer is a Claude Code session in its own git worktree, running in herdr so it survives me closing the page. A "Number One" session (Fable 5.1) writes their orders, reviews their diffs and deploys what passes. Engineers are Opus 5.5. Things that turned out to matter: - nothing deploys on its own - a fixed script rebases, runs the test suite (including a 60 fps frame budget in headless Chromium), merges and restarts; 28 of 230 deploys failed, almost all caught by tests - one engineer at a time ("the seat"): parallel agents fight over the same files and merge conflicts burn tokens - every engineer gives an estimate; they run about 3x too long - anything the crew needs to remember is an entry in the journal, so I can read and edit it I haven't written a line of it since October, and I'm the only user. Write-up with videos (including a real navigator agent planning a hike from one sentence): https://mihai-safta.dev/posts/lcars_journal/?utm_source=reddit&utm_medium=social&utm_campaign=lcars_journal&utm_content=r_claudeai Not open source yet - happy to answer how any part works.
