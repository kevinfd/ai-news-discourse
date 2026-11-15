---
id: "b1c17b635b6016d0"
title: "Dotcker: Run your Dot on a headless server"
url: "https://reddit.com/r/OpenAI/comments/1xwit3f/dotcker_run_your_dot_on_a_headless_server"
link: "https://reddit.com/r/OpenAI/comments/1xwit3f/dotcker_run_your_dot_on_a_headless_server"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T01:22:35Z"
published_date: "2026-11-15"
collected_at: "2026-11-15T13:03:31Z"
authors: ["LetterheadNew5447"]
language: "en"
summary: "Moin, I made a small project called dotcker (dumb name, I know). It runs the official Codex CLI in a container and lets you connect that environment to ChatGPT. No desktop or Electron app needed on the server. I wanted a dedicated workspace for the agent, with access to the repos it should work on, without exposing my whole home directory, SSH keys and browser profiles. My own setup uses…"
tags: ["r/OpenAI"]
orgs: ["OpenAI"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 211
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xwit3f/dotcker_run_your_dot_on_a_headless_server/"
score: null
comments: null
community: "r/OpenAI"
---

# Dotcker: Run your Dot on a headless server

Reddit · LetterheadNew5447 · 2026-11-15

Moin, I made a small project called dotcker (dumb name, I know). It runs the official Codex CLI in a container and lets you connect that environment to ChatGPT. No desktop or Electron app needed on the server. I wanted a dedicated workspace for the agent, with access to the repos it should work on, without exposing my whole home directory, SSH keys and browser profiles. My own setup uses OpenSandbox. I have my coding harnesses in there and use my Dot as the orchestrator. I talk to Dot through ChatGPT, including from my phone, and it coordinates the work through the harnesses inside the sandbox. That is what I mainly use it for. A server environment where my tools and repos are available, with Dot handling the orchestration. You can also run it with Docker Compose. Mount your workspace, log in with your own ChatGPT account and pair the device. There is a local HTTP bridge for chat requests, streaming, persistent conversations and health checks too. The project is unofficial and uses the unmodified Codex CLI. The optional experimental connector relies on undocumented endpoints, so it can break when OpenAI changes things. Code and setup: https://github.com/EricVogt93/dotcker If you try it with a similar setup, let me know how it goes.
