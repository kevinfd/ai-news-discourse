---
id: "797fcd855a43c389"
title: "I built a free, private meeting recorder for Mac entirely with Claude Code. You can chat with your meeting notes in Claude Desktop via MCP"
url: "https://reddit.com/r/ClaudeAI/comments/1x9zao5/i_built_a_free_private_meeting_recorder_for_mac"
link: "https://reddit.com/r/ClaudeAI/comments/1x9zao5/i_built_a_free_private_meeting_recorder_for_mac"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T15:03:31Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["davernow"]
language: "en"
summary: "I'm an ex-Apple engineer who got sick of non-private, non-native meeting recording apps, so I built Biscotti : a private and free meeting recorder for macOS. Free, no account, no subscription, no upsell. Source is on GitHub: https://github.com/scosman/Biscotti The whole app was built with Claude Code. It also has a built-in MCP server, so you can chat with your meeting notes and transcripts in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches", "agents & coding", "search & media", "models & research"]
content_source: "post"
word_count: 515
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9zao5/i_built_a_free_private_meeting_recorder_for_mac/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free, private meeting recorder for Mac entirely with Claude Code. You can chat with your meeting notes in Claude Desktop via MCP

Reddit · davernow · 2026-10-19

I'm an ex-Apple engineer who got sick of non-private, non-native meeting recording apps, so I built Biscotti : a private and free meeting recorder for macOS. Free, no account, no subscription, no upsell. Source is on GitHub: https://github.com/scosman/Biscotti The whole app was built with Claude Code. It also has a built-in MCP server, so you can chat with your meeting notes and transcripts in Claude Desktop. Ask things like "What did Sarah and I agree to last time?" or "Draft a follow-up email from today's design review" (see demo video). What it does 🔒 Private by design - recording, transcription, and AI all run on your Mac. Your data stays local. 🧠 Powerful AI summaries - automatic summaries, action items, meeting titles, and real speaker names. 🤖 No bots, any app - records Zoom, Teams, Meet, FaceTime, Slack huddles, or even an in-person conversation. No bot joins your call. 🗣️ Knows who said what - transcripts split by speaker, and it recognizes voices across meetings to tag names automatically. 💬 Chat with your meetings - MCP server for Claude Desktop. Claude can search your meetings and read summaries, notes, and full transcripts. 📅 Calendar-aware - sees your upcoming meetings, offers to start recording. ⏹️ Auto-stop - detects when your call ends and stops recording. 🎤 Voice isolation - captures your mic and everyone else as separate, clean channels. No echo. 🌍 Any language - detects the spoken language automatically. 🔍 Search and import - instant full-text search across thousands of meetings, plus import from Granola or any CSV. Private AI == Local AI With Biscotti, you still get state-of-the-art AI for transcription, speaker identification, and summaries. It just runs locally on your Mac. It works fully offline once the models are downloaded. Your data lives on your Mac, and you own and control it. (Yes, Claude Code isn't local, and if you chat with your meetings in Claude Desktop, Claude sees what it retrieves. But the app itself runs all of its AI on-device, and nothing leaves your Mac unless you connect it.) How I built it with Claude Code I spent years at Apple building the Photos app, Memories, the lock screen, and more, and I wanted this to feel like it belongs on the Mac: Swift and SwiftUI, launches instantly, small on disk. Claude Code wrote the code: the native app, system audio capture, the on-device model pipeline, SQLite full-text search, and the MCP server. I used spec-driven development with /spec, a Claude Code skill I open-sourced: https://github.com/scosman/vibe-crafting Demo Video Made in Claude Code Too! The demo video was also done in Claude Code with Videowright: another open-source skill/framework I made for making videos with claude. https://github.com/scosman/videowright Try it (free) Download the notarized app: https://github.com/scosman/Biscotti Requirements: Apple Silicon (M1+), macOS 15+, 16GB RAM recommended. App details: Notarized, Free (no upsell), Private (zero data collection, all AI is local), Source Available on GitHub (PolyForm Perimeter License), built with Claude Code using spec-driven development. What should I build next? And what else would you want Claude to be able to do with your meeting notes/transcripts?
