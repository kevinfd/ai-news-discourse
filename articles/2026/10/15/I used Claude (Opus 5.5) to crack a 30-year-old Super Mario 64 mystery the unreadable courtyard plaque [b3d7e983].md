---
id: "b3d7e98306f2b734"
title: "I used Claude (Opus 5.5) to crack a 30-year-old Super Mario 64 mystery: the unreadable courtyard plaque"
url: "https://reddit.com/r/ClaudeAI/comments/1x6lz8p/i_used_claude_opus_55_to_crack_a_30yearold_super"
link: "https://reddit.com/r/ClaudeAI/comments/1x6lz8p/i_used_claude_opus_55_to_crack_a_30yearold_super"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T13:42:03Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["decorator"]
language: "en"
summary: "Side project that got out of hand. The plaque in Mario 64's courtyard is a 32×32 texture that fans have argued about since the 90s (\"L is real 2401\"). No upscaler can read it because the pixels aren't there. What Opus did: - wrote a forward model of how a 1996 artist made the texture (font → canvas → resize → blur → stone), then a GPU search over fonts, sizes, kerning and words - built a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media", "models & research", "chips & infrastructure"]
content_source: "post"
word_count: 172
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6lz8p/i_used_claude_opus_55_to_crack_a_30yearold_super/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude (Opus 5.5) to crack a 30-year-old Super Mario 64 mystery: the unreadable courtyard plaque

Reddit · decorator · 2026-10-15

Side project that got out of hand. The plaque in Mario 64's courtyard is a 32×32 texture that fans have argued about since the 90s ("L is real 2401"). No upscaler can read it because the pixels aren't there. What Opus did: - wrote a forward model of how a 1996 artist made the texture (font → canvas → resize → blur → stone), then a GPU search over fonts, sizes, kerning and words - built a dictionary search (K-best DP over 17.7k words) for line 2 and a simulation harness that plants known text in fake plaques to measure how often the method is fooled - wrote the 40-page LaTeX report and the open-source package What went wrong along the way: a word-gap bug that let overlapping words double-count ink, and an early overclaim about the capital S that the joint test didn't actually support. Being strict about held-out tests mattered more than anything. Result: "Eternal Star / We hope so", in Adobe's 1990 Palatino Bold Italic. code + report: github.com/supermochi64/sm64-plaque-decode
