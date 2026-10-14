---
id: "382d5ff8a5922717"
title: "I forked Chromium to fix my browser automation headaches with Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1x5iwlj/i_forked_chromium_to_fix_my_browser_automation"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T05:22:05Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["sabotizer"]
language: "en"
summary: "I use Claude Code for a lot of browser work. Mainly tools I need that were never built for agents, smoke-testing my work and searching the web for things I care about. Things kept going wrong: chrome-devtools-mcp tends to open throwaway instances and profiles, and rarely cleans them up. \"Allow remote debugging?\" prompts on every connect (when using autoConnect). \"Chrome is being controlled by…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["agents & coding"]
content_source: "post"
word_count: 409
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5iwlj/i_forked_chromium_to_fix_my_browser_automation/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I forked Chromium to fix my browser automation headaches with Claude Code

Reddit · sabotizer · 2026-10-14

I use Claude Code for a lot of browser work. Mainly tools I need that were never built for agents, smoke-testing my work and searching the web for things I care about. Things kept going wrong: chrome-devtools-mcp tends to open throwaway instances and profiles, and rarely cleans them up. "Allow remote debugging?" prompts on every connect (when using autoConnect). "Chrome is being controlled by automated test software" on top of every page (might just be my OCD). Tab sprawl. After an hour: a dozen windows and no idea which tab belonged to which session, or whether I could close it. Agents stepping on each other. On a shared profile they took over each other's tabs. With --isolated , every login was gone on close. RAM. One chrome-devtools-mcp per Claude Code session, about 270 MB each before it even starts Chrome. Ten agents: ~2.7 GB before a single page loads. I tried various Cloud browser services . Mostly unreliable and/or expensive. And most sites blocked by bot detection due to non-residential IP address. So I forked Chromium and moved the agents in. Shuttle : Every agent is a named identity (name, color, avatar) with its own storage. My agents log in once, and stay logged in. Claude agents see the "browser agent" surface, and have their own control plane to create "Agent Profiles", sessions and tabs as needed. MCP server is built in (http, loopback-only by default). So no middle-man needed. Every agent works in its own tab group in your window, color-coded. This is the biggest UX improvement for me, as I can clearly see what each agent is doing. No DX friction: no debugging dialog, no automation bar, navigator.webdriver is false, and no window pops up until an agent needs one. Clean & minimal MCP surface: 12 browser tools + 24 page tools. Vercel's awesome agent-browser is bundled in, so tool calls are directly controlling the browser. Per-session CDP endpoints for Playwright if needed, e.g. for scripted e2e tests. Meticulously removed bloat from Chromium: Google sign-in, Profile Sync, Telemetry, Google AI features, Translate, Password manager, Chrome Apps, Bookmarks, and many more. Site: https://www.shuttlebrowser.com Some humor and easter eggs are hidden on this site. Code: https://github.com/shuttle-browser/shuttle Disclosure: I'm promoting my own tool. It's free and open source (BSD-3). I hope others use it, like it, and share their feedback and ideas with me. I've used Claude Opus 5.5 primarily for implementation, and Fable 5.1 and Astra for adversarial review.
