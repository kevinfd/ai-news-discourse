---
id: "2c1f917f6d28499d"
title: "Your AI Agent Inventory Is Already Wrong"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/24/your-ai-agent-inventory-is-already-wrong"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/24/your-ai-agent-inventory-is-already-wrong"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-24T11:30:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Davie Sweis, Forbes Councils Member"]
language: "en"
summary: "The next time someone asks what AI is operating on your data, you want an answer that was true before they asked."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Microsoft", "Google", "Amazon", "IBM", "EU"]
topics: ["agents & coding", "products & launches", "policy & regulation", "chips & infrastructure"]
content_source: "fulltext"
word_count: 906
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6a722f31d133a295d26c7d97/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Your AI Agent Inventory Is Already Wrong

Forbes · Davie Sweis, Forbes Councils Member · 2026-11-24

Davie Sweis is Chief Data and AI Officer, Bosch Mobility, at Bosch.
Sooner or later, someone will ask you for a complete list of the AI systems operating on your company’s data, with a named owner for each one. It could be a regulator, an auditor or your security team during an incident. “We’re pulling that together” won’t be an acceptable answer.
Most companies can’t produce that list today, and I don’t think it’s carelessness. The reason is the way the list gets built.
Start with what we’re counting. An AI agent is software that takes a goal, plans its own steps and acts on them without a person approving each one. It files, routes, books and escalates. The inventory also has to cover AI features inside software you already license, which can arrive in a routine update and be making decisions before anyone has reviewed them.
These systems enter the company in three ways: Your own teams build them, they get switched on inside platforms you already license, and employees adopt tools on their own. Netskope’s 2026 Cloud and Threat Report, drawn from its customers’ network traffic, found that 47% of people using generative AI at work still do so through personal accounts. Those accounts sit outside purchasing records, and a spreadsheet won’t keep up with them.
The EU AI Act keeps its oversight, monitoring and incident-reporting duties for organizations that deploy high-risk systems, even though this year’s amendment pushed the deadlines out to late 2027 and 2028. The later dates don’t change the first step: knowing which of your systems are covered.
Security puts the same pressure on a shorter clock. In October 2026, Axios reported that third-party AI agents had been accessing customer accounts at several large U.S. banks, some acting without the customer’s instruction. Every incident asks the question those banks faced: Which agent acted, under whose authority and on what? In a business-to-business setting, where partners’ agents will increasingly act inside your systems, you can only answer it if registering an agent is part of letting it in.
So, why doesn’t the list exist? The natural place to look is the platform console, which every major vendor now ships. Each sees its own environment, and beyond it, only as far as its connectors reach. There are also products that pull records from several platforms into one view. Whether you buy one or build your own, responsibility for what the list covers, which sources are connected and what happens when a record is missing stays with you.
In the early 2000s, Universal Description, Discovery and Integration, or UDDI, promised a universal directory of web services, backed by IBM, Microsoft and SAP. The public registry closed in 2006. Web services could run without being published to it, so keeping the directory current was never a condition of deploying anything.
Kubernetes, the open-source system behind much of today’s cloud software, offers the opposite design. Once a team defines a Service—the stable address Kubernetes gives an application—the cluster publishes that name for other applications to find. There’s no separate registration step to forget.
For a large enterprise, that’s the design I would copy: Make inventory updates part of how you deploy and buy software, not a separate reporting task someone has to remember.
In practice, three feeds keep one list current:
1. Systems You Build: Put the owner and a short description in the file used to deploy the agent, and have the release process publish the record whenever the agent is created, changed or retired. Nobody fills out a separate form.
2. Software You Rent: Use the vendor’s interface or a scheduled export to collect records, backed by a contract clause requiring updates when the AI features change.
3. Everything Nobody Declared: Use your network and sign-in logs to flag AI activity that was never registered, and route the findings to someone for review. The strongest version of this feed is a gateway: If every agent’s calls to AI models pass through one point you control, that point sees every call, and if each call carries the agent’s identity, it sees every agent, declared or not.
The same feeds have to carry changes and retirements, not only new entries, and someone has to own the records that come back incomplete.
Vendors have started building parts of this. In June 2026, Google, Microsoft and other partners announced Agentic Resource Discovery, a draft specification for publishing AI capability descriptions that compatible registries can read. In August 2026, AWS made its Agent Registry generally available, with an option to detect agents on its own agent platform. The first covers publishing across organizations and the second, detection inside one platform. You still decide which sources to connect and who reviews the gaps.
The next practical step is to ask procurement and legal to add an inventory clause to upcoming software renewals, not only the ones labeled AI: The vendor provides a machine-readable list of the AI features and agents used on your data, with stable identifiers, and updates it when features are activated, changed or retired. Then have the responsible team test whether that export can create, update and retire records in your inventory.
The next time someone asks what AI is operating on your data, you want an answer that was true before they asked. Start with the next deployment and the next renewal, and make sure each one leaves a record your team can keep using.
