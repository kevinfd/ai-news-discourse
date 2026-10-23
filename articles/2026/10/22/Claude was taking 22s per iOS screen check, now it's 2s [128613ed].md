---
id: "128613ed62949ae3"
title: "Claude was taking 22s per iOS screen check, now it's 2s"
url: "https://reddit.com/r/ClaudeAI/comments/1xcsqmt/claude_was_taking_22s_per_ios_screen_check_now"
link: "https://reddit.com/r/ClaudeAI/comments/1xcsqmt/claude_was_taking_22s_per_ios_screen_check_now"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T19:46:57Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Low-Future-9387"]
language: "en"
summary: "If you build iOS apps with Claude, most of the time goes to it waiting on the Simulator to build, install, launch and screenshot, and then it burns tokens reading the screenshot. I started using simless, which runs your real SwiftUI app natively on the Mac with no simulator. Claude gets each screen back as a short text tree (~150 tokens) in about 2 s after an edit. It can also run your unit…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 125
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xcsqmt/claude_was_taking_22s_per_ios_screen_check_now/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude was taking 22s per iOS screen check, now it's 2s

Reddit · Low-Future-9387 · 2026-10-22

If you build iOS apps with Claude, most of the time goes to it waiting on the Simulator to build, install, launch and screenshot, and then it burns tokens reading the screenshot. I started using simless, which runs your real SwiftUI app natively on the Mac with no simulator. Claude gets each screen back as a short text tree (~150 tokens) in about 2 s after an edit. It can also run your unit tests and UI tests the same way. For me that meant: 10x faster checks on a 280-file production app several agents working on one Mac at once, without it grinding to a halt Claude catching small tap targets and missing accessibility labels on its own, because the tree flags them https://github.com/abacusai/simless
