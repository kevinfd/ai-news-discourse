---
id: "eae431b19328080d"
title: "I'm not a programmer, so I directed Claude Code to build a self-hosted YouTube client"
url: "https://reddit.com/r/ClaudeAI/comments/1xxmu5e/im_not_a_programmer_so_i_directed_claude_code_to"
link: "https://reddit.com/r/ClaudeAI/comments/1xxmu5e/im_not_a_programmer_so_i_directed_claude_code_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T11:16:27Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["lovespeedtest"]
language: "en"
summary: "GitHub: https://github.com/biolend83/tubehaus I built TubeHaus with Claude Code. I can read a bit of code, but I'm not a programmer, so my job has been to direct it, test what comes back, and say when something is wrong. Claude Code wrote about 95% of the code. I spent about nine months building this for myself; then Claude suggested I publish it, so I put the public repo up on October 18. I…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["search & media", "products & launches", "jobs & society"]
content_source: "post"
word_count: 663
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xxmu5e/im_not_a_programmer_so_i_directed_claude_code_to/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I'm not a programmer, so I directed Claude Code to build a self-hosted YouTube client

Reddit · lovespeedtest · 2026-11-16

GitHub: https://github.com/biolend83/tubehaus I built TubeHaus with Claude Code. I can read a bit of code, but I'm not a programmer, so my job has been to direct it, test what comes back, and say when something is wrong. Claude Code wrote about 95% of the code. I spent about nine months building this for myself; then Claude suggested I publish it, so I put the public repo up on October 18. I posted about it on Reddit, and in about a month since then it has taken off more than I expected: 470+ stars and 30+ forks, including 72 stars on 15 November. I wanted YouTube on my TV and phone without a Google account. Setting up the existing options was hard for me, so I started asking Claude Code to build something I could actually run myself. What I ended up with is a private YouTube client you host yourself, plus native apps. There is no Google account and no tracking. The server is one Python file that uses only the standard library, with a vanilla JavaScript web UI: plain ES modules, no framework and no build step. Up to 1.5 the server sat on Invidious, its companion and PostgreSQL. In 1.6 I had that replaced with a built-in engine, so the install no longer needs those three containers. It still answers in Invidious' API format, so the web app and other tools that already spoke that API kept working. A lot of what this project knows about YouTube was learned from Invidious, and I'm grateful for that. The apps are written in Kotlin and share about 80% of their code across Android, Android TV, desktop (Windows, macOS and Linux) and iOS. The iOS app is a sideloaded beta. The server is AGPL-3.0; the apps are GPL-3.0. The part that talks to Chromecast and Google TV was later split out as a library called castwire. Cloudflare WARP is optional. The default Docker setup can send YouTube traffic through WARP in proxy mode, so YouTube sees a WARP address instead of your home. The home and app-store setup turns WARP off. If YouTube starts blocking that address, the server can reconnect WARP to get a new one. It does not rotate addresses all the time; it only does this when it gets walled. Because I can only read a bit of code, I don't review a diff the way a programmer would. I review mainly by using the result. I describe the behaviour I want in ordinary language, then I install the build, click through the screens, play a video, and check whether the thing I asked for is actually there. I test every release on my own devices. I also had Claude Code add a --doctor self-check and some automated tests, because those give me a yes or no I can run even when I don't want to read through the whole change. Where this goes wrong is usually my instructions. If I ask for too much at once, it changes things I didn't ask for, and I only notice later when something I already used stops working. I learned to ask for one change, test it, then ask for the next. When something breaks I don't guess at the cause. I send back what I saw: this page is blank, this button does nothing, the install is still asking for a database. That has been more useful than me pretending I understood the patch. The rewrite in 1.6 is a good example. I could skim the change, but I couldn't really judge the code quality of replacing Invidious. I judged it by whether the same screens still worked, and whether docker compose really came up with three fewer containers. It's free to try. The code is open source; you can run the server with docker compose or install the apps from the releases. If you're also directing Claude Code without being a programmer, I'm happy to answer questions about the workflow.
