---
id: "b5796cd2e8d32d7f"
title: "Sandboxed Claude agents wrote 159 of my 188 PRs"
url: "https://reddit.com/r/ClaudeAI/comments/1xagj87/sandboxed_claude_agents_wrote_159_of_my_188_prs"
link: "https://reddit.com/r/ClaudeAI/comments/1xagj87/sandboxed_claude_agents_wrote_159_of_my_188_prs"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T02:37:45Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["dbggr-au"]
language: "en"
summary: "I'd been playing with Matt Pocock's sandcastle , which gives you the pieces to build your own agent loops. I liked it, but I kept wanting something with fewer choices: one loop, already decided, that I could point at a repo and walk away from. So I built bunker . You put a bunker:queued label on a GitHub issue, and it: runs Claude Code on it in its own git worktree and Docker container has a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 238
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xagj87/sandboxed_claude_agents_wrote_159_of_my_188_prs/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Sandboxed Claude agents wrote 159 of my 188 PRs

Reddit · dbggr-au · 2026-10-20

I'd been playing with Matt Pocock's sandcastle , which gives you the pieces to build your own agent loops. I liked it, but I kept wanting something with fewer choices: one loop, already decided, that I could point at a repo and walk away from. So I built bunker . You put a bunker:queued label on a GitHub issue, and it: runs Claude Code on it in its own git worktree and Docker container has a second Claude session review the change and send it back if it's not right runs the repo's tests in the sandbox with no network opens a PR and turns on GitHub auto-merge, so your required CI check decides whether it lands Anything touching CI, its own config or agent instructions waits for a human. Only maintainers can queue work. It's been building itself. About 160 of its first 190 PRs were its own, and an issue costs around $1.30 of Sonnet time on average. This week I pointed it at a few of my other repos and found a pile of wrong assumptions on bunker's side. For example, fine-grained GitHub tokens can't read check runs at all, so its "fix the red CI" step was blind until I changed how it reads CI. It's v0.11 (and moving towards v1), Claude only, Linux/macOS with Docker. MIT. Repo: https://github.com/dbggr/bunker · Docs: https://bunker.true.engineer If you try it, I'd really like to hear where it breaks.
