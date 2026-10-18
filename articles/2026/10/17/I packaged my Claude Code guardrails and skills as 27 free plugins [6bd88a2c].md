---
id: "6bd88a2c28027812"
title: "I packaged my Claude Code guardrails and skills as 27 free plugins"
url: "https://reddit.com/r/ClaudeAI/comments/1x8bp26/i_packaged_my_claude_code_guardrails_and_skills"
link: "https://reddit.com/r/ClaudeAI/comments/1x8bp26/i_packaged_my_claude_code_guardrails_and_skills"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T14:31:47Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["rezk2ll"]
language: "en"
summary: "I run Claude Code on real work repos, and I built up a set of hooks that stop it from doing things I'd regret. It can't merge, post GitHub comments as me, read .env files or rewrite tracked files with sed -i until I give an explicit go. I cleaned these up and published them as a free, MIT-licensed plugin marketplace, along with the skills I use for PRs, code reviews, ADRs and postmortems. How…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["safety & ethics"]
content_source: "post"
word_count: 208
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8bp26/i_packaged_my_claude_code_guardrails_and_skills/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I packaged my Claude Code guardrails and skills as 27 free plugins

Reddit · rezk2ll · 2026-10-17

I run Claude Code on real work repos, and I built up a set of hooks that stop it from doing things I'd regret. It can't merge, post GitHub comments as me, read .env files or rewrite tracked files with sed -i until I give an explicit go. I cleaned these up and published them as a free, MIT-licensed plugin marketplace, along with the skills I use for PRs, code reviews, ADRs and postmortems. How Claude helped: I built all of it with Claude Code. Many of the guardrails started as a mistake it made in a session: I log every mistake, and when one keeps coming back it becomes a hook that blocks it. The site that documents the plugins reads each plugin's README at build time, so the docs can't drift from the code. What's in it (27 plugins): Guardrails: guard , pre-ship-gate (refuses commits that mix file moves with logic), worktree-guard , stop-check , text-lint Skills: pr , review-pr , pr-address-comments , adr-template , postmortem-template , github-work Mods: gh-guard , context-hud , secret-redactor , read-guard Each plugin has a page with what it does, when to use it, and its source: https://ferjani.dev/skills Install one: /plugin install guard --marketplace rezk2ll/skills Curious what guardrails other people run.
