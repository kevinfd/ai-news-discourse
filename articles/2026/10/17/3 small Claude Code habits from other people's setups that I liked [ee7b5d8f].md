---
id: "ee7b5d8f9b567bd3"
title: "3 small Claude Code habits from other people's setups that I liked"
url: "https://reddit.com/r/ClaudeAI/comments/1x8lae3/3_small_claude_code_habits_from_other_peoples"
link: "https://reddit.com/r/ClaudeAI/comments/1x8lae3/3_small_claude_code_habits_from_other_peoples"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T21:08:09Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["abe17124"]
language: "en"
summary: "I've been collecting Claude Code setups people have written up about their real day-to-day use (blogs, X, GitHub), and I tried a bunch of them. These 4 I have been finding useful recently. 1. Install 2 or 3 subagents. VoltAgent's awesome-claude-code-subagents repo has 160+ definitions. What worked was asking Claude which 3 would help this specific repo, reading each file before installing…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 221
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8lae3/3_small_claude_code_habits_from_other_peoples/"
score: null
comments: null
community: "r/ClaudeAI"
---

# 3 small Claude Code habits from other people's setups that I liked

Reddit · abe17124 · 2026-10-17

I've been collecting Claude Code setups people have written up about their real day-to-day use (blogs, X, GitHub), and I tried a bunch of them. These 4 I have been finding useful recently. 1. Install 2 or 3 subagents. VoltAgent's awesome-claude-code-subagents repo has 160+ definitions. What worked was asking Claude which 3 would help this specific repo, reading each file before installing (they're prompts that can request tools), and trimming the tool access. 2. Get a desktop notification when Claude is waiting on you - Prashanth Vaidya had Claude Code set up its own Notification hook. The prompt is basically: "Set up a Notification hook in my user settings that shows 'Claude needs input: [project folder]' whenever you're waiting on me. Show me the settings JSON before writing it." Was super useful so I could stop going back to VSCode to check 3. Claude builds, something else reviews - Santiago uses Claude Code to build and Codex as a read-only reviewer that hunts bugs and pushes back on architecture, and also added a fleet rule: the model that wrote a piece of work never reviews it. Originals: Prashanth Vaidya: https://x.com/pvbuilds/status/2009209023833493972 santiagoo24_: https://x.com/santiagoo24_/status/2083004127144001812 VoltAgent: https://github.com/VoltAgent/awesome-claude-code-subagents Disclosure : I put all 51 at Agent Cookbooks each linked to its original with a copy-paste prompt. It's free because fuck people who gatekeep with paywalls!!
