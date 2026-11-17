---
id: "5ab3b094f3584861"
title: "I built a Mac app where Claude leads a team of different AIs — Codex, Gemini, Cursor — and they check each other's work"
url: "https://reddit.com/r/ClaudeAI/comments/1xyg0ed/i_built_a_mac_app_where_claude_leads_a_team_of"
link: "https://reddit.com/r/ClaudeAI/comments/1xyg0ed/i_built_a_mac_app_where_claude_leads_a_team_of"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T09:24:15Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["No-Advisor-4882"]
language: "en"
summary: "I kept running into the same loop with AI coding: ask, copy, paste, test, ask again. The models were smart, but I was still the glue between every step. So I built Sumparo, a Mac app where one task becomes a team: - A lead agent (Claude) splits the task into parts. - Each part goes to a different AI — e.g. Codex builds, Gemini translates, Cursor designs, Claude writes tests. - Every agent works…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Cursor"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "post"
word_count: 288
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xyg0ed/i_built_a_mac_app_where_claude_leads_a_team_of/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Mac app where Claude leads a team of different AIs — Codex, Gemini, Cursor — and they check each other's work

Reddit · No-Advisor-4882 · 2026-11-17

I kept running into the same loop with AI coding: ask, copy, paste, test, ask again. The models were smart, but I was still the glue between every step. So I built Sumparo, a Mac app where one task becomes a team: - A lead agent (Claude) splits the task into parts. - Each part goes to a different AI — e.g. Codex builds, Gemini translates, Cursor designs, Claude writes tests. - Every agent works in its own copy of the project (git worktree), so nobody breaks anyone's work. - Another model reviews the result, and a quick checker sends unfinished work back before it reaches the lead. - Nothing counts as "done" until there's proof — a command that actually ran (tests, a build, a live page). - I can approve or redirect from my iPhone while my Mac does the work. The fun part: I built Sumparo with Sumparo. The landing page, two promo films, a licensing server and an animated assistant inside the app were all done by fleets of agents, with Claude leading. The video shows one task — "build a bakery website in 3 languages, fully tested" — going from one line to a finished site with four different AIs working at once. Things I learned building it: Agents explain when the goal is fuzzy and execute when the finish line is concrete and checkable. A different model reviewing the work catches far more than the same model reviewing itself. Background tasks are the #1 reason agents "finish" without a result — they say "waiting for the tests" and end the turn. It's a free beta right now. Link in the comments. What would you hand to a team of different AIs first?
