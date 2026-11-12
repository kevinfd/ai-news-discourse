---
id: "5f9dc11546f64b49"
title: "Memory can silently burn your usage. Suggestion for a fix"
url: "https://reddit.com/r/ClaudeAI/comments/1xtwsa2/memory_can_silently_burn_your_usage_suggestion"
link: "https://reddit.com/r/ClaudeAI/comments/1xtwsa2/memory_can_silently_burn_your_usage_suggestion"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T23:14:05Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["NumbersLie_"]
language: "en"
summary: "Not here to complain about limits, just sharing something I found that I think is worth fixing. I’m on Pro and noticed my usage was draining way faster than normal for the same kind of work. Last night I burned about 20% of my weekly limit in one evening. Turns out it was memory. I’d been building a website with Claude, and at some point I asked it to remember my designs. Instead of short notes,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 276
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtwsa2/memory_can_silently_burn_your_usage_suggestion/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Memory can silently burn your usage. Suggestion for a fix

Reddit · NumbersLie_ · 2026-11-11

Not here to complain about limits, just sharing something I found that I think is worth fixing. I’m on Pro and noticed my usage was draining way faster than normal for the same kind of work. Last night I burned about 20% of my weekly limit in one evening. Turns out it was memory. I’d been building a website with Claude, and at some point I asked it to remember my designs. Instead of short notes, it saved the full code of my sections into memory (around 110 KB total), plus a note to read those files before every website task. So every chat about my site quietly loaded 100+ KB of code before doing anything, and that cost stacked up with every single message. Nothing warned me. I only figured it out because I asked Claude to list my memory files and their sizes. Once I deleted the code files, things went back to normal. I think most people would never notice this and would just assume Claude got more expensive. A few ideas that could help, not sure what’s best on their side: don’t save full code or long docs to memory, keep it to short notes (or at least ask first and mention it costs usage) show a warning when a memory file gets really big only load big memory files when they’re actually needed, not at the start of every related chat Seems like a win both ways: users keep their limits and Anthropic saves compute. Tip if your usage feels weird: ask Claude to list your memory files with sizes. If something’s huge, ask it to trim it to key points.
