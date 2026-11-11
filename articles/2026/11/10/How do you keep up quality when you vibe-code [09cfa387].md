---
id: "09cfa387d82b5aee"
title: "How do you keep up quality when you vibe-code?"
url: "https://news.ycombinator.com/item?id=50444380"
link: "https://news.ycombinator.com/item?id=50444380"
source: "Hacker News"
domain: "news.ycombinator.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-10T18:41:15Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["nkcodes"]
language: "en"
summary: "I'm having a really hard time working with claude. In the past when I wrote all the code manually, it was always carefully reviewed and architected, with all possible flows carefully mapped out. Now, my code is mostly AI written which has led to things going out of control. Since it's easy to add new features and support many user flows, we went ahead and implemented flows that support a lot of…"
tags: []
orgs: []
topics: []
content_source: "post"
word_count: 174
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50444380"
score: 31
comments: 29
community: "Hacker News"
---

# How do you keep up quality when you vibe-code?

Hacker News · nkcodes · 2026-11-10

I'm having a really hard time working with claude. In the past when I wrote all the code manually, it was always carefully reviewed and architected, with all possible flows carefully mapped out. Now, my code is mostly AI written which has led to things going out of control. Since it's easy to add new features and support many user flows, we went ahead and implemented flows that support a lot of cases our users run into. But now, I feel like things are getting too complex with no central notion of behaviour definitions, which causes every bug-fixing session to feel like a game of whack-a-mole, and results in missing edge cases and UI bugs that are becoming impossible to review and keep track of. Every time I build anything new, it adds more complexity and the agent only seems to focus on the surrounding code within that session without keeping track of how it fits into the rest of the code base/product. How do you all deal with this? Any suggestions for improving?
