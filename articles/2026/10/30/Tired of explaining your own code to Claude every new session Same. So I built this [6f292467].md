---
id: "6f2924674e8882e0"
title: "Tired of explaining your own code to Claude every new session? Same. So I built this."
url: "https://reddit.com/r/ClaudeAI/comments/1xj8gmc/tired_of_explaining_your_own_code_to_claude_every"
link: "https://reddit.com/r/ClaudeAI/comments/1xj8gmc/tired_of_explaining_your_own_code_to_claude_every"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T07:02:05Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["dheeraj_ponnaganti"]
language: "en"
summary: "Every new session I'd spend the first few minutes explaining why the code looks the way it does. The reasons were all sitting in old chats. Claude couldn't see them. So I built Thenwise , a free, open source plugin for Claude Code that gives Claude a memory of your past chats, commits and notes. All of it stays on your machine. You can ask things like: why did we split the cache? what did we…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 341
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj8gmc/tired_of_explaining_your_own_code_to_claude_every/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Tired of explaining your own code to Claude every new session? Same. So I built this.

Reddit · dheeraj_ponnaganti · 2026-10-30

Every new session I'd spend the first few minutes explaining why the code looks the way it does. The reasons were all sitting in old chats. Claude couldn't see them. So I built Thenwise , a free, open source plugin for Claude Code that gives Claude a memory of your past chats, commits and notes. All of it stays on your machine. You can ask things like: why did we split the cache? what did we already try for the retry bug? what was the plan on 6 Oct? Claude answers with the date and the chat it came from. How I built it with Claude Writing the code: I built it with Claude Code. I planned each part and Claude wrote most of the TypeScript with me: the local store, the search, the MCP server with its seven memory tools, and the hooks that save each chat when it ends. Reviewing: before each release I ran a separate Claude session that only looked for bugs. It found real problems (race conditions and sync edge cases) that I fixed before shipping. Testing: the eval runs Claude Code itself on questions about real project history with the answers hidden, once with Thenwise and once without, then grades the replies blind. Using it on itself: from early on I had Thenwise installed while building Thenwise, so Claude could look up why we made earlier decisions in the same repo. That surfaced a lot of rough edges fast. Results from that eval 83% right, against 47% for plain Claude Code about 40% fewer tokens 2.2x faster answers The method is in docs/eval.md if you want to poke holes in it. Free to try It's free and Apache 2.0, with no paid tier, no account and no telemetry. API keys get masked before anything is saved, and putting [no-memory] in a prompt means that chat is never kept. Install, inside Claude Code: /plugin marketplace add dheerajponnaganti/thenwise /plugin install thenwise@thenwise Repo: github.com/dheerajponnaganti/thenwise I use it every day while building it, so bug reports are very welcome.
