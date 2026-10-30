---
id: "e0738270a4bf2c52"
title: "The Balance Sheet Liability Of 'Mostly Right' AI"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/30/the-balance-sheet-liability-of-mostly-right-ai"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/30/the-balance-sheet-liability-of-mostly-right-ai"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-30T11:45:00Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Raju Malhotra, Forbes Councils Member"]
language: "en"
summary: "Enterprise AI doesn’t fail when it’s wrong once, but when small errors compound across workflows."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "safety & ethics", "models & research"]
content_source: "fulltext"
word_count: 920
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6a3024edee876f8f7d9746d0/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# The Balance Sheet Liability Of 'Mostly Right' AI

Forbes · Raju Malhotra, Forbes Councils Member · 2026-10-30

Raju Malhotra is Chief Product & Technology Officer at Certinia where he leads product strategy and AI innovation for professional services.
Ask any enterprise software vendor if their AI is accurate, and the answer is almost always yes. Ask what “accurate” means, and the conversation gets vague fast. A chatbot that gets something wrong 1% of the time in a consumer setting is a minor annoyance. That same 1% behaves very differently in the parts of a business that touch cash, contracts and compliance.
The Math Behind ‘99% Accurate’
Consider a mid-sized professional services firm processing 10,000 invoices a month through an AI agent running at 99% accuracy. That sounds like a strong number. It means 100 invoices a month with an error a human has to catch, correct or explain to an auditor. Multiply that across a fiscal year, and you get over 1,000 small failures sitting in the general ledger, waiting to surface at close, in an audit or in a client dispute.
The trouble starts when that response is one step in a longer process, because step-level accuracy doesn’t carry over to the whole task. It multiplies against itself. An agent that is 99.9% accurate at each step of a 20-step invoicing workflow (matching line items, flagging exceptions, routing approvals and applying the right rate card) isn’t 99.9% accurate on the finished invoice. Run the math (0.999 raised to the 20th power), and the task-level success rate drops to about 98%.
Two percent sounds small until you apply it at volume. A firm processing 10,000 invoices a month at that rate generates roughly 200 invoices a month with an error buried somewhere in the chain, more than 2,000 a year sitting in the general ledger waiting to surface at close, in an audit or in a client dispute.
And that’s the optimistic version, assuming every step in the chain holds steady at 99.9%. In practice, some steps are far less reliable than that, which is exactly why real-world deployments show failure rates no single accuracy number would predict.
The Reliability Gap In The Data
This gap between demoed capability and delivered reliability shows up in survey data, too. My company’s “2026 Global Service Dynamics Report,” based on a survey of 1,000 professional services and technology leaders, found that among organizations that have already deployed AI, only 20% describe their results as exceeding expectations. Success rates ranged from 43% among accounting, tax and audit firms to 74% among IT service providers, a 31-point spread inside the same broad technology category. The report’s explanation lines up with what shows up in the field: AI layered on top of fragmented systems and unclear ground truth inherits that fragmentation, regardless of how capable the underlying model is.
Most of the current AI conversation is still about capability: what a model can do, how fluently it reasons and how good its output looks in a demo. Reliability is a separate question, and in finance and operations, it is the one that decides whether a deployment survives contact with a real ledger. What a CFO wants to know is when the agent is wrong, why and what it costs to fix. A confident answer about capability says very little about that.
Fixing The Problem Upstream
I’ve spent years watching professional services organizations run finance, resourcing and delivery on tight margins and even tighter compliance requirements. This industry doesn’t get to round up. A misstated accrual becomes a restatement risk. An incorrectly billed project becomes a client relationship problem, and at scale, a revenue recognition problem. Every enterprise AI deployment in the back office should be held to that standard. Most vendors are still building toward something looser.
The industry’s default fix has been to bolt guardrails onto probabilistic models: a rules engine here, a review step there, a human approval gate stacked on top of both. Guardrails help, but they sit downstream of where the real problem starts. An agent making a financial decision needs to reason over the same ground truth a trained employee would use: the contract terms, the approved rate card, the project’s actual staffing history and the policy governing the exception sitting in front of it. Skip that context and no amount of review afterward closes the gap. Everything ends up getting checked by hand, which quietly defeats the purpose of automating in the first place.
“Mostly right” AI can be harder to catch than no AI at all. A person who makes a mistake on an invoice tends to make an inconsistent one, visible the moment someone looks closely. An AI agent making a systematic error at scale can repeat that same mistake a thousand times before the pattern surfaces. Putting probabilistic systems into deterministic functions without first solving for context produces exactly that kind of quiet, repeating failure.
What To Ask Before You Trust An Agent With The Ledger
Enterprise leaders evaluating agentic AI for finance, billing or resource management should stop asking vendors how accurate their AI is. Ask for the multistep number instead, and ask what ground truth the agent reasons over before it makes a call. A vendor who dodges either question is asking you to bet your balance sheet on a coin flip they never showed you.
The AI industry has spent the last three years chasing capability. The next three belong to whoever solves for reliability first. At enterprise scale, a mostly right answer carries the same balance sheet risk as a wrong one. It just comes with a much better demo.
