---
id: "2d52235a822456d6"
title: "A clause that lifted human investment to 67% (2011 lab study): in a new preprint's game, no AI seller invested"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xmi2g2/a_clause_that_lifted_human_investment_to_67_2011"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xmi2g2/a_clause_that_lifted_human_investment_to_67_2011"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T03:17:41Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "A new preprint (\"Renegotiable Options Fail to Prevent Hold-Up Between Two Profit-Maximizing Frontier LLM Agents\", arXiv 2610.40961, seven independent authors) put two AI agents into a classic economics game. The human numbers below come from a different experiment, a 2011 lab study by Hoppe and Schmitz with its own subjects and setup, not from these authors. The game: a seller can pay to adapt a…"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI", "Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 368
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xmi2g2/a_clause_that_lifted_human_investment_to_67_2011/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# A clause that lifted human investment to 67% (2011 lab study): in a new preprint's game, no AI seller invested

Reddit · shoumikgoswami · 2026-11-03

A new preprint ("Renegotiable Options Fail to Prevent Hold-Up Between Two Profit-Maximizing Frontier LLM Agents", arXiv 2610.40961, seven independent authors) put two AI agents into a classic economics game. The human numbers below come from a different experiment, a 2011 lab study by Hoppe and Schmitz with its own subjects and setup, not from these authors. The game: a seller can pay to adapt a product to one buyer. Once the money is spent, the buyer can offer almost nothing and the seller will still accept, so a seller who sees this coming never adapts. One fix is an option: the buyer can buy at a fixed price. In theory that stops working if the buyer can let the option lapse and offer their own price instead (a renegotiable option). In the 2011 human study, that renegotiable option raised the share of pairs where the seller adapted from 41.5% (22 of 53) with no contract to 67.2% (43 of 64). Their denominator counts pairs where someone declined to take part or sign. The preprint had Claude Opus 5.5 and GPT-6.1 Sol, each told to maximize its side's profit, play the same structure: 1,440 one-shot games (96 written scenarios, five contract types, three model pairings). Results by contract type: - Option with no renegotiation (288 games): the seller adapted every time. - No contract, a non-binding reference price, or the renegotiable option (864 games together): no seller adapted. - Fixed price (the remaining 288 games): buyers refused to sign every time, so there was no sale and no investment. Two checks from the authors: removing the "maximize profit" instruction changed no seller's choice under no contract, the option, or the renegotiable option, and when the numbers were changed so that adapting only added cost, sellers didn't adapt just because an option was on offer. Limits: it's a preprint, the games are one-shot written scenarios, two models carry the results, and the comparison with humans crosses two different experiments. If agents end up signing contracts for people, which protections that work because of how humans behave would you expect to stop working? And which ones only work because the agent can't be talked out of its own incentive? Source: https://arxiv.org/abs/2610.40961
