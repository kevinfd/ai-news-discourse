---
id: "60f729bfbf302949"
title: "I vibecoded this MCP that lets Claude Code build Wii Sports-style games you play with your body through your webcam"
url: "https://reddit.com/r/ClaudeAI/comments/1x8vqa3/i_vibecoded_this_mcp_that_lets_claude_code_build"
link: "https://reddit.com/r/ClaudeAI/comments/1x8vqa3/i_vibecoded_this_mcp_that_lets_claude_code_build"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T06:08:01Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["singing_coach_ai"]
language: "en"
summary: "https://preview.redd.it/ssf7j08o06wh1.png?width=2277&format=png&auto=webp&s=a60ae4a95c83501c67aee3a43b918b9f5971fa15 I wanted to relive the Wii Sports experience, but in a browser, without needing a console or controllers. So I built a free MCP that lets you oneshot hosted multiplayer games controlled by your body: using your hands, arms, face, and microphone. It's really fun, and gets your body…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 291
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8vqa3/i_vibecoded_this_mcp_that_lets_claude_code_build/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I vibecoded this MCP that lets Claude Code build Wii Sports-style games you play with your body through your webcam

Reddit · singing_coach_ai · 2026-10-18

https://preview.redd.it/ssf7j08o06wh1.png?width=2277&format=png&auto=webp&s=a60ae4a95c83501c67aee3a43b918b9f5971fa15 I wanted to relive the Wii Sports experience, but in a browser, without needing a console or controllers. So I built a free MCP that lets you oneshot hosted multiplayer games controlled by your body: using your hands, arms, face, and microphone. It's really fun, and gets your body moving! You can give this MCP to Claude Code and ask it to build you a multiplayer game that you play using your camera: MCP: https://oneshotgems.ai/developers/mcp Try an example game: https://oneshotgems.ai/app/game/3b5fhco5cf92?s=7sxgmnit How it works Everything runs locally: Hand, body, and face tracking models run on your device, along with voice input. Claude Code builds the game: The MCP gives it an SDK with assets, on-device tracking models, multiplayer functionality, lobbies, and more. It also provides a local preview with camera access so Claude Code can test the games it creates. Play with friends: Share a link to invite friends into a game. Everyone in the lobby can see each other's camera feeds, kind of like a video call. How I built it I used Opus 5.5 with Claude Code to build the platform, including all the underlying infrastructure for hosting games, multiplayer sessions, and lobbies. Then I iterated in a single conversation until we got the body-tracking controls working properly on-device. The first version worked on my MacBook, but performance was a problem, especially on mobile. I did a performance optimization pass with Opus, and got local model inference running at around 50–100+ FPS on my Mac. The goal is to make it as easy as possible to go from an idea to a playable, AI-generated multiplayer game, no game engine setup, no controller hardware, just your browser and camera. I'd love to hear what games you'd try building with this!
