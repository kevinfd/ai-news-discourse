---
id: "6040ecac27b6ba4c"
title: "I got tired of being the clipboard between Claude Code, Codex and my other agents, so I built them a shared memory (open source, benchmarked against Git)"
url: "https://reddit.com/r/ClaudeAI/comments/1xdpggi/i_got_tired_of_being_the_clipboard_between_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xdpggi/i_got_tired_of_being_the_clipboard_between_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T20:41:09Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["yash456k"]
language: "en"
summary: "https://preview.redd.it/4cakwj223axh1.png?width=1080&format=png&auto=webp&s=ba98e45aaa3aa15a57a8a73d14d35d312ab35553 Basically I have claude code , codex and my hermes agent ( powered by codex + claude code , mostly opus 5.5 rn lol ) and it was kinda annoying managing information and memory between them. Hivenote is basically them being able to share the same ultimate memory system.. its not a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 176
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdpggi/i_got_tired_of_being_the_clipboard_between_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I got tired of being the clipboard between Claude Code, Codex and my other agents, so I built them a shared memory (open source, benchmarked against Git)

Reddit · yash456k · 2026-10-23

https://preview.redd.it/4cakwj223axh1.png?width=1080&format=png&auto=webp&s=ba98e45aaa3aa15a57a8a73d14d35d312ab35553 Basically I have claude code , codex and my hermes agent ( powered by codex + claude code , mostly opus 5.5 rn lol ) and it was kinda annoying managing information and memory between them. Hivenote is basically them being able to share the same ultimate memory system.. its not a full replacement for a proper memory system but for agent handoffs and stuff I wanna store for getting work done, its really helpful ! At first I tried to use git but felt that I could build a product directly to meet my needs. Has stuff like "wait" where an agent waits for a task another agent will give it etc ( a handoff lands in ~0.1 s vs ~12 s with agents polling github ! ) How I built it : I designed and built hivenote using claude code with opus. I decided the architecture, what to build etc, and claude code helped me write the code and the tests here MIT, self-hosted: npm i -g hivenote https://github.com/Yash456k/hivenote Appreciate any feedback !
