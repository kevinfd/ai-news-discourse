---
id: "d13b635b648e7558"
title: "Show HN: VoidAccess – open-source dark web OSINT, from query to a graph"
url: "https://github.com/KatrielMoses/voidaccess"
link: "https://github.com/KatrielMoses/voidaccess"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-20T14:49:33Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["coding-maniac"]
language: "en"
summary: "Hi HN! Im Katriel, and im a Security Researcher/Enthusiast and in the wave of AI, i wanted to build that next gen of security tooling that surpasses the current tools, and even the paid industries with an open source engine. I built MailAccess as well, which is going to be the best damn email osint tool out there, in another year. But just before building MailAccess i built VoidAccess, because i…"
tags: []
orgs: []
topics: ["models & research", "safety & ethics", "search & media"]
content_source: "fulltext"
word_count: 364
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50167286"
score: 185
comments: 13
community: "Hacker News"
---

# Show HN: VoidAccess – open-source dark web OSINT, from query to a graph

GitHub · coding-maniac · 2026-10-20

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert
Star896 (896)You must be signed in to star a repository
About
Self-hosted dark web OSINT platform. Automated threat intelligence from query to graph in 13 steps. Free alternative to Recorded Future, DarkOwl, and Flare.
Ask one question. Get a sourced report, a graph you can search, and IOCs you can load.
For security researchers, threat-intel teams, MSSPs and authorized investigators.
The hosted version runs this engine for you. Searches and page fetches go out from our servers through Tor, so your research doesn't start from your laptop or office network. A live view shows every link found, kept or discarded (duplicates, 404s, timeouts, the safety filter), then the results open as a graph with every value searchable by category.
One query fans out in parallel to 12+ Tor search engines, code hosts, security feeds and curated .onion seeds, then follows new .onion links as it finds them. Prohibited queries, URLs and content are dropped at mandatory safety gates. The full pipeline, with timeouts and recovery, is in Architecture.
What it finds
Entities are linked into a relationship graph with communities and infrastructure clusters, and cross-referenced against earlier findings.
No Tor or LLM key yet? voidaccess investigate "LockBit ransomware" --no-llm --no-tor --depth shallow runs a clearnet-only pass. For the full stack (PostgreSQL, Tor, API and web UI) with Docker Compose, see the self-hosting guide. Python 3.10+.
CLI reference
Optional clearnet requests can use ScrapingAnt with --use-scraping-api or --use-proxies; Tor, .onion, GitHub and GitLab traffic are unaffected.
Sources and enrichment
Sources that need an API key are skipped cleanly without one. The hosted version uses a subset whose terms allow it. Full configuration: Architecture. For full sentence-transformer embeddings, pip install "voidaccess[nlp]"; without it, a deterministic fallback encoder is used.
MIT. Use VoidAccess only for authorized security research and threat-intelligence work; see the Usage Policy.
About
Self-hosted dark web OSINT platform. Automated threat intelligence from query to graph in 13 steps. Free alternative to Recorded Future, DarkOwl, and Flare.
