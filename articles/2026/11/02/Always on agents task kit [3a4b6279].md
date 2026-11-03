---
id: "3a4b627920f581be"
title: "Always on agents task kit"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xm8az3/always_on_agents_task_kit"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xm8az3/always_on_agents_task_kit"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T20:20:06Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["ConstructTech"]
language: "en"
summary: "I built this approach to give my dot agent a lasting working memory and a structured way to move tasks forward without repeatedly explaining their history. Work is organized into persistent projects, either ongoing subject areas such as finance and troubleshooting or individual projects with milestones and deadlines. Each keeps concise records of tasks, decisions, supporting evidence, and…"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI"]
topics: ["agents & coding"]
content_source: "post"
word_count: 279
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xm8az3/always_on_agents_task_kit/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Always on agents task kit

Reddit · ConstructTech · 2026-11-02

I built this approach to give my dot agent a lasting working memory and a structured way to move tasks forward without repeatedly explaining their history. Work is organized into persistent projects, either ongoing subject areas such as finance and troubleshooting or individual projects with milestones and deadlines. Each keeps concise records of tasks, decisions, supporting evidence, and follow-ups. I use ChatGPT’s dot, but this is meant to be platform agnostic. I hope this helps someone! A central Active Tasks List serves as the agent’s starting point. Each task has an identifier, status, owner, next action, dependencies, and links to supporting material. The agent reads deeper project records only when needed. Scheduled refreshes inspect new messages and changed files, preserving successful checkpoints and flagging gaps in coverage. The agent then selects unfinished work it can advance: researching requirements, reconciling receipts, preparing documents, checking responses, or assembling decisions. No new messages does not mean no work remains. Execution and recordkeeping are separated. The agent logs its results, and a reconciliation process updates the project records and central list. This reduces conflicting edits and preserves decisions and completed history. Human approval remains essential for consequential actions. A task entry alone does not authorize communications, payments, submissions, or account changes. Progress reports distinguish preparation from completion and assumptions from verified outcomes. I interact mainly through conversation and concise updates. This repository shares the instructions, templates, and conventions behind that workflow. It requires compatible connected tools and configured scheduling, rather than functioning as a standalone agent platform. Here’s the direct link: https://github.com/62zkjj4k67-dot/Dots_long_context Link that an always on agents can utilize for the setup file: https://raw.githubusercontent.com/62zkjj4k67-dot/Dots_long_context/main/SETUP.md Finally, the link to the whole kit: https://github.com/62zkjj4k67-dot/Dots_long_context/releases/tag/v2.0.0
