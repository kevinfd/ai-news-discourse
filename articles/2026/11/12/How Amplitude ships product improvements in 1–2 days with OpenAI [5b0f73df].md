---
id: "5b0f73df89a6e310"
title: "How Amplitude ships product improvements in 1–2 days with OpenAI"
url: "https://openai.com/business/customer-stories/amplitude"
link: "https://openai.com/business/customer-stories/amplitude"
source: "OpenAI"
domain: "openai.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-12T20:00:00Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: []
language: "en"
summary: "Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact."
tags: []
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research", "products & launches", "health & science"]
content_source: "fulltext"
word_count: 1008
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How Amplitude ships product improvements in 1–2 days with OpenAI

OpenAI · 2026-11-12

How Amplitude ships product improvements in 1–2 days with OpenAI
Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.
160%
Lift in agent engagement vs. control after one day
1–2 days
Estimated time to ship a product improvement with Wave
51%
Lower mean model cost per dispatch for GPT‑6.1 Sol in Amplitude’s Data Science Agent evaluation.
$1.34
Model cost for GPT‑6.1 Sol in Amplitude’s Opportunity Investigator evaluation.
Amplitude has always helped teams see how people actually use their products. Its proactive product agent Wave helps teams turn those insights into shipped improvements. Amplitude describes Wave as roughly 80% powered by OpenAI models, including GPT‑6.1 Sol, GPT‑6 Luna, and GPT‑Image‑2.5 Flare. Wave turns product insights into implementation plans teams can ship to coding agents, including Codex, then measures the impact.
Amplitude estimates that Wave can help teams ship product improvements in 1–2 days, down from roughly a month. On Amplitude’s own homepage, Wave helped personalize suggestion cards, driving a 160% lift in card-driven sends.
“AI can now find useful work we never thought to assign it. OpenAI’s models can investigate a problem, write and run code, and use the results to decide what to try next.”
Wave is Amplitude’s proactive product agent. Teams give it a product area and the goals and metrics they want to improve. Wave brings together Amplitude data, session replays, customer feedback, and code to identify and prioritize opportunities, develop solutions, and coordinate implementation with people and coding agents. It then tracks outcomes and uses those learnings to inform the next round of improvements.
Behind that workflow, Amplitude uses different OpenAI models for different tasks. GPT‑6.1 Sol supports the opportunity manager and deep investigations into code and data. GPT‑6 Luna handles frequent, lower-cost tasks such as scanning code and running small evaluation checks. GPT‑Image‑2.5 Flare generates product mockups using screenshots from session replays as visual references.
When an opportunity is ready to build, teams can send it directly from Wave to coding agents, including Codex, with a technical plan and acceptance criteria to guide implementation.
“The idea with Wave is you have a unified platform with agents that comb through massive amounts of session replays, analytics, and code to find opportunities to improve products,” explains Jacob Newman, Principal AI Product Manager at Amplitude.
Amplitude tested Wave on its own homepage, where generic suggestion cards were meant to help users start a conversation with an AI agent. Wave discovered that people often bypassed them: in a sample of 100 session replays, 80 users typed their own questions and only 12 selected a suggestion.
Wave proposed personalizing the cards using recent charts, dashboards, or the page a user had come from. It illustrated the change and produced a technical plan, including preserving free typing and showing generic suggestions when personalization context was unavailable. After a brief review, the team handed the work to a coding agent and A/B tested the change.
In the experiment readout Amplitude shared, messages sent through homepage suggestion cards increased 160% relative to control after one day. “It is a great example of how non-groundbreaking things that just get ignored can increase the adoption of features in unexpected ways.” explains Eric Carlson, Senior Principal AI Engineer at Amplitude.
Wave’s tasks place different demands on its models. A deep investigation needs strong reasoning and well-supported conclusions. A small check repeated hundreds of times needs to be fast and inexpensive. Amplitude evaluates quality, latency, and cost for each task, then assigns models accordingly.
“OpenAI gave us both strong reasoning models and smaller, faster models, so we could balance quality, latency, and inference cost across the product”
For Wave’s Opportunity Investigator, Amplitude evaluated whether models corroborated findings, avoided false positives, incorporated evaluator feedback, recovered from tool failures, and kept claims aligned with evidence. GPT‑6.1 Sol scored 4.06 out of 5 overall, compared with 3.62, 3.52, and 2.94 for three alternative models. It led on all five investigation criteria and had the fastest median investigation time, at 54 minutes.
In a separate evaluation of Wave’s Data Science Agent, GPT‑6.1 Sol scored 67.5 out of 100, compared with 69.3 for another leading model, at a mean model cost of $1.28 versus $2.63 per dispatch. GPT‑6.1 Sol also scored higher on tool-contract compliance, estimation and uncertainty, and evidence grounding.
For high-volume work such as scanning code and running small evaluation checks, Amplitude uses GPT‑6 Luna to keep latency and cost low. Splitting work across specialist agents lets the team reserve more expensive reasoning for the tasks that need it the most.
For generating wireframes and mockups, OpenAI’s image generation model scored 80.3 out of 100 for solution wireframes, compared with 63.9 for another image generation model. Amplitude’s evaluation covered communication quality, product fidelity, instruction adherence, text and UI legibility, and visual coherence across 15 opportunities.
Customers across industries are already using Wave in beta to identify and ship product improvements. Wave analyzes session and analytics data, then develops recommendations with a proposed fix, technical plan, and acceptance criteria.
From there, teams can control the level of automation. Most teams send bug fixes straight to coding agents, while new features and bigger bets get a human review.
For changes that reach launch, the path from discovery to execution can be short: among customer-launched experiments, flags, and guides, one in four went live the same day Wave surfaced the opportunity, half in under four days, and two in three within a week.
“Our ambition with OpenAI is to make self-improving products the way companies build software,” says Skates. As OpenAI’s models get better at reasoning and coding, teams will be able to delegate more investigation and implementation work to agents, ultimately resulting in better products reaching users faster. Amplitude is already seeing it, as agents find and help deliver improvements in its own product while the team works on other priorities: “I think teams will be surprised by how much they can accomplish when their software is working alongside them to make the product better.”
