---
id: "5eb967d2fbc17167"
title: "Claude weekly roundup (Oct 11–17): Claude found the NIST curve seeds, Code Review goes GA"
url: "https://reddit.com/r/ClaudeAI/comments/1x7tcj3/claude_weekly_roundup_oct_1117_claude_found_the"
link: "https://reddit.com/r/ClaudeAI/comments/1x7tcj3/claude_weekly_roundup_oct_1117_claude_found_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T22:01:17Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["reactornewbie"]
language: "en"
summary: "Here's what happened around Claude and Claude Code this week, with links to the original sources. 1. Claude worked out where the NIST ECDSA curve seeds came from Anthropic's Frontier Red Team says an internal research model figured out in under half an hour that the seeds for P-192 through P-521 weren't hashes at all. They're output from the old C lrand48 generator seeded with Unix timestamps…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "US government"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 404
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7tcj3/claude_weekly_roundup_oct_1117_claude_found_the/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude weekly roundup (Oct 11–17): Claude found the NIST curve seeds, Code Review goes GA

Reddit · reactornewbie · 2026-10-16

Here's what happened around Claude and Claude Code this week, with links to the original sources. 1. Claude worked out where the NIST ECDSA curve seeds came from Anthropic's Frontier Red Team says an internal research model figured out in under half an hour that the seeds for P-192 through P-521 weren't hashes at all. They're output from the old C lrand48 generator seeded with Unix timestamps from May 1997 to April 1998 (P-256 was candidate 1,842 of its run). Anthropic says this isn't a break and makes a backdoor less plausible. The $36,864 bounty goes to ISRG. Source: https://www.anthropic.com/research/ecdsa-curve-origins 2. Claude Code Review is generally available Code Review is out of research preview on Team and Enterprise. Most reviews now finish in about 6–10 minutes, roughly 3x faster than in preview, and admins can pick Quick, Standard or Deep per repo. Source: https://claude.com/resources/articles/code-review-is-now-generally-available 3. "Claude writes about 90% of Claude Code's code" The Claude Code team wrote up how they review code at that volume. From June to September, merged PRs more than doubled while the share that had to be reverted fell by more than 40%. Most reading is done by agents, and a classifier decides whether a PR needs zero, one or two human approvers. Source: https://claude.dev/blog/solving-code-review-at-anthropic/ 4. Opus 5.5 fast mode: waitlist removed on the API Fast mode (same Opus 5.5, up to 2.5x faster output) is out of research preview for all API customers at $8/$40 per million input/output tokens. Set speed: "fast" ; no beta header needed. In Claude Code it still draws on extra usage credits. Source: https://platform.claude.com/docs/en/build-with-claude/fast-mode 5. Linus Torvalds used Claude Code for a kernel patch Phoronix spotted a branch in Torvalds' tree where the commit message says the code, test programs and first draft of the text "were done with an LLM coding assistant (Claude Code) under my direction." Source: https://www.phoronix.com/news/Linus-Torvalds-Claude-Code Claude Code tips from this week Copy gitignored files into worktrees. Put a .worktreeinclude file in the project root (gitignore syntax, e.g. .env , .env.local ) and Claude Code copies matching gitignored files into every new worktree session. Docs: https://code.claude.com/docs/en/worktrees#copy-gitignored-files-into-worktrees See what's eating your plan limits. /usage on Pro/Max/Team/Enterprise now breaks recent usage down by skills, subagents, plugins and individual MCP servers, and flags things like long context or cache misses when they account for 10%+. Docs: https://code.claude.com/docs/en/costs#plan-usage-breakdown I put this together for a small free daily digest ( https://ailetter.ai.kr/en ). Corrections welcome.
