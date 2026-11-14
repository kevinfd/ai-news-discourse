---
id: "e3711e3ebf795fec"
title: "Claude Code limits in a desktop pet"
url: "https://reddit.com/r/ClaudeAI/comments/1xveugv/claude_code_limits_in_a_desktop_pet"
link: "https://reddit.com/r/ClaudeAI/comments/1xveugv/claude_code_limits_in_a_desktop_pet"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T17:59:12Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["SuccessfulCress7441"]
language: "en"
summary: "I built Clauddy, a small pixel pet that sits in a corner of your screen and keeps your Claude Code session and weekly limits in view, along with when each one resets. The Fable weekly limit shows on its own too. It types at its desk while Claude is working, catches fire past 90%, and naps when you step away. If you use Codex or Cursor as well, they show up next to Claude, each with its own…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Cursor"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 264
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xveugv/claude_code_limits_in_a_desktop_pet/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code limits in a desktop pet

Reddit · SuccessfulCress7441 · 2026-11-13

I built Clauddy, a small pixel pet that sits in a corner of your screen and keeps your Claude Code session and weekly limits in view, along with when each one resets. The Fable weekly limit shows on its own too. It types at its desk while Claude is working, catches fire past 90%, and naps when you step away. If you use Codex or Cursor as well, they show up next to Claude, each with its own limits. How Claude Code helped All of it was built with Claude Code, mostly in long sessions where I described the behavior and it wrote the code, the tests and the docs. The rewrite: Claude Code moved it to a native Rust app (egui), screen by screen, porting each piece's tests along the way. CPU went from ~7% to ~1%. Knowing when Claude is working: it read through Claude Code's own session logs to find what marks a turn as open or done, so the pet keeps working through a long command instead of dozing off mid-task. Reviewing the UI without running it: it set up a snapshot gallery that renders every screen state to a PNG. I review the images in each PR instead of clicking through the app. The pets: the sprite sheets are AI-generated, and Claude Code built the step that cuts them, measures every frame and checks each sheet in the tests. One instructions file: an AGENTS.md keeps the project rules, so every session follows the same conventions. Try it Free and open source, on Mac, Windows and Linux: npx clauddy https://github.com/renatoaug/claude-usage-monitor
