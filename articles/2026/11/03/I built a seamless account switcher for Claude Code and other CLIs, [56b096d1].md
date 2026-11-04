---
id: "56b096d1f8f37637"
title: "I built a seamless account switcher for Claude Code and other CLIs,"
url: "https://reddit.com/r/ClaudeAI/comments/1xmteq5/i_built_a_seamless_account_switcher_for_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xmteq5/i_built_a_seamless_account_switcher_for_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T13:49:34Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["YasufoKiddo"]
language: "en"
summary: "acswi saves the sign-in of every account you use in an app, then switches the app between them. Switching Claude Code from personal to work is acswi claude work , or one click in a small window. No logging out, no browser round trip. It works the same for Codex, GitHub CLI, Azure CLI, Cursor, Discord and GitHub Desktop, and you can add other apps with a short TOML file. Why: I have a personal…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft", "Cursor"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 302
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmteq5/i_built_a_seamless_account_switcher_for_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a seamless account switcher for Claude Code and other CLIs,

Reddit · YasufoKiddo · 2026-11-03

acswi saves the sign-in of every account you use in an app, then switches the app between them. Switching Claude Code from personal to work is acswi claude work , or one click in a small window. No logging out, no browser round trip. It works the same for Codex, GitHub CLI, Azure CLI, Cursor, Discord and GitHub Desktop, and you can add other apps with a short TOML file. Why: I have a personal and a work account on Claude Code, Codex and GitHub, and /logout → /login several times a day got old. How Claude helped: Claude Code wrote most of it: a Rust engine, a CLI and a Tauri desktop app, about 4.7k lines in a day. My part was the decisions and the testing: Rust over Python, because I wanted quality over ease of build. Apps described in small data files instead of code for each app. Make the CLI friendly for people, not just for agents. Don't try to be more secure than the apps themselves are with their tokens. Claude also drove the real desktop window over the WebView debug port to test clicks, and recorded this GIF with sample accounts. Things I had to catch: An early "add account" flow could save an account it already had under a new name. The first CLI was clearly made for agents. It now opens a numbered menu when a person runs it. For agents: every command has --json output and stable exit codes, so an agent can switch accounts by name. acswi never prints a token. The docs show how to deny an agent access to the vault folder and to gh auth token . Status: first version, Windows only(working on linux and MacOS). Feedback welcome from anyone who juggles several Claude accounts. Free and MIT: https://github.com/OpenRootdev/acswi
