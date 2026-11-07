---
id: "f75df462e0d0cf39"
title: "Android Remote Control MCP v1.13.0 is out: free end-to-end encrypted tunnel, no account needed"
url: "https://reddit.com/r/artificial/comments/1xpf8k5/android_remote_control_mcp_v1130_is_out_free"
link: "https://reddit.com/r/artificial/comments/1xpf8k5/android_remote_control_mcp_v1130_is_out_free"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T15:13:33Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["daniele_dll"]
language: "en"
summary: "🚀 It has been a while since the last release, but Android Remote Control MCP is back and v1.13.0 is now out! It's the MCP server that runs on your phone and lets your AI agent use any app you want. https://github.com/danielealbano/android-remote-control-mcp/releases/tag/v1.13.0 The big news of this release is the free end-to-end encrypted HTTPS tunnel, built into the app, which doesn't require…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Anthropic", "Google", "Meta"]
topics: ["products & launches", "agents & coding", "search & media"]
content_source: "post"
word_count: 452
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xpf8k5/android_remote_control_mcp_v1130_is_out_free/"
score: null
comments: null
community: "r/artificial"
---

# Android Remote Control MCP v1.13.0 is out: free end-to-end encrypted tunnel, no account needed

Reddit · daniele_dll · 2026-11-06

🚀 It has been a while since the last release, but Android Remote Control MCP is back and v1.13.0 is now out! It's the MCP server that runs on your phone and lets your AI agent use any app you want. https://github.com/danielealbano/android-remote-control-mcp/releases/tag/v1.13.0 The big news of this release is the free end-to-end encrypted HTTPS tunnel, built into the app, which doesn't require any account and uses well known services for the HTTPS certificates (Let's Encrypt, Google Trust Services and ZeroSSL)! Cloudflare and ngrok can see your traffic. With my infrastructure no one can, apart from you and your AI provider! The encryption ends on the phone, the certificate key never leaves it, and the app also watches the Certificate Transparency logs and warns you if a certificate for your name gets issued to another key. Basically: install the app, do a few clicks, start it, and in less than a minute you are up and running without having to create any account or pay anything! Adding your phone to Claude.ai or ChatGPT is very straightforward: - Claude: https://claude.ai/new?modal=add-custom-connector#customize/connectors/yours - ChatGPT: https://chatgpt.com/plugins -> Top Right "Add" -> "Add custom MCP server" The only 2 relevant fields are the URL and the name, the rest is secure by default as-is! Android Remote Control MCP also works great with Hermes and OpenClaw! Unlike the adb based tools, nothing runs on your computer: it works through the accessibility service on the phone, most of the time it doesn't need vision and the output is kept short, so it's light on tokens (even Haiku does fine with good directions). This release also brings a bunch of other improvements and fixes, the details are in the release page. A special thanks to the people who forked Android Remote Control MCP: plenty of fixes from the forks have been brought back in thanks to your efforts! Thank you!!! Also, I love open source, so now the app is GPL-3.0-or-later 🔒 and the free e2e tunnel source code is available at https://github.com/danielealbano/android-remote-control-mcp-tunneld (with its own releases). A few things you can do with it: 📣 Find and share your news on LinkedIn, Instagram, Reddit and Discord and reply to the comments without the need of additional more complex platforms, your agent can easily manage your account! ✈️ Plan a trip: flights on momondo and easyJet, stays on Booking.com and Airbnb, best options back to you 🍜 The usual place from where you get your ramen is closed? No worries, your agent can also use Uber Eats, Just Eat, DoorDash, etc. to find the best alternative for you! No adb, no cables, no root! If there's an app for it, your agent can drive it ... you just have to ask!
