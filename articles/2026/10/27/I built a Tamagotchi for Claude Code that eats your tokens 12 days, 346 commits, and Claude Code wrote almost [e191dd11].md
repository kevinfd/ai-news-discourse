---
id: "e191dd1138cdb25e"
title: "I built a Tamagotchi for Claude Code that eats your tokens: 12 days, 346 commits, and Claude Code wrote almost all of it"
url: "https://reddit.com/r/ClaudeAI/comments/1xgijef/i_built_a_tamagotchi_for_claude_code_that_eats"
link: "https://reddit.com/r/ClaudeAI/comments/1xgijef/i_built_a_tamagotchi_for_claude_code_that_eats"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T03:59:35Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Smell_Equal"]
language: "en"
summary: "I built Claude Buddy, a pixel-art desktop pet for Windows that lives on your Claude Code usage. It hatches from an egg and grows through seven life stages by eating the tokens you spend. If you ignore it for too long it gets hungry, starves and ends up in a graveyard. It also does useful things: - Shows your 5-hour and weekly limit usage and when each one resets, plus tokens and cost for today,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "jobs & society", "agents & coding"]
content_source: "post"
word_count: 567
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgijef/i_built_a_tamagotchi_for_claude_code_that_eats/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Tamagotchi for Claude Code that eats your tokens: 12 days, 346 commits, and Claude Code wrote almost all of it

Reddit · Smell_Equal · 2026-10-27

I built Claude Buddy, a pixel-art desktop pet for Windows that lives on your Claude Code usage. It hatches from an egg and grows through seven life stages by eating the tokens you spend. If you ignore it for too long it gets hungry, starves and ends up in a graveyard. It also does useful things: - Shows your 5-hour and weekly limit usage and when each one resets, plus tokens and cost for today, the week and all time - Lists every running Claude Code session as Blocked, Working or Idle. When one is waiting for a permission or answer, the buddy holds up a "!" sign, and clicking it takes you to that terminal. - Shows your real local weather on its stage, wears seasonal hats, and picks up habit traits (Night Owl, Tycoon…) based on how you code How I built it with Claude Code I wrote very little of the code by hand. Claude Code (Opus) did most of the work, and my job was mostly design decisions and playtesting. The workflow that worked: Spec first, every version. For each feature batch I brainstormed with Claude until we had a short design spec. Then it wrote an implementation plan with checkboxes and ticked them off as it committed. The repo now has a spec and plan for every version, which made it easy to pick up where I left off. Tests as the safety net. I had Claude write tests alongside every feature. The suite is now about 18,900 parametrized cases, including golden-image tests for the UI cards. These caught a lot of "fixed one thing, broke another" regressions before I saw them. A CLAUDE.md for standing rules. Every time I corrected Claude on something (the repo is on a network drive and builds fail there, the version number lives in two files, and so on), the rule went into CLAUDE.md so I didn't have to repeat it. Sprite art from an HTML prototype. Claude drew the pixel art as an HTML mockup first. I iterated on it in the browser until I liked it, then that file became the reference the app's sprites are tested against. Release automation. Claude wrote the whole release pipeline: run the tests, build with Nuitka, sign the update, publish a GitHub release. Shipping a fix is now one command. What was hard: - Getting usage data out of Claude Code. The app reads Claude Code's local transcript files for token counts, and it installs a small bridge as a status Line and hooks for the live limit percentages and Blocked/Working state. Claude worked out the hook and status line formats with me by experimenting. - Crashes that only appeared after hours of running. They turned out to be Python garbage collection running on a background thread. Claude added crash logging that dumps every thread's stack, which is what finally pinned it down. Free to try (Donations Welcome!): it's completely free with no account and no telemetry. Everything stays on your PC; the only network calls are the weather and the update check. You need Windows 10/11 and Claude Code (the CLI or the desktop app's Code tab). Download the installer from the latest release, run it (no admin needed), and click Connect on the Settings page. https://github.com/skealeye/ClaudeBuddy-releases I'd like feedback, especially on the balance (how fast it gets hungry versus how many tokens a normal day uses).
