---
id: "bc6b0eca02367eaf"
title: "Amex introduces a framework to prevent AI agents from making unauthorized purchases"
url: "https://techcrunch.com/2026/10/13/amex-introduces-a-framework-to-prevent-ai-agents-from-making-unauthorized-purchases"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T13:00:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Sarah Perez"]
language: "en"
summary: "American Express is introducing a new framework designed to ensure AI agents only make purchases their users have authorized, potentially preventing costly mistakes and disputes as AI-powered shopping grows."
tags: ["AI", "Commerce", "TC", "agentic commerce", "AI agents", "American Express", "amex"]
orgs: []
topics: ["agents & coding", "models & research", "products & launches", "safety & ethics"]
content_source: "fulltext"
word_count: 774
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Amex introduces a framework to prevent AI agents from making unauthorized purchases

TechCrunch · Sarah Perez · 2026-10-13

Personal AI agents are increasingly making transactions on their users’ behalf, but given the nondeterministic nature of large language models, AI bots are prone to doing what they’re not supposed to. Which, in this case, raises the possibility of AI misfiring and making unauthorized transactions.
To get ahead of this problem, American Express is introducing a new framework designed to capture and authenticate a customer’s purchase intent before an AI agent completes the transaction.
The idea is that there should be a way to ensure that the customer’s purchase instructions are carried throughout the transaction lifecycle, Amex says, from the purchase to everything that follows.
Dubbed the “Intent Intelligence Framework,” the company hopes it will become an industry standard for AI-powered transactions.
“These new transactions will have a consumer, a merchant, and an agent,” explained Amex’s VP of Agentic Partnerships and Strategy, Hannah Bozian, in an interview with TechCrunch. She said the company wanted to ensure that agentic transactions are still “seamless, trusted, and secure, the way our card members expect them to be.”
This framework’s release follows the company’s April launch of Amex’s Agentic Commerce Experiences, or the ACE Developer Toolkit, which includes a handful of services that now include the intent framework.
Amex said it has not yet seen an increase in disputes because of agentic commerce, but it wanted to be proactive in building this technology as this type of commerce scales. In part, that’s because consumers have signaled they’re open to trying agentic commerce.
In a recent Amex Trendex report, 66% of surveyed U.S. consumers said they’re likely to use AI agents to research the best price for a product or service, and 61% said they’re likely to use it for a product or service recommendation over the next 12 months, the company told TechCrunch.
To start, Amex’s new intent framework begins with a Create Intent API, which will capture the customer’s purchase instructions along with other constraints they may have included in their request, like the merchant’s name, maximum budget, and other product preferences. How this intent is collected may vary depending on the AI model involved, but the plan is to make this framework flexible enough to support all agentic commerce models, Bozian said.
The customer then authenticates their identity and signs off on the intent captured by the agent.
Then an Intent ID, a unique identifier representing the intent, is created, along with a Proof of Intent Token, which includes the customer’s high-level constraints. This token is used to obtain a secure digital payment credential that the agent will use at checkout instead of the customer’s actual credit card number. In doing so, Amex says, the purchase will remain secure while being aligned with what the customer authorized the agent to do.
This Intent ID and token can also be used in different parts of the transaction process, helping companies to manage areas like fraud prevention and dispute resolution, Amex said.
“Our approach differs from the implementations of others in that it pulls intent earlier into the transaction flow. And this is important because it helps mitigate some risk before the risk occurs,” said Bozian. She offered the example of a customer asking an agent to buy white Nike sneakers in a size 9, but the agent submits a request to purchase shoes from Adidas. In such a case, Amex could prevent the transaction from going through because the agent made a mistake.
Bozian also notes that while many agents today ask for customer consent before making a purchase, Amex foresees a future where agents may act much more autonomously in some cases. For instance, a consumer might allow their agent to re-order household staples, like paper towels or toilet paper — categories in which the only real constraint is the price and size, not merchant or brand. In these scenarios, it makes sense to have technology in the loop performing that extra check, to ensure the transactions match the customer’s intent.
Having a log of what was authorized by which agent and when could also help address fraud on behalf of the agent, she noted.
Amex is already in discussions with partners across the payments ecosystem for implementing ACE, which includes the agentic tokens that contain Amex’s payment credentials, as well as other parts of the developer kit.
The company said it plans to actively develop ACE further as the agentic commerce ecosystem evolves.
On October 13 at TechCrunch Disrupt 2026‘s Industry Stage, Amex VP of Agentic Partnerships and Strategy at American Express, Hannah Bozian, will discuss the company’s new “Intent Intelligence Framework” in more detail, and what it means for the world of agentic commerce.
