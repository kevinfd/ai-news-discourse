---
id: "b62a7ddc21b813aa"
title: "I open-sourced YANGPA, a serverless P2P messenger over Tor. All of the code was written with Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xr601i/i_opensourced_yangpa_a_serverless_p2p_messenger"
link: "https://reddit.com/r/ClaudeAI/comments/1xr601i/i_opensourced_yangpa_a_serverless_p2p_messenger"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T18:56:37Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["SayYoung530"]
language: "en"
summary: "YANGPA is a serverless P2P messenger built on Tor. Data between users is end-to-end encrypted with post-quantum hybrid cryptography. Most of it is Rust, with a Tauri/React app. Ephemeral channels keep messages and keys only in RAM, never on disk , in logs or in cache. and, That's why YANGPA's icon is a flame.🔥 (Rust's type system enforces that: ephemeral data uses types the storage code can't…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 124
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xr601i/i_opensourced_yangpa_a_serverless_p2p_messenger/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I open-sourced YANGPA, a serverless P2P messenger over Tor. All of the code was written with Claude Code

Reddit · SayYoung530 · 2026-11-08

YANGPA is a serverless P2P messenger built on Tor. Data between users is end-to-end encrypted with post-quantum hybrid cryptography. Most of it is Rust, with a Tauri/React app. Ephemeral channels keep messages and keys only in RAM, never on disk , in logs or in cache. and, That's why YANGPA's icon is a flame.🔥 (Rust's type system enforces that: ephemeral data uses types the storage code can't accept.) How Claude helped: I wrote the spec and tested on real devices (two Windows PCs and a Galaxy phone). Claude Code wrote all of the code, tests, CI and docs in about 3 weeks (~265k lines), including the post-quantum migration and a real-network Tor leak test. Free to try on Windows, macOS, Linux and Android: https://github.com/dhtpdud/YANGPA
