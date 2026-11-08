---
id: "a881ade2b8493cef"
title: "I made a management game where Claude Code does the work and you deal with the office drama"
url: "https://reddit.com/r/ClaudeAI/comments/1xqus4b/i_made_a_management_game_where_claude_code_does"
link: "https://reddit.com/r/ClaudeAI/comments/1xqus4b/i_made_a_management_game_where_claude_code_does"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T09:47:05Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Vegetable-Cod-5098"]
language: "en"
summary: "It started as a joke about how lonely it is to spend all day in a terminal full of agents. Now it's a cozy management game. You hire people one at a time, starting from one desk in a small flat. Each one is a Claude Code agent with a personality and opinions about the others. Keep them happy and the studio earns more, all the way to an office in Manhattan. In one playtest Mia sent Noah's work…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 353
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqus4b/i_made_a_management_game_where_claude_code_does/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a management game where Claude Code does the work and you deal with the office drama

Reddit · Vegetable-Cod-5098 · 2026-11-08

It started as a joke about how lonely it is to spend all day in a terminal full of agents. Now it's a cozy management game. You hire people one at a time, starting from one desk in a small flat. Each one is a Claude Code agent with a personality and opinions about the others. Keep them happy and the studio earns more, all the way to an office in Manhattan. In one playtest Mia sent Noah's work back, he sulked, and I had to talk him into asking her what she wanted. They're friends now. How it works Every employee turn is a Claude Code process started through the Agent SDK. Each studio has its own CLAUDE_CONFIG_DIR, so it never touches my own setup. Projects start with a meeting where teammates split the work, and each piece gets a teammate as reviewer. A failed review goes back into the same session with notes. When someone needs me they use Claude Code's own AskUserQuestion, which the game turns into a note on my desk. Work can change their mood, like Noah taking that rework hard, but moods never go into the prompts, so they don't change the work. They only change how much the studio earns. Nobody wants a grumpy agent near rm -rf. How I built it Under a month with Claude Code, which wrote nearly all of the code while I directed. What helped most was turning CLAUDE.md rules into checks it has to pass before every commit, because it drifts from written rules on a long project. All 381 3D models are Blender Python scripts Claude wrote. The music works the same way. The background track and four jukebox songs are scores Claude wrote in JavaScript, turned into MIDI and rendered with FluidSynth. The sound effects come out of the same scripts. Bring your own API key, or use the free credits new players get. It's free in Early Access on Mac and Windows, link in the comments. Would you want your agents to come with a little office drama, or do you get enough of that at work?
