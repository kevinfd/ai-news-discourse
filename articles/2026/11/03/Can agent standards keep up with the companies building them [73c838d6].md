---
id: "73c838d61357194d"
title: "Can agent standards keep up with the companies building them?"
url: "https://thenewstack.io/mazin-gilbert-aaif-interview"
link: "https://thenewstack.io/mazin-gilbert-aaif-interview"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T22:50:15Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Mazin Gilbert, executive director of the Linux Foundation’s Agentic AI Foundation , left Google earlier this year to lead the new AAIF, and he recently shared with  The New Stack  a truth central to its mission: The AAIF has to move faster than its members. \n\n Gilbert , speaking in an interview at AGNTCon + MCPCon North America in San Jose last month, said on  The New Stack  podcast, “If this…"
tags: ["AI Agents", "AI Models", "Anthropic", "Podcast", "sponsor-cncf", "sponsored-podcast", "Video"]
orgs: ["Anthropic", "Google", "OpenAI", "Hugging Face", "Alibaba"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1195
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Can agent standards keep up with the companies building them?

The New Stack · Frederic Lardinois · 2026-11-03

Can agent standards keep up with the companies building them?
Mazin Gilbert, executive director of the Linux Foundation’s Agentic AI Foundation, left Google earlier this year to lead the new AAIF, and he recently shared with The New Stack a truth central to its mission: The AAIF has to move faster than its members.
Gilbert, speaking in an interview at AGNTCon + MCPCon North America in San Jose last month, said on The New Stack podcast, “If this foundation does not move at the speed of light, it becomes irrelevant.”
He also talked about how he gets OpenAI, Anthropic, and Google to agree on standards — even though they compete on products. Those companies are going to build products “with and without the standards,” he says.
All of this is happening while the foundation’s own members are often still figuring out how to build and use agents themselves. Some contribute to protocols and ship products, but others are still trying to get their agents out of the lab and into production. Gilbert says a third group of companies “frankly are panicking,” because they don’t have an agent strategy yet.
The San Jose event drew 4,300 registrants, he says, double the size of the foundation’s previous largest event in Amsterdam earlier this year.
How MCP gets built
Before our recording, Gilbert had just met with a group of maintainers from “very fiercely competing companies” who were working on the protocols together. All of those companies depend on these standards, he says, so they have a reason to get the work done.
“These protocols are the air you breathe.” 
—Mazin Gilbert, executive director, AAIF.
“These protocols are the air you breathe. These protocols are the plumbing,” Gilbert says. “They may not be that sexy, maybe, but if we don’t get those right, that entire agentic AI space will be a mess, expensive and prohibitive basically for any company to deploy this at scale.”
As an example, he points to the July release of the Model Context Protocol (MCP) specification, which made the protocol stateless. “Every one of those companies not only contributed to it, but they ended up completely updating their entire stack to the stateless MCP,” he says.
MCP downloads grew tenfold in the protocol’s first 10 months at the foundation, according to Gilbert, after Anthropic donated it last December. Today, fewer than 15 percent of its maintainers work at Anthropic, and more than 1,000 organizations contribute 75 percent of the pull requests, he says. Those contributors include U.S. retailers and companies around the world.
At the Cloud Native Computing Foundation (CNCF), many projects started at startups before they were donated. At the AAIF, Gilbert says, large companies tend to contribute the protocols, and smaller companies extend them and build businesses on top.
Some of those startups were doing something “very different” six months or a year ago, he says, and some didn’t exist yet. Now they’re building enterprise products on MCP and the foundation’s gateway projects to connect agents to companies’ back-end systems.
Getting members to contribute
The AAIF now has 305 members, and Gilbert said in his keynote that about one new company joins every business day. He calls it the fastest-growing foundation in the Linux Foundation’s history. About 40 percent of its members are startups, and 19 percent are nonprofits, national labs, and academic institutions.
“None of us have done this before, so I just want to be very clear about that. We are learning this as we go,” he says.
Part of the job is making membership worth enough that companies actively contribute. “It’s not about the money. Their time is far more valuable than their money. Their people are far more valuable than the money,” Gilbert says.
He’d like every member to contribute, but also acknowledges that’s not the case yet. He knows who does, because he uses his own agents to track contributions across the foundation.
Some companies are still trying to understand what agents can do for them and what they’d get back on the investment. Others don’t know how to contribute. Gilbert encourages them to start by joining a working group and listening, and says they don’t have to arrive as experts. For companies still learning, the foundation launched its first certification in September: the Model Context Protocol Associate (MCPA).
The Gates Foundation, which joined in September, now sits on the AAIF’s board. Gilbert says it’s helping developers in parts of Africa and South Asia get the training and certification they need to contribute, and to attend events they couldn’t otherwise afford.
Pressed on whether nonprofits and for-profit companies clash inside the foundation, Gilbert says he hasn’t seen it yet. “Whether you are a nonprofit, for-profit, small, large, your value, your impact, your power in this foundation really depends on contributions,” he says.
How many gateways do you need?
The foundation is also choosing which projects to accept. The community has submitted 65 projects through its public intake process, Gilbert says, and the AAIF has declined some. The first 10 to 20 projects “really define the DNA of this foundation,” he says.
With the four projects it announced in San Jose (Agent Skills from Anthropic, Open Responses from OpenAI, OpenEnv from Hugging Face, and OpenSandbox from Alibaba), the AAIF now hosts 10.
In some cases, the foundation is taking in technologies that are already widely adopted, like MCP and Agent Skills. In others, nobody agrees yet on what a standard should look like.
Gateways are one example. The AAIF approved two gateway projects this year, Solo.io’s agentgateway and Agent Router, which moved over from the CNCF’s Envoy project in September. Gilbert says five or six more companies want to contribute their own. Does the community need “six gateways or 10 gateways,” he asks, “or do we need to harmonize those together?”
He doesn’t have an answer yet, and says the community doesn’t either. The foundation gives those companies neutral governance to work it out together, he says.
The technical committee and governing board evaluate each proposal, including whether the AAIF is the right home for it, Gilbert says. They look at every layer of the stack, including agent frameworks, execution harnesses, gateways, guardrails, memory, protocols, observability, and identity. Not every project the foundation accepts will become the standard, he notes.
Agents that can transact
Gilbert wants the foundation to work on identity, security, trust, and observability. He also wants it to take on agent commerce.
“These agents, the internet of agents, must be transactional,” he says. An agent making a purchase would need to discover a catalog, talk to a merchant’s agent, negotiate, pay, and handle returns or disputes, and Gilbert says each step still needs a protocol.
He’s also excited about physical AI, meaning protocols for agents that talk to machines and appliances instead of databases. “Your refrigerator, your washing machines. It’s so cool,” he says. “It’s like science fiction, but it’s happening now.”
Wherever the protocols fall short, Gilbert says, companies will write custom code, and customers will end up paying to support it. A standard that arrives after a customer has built and deployed its own integration still leaves that customer with code to maintain.
