---
id: "fcae1e1c87694f95"
title: "I made Claude Code and Codex message each other by name, no tmux"
url: "https://reddit.com/r/ClaudeAI/comments/1xpyq1r/i_made_claude_code_and_codex_message_each_other"
link: "https://reddit.com/r/ClaudeAI/comments/1xpyq1r/i_made_claude_code_and_codex_message_each_other"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T05:40:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Seunghyeon413"]
language: "en"
summary: "tmux and herdr send a message by putting text into the other agent's terminal. With tmux, I had Enter land on an approval prompt, and messages got stuck onto a sentence I was typing. peer skips the terminal and sends straight to Claude Code's and Codex's own input paths. peer say review \"please check src/auth.ts\" -> delivered It never mixes with what you're typing. Keep the terminal you already…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 157
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpyq1r/i_made_claude_code_and_codex_message_each_other/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made Claude Code and Codex message each other by name, no tmux

Reddit · Seunghyeon413 · 2026-11-07

tmux and herdr send a message by putting text into the other agent's terminal. With tmux, I had Enter land on an approval prompt, and messages got stuck onto a sentence I was typing. peer skips the terminal and sends straight to Claude Code's and Codex's own input paths. peer say review "please check src/auth.ts" -> delivered It never mixes with what you're typing. Keep the terminal you already use. No need to start agents inside tmux or herdr. (Codex only: start it with peer run codex .) You know right away if it was delivered, and if the other agent's turn dies on a rate limit, you're told why. If you also want screen management, herdr is better. peer only does messaging. Free and open source. Built with Claude Code: it wrote most of the code, and I steered and tested it. https://github.com/oesoll/peer Edit: rewrote this to say what actually changes compared to tmux and herdr.
