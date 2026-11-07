---
id: "903f3d6e677960b5"
title: "Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2"
url: "https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2"
link: "https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-06T17:09:23Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Hammad Ausaf"]
language: "en"
summary: "In Part 1 , you built a task agent on Amazon Bedrock AgentCore , a platform to build, connect, and optimize agents at scale, with any framework or model. The agent runs on Amazon Bedrock AgentCore runtime, a capability of Amazon Bedrock AgentCore, and acts for signed-in users through Okta Cross App Access (XAA). Okta decided which agent might act for which user, and Amazon Bedrock AgentCore…"
tags: ["Amazon Bedrock AgentCore", "Expert (400)", "Technical How-to"]
orgs: ["Amazon"]
topics: ["agents & coding", "policy & regulation", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 2591
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2

AWS Machine Learning Blog · Hammad Ausaf · 2026-11-06

Artificial Intelligence
Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2
In Part 1, you built a task agent on Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale, with any framework or model. The agent runs on Amazon Bedrock AgentCore runtime, a capability of Amazon Bedrock AgentCore, and acts for signed-in users through Okta Cross App Access (XAA). Okta decided which agent might act for which user, and Amazon Bedrock AgentCore Identity, a capability of Amazon Bedrock AgentCore, redeemed Okta’s grant inside the agent. That proves the governance mechanism, and it runs on a deliberately small topology: one agent, two Model Context Protocol (MCP) servers, and the authorization check written into each server.
The mechanism scales. The topology doesn’t. Three things that are fine for one agent and two tools become the work in an enterprise with hundreds of agents and thousands of tools:
In this post, you make that change on the Part 1 solution. Amazon Bedrock AgentCore Gateway, a capability of Amazon Bedrock AgentCore, becomes the single front door and redeems Okta’s grant for each target. Policy in Amazon Bedrock AgentCore evaluates Cedar policies that bind each tool to the agent and the scope Okta delegated. A second agent on Amazon Elastic Kubernetes Service (Amazon EKS) joins under its own Okta identity, to show that the front door doesn’t care where an agent runs. And Amazon Bedrock AgentCore Observability, a capability of Amazon Bedrock AgentCore, with Amazon CloudWatch gives you one place to read every decision, including Okta’s. We also compare XAA with per-user OAuth consent for applications that can’t accept Okta’s grant.
What changes from Part 1
The Okta configuration, the AgentCore Identity credential provider, and the MCP servers from Part 1 stay as they are. Figure 1 shows the architecture with the additions.
- The user signs in, and the backend for frontend (BFF) exchanges the ID token for an Identity Assertion JWT Authorization Grant (ID-JAG) issued to the task agent, agent A, as in Part 1.
- The BFF invokes agent A on AgentCore runtime with the ID-JAG.
- Agent A forwards the ID-JAG to its Gateway as the bearer token of its MCP session. The Gateway’s inbound authorizer accepts only agent A’s ID-JAGs.
- Policy in AgentCore evaluates Cedar policies for each tool listing and each tool call, before the Gateway invokes a target.
- For calls that Cedar permits, the Gateway has AgentCore Identity redeem the ID-JAG for each target at Okta’s custom authorization server through the Part 1 credential provider. A call that Cedar denies doesn’t redeem the ID-JAG.
- The MCP server checks the user’s groups and scope, as in Part 1, and records each decision as an authz.check span.
- Every hop emits OpenTelemetry spans to AgentCore Observability, which CloudWatch Transaction Search collects, and Okta streams its System Log to CloudWatch through Amazon EventBridge.
The reporting agent, agent B, runs on Amazon EKS and follows the same path through its own Gateway.
Prerequisites
In addition to the Part 1 solution, you need the following:
The additions take about 90 minutes. The EKS control plane costs $0.10 per hour, plus nodes and the Amazon EKS Auto Mode management fee, and the AgentCore features charge for what you use. See Amazon EKS pricing and Amazon Bedrock AgentCore pricing.
As in Part 1, the base for this solution is the AWS sample 08-okta-xaa-delegation-chain on GitHub, and you can build the Part 2 additions on top of it. Beyond that sample, the snippets and configurations in this post show the pattern conceptually. They aren’t a complete, deployable solution. The code is sample code for non-production use, so work with your security and legal teams to meet your organization’s security, regulatory, and compliance requirements before you deploy it.
Create a Gateway that accepts the ID-JAG
The Gateway’s inbound authorizer works like the runtime authorizer from Part 1. Its issuer is Okta’s org authorization server, its audience is the custom authorization server, and allowedClients pins it to one agent:
Figure 2 shows the resulting inbound authorizer.
Each MCP server becomes a Gateway target whose outbound authorization uses TOKEN_EXCHANGE through the Part 1 credential provider, so the Gateway performs the second exchange:
Figure 3 shows a target configured this way.
Three details matter here. First, as in Part 1, the target’s scopes must equal the ID-JAG’s. Second, give each target a static tool schema (listingMode set to DEFAULT with an inline mcpToolSchema), so the tool names your Cedar policies reference are fixed when you write them. In our tests, policies that name tools also couldn’t attach to dynamically listed targets. Third, the Gateway pages tools/list by target, so your client must follow the pagination cursor, or tools from later targets disappear. AgentCore Identity keeps the token from the Gateway’s exchange, so one single-use ID-JAG serves every tool call in a session. In our tests, it also opened a second session within its 5-minute life.
Because a credential provider authenticates as one Okta agent, give each agent its own Gateway and provider. Sample 08-okta-xaa-delegation-chain takes a different route, in which a Gateway interceptor performs both exchanges itself.
Bind tools to agents with Cedar
Attach a Policy in AgentCore engine to the Gateway in ENFORCE mode, and write permit-only policies. Cedar exposes JWT claims as tags. A policy that reads a missing tag errors and is skipped. A skipped permit grants nothing, so default deny holds, but a skipped forbid blocks nothing. Guard each tag with hasTag:
The scope tag holds the ID-JAG’s space-separated scope claim, so the four conditions match xaa:write only as a whole entry. A scope such as xaa:write-admin doesn’t match. A matching policy, written the same way, permits the read tools with xaa:read. Check that every policy is ACTIVE before you attach the engine: an engine whose policies failed to create leaves the Gateway denying every call. Cedar binds tools to the agent and its delegated scope, and the MCP server still decides each user’s authority from the groups claim, as in Part 1.
Point the agent at the Gateway
Agent A now forwards its inbound ID-JAG to the Gateway instead of calling AgentCore Identity itself:
Remove the Part 1 AgentCore Identity statements from the agent’s execution role. That’s the only change to the role, which now holds no token-exchange or secret permissions, because the Gateway’s role holds the permission to exchange tokens. Keep allowedClients on the runtime’s authorizer.
Run a second agent on Amazon EKS
Our second agent, a reporting agent, runs the same code on Amazon EKS with its own Okta registration. Its resource connection allows only xaa:read, and it has its own Gateway and credential provider. EKS Pod Identity gives the pod an IAM role that can invoke models and write its own logs and traces, and nothing else. The AWS Distro for OpenTelemetry (ADOT) SDK exports its traces. The agents-on-eks sample shows the Pod Identity setup.
Outside AgentCore runtime, no authorizer sits in front of the pod, so the agent validates the ID-JAG before a model call. It checks the signature, issuer, audience, token type oauth-id-jag+jwt, expiry, and that client_id is its own. If you kept the Part 1 agent check in the MCP servers, add agent B’s client ID to REGISTERED_AGENTS. Two settings tripped us up. The EKS Auto Mode general-purpose node pool runs only amd64, so build multi-architecture images. And the AgentCore Python SDK, a capability of Amazon Bedrock AgentCore, binds to localhost unless you set DOCKER_CONTAINER=true.
Trace every decision with AgentCore Observability
The spans in this section are AgentCore Observability, the component in Figure 1 that sits between the agents and CloudWatch. Runtime, Gateway, Identity, and Policy emit OpenTelemetry spans for each hop without code changes, after you turn on Transaction Search and trace delivery. Your own services add theirs with the AWS Distro for OpenTelemetry (ADOT). CloudWatch Transaction Search collects them, the AgentCore console reads them as agent traces, and Amazon CloudWatch Omni reads the same spans as traces.default, which is what lets one query put them beside Okta’s events.
One tool call therefore produces this chain of spans, each naming the control that made a decision:
Okta’s System Log is the one record AWS can’t emit, so you bring it in. Figure 4 shows both paths meeting in Omni.
To set it up:
- Turn on CloudWatch Transaction Search, turn on trace delivery for each Gateway (see this sample script), and add ADOT to the BFF and the MCP servers. The task manager writes each decision, the user, and the agent onto an authz.check span.
- In Okta, add a Log Stream for Amazon EventBridge. Okta delivers each event to a partner event bus in your account, and a rule writes it to a CloudWatch Logs log group. In our tests, events arrived about 1 second after Okta published them. Each ID-JAG grant event names the agent as the actor, the user as a target, and the granted scopes and resource connection.
- Set up an Omni space in the account and AWS Region, add the Okta log group to the CloudWatch Dataset integration, and save a view, view.xaa_authz_decisions, over the authz.check spans.
One query then joins each ID-JAG grant to the decisions it led to:
For Alice, the result shows Okta granting the task agent xaa:read xaa:write for her, then the MCP server denying her create_task 16.7 seconds later and allowing list_tasks after that, as Figure 5 shows.
Each request is also one trace, from the BFF through the agent, the Gateway’s identity and policy checks, and the MCP server’s decision, as Figure 6 shows. Omni marks the trace as a fault because the agent’s create_task call returned the denial.
Two instrumentation details matter. ADOT finds the Region and signs its exports through botocore, so add botocore to services that lack it. Until we did, our MCP servers exported no spans. And ADOT’s agent mode turns off instrumentation for HTTP client libraries such as requests and urllib3 by default, so set OTEL_PYTHON_DISABLED_INSTRUMENTATIONS in your BFF to override that default with a list that leaves out the BFF’s HTTP client (requests, in ours), or its trace context won’t reach the agent.
Validate the results
We ran each check through both Gateways with the users from Part 1. Each session listed the tools, then called list_tasks, create_task, and an employee lookup:
Through the deployed agents, the results matched: agent A denied Alice and Carol and created Bob’s task, and agent B told Bob it had no tool to create tasks. The same user got different authority through different agents, and Okta decided it.
These requests stopped at the front door:
The Gateway returns the same generic error for a wrong agent and for the wrong token type, so check your configuration against the token’s client_id and aud when you see it.
The Gateway’s identity and policy work is small next to the tool itself. Medians and 90th percentiles from 24 hours of Gateway A spans in Omni:
The identity and policy spans for one tool call sum to about 0.2 seconds at their medians, and the MCP server’s own authz.check span took under 1 millisecond. Gateway B showed the same pattern, with GetResourceOauth2Token at 408 milliseconds at the median.
Cross App Access or per-user consent
XAA applies where the target application’s authorization server accepts an ID-JAG. There, your Okta administrator decides which agent may act for which users, users see no consent prompt, and Okta evaluates policy each time a token is requested. Applications with their own authorization servers, such as GitHub, rely on each user’s own OAuth consent instead. Figure 7 compares the two, as we measured them.
We deployed the AWS sample 07-consent-portal-auth-code-flow-targets beside our stack, with Okta signing users in to an AgentCore Identity consent portal and a GitHub target on its own Gateway. Alice connected a GitHub test account through the portal, and Bob never connected one. The post Manage end-user OAuth consent for AI agents with Amazon Bedrock AgentCore describes this lane in full. Here’s what we observed:
The two lanes revoke differently. In XAA, Okta’s controls stop the next ID-JAG mint, and issued tokens expire within about 5 minutes. In the consent lane, Okta controls only sign-in: the stored grant outlived the suspension and stayed until we disconnected it. Choose per target application, not once for the enterprise.
Where this pattern applies
In media and entertainment, the fleet arrives quickly. A studio or streaming or games organization has agents for production tracking, title and asset metadata, rights and localization, and viewer or player support, each sitting in front of a different system with its own authorization model and its own auditors. The question isn’t whether one agent can be governed. It’s whether the hundredth one is governed the same way, and whether an administrator can still answer which agents reach which systems for which users.
Nothing here is specific to that industry. The agent is an identity in your IdP, the target is an OAuth 2.0 authorization server, and the Gateway is where authorization is decided. Teams in financial services, healthcare, and the public sector put different resources behind the same front door and get the same audit trail.
What’s next: observability and evaluations
This post uses AgentCore Observability for one purpose: to prove that each allow and deny traces back to a control. There’s more in it than that, and it’s a body of work in its own right. The spans already carry the model and tool latency behind every governance decision, Transaction Search can alert on a spike in denials, and AgentCore evaluations can score an agent’s behavior against your own criteria, online for live traffic or on demand over a chosen set of spans. A later post takes that up: what to measure on a governed agent, which evaluators catch an agent that reports success after a refused tool call, and how to run both without turning your traces into your largest bill.
Clean up
To avoid ongoing charges, delete the Part 2 resources, then follow the cleanup steps in Part 1:
- Delete the Amazon EKS cluster (eksctl delete cluster) and its Amazon Elastic Container Registry (Amazon ECR) repository.
- Delete the Gateways and their targets, then the Policy in AgentCore engines, and then agent B’s credential provider.
- Delete the CloudWatch Omni space and domain, the Dataset integration, the Amazon EventBridge rule and partner event bus, and the CloudWatch log groups.
- If you deployed sample 07, follow its cleanup steps.
- Delete the IAM roles and policies you created.
- In Okta, delete the log stream, and deactivate and delete agent B and its linked app.
Conclusion
In this post, you moved the Part 1 solution from a topology that suits a few agents and tools to one that holds up across many. The Gateway became the single front door and redeemed Okta’s grant, so the agents held no tool credentials. Cedar policies evaluated by Policy in AgentCore replaced the check copied into each server. A second agent on Amazon EKS joined under its own Okta identity. And AgentCore Observability, with Okta’s System Log beside it in CloudWatch Omni, traced each allow and deny back to the agent, the user, and the control that decided it. The governance mechanism didn’t change, which is the point: only the topology around it did.
To get started, explore the AgentCore samples and Okta’s Cross App Access documentation. For plain token exchange through a Gateway, read Implement on-behalf-of token exchange for multi-tenant agents with Amazon Bedrock AgentCore Gateway.
