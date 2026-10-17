---
id: "6a9dae8d13e9800c"
title: "Anthropic Console overcharged my card 100x due to internationalization input bug"
url: "https://news.ycombinator.com/item?id=50121562"
link: "https://news.ycombinator.com/item?id=50121562"
source: "Hacker News"
domain: "news.ycombinator.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-16T17:31:42Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["rsorto"]
language: "en"
summary: "I am a LegalTech Attorney leading a developer team from Costa Rica. While trying to load credits onto my Anthropic API account (claude.com), I experienced a critical internationalization (i18n) and UX failure that has placed an unfair financial burden on me due to a severe oversight in their payment pipeline. The platform prompted me for a payment. Since I am in a Spanish-speaking region where…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 485
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50121562"
score: 87
comments: 36
community: "Hacker News"
---

# Anthropic Console overcharged my card 100x due to internationalization input bug

Hacker News · rsorto · 2026-10-16

I am a LegalTech Attorney leading a developer team from Costa Rica. While trying to load credits onto my Anthropic API account (claude.com), I experienced a critical internationalization (i18n) and UX failure that has placed an unfair financial burden on me due to a severe oversight in their payment pipeline. The platform prompted me for a payment. Since I am in a Spanish-speaking region where localized systems and keyboards handle dots and commas differently, I typed 5.04. Anthropic’s input system completely failed to sanitize or validate the data. Instead of throwing a formatting error or converting it properly, it silently stripped the decimal internally and instantly charged my credit card $504.00 USD instead of $5.04 USD. To make matters worse, there was no confirmation modal or review screen summarizing the final amount before processing the transaction. It was a single-click, instantaneous overcharge. Anticipating the Obvious Skepticism:
Before anyone suggests "you should have checked your regional settings" or "just wait for the chargeback": 1. Users are not the QA team: In financial software, a system is never supposed to guess or automatically manipulate a numerical input without explicit validation. If an input is ambiguous due to locale differences, the application must reject it or ask for clarification, not execute a 100x overcharge. 2. Scale of the vulnerability: This time it was $504.00, which is an unfair and frustrating burden for independent developers. But because this pipeline completely lacks a confirmation screen and basic input sanitization, the exact same bug could happen to someone typing 50.00 and end up charging them $5,000.00 or more instantly. It is a systemic financial risk. 3. The Chargeback Illusion: Yes, I have already initiated a chargeback with my bank in Costa Rica. However, banking processes here are slow and take up to 120 days to resolve. In the meantime, the $504.00 has already been deducted and charged to my credit card statement. I am forced to pay for Anthropic’s engineering mistake out of my own pocket right now. The Support Wall:
I filed an official complaint on the exact same day, minutes after it happened. I wasn't met with a human; I was blocked by an automated support BOT. The bot repeatedly and rigidly denied the refund, closing the ticket by citing generic policies without a single human ever looking at the fact that the overcharge was caused by a technical bug in their own platform. As developers, we build systems that process people's money. Omitting a confirmation screen on a financial transaction, failing to sanitize localized numerical inputs, and then hiding behind unyielding AI support bots to keep money that doesn't belong to you is completely unacceptable. If anyone from Anthropic's billing or engineering team is reading this, please look into this bug and review my case. It is a critical flaw that is actively harming international developers who are just trying to build on your ecosystem. Pura vida! R.S.G.
