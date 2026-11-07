---
id: "0f0cb95e5bb05a5c"
title: "Serverless MCP server for AI agent data lake access on Amazon ECS Fargate"
url: "https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate"
link: "https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-06T17:13:13Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Aishwarya Pawar"]
language: "en"
summary: "Organizations building applications powered by artificial intelligence (AI) face a recurring challenge: giving large language model (LLM) agents access to enterprise data lakes without duplicating integration logic across every agent and application. Most teams begin by wiring agents directly to databases and APIs, with no shared gateway such as a Model Context Protocol (MCP) server in between.…"
tags: ["Amazon Elastic Container Service", "AWS Fargate", "Intermediate (200)", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "fulltext"
word_count: 2192
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Serverless MCP server for AI agent data lake access on Amazon ECS Fargate

AWS Machine Learning Blog · Aishwarya Pawar · 2026-11-06

Artificial Intelligence
Serverless MCP server for AI agent data lake access on Amazon ECS Fargate
Organizations building applications powered by artificial intelligence (AI) face a recurring challenge: giving large language model (LLM) agents access to enterprise data lakes without duplicating integration logic across every agent and application. Most teams begin by wiring agents directly to databases and APIs, with no shared gateway such as a Model Context Protocol (MCP) server in between. Each new dataset demands custom code, and each agent reimplements its own access control. As the number of datasets or agents grows, permission enforcement drifts, and onboarding a new data source becomes a multi-day engineering effort.
Our team supports Amazon’s North America Sort Center (NASC) network, where planning teams rely on operational data to manage capacity, labor, and package flow. To give those teams conversational access to that data, we built a serverless Model Context Protocol (MCP) server on Amazon Elastic Container Service (Amazon ECS) with AWS Fargate to address this problem for planning teams in NASC. The server acts as a centralized, agent-agnostic gateway between AI agents and our enterprise data lake. Exposing a new dataset requires only a JSON metadata file that the server discovers automatically on the next pipeline sync.
In this post, we describe the architecture, show how a metadata-driven approach removes the need for per-dataset integration code, and explain how the serverless infrastructure supports multiple agents and applications in a multi-tenant environment.
Problem statement and design goals
Two interrelated challenges shaped how we designed this system: fragmented data access patterns and an unsustainable onboarding model.
Integration challenge at scale
Our data lake contains thousands of datasets spanning operational metrics, business analytics, and domain-specific data. Multiple teams wanted AI assistants that could query this data conversationally, but each built its own integration from scratch. Each agent embedded its own SQL generation logic, schema knowledge, and connection handling, so a schema change meant patching every agent individually. Access control was fragmented, with no single audit point for data access decisions. Onboarding a new dataset required custom tool code, query validation, and redeployment, typically a multi-day effort per table.
Design goals
We established four requirements:
- Configuration-driven data lake access. Adding a dataset requires only a metadata file, not code.
- Agent-agnostic tool interfaces. Any MCP-compatible client can invoke the same tools.
- Centralized permission enforcement. Access control is enforced at the MCP server layer.
- Elastic infrastructure. The system scales with bursty AI workload patterns.
Solution overview
The architecture separates concerns into four layers (client, MCP server, tools, and knowledge-base refresh), each independently scalable and deployable. A metadata catalog underpins the tools layer, storing schema descriptions, column-level semantics, and table relationships that the AI agent references when generating SQL. Because the agent derives schema knowledge from the catalog at query time, there is no need to hardcode table structures or redeploy when schemas change. The knowledge-base refresh layer keeps that catalog current, indexing new dataset metadata as it arrives. The following sections describe each layer in detail.
Architecture walkthrough
The following diagram shows the request flow from user query to data layer across all four layers. A user submits a query from a client application (web chat, Slack, an IDE plugin, or an external agent). The request resolves through Amazon Route 53 for DNS and reaches an Application Load Balancer in a public subnet, configured with HTTPS and AWS WAF. The load balancer routes to Amazon Cognito, which authenticates the user and enriches the request. Authenticated traffic then enters the private subnet, where the client layer runs on Amazon ECS Fargate. This layer handles session state in Amazon DynamoDB and forwards requests through an internal Application Load Balancer to the MCP server layer, also on Amazon ECS Fargate. In the MCP server layer, an AI agent powered by Amazon Bedrock orchestrates tools built with FastMCP (a Python framework for building MCP servers). Amazon Bedrock Guardrails is applied to every model interaction. On the right, the data layer holds the tool backends. Amazon Athena and Amazon Redshift run SQL queries against the data lake, and Amazon Bedrock Knowledge Bases, the fully managed Retrieval Augmented Generation (RAG) capability, handles semantic search. Data ingestion into Amazon Simple Storage Service (Amazon S3) and the knowledge bases is handled by AWS Lambda. Each layer is described in detail in the sections that follow.
MCP client layer: Authentication and session management
A request flows from the client application through Amazon Route 53 for DNS resolution to an Application Load Balancer configured with HTTPS and AWS WAF. The load balancer forwards traffic to the Amazon ECS Fargate client service, which integrates with Amazon Cognito for JSON Web Token (JWT) authentication and Amazon DynamoDB for session storage.
A context mapping configuration drives this enrichment, scoping each query to only the relevant tables. In our testing, this scoping keeps end-to-end interaction latency in the 15–20 second range. The following example shows a context mapping configuration:
When a context specifies tables, the MCP server narrows its search of the metadata catalog to those tables, reducing noise and improving SQL generation accuracy. Adding a new business domain requires only adding an entry to this mapping.
MCP server layer: Stateless execution with conversation state
The MCP server runs on its own ECS Fargate cluster, isolated from the client layer. Requests reach it through Amazon Route 53 and an internal Application Load Balancer in a private subnet. The server handles full orchestration including query analysis, tool selection, execution, and response generation. Through the MCP protocol endpoint (/mcp), a FastMCP-powered JSON-RPC interface, external MCP-compatible clients such as Amazon Q Developer or IDE extensions can discover and invoke tools directly.
Fargate tasks are stateless with conversation state persisted in DynamoDB, so tasks can be replaced or scaled without data loss. When a request arrives, the agent retrieves session history, analyzes user intent using Amazon Bedrock, discovers and invokes appropriate tools, and streams results back to the user.
Tools layer and metadata-driven data lake access
Each tool is registered with FastMCP and discoverable at runtime:
The Athena query tools are the primary interface to the data lake. The agent first queries the metadata catalog to understand available schemas, generates an optimized SQL query through Amazon Bedrock, validates and auto-corrects the SQL for Athena compatibility, then executes it. Results flow back to the orchestrating agent for natural language synthesis.
Responsible AI controls
Amazon Bedrock Guardrails is applied to all LLM interactions and is designed to filter harmful content, enforce grounding checks, and help block prompt injection attempts. These guardrails operate as production controls at the MCP server layer, so every connected agent benefits from the same content safety policies regardless of how it connects. The Athena query tools enforce SELECT-only queries, rejecting write operations at the tool level before they reach the data lake.
Knowledge base refresh layer: Dataset onboarding with a single JSON file
The entire system is built around configuration-driven extensibility. Adding a new dataset requires a metadata JSON file describing the table and an optional context mapping entry. The file captures the table’s schema, business context, and column-level semantics. It serves as the single source of truth that the AI agent uses to understand and query the dataset:
The business_description_for_the_table field carries engine-specific query hints, such as “always use date() to wrap string literals,” that reduce SQL validation failures. The column_details field pairs each column_name [type] with a natural language description and sample values, giving the agent both schema awareness and business semantics. The sample_values field matters for accurate WHERE clause generation because the agent learns real data patterns, for instance that warehouse_id holds codes like FC-EAST-07 rather than spelled-out names like “East region facility.”
The pipeline picks up metadata files, generates vector embeddings with Amazon Titan Text Embeddings, and indexes them into Amazon Bedrock Knowledge Bases. Once indexed, the table is discoverable by all connected agents without manual re-indexing or server restarts.
To improve accuracy for specific applications, an engineer can optionally associate the dataset with a business context. This narrows the search scope, so the agent prioritizes the right tables. The following example shows a context mapping entry:
If no context is specified, the agent searches across all indexed tables. The context mapping reduces latency and improves SQL accuracy by limiting the search space. This scoping is optional and can be added at any time without modifying the metadata files themselves.
Putting it together: A query in action
When a user asks, “What were our top 10 highest-value orders last month?”, the client enriches the request with business context to narrow scope. The agent converts the question into a vector embedding, searches the metadata catalog for matching schemas, and selects the most relevant table via a lightweight LLM call.
Using the selected schema, column descriptions, and engine-specific query hints, the agent generates a SQL statement such as:
The SQL is validated and auto-corrected for engine compatibility, then executed against Amazon Athena. The agent formats the results into a natural language response and streams it back to the user. In our testing, this end-to-end flow completes within 15–20 seconds.
The same orchestration extends beyond pure SQL. Because document search is registered as another tool on the same server, the agent can answer questions that span structured and unstructured sources in a single turn, such as “What was our return rate for Q4, and what does the product team’s analysis say about the root causes?” For that request, the agent runs an Athena query for the return-rate figure and a Knowledge Bases document search for the analysis, then combines both into one response.
Security and multi-tenant access
That single-turn orchestration works only because every tool call passes through the same controlled gateway. The architecture uses layered security rather than a single enforcement point. The MCP server runs in private subnets behind an internal Application Load Balancer and is not reachable from the internet. Only the client layer, which sits behind a public-facing Application Load Balancer with AWS WAF, can route requests to it. Amazon Cognito validates user identity at the client layer, and only authenticated, token-bearing requests are forwarded downstream. At the tool level, the Athena query tools enforce SELECT-only queries, rejecting write operations before they reach the data lake. All tool invocations are logged to Amazon CloudWatch with structured JSON, which gives security teams a single audit point for data access across every agent and application. This architecture is available in the AWS Regions where Amazon Bedrock and Amazon Bedrock Knowledge Bases are available.
This centralized design is also what makes the server multi-tenant. Because the standardized /mcp endpoint accepts any MCP-compatible client regardless of which LLM or orchestration framework it uses, multiple agents share the same tools and the same access controls. Adding a new agent requires only pointing it at the server endpoint, so onboarding another team extends the system without weakening or duplicating the security model.
Serverless infrastructure and scaling
Each layer scales through a mechanism suited to its workload pattern:
Amazon ECS Fargate provides serverless compute with no EC2 instances to manage. Downstream services (Athena, Bedrock) scale automatically, so the system handles a single query or hundreds of concurrent queries without configuration changes.
Use cases and extensions
This architecture supports several patterns beyond basic question-answering. Enterprise knowledge assistants can combine data lake queries with document search to answer complex questions spanning both structured data and unstructured knowledge, such as “What’s our return rate for Q4, and what does the product team’s analysis say about the root causes?” Internal analytics copilots let business users query the data lake conversationally without writing SQL, relying on the metadata descriptions and query hints to guide the agent toward accurate, performant query patterns.
The standardized /mcp endpoint also supports multi-agent workflows. Multiple specialized agents for data analysis, document retrieval, and operational alerting can share the same MCP server, each accessing the full tool suite through a common protocol. Onboarding a new team’s data follows the same configuration-driven pattern. They add a metadata JSON file, and within one pipeline sync cycle their dataset is discoverable by every connected agent and application.
Conclusion
A centralized MCP server on Amazon ECS Fargate provides a scalable, secure gateway between AI agents and enterprise data lakes. The metadata-driven approach removes the need for per-dataset integration code, and the Model Context Protocol standard means any MCP-compatible client can connect without custom adapters.
The key architectural decision is separating the tool layer from the agent layer. Agents evolve rapidly, but data access patterns should outlive any single agent implementation. Treating extensibility as a configuration problem rather than a code problem accelerates onboarding.
To learn more, see Amazon ECS on AWS Fargate, Amazon Bedrock, the Amazon Bedrock Knowledge Bases user guide, Amazon Athena, and the Model Context Protocol specification.
Next steps
We are extending this architecture in two directions. First, finer-grained access control where table owners can mark sensitive columns as restricted per permission group, and the agent automatically excludes those columns from generated SQL without prompt-level changes.
Second, closing the feedback loop so that when queries fail or produce low-confidence results, the system captures the failure pattern and surfaces targeted suggestions for improving column descriptions, adding query hints.
