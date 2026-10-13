---
id: "dd106deebac2ad6f"
title: "How Postman runs Agent Mode for 40 million developers on Amazon Bedrock"
url: "https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-09T15:35:02Z"
published_date: "2026-10-09"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Srinivas Kini"]
language: "en"
summary: "Building an AI agent for a demo and operating one for 40 million developers are different engineering problems. Postman set out to build Agent Mode , an AI-native way to work across API testing , documentation , discovery, and implementation. The team expected model quality and prompt design to be the hardest problems. The deeper challenges came from integrating an agent into a mature product…"
tags: ["Advanced (300)", "Amazon Bedrock", "Customer Solutions"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "business & funding", "safety & ethics"]
content_source: "fulltext"
word_count: 2394
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How Postman runs Agent Mode for 40 million developers on Amazon Bedrock

AWS Machine Learning Blog · Srinivas Kini · 2026-10-09

Artificial Intelligence
How Postman runs Agent Mode for 40 million developers on Amazon Bedrock
Building an AI agent for a demo and operating one for 40 million developers are different engineering problems. Postman set out to build Agent Mode, an AI-native way to work across API testing, documentation, discovery, and implementation. The team expected model quality and prompt design to be the hardest problems. The deeper challenges came from integrating an agent into a mature product with years of interface-driven assumptions, a wide surface area, and specialized concepts.
In this post, Postman and AWS describe the architectural patterns that emerged while making a mature product legible to an AI agent. These patterns include controlling tool sprawl, exposing schema-based reads, and treating context rather than capability as the primary bottleneck.
We also explain how Agent Mode uses Amazon Bedrock for model flexibility, geographically scoped cross-Region inference, model-dependent zero data retention, and multi-tier prompt caching. Together, these lessons can help teams move production agents beyond prototypes.
Why Postman built Agent Mode
Agent Mode is Postman’s portal for working with the product in an AI-native way across testing, documentation, discovery, and implementation. Postman has evolved over 11 years, and developers and users learned to locate information through the interface by expanding sidebars, checking tabs, and opening requests. Re-engineering that awareness for an agent surfaced structural assumptions in the product’s APIs, user experience, and distribution of product knowledge. An agent reasons over data rather than navigating a screen. Figure 1 illustrates how Agent Mode works directly against the application.
Agent Mode runs on Amazon Bedrock, which provides managed access to foundation models behind the agent. Supporting Postman’s global developer community creates variable, latency-sensitive demand with sharp traffic bursts. With Amazon Bedrock, Postman can scale this production workload without operating its own model-serving infrastructure while retaining flexibility in model selection and control over throughput, geographic processing, and cost. Figure 2 provides a high-level view of the production architecture before the following sections examine its components.
Human oversight is part of the production design. Agent Mode requires user approval before actions that modify application state. Postman also scopes available tools to the task, selects purpose-built context, and applies model-dependent data-retention settings. These controls reduce unintended actions and unnecessary data exposure, while production testing and monitoring remain necessary. As a responsible AI control, Postman uses Amazon Bedrock Guardrails to redact personally identifiable information before it reaches the underlying large language model (LLM). Enterprise admins can turn this on in Agent Mode’s guardrail settings.
Handling tool sprawl
In Agent Mode, tools define how the agent acts inside Postman. Early on, the team leaned toward highly atomic tools: small, precise actions such as opening a request, updating one field, or fetching a specific piece of metadata. That approach supported correctness and control in early iterations, but it also revealed several problems.
Many real-world workflows require long sequences of tool calls. Even when each step was fast, the overall experience felt slow, because every action had to return to the model before the next one could begin. Users watched the agent step through actions they had mentally grouped as a single operation.
In Postman’s testing, tool-selection errors increased once the visible toolset exceeded approximately 40 tools. The agent could call nonexistent tools, pass incorrect arguments despite valid schemas, or select tools that seemed semantically reasonable but were wrong in context. Larger or newer models reduced this behavior but didn’t remove it.
Past a certain toolset size, exposing more tools can reduce agent effectiveness. The current architecture selects tools based on need and context and isolates individual execution threads. The model sees only the tools relevant to the current task. Figure 3 illustrates this dynamic selection process.
A subtler problem was that many client APIs were implicitly coupled to interface state. Tools that modified requests needed certain elements to be open, while other tools opened new tabs as side effects. The agent had to open a request tab to read it, mimicking interface interactions instead of reasoning about data. Postman is actively decoupling tools from tabs, and its Native Git feature makes extensive use of this approach. For example, Agent Mode can now send requests in the background without an open tab, although user approval is still required.
Builder takeaway: Treat your tool catalog as part of the context budget. Dynamically scope the tools exposed to the model per task, and decouple “what the agent can do” from “what the UI happens to have open.”
Exposing schema-based reads
For products such as the API Catalog, Postman consolidated multiple narrow views into a single query tool. These products expose structured data such as service uptime, test results, and endpoint response times across many services.
Given the schemas of the underlying ClickHouse tables, the agent can generate complex queries with joins and WHERE clauses. This substantially reduces the number of distinct tools needed to answer an analysis question:
With this approach, the engineering job shifts from building a tool per question to modeling the data well once. The agent can then generate a far wider variety of queries than the team could ever have enumerated as individual tools.
Builder takeaway: Where you have well-structured data, give the agent schema-aware read access to a query engine instead of a proliferation of single-purpose read tools. You trade tool count for data modeling, which produces a better scaling curve.
Context was the real bottleneck
Postman initially assumed missing tools would be the biggest blocker. In practice, missing or incomplete context caused more failures than missing capabilities.
Context is the agent’s understanding of where the user is in Postman, which entities are active, and what state has already been established. When that context was wrong or absent, even correct tools became ineffective. Figure 4 distinguishes the two forms of context supplied to the agent.
The challenge was structural. Over 11 years, developers and users learned to find information through the interface. Re-engineering that awareness for an agent required multiple iterations to determine what mattered for each workflow and what was noise. Serializing the existing interface data model did not produce useful context because those objects were shaped for rendering and data transfer, not reasoning. Postman therefore built dedicated context handlers that distilled each entity into what the agent needed to know.
As more objects gained handlers, truncation became the next problem. Many fields contain open-ended user-generated data, including request descriptions, OpenAPI specifications, and request payloads. This data can crowd the context window. Managing the context budget carefully is essential at scale and supports the filesystem-backed approach the team is exploring, where each handler does not need custom truncation and expansion logic.
Builder takeaway: Don’t feed the model your rendering data model. Build purpose-shaped context handlers and treat the context window as a scarce, actively managed budget. Noise crowds out signal long before the model reaches its limit.
Putting it all together
As Agent Mode evolved, it became clear the system had to aggregate three distinct components, each solving a different problem.
- Client-side tools live in the Postman application and represent the final actions the agent can take, such as opening requests, modifying settings, running collections, and inspecting authentication. Agent Mode also uses server-side tools for functions such as web search and agent-loop management, but most tools operate on the Postman application.
- Generic agent instructions define system-level behavior, including how proactive Agent Mode should be, how it communicates uncertainty, and what baseline product knowledge it carries.
- A knowledge base uses a Retrieval Augmented Generation (RAG) approach. Postman has a large product surface that includes multiple request protocols, mock servers, monitors, documentation, the API Network, workspace governance, variables, helpers, code generation, request settings, and collection runs.
Encoding all of this in static prompts was not feasible, and most of it is irrelevant to a given query. For initial seeding, the team used Postman’s Learning Center to generate concise feature-specific articles. At runtime, Agent Mode selects knowledge articles based on the incoming query and available context. For example, when a user selects a mock server, Agent Mode injects the related article automatically. This keeps the agent lightweight by default while providing depth when needed. The knowledge base evolves with the application, so teams can ship Agent Mode documentation with new features.
Running Agent Mode on Amazon Bedrock
The three components previously described resolve to the same runtime action: an inference call to a foundation model (FM). At Postman’s scale, traffic is bursty and developer-driven. Routing, caching, and geographic processing controls help Postman accommodate traffic bursts, manage inference cost, and address workload-specific processing requirements. Amazon Bedrock provides four capabilities that matter most here.
Model flexibility across the Claude family
Agent Mode isn’t tied to one model. Through Amazon Bedrock model inference APIs, Postman can access supported Anthropic Claude models and route each workload to an appropriate model. A faster model can serve high-volume, latency-sensitive interactions, while a larger model can handle complex reasoning where quality matters more than cost. Moving between supported Claude models is primarily a configuration change rather than a new integration. This flexibility directly supports the tool-sprawl and context challenges described earlier. In Postman’s testing, newer and larger models reduced tool hallucinations, and Postman can adopt supported models without rebuilding the integration. See supported models by AWS Region in Amazon Bedrock.
Cross-Region inference for high throughput
Developer traffic is spiky, and provisioning for peak demand in one AWS Region can be costly. Agent Mode uses Amazon Bedrock cross-Region inference to automatically route requests among the destination Regions defined by an inference profile. At runtime, the application passes the selected inference profile ID or Amazon Resource Name (ARN) as the modelId in Converse or InvokeModel. The profile, applicable AWS Identity and Access Management (IAM) and service control policies, and quotas must permit every destination Region that Bedrock might select.
- Geographic inference profiles route requests only among supported Regions within a defined geography, such as the United States or European Union. This option combines increased throughput with a configured geographic processing boundary.
- Global inference profiles can route requests among supported destination Regions worldwide to provide additional throughput during traffic bursts. They are appropriate only when the workload does not require a geographically constrained processing boundary.
Postman can select the inference profile per workload: a global profile for maximum available throughput or a geographic profile when processing must remain within the profile’s defined geography. This choice is explicit in the modelId used for each Bedrock inference request.
Data residency and enterprise controls
For enterprise customers, permitted processing geography can be as important as throughput. Geographic inference profiles constrain Bedrock routing to the profile’s supported destination Regions within the selected geography. This does not mean that inference runs inside Postman’s own AWS environment. Amazon Bedrock processes requests in the eligible AWS Regions for that profile, with data encrypted in transit and at rest. AWS states that Bedrock doesn’t use prompts and completions to train AWS models or distribute them to third parties. Postman has configured zero data retention with data_retention_mode set to none for supported Agent Mode models. Availability and behavior are model-dependent, so each production model must be checked against the current Amazon Bedrock data-protection and retention documentation.
Prompt caching to keep costs in check
A production agent resends substantial stable context on each turn, including system instructions, generic agent behavior, a core tool set, selected knowledge, and conversation context. Reprocessing the unchanged prefix on every request adds avoidable latency and cost.
Agent Mode uses Amazon Bedrock prompt caching to reuse stable prompt prefixes. The near-immutable core, including the system prompt, agent instructions, and core tool definitions, uses a one-hour cache checkpoint. More variable context uses a five-minute checkpoint that refreshes on a cache hit. Bedrock requires the longer-lived checkpoint to appear before the shorter-lived checkpoint. The shorter tier suits interactive sessions because idle context expires, while the one-hour tier can amortize its higher cache-write price across many reads. Cache benefits and supported TTLs depend on the selected model. Teams can verify behavior through the cacheReadInputTokens and cacheWriteInputTokens usage fields and measure time to first token for their own workloads.
Builder takeaway: Treat inference as a routing-and-caching problem, not only a model-selection decision. Select the Claude model per workload, choose the appropriate cross-Region inference profile, and cache the stable prompt prefix with TTLs that match how frequently each layer changes.
Best practices for scaling agents in production
Distilled from Postman’s journey, for builders working on Amazon Bedrock:
- Budget tools as carefully as tokens. Dynamically select the tools exposed per task. In Postman’s testing, tool-selection errors increased as the visible toolset became large.
- Prefer schema-aware reads over tool proliferation. Model your data well and let the agent query it.
- Decouple agent actions from interface state. If a tool requires an open tab, the agent is navigating the interface rather than reasoning directly over data.
- Engineer context deliberately. Purpose-built context handlers beat serializing your rendering model every time.
- Manage the context window as a scarce resource. Truncation and expansion strategy is a first-class design problem, not an afterthought.
- Ship docs with features. A RAG knowledge base only stays useful if it evolves in lockstep with the product.
- Route and cache on Bedrock. Match each workload to the appropriate Claude model, choose cross-Region inference based on throughput and geographic requirements, and apply tiered caching to stable prompt prefixes.
Conclusion
Building Agent Mode required Postman to confront the gap between large language model capabilities and the structure of mature products: interface assumptions, coupled clients, sprawling tool catalogs, and knowledge distributed across documentation and teams. Dynamic tool selection, schema-based reads, and deliberate context engineering emerged as repeatable patterns at the scale of Postman’s developer community. Amazon Bedrock provides the managed model access, cross-Region inference, model-dependent retention controls, and prompt caching that support the production architecture.
Whether you’re building your first agent or scaling an existing one, these patterns can help teams avoid common agent-integration and scaling challenges.
To learn more, see the Amazon Bedrock documentation, including guidance for cross-Region inference, prompt caching, and data protection and retention. For related implementation guidance, read Effectively use prompt caching on Amazon Bedrock and Amazon Bedrock announces global cross-Region inference for increased throughput on the AWS Machine Learning Blog. To explore the product, see the Postman Agent Mode documentation.
Postman’s production implementation is proprietary and isn’t available as a public sample repository.
