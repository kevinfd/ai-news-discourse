---
id: "79f378c373a2c371"
title: "How Agentic Commerce Is Rebuilding The Payment Stack"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/21/how-agentic-commerce-is-rebuilding-the-payment-stack"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/21/how-agentic-commerce-is-rebuilding-the-payment-stack"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-21T12:00:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Chuck Yu, Forbes Councils Member"]
language: "en"
summary: "Much of the economics of agentic commerce will likely be decided by how spending authority is represented, scoped and trusted.​"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["OpenAI", "Google"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 776
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/684b4691ba9ac998b49bca7b/0x0.jpg?width=960&precrop=1915%2C1077%2Cx0%2Cy87"
discussion_url: null
score: null
comments: null
community: null
---

# How Agentic Commerce Is Rebuilding The Payment Stack

Forbes · Chuck Yu, Forbes Councils Member · 2026-10-21

Chuck Yu is CEO of VGS, a trusted infrastructure powering payment tokenization and agentic commerce for the world’s leading enterprises.
Agentic commerce is often described as chatbots that make purchases. It’s something I see, hear and read almost every day. What’s actually happening is a rebuild of the payment stack: new infrastructure governing how software spends money on a person’s behalf.
That rebuild isn’t happening from scratch. It’s happening on top of the same card networks, processors and bank rails that already move most of the world’s money, just used in new ways to support a buyer that isn’t human.
This is an infrastructure race, not a product feature, and the stakes look a lot like the early build-out of digital payments.
The Problem With Giving An Agent Your Card Number
Card numbers were built for a world where a human decides what to purchase and how much to spend. That assumption breaks when an agent does the shopping.
An agent holding a raw card number is a liability. It has no built-in sense of how much it can spend, on what, with which merchants, for how long and under whose authority. It requires proper intent signals and security.
That’s why networks, processors and standards bodies are increasingly exploring payment credentials that combine tokenization with explicit authorization and intent controls. Instead of giving an agent access to a static card number, these approaches can provide a credential that is linked to the agent’s authority and subject to controls such as spending limits, transaction conditions or time constraints. The underlying payment account can remain protected while the payment system verifies whether a transaction falls within the authority granted to the agent.
This shifts the trust question. It’s no longer “Does this agent have valid card credentials?” It’s “Does this grant of authority match this specific transaction?”
Eighteen Months Of Fast, Fragmented Innovation
In the past 18 months, we’ve seen almost every major payments player ship their own agentic initiative:
• Visa launched Intelligent Commerce and the Trusted Agent Protocol.
• Mastercard launched Agent Pay, then Agent Pay for Machines.
• OpenAI and Stripe built the Agentic Commerce Protocol.
• Google introduced AP2, now under the FIDO Alliance.
• EMVCo released a draft framework for card-based agentic payments.
All initiatives are converging on a similar solution shape in months, not years. Payments don’t usually move this fast, suggesting that major players see agentic payments as both an emerging infrastructure challenge and a competitive opportunity.
Why Protocol Fragmentation May Matter Less Than It Appears
Protocols are multiplying and changing, and they probably will for the near term. Payments have a long history of parallel standards coexisting rather than resolving into a single one. But every agentic transaction still has to resolve to a credential approved by an issuer, and that layer has already proven value. For example, Visa tokens cut fraud 28% and lifted approvals 3%. Value could still go elsewhere, such as to the networks themselves, or across several layers, as EMVCo’s draft suggests.
In my experience, the most underestimated implementation problem isn’t protocol integration, but credential portability. Network tokens are typically provisioned under a specific token requestor, often the merchant’s processor, and generally can’t follow a merchant to a new provider without being re-provisioned. That friction already shapes processor decisions today. Agentic commerce multiplies it, because the same consumer authority may need to travel across several agents, merchants and rails, including stablecoins.
I think the infrastructure that issues and manages the scoped, tokenized credentials agents use to transact will be worth watching, regardless of which network or protocol ultimately dominates the interface layer above it. In a race where the layer that matters most may be the one nobody has to think about, the ability to move credentials across providers and payment environments could become an important competitive and interoperability question.
And a credential only works if issuers recognize it, which makes compatibility with existing network-supported formats an important consideration. The challenge will be balancing that existing infrastructure with the portability agentic commerce may require. A credential that can move across processors and agents while still enforcing scoped authorization, consistent fraud controls and compatibility with established network tokens could help reduce fragmentation. How the industry solves that tension—and where those responsibilities ultimately sit—may be one of the more consequential infrastructure questions in agentic payments.
The consumer-facing demos will keep getting flashier. But from my point of view, much of the economics of this shift will likely be decided one layer down, in how spending authority is represented, scoped and trusted. 
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
