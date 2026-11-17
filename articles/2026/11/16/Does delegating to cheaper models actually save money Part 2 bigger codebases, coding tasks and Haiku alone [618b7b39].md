---
id: "618b7b3911478aab"
title: "Does delegating to cheaper models actually save money? Part 2: bigger codebases, coding tasks and Haiku alone"
url: "https://reddit.com/r/ClaudeAI/comments/1xy1zw7/does_delegating_to_cheaper_models_actually_save"
link: "https://reddit.com/r/ClaudeAI/comments/1xy1zw7/does_delegating_to_cheaper_models_actually_save"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T21:34:25Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["BeginningSir7334"]
language: "en"
summary: "TL;DR - I’ve run about 300 benchmarks on real open-source codebases, testing how Claude Code splits work between models (Opus as the lead, cheaper models like Haiku as helpers) and when that pays off. It depends on codebase size and task. - On small jobs, Opus alone can be cheaper than Opus + subagents, and more accurate on small-codebase reviews, probably because of less overhead and cheap…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding", "jobs & society"]
content_source: "post"
word_count: 281
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xy1zw7/does_delegating_to_cheaper_models_actually_save/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Does delegating to cheaper models actually save money? Part 2: bigger codebases, coding tasks and Haiku alone

Reddit · BeginningSir7334 · 2026-11-16

TL;DR - I’ve run about 300 benchmarks on real open-source codebases, testing how Claude Code splits work between models (Opus as the lead, cheaper models like Haiku as helpers) and when that pays off. It depends on codebase size and task. - On small jobs, Opus alone can be cheaper than Opus + subagents, and more accurate on small-codebase reviews, probably because of less overhead and cheap cached context. - Opus told not to delegate may work harder than Opus left alone: on one big docs check it wrote about 50% more, cost more and found more errors (44 vs 36). - On coding, Opus + Haiku saved about 20-30% at the same quality. But Haiku alone is very capable for the price on well-defined tasks with tests: about 5% of Opus alone's cost, with almost the same results, though a bit less thorough. - Here’s one of the most important charts of this project. On an 85-page docs check, Opus + Haiku read almost 3 times as much as Opus alone and wrote 8 times as many tokens, yet cost 53% less and found 72 real errors against 49. Several subagents probably cover much more ground, which makes up for Haiku being weaker. https://preview.redd.it/bamto2rnm12i1.png?width=3000&format=png&auto=webp&s=5c8def74ba50485af5f0bfb0bfa54280081221cd A couple of weeks ago I shared an experiment ( https://www.reddit.com/r/ClaudeCode/comments/1xn18cu/does\_delegating\_to\_cheaper\_models\_actually\_save/ ) testing whether Claude Opus uses subagents effectively. I compared four setups: - Forced Opus: told not to use subagents. - Spontaneous Opus: free to delegate, but it never did. - Skill-routed: my skill chooses when to delegate and to which model. - Forced Haiku: all subagents use Haiku, while Opus plans and checks. Full post available at https://www.reddit.com/r/ClaudeCode/comments/1xxyc5a/does_delegating_to_cheaper_models_actually_save/ Full results, charts and checker: https://github.com/Manuele-T/claude-model-router
