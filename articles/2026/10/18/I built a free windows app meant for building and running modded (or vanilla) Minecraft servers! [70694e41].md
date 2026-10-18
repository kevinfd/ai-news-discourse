---
id: "70694e4177e4005a"
title: "I built a free windows app meant for building and running modded (or vanilla) Minecraft servers!"
url: "https://reddit.com/r/ClaudeAI/comments/1x8th3i/i_built_a_free_windows_app_meant_for_building_and"
link: "https://reddit.com/r/ClaudeAI/comments/1x8th3i/i_built_a_free_windows_app_meant_for_building_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T03:57:24Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["bbnorico"]
language: "en"
summary: "I host Minecraft servers for friends on my own PC. A lot of modpacks don’t come with server files, and setting them up by hand is a pain: picking the right loader and Java version, removing mods that only work in the game, fixing crashes. So I built an app to do that for me. I originally made it for myself, but it turned out well enough that I wanted to share it. What it does Search for a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding", "search & media"]
content_source: "post"
word_count: 515
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8th3i/i_built_a_free_windows_app_meant_for_building_and/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free windows app meant for building and running modded (or vanilla) Minecraft servers!

Reddit · bbnorico · 2026-10-18

I host Minecraft servers for friends on my own PC. A lot of modpacks don’t come with server files, and setting them up by hand is a pain: picking the right loader and Java version, removing mods that only work in the game, fixing crashes. So I built an app to do that for me. I originally made it for myself, but it turned out well enough that I wanted to share it. What it does Search for a modpack (or use a .zip/.mrpack file) and it builds a working server: it downloads the mods, installs the loader, picks the right Java and removes client-only mods. Start and stop servers, see the console, live memory use and tick speed, and the addresses friends need to join. If a server crashes, it explains why in plain words and can try to fix it with one click. There’s a Mods tab that warns you when a mod is client-only or made for the wrong version, plus easy operator and whitelist management. You can run several servers at once. How I built it with Claude I’m not a programmer, so Claude Code did all of the coding. My job was deciding what the app should do, testing it on my PC, and passing along bugs my friends hit. The workflow went like this: Plain-language requests. I described what I wanted the way a user would. For example: “the save button should always be visible instead of having to scroll down”, “add a warning if someone leaves settings without saving”, or “make it so you can right-click a server to delete it or edit its properties”. Claude turned those into code and asked when something was unclear. Bug reports pasted straight in. When a user got an error like [WinError 87] The parameter is incorrect while downloading a modpack, I pasted it in. Claude found the cause (a “:” in the file name, which Windows doesn’t allow), fixed it, and changed the app so errors come with step-by-step instructions. Testing before every release. Claude built a fake Minecraft server and a test setup, then used Playwright to click through the real interface automatically (create a server, start it, crash it, fix it, add mods). It also used Wine to build and test the Windows installer, including updating from older versions and uninstalling. Code reviews. I periodically asked it to “double check everything for bugs”. It used sub-agents to review different parts of the app in parallel, and that caught real issues before users hit them. Releases. It set up GitHub Actions so that adding a changelog entry builds the installer and publishes a signed release, and the app updates itself. The app is a single Python file with a native Windows window. Everything (code, tests, release setup and the demo video) was done through Claude Code. Try it (free) It’s completely free and open on GitHub. Download MinecraftServerManager-Setup.exe from the Releases page and run it (Windows only): https://github.com/ricoism/minecraft-server-manager I’d love feedback, and please tell me if you find bugs or have ideas! (App demo video also made by Claude!)
