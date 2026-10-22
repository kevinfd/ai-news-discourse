---
id: "918065aafd8b1ca4"
title: "Today's PHP Security Release, and How We're Strengthening PHP Security"
url: "https://simonwillison.net/2026/Oct/21/php-security-release"
link: "https://simonwillison.net/2026/Oct/21/php-security-release"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-21T18:41:53Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Simon Willison"]
language: "en"
summary: "Today's PHP Security Release, and How We're Strengthening PHP Security \nIf you're running anything on PHP it's vital you upgrade - today's updates (across the entire PHP 8.x line) address two remote code execution holes, and there have been exploits circulating since last night, thanks to a leak in the coordinated disclosure process. \n This post from the PHP Foundation explain what went so…"
tags: ["open-source", "php", "security", "ai", "ai-security-research"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["products & launches", "search & media", "models & research"]
content_source: "fulltext"
word_count: 386
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Today's PHP Security Release, and How We're Strengthening PHP Security

Simon Willison · Simon Willison · 2026-10-21

21st October 2026 - Link Blog
Today's PHP Security Release, and How We're Strengthening PHP Security (via) If you're running anything on PHP it's vital you upgrade - today's updates (across the entire PHP 8.x line) address two remote code execution holes, and there have been exploits circulating since last night, thanks to a leak in the coordinated disclosure process.
This post from the PHP Foundation explain what went so wrong:
On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked. In response, the PHP project brought its pre-announcement forward and published it at 19:30 UTC. It also moved the release from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC [...]
As a result of the leak and pre-announcement around 20:00 UTC, Calif, one of the security firms that had reported the issues mistakenly published a video. It showed their proof of concept working against a number of targets and revealed a few additional, though limited, details about the vulnerabilities. Copies of the deleted video started circulating on social media soon after. The video contributed to accelerated development of various PoCs (exploitation proof of concepts), which then increased circulation on October 21st.
This article from the team that discovered the original vulnerability includes a more detailed timeline of the original intended responsible disclosure:
- August 19, 2026: Wiz Research discovers the first PHP vulnerability using Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol.
- August 20, 2026: Unauthenticated RCE is confirmed against Drupal.
- August 21, 2026: Unauthenticated RCE is confirmed against WordPress.
- August 24, 2026: Wiz Research reports the vulnerabilities to the PHP security team.
- September 21, 2026: PHP acknowledges the reports and begins developing a coordinated fix.
- October 21, 2026: Patched PHP releases become available.
- October 21, 2026: Public disclosure.
Recent articles
- Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
- Claude Haiku 5.5 - 7th October 2026
