---
id: "c26ce9de72d8b220"
title: "I’m experimenting with Codex and Claude Code working on the same project. Here’s what I’m trying to solve."
url: "https://reddit.com/r/ClaudeAI/comments/1xpp347/im_experimenting_with_codex_and_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1xpp347/im_experimenting_with_codex_and_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T21:44:07Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["holyhacker"]
language: "en"
summary: "I’m experimenting with Codex and Claude Code working on the same project. Here’s what I’m trying to solve. I’ve been using AI coding tools for a while, and lately I’ve been thinking about something that seems more complicated than it should be. Why am I still treating each coding agent like a separate developer working alone? Codex is good at certain tasks. Claude Code is good at others. But…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 479
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpp347/im_experimenting_with_codex_and_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I’m experimenting with Codex and Claude Code working on the same project. Here’s what I’m trying to solve.

Reddit · holyhacker · 2026-11-06

I’m experimenting with Codex and Claude Code working on the same project. Here’s what I’m trying to solve. I’ve been using AI coding tools for a while, and lately I’ve been thinking about something that seems more complicated than it should be. Why am I still treating each coding agent like a separate developer working alone? Codex is good at certain tasks. Claude Code is good at others. But when you’re working on a real project, switching between them manually gets old pretty quickly. So I’ve started exploring a setup where both can work on the same codebase, potentially at the same time. Not just passing prompts between them, but actually coordinating the work. The problem I’m trying to solve Imagine having two developers working on the same project. One is implementing a feature while the other is reviewing the architecture, checking security, or writing tests. That sounds useful until both start modifying the same files, making conflicting assumptions, or introducing changes that work individually but break when combined. Now replace those developers with Codex and Claude Code. That’s basically the challenge. What I’m exploring My current direction is to use an orchestration layer that can: Break larger tasks into smaller, independent pieces. Assign tasks to Codex or Claude Code based on what needs to be done. Give each agent an isolated Git worktree or branch. Keep a shared understanding of the project requirements without letting agents blindly overwrite each other’s work. Run tests and validation before integrating changes. Have one agent review another agent’s work. Require human approval for sensitive operations and important merges. I’m also considering whether a third agent should act as a coordinator, or whether that would just introduce another layer of complexity. The part I’m most interested in is failure handling. What happens when one agent finishes a task based on code that another agent has already changed? What if both agents produce perfectly valid changes that are incompatible when merged? And how do you prevent an automated reviewer from confidently approving something it doesn’t fully understand? I don’t want to build a system that just runs more AI agents and burns more tokens. The goal is to make the development process more reliable and useful, not just more automated. A few questions for people using Claude Code seriously: Have you tried running Claude Code alongside Codex on the same project? Are you using Git worktrees, separate containers, or something else for isolation? Do you prefer one orchestrator assigning tasks, or agents coordinating directly? How do you handle shared context without constantly copying massive instruction files between agents? Has multi-agent development actually improved your results, or just increased cost and complexity? I’m particularly interested in setups people are actually using, including the things that didn’t work. If you’ve built something similar or found a workflow that works well, I’d love to hear about it.
