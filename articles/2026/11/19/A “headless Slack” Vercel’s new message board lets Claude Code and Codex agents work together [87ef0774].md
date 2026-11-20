---
id: "87ef0774c1e38e16"
title: "A “headless Slack”: Vercel’s new message board lets Claude Code and Codex agents work together"
url: "https://thenewstack.io/vercel-board-agent-swarms"
link: "https://thenewstack.io/vercel-board-agent-swarms"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T16:58:48Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Paul Sawers"]
language: "en"
summary: "For AI agents to work together effectively, they need a way to communicate and divvy up tasks — much as humans already do through a swath of digital collaboration tools. \n\n Vercel is tackling this with Board , an experimental shared message board through which agents can claim tasks, exchange findings and track progress across different tools and environments, while allowing developers to follow…"
tags: ["AI", "AI Agents", "Developer tools", "Security"]
orgs: ["OpenAI", "Anthropic", "Google", "Hugging Face", "Salesforce", "Cursor"]
topics: ["agents & coding", "models & research", "business & funding"]
content_source: "summary"
word_count: 1082
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# A “headless Slack”: Vercel’s new message board lets Claude Code and Codex agents work together

The New Stack · Paul Sawers · 2026-11-19

For AI agents to work together effectively, they need a way to communicate and divvy up tasks — much as humans already do through a swath of digital collaboration tools. 

 Vercel is tackling this with Board , an experimental shared message board through which agents can claim tasks, exchange findings and track progress across different tools and environments, while allowing developers to follow and intervene in the work. 

 In a blog post published on Wednesday, Vercel says it developed Board for its own engineering operations, first using it to coordinate security agents investigating vulnerabilities and submitting fixes. It then rebuilt v0 ’s software factory around Board, which Vercel says now “merges over 50% of PRs.” 

 “It packages what we’ve learned about coordinating work across agent fleets.” 

 “It packages what we’ve learned about coordinating work across agent fleets and builds towards a future where multiple teams of humans and agents orchestrate swarms, software factories, and other agentic workflows,” the company writes. 

 The coordination conundrum 

 OpenAI demonstrated the importance of multi-agent communication in September when it announced that its agents had solved the Navier–Stokes problem, a longstanding mathematical challenge concerning the behavior of fluids. 

 The company said some 10,000 agents operated concurrently in the group that produced the result, exchanging information as they worked. 

 “In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens,” the company wrote. 

 The need to manage multiple agents in parallel is becoming increasingly apparent in software development. Just last week, Google and Cursor introduced competing approaches to coordinating coding agents, with Google focusing on agents working on behalf of a single developer and Cursor enabling agents belonging to different teammates to communicate. 

 Then on Tuesday, Replit introduced Missions , bringing multiple agents together to tackle larger development projects. 

 Elsewhere, companies are also turning to existing collaboration platforms to bring humans and AI agents together. Devin Bots , which Cognition launched on Tuesday , uses Slack to connect agents with their human teammates. 

 In an X post published on Thursday, Salesforce CEO Marc Benioff says more than 226,000 custom agents have been deployed to Slack from across the major agent-building platforms. Notably, he says that he hadn’t anticipated this use of Slack when Salesforce acquired it back in 2021 , acknowledging that companies are now using the platform as “trusted agent infrastructure.” 

 Vercel itself added its Agent to Slack code channels in August, allowing teammates to follow its work, give instructions and review proposed changes. 

 With Board, Vercel provides channels and threaded discussions where agents can pick up assignments, exchange findings, monitor dependencies and record completed work. It also maintains a history of activity, allowing developers to follow what their agents have been doing. 

 Crucially, Board is designed to accommodate agents built on different technologies. Vercel explicitly lists Claude Code, Codex, Pi, OpenCode, eve, fx, Mastra and LangChain, as tools that can work together through Board. 

 “This is an important building block for software factories, self-optimizing systems, and scientific research.” 

 In an X post published on Wednesday, Vercel CEO Guillermo Rauch described the technology as a “message board infrastructure primitive.” Or, a “headless Slack” for agents. 

 “This is an important building block for software factories, self-optimizing systems, and scientific research, where the human prompting is just the seed of the system, and millions of agents can operate in a decentralized fashion,” Rauch writes, adding that Board is designed to work independently of any particular model, agent harness or hosting provider. 

 “Just bring your agents, give them our CLI, and watch magic happen,” he adds. 

 One of the most impressive things I've seen, and I think this is an important advancement to the state of the art. Message boards were the enabling technology of both the Navier-Stokes math breakthrough and even the OpenAI/HuggingFace cyber feat. We built a message board… https://t.co/S3spbJQdAk — Guillermo Rauch (@rauchg) November 19, 2026 

 Keeping humans in the loop 

 Board also connects agents to the tools developers already use, including Slack, GitHub and Linear. For example, a developer can submit a request through Slack, which an agent can then pick up and break into smaller assignments for other agents to complete. 

 The ensuing discussion, task ownership and progress updates are maintained in Board. 

 Slack request becomes agent tasks 

 As work progresses, Board can synchronize information with GitHub, allowing agents and developers to follow changes to pull requests and review feedback, without having to manually relay information between systems. It also supports event-driven triggers, so agents can resume work when new messages arrive or task statuses change. 

 GitHub updates appear as messages 

 It’s worth noting that human oversight remains a crucial part of the process. Agents can report findings and wait for developers to approve changes before proceeding, while Board also provides channel-level permissions that determine which people and agents can access information or perform particular actions. 

 Agents request human approval 

 The security question 

 The ability of agents to communicate independently raises key questions about who controls those conversations and what information they can exchange. 

 Indeed, Rauch points to the OpenAI/Hugging Face cybersecurity incident from July as another high-profile example of message boards facilitating agent coordination. During the breach, agents repurposed an internal software repository to exchange findings and coordinate their activities. 

 “A core part of why we built Vercel Board was to fulfill our own needs for security and auditability.” 

 Thus, security and oversight are key considerations for systems such as Board. Vercel says it built access controls and activity logs into the service, allowing teams to restrict which agents can interact with particular channels and track their actions. 

 “A core part of why we built Vercel Board was to fulfill our own needs for security and auditability,” the company writes. 

 The accompanying documentation also warns that agents may “read messages as instructions,” making it important to control who can post in channels where agents receive tasks. By default, channels are accessible to team members, project deployments and installed apps unless administrators restrict access. Vercel recommends creating private channels or restricting permissions where necessary, and keeping sensitive information such as API keys and tokens off Board entirely. 

 Vercel Board is available now as an experimental feature on all Vercel plans, accessible through the Vercel CLI or JavaScript SDK. It’s free during the experimental period, though Vercel says it may introduce charges later. 
 The post A “headless Slack”: Vercel’s new message board lets Claude Code and Codex agents work together appeared first on The New Stack .
