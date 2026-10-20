---
id: "2979d7d30747878d"
title: "Microsoft wants to limit AI agents’ permissions when they stray from the job"
url: "https://helpnetsecurity.com/2026/10/20/microsofts-ai-agents-threats-guardian-agents"
link: "https://helpnetsecurity.com/2026/10/20/microsofts-ai-agents-threats-guardian-agents"
source: "Help Net Security"
domain: "helpnetsecurity.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-20T02:56:00Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Anamarija Pogorelec"]
language: "en"
summary: "Microsoft introduces Guardian Agents in Project Perception to monitor AI agents, detect risky behavior, restrict access, and contain threats."
tags: []
orgs: ["Microsoft", "OpenAI", "Anthropic"]
topics: ["agents & coding", "safety & ethics", "policy & regulation", "chips & infrastructure"]
content_source: "fulltext"
word_count: 812
paywalled: false
image: "http://www.bing.com/th?id=ONUT.Tx_Nwrp4Nrkaf1_UHo_N6w&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Microsoft wants to limit AI agents’ permissions when they stray from the job

Help Net Security · Anamarija Pogorelec · 2026-10-20

Microsoft wants to limit AI agents’ permissions when they stray from the job
Microsoft’s Guardian Agents in Project Perception adapt as agent activity, risk, security context and organizational policy change. They help security teams understand why risk changed, investigate relevant evidence, recommend or apply containment measures and use what they learn to strengthen policies. People retain control over objectives and consequential decisions.
Microsoft announced the Guardian Agents and new Playbooks as an extension of Project Perception, its agentic security system. Playbooks define desired security outcomes and coordinate protective actions.
Secure the agentic insider (Source: Microsoft)
Project Perception shares signals, context and a unified registry with Microsoft Agent 365, the company’s control plane for deploying, organizing and governing agents. This gives IT and security teams a consistent view of agents and associated risks, along with controls suited to their roles.
Setting boundaries for AI agents
Microsoft’s approach surrounds non-deterministic intelligence with deterministic controls, independent evidence and containment boundaries. It spans identity, permissions, data, endpoints, networks, cloud infrastructure and runtime environments.
The system has four ongoing responsibilities: know, contain, protect and adapt. Teams must identify agents, their owners, their purpose and their activity, contain their access and actions before they act, protect the resources they interact with, and adjust safeguards as context, behavior and risk change.
“Treating frontier closed and open weight models like insider risks is a way to build such a system. Not because they are necessarily malicious, but because any sufficiently capable actor with access to important systems can make mistakes or be compromised, and the architecture of containment and control must account for that,” Satya Nadella, CEO of Microsoft, wrote.
Identifying agents and tracking ownership
Microsoft Security is expanding discovery to 35 additional types of local agents, bringing the total supported to 60, including Claude Code, OpenAI Codex and GitHub Copilot. Native integrations, connectors and sensors across the security stack gather information about agents. Organizations can bring discovered agents into the unified registry to track ownership, activity and risk.
The company is extending Microsoft Entra Agent ID with identity types for additional agent patterns, including local agents and previously unknown agents discovered through security sensors. The approach gives agents identities distinct from the people using or sponsoring them.
Nadim Abdo, CVP, Identity and Network Access at Microsoft, explained that an agent can become a policy target even when it was not originally integrated with Microsoft Security. Agent identity anchors attribution, ownership, lifecycle, risk, permissions, authorization and policy, allowing organizations to distinguish a person’s actions from those an agent takes on their behalf.
Managing agent permissions and risk
Organizations need to control and monitor agents’ connections to tools, APIs, Model Context Protocol (MCP) servers, data and other agents. These controls must examine both destinations and the information exchanged, including sensitive data and untrusted instructions that could redirect an agent.
Microsoft announced Dynamic Permissions to give agents only the authority needed for an approved task, for as long as the task requires and within organization-wide policies. Those policies prevent an agent from obtaining authority its user does not have. Higher-impact actions can require verified human approval.
Agents receive their own identities and task-scoped permissions, which can shrink or expire as tasks change or end. Employees retain their existing access.
Least privilege does not eliminate risk. An agent with appropriate access could encounter a malicious instruction hidden in an external document and attempt an action outside its assigned task.
Microsoft also announced Dynamic Agent Risk, which combines signals from identity, data, endpoints, cloud, networks, runtime environments and the agent’s own activity. It considers configuration, accessible resources, potential impact and signs that an agent’s actions are drifting from the user’s or organization’s intent. The assessment updates continuously as the agent works.
Dynamic Agent Risk (Source: Microsoft)
Dynamic Conditional Access uses changes in risk to coordinate restrictions across enforcement points. Depending on policy and risk, it can preserve read access while blocking writes, narrow the data and resources an agent can reach, restrict network connections, shorten or revoke time-bound access, or require verified human approval. At the highest risk levels, it can isolate the runtime or stop execution.
For example, if an expense-processing agent encounters suspicious instructions and attempts an unrelated action, the system could remove its permission to approve expenses while preserving its ability to review them. Further increases in risk could trigger isolation or stop the agent.
“Agents will only be adopted at scale if they can be trusted at scale. At Microsoft, we are already operating in a world of hundreds of thousands of agents. As Customer Zero, we have learned that securing agents requires continuous visibility into agent activity, proactive protection of access and data, and adaptive protection that keeps pace with evolving threats. Those lessons directly inform the innovations we are delivering to help every organization adopt agents with confidence,” said Terrell Cox, CVP and Deputy CISO, Customer Security, Microsoft.
