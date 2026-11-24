---
id: "91d4c1b5c3984a99"
title: "Why are so many services using email magic links for login?"
url: "https://news.ycombinator.com/item?id=50625996"
link: "https://news.ycombinator.com/item?id=50625996"
source: "Hacker News"
domain: "news.ycombinator.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-24T09:53:26Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["bfbf"]
language: "en"
summary: "I've noticed a big uptick in login screens defaulting to sending email magic links rather than asking for a password. Notably Claude does this (which during the Outlook outage last week completely blocked me from accessing it). I can only assume that this is a misguided attempt to make login easier for the people who use the Forgot Password link all the the time instead of a proper password…"
tags: []
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 144
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50625996"
score: 11
comments: 8
community: "Hacker News"
---

# Why are so many services using email magic links for login?

Hacker News · bfbf · 2026-11-24

I've noticed a big uptick in login screens defaulting to sending email magic links rather than asking for a password. Notably Claude does this (which during the Outlook outage last week completely blocked me from accessing it). I can only assume that this is a misguided attempt to make login easier for the people who use the Forgot Password link all the the time instead of a proper password manager. It's 1FA where your single factor is access a different service (your email) rather than a known secret. Is there an actual best practice HIG or security guideline that recommends this approach? To my mind, it's both less secure and less convenient. I'm wondering if it's an anti pattern where someone (or an LLM) has copied a service which does this, and that creates a feedback loop where more orgs jump on the bandwagon.
