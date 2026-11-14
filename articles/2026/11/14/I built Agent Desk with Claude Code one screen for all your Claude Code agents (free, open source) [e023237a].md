---
id: "e023237a10b7003a"
title: "I built Agent Desk with Claude Code: one screen for all your Claude Code agents (free, open source)"
url: "https://reddit.com/r/ClaudeAI/comments/1xvvqzh/i_built_agent_desk_with_claude_code_one_screen"
link: "https://reddit.com/r/ClaudeAI/comments/1xvvqzh/i_built_agent_desk_with_claude_code_one_screen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-14T06:51:55Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["theguysperry"]
language: "en"
summary: "I run a lot of Claude Code agents at once with agent-manager, each in its own tmux pane. I kept finding one stuck on a permission prompt for twenty minutes while I watched another. So I built Agent Desk : a free, open-source (Apache 2.0) local GUI where every agent is on one screen. What it does Answer any agent in one click. Permission prompts and AskUserQuestion dialogs become buttons:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "post"
word_count: 398
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvvqzh/i_built_agent_desk_with_claude_code_one_screen/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built Agent Desk with Claude Code: one screen for all your Claude Code agents (free, open source)

Reddit · theguysperry · 2026-11-14

I run a lot of Claude Code agents at once with agent-manager, each in its own tmux pane. I kept finding one stuck on a permission prompt for twenty minutes while I watched another. So I built Agent Desk : a free, open-source (Apache 2.0) local GUI where every agent is on one screen. What it does Answer any agent in one click. Permission prompts and AskUserQuestion dialogs become buttons: multi-select, typed answers, and going back to change an earlier answer. It re-reads the screen before pressing a key, so it never answers a question that changed. Sessions read like documents. Prose first, tool runs folded to one line, edits as diffs, search across every transcript. The whole fleet at a glance. A card per session, waiting ones first, notifications, and a live row showing what each agent is doing, with Interrupt. Review and steer. Comment on a session's diff line by line; the comments go back as one prompt. System stats (CPU, memory, swap, disk), with an alert before parallel builds fill your disk. From your phone over Tailscale or Cloudflare, at a permission level you set. A signed Mac app with a dock badge for agents that need you. No API key and no model calls. It reads Claude Code's files locally, and your agents keep running in tmux if you close it. How Claude Code built it Claude Code wrote nearly all of it: Go server, React UI, tests and the Mac app. I made the product calls, set the rules and reviewed every PR. Rules in CLAUDE.md first: never write to ~/.claude , never call a model API, talk to agent-manager only through its CLI. It held to them for the whole build. Plan, then small milestones, each ending in passing tests and a PR. It checked its own UI with Playwright screenshots, which caught layout and dark-mode bugs the tests missed. Real prompts, not guesses: it ran throwaway Claude Code sessions to capture real permission and question screens as test fixtures, and verified fixes against live prompts. Built from inside itself: the session building Agent Desk ran in agent-manager, so I answered its questions in Agent Desk, and most bugs came from that daily use. Try it free (macOS or Linux): brew install gsperry/tap/agent-desk The Mac app, a 20-second demo and the source: https://agent-desk.app It's early. Tell me what breaks and what's missing.
