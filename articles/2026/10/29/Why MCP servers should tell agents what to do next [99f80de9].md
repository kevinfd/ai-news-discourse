---
id: "99f80de980654e13"
title: "Why MCP servers should tell agents what to do next"
url: "https://thenewstack.io/aws-mcp-agent-observability"
link: "https://thenewstack.io/aws-mcp-agent-observability"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T15:55:39Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Matthew Burns"]
language: "en"
summary: "Many MCP servers do one thing. An agent asks for data, and the server hands it back. AWS’s James Ward thinks that leaves a lot on the table. The protocol works best, he told me, when the server acts less like a database and more like another voice in the conversation. \n\n Ward is a principal developer advocate at AWS and sits on the technical committee of the Agentic AI Foundation, the Linux…"
tags: ["AI Agents", "Model Context Protocol", "Observability", "Podcast", "sponsor-aws-marketplace", "Sponsored", "sponsored-podcast", "sponsored-premium-event-coverage", "Video"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 518
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Why MCP servers should tell agents what to do next

The New Stack · Matthew Burns · 2026-10-29

Why MCP servers should tell agents what to do next
Many MCP servers do one thing. An agent asks for data, and the server hands it back. AWS’s James Ward thinks that leaves a lot on the table. The protocol works best, he told me, when the server acts less like a database and more like another voice in the conversation.
Ward is a principal developer advocate at AWS and sits on the technical committee of the Agentic AI Foundation, the Linux Foundation group that now houses MCP. I sat down with him last week at AGNTCon + MCPCon in San Jose the day before he and co-presenter Alexander Ioffe were set to give a session on moving MCP from a basic API to an agent integration interface.
“Many times our MCP servers are just these APIs, like ‘get me the customers,’ and that is a good place to start,” Ward said. “I imagine MCP as the third person in this conversation, or a fourth or a fifth, depending on how many MCP servers you have.”
In practice, that means a tool response carries guidance with the data. It tells the agent what it just did, what it might want to do next, and where to find more.
The other half of his pitch is visibility. Web developers can trace a click on a page all the way down to the database. “MCP by default doesn’t have any way to do trace ID,” Ward said.
The workaround AWS uses is rather low-tech. Add a session ID parameter to the tools and tell the agent to pass it on every call, so individual calls can be stitched into one journey. A second parameter can carry the user’s prompt or a summary of their goal. Teams can then compare what the user wanted with the path the agent took, build an eval around it, adjust a tool description or parameter, and measure whether more tasks get completed. Ward said AWS built much of this for the MCP servers its own developers use.
In May, AWS opened its MCP Server to everyone and added Lambda diagnostics in September. In an Agentic AI Foundation profile published before the conference, Ward described an agent fetching customer records one at a time because the server only offered a one-record tool. Watching the full journey is how teams spot that pattern and build a batch tool to fix it.
Ward didn’t present MCP as the only solution. AWS also ships a CLI and skills, he said, partly because MCP’s OAuth model can’t toggle between AWS user profiles the way the CLI can. Which works best depends on the model, the tool descriptions, and how the agent discovers tools, so AWS tests them against each other with evals.
None of this is exotic, and Ward knows it. “There’s nothing new under the sun,” he said. Observe the journey, reproduce it, measure it, and improve it. The difference is that teams now have to understand the path a human and an agent take together, and test whether changes to their tools actually help them finish the task.
