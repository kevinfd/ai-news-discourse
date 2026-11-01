---
id: "31d775cc4e27c1e8"
title: "I built an app where my AI agents delegate to each other and only ask me when they're stuck"
url: "https://reddit.com/r/ClaudeAI/comments/1xkgzcu/i_built_an_app_where_my_ai_agents_delegate_to"
link: "https://reddit.com/r/ClaudeAI/comments/1xkgzcu/i_built_an_app_where_my_ai_agents_delegate_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T18:03:18Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["jidma81"]
language: "en"
summary: "I'm a full-stack developer and like a lot of devs I use AI in my daily work, usually several Claude and Codex sessions in parallel, each on a different piece of work. At some point it was too much mental load and the bottleneck was me. I was passing context between sessions, reading what each agent said to figure out what to do next, and when I wanted to move a task from Claude to Codex I had to…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "post"
word_count: 329
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkgzcu/i_built_an_app_where_my_ai_agents_delegate_to/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an app where my AI agents delegate to each other and only ask me when they're stuck

Reddit · jidma81 · 2026-10-31

I'm a full-stack developer and like a lot of devs I use AI in my daily work, usually several Claude and Codex sessions in parallel, each on a different piece of work. At some point it was too much mental load and the bottleneck was me. I was passing context between sessions, reading what each agent said to figure out what to do next, and when I wanted to move a task from Claude to Codex I had to explain everything again. And I had to be present and supervising all the time. So I built BroCrew, an open-source desktop app where agents delegate work to each other and report back. I follow their work in a tree and answer their questions in one place. What it does in practice: - Claude and Codex agents (more providers planned) hand work to each other and come to me when they need something. - I can ask an agent to speed up or slow down depending on my usage, or to give work to Codex instead of Claude. - It runs the native Claude Code and Codex themselves underneath. - Each agent keeps its own memory: my "developer" agent remembers dev stuff across projects, the "travel-manager" remembers my travel preferences. - You describe in plain English how you want the agents to work and it sets up the team. - All subagents are actual Claude/Codex agents you can talk to directly. I've been using it exclusively for the past few weeks, including to build BroCrew itself. It made my own experience way better. Claude Code wrote most of it and Codex did the testing and reviews. It's free to try and open source. The Windows and the Mac apps aren't signed yet, so your system will warn you the first time; the install guides show how to open it. You can also run it from source. Code: https://github.com/brocrew/brocrew If you give it a try, please let me know what you think.
