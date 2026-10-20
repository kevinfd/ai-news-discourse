---
id: "ababfceaf90aed74"
title: "I used Claude to build MeshLive - offline voice/video calls + livestreams that hop phone-to-phone over Bluetooth"
url: "https://reddit.com/r/ClaudeAI/comments/1xaa59y/i_used_claude_to_build_meshlive_offline"
link: "https://reddit.com/r/ClaudeAI/comments/1xaa59y/i_used_claude_to_build_meshlive_offline"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T21:47:29Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["gautamgpt"]
language: "en"
summary: "A few weeks ago I started wondering whether you could do more than text over Bluetooth when the internet is down. Bitchat already showed phones can message each other offline. What about actual video calls and live streams that also hop across other phones? That’s MeshLive. Every phone that joins becomes a node. A live video or audio stream starts on one phone, gets received by nearby phones,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 358
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xaa59y/i_used_claude_to_build_meshlive_offline/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude to build MeshLive - offline voice/video calls + livestreams that hop phone-to-phone over Bluetooth

Reddit · gautamgpt · 2026-10-19

A few weeks ago I started wondering whether you could do more than text over Bluetooth when the internet is down. Bitchat already showed phones can message each other offline. What about actual video calls and live streams that also hop across other phones? That’s MeshLive. Every phone that joins becomes a node. A live video or audio stream starts on one phone, gets received by nearby phones, and those phones can rebroadcast it further. Same idea for calls. No internet, no servers, no accounts. In theory the range is limited only by how many phones are in the chain, not by any single Bluetooth radio. Getting even a rough version of that working was the interesting part. AI wrote a lot of the initial implementation under direction media pipeline, Bluetooth handling, UI, the early relay logic. It was useful for speed. The part that stopped being a prompt problem was the second phone, then the third, fourth and fifth one. Bluetooth behavior is extremely inconsistent across manufacturers, Android versions, chipsets, and codecs. A stream that looks fine on one pair of phones falls apart on another. Video frames back up behind a slow hop, audio latency grows, connections drop and recover in weird ways, and relays introduce their own timing and admission problems. I ended up buying another Android phone just to have more combinations to test against, and a lot of the real work after the first version was sitting with devices and chasing those failures. Current beta (0.3.0) has: Voice and video calls Live video streams and audio-only streams (lighter, longer range, can keep playing with screen off) Multi-hop relaying for streams (call relay still experimental and off by default) Rotating discovery IDs, lock-screen call handling, cleaner UI, basic Android ↔ iPhone discovery Fully offline, open source It is still beta. Some device pairs are slow or flaky, relayed calls are not production-ready, and there has been no independent security audit. I open-sourced it because the only realistic way this gets better coverage is more people testing on hardware I don’t own. Android source + APK: https://github.com/MeshLive/meshlive-android Early iOS: https://github.com/MeshLive/meshlive-ios Feedback, Testers, Contributors are welcome.
