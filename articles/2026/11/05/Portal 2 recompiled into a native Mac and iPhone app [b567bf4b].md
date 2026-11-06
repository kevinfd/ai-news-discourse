---
id: "b567bf4bc0bd1723"
title: "Portal 2 recompiled into a native Mac and iPhone app"
url: "https://reddit.com/r/ClaudeAI/comments/1xom0ii/portal_2_recompiled_into_a_native_mac_and_iphone"
link: "https://reddit.com/r/ClaudeAI/comments/1xom0ii/portal_2_recompiled_into_a_native_mac_and_iphone"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T15:46:59Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["kanapitsas"]
language: "en"
summary: "I wanted to play Portal 2 natively on Apple silicon, so we (that is, Opus 5.5 and I) built a tool that translates the Linux release’s machine code into C (about 125,000 functions) and then compiles it to native ARM64. It turns out it took only two days to get a playable room (Claude thought it would take many months). There’s no emulator, Wine or Rosetta involved. You need your own copy of…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches"]
content_source: "post"
word_count: 222
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xom0ii/portal_2_recompiled_into_a_native_mac_and_iphone/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Portal 2 recompiled into a native Mac and iPhone app

Reddit · kanapitsas · 2026-11-05

I wanted to play Portal 2 natively on Apple silicon, so we (that is, Opus 5.5 and I) built a tool that translates the Linux release’s machine code into C (about 125,000 functions) and then compiles it to native ARM64. It turns out it took only two days to get a playable room (Claude thought it would take many months). There’s no emulator, Wine or Rosetta involved. You need your own copy of Portal 2. The repo has no game files; the native app is generated on your machine. It’s playable on an iPhone 15 Pro Max with touch controls. You fire portals by tapping the back of the phone: https://youtu.be/YWX2BeMnlQI . You can also use a Bluetooth controller (tested with 8BitDo). Co-op works over LAN: a Mac hosts, and another Mac or an iPhone joins by IP address. We recently replaced OpenGL with a direct D3D9 → Metal path, built on mtld3d ( https://github.com/athei/mtld3d ). In one scene on an M3 Pro, it ran at 122 fps versus 81 with OpenGL. Numbers vary a lot by room. Claude Code wrote the code; I set the direction, tested on my devices and made the calls. I used Codex as a reviewer and for second opinions when Claude was stuck. Happy to answer questions about the project. Contributions on GitHub are welcome: https://github.com/kanapitsas/portal2-recomp
