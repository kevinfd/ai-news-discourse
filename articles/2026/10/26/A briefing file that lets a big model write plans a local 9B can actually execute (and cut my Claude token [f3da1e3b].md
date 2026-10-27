---
id: "f3da1e3b146f8b29"
title: "A briefing file that lets a big model write plans a local 9B can actually execute (and cut my Claude token spend)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xg29rq/a_briefing_file_that_lets_a_big_model_write_plans"
link: "https://reddit.com/r/LocalLLaMA/comments/1xg29rq/a_briefing_file_that_lets_a_big_model_write_plans"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T16:49:34Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Electrical_Ninja3805"]
language: "en"
summary: "I've been running Ornith 1.5-9B (8-bit) as a local coding agent on real engineering work. It can do the work, but only when the plan is written for a small model. I wrote down what I learned into a public file meant to be handed to a stronger planning model (I use Claude Code): https://git.teamide.dev/David/TeamIDE-methodology/src/branch/main/Model-Best-Practices/Ornith-q8-best-practices.md The…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 290
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xg29rq/a_briefing_file_that_lets_a_big_model_write_plans/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# A briefing file that lets a big model write plans a local 9B can actually execute (and cut my Claude token spend)

Reddit · Electrical_Ninja3805 · 2026-10-26

I've been running Ornith 1.5-9B (8-bit) as a local coding agent on real engineering work. It can do the work, but only when the plan is written for a small model. I wrote down what I learned into a public file meant to be handed to a stronger planning model (I use Claude Code): https://git.teamide.dev/David/TeamIDE-methodology/src/branch/main/Model-Best-Practices/Ornith-q8-best-practices.md The split The stronger model writes the spec and a plan of small task cards, then verifies the result before merge. The local model does the long, mechanical middle: running commands, builds, polling jobs, git work. That's where most of the tokens go, and it runs on my own hardware. What the file covers What the small model is good at, and what to expect (work more reliable than its reports; doesn't explore on its own; doesn't know when it's done; slows down at long context). How to brief it: exact files and line ranges, absolute paths, 1–3 line edits, exact function signatures, every rule written down, every step ending in a command with its exact expected output, explicit stop rules. How to run it: one task per fresh session, small context, the plan file as memory. Before anything lands: verify claims against git and logs, not the model's summary. Results so far: a 75-commit merge across two repos with every regression test passing, done by the 9B. Its notes about what it did were wrong more than once; the plan's checks and a final verification caught every one. Limitations: slower (most of a day vs about an hour for Claude alone on that phase), and you need hardware that runs a decent local model. The rules are harness-agnostic but were learned with one model; I'd like to hear how they hold up with others.
