---
id: "19dd00d78e433d65"
title: "I turned my Claude Code + Knowledge Graph idea into an open-source project"
url: "https://reddit.com/r/ClaudeAI/comments/1xvd64t/i_turned_my_claude_code_knowledge_graph_idea_into"
link: "https://reddit.com/r/ClaudeAI/comments/1xvd64t/i_turned_my_claude_code_knowledge_graph_idea_into"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T16:57:44Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Shivam__kumar"]
language: "en"
summary: "A while ago, I shared an idea here about using Claude Code as an autonomous agent to explore a structured knowledge environment instead of building traditional retrieval pipelines. Previous discussion: https://www.reddit.com/r/ClaudeAI/comments/1xpjadb/comment/19sc8n19k5rdu/ Since then, I've actually built a working prototype around that idea. It's called Agent Workcell , and I've made it open…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "robotics & autonomy"]
content_source: "post"
word_count: 185
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvd64t/i_turned_my_claude_code_knowledge_graph_idea_into/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I turned my Claude Code + Knowledge Graph idea into an open-source project

Reddit · Shivam__kumar · 2026-11-13

A while ago, I shared an idea here about using Claude Code as an autonomous agent to explore a structured knowledge environment instead of building traditional retrieval pipelines. Previous discussion: https://www.reddit.com/r/ClaudeAI/comments/1xpjadb/comment/19sc8n19k5rdu/ Since then, I've actually built a working prototype around that idea. It's called Agent Workcell , and I've made it open source. Website: https://shivam7414.github.io/agent-workcell/ GitHub: https://github.com/Shivam7414/agent-workcell The idea is to reuse Claude Code as the agent runtime and give it an engineered environment containing structured knowledge, MCP tools, business rules, and controlled database access. Instead of building separate retrieval pipelines for different question types, the agent can explore the available knowledge, decide which tools to use, and take multiple steps to answer questions. I tested this approach against my traditional RAG implementation on an existing ERP system, and the results were very promising. The project currently uses Python, Claude Agent SDK, MCP, and PostgreSQL. It's still an early experiment. One challenge I'm working on is scaling it, since each user currently needs a separate CLI process and session. I'd be interested to hear what other Claude Code developers think of this approach and implementation.
