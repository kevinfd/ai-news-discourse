---
id: "5cb046ed258978e7"
title: "Five Questions That Decide If An AI Agent Works In Finance"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/14/five-questions-that-decide-if-an-ai-agent-works-in-finance"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-14T11:45:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Mitul Tiwari, Forbes Councils Member"]
language: "en"
summary: "Here are five questions to ask before deploying an agent in finance.​"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 1057
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/68823eb753baa72007a24425/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Five Questions That Decide If An AI Agent Works In Finance

Forbes · Mitul Tiwari, Forbes Councils Member · 2026-10-14

Mitul Tiwari is co-founder and CTO of Numos AI, which builds AI agents for finance teams.
Finance systems record the state of a transaction: the general ledger balance, the posted journal entry or the “paid” flag on an invoice. They capture what happened, but not the reasoning that led from one state to the next. Why was that accrual booked at $40,000 instead of $52,000? Why did the controller override an automatic bank match?
That reasoning gets reconstructed in an email the night before the board deck is due. I call this the “fragmentation tax”: the cost of re-stitching context that the ERP, bank feed and procurement tool each hold a piece of, but none hold together. Now we’re asking AI agents to exercise judgment over the close with none of that precedent in scope.
If 2025 was the year of the agent, 2026 is the year of the harness: everything that wraps a model so it can do real work, from context and tools to verification and audit trails. The question has moved from “Can the model do it?” to “Can the system around the model do it reliably with a trail an auditor would accept?”
Finance makes that question unusually hard. Coding agents have fast feedback from compilers and tests. Finance has no off-the-shelf unit test for “this reconciliation is correct.” The cost of a hallucinated number is not a broken build, but a restated earnings release. That is why finance co-pilots without a harness often follow a predictable arc: a demo that impresses, a pilot that drifts and a quiet rollback.
I’ve worked on this problem as a co-author of TapeAgents—an open-source framework built around durable records of everything an agent does—and while building a harness that runs inside live month-end finance closes. Here are five questions I would ask before deploying an agent in finance.
1. What context does the agent reason over?
Generic agents fail in finance because retrieval returns snippets, and snippets alone cannot reconcile a transaction. A finance agent needs a connected view of the underlying records: the general ledger tied to the subledger, the bank feed, and supplier and customer records. Integrations should exist not simply to move data, but to build the context the agent reasons over, including which accrual policy was applied last quarter and how a vendor’s invoices have historically been coded.
Every company can call the same frontier models. What cannot be replicated is how your close actually unfolds and how your controllers apply variance thresholds. Without that context, “explain every variance in seconds” becomes pattern matching over numbers the agent does not have enough context to interpret or trust.
2. Does it learn how your team actually works?
Modeling human intent is tempting, but intent rarely persists. Behavior does, and it leaves a structured trail across the ERP, bank feed, payables inbox and approval chain. By capturing timestamped actions—such as a bank line being matched or a journal entry being drafted—and grouping them into processes such as “month-end reconciliation,” an agent can learn when a step typically proceeds, pauses or requires escalation. This way, the standard operating procedure can emerge from observed behavior rather than being written down in advance.
3. Does it see everything, or only what the step needs?
As context windows grow, accuracy can degrade because irrelevant information competes for the model’s finite attention. In finance, that can produce confident but incorrect results.
The design goal should be progressive disclosure: surface the minimum high-signal context when it becomes relevant. An agent triaging a vendor invoice does not need the intercompany elimination policy until the entity and currency are resolved. Routing policies, accrual rules and approval thresholds can function as modular blocks of context, released by specific triggers.
4. What record does it leave, and can an auditor read it?
Engineering logs are often ephemeral, discarded once a bug is fixed. In finance, a wrong journal entry may surface in an audit six months later. The harness I use therefore gives every agent run a durable execution record, or “tape”: a structured record of the prompts it received, the reasoning and actions it produced, the tools it called, the data it observed and the actions it took. The tape becomes the agent’s persistent state, allowing a run to be paused, replayed or audited from a single record.
A durable execution record also gives finance teams a foundation for auditability and improvement. If the record captures the relevant inputs, decisions, tool calls and resulting actions, a controller can review how an agent reached an outcome rather than seeing only the final entry. Approved records can also become evaluation cases tailored to the company’s own chart of accounts and workflows, so the same underlying record can support observability, evaluation and improvement.
5. What stops it from acting when it should not?
Authorization in finance is existential, so permissions must be enforced by the system. The model can determine what it wants to do; a deterministic authorization layer determines what it is allowed to do. That means role-based access control on every endpoint and tenant scoping enforced at the data layer rather than in the prompt. Even if a model is manipulated, it cannot escalate its own privileges because the authorization layer does not rely on the model to enforce permissions.
The same separation of duties should govern generation and verification. The agent that drafts a journal entry should not also validate it against chart-of-accounts policy, period accruals and vendor history. Every action should pass verification before it reaches a system of record, while human review should remain where judgment is required rather than where routine data entry occurs. In practice, that could mean one-click approval for drafted actions, with every change reversible. Autonomous does not mean unsupervised.
Start by mapping your own close.
Before deploying an agent, ask these five questions of any system you evaluate.
Prompt engineering is tactical. Harness engineering is architectural, and it cannot be retrofitted. Models will keep improving, but a harness built for a domain where every number must be right does not commoditize.
If your finance team’s reasoning was captured today, would it be a blueprint for a self-improving close, or tribal knowledge about to be lost to the fragmentation tax?
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
