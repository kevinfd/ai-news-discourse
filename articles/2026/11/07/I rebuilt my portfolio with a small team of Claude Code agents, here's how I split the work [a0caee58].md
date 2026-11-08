---
id: "a0caee5811a6a193"
title: "I rebuilt my portfolio with a small team of Claude Code agents, here's how I split the work"
url: "https://reddit.com/r/ClaudeAI/comments/1xqbnap/i_rebuilt_my_portfolio_with_a_small_team_of"
link: "https://reddit.com/r/ClaudeAI/comments/1xqbnap/i_rebuilt_my_portfolio_with_a_small_team_of"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T17:19:37Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["WillowFar6967"]
language: "en"
summary: "I'm a Webflow developer, and I used my own portfolio as a test of how far I could get with Claude Code on a real build I'd actually put my name on. Instead of one long session, I split it into agents that each own one area: one for code, one for copy, one for 3D, one for brand. Each has its own folder and a handover file it updates as it works. When one needs something from another, it sends a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 199
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqbnap/i_rebuilt_my_portfolio_with_a_small_team_of/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I rebuilt my portfolio with a small team of Claude Code agents, here's how I split the work

Reddit · WillowFar6967 · 2026-11-07

I'm a Webflow developer, and I used my own portfolio as a test of how far I could get with Claude Code on a real build I'd actually put my name on. Instead of one long session, I split it into agents that each own one area: one for code, one for copy, one for 3D, one for brand. Each has its own folder and a handover file it updates as it works. When one needs something from another, it sends a message and the owner makes the change. What made the difference: - Handover files. A new session reads one file and knows where things stand, so I'm not re-explaining the project every time - Clear ownership. Most of the mess early on came from two agents touching the same file - I made the calls on stack, architecture and what goes to production, and reviewed everything before it shipped Stack ended up as Astro with MDX, three.js, GSAP and Lenis, deployed to Cloudflare Workers, with staging deploying on every push and main only when I say so. If you're running more than one agent on a project, how are you stopping them overwriting each other? Site Link
