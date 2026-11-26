---
id: "7cd345fb5c7ef2ad"
title: "What To Define Before Deploying AI Agents, The Newest Class Of Business Software"
url: "https://forbes.com/councils/forbesbusinesscouncil/2026/11/25/what-to-define-before-deploying-ai-agents-the-newest-class-of-business-software"
link: "https://forbes.com/councils/forbesbusinesscouncil/2026/11/25/what-to-define-before-deploying-ai-agents-the-newest-class-of-business-software"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-25T08:00:00Z"
published_date: "2026-11-25"
collected_at: "2026-11-26T13:04:05Z"
authors: ["Ihor Hamal"]
language: "en"
summary: "A chatbot generates answers. An agent acts on behalf of the company and reaches its internal data. One agent error can hit a company’s finances and its clients."
tags: []
orgs: []
topics: ["agents & coding", "safety & ethics", "models & research"]
content_source: "fulltext"
word_count: 1024
paywalled: false
image: "http://www.bing.com/th?id=ONUT.cswQ-453NP8uhf_oc6nzfg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# What To Define Before Deploying AI Agents, The Newest Class Of Business Software

Forbes · Ihor Hamal · 2026-11-25

Ihor Hamal, COO at SapientPro. Expert in automating repetitive workflows across video, image, voice, and document processing.
AI agents are leaving the experimental category and joining the standard corporate software stack. McKinsey’s latest State of AI survey puts the share of large companies scaling agents in at least one business function at 40%, up from 27% the year before.
A chatbot generates answers. An agent acts on behalf of the company and reaches its internal data. One agent error can hit a company’s finances and its clients. Before thinking about productivity, then, companies deploying agents should settle permissions, autonomy limits, oversight and accountability.
Increased Risk When Agents Can Act
OWASP guidance names a problem I keep seeing as companies bring AI into their business processes. Two of the risk sources for excessive agency it lists, excessive functionality and excessive permissions, concern what the agent can touch. The third, excessive autonomy, concerns how far it can go on its own.
An agent that only reads documents has no use for the right to edit or delete them. An agent serving one user’s data shouldn’t log in to a corporate system through a shared account that opens everyone’s records.
A wrong AI answer is an information-quality problem. A wrong AI action is a potential business incident with financial or reputational consequences.
In my experience, the decisions that shape these projects rarely concern the choice of model. Before an agent touches corporate systems, the company has to decide what it can see and change and which of its actions need human sign-off. Someone also has to own the consequences.
Rules For Implementing AI Agents In Business Processes
In practice, it comes down to one question: how to fit an agent into a business process so that its capabilities match the task and the level of responsibility involved. Here are the main principles.
Define permission boundaries before choosing the model.
Before development starts, draw a permission map for the workflow. It should show what the agent can read and change, plus the tools and actions available to it. Forbidden operations deserve a separate list, as do those needing a manager’s confirmation.
A customer support agent reads ticket history and looks up orders to draft a reply. None of that implies a need to issue refunds or change prices, let alone edit contracts or delete customer data.
Under the principle of least privilege, an agent receives only the rights its scenario requires; however many more the platform could grant.
Keep passwords and keys out of agents’ reach.
In my view, popular open-source agents have a weak design when it comes to protecting API keys and MCP credentials. In many setups, these secrets live in a file the agent can open, guarded by nothing more than an instruction to leave that file alone.
Such protection rests on a rule, whereas isolation would leave the agent no path to the secrets at all. Models hallucinate and find ways around their instructions, which makes a rule the weakest form of control a company can choose.
From day one, my team designs agent-based systems in which the agents have no access to passwords or keys of any kind. Security means full control over everything an agent can reach.
Match agent autonomy to the risk of each action.
Low-risk actions can run without step-by-step approval, provided the agent’s data access and scope have firm limits. Summarizing internal information, drafting documents, routing requests and compiling internal reports fall into this group.
Medium-risk actions let the agent do much of the work alone, but certain steps need human confirmation. Examples include updating CRM records, creating internal tasks, preparing a client reply or changing a workflow status.
High-risk actions carry financial or legal weight and call for explicit approval and logging. Some also need caps on scale or a human in the loop. External communication, contract changes, fund transfers, data deletion and changes to access rights belong here.
Each level needs its own approval threshold and audit requirements.
Plan how to undo an agent’s mistakes.
I often hear the question, “Can the agent do this task?” A more useful one is whether the company can roll back the result if the agent gets the task wrong.
If an agent updates thousands of CRM records, you need to know how to halt the process and restore the previous state after the first faulty changes.
The workflow needs sandbox testing and a phased rollout, plus approval gates before critical operations and a defined way to reverse changes. A kill switch and a cap on autonomous actions belong there too.
Treat observability as a management tool.
A company needs to know who launched and approved the agent and when. It also needs a record of the data and tools the agent used, along with the instructions behind its actions and their outcome.
If the team can’t reconstruct the chain of events after an incident, the company doesn’t actually control the system.
Name the people who own each agent.
Once an agent affects clients, revenue, operations or sensitive data, named people have to carry responsibility for it. An abstract “AI team” can’t fill that role. A business owner answers for the agent’s purpose and the level of risk the company will accept. A technical owner answers for architecture, integrations, access rights and monitoring.
Three more things belong in writing. The permission scope documents the data and systems available to the agent, as well as the actions it may take. The escalation path describes how a problem reaches a human. The review date marks when someone revisits the permissions and the agent’s real level of autonomy.
The Value Of AI Agents: Control
Gartner expects more than 40% of agentic AI projects to be canceled by the end of 2027. Rising costs and unclear business value top its list of reasons, together with weak risk controls. By 2028, Gartner forecasts, 33% of enterprise software applications will include agentic AI. I believe the value of these agents will depend on how well companies control their autonomy.
Forbes Business Council is the foremost growth and networking organization for business owners and leaders. Do I qualify?
