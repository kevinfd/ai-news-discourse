---
id: "abd69b38a2143153"
title: "Claude Code ported my React Native app to Swift. A benchmark found the bugs it missed"
url: "https://reddit.com/r/ClaudeAI/comments/1xol3l9/claude_code_ported_my_react_native_app_to_swift_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xol3l9/claude_code_ported_my_react_native_app_to_swift_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T15:11:04Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Xatpy"]
language: "en"
summary: "I gave Claude Code a whole port, React Native to native Swift, as one long task with \"done\" criteria it could check itself: it builds, the tests pass, every string exists in all 7 languages, and every screen is screenshotted next to the React Native one. Translations were generated from the React Native source instead of retyped, and the \"random photo\" logic was tested against fixtures produced…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 227
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xol3l9/claude_code_ported_my_react_native_app_to_swift_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code ported my React Native app to Swift. A benchmark found the bugs it missed

Reddit · Xatpy · 2026-11-05

I gave Claude Code a whole port, React Native to native Swift, as one long task with "done" criteria it could check itself: it builds, the tests pass, every string exists in all 7 languages, and every screen is screenshotted next to the React Native one. Translations were generated from the React Native source instead of retyped, and the "random photo" logic was tested against fixtures produced by running the original TypeScript. The port itself was the fast part. The slow part was everything after: using it on my phone, a few rounds of code review, and fixing what came up. Things it got wrong: A benchmark-only bundle ID ended up in the App Store project. Twice. A freeze on first launch that only happened on a real iPhone. Two performance bugs that only show up with a big library: a first load that never finished during an iCloud sync, and a photo viewer that reached 404 MB. The last two were found by benchmarking both apps with the same XCUITest suite against 21,000 generated photos. The code was correct, it just didn't scale, and that's the kind of thing an agent won't find without a test that makes it visible. The result: 7x less CPU to load days, the first photo in 0.58 s instead of 2.17 s, and half the memory at launch. Write-up: https://blog.jaimechapinal.com/posts/i-rewrote-my-react-native-app-in-swift/
