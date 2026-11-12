---
id: "bc358fc5e9b4c073"
title: "Heads up: Claude Code's \"don't ask again\" has been leaking secrets into public repos"
url: "https://reddit.com/r/ClaudeAI/comments/1xtx4ik/heads_up_claude_codes_dont_ask_again_has_been"
link: "https://reddit.com/r/ClaudeAI/comments/1xtx4ik/heads_up_claude_codes_dont_ask_again_has_been"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T23:29:02Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Predictor_2718"]
language: "en"
summary: "GitLab wrote about this a few days ago, and the number is worth repeating. Apiiro found 104,185 copies of `.claude/settings.local.json` in public repositories, and 1,122 of them had a secret in them. Here is how a secret ends up in that file. When you approve a shell command with \"Yes, and don't ask again\", Claude Code stores the exact command in that file under `permissions.allow`, so it stops…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Microsoft", "Cursor"]
topics: ["agents & coding"]
content_source: "post"
word_count: 335
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtx4ik/heads_up_claude_codes_dont_ask_again_has_been/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Heads up: Claude Code's "don't ask again" has been leaking secrets into public repos

Reddit · Predictor_2718 · 2026-11-11

GitLab wrote about this a few days ago, and the number is worth repeating. Apiiro found 104,185 copies of `.claude/settings.local.json` in public repositories, and 1,122 of them had a secret in them. Here is how a secret ends up in that file. When you approve a shell command with "Yes, and don't ask again", Claude Code stores the exact command in that file under `permissions.allow`, so it stops prompting you for it. If you had typed a token or a password into the command, it is now saved there as plain text. The reason it leaks is a bit subtle. Claude Code keeps the file out of git by adding it to your personal global git excludes, and those only exist on your own machine. The project `.gitignore` does not list it by default. So the moment the repo is shared or someone clones it, the file can be committed and pushed by someone whose machine never had that exclude. Two things if you find one in your own repos. Rotate the secret, do not only delete the line. Once it was pushed, the value is in the git history, so removing the entry changes nothing until you rotate the key at the provider. It is also not specific to Claude Code. Any agent that remembers a "don't ask again" decision keeps a file like this, so Cursor, Copilot, Gemini and others have the same pattern. Quick check by hand: search your repos for `.claude/settings.local.json`, confirm it is in the project `.gitignore` and not only in your global excludes, and read through the permission entries for anything that looks like a token. I maintain a small open-source tool called cfgaudit that checks this across the different agents: a hardcoded secret inside a permission entry, and the file not being gitignored. It runs as a pre-commit hook, as a CI step, or as a one-off scan. Write-up with the details: https://cfgaudit.github.io/blog/claude-code-dont-ask-again-secret-leak/ repo: https://github.com/cfgaudit/cfgaudit Disclosure: I maintain cfgaudit. Have you checked your own repos for this file?
