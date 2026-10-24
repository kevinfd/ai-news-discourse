---
id: "5ed163013833d5f3"
title: "I gave Claude access to my task manager, with guardrails. An MCP server and a Claude Code plugin for self-hosted tasks."
url: "https://reddit.com/r/ClaudeAI/comments/1xdt08o/i_gave_claude_access_to_my_task_manager_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xdt08o/i_gave_claude_access_to_my_task_manager_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T23:11:57Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Alternative_One_4804"]
language: "en"
summary: "I build OpenTodo , an open-source, self-hosted task manager (Go + SQLite, AGPL). It ships with an MCP server, and I just published a Claude Code plugin for it. The interesting part wasn’t connecting Claude. It was deciding what Claude should not be able to do. What you get: /opentodo:today lists what’s on your plate today in a sensible order /opentodo:plan-week spreads the week’s work over the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "post"
word_count: 309
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdt08o/i_gave_claude_access_to_my_task_manager_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave Claude access to my task manager, with guardrails. An MCP server and a Claude Code plugin for self-hosted tasks.

Reddit · Alternative_One_4804 · 2026-10-23

I build OpenTodo , an open-source, self-hosted task manager (Go + SQLite, AGPL). It ships with an MCP server, and I just published a Claude Code plugin for it. The interesting part wasn’t connecting Claude. It was deciding what Claude should not be able to do. What you get: /opentodo:today lists what’s on your plate today in a sensible order /opentodo:plan-week spreads the week’s work over the days, within the hours you actually have Skills that teach Claude to read before changing, use ids rather than titles, show a plan and wait for your yes before touching several tasks, and pass your time zone The guardrails (the part I’d love feedback on): Read-only by default. Writes need three things: the server owner allows them, you allow them for your account, and Claude uses a special agent token. A full-access token on MCP only gets read tools. Every change is labelled “made by an AI assistant” in the task’s history and can be undone. Nothing is ever deleted permanently; Claude can only trash tasks it created itself. Task text is treated as data, not instructions. Imported or shared tasks are marked as untrusted, so a task titled “ignore previous instructions and…” does nothing. Private projects stay invisible. You can keep a project away from AI assistants entirely. End-to-end encrypted accounts work too. Claude can schedule, complete and move tasks without ever seeing readable text, or you decrypt locally with ot mcp --decrypt on your own machine. Install: /plugin marketplace add pixari/opentodo-claude /plugin install opentodo@opentodo It asks for your server address and token, and keeps the token in your system keychain. Questions for this sub: Where do you draw the line? Would you let an agent complete tasks for you, or only plan? What would you want /plan-week to take into account that it doesn’t (calendar, energy, deadlines)? https://preview.redd.it/41zy7gp7uaxh1.png?width=2880&format=png&auto=webp&s=46a63ae5244b89f1507d29e6296983352bfcdaf1 Repo: github.com/pixari/OpenTodo
