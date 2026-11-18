---
id: "2c0a64e08e41f662"
title: "Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads"
url: "https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads"
link: "https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-17T22:44:51Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Pallav Gupta"]
language: "en"
summary: "As enterprises build production agents with dozens of tools and large structured inputs, token consumption and latency become the primary blockers to a good user experience. When these agents process large JSON data, every additional tool invocation injects the full payload into the large language model (LLM) context window, causing token usage and response latency to spike. Over multi-turn…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Customer Solutions"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 2129
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads

AWS Machine Learning Blog · Pallav Gupta · 2026-11-17

Artificial Intelligence
Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads
As enterprises build production agents with dozens of tools and large structured inputs, token consumption and latency become the primary blockers to a good user experience. When these agents process large JSON data, every additional tool invocation injects the full payload into the large language model (LLM) context window, causing token usage and response latency to spike. Over multi-turn conversations, this pressure compounds, driving up costs and degrading response quality. Effectively managing context-window pressure in agentic systems is key to reliability and responsiveness at scale. In this post, we share three composable strategies we used to build a production agent for Flightscape that handles 20 MB+ JSON payloads. You can apply them to reduce token costs, lower latency, and maintain full reasoning capability across extended sessions. Together, these optimizations reduced token consumption by up to 71% and cut average latency by up to 80% across our benchmark runs on a representative 23 MB payload.
Solution overview
Flightscape is an airline operations platform that helps airlines plan and manage their crews, flights, and operations. As part of Flightscape’s crew management capabilities, we built a Training Schedule Optimization agent that verifies crew training schedule assignments against business rules. With 40+ tools and JSON inputs in megabytes, this agent could answer complex queries across crew assignments, scheduling, and resource allocation. Although the agent delivered the required functionality, average request latencies exceeded 15 seconds across most calls. Every tool call injected its full payload into the model context, inflating token counts and costs. On larger datasets, the context window filled up before the agent could finish reasoning. The following diagram (Figure 1) details the agentic architecture and data flow:
In Figure 1, the Optimizer receives a Request JSON and produces a Response JSON, which is then validated by a Business Rules Validator to generate a Validation Report JSON. All three JSON documents are ingested by an AI Agent that provides a conversational interface for users to query optimization results, understand validation errors, and explore scheduling assignments. The agent is built with LangGraph, an open source framework by LangChain, and runs on Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale, with any framework or model. Amazon Bedrock Guardrails can be applied to validate and filter the agent’s conversational responses, helping facilitate responsible AI practices in production deployments. We defined a custom agent state that holds the data needed by our tools: optimization request JSON, optimization response JSON, and validation report JSON. We also added basic statistics and cache data to state for rich queries. The agent uses an Amazon Bedrock model for reasoning and Amazon Bedrock AgentCore memory, a capability of Amazon Bedrock AgentCore, to persist chat interactions across turns, and each turn follows this flow (Figure 2):
This is what the state structure looks like. The state references TOPT (Training Optimizer) request and response objects, which represent the crew scheduling inputs and optimization results:
Note: This state originally held heavy payloads inline. Later sections explain how we moved large artifacts out of conversational context to reduce token usage.
We implemented three strategies to reduce the token costs, latency, and memory overhead caused by passing large JSON payloads through the model context. The following diagram (Figure 3) shows how the three strategies fit into a single agent turn. Strategy 1 runs at the start and end of each turn, and Strategies 2 and 3 run each time a tool returns a result.
At the start of a turn, the hydrate_state() function restores lightweight session state from AgentCore memory. When a tool returns an oversized list or dictionary, the agent stores the full result in Amazon Simple Storage Service (Amazon S3) and passes the model a compact summary with a handle. The model can then retrieve more detail with get_result_page_tool(). At the end of the turn, the dehydrate_state() function writes heavy payloads to the S3ArtifactStore and saves only references to AgentCore memory. The following sections describe each strategy in detail.
Prerequisites
To implement these strategies, make sure the following are in place:
- An AWS account with access to Amazon Bedrock and a supported model.
- An Amazon S3 bucket for artifact storage.
- Amazon Bedrock AgentCore with Amazon Bedrock AgentCore memory enabled for session-state persistence.
- A LangGraph-based agent (or equivalent graph-orchestration framework) with tool-calling support.
- A Python 3.12+ environment with boto3, langchain-core, and langgraph.
Optimization strategies
The companion code is available in this GitHub repository.
Strategy 1: Persist lightweight session state, offload heavy artifacts
Our first optimization was to change how we persist session state. Initially, large payloads were being stored too close to the conversational state. We therefore moved heavy artifacts (request JSON, response JSON, validation data, and other large derived payloads) to Amazon S3. AgentCore memory then persists only stable references to these objects, keeping the session state lightweight.
To support this, we introduced a dedicated persisted-state schema that keeps only lightweight fields and artifact references. The live graph state still includes parsed domain objects for tool execution, but persistence now writes a dehydrated form. At runtime, tools hydrate heavy payloads on demand using those references, instead of loading everything on every turn.
This PersistedState schema is what gets written to AgentCore Memory:
The updated GraphState mirrors these references alongside the live domain objects:
The dehydrate_state function strips heavy payloads from the live state and returns the lightweight persisted form along with the artifacts to upload:
Rehydration reverses this process. When a session resumes, we rebuild the live graph state: deserialize LangChain messages, re-parse raw payloads into domain objects, and restore every reference key so later turns can locate their artifacts:
Both dehydration and rehydration rely on the artifact store returning a consistent reference for each payload. Instead of minting a random key, we derive the reference from the payload itself. This approach, known as content addressing, serializes the JSON with sorted keys and compact separators, and uses the SHA-256 digest of those bytes as the reference.
The _content_hash helper produces a deterministic SHA-256 reference from a JSON-serializable payload:
Content addressing makes writes idempotent. Identical payloads map to the same key, so a turn that re-serializes an unchanged request JSON reuses the object already in the bucket instead of uploading it again. The S3-backed store exposes a put_json and get_json interface. It also keeps a small in-process cache, so payloads already read or written during the current invocation do not require a second S3 round trip.
The S3ArtifactStore class wraps the put_json/get_json interface with an in-process cache and content-addressed keys:
Offloading heavy artifacts to S3 and persisting only lightweight references reduced per-turn latency and the volume of data stored in AgentCore memory. With heavy payloads no longer persisted inline, tool-call responses became the dominant consumer of context tokens, prompting us to introduce result paging.
Strategy 2: Page large result lists on demand
Even after moving heavy payload persistence to Amazon S3, we still had a major token bottleneck at tool-response time. Many tool results were too large, which created two problems. First, we were sending full lists to the model even when it only needed a small subset, making each turn slower and more expensive. Second, those full list payloads were injected into context, which quickly consumed the context window over multi-turn conversations.
In some cases, a single tool response exceeded 80,000 tokens, and the cost compounded as users continued interacting with the agent. We wanted to preserve full data access without sending everything by default. To solve this, we introduced on-demand result paging for large tool outputs. Instead of returning full lists, tools now return a compact payload with total count, a small sample, and a result handle.
When a tool result exceeds the sample-size threshold, the full list is stored in S3 and only a compact summary is returned to the model:
The handle points to the complete result stored in S3. When the agent needs more detail, it calls a paging tool with the handle and requests only the required slice, for example using offset and limit.
The get_result_page_tool function lets the model retrieve additional slices of a stored result by handle, offset, and limit:
On-demand paging kept the full list in S3 and served only the requested slice per turn, controlling context growth and significantly reducing token usage. However, not all oversized outputs were lists. Some tools returned large dictionaries that required a different compaction approach.
Strategy 3: Compact oversized dictionary outputs
Unlike lists, dictionary outputs contain deeply nested structured data that are useful for reasoning but typically too expensive to include verbatim on each turn. We needed a compact representation that preserved structural cues while drastically cutting the token footprint.
To solve this, we introduced descriptor-based compaction for oversized dictionary outputs. Instead of returning an oversized dictionary in full, we return a compact descriptor:
- List fields are represented by count and sample.
- Nested dictionaries are summarized by key count.
- Scalar values remain inline where useful.
The full payload is stored in the artifact store, and the response includes a result handle. When the agent needs deeper detail, it uses that handle to fetch only the required data. This response format remained navigable for the model while significantly reducing unnecessary token usage.
The _oversized_descriptor function builds a compact structural summary of a dictionary payload, preserving field types and sample data without the full content:
If the serialized output still exceeds the character limit, the fallback stores the full payload and replaces the response with its descriptor:
With lightweight persisted state, on-demand paging, and dictionary compaction in place, token growth became predictable and the agent stayed responsive even on multi-megabyte datasets.
Results
To validate the impact of these three strategies, we ran the same set of questions over the same dataset against both the pre-optimization and optimized versions of the agent. We then compared token usage and latency in Amazon Bedrock AgentCore Observability (a capability of AgentCore), and observed clear improvements in both cost and responsiveness.
Across a 5-question conversation run, total token usage dropped by approximately 71%, from ~289,500 to ~82,900 tokens, while average trace latency decreased by nearly 80%, from 15.4 s to 3.1 s (Figure 4). Across 100 sample questions (Figure 5), total tokens fell from 23.6 M to 8.5 M (64%) and average trace latency dropped from 7,930 ms to 2,461 ms (69%).
The effect was most dramatic on large single-turn payloads. Table 1 breaks down the per-turn impact for the heaviest single query (listing valid crews across every validation category).
Table 1: Input, output, and latency impact
Figure 6 and Figure 7 show the corresponding trace details before and after optimization.
These gains came primarily from avoiding full payload injection into model context at every turn. Instead, the model now receives compact summaries first and fetches additional detail only when needed.
The improvement was also visible in the trace timelines: the pre-optimization turn stretched to nearly 2 minutes 46 seconds, while the optimized turn completed in about 15 seconds (Figure 9).
The changes also improved behavior in longer conversations. Context growth became more predictable across turns, and the agent remained responsive even when users asked follow-up questions over large datasets. In practice, this shifted the system from compounding token cost to a more controlled, demand-driven access pattern.
Most importantly, these gains came without sacrificing capability. Full payloads remain in artifact storage and can be retrieved through handles whenever deeper inspection is needed. At Flightscape, this pattern provides a foundation for bringing conversational AI capabilities to complex airline operations workflows, keeping the underlying AI experience scalable and cost efficient.
Clean up
To avoid ongoing charges, delete the resources you created for this walkthrough:
- Empty and optionally delete the S3 bucket used for the artifact store, or remove all objects under the artifact prefix (for example, artifacts/).
- Delete any Amazon Bedrock AgentCore agents and associated AgentCore memory sessions created during testing.
- Remove AWS Identity and Access Management (IAM) roles and policies created for S3 or Bedrock access.
- Delete Amazon CloudWatch log groups generated by the agent runtime.
- Remove any Amazon Virtual Private Cloud (Amazon VPC) endpoints or networking resources provisioned for this walkthrough.
Conclusion
If your Amazon Bedrock AgentCore agent handles large JSON data, start by identifying which tool outputs dominate your context window. Begin with offloading artifacts to S3 (Strategy 1) because it provides the foundation for the other optimizations, then add paging (Strategy 2) and compaction (Strategy 3) as needed to improve the token usage and latency of your agents. To get started, clone the GitHub repository and adapt the strategies to your own agent. To learn more about building agents with AgentCore and LangGraph, see the Amazon Bedrock AgentCore documentation and the LangGraph framework documentation.
