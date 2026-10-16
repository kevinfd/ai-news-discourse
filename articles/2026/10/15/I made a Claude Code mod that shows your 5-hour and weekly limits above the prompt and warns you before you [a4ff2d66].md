---
id: "a4ff2d6641169452"
title: "I made a Claude Code mod that shows your 5-hour and weekly limits above the prompt and warns you before you hit them"
url: "https://reddit.com/r/ClaudeAI/comments/1x6al0c/i_made_a_claude_code_mod_that_shows_your_5hour"
link: "https://reddit.com/r/ClaudeAI/comments/1x6al0c/i_made_a_claude_code_mod_that_shows_your_5hour"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T02:55:55Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Equivalent_Scary"]
language: "en"
summary: "I kept getting blocked mid-week without warning, so I built two small Claude Code mods. They hook into Claude Code's plugin API, so there's no wrapper and no extra process. limits : an always-on band above the prompt 5-hour and weekly usage: a bar, the percent used and a countdown to the reset The percent turns red when your current pace would use up the limit before it resets. You find out on…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 224
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6al0c/i_made_a_claude_code_mod_that_shows_your_5hour/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a Claude Code mod that shows your 5-hour and weekly limits above the prompt and warns you before you hit them

Reddit · Equivalent_Scary · 2026-10-15

I kept getting blocked mid-week without warning, so I built two small Claude Code mods. They hook into Claude Code's plugin API, so there's no wrapper and no extra process. limits : an always-on band above the prompt 5-hour and weekly usage: a bar, the percent used and a countdown to the reset The percent turns red when your current pace would use up the limit before it resets. You find out on Tuesday, not when you're blocked on Thursday. Context window fill, plus toasts at 75/90/100% idle-compact : cheaper returns to big chats The prompt cache expires after an hour, so coming back to a 300k-token chat reloads all of it at full price After 40 min idle, it runs /compact while the cache is still warm, so the chat you return to is small It never compacts a chat you reopened cold, since that would cost full price How it works (if you want to build your own): limits renders an AbovePrompt band from the rate-limit readings Claude Code already receives. It shares one reading across all open sessions through the plugin store, so 10 open chats still make only one 1-token Haiku request every 2 min to stay fresh. Install (in terminal claude ): /plugin install limits --marketplace Ryan-LT/claude-mods /plugin install idle-compact --marketplace Ryan-LT/claude-mods Repo (MIT): https://github.com/Ryan-LT/claude-mods Feedback and ideas welcome!
