---
id: "68a655e47c279f98"
title: "I made my dictation key press the Claude app's own mic button (free, open source, built with Claude Code)"
url: "https://reddit.com/r/ClaudeAI/comments/1xpar4h/i_made_my_dictation_key_press_the_claude_apps_own"
link: "https://reddit.com/r/ClaudeAI/comments/1xpar4h/i_made_my_dictation_key_press_the_claude_apps_own"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T11:42:57Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["breakzoras"]
language: "en"
summary: "I dictate almost everything I send to Claude, so over the last months I built FU Flow, a fully free dictation app for Windows and Ubuntu that runs Whisper locally on your own PC. Version 0.9.19 went out this morning with the bit I wanted most: when the Claude desktop app is in front, my dictation key presses Claude's own microphone button. Claude listens and writes into its own box, and FU Flow…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["products & launches"]
content_source: "post"
word_count: 243
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpar4h/i_made_my_dictation_key_press_the_claude_apps_own/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made my dictation key press the Claude app's own mic button (free, open source, built with Claude Code)

Reddit · breakzoras · 2026-11-06

I dictate almost everything I send to Claude, so over the last months I built FU Flow, a fully free dictation app for Windows and Ubuntu that runs Whisper locally on your own PC. Version 0.9.19 went out this morning with the bit I wanted most: when the Claude desktop app is in front, my dictation key presses Claude's own microphone button. Claude listens and writes into its own box, and FU Flow only shows a small bar while you talk. Same with the Codex app. Anywhere else it types with its local Whisper like before. It's a switch in Settings, off by default, Windows only for now. The 10 second clip shows how it looks. How Claude built it: Claude finds the mic button through Windows UI Automation, the same layer screen readers use, and presses it by its name. Nothing gets clicked by screen position and FU Flow records nothing while Claude is the one listening. Claude also wrote the Rust side, the What's new window, the tests (269 Rust tests pass on this release) and the scripts that build and sign the installers. Before every release it replays my whole dictation history through the new text cleanup and reads every line that changes. That's how it caught the Greek word for "why" turning my "because" sentences into questions, which made it into this release too. Free download and source (MIT): https://fuckyouflow.app https://github.com/Breakzoras/fuck-you-flow Independent project, no ties to Anthropic or OpenAI.
