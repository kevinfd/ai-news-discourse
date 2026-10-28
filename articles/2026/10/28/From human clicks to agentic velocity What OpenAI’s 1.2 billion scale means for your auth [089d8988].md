---
id: "089d8988c52d5b40"
title: "From human clicks to agentic velocity: What OpenAI’s 1.2 billion scale means for your auth"
url: "https://thenewstack.io/openai-agentic-identity-scale"
link: "https://thenewstack.io/openai-agentic-identity-scale"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T12:00:00Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Damon Tepe"]
language: "en"
summary: "When OpenAI announced at DevDay that ChatGPT had crossed 1.2 billion weekly active users (WAUs), roughly 15% of the human population, most engineering discussions naturally centered on model context windows, compute clusters, and distributed GPU inference . \n\n However, behind every chat session, API call, and model invocation sits an equally monumental infrastructure challenge: Identity and…"
tags: ["AI Agents", "AI Infrastructure", "Security", "sponsor-ory", "sponsored-post-contributed"]
orgs: ["OpenAI", "Google"]
topics: ["agents & coding", "models & research", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 869
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# From human clicks to agentic velocity: What OpenAI’s 1.2 billion scale means for your auth

The New Stack · Damon Tepe · 2026-10-28

From human clicks to agentic velocity: What OpenAI’s 1.2 billion scale means for your auth
When OpenAI announced at DevDay that ChatGPT had crossed 1.2 billion weekly active users (WAUs), roughly 15% of the human population, most engineering discussions naturally centered on model context windows, compute clusters, and distributed GPU inference.
However, behind every chat session, API call, and model invocation sits an equally monumental infrastructure challenge: Identity and Access Management (IAM) at extreme web scale.
“Behind every chat session, API call, and model invocation sits an equally monumental infrastructure challenge: Identity and Access Management (IAM) at extreme web scale.”
Before OpenAI can serve a token from an LLM, its backend systems must authenticate the request, validate OAuth2 access tokens, inspect fine-grained permissions, and maintain secure session contexts globally. To manage this massive transaction volume without introducing latency bottlenecks, OpenAI turned to Ory, utilizing its lightweight, decoupled authentication engine and OAuth2/OIDC infrastructure.
Here is an architectural breakdown of how identity scale shifts when moving from human traffic to agent workloads, why legacy IAM platforms break at this volume, and how decoupled, edge-ready authorization handles extreme throughput.
The scale problem: human traffic vs. agentic workloads
To understand why traditional IAM platforms fail at extreme scale, consider how user authentication patterns change as architectures evolve from standard web applications to agentic AI platforms.
“When an enterprise moves from human-initiated UI clicks to autonomous AI agents… the ratio of token validations to human interactions scales non-linearly.”
When an enterprise moves from human-initiated UI clicks to autonomous AI agents (e.g., OpenAI’s Work and Codex suites), the ratio of token validations to human interactions scales non-linearly:
- Transaction velocity: A single user request to an AI agent can trigger dozens of downstream sub-tasks, database queries, and third-party API tool calls. Each step requires session verification and token introspection.
- Token introspection overhead: Legacy central identity providers (IdPs) typically validate access tokens via centralized RPCs or database lookups. At billions of requests per minute, centralized introspection introduces severe network hops and database lock contention.
- Stateless edge verification: To prevent authorization from becoming the primary bottleneck in the request path, session validation must happen synchronously at the edge using lightweight cryptographic verification (such as JSON Web Key Sets / JWKS caching) rather than stateful network calls.
Architectural comparison: modern composable IAM vs. legacy monolithic SaaS
When evaluating identity platforms for ultra-high throughput, engineering teams frequently hit performance and cost walls with traditional multi-tenant identity SaaS products (e.g., Auth0, Okta, Ping Identity).
“OpenAI wanted a partner that could help enable our vision for owning our identity processes, data, and success. We have a lot of partners, and Ory is one of our best.”
- Benjamin Billings, Engineering Manager, OpenAI (Case study)
Key infrastructure requirements for billion-user identity systems
Securing identity at scale requires a clear separation of concerns across the auth stack. Based on high-throughput deployments like OpenAI’s, modern identity architectures depend on four core principles:
1. Separation of identity state from business logic
Monolithic frameworks often bind user profiles, authentication state, and business roles together in single relational databases. High-throughput architectures decouple these responsibilities into distinct microservices:
- Identity storage & auth engines: Dedicated microservices handling identity lifecycle, credential hashing, and session management (e.g., Ory Kratos).
- OAuth2 / OIDC token issuance: High-performance OAuth2 server implementations capable of issuing signed access tokens and managing grant flows with minimal latency (e.g., Ory Hydra).
- Fine-grained access control (FGAC): Relationship-based access control engines based on Google’s Zanzibar model (e.g., Ory Keto) to evaluate tuple relationships (ObjectRelationSubject) in sub-millisecond execution times.
2. Distributed persistence across cloud regions
To support global edge routing, the underlying storage layer must support geo-distributed writes and low-latency local reads. Combining a self-hosted identity engine with distributed SQL engines (such as CockroachDB or cloud-native multi-region databases) ensures token-verification state can be replicated globally without split-brain risks or cross-continental network latency.
3. Agent security: transitioning from “enforce first” to “observe mode”
As enterprises deploy autonomous agents that execute commands on users’ behalf, writing restrictive IAM policies immediately can break workflows or cause silent failures. Modern security practices emphasize runtime observability before strict policy enforcement:
- Step 1: agent fingerprinting: Map every machine-to-machine (M2M) credential and agent service account operating across internal networks.
- Step 2: execution tracing: Audit tool usage, API invocations, and database queries initiated by autonomous runtimes.
- Step 3: identity delegation: Implement scoped OAuth2 Token Exchange (RFC 8693) to ensure agents operate under strict downscoped permissions tied directly to the delegating human user.
For a limited time, you can create a complimentary Ory account and turn on observe mode to learn how best to build enforcement.
“Scaling authentication to 1.2 billion weekly active users proves that identity is no longer just a security checkbox; it is a core distributed systems challenge.”
Scaling authentication to 1.2 billion weekly active users proves that identity is no longer just a security checkbox; it is a core distributed systems challenge.
As software shifts from human-driven UI interactions to high-velocity AI agent execution, engineering teams must evaluate whether their identity stack can handle exponential API volume. Decoupled, stateless-first identity engines offer the low latency, data sovereignty, and predictability modern platforms need to scale into the agentic era.
