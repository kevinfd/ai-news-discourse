---
id: "a3e718c63bf3b9c3"
title: "Docker SBX native macOS app"
url: "https://reddit.com/r/ClaudeAI/comments/1xowocx/docker_sbx_native_macos_app"
link: "https://reddit.com/r/ClaudeAI/comments/1xowocx/docker_sbx_native_macos_app"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T22:44:33Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Hekos"]
language: "en"
summary: "I've used docker sbx exclusively for months now and its worked well for me. I know what the agents are doing and my credentials feel safer with isolation. But it was tedious to keep making wrappers, running the TUI to grant permissions and so on. The recent sbxenv.yaml and menu bar helped a lot but it was still more tedious than it needed to be. So I built Paddock, a native macOS app on top of…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "post"
word_count: 337
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xowocx/docker_sbx_native_macos_app/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Docker SBX native macOS app

Reddit · Hekos · 2026-11-05

I've used docker sbx exclusively for months now and its worked well for me. I know what the agents are doing and my credentials feel safer with isolation. But it was tedious to keep making wrappers, running the TUI to grant permissions and so on. The recent sbxenv.yaml and menu bar helped a lot but it was still more tedious than it needed to be. So I built Paddock, a native macOS app on top of Docker sbx. projects have tabs for each agent, tabs for browser output and playwright tabs so you can quickly give it feedback network rules, storage, processes have their own tabs and bubble up to the projects via notificaitons uses sbxenv.yaml so developers without Paddock get the same base via a simple shell command voice chat and hands free mode optimized for Claude but works with anything sbx including local models Here's how I used Claude to build it: I started with `backlog`, building out the requirements and using subagents to research the viability of each feature request; like voice, template handling; real time actions; its still in the source if you want some insight I dogfeed the entire process - I started with running inside a stack sandbox and installed the toolchain within, build out the initial shell then started working in that, and restarted at each milestone I created "probes" where Claude made tests that I ran against the local `sbx` process ( you can still find the command in the codebase if you want to try ) - the `sbx` TUI was used to fetch data at the start ( it's still there as a backup ) but I later turned to the internal API's to get better performance The window sometimes crashed and I needed a way to diagnose it for Claude, so there is a command for that as well - the logs were then used to fix bugs and make the app more robust It's free and open source (MIT). Happy to hear feedback. https://gik.si/paddock/ https://github.com/MarZab/paddock
