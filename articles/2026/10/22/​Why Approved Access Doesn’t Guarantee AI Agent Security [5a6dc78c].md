---
id: "5a6dc78c64dce663"
title: "​Why Approved Access Doesn’t Guarantee AI Agent Security"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/22/why-approved-access-doesnt-guarantee-ai-agent-security"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/22/why-approved-access-doesnt-guarantee-ai-agent-security"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-22T11:15:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Ofer Klein, Forbes Councils Member"]
language: "en"
summary: "That is why agent security has to move beyond one-time approval."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "safety & ethics", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 893
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6930792707d9404bcb71d276/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# ​Why Approved Access Doesn’t Guarantee AI Agent Security

Forbes · Ofer Klein, Forbes Councils Member · 2026-10-22

Ofer Klein is CEO and co-founder of Reco, a provider of agent security.
Security teams often view agent risk through a model, prompt or identity security lens. Each matters, but none captures the full problem. Enterprise agents operate inside a business ecosystem where applications, identities, permissions, workflows and data stores overlap.
Consider a support operations team that connects an agent to its ticketing, CRM, observability and collaboration systems so engineers can triage incidents faster. The agent can read customer tickets, contract terms, service logs, runbooks and escalation channels, then draft customer updates or route issues to the right team. Each permission supports the workflow and appears reasonable.
Then a major customer reports a production outage. The agent draws from these systems and drafts an update that includes unverified root-cause notes and sends the case to the wrong escalation queue. The agent did not break in. It used approved access, but its combined reach turned a support workflow into an operational risk with implications for incident response, service level commitments and customer trust.
When Approved Access Goes Too Far
This is where agent risk starts to look less like an AI problem and more like an enterprise access problem. Agents are entering through productivity suites, ticketing systems, CRM platforms, collaboration tools and developer environments, where they can inherit user permissions, use service accounts, rely on OAuth grants and call APIs.
A list of agents is only a starting point. The risk depends on where each agent operates, which identities it uses, what permissions it inherits, what data it can reach and which actions it can take. A low-profile agent connected to customer records, finance workflows and internal documents is likely to create more exposure than a widely used chatbot with limited access.
Where Routine Permissions Become Risky
OAuth grants are one place to see the problem clearly. Employees approve app connections because the request appears familiar. Over time, those grants can accumulate access to email, calendars, documents, CRM records, tickets or shared drives. When an agent uses the same grant, the risk changes. A permission originally approved for convenience can become a path for automated data retrieval or workflow action.
Service accounts and API keys create a similar challenge. They often sit outside normal employee lifecycle controls and may have broad permissions because they support integrations across multiple systems. An agent that uses one of those credentials can inherit access that no individual employee would receive. If that credential is stale, over-permissioned or poorly monitored, the agent becomes another way for hidden access to spread.
The most dangerous exposure often comes from ordinary connections that were approved separately. A meeting assistant, CRM integration, support ticket feed and shared drive permission may each be justified, but together they can let an agent combine sensitive data in a single workflow no one intended to expose.
CISOs need to view the enterprise ecosystem as the agent’s true operating environment, rather than stopping at whether an AI tool has been approved. Each agent needs a clear owner, business purpose, credential path, permission scope, data access profile and application map. Security teams also need to know which systems it can read from, which records it can change, which workflows it can trigger and which human or non-human identity gives it authority.
Access Drift Is The Real Governance Test
An agent’s risk profile evolves with the business around it. An employee may move into a new role, a third-party application may add an AI feature, a workflow may connect to another data source or an OAuth grant may remain active long after the original project ends. Any one change may seem minor, but together they can quietly expand an agent’s reach and give it more authority than the business originally intended.
That is why agent security has to move beyond one-time approval. The objective is to keep each agent’s access matched to its business purpose as roles, workflows, applications and data sources change. That means reducing permissions that exceed the agent’s job, removing OAuth grants that are no longer needed, rotating or retiring stale API keys, narrowing service accounts to the work they actually support and applying closer review before agents act inside sensitive workflows.
Agent security should be part of the broader enterprise security operating model, not a separate AI governance silo. Privacy and compliance teams require evidence when agents interact with regulated data, while identity teams must maintain ownership and lifecycle controls around service accounts. Business leaders have to know which agents can trigger operational workflows, and incident responders need a clear record of what happened, which systems were involved and how far the activity spread.
The chatbot or agent interface is where AI adoption becomes visible, but the real risk sits in the systems the agent is allowed to interact with. As agents move deeper into enterprise workflows, approval alone is too weak a standard.
Security leaders need a clear view of each agent’s business authority: the data it can reach, the records it can change, the identity behind its access, the owner accountable for its behavior and the points where that access could create exposure.
Agent security is no longer just about prompts, models or standalone tools. It is about governing what agents can actually do inside the business.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
