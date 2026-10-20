---
id: "7d6d6a347b4a0fd7"
title: "Research shows AI agents reject sponsored listings 97% of the time. Nobody is building the advertising infrastructure for what comes next."
url: "https://reddit.com/r/artificial/comments/1xadsk6/research_shows_ai_agents_reject_sponsored"
link: "https://reddit.com/r/artificial/comments/1xadsk6/research_shows_ai_agents_reject_sponsored"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T00:26:43Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["peaceinmind2002"]
language: "en"
summary: "Two recent papers caught my attention and I think they point to a massive blind spot in how we're thinking about AI agents in commerce. Wadi & Ma (McGill, Sep 2026) tested what happens when you tell an LLM \"you work for the traveler\" vs \"you work for the booking platform.\" The consumer-deployed agent chose sponsored listings only 2.8% of the time — a 97.2% rejection rate. The platform-deployed…"
tags: ["r/artificial"]
orgs: ["Google", "Anthropic", "Microsoft", "OpenAI"]
topics: ["agents & coding", "search & media", "models & research"]
content_source: "post"
word_count: 303
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xadsk6/research_shows_ai_agents_reject_sponsored/"
score: null
comments: null
community: "r/artificial"
---

# Research shows AI agents reject sponsored listings 97% of the time. Nobody is building the advertising infrastructure for what comes next.

Reddit · peaceinmind2002 · 2026-10-20

Two recent papers caught my attention and I think they point to a massive blind spot in how we're thinking about AI agents in commerce. Wadi & Ma (McGill, Sep 2026) tested what happens when you tell an LLM "you work for the traveler" vs "you work for the booking platform." The consumer-deployed agent chose sponsored listings only 2.8% of the time — a 97.2% rejection rate. The platform-deployed agent? 25%. Nearly 9x higher. This replicated across GPT, Gemini, and Claude. Qiu & Mei (Michigan, May 2026) mapped out four tiers of advertising influence in generative AI and cataloged the commerce protocols being built — Google's UCP, OpenAI's ACP, Microsoft's Copilot Checkout. But here's what struck me: all of these handle transactions. None of them handle demand generation — how does a brand even get into an agent's consideration set? Both papers study platform-deployed agents (Booking.com's assistant, Expedia's agent). But the market is heading toward user-deployed agents that work exclusively for you, with no platform allegiance. When that happens: Traditional ads are invisible to agents (designed for human psychology, not machine parsing) Independent agents over-filter commercial info — even a role-neutral agent penalizes "sponsored" content by 42 percentage points just from training data bias The protocols being built to replace this (UCP, ACP) are platform-owned, not neutral So we have a paradox: the agent that's best for the user (conflict-free, fiduciary) is actually worse in practice because there's no open infrastructure for commercial discovery. Has anyone seen work on this? Specifically on how brands would present structured, machine-evaluable product data to independent agents — not persuasion, but information provision. I wrote a longer synthesis here . Papers referenced: Wadi & Ma, "Whom Do AI Agents Serve?" — https://arxiv.org/abs/2609.17989 Qiu & Mei, "Generative AI Advertising as a Problem of Trustworthy Commercial Intervention" — https://arxiv.org/abs/2605.18673
