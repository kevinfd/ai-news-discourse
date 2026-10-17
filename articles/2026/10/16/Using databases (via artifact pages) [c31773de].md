---
id: "c31773dec45ca617"
title: "Using databases (via artifact pages)"
url: "https://reddit.com/r/ClaudeAI/comments/1x7vrzh/using_databases_via_artifact_pages"
link: "https://reddit.com/r/ClaudeAI/comments/1x7vrzh/using_databases_via_artifact_pages"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T23:52:10Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["thatzombiefilm"]
language: "en"
summary: "I'm an attorney and Claude (Cowork) is keeping two databases to 1) keep track of work and personal matters (case tracking, calendar obligations, etc.), and 2) somewhere for the projects to communicate and save stored knowledge. I work out of three projects that access the databases: personal assistant, research & writing, and intake (potential new clients). I am NOT a sophisticated user and have…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 331
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7vrzh/using_databases_via_artifact_pages/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Using databases (via artifact pages)

Reddit · thatzombiefilm · 2026-10-16

I'm an attorney and Claude (Cowork) is keeping two databases to 1) keep track of work and personal matters (case tracking, calendar obligations, etc.), and 2) somewhere for the projects to communicate and save stored knowledge. I work out of three projects that access the databases: personal assistant, research & writing, and intake (potential new clients). I am NOT a sophisticated user and have only been using Claude for a month, so I appreciate any tips before I travel too far down this path. Database 1: The tracker (“Daily To-Dos” page) Holds to-dos, matters, deadlines, intake, voicemails and the page’s working data. There’s one doc per row with permanent ids, and nothing is deleted. The page renders live from the data, and scheduled tasks update it all day. Database 2: The Decision Record The idea is to have a place where Claude can reference prior decisions or discussions without reading stored chats. Holds workflow decisions only. Each has five parts: question, options, decision (and who decided), why, and “revisit if.” It’s stored as one doc per project per day. It’s kept separate to protect the tracker’s 25,000-doc cap. A nightly task exports it to Markdown for project search and flags any entry that might name a client. It’s shared across projects (Personal Assistant, Research & Writing, and Intake), and a mail collection lets those projects message each other independently. How the projects split the data People and events go in the tracker, workflow goes in the Decision Record, and case substance stays in the firm’s own files. (I have separate case notes MD and discovery MD files in each separate client folder, rather than separate projects or bloating the reference docs in the R&W project). Single-writer rule: each collection has one owning project. Backups A nightly mirror writes the tracker to SharePoint with sha256 fingerprints, and a restore test runs monthly. Project docs are exported to SharePoint monthly. The biggest risk: deleting either artifact page would most likely delete its database.
