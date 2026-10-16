---
id: "d91ead6950e7810d"
title: "Anthropic's Scion is heavily inspired by Mononoke"
url: "https://sunshowers.io/posts/anthropic-mononoke"
link: "https://sunshowers.io/posts/anthropic-mononoke"
source: "Anthropic's Scion is heavily inspired by Mononoke"
domain: "sunshowers.io"
source_type: "community"
collector: "hackernews"
date: "2026-10-14T20:30:54Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["sunshowers"]
language: "en"
summary: "Anthropic’s Scion is heavily inspired by Mononoke\nDiscuss on Hacker News or Lobsters.\nHere is Anthropic describing (archive link) yesterday how their new version control system, Scion, uses a concept called “derived data” to make operations like blames more efficient:\nHere is me, back in 2022, describing in my Oxide candidate materials how the Mononoke source control server I helped build uses a…"
tags: []
orgs: ["Anthropic", "OpenAI", "Google", "Meta", "Cursor"]
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 347
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50094694"
score: 382
comments: 140
community: "Hacker News"
---

# Anthropic's Scion is heavily inspired by Mononoke

Anthropic's Scion is heavily inspired by Mononoke · sunshowers · 2026-10-14

Anthropic’s Scion is heavily inspired by Mononoke
Discuss on Hacker News or Lobsters.
Here is Anthropic describing (archive link) yesterday how their new version control system, Scion, uses a concept called “derived data” to make operations like blames more efficient:
Here is me, back in 2022, describing in my Oxide candidate materials how the Mononoke source control server I helped build uses a concept called “derived data” to make operations like blames more efficient:
I think the level of imitation goes well beyond having similar insights1. The fact that Sapling was only credited for “hard-won lessons”, and that Mononoke was not mentioned at all, borders on plagiarism. The post comes off as Anthropic claiming that Claude designed all this, while the reality is that our (extraordinary) team at Meta came up with many of the insights that Claude dutifully applied almost a decade later. (We looked at plenty of prior art for Mononoke and Sapling too, from Google’s SrcFS to write-ahead logs in databases.)
I am very glad that the vision our team had back in 2017-18 was so powerful and enduring — when you go against the grain, you’re always a bit unsure if what you’re doing is genius or madness, and I think Mononoke’s design has stood the test of time. And, to be clear, I do not have a problem with Anthropic copying Mononoke’s design. (This is part of why we put out open source — to benefit humanity through the spread of good ideas.)
But as LLMs continue to assist in designing new systems, they are likely to index heavily on existing designs. Mononoke is open source and in every LLM’s training set. If you ask Opus 5.5 or GPT-6 Astra (thanks Matthew Fowle) about prior art, they both immediately point out the similarities to Mononoke.
Giving credit to those that came before us is now easier — and more important — than ever. There is no longer an excuse.
- For an example of a system with similar insights but many key design differences, see Vicent Marti’s blog post for Cursor. ↩︎
