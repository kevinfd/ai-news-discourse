---
id: "9eaa1b98c1542707"
title: "A gist of starter docs that help coding agents keep a codebase documented"
url: "https://reddit.com/r/ClaudeAI/comments/1x9y9ty/a_gist_of_starter_docs_that_help_coding_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1x9y9ty/a_gist_of_starter_docs_that_help_coding_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T14:23:47Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["CaHoop"]
language: "en"
summary: "I've put together a small set of docs I copy into every new repo. They help Claude Code write down what a fresh session needs, such as what the project is for, which decisions were made and why, and how the work runs. Every session starts with no memory, so this is the part that usually goes missing. https://gist.github.com/coopie/c9ca8c4563b2e1e8506a707a508084b8 A few ideas run through them:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 165
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9y9ty/a_gist_of_starter_docs_that_help_coding_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# A gist of starter docs that help coding agents keep a codebase documented

Reddit · CaHoop · 2026-10-19

I've put together a small set of docs I copy into every new repo. They help Claude Code write down what a fresh session needs, such as what the project is for, which decisions were made and why, and how the work runs. Every session starts with no memory, so this is the part that usually goes missing. https://gist.github.com/coopie/c9ca8c4563b2e1e8506a707a508084b8 A few ideas run through them: Context and guidance first, with the reasons, and few instructions. A CLAUDE.md that grows one rule at a time slowly gets worse. Rewrite the whole doc when something changes, so it doesn't turn into a list of patches. Use a fresh agent to review each piece of work. It has only the repo to go on, so it shows where the docs have gaps. They work just as well when the thing you're building is an agent itself. I wrote up the thinking behind them here, if it's useful: https://grokking.agency/posts/building-agents-with-agents-part-1 I'm curious what others keep in their repos for agents.
