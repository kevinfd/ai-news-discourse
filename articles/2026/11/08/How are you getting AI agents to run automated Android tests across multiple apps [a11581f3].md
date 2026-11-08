---
id: "a11581f38cfc2988"
title: "How are you getting AI agents to run automated Android tests across multiple apps?"
url: "https://reddit.com/r/ClaudeAI/comments/1xql8z9/how_are_you_getting_ai_agents_to_run_automated"
link: "https://reddit.com/r/ClaudeAI/comments/1xql8z9/how_are_you_getting_ai_agents_to_run_automated"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T00:28:27Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["milkygirl21"]
language: "en"
summary: "I'm building Android apps with AI coding agents, and I'd like the agents to handle the testing too: spin up the environment, run end-to-end scenarios that span several apps on a real device or emulator, and report back what broke. My automated tests pass, but they only cover my app on its own, which leaves out exactly the cross-app behavior where real bugs show up. The example that pushed me…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 230
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xql8z9/how_are_you_getting_ai_agents_to_run_automated/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How are you getting AI agents to run automated Android tests across multiple apps?

Reddit · milkygirl21 · 2026-11-08

I'm building Android apps with AI coding agents, and I'd like the agents to handle the testing too: spin up the environment, run end-to-end scenarios that span several apps on a real device or emulator, and report back what broke. My automated tests pass, but they only cover my app on its own, which leaves out exactly the cross-app behavior where real bugs show up. The example that pushed me here is a voice keyboard (an IME) I'm working on. Dictation can get lost inside WhatsApp even though my tests are passing. I'd want an agent to catch that kind of thing by driving the keyboard into real third-party apps, interrupting things mid-flow (killing the target app, restarting the input connection), and checking the text actually lands in the field. So I'm curious what tooling has held up for you in multi-app flows like this, whether that's UI Automator, Appium, Maestro or something else. For those letting agents drive devices, do you run a local emulator, a physical phone over adb, or a cloud farm like Firebase Test Lab or BrowserStack, and what does that realistically cost? Any IME-specific gotchas, like switching the active keyboard programmatically or quirks in apps like WhatsApp, would be great to hear about too. And how do you keep it all stable enough that an agent can run it unattended without drowning in flaky failures?
