---
id: "841c3ce16d85bb46"
title: "ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway"
url: "https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway"
link: "https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-03T16:47:40Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Greg Biegel"]
language: "en"
summary: "AI agents that interact with enterprise APIs on behalf of users need to maintain user identity throughout the request chain. Without identity propagation, API calls arrive at downstream services as the application itself rather than the user who initiated the action. This breaks audit trails, bypasses user-level access controls, and violates the principle of least privilege. \n Amazon Bedrock…"
tags: ["Advanced (300)", "Amazon Bedrock AgentCore", "Technical How-to"]
orgs: ["Amazon", "Microsoft"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1695
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway

AWS Machine Learning Blog · Greg Biegel · 2026-11-03

Artificial Intelligence
ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway
AI agents that interact with enterprise APIs on behalf of users need to maintain user identity throughout the request chain. Without identity propagation, API calls arrive at downstream services as the application itself rather than the user who initiated the action. This breaks audit trails, bypasses user-level access controls, and violates the principle of least privilege.
Amazon Bedrock AgentCore is a platform to build, connect, and optimize agents at scale, with any framework or model. This post shows how to configure AgentCore Gateway, a capability of Amazon Bedrock AgentCore, for an on-behalf-of (OBO) token exchange with Microsoft Entra ID. An AI agent can then call the ServiceNow REST API while preserving the calling user’s identity. You configure the token exchange on the gateway target, and AgentCore Gateway performs the exchange on each request. The pattern can be applied to other REST APIs protected by OAuth.
In production, you can additionally pair identity propagation with Amazon Bedrock Guardrails to filter harmful content and validate the agent’s inputs and outputs.
Solution overview
The architecture involves three key components connected through AgentCore Gateway:
- An AI agent application, protected by Microsoft Entra ID through an OAuth application registration.
- A Model Context Protocol (MCP) server, implemented using AgentCore Gateway, sitting between the agent and ServiceNow.
- The ServiceNow REST API, configured with an inbound OAuth integration tied to Microsoft Entra ID.
The following figure shows the end-to-end solution architecture, including components within AWS, Microsoft Entra ID, and ServiceNow.
As shown in Figure 1, the user acquires a JSON Web Token (JWT) to invoke the agent 1. The agent authenticates to the gateway with a JWT token scoped to the agent’s own application registration 2. The gateway then exchanges that token, using the OBO flow, for a new token scoped to the ServiceNow API connector, with the original user’s identity preserved 3. ServiceNow receives a valid token whose preferred_username claim maps to an existing ServiceNow user and applies that user’s permissions to the API call 4.
How OBO token exchange works in this context
When the agent calls the gateway, it presents a JWT with an audience claim matching the agent’s client ID (for example, 3ff88e17-XXXX-XXXX-XXXX-XXXXXXXXXXXX). ServiceNow, however, expects a token with an audience claim matching its own API connector client ID (5d4a7a11-XXXX-XXXX-XXXX-XXXXXXXXXXXX).
The OBO flow bridges this gap. AgentCore Gateway sends the inbound token to the Entra token endpoint along with the agent application’s client credentials, the target scope, and a parameter requested_token_use: on_behalf_of. Entra validates that the calling user consented to the delegation, then issues a new token for the ServiceNow API with the original user’s claims intact.
Prerequisites
Before you begin, you need the following:
- An AWS account with access to AgentCore Gateway.
- A Microsoft Entra ID tenant with permissions to create application registrations. Your account needs at least the Application Developer role to register applications.
- A ServiceNow instance with administrative access to configure inbound OAuth integrations. You can create a ServiceNow personal developer instance (PDI) at the ServiceNow personal developer instance signup page https://developer.servicenow.com/.
- Two Entra application registrations: one representing the AI agent, and one representing the ServiceNow API connector.
Configuring Microsoft Entra ID
Start by creating an application registration to represent the ServiceNow API connector. The following screenshot shows the application registration page for the ServiceNow API Connector in Microsoft Entra ID.
After creating, in the Overview page note the Application (client) ID.
In the navigation menu expand Manage and select Expose an API and add a scope named user_impersonation using the default Application ID URI. This scope is what the OBO flow requests when exchanging tokens. The following screenshot shows how to expose an API in Microsoft Entra ID.
Next, create an application registration for the AI agent. The following screenshot shows the application registration page in Microsoft Entra ID for the ServiceNow Agent application.
Note the Application (client) ID for the ServiceNowAgent.
Create a client secret on this registration. The gateway needs these credentials to perform the OBO exchange. The following screenshot shows how you can create a client secret on the ServiceNow Agent application registration in Microsoft Entra ID.
Then configure the agent application to have API permissions to call the ServiceNow API connector application. The following screenshot shows the API permissions that you need to configure on the ServiceNow Agent application registration in Microsoft Entra ID.
No changes to the Entra configuration are needed beyond what you would set up for any standard OBO integration between two applications.
Configuring ServiceNow
In the ServiceNow administrative console, navigate to System OAuth > Inbound Integrations and create a new inbound integration (Third party ID token issued by OIDC supporting identity provider). Specify the client ID from the ServiceNow API connector application registration you created in Entra. The following screenshot shows the configuration of the inbound integration in ServiceNow.
In the same screen, create a new OpenID Connect (OIDC) provider configuration and enter the OIDC metadata URL for your Entra tenant. Map the user claim to the appropriate user field. For example, if your Entra tenant places the user’s email in the preferred_username claim, map that to the Email field in ServiceNow. Clear JTI verification if your Entra tenant doesn’t include it in tokens. Entra uses an internal claim named uti on tokens it issues, which is equivalent to JTI. Consider mapping this uti claim to a jti claim to provide additional replay protection and denylisting. The following screenshot shows how to configure the OIDC provider in ServiceNow.
Finally, in the same screen, create an auth scope for the integration (for example, APIConnector). The following screenshot shows how to create a new auth scope in ServiceNow.
Limit the auth scope to the Table API, or whichever ServiceNow APIs your agent needs to access, as shown in the following screenshot.
After this configuration is complete, ServiceNow accepts authorization tokens with an audience of your API connector’s client ID and resolves the calling user from the preferred_username claim.
Configuring AgentCore Gateway
With Entra and ServiceNow configured, you can now set up AgentCore Gateway to handle the OBO exchange natively.
Step 1: Create an outbound auth configuration
Create a new outbound auth configuration (choose Build > Identity > Add Outbound Auth > Add OAuth client) in AgentCore and select Customized provider. Enter the client ID and client secret from your agent application registration, along with the Entra discovery URL as shown in the following screenshot.
Expand Additional configurations and select JWT authorization grant as shown in the following screenshot. This tells the gateway to use a JWT-based grant type for token exchange.
Step 2: Create the gateway with MCP version 2025-11-25
Create a new AgentCore Gateway (Build > Gateways > Create gateway). When defining the gateway details, expand Additional configurations — optional and select MCP version 2025-11-25 as shown in the following screenshot. This version is required for native OBO support. You can’t turn on native OBO for gateways created with earlier MCP versions.
Configure the inbound identity using your agent’s application registration (select Use existing identity provider configurations), as you would for any gateway that accepts Entra-authenticated requests.
Under JWT Authorization Configuration add the Application ID we documented earlier for the ServiceNowAgent as shown in the following screenshot.
Step 3: Add a target with token exchange
Add a target to the gateway pointing to your ServiceNow REST endpoint. Define the schema inline. For example, to expose a tool called ListIncidents that calls the ServiceNow Table API, you can use the following OpenAPI specification (replace the server URL with that for your PDI).
The following screenshot shows how to configure the REST API target in AgentCore Gateway with the OpenAPI schema.
For the Outbound Auth configuration on the target, select OAuth as the outbound identity provider and choose the outbound auth configuration you created in Step 1.
Now expand the Additional configurations section and select Token exchange grant. Configure the following:
Scope: api://5d4a7a11-xxxx-xxxx-xxxx-xxxxxxxxxxxx/user_impersonation
This is the scope you exposed on the ServiceNow API connector application registration in Entra.
Custom parameter (key-value pair): requested_token_use:on_behalf_of
This parameter is critical. Without it, Entra doesn’t perform the OBO exchange and the call to ServiceNow fails with an authentication error.
The final configuration is shown in the following screenshot.
Step 4: Save and test
Save the target configuration. AgentCore Gateway now automatically exchanges inbound tokens for valid ServiceNow tokens, preserving user identity, with no custom code.
When an agent calls the gateway, the following happens transparently:
- The gateway receives the agent’s JWT (audience: agent client ID).
- The gateway sends the token to Entra’s token endpoint with the OBO grant type.
- Entra issues a new token (audience: ServiceNow API connector client ID) with the original user’s claims.
- The gateway forwards the request to ServiceNow with the exchanged token.
- ServiceNow resolves the user from the token and applies their permissions.
The following code snippet shows a minimal chat agent that interacts with ServiceNow through the MCP server.
Troubleshooting
If you receive authentication errors from ServiceNow, verify that:
- The preferred_username claim in the exchanged token maps to a valid user email in ServiceNow.
- The auth scope on the ServiceNow inbound integration permits access to the API endpoints your agent is calling.
- The agent application has API permissions to the ServiceNow API connector application in Entra.
Cleaning up
To avoid ongoing charges, delete the following resources if you created them for testing:
- The AgentCore Gateway and its targets.
- The outbound auth configuration.
- The Entra application registrations (if created specifically for this walkthrough).
- The ServiceNow inbound integration and OIDC provider configuration.
Conclusion
The native OBO support in AgentCore Gateway removes the need for custom AWS Lambda interceptors to perform token exchanges. You configure the token exchange directly on the gateway target, and the gateway handles it transparently on every request. This approach maintains user identity across the agent-to-API chain, supports ServiceNow’s user-level access controls, and eliminates custom code that would need to be maintained separately.
To get started with AgentCore Gateway, see the Amazon Bedrock AgentCore documentation. For more on Microsoft Entra’s OBO flow, refer to the Microsoft identity platform documentation.
