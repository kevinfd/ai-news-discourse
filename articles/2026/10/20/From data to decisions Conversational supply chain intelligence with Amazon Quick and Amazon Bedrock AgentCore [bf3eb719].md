---
id: "bf3eb719b179efc5"
title: "From data to decisions: Conversational supply chain intelligence with Amazon Quick and Amazon Bedrock AgentCore"
url: "https://aws.amazon.com/blogs/machine-learning/from-data-to-decisions-conversational-supply-chain-intelligence-with-amazon-quick-and-amazon-bedrock-agentcore"
link: "https://aws.amazon.com/blogs/machine-learning/from-data-to-decisions-conversational-supply-chain-intelligence-with-amazon-quick-and-amazon-bedrock-agentcore"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-20T17:52:50Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Vineet Kachhawaha"]
language: "en"
summary: "Giving supply chain teams direct access to the systems behind their decisions. \n Every supply chain generates constant signals: orders in approval, shifting lead times, slowing ports, drifting prices, disruptions. The problem isn’t scarce data. It’s the distance between the data and the decision-maker. \n Answering “which top-revenue SKUs are exposed to the current port closure, and what will it…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Amazon Quick Suite", "Technical How-to"]
orgs: ["Amazon", "Oracle"]
topics: ["agents & coding", "models & research", "business & funding", "search & media"]
content_source: "fulltext"
word_count: 2349
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# From data to decisions: Conversational supply chain intelligence with Amazon Quick and Amazon Bedrock AgentCore

AWS Machine Learning Blog · Vineet Kachhawaha · 2026-10-20

