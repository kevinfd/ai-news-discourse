---
id: "7e550c5cd0d8315a"
title: "Used Claude Code to patch MLB The Show 16 on RPCS3 so I could play online with a friend again"
url: "https://reddit.com/r/ClaudeAI/comments/1xgjfvg/used_claude_code_to_patch_mlb_the_show_16_on"
link: "https://reddit.com/r/ClaudeAI/comments/1xgjfvg/used_claude_code_to_patch_mlb_the_show_16_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T04:48:20Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["tony_b_the_masseuse"]
language: "en"
summary: "Spent the past weekend patching MLB The Show 16 on RPCS3 with Claude Code so I could play online with a friend. This game was historically unplayable on RPCS3 due to graphics glitches, and it’s now not only playable, but also playable online. PC has been ignored by MLB The Show forever. The series has never had a native PC release, and the last officially licensed MLB game you could actually…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 468
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgjfvg/used_claude_code_to_patch_mlb_the_show_16_on/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Used Claude Code to patch MLB The Show 16 on RPCS3 so I could play online with a friend again

Reddit · tony_b_the_masseuse · 2026-10-27

Spent the past weekend patching MLB The Show 16 on RPCS3 with Claude Code so I could play online with a friend. This game was historically unplayable on RPCS3 due to graphics glitches, and it’s now not only playable, but also playable online. PC has been ignored by MLB The Show forever. The series has never had a native PC release, and the last officially licensed MLB game you could actually play on the field on PC was MLB 2K12, in 2012. RPCS3 runs on Windows, Linux and macOS, so this is also a way to play a licensed MLB game on a computer at all. Claude Workflow It cost ~$60 in API credits using Opus 5.5 and ~8 hours to go from me not knowing how to do this at all to getting it working barebones on my local network. Getting my launcher working and everything cleaned up and bug fixed to my liking took maybe another 8 hours and $150 of Opus (~200k input and ~1.5m output tokens total). I’m very impressed! I used Ghidra MCP (with Ps3GhidraScripts) and RenderDoc MCP to automate a lot of the debugging process. The result A collection of graphics and server patches for MLB 16 played via the RPCS3 emulator. You can play 1v1 games and Home Run Derby over the internet or on a local network with another computer. I’ve tested it on my home network across a PC and a Mac, and online with my friend PC vs. PC. We were able to play a full 9 innings online with minimal issues. Download, setup guide, source code and technical write-ups: https://github.com/MatRanc/mlb16-revival-server How it works (briefly) Sony shut down the game’s servers in 2020, so the launcher runs a small replacement on the host’s computer, and RPCS3 redirects the game’s old Sony addresses to it. Once a challenge is accepted, RPCN (RPCS3’s free PSN replacement) tells each game where the other is, and they connect directly, peer to peer. Five patches get past what blocks online play, like the “ONLINE DISABLED” popup and a challenge check that used to depend on Sony’s servers. Is this legal? Yep. My repo hosts no game code, no game files, no Sony/SDS data. The patches don’t even touch the ISO you provide yourself, they just change how RPCS3 interprets the file in its own memory. Could this work for other PS3 games? Probably. For PS3 games, the online code is usually still in the game, they trust whatever certificates are on the console (which RPCS3 lets you change), and their protocols are simple. There’s a “Reviving another game” section in the technical docs, and an AGENTSmd in the repo. Point your favourite AI agent at the repo and let it cook. It’s Apache 2.0, so feel free to fork it and go crazy.
