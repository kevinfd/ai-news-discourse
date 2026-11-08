---
id: "44f4cbe337357b6d"
title: "Does adding \"make the smallest change\" to a bug prompt stop Claude from editing unrelated code?"
url: "https://reddit.com/r/ClaudeAI/comments/1xqs3rk/does_adding_make_the_smallest_change_to_a_bug"
link: "https://reddit.com/r/ClaudeAI/comments/1xqs3rk/does_adding_make_the_smallest_change_to_a_bug"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T06:49:47Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Fuelimit"]
language: "en"
summary: "I've been trying a one-line addition to bug prompts: \" Make the smallest change that fixes this. Don't refactor or rename anything else .\" The idea is that it might cut down on unrelated edits. My first attempt wasn't a clean comparison, because both versions made the same one-line fix, so the instruction had nothing to change. Has anyone measured this? In particular: Did the number of files or…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 98
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xqs3rk/does_adding_make_the_smallest_change_to_a_bug/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Does adding "make the smallest change" to a bug prompt stop Claude from editing unrelated code?

Reddit · Fuelimit · 2026-11-08

I've been trying a one-line addition to bug prompts: " Make the smallest change that fixes this. Don't refactor or rename anything else ." The idea is that it might cut down on unrelated edits. My first attempt wasn't a clean comparison, because both versions made the same one-line fix, so the instruction had nothing to change. Has anyone measured this? In particular: Did the number of files or lines changed actually drop? Did it ever stop Claude from making a fix it needed? Do you add it to every prompt, or only where Claude tends to over-edit?