Artificial Intelligence
From data to decisions: Conversational supply chain intelligence with Amazon Quick and Amazon Bedrock AgentCore
Giving supply chain teams direct access to the systems behind their decisions.
Every supply chain generates constant signals: orders in approval, shifting lead times, slowing ports, drifting prices, disruptions. The problem isn’t scarce data. It’s the distance between the data and the decision-maker.
Answering “which top-revenue SKUs are exposed to the current port closure, and what will it cost?” used to mean knowing which system held each piece and stitching them together by hand while the domain expert waited.
Could that manager instead ask in plain language and get an actionable, cross-system answer in seconds? Amazon Bedrock AgentCore is the intelligence layer, exposing enterprise Model Context Protocol (MCP) servers as a composable tool layer. Amazon Quick turns that into action for personas with no setup. Answers come from live systems of record and grounded documents, not model recall, and every change waits for a named human. In this post, we walk through this pattern end to end, from a conversational walkthrough in Amazon Quick to the AgentCore tool layer behind it, and we show you how to deploy it yourself.
The problem: Data-rich, insight-poor
Each question needs its own tool: inventory from the enterprise resource planning (ERP) system, disruptions from email or news, a request for quotation (RFQ) from procurement, and compliance from a checklist. Correlating is manual.
A day in the life
A manager’s morning traditionally spans the ERP (inventory exceptions), monitoring tool (alerts), procurement (alternatives), email (RFQ), and a tracker: 45–60 minutes across five systems with a dozen-plus context switches.
Conversationally it’s three prompts in one tool, “Any critical disruptions affecting my top-revenue SKUs?” → “Assess the TechComp halt and issue an emergency RFQ to approved alternatives” → “Looks good. Send it.”, in minutes.
Deep dive: Supply chain scenario walkthrough
The following five steps follow one disruption from detection to an approved emergency RFQ, all in a single Amazon Quick conversation.
Step 1: Discovery – “What tools do I have?”
The user asks “What supply chain tools do I have?” and Amazon Quick lists the supply chain MCP servers published in AWS Agent Registry. Because an administrator has turned on the registry integration, the four business MCP servers already appear as connector cards, with connection details pre-populated and no URLs to enter by hand. The orchestration agent is added as its own MCP connector.
Step 2: Querying – “Show me active disruptions”
“Check active supply disruptions” calls the Disruption Alerts MCP (assess_disruption_impact): three disruptions with severity, region, and SKU counts. How we solve it: Quick routes the request through AgentCore to the MCP server, which queries backend monitoring and returns a structured result, no dashboard or export.
Step 3: Drill-down – “Assess the critical one”
The user opens the TechComp Production Halt. assess_disruption_impact(disruption_id="DISR-002") correlates order, customer, and inventory data: $750K at risk, 23 orders, three days of supply. How we solve it: one MCP tool call fans out across systems of record, so the manager gets a consolidated impact read without touching the ERP.
Step 4: Action – “Get mitigation recommendations”
The user asks for mitigation. recommend_mitigation(disruption_id="DISR-002") chains the Governance MCP (verify approved alternatives) and Quoting MCP (contract-aligned quote), one flow from one request. How we solve it: the agent plans and sequences the calls, so a single ask spans disruption, governance, and quoting with no manual hand-offs.
Step 5: Automated follow-up
The user then sets up proactive monitoring (“Alert me every morning if there’s a new critical disruption”). The same flow can run unattended from an inbound supplier email. How we solve it: the same agent and tools run on a schedule or email trigger, posting review-ready cards to the Activity Feed for a person to approve.
Put end to end, those five steps are a single runtime sequence:
Solution architecture
That’s the experience. Here’s how it is built: the pattern separates the intelligence layer from the interface layer, so each evolves independently, with Amazon Quick as the interface and AgentCore as the intelligence.
Amazon Bedrock AgentCore: The intelligence layer
Amazon Bedrock AgentCore is a modular agentic platform for building, deploying, and operating agents securely at scale. It offers more than we use here. Four of its services are relevant to this pattern:
- Runtime – Serverless hosting for MCP servers and agents, with session isolation and built-in identity.
- Gateway – Turns APIs, AWS Lambda functions, and services into MCP-compatible tools behind a secure managed endpoint, standardizing tool access. Reasoning is the calling agent’s.
- Identity – Authentication and credential management, compatible with existing identity providers.
- Policy – Deterministic authorization rules, authored in natural language or Cedar, that intercept every tool call before execution, keeping an agent in its lane on procurement and financial data.
The MCP protocol: How tools communicate
MCP is an open standard for how AI models interact with external tools. Each server exposes tools with typed parameters:
This means:
- AI clients (Quick, custom agents, other MCP apps) can consume the same servers.
- Backends (SAP, Oracle, custom microservices) can be wrapped as an MCP server.
- Tool discovery is automatic. Clients query the registry for schemas at runtime.
AWS Agent Registry: The discovery layer
The registry is the governed discovery layer: a publisher submits a record, a curator approves it, and only then is it discoverable through hybrid search, browsing, or the registry’s MCP endpoint. One scale reality worth noting: because schemas are discovered at runtime, treat each as a contract, versioning new alongside old for breaking changes.
Multi-step orchestration
The reasoning layer is an agent on AgentCore Runtime, an agent record at its direct invocation URL through a Custom MCP connector, with no Lambda or gateway. Here, it’s the Order Fulfillment Agent. Given one request it plans which tools to call and in what order:
Security and governance architecture
Every tool call passes through the same AgentCore control set before it reaches a backend.
The MCP servers in this pattern
Amazon Quick: The enterprise AI assistant
Amazon Quick puts AgentCore tools before business users through chat, agents, the Activity Feed, and automated workflows, with no technical setup.
Key components used
Automated Activity Feed and proactive monitoring
The Activity Feed is the proactive surface of Amazon Quick, a unified inbox where agents post results, alerts, and recommendations. Feed items are:
- Actionable, each carries context and next-step actions.
- AI-triaged, with priority indicators (Reply needed, Follow up, Deadline).
- Cross-source, spanning email, schedules, agent runs, and external systems.
- Human-in-the-loop, where agents propose and humans decide.
How automated monitoring works
AgentCore tools plus the proactive capabilities of Amazon Quick give two paths, time-based and email-driven, through a common trigger → agent → output pipeline.
Use case: Validate supplier responses from email
Suppliers reply to an emergency RFQ by email with pricing. The agent validates each (approved supplier? within guidelines?) and stages the result. It does not author a quote, pick a winner, or issue a purchase order (PO).
Phase 1: Setup (one-time, approximately 5 minutes)
- Connect Outlook: in Amazon Quick, choose Settings → Connections → Add Outlook.
- Configure Activity Feed: turn on email monitoring in feed preferences.
- Create SC Agent: build an agent with these instructions:
- Create Schedule: “Every 2 hours during business hours, check for new supplier replies and validate them.”
Phase 2: Runtime (fully automated)
The feed card carries the validation results and decision-relevant facts:
Phase 3: Human-in-the-loop
The reviewer compares validated responses and either selects a supplier and issues the PO, or rejects with a logged reason. Selection and the PO stay with a person.
Use case: Proactive disruption monitoring
Schedule-triggered, the same pattern applies: a daily 8:30 AM agent checks for new critical or high-severity disruptions, assesses impact, flags anything under seven days of supply as URGENT, and posts an alert card with an Issue Emergency RFQ action.
Where this fits alongside traditional BI
This isn’t a “replace everything” argument. Dashboards remain superior for trend visualization, collaborative analysis, regulatory reporting, and exploratory analysis. Use conversational AI for real-time operational decisions and BI for strategic analysis. They complement, not compete.
Personas and use cases
One Quick Agent serves all three personas: the manager maintains continuity, procurement sources with compliance-awareness, the analyst correlates signals. Persona also bounds reach, through row/column-level security and per-persona MCP-tool scoping, so procurement does not see finance data.
Getting started
Deploying the pattern takes three phases: provision the infrastructure, connect Amazon Quick to your data and the registry, and turn on monitoring.
Prerequisites
Before you begin:
- An AWS account with Amazon Bedrock AgentCore and AWS Agent Registry.
- AWS Command Line Interface (AWS CLI) v2, AWS Serverless Application Model (AWS SAM) CLI, and Docker (the agent runs as an arm64 container).
- Python 3.12 or later, with Boto3 1.43.94 or later for the registry step.
- Active credentials with AWS Identity and Access Management (IAM) permissions to deploy and register (aws sts get-caller-identity returns the target account).
- Data layer: a database (Snowflake, PostgreSQL/RDS, or a SQLAlchemy engine), an Amazon S3 bucket, optionally a Salesforce org.
- Amazon Quick set up for your organization.
- (Optional) An Outlook account for email automation.
Setup uses two surfaces, so each of the following steps names where it happens: the Amazon Quick web console in a browser (Amazon Quick Sight permissions, Agent Registry linking, connectors, and agent settings) and the Quick Desktop App (connecting Outlook for email automation). The conversational experience in the Desktop App comes last, once setup is done.
Deploy the infrastructure
Everything is open source and scripted: clone the quick-for-supply-chain example in the aws-samples/sample-amazon-quick-suite-knowledge-hub repository and follow its README.md, or point a coding agent like Kiro at it.
The README.md covers three phases. Phase 1 deploys the AgentCore stack: the identity layer (an Amazon Cognito user pool and app client, authorization-code OAuth flow, plus a test user), four business-rule MCP servers (each an AWS Lambda function fronted by its own AgentCore Gateway, a capability of Amazon Bedrock AgentCore, using CUSTOM_JWT authorization), the gateway targets mapping the tools of each Lambda function, and sc-order-fulfillment-agent on AgentCore Runtime as a container, with least-privilege IAM roles. Phase 2 uploads the synthetic dataset to Amazon S3. Phase 3 verifies gateways and runtime are Ready. Six Agent Registry records are approved.
Grant Amazon Quick access to your data
In the Amazon Quick web console (browser): grant Amazon Quick access from the Amazon Quick Sight admin page (Manage Quick Sight → Security and permissions) to both the S3 bucket and Amazon Athena, since each table is served through an Athena source over an AWS Glue database. Without the Athena grant, dataset creation fails.
Link the registry and create connectors
Linking the registry is one-time and administrator-level. Creating a connector is per-user. Both happen in the Amazon Quick console. See the AWS Agent Registry integration guide.
Link the registry (administrator, one-time)
An administrator links one Agent Registry to the Quick account. In the Amazon Quick web console (admin): go to Manage account → Permissions → AWS Agent Registry and turn on the registry (sc-supply-chain-registry, one per account). Only registries in your account and Region, agent-registry namespace, AWS_IAM (SigV4) authorization, and READY status appear. The Quick-managed service role links it.
Create a connector
After the registry is linked, approved MCP server records become connector cards: the four business MCPs as cards, the order-fulfillment agent added manually. At scale, federate connector authentication through your identity provider and provision connectors to groups, with the Cognito user pool as the seam.
In the Amazon Quick web console (per user): the four cards appear on the Connectors page (sc-quoting-mcp, sc-governance-mcp, sc-invoice-processing-mcp, sc-disruption-alert-mcp). Authenticate through the OAuth authorization-code flow (OAUTH2_AUTHORIZATION_CODE) with client ID, secret, and token, authorization, and redirect URLs from the deploy script. Sign in as the test user, turn on tools, create and share.
Registry-sourced connectors are Custom MCP connectors (relevant for custom permissions). Removing the link later doesn’t delete connectors already created.
Add the order-fulfillment agent connector
In the Amazon Quick web console: because it is an agent record, create its connector manually (Connectors → Create for your team → Model Context Protocol → Create new): name it sc-order-fulfillment-agent, point it at the AgentCore Runtime direct invocation URL from the deploy script, complete the same OAuth sign-in, create and share.
Attach the connectors to your agent
The deployment creates the Supply Chain agent: a Quick Space, imported datasets and S3 knowledge base, and the agent with instructions, starter prompts, and welcome message. What remains is attaching the connectors.
In the Amazon Quick web console (agent settings): open the deployment-created Supply Chain agent (default id sc-supply-chain-agent) and attach all five connectors (four business MCPs plus sc-order-fulfillment-agent), or pass the five connector IDs to the setup script.
Set up proactive monitoring
To make it proactive, Quick runs the same agent on a schedule or on incoming email and posts results to the Activity Feed. Both paths reuse the agent and tools you configured.
In the Quick Desktop App (Settings → Connections): connect Outlook and turn on email monitoring. Then, in Quick Chat, create two natural-language schedules, time-based (“Every morning, check for new critical disruptions”) and email-driven (“Every two hours in business hours, check supplier replies and validate”). The agent extracts pricing, runs the checks, and posts a card.
Try it in Amazon Quick
With the agent and connectors ready, ask in natural language in Amazon Quick Chat. Each prompt shows the data-then-rules pattern.
Conclusion
AgentCore and Amazon Quick are a repeatable enterprise-AI pattern: separate intelligence from interface. AgentCore turns fragmented backends into a composable, governed, AI-accessible layer through standard MCP interfaces. Amazon Quick democratizes access in natural language.
The gain is the collapsed decision chain: detect, research, decide, act, and log once spanned five tools, now one conversation. The AI researches, correlates, validates. The person decides. Every call is authenticated, authorized, policy-checked, and audited, and a 45-60 minute routine across five systems can collapse to minutes.
That is the shift from data-rich, insight-poor to data-rich, decision-ready. Start with one MCP server and one persona. The registry grows and the experience stays the same.
