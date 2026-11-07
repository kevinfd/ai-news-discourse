---
id: "e61f53f92591ceab"
title: "I built a sailing sim with Claude Code and made the frontier models race each other in it"
url: "https://reddit.com/r/ClaudeAI/comments/1xpij9t/i_built_a_sailing_sim_with_claude_code_and_made"
link: "https://reddit.com/r/ClaudeAI/comments/1xpij9t/i_built_a_sailing_sim_with_claude_code_and_made"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T17:22:13Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["abhi3188"]
language: "en"
summary: "I built a sailing sim with Claude Code. Claude Code wrote basically all of it (the boat physics, wind, the 3D water and coast, and the setup that lets AI models sail it) while I directed what to build and checked the results. How the race works: every 5 secs each model gets the full state of the world (23 raw numbers like heading, speed, wind, where the next mark is etc) and sets its helm and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["models & research"]
content_source: "post"
word_count: 132
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpij9t/i_built_a_sailing_sim_with_claude_code_and_made/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a sailing sim with Claude Code and made the frontier models race each other in it

Reddit · abhi3188 · 2026-11-06

I built a sailing sim with Claude Code. Claude Code wrote basically all of it (the boat physics, wind, the 3D water and coast, and the setup that lets AI models sail it) while I directed what to build and checked the results. How the race works: every 5 secs each model gets the full state of the world (23 raw numbers like heading, speed, wind, where the next mark is etc) and sets its helm and sails. No sailing tips. The sim pauses while it thinks, so slow models aren't punished. Opus, GPT-6 Astra and Gemini 4 Argon raced. And yes I know qwen3.5-9b is not frontier but I threw it in there for fun. Not only did argon win it was 5x cheaper than Astra ($0.78 per run versus $3.58)
