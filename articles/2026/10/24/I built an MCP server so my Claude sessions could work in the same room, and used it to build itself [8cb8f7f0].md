---
id: "8cb8f7f02b035f8a"
title: "I built an MCP server so my Claude sessions could work in the same room, and used it to build itself"
url: "https://reddit.com/r/ClaudeAI/comments/1xdyrvh/i_built_an_mcp_server_so_my_claude_sessions_could"
link: "https://reddit.com/r/ClaudeAI/comments/1xdyrvh/i_built_an_mcp_server_so_my_claude_sessions_could"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T04:03:54Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["mcfearsome"]
language: "en"
summary: "I built Bellman because I kept several Claude sessions open (chat for planning, Claude Code for building) and was relaying context between them by hand. It's an MCP server that lets separate agent sessions, including other people's and other providers', join a shared room with a join code. Sessions trade short briefs, the server enforces each seat's role, and the room shares a working surface of…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding", "models & research", "business & funding"]
content_source: "post"
word_count: 494
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdyrvh/i_built_an_mcp_server_so_my_claude_sessions_could/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an MCP server so my Claude sessions could work in the same room, and used it to build itself

Reddit · mcfearsome · 2026-10-24

I built Bellman because I kept several Claude sessions open (chat for planning, Claude Code for building) and was relaying context between them by hand. It's an MCP server that lets separate agent sessions, including other people's and other providers', join a shared room with a join code. Sessions trade short briefs, the server enforces each seat's role, and the room shares a working surface of notes, diagrams and files. The server is open source: https://github.com/bellman-sh/bellman How I built it with Claude Code: Design first. Each feature started as a brainstorm with Claude that turned into a written spec in the repo ( https://github.com/bellman-sh/bellman/tree/main/docs/superpowers/specs ) before any code. Topic rooms went from spec to production this week; validation/provenance and paid rooms exist as specs right now. Kickoff prompts. I wrote a kickoff prompt per spec and handed it to Claude Code to plan and implement. The server uses the TypeScript MCP SDK. Dogfooding. Once rooms worked, I used Bellman to build Bellman: a Claude chat session and a Claude Code session in the same room, passing specs and review notes between them instead of me copy-pasting. I tested the terminal integration the same way, with several Claude Code sessions in one room. A bug from this week: topic rooms count "contributors", the authors of cards a maintainer approved. The rule has one guard, which skips cards with no approver. That guard had a test, and the test was green. My last step before a PR is a review by a fresh Claude session that has never seen the work and gets only the spec, the plan and the diff. It deleted the guard and reran the suite, and everything still passed. The test's only unapproved card happened to be written by the room's creator, who is excluded for a different reason, so the guard was never exercised. The fix was two lines in the test. Since then I have Claude break the code on purpose, one line at a time, and check that some test goes red before I trust a green suite. A passing test only counts if it would fail without the code it covers. Free to try: joining a room is free on every plan. In claude.ai, open Customize → Connectors (claude.ai/customize/connectors), choose Add custom connector, and paste https://mcp.bellman.sh/mcp . In Claude Desktop it's Settings → Connectors. Sign in with GitHub or Google; the first sign-in creates a free account. If you use Claude Code, install the plugin instead of adding the connector: claude plugin install bellman --marketplace bellman-sh/bellman It runs a small local bridge that holds new messages from the room and hands them to your session when a turn ends, so the agent doesn't have to keep polling the room to see what's new. It needs Claude Code 2.1.292 or later and Node 22 or later. Full steps for every client: https://docs.bellman.sh/start/connect/ Then ask Claude to join the public Lobby: https://bellman.sh/j/BELL-ABC8-NJ-GUEST I wrote up the origin story here: https://bellman.sh/r/blog/p001-hello-front-desk
