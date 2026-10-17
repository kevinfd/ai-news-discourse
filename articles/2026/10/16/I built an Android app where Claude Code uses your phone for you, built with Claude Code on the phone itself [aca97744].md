---
id: "aca97744bebf8ebe"
title: "I built an Android app where Claude Code uses your phone for you, built with Claude Code on the phone itself"
url: "https://reddit.com/r/ClaudeAI/comments/1x7hzn8/i_built_an_android_app_where_claude_code_uses"
link: "https://reddit.com/r/ClaudeAI/comments/1x7hzn8/i_built_an_android_app_where_claude_code_uses"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T14:39:14Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["3amae404"]
language: "en"
summary: "Buddy is a free, open-source Android app: a chat bubble that floats over your apps. You say \"reply to Sam that I'm late\" or \"start navigation to work\", and Claude Code reads the screen and taps through your apps for you. How it works: - Claude Code runs inside the app, in a small Alpine Linux (no root, no PC, no adb), on your own Claude plan. Codex and OpenCode work too. - It gets phone tools…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research", "safety & ethics", "agents & coding"]
content_source: "post"
word_count: 203
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7hzn8/i_built_an_android_app_where_claude_code_uses/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an Android app where Claude Code uses your phone for you, built with Claude Code on the phone itself

Reddit · 3amae404 · 2026-10-16

Buddy is a free, open-source Android app: a chat bubble that floats over your apps. You say "reply to Sam that I'm late" or "start navigation to work", and Claude Code reads the screen and taps through your apps for you. How it works: - Claude Code runs inside the app, in a small Alpine Linux (no root, no PC, no adb), on your own Claude plan. Codex and OpenCode work too. - It gets phone tools over MCP: read the screen, tap, type, scroll, open apps. - Tap the bubble and just talk: voice waves under the bubble, and it sends when you pause. Safety lives in the app, not the prompt. Sending, paying and deleting in messaging, shopping or banking apps stop on a card until you say OK. Apps you trust run hands-free. A model once picked "Buy now" instead of "Add to cart", and that check is why nothing got ordered. How I build it: Claude Code in Termux on the same phone writes the code, builds the APK, installs it and tests it by driving the phone with Buddy's own tools. Most bugs people report get fixed that way within hours. Free and open source (Apache 2.0): https://github.com/ghorbelhamdi/buddy-android
