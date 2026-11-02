---
id: "44e062c310dfbc9e"
title: "Claude Code's docs say CLAUDE.md is context, not enforced config. What have you moved into hooks because Claude kept skipping it?"
url: "https://reddit.com/r/ClaudeAI/comments/1xlujwl/claude_codes_docs_say_claudemd_is_context_not"
link: "https://reddit.com/r/ClaudeAI/comments/1xlujwl/claude_codes_docs_say_claudemd_is_context_not"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T11:19:40Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["ombre-ai"]
language: "en"
summary: "Anthropic's memory docs for Claude Code say CLAUDE.md and auto memory are both loaded at the start of every conversation, but Claude treats them as context, not enforced configuration. For anything that has to happen no matter what, the docs point to hooks (a PreToolUse hook can block an action). That's easy to nod along to and still leave mandatory rules as polite sentences in a markdown file.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["agents & coding"]
content_source: "post"
word_count: 188
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlujwl/claude_codes_docs_say_claudemd_is_context_not/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code's docs say CLAUDE.md is context, not enforced config. What have you moved into hooks because Claude kept skipping it?

Reddit · ombre-ai · 2026-11-02

Anthropic's memory docs for Claude Code say CLAUDE.md and auto memory are both loaded at the start of every conversation, but Claude treats them as context, not enforced configuration. For anything that has to happen no matter what, the docs point to hooks (a PreToolUse hook can block an action). That's easy to nod along to and still leave mandatory rules as polite sentences in a markdown file. OpenAI's Codex team wrote something related in their Feb 2026 harness engineering post. Their "one big AGENTS.md" approach failed (context crowded out, rules went stale), so they cut it to a roughly 100-line map that points to deeper docs, and enforced the invariants that mattered with linters and tests instead of prose. I'm curious how people here actually split it: - What lives in CLAUDE.md (conventions, where things are, how to run stuff)? - What did you move into a hook or a test because Claude kept missing it? - What did you delete because it stopped being true? Sources: Claude Code docs ("How Claude remembers your project"), OpenAI "Harness engineering: leveraging Codex in an agent-first world" (Feb 11, 2026).
