---
id: "3eb370fd02c8304c"
title: "Agentic Disk Cleanup Workflow"
url: "https://reddit.com/r/ClaudeAI/comments/1xd77e8/agentic_disk_cleanup_workflow"
link: "https://reddit.com/r/ClaudeAI/comments/1xd77e8/agentic_disk_cleanup_workflow"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T07:16:31Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["rjz4"]
language: "en"
summary: "My Mac’s 494 GB disk was 99% full, so I worked through a disk audit with an AI coding agent and turned the workflow into a reusable prompt. Some of the biggest wins were: 18 GB from node_modules and .next caches. 36 GB from old iOS simulator runtimes. 14 GB from Library caches. 14 GB from downloads I no longer needed. There were also misleading numbers. Docker.raw showed an apparent size of 60…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["agents & coding", "safety & ethics"]
content_source: "post"
word_count: 180
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xd77e8/agentic_disk_cleanup_workflow/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Agentic Disk Cleanup Workflow

Reddit · rjz4 · 2026-10-23

My Mac’s 494 GB disk was 99% full, so I worked through a disk audit with an AI coding agent and turned the workflow into a reusable prompt. Some of the biggest wins were: 18 GB from node_modules and .next caches. 36 GB from old iOS simulator runtimes. 14 GB from Library caches. 14 GB from downloads I no longer needed. There were also misleading numbers. Docker.raw showed an apparent size of 60 GB, but its actual disk usage was 14 GB. The prompt tells the agent to measure first, explain what it finds, group candidates into three risk tiers, and wait for approval. It also tells it to protect source code, git history, secrets, photos, mail stores, and cloud-sync folders. I’ve shared the full prompt in 7 languages, with instructions for macOS, Linux, and Windows: https://github.com/riza/ai-disk-cleanup A caveat: these are instructions to an agent, not enforced safety controls. Keep permission checks enabled, review the findings, and have a backup before approving deletions. I’m the author. Feedback on the workflow, especially anything it should never suggest deleting, would be useful.
