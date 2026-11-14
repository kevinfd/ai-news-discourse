---
id: "9e23d403b5e8c3da"
title: "How do you keep Claude Code from fixing one bug and creating two more?"
url: "https://reddit.com/r/ClaudeAI/comments/1xvl9eq/how_do_you_keep_claude_code_from_fixing_one_bug"
link: "https://reddit.com/r/ClaudeAI/comments/1xvl9eq/how_do_you_keep_claude_code_from_fixing_one_bug"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T22:07:02Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Huge-Arrival-9791"]
language: "en"
summary: "I’m building products with Claude Code, and I can move pretty fast until I get into bug-fixing mode. Then it starts to feel like one step forward, two steps back. I ask for a specific fix, Claude changes something outside the scope, and a workflow that was fine yesterday suddenly breaks. I’m starting to think the biggest skill here is learning how to keep changes small and prove they’re safe…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 203
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvl9eq/how_do_you_keep_claude_code_from_fixing_one_bug/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How do you keep Claude Code from fixing one bug and creating two more?

Reddit · Huge-Arrival-9791 · 2026-11-13

I’m building products with Claude Code, and I can move pretty fast until I get into bug-fixing mode. Then it starts to feel like one step forward, two steps back. I ask for a specific fix, Claude changes something outside the scope, and a workflow that was fine yesterday suddenly breaks. I’m starting to think the biggest skill here is learning how to keep changes small and prove they’re safe before shipping. I want Claude to fix the issue I asked about, flag any unrelated problems it finds, and stop there. I also want tests that catch regressions in the flows users actually depend on. For those of you shipping real products with Claude Code, what does your bug-fix workflow look like? What goes in CLAUDE.md , and what do you spell out in each prompt? Do you have Claude write a test that fails before it touches the fix? How do you check that the test actually covers the bug? What do you review or run before merging? Which checks have saved you from breaking production? I’d love to see a real example: the prompt you gave Claude, how you kept the diff focused, and what gave you enough confidence to ship.
