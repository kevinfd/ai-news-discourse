---
id: "40b025ced3ef3b08"
title: "Half-Life 2 running natively on Mac and iPhone (static recompilation)"
url: "https://reddit.com/r/ClaudeAI/comments/1xsije8/halflife_2_running_natively_on_mac_and_iphone"
link: "https://reddit.com/r/ClaudeAI/comments/1xsije8/halflife_2_running_natively_on_mac_and_iphone"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T09:27:27Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["kanapitsas"]
language: "en"
summary: "After Portal 2 it’s time for Half-Life 2 to run on Apple Silicon! Including Episode One, Episode Two and Lost Coast. (There was already a native port some years ago, but it relied on leaked code.) Claude Code (mainly Opus 5.5) wrote the code, I tested on my Mac and iPhone and made the decisions. The recompiler we built for Portal 2 translates the x86 code of the Linux version into C, then…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches"]
content_source: "post"
word_count: 249
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsije8/halflife_2_running_natively_on_mac_and_iphone/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Half-Life 2 running natively on Mac and iPhone (static recompilation)

Reddit · kanapitsas · 2026-11-10

After Portal 2 it’s time for Half-Life 2 to run on Apple Silicon! Including Episode One, Episode Two and Lost Coast. (There was already a native port some years ago, but it relied on leaked code.) Claude Code (mainly Opus 5.5) wrote the code, I tested on my Mac and iPhone and made the decisions. The recompiler we built for Portal 2 translates the x86 code of the Linux version into C, then compiles it for ARM64. It got us most of the way: from the first Half-Life 2 commit to the game running on my iPhone took less than two days. Day 1: Claude added per-game profiles, the SSSE3 instructions and missing Linux imports of HL2, and bridged its newer Steam SDK. By the evening the game was playable, but the textures had no filtering: macOS’s OpenGL has no sampler objects. Claude fixed it, then made HL2 run on Metal with the Direct3D 9 bridge from Portal 2. Day 2: performance, Metal by default, and the iOS build with touch controls (they might still need some work). There’s now an installer app. It finds your Steam games and builds them on your Mac (about 10-20 minutes per game). You need the Xcode command line tools and the Linux binaries (downloaded with the Steam console). You need to own the games on Steam. No game files are included. Please don’t share built apps. This project is unofficial and not affiliated with Valve. Repo: https://github.com/kanapitsas/source-recomp Installer: https://github.com/kanapitsas/source-recomp/releases/tag/v0.3.1 Feedback is welcome!
