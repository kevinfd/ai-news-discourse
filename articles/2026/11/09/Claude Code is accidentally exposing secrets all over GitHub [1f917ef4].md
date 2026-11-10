---
id: "1f917ef42e116f1b"
title: "Claude Code is accidentally exposing secrets all over GitHub"
url: "https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github"
link: "https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T17:24:26Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Kyle Orland"]
language: "en"
summary: "Claude Code is leaking sensitive information on public GitHub instances thanks to a partial oversight in the way its settings files are handled. That's the finding of AI security researchers at Apiiro, who discovered thousands of secrets , including database passwords, API tokens, and root logins, amid Claude Code settings files embedded in GitHub repositories. \n The leak stems from the way…"
tags: ["AI", "Security", "AI agents", "Anthropic", "Claude Code", "GitHub", "setting"]
orgs: ["Anthropic"]
topics: []
content_source: "fulltext"
word_count: 311
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/11/claude-github-leaks-1152x648.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Claude Code is accidentally exposing secrets all over GitHub

Ars Technica · Kyle Orland · 2026-11-09

Claude Code is leaking sensitive information on public GitHub instances thanks to a partial oversight in the way its settings files are handled. That’s the finding of AI security researchers at Apiiro, who discovered thousands of secrets, including database passwords, API tokens, and root logins, amid Claude Code settings files embedded in GitHub repositories.
The leak stems from the way Claude Code handles user approval for automated shell commands. When a user chooses the “Yes, and don’t ask again” option to approve running a command, that choice gets stored as part of a rule in the local “.claude/settings.local.json” file on the user’s computer. That rule is sometimes coded as a pattern, but the command itself is often written to that settings file as is, including any sensitive information that may be embedded within it.
This isn’t really a significant security issue if the settings file stays on the user’s local machine (assuming that machine doesn’t become compromised itself, of course). And Anthropic notes in its Claude Code documentation that this particular settings file gets added to the developer’s global .gitignore list, which usually prevents it from being shared publicly.
But that .gitignore setting isn’t reflected at the repo level, meaning the sensitive file can be uploaded accidentally if a repo is cloned to another machine or a folder becomes a repo later, for instance. In many cases, Claude Code itself will commit changes to the settings file without the user’s input, Apiiro writes.
Apiiro’s researchers found over 100,000 cases where Claude Code’s local settings file had been uploaded to a public GitHub repository. Of these, only about 1,100 from 63 different organizations contained secrets such as public API tokens, database passwords, or private keys. Even after these files are discovered and removed from a repository, the secrets can persist in forks of the original project if a GitHub user isn’t careful.
