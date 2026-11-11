---
id: "fd8d4164a51a7de7"
title: "I reverse-engineered Apple Photos and rebuilt it for my own server – iCloud Photos without iCloud with Claude"
url: "https://reddit.com/r/ClaudeAI/comments/1xsvh4x/i_reverseengineered_apple_photos_and_rebuilt_it"
link: "https://reddit.com/r/ClaudeAI/comments/1xsvh4x/i_reverseengineered_apple_photos_and_rebuilt_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T19:01:04Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["SilentMode46"]
language: "en"
summary: "I got tired of paying Apple every month to keep my own photos, so I moved ~85,000 photos and videos to my own server (Immich) and switched iCloud Photos off. I built HomeRoll, a native iOS 26 app (SwiftUI + UIKit) that looks and behaves like Apple Photos but stores everything on your own Immich server. I built it with Claude Code. I’m not an iOS developer by trade, so nearly all of the code was…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 507
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsvh4x/i_reverseengineered_apple_photos_and_rebuilt_it/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I reverse-engineered Apple Photos and rebuilt it for my own server – iCloud Photos without iCloud with Claude

Reddit · SilentMode46 · 2026-11-10

I got tired of paying Apple every month to keep my own photos, so I moved ~85,000 photos and videos to my own server (Immich) and switched iCloud Photos off. I built HomeRoll, a native iOS 26 app (SwiftUI + UIKit) that looks and behaves like Apple Photos but stores everything on your own Immich server. I built it with Claude Code. I’m not an iOS developer by trade, so nearly all of the code was written by Claude, with me deciding what to build, testing on my iPhone and saying what felt wrong. Why: I was tired of paying for iCloud storage, so I moved ~85,000 photos and videos to my own server and switched iCloud Photos off. Every Immich app I tried felt nothing like the Photos app I was used to. How Claude Code was used Reverse engineering: Claude took Apple’s Photos frameworks from iOS 26.3 apart with a reverse-engineering MCP server and listed all 226 actions the Photos app can perform (copy edits, print, hide, set key photo, drag to album, Spotlight ...). To keep it clean-room, one agent only wrote plain behavior descriptions (“what happens when you do X”), and the app was written from those descriptions, not from Apple’s code. Implementation: Claude wrote the app from that list. 147 of the 226 actions work now. 62 are iCloud/Apple-service only, 16 are Apple-internal, 1 isn’t possible on iOS. Testing: Claude wrote the automated UI tests and ran them in the iOS Simulator itself, looking at screenshots to compare against the real Photos app. 140 of the 147 actions are covered. Maintenance: Claude reads the GitHub issues, reproduces bugs in the simulator, proposes a fix and drafts the reply. Nothing is released until I’ve said go. What worked well: giving Claude a concrete checklist (the 226 actions) instead of “make it like Photos”, and letting it verify its own work in the simulator. What didn’t: performance with a library this size. The first versions crashed or stuttered with 85,000 items, and that took many rounds of measuring on the real device. What the app does Library with pinch-to-zoom grid, Years / Months / All Viewer with preview strip, video scrubbing, Live Photos, HDR originals Editor: light, color, filters, crop, copy and paste edits Memories, people, places Search for receipts, documents, handwriting, QR codes, screenshots Album folders, drag photos onto albums, Spotlight Backup of new photos and videos in the background while charging Free Up Space: deletes only what’s verified to be on your server (checksum + server check) Widgets and a share extension Free to try The app is free and open source (MIT), no paid tier. You need your own Immich server (tested with v3.3.5). Download the IPA from the GitHub releases page and install it with SideStore, AltStore or your own signing tool, then log in with your server URL. https://github.com/silentprovider423/HomeRoll There is also a Mac version, built the same way: https://github.com/silentprovider423/HomeRoll-Desk Not affiliated with Apple or Immich/FUTO. Happy to answer questions about the Claude Code workflow or the reverse engineering.
