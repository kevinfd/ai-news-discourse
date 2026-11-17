---
id: "521ebfbb4819dc52"
title: "Anthropic and Google Project Zero Cut Bug Disclosure to 30 Days"
url: "https://vectorwire.ai/article/anthropic-and-google-project-zero-cut-disclosure-windows-as-ai-driven-bug-discov-ece66d"
link: "https://vectorwire.ai/article/anthropic-and-google-project-zero-cut-disclosure-windows-as-ai-driven-bug-discov-ece66d"
source: "Vector Wire"
domain: "vectorwire.ai"
source_type: "community"
collector: "reddit"
date: "2026-11-17T03:47:59Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["VectorWireAI"]
language: "en"
summary: "Anthropic is shortening its coordinated vulnerability disclosure window from 90 days to 30 days for high- and critical-severity issues, citing the growing speed at which frontier models discover software vulnerabilities. Google Project Zero is on a similar trajectory. Starting November 13, the team eliminated the 30-day grace period it previously granted vendors for patch rollout after the…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic", "Google"]
topics: ["policy & regulation"]
content_source: "fulltext"
word_count: 430
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xyaap3/anthropic_and_google_project_zero_cut_bug/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Anthropic and Google Project Zero Cut Bug Disclosure to 30 Days

Vector Wire · VectorWireAI · 2026-11-17

Anthropic is shortening its coordinated vulnerability disclosure window from 90 days to 30 days for high- and critical-severity issues, citing the growing speed at which frontier models discover software vulnerabilities3. The new timelines take effect for vulnerabilities reported to vendors and maintainers on or after January 1, 2027; in-progress reports as of that date keep their existing deadlines.
For all other severity levels, Anthropic is compressing the window to 45 days. The company is also accelerating escalation: it will aim to contact an external vulnerability coordinator after 15 days, down from 30, if a maintainer does not respond to an initial report. Anthropic will wait 30 days instead of 45 after a patch is available before sharing full technical details.
Anthropic noted that some high- and critical-severity vulnerabilities it reported more than 90 days ago, already past the deadline under its current policy, have not yet been disclosed publicly.
Google Project Zero's parallel compression
Google Project Zero is on a similar trajectory. Starting November 13, the team eliminated the 30-day grace period it previously granted vendors for patch rollout after the 90-day disclosure clock expired2. Under its new "Full X" policy, Project Zero will publish vulnerability details 90 days after reporting them, regardless of whether a fix has shipped.
The timeline tightens further on a set schedule: disclosure will move to 60 days beginning February 2, 2027, and to 30 days on January 3, 2028. Project Zero is also removing most special-case exceptions, retaining only its 7-day window for vulnerabilities actively exploited in the wild and its treatment of flaws already made public by others. Vendors may request early publication, and Project Zero may grant exceptions for serious vulnerabilities, as it has done on rare occasions such as Spectre and Meltdown.
What the compression means for vendors
Both policy changes respond to the same pressure: AI-assisted vulnerability discovery is shortening the effective window between a bug's identification and its potential exploitation1. Anthropic said frontier models have become "much better at discovering vulnerabilities" over the last several months. Google Project Zero framed its move explicitly in the context of AI-assisted vulnerability discovery and exploitation.
ANALYSIS The convergence on a 30-day high-severity window from two organizations with different roles — one an AI developer, the other a dedicated offensive-security research team — compresses the patch cycle that every software vendor must meet. Maintainers who previously operated against a 90-day-plus-grace clock will face a deadline one-third as long once both policies fully phase in.
Anthropic's new policy takes effect January 1, 2027. Google Project Zero reaches its 30-day target on January 3, 2028.
