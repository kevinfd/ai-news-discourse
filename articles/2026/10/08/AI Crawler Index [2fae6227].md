---
id: "2fae6227e118a2e9"
title: "AI Crawler Index"
url: "https://mojodojo.io/ai-crawler-index"
source: "Mojo Dojo"
domain: "mojodojo.io"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T06:26:03Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["zenincognito"]
language: "en"
summary: "AI Crawler IndexWhich AI bots crawl a real website, and how often\nAI crawlers made 29% of our bot traffic in the last 30 days. We log every crawler that visits mojodojo.io and sort it into AI training bots, AI search bots, assistants reading a page for a user, and search engines like Google and Bing. Each visit is checked against the IP addresses the bot's owner publishes, so anything pretending…"
tags: []
orgs: ["OpenAI", "Anthropic", "Google", "Perplexity", "Apple"]
topics: ["models & research", "search & media", "agents & coding"]
content_source: "fulltext"
word_count: 436
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50002419"
score: 23
comments: 1
community: "Hacker News"
---

# AI Crawler Index

Mojo Dojo · zenincognito · 2026-10-08

AI Crawler IndexWhich AI bots crawl a real website, and how often
AI crawlers made 29% of our bot traffic in the last 30 days. We log every crawler that visits mojodojo.io and sort it into AI training bots, AI search bots, assistants reading a page for a user, and search engines like Google and Bing. Each visit is checked against the IP addresses the bot's owner publishes, so anything pretending to be Googlebot or GPTBot is left out. We started checking IPs on 7 Oct 2026, so earlier visits are sorted by the name the bot gives itself.
22,339 of 77,578 counted bot hits.
AI bots made 1.18 hits for every search engine hit.
Pages an assistant like ChatGPT read on the spot because someone asked it a question.
Of hits claiming to be a bot we can verify, the share that came from the wrong IP.
Crawler hits per day, fakes removed
Who is crawling
Spoofed hits are excluded from every share on this page. 1,507 were removed in this period.
Every bot, ranked
The standouts of the last 30 days
Most hits per day
Fewest hits per page: visits once and moves on
Most hits per page: keeps fetching the same few
Most different pages visited
Fewest days seen (at least 10 hits)
Most fake hits caught by the IP check
A bot needs at least 100 hits in the period to win (10 for rarest visitor). Where an AI bot would win its own category, it is listed underneath.
How the numbers are made
Source. Every page request to mojodojo.io whose user agent looks like a crawler, logged at the web server with the visitor's IP. One site, so read the numbers as a case study rather than a census. Tracking since 6 June 2026. IPs were recorded from 7 Oct 2026; hits before that are classified by user agent only and counted as unverified.
Categories. AI training bots collect pages for model training (GPTBot, ClaudeBot, CCBot). AI search bots build the index behind AI answers (OAI-SearchBot, Claude-SearchBot, PerplexityBot). AI user fetches are live reads on behalf of a person (ChatGPT-User, Claude-User, Perplexity-User).
Verification. A hit counts as verified when its IP sits inside the ranges the operator publishes (OpenAI, Anthropic, Perplexity, Google, Bing, Apple, Common Crawl, DuckDuckGo, Ahrefs), or passes forward-confirmed reverse DNS. Ranges refresh daily. A hit that fails the check is marked spoofed and left out. Bots whose operator publishes no method are counted as unverifiable.
Cite this. Mojo Dojo, “AI Crawler Index”, mojodojo.io/ai-crawler-index, accessed 13 Oct 2026. Free to reuse under CC BY 4.0 with a link back.
