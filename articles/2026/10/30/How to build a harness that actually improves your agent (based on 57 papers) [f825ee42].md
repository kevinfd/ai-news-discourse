---
id: "f825ee420533008e"
title: "How to build a harness that actually improves your agent (based on 57 papers)"
url: "https://reddit.com/r/ClaudeAI/comments/1xjcfjs/how_to_build_a_harness_that_actually_improves"
link: "https://reddit.com/r/ClaudeAI/comments/1xjcfjs/how_to_build_a_harness_that_actually_improves"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T11:09:21Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Marmelab"]
language: "en"
summary: "I think by now most of us have figured out that picking a bigger model isn't necessarily how you get a better agent. What actually matters is how you wrap the model, aka its harness. And the numbers back this up: Research from the University of Toronto shows the same model produces up to 6x performance gaps depending on harness design, which is wild IMO. So I got curious what people are actually…"
tags: ["r/ClaudeAI"]
orgs: ["OpenAI", "Microsoft"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 455
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xjcfjs/how_to_build_a_harness_that_actually_improves/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How to build a harness that actually improves your agent (based on 57 papers)

Reddit · Marmelab · 2026-10-30

I think by now most of us have figured out that picking a bigger model isn't necessarily how you get a better agent. What actually matters is how you wrap the model, aka its harness. And the numbers back this up: Research from the University of Toronto shows the same model produces up to 6x performance gaps depending on harness design, which is wild IMO. So I got curious what people are actually doing to get those gains. I went through 57 publications to try to get a clearer picture. (FYI I’ve limited the research to harnesses used for software development and coding agents as it’s what I know best.) Here’s what the common practices boil down to, based on that literature research + my own experience: TLDR: The best harnesses are small, evidence-based and constantly pruned. Mine your previous sessions for patterns and turn past failures into rules. Every time you had to correct your agent, it probably lacked guidance or a guardrail. That right there is a solid candidate for your harness. Delete any rule you can’t prove helps. The flip side of the first point: if you never had to correct it, you don’t need a rule for it. If you can’t show it improves outcomes, it’s just noise eating your context window. Keep your instruction file short. OpenAI tried one giant instruction file and it failed miserably. When everything is “important,” nothing is. They eventually brought it down to around 100 lines. Your main AGENTS.md should act more like a table of contents that points to other rules than a place to dump every rule. Use fewer, sharper tools. Vercel removed 80% of its agent's tools and success went from 80% to 100%. Token usage dropped by more than half, and latency went from 724 to 141 seconds. Microsoft reportedly cut 100 tools down to 5 . Less really can be more. Back up your rules with scripts. Researchers checked how many written security rules had any real effect: only 4-16% did. Prose rules are basically suggestions the agent may or may not follow. The strongest harnesses enforce rules with executable guards like git hooks,linter rules, static code analysis, custom scripts. Garden your harness regularly. Rules go stale and docs drift from what the code actually does. Prune old rules before adding new ones and re-check that everything still works after big changes. OpenAI partly automates this with “a recurring ‘doc-gardening’ agent [that] scans for stale or obsolete documentation and opens fix-up pull requests.” Harness engineering is still a pretty new field, so I think sharing what we learn matters a lot. Which practices are you seeing hold up in your own work and which ones turned out to be hype?
