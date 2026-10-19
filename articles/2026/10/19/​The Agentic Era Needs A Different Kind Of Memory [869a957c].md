---
id: "869a957c92f7234c"
title: "​The Agentic Era Needs A Different Kind Of Memory"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/19/the-agentic-era-needs-a-different-kind-of-memory"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/19/the-agentic-era-needs-a-different-kind-of-memory"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-19T11:00:00Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Gopi Duddi, Forbes Councils Member"]
language: "en"
summary: "An agent embedded in a mobile app or a field device needs to run locally and reconcile with the rest of the system once connectivity comes back."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "search & media", "robotics & autonomy", "products & launches"]
content_source: "fulltext"
word_count: 1046
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ad13e5a7560494d2b4fc81a/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# ​The Agentic Era Needs A Different Kind Of Memory

Forbes · Gopi Duddi, Forbes Councils Member · 2026-10-19

Gopi Duddi is Chief Technology Officer at Couchbase, where he leads engineering for the company’s operational data platform for AI.
There’s a pattern I keep noticing in AI infrastructure conversations lately. A vendor with a key-value store bolts on a vector index and calls it an AI database. A vendor with a caching layer does the same thing. A vendor built on a rigid relational core adds a vector extension and calls it AI-ready, too. The message is always some version of “we were already trusted, now we’re trusted and AI-ready.”
It’s a compelling pitch, but I don’t think it’s the right one.
The hard problem in agentic AI was never raw lookup speed or a familiar SQL dialect. It’s context, meaning the right operational state, conversation history, retrieved knowledge and real-time signals pulled together coherently at the exact moment an agent needs to act, whether that agent is running in a cloud data center or on a phone with a flaky connection.
What Agents Actually Need From Their Data Layer
An agent is a loop, not a single query against a single index: It retrieves context, reasons, acts, observes the result, updates its memory and retrieves again, often working across several different data shapes within the same decision cycle. An agent embedded in a mobile app or a field device needs to run locally and reconcile with the rest of the system once connectivity comes back.
That loop asks a lot of the underlying data platform: rich querying alongside retrieval, the ability to join results against operational data and filter them using real business logic in a query language developers already know and a real optimizer behind that language because agents generate queries dynamically and at volume.
Hybrid search should be native rather than stitched on. The platform should offer the flexibility to store information before deciding exactly what shape it takes, since agent context and evolving conversation state rarely arrive in a clean, predefined structure. Security and guardrails need to be built for autonomous access, while memory should persist and be governed rather than dropped at a TTL boundary. And continuity should extend wherever the agent runs, whether it is sitting next to the main database or disconnected on a device in the field.
A key-value store answers “What’s the value for this key?” about as fast as anything on earth, which is genuinely useful but more or less all it answers. A cache answers “Was this asked recently?” This is useful in its place, but it was never meant to be a system of record. A rigid relational engine answers “Here is your data, exactly as the schema you defined months ago said it should look,” which is a fine answer for a ledger and a poor one for information that didn’t exist in that shape when the schema was written.
Old Wine, New Bottle
A lot of these retrofits follow the same shape. Take an engine built for one narrow, valuable job and attach a vector index to it. The label changes. What the engine is architecturally built to do doesn’t.
That shows up in practical ways. There’s usually no real query language to reason across the vector index and the rest of the data, just a similarity search sitting next to whatever the engine already did. Where a query surface does get bolted on, there’s rarely a mature optimizer underneath, because the engine was never built around cost-based planning in the first place.
There’s usually no way for that engine to follow the agent out to a mobile app or an offline environment, because reaching the edge was never part of the original design brief. Security was designed around known human users, not an autonomous process making its own retrieval decisions. The relational retrofit has its own version of the same tension.
A schema-first design asks you to declare the exact shape of your data before a single row can be written, then treats every later change as a migration event. Agentic AI lives in the opposite world. Retrieved documents, embeddings, tool outputs and evolving conversation history rarely fit a shape anyone defined ahead of time, and the shape that works today may not be the shape a new model or tool integration needs tomorrow.
Why A Document-And-Query-Native Platform Holds Up Better Here
Imagine a JSON document database with a real query engine and optimizer built in from day one, and schema flexibility from the outset rather than added as an afterthought. That distinction has become sharper over the past five years because agentic workloads need precisely what a document-plus-query architecture was built for: reasoning across mixed, evolving data shapes at the volume of machine-generated queries, wherever the agent happens to be running.
Concretely, that looks like schema flexibility as a starting assumption rather than a bolt-on. A cost-based query optimizer doing the work developers shouldn’t have to, choosing between index scans and adapting plans as data shifts. Hybrid search that’s actually native, with vector similarity, full text, range and geospatial search queryable through SQL and planned by the same optimizer. Guardrails designed for an autonomous consumer, enforced as part of the platform rather than stitched together afterward. And that same architecture extending naturally to the edge, so an agent on a mobile device can retrieve, search vectors and reason locally, then sync peer to peer once connectivity allows.
Where This Argument Has Limits
None of this means a fast key-value store, a cache or a mature relational database is a bad choice for workloads that genuinely have a stable, well-understood shape and no need for flexible retrieval or autonomous access. Those tools are excellent at the narrow thing they do, and plenty of enterprise data will always look like that.
The point is that agentic AI isn’t that kind of workload. Its information is schemeless by nature, generated and reshaped faster than any migration process was built to handle and increasingly retrieved and acted on by something other than a human behind a known set of credentials. Bolting a vector index onto something built around a fixed, pre-declared shape and a human-centric security model doesn’t turn it into something designed for that world.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
