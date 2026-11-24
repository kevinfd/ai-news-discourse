---
id: "e1640428c2d67c9b"
title: "AI Agents And Ontology: Why Data Access Is Not Enough"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/24/ai-agents-and-ontology-why-data-access-is-not-enough"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/24/ai-agents-and-ontology-why-data-access-is-not-enough"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-24T11:15:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Mohan Shekar, Forbes Councils Member"]
language: "en"
summary: "AI agents are beginning to act on business meanings that organizations have not consistently reconciled across systems"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "models & research", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 790
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/69247ab789a89b497cc9d2cb/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# AI Agents And Ontology: Why Data Access Is Not Enough

Forbes · Mohan Shekar, Forbes Councils Member · 2026-11-24

Mohan Shekar is VP at SAP, driving enterprise AI adoption, with a focus on emerging computing technologies.
For decades, CIOs have managed technical debt, including aging applications and expensive workarounds. AI agents are now exposing a second liability that has built up alongside it: semantic debt. This is the accumulated cost of inconsistent business definitions and unwritten rules, the things experienced employees navigate by instinct but software cannot reliably infer.
Consider a company whose CRM marks a customer as a strategic account. Its ERP records several legal entities under that relationship. Its finance system flags an overdue invoice against one of them and an agent asked to release a delayed order can retrieve all three records. Yet retrieving those records does not necessarily answer the critical questions: Which entity signed the contract? Does that invoice block this shipment? Who can approve an exception?
If the agent guesses wrong, it could hold an order the business wanted shipped or ship one finance would have stopped. The data was available, but the meaning was not.
An Old Problem, Newly Exposed
Master data management and integration platforms have improved consistency and access for years. Conventional workflows often rely on business definitions and rules settled during design. A shipment-blocking workflow, for example, follows a predefined interpretation of a particular credit status.
Agents encounter ambiguity dynamically, across systems, while deciding what to do next. Handling an unfamiliar exception, an agent must identify the right entity, find the governing contract, interpret a credit policy and route a proposal to the right approver. Each step depends on relationships that may be familiar to an experienced employee but unclear across applications.
What has changed is that AI agents are beginning to act on business meanings that organizations have not consistently reconciled across systems. Before blaming the model, leaders should ask whether the relevant business rule, and the system authorized to define it, has been made explicit. More connectors may simply deliver conflicting answers faster.
Where Ontology Helps And Where It Doesn’t
An ontology is an explicit model of business concepts, their relationships and, where needed, their constraints. It can state that an account belongs to a legal entity, that the entity is party to a contract and that a credit policy applies to certain orders. Combined with trustworthy data, it helps establish which records and rules belong together.
But not every agent needs a formal enterprise ontology. Clean APIs, reliable data and explicit rules may be enough, and even a complex agent may gain more from repaired master data than from another modeling platform.
It helps to keep four layers distinct:
- Access: APIs and protocols such as the Model Context Protocol connect agents to data and tools.
- Reasoning: AI models interpret requests and propose steps.
- Meaning: Semantic models define the business’s terms and how they relate.
- Authority: Permissions, validation and human oversight determine what an agent may do.
An agent can understand an exception perfectly and still lack the authority to approve it. Confusing these layers is how organizations end up funding the wrong fix.
Who Owns Enterprise Meaning?
Vendors’ models encode deep domain knowledge and often work well within their own systems. The trouble is at the boundaries: An enterprise running agents across platforms cannot assume they define customer, supplier, obligation or approval the same way, or that those meanings reconcile cheaply.
CIOs can rely on each vendor’s semantics, build a centrally governed enterprise model or federate definitions across domains. Federation offers a practical starting point: Finance stays authoritative for financial obligations, sales for customer relationships and procurement for supplier classifications, with cross-domain relationships documented where agents need them. That ownership cannot sit with IT alone. Business leaders define what terms and policies mean; technology teams make those definitions accessible and testable.
Make The Business Case Small And Measurable
Start with one consequential workflow, such as order release or claims resolution, and measure how often agents select the wrong entity, miss an applicable rule, need human correction or produce a decision no one can explain.
Then compare fixes: cleaner master data, clearer APIs, deterministic rules or an explicit relationship model. Evaluate the reduction in errors alongside the cost of keeping each solution current. The goal is the lowest sustainable cost of correct business interpretation.
Making business relationships explicit is necessary but not sufficient. Once agents act on those definitions, they become operational infrastructure: They must be versioned, tested against real decisions, governed as controls and updated when policies change. An ontology nobody maintains becomes semantic debt of its own.
So beyond choosing who supplies their agents, CIOs need to decide who owns the meaning those agents rely on and whether that meaning holds when an agent crosses from one system to the next.
