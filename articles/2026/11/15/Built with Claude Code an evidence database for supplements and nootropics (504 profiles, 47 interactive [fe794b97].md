---
id: "fe794b97f91f46fd"
title: "Built with Claude Code: an evidence database for supplements and nootropics (504 profiles, 47 interactive mechanism figures, every claim rated against the studies)"
url: "https://reddit.com/r/ClaudeAI/comments/1xx46i9/built_with_claude_code_an_evidence_database_for"
link: "https://reddit.com/r/ClaudeAI/comments/1xx46i9/built_with_claude_code_an_evidence_database_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T19:21:22Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Zukunftselite"]
language: "en"
summary: "I'm a nutrition scientist (biochemistry focus), not a developer. Over the last few weeks I built synaptiklabs.org with Claude Code: a bilingual (English/German) reference that shows where a compound acts in the body and rates every popular claim about it against the human studies. It's free to read; a paid tier is planned for later. What it does: 504 compound profiles (supplements, nootropics,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 350
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xx46i9/built_with_claude_code_an_evidence_database_for/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Built with Claude Code: an evidence database for supplements and nootropics (504 profiles, 47 interactive mechanism figures, every claim rated against the studies)

Reddit · Zukunftselite · 2026-11-15

I'm a nutrition scientist (biochemistry focus), not a developer. Over the last few weeks I built synaptiklabs.org with Claude Code: a bilingual (English/German) reference that shows where a compound acts in the body and rates every popular claim about it against the human studies. It's free to read; a paid tier is planned for later. What it does: 504 compound profiles (supplements, nootropics, peptides, medicines, drugs), 1,794 rated claims and about 7,000 cited sources. Each claim gets an evidence level from 0 to 4 (what kind of study tested it) and a separate result (benefit, mixed, no benefit, never studied). 47 interactive figures show the mechanism, like the dopaminergic synapse in the video, where you switch between compounds. There is also a compare view, a hype check, a simple/technical reading mode and a glossary. No doses, no shops, no tracking. How Claude helped, in detail: Research pipeline: multi-agent workflows draft each profile from primary literature, then separate agents try to refute it. Every DOI and PMID is resolved automatically against Crossref and PubMed, so a made-up citation fails the checks. I set the rating rules and check ratings and key statements myself. Figures: each SVG figure is built by one agent and reviewed by two independent ones (one for the science, one for design and accessibility) before it is merged. Code: Next.js static export on Cloudflare Pages. Claude wrote the components and about 1,600 unit tests plus roughly 2,000 Playwright browser tests. Nothing goes to main without green tests, and scheduled cloud runs repeat the checks off my laptop. Night shifts: I give a goal and a budget, Claude runs agents in parallel git worktrees, keeps a ledger and asks me only for real decisions. What I learned: Claude is only as reliable as the checks you script around it. The biggest gains came from making every claim verifiable (resolvable sources, validation scripts) instead of trusting the text. Parallel agents also need hard limits: my laptop ran out of memory more than once. Free to try: https://synaptiklabs.org/en Happy to answer questions about the workflow, or take criticism of the ratings.
