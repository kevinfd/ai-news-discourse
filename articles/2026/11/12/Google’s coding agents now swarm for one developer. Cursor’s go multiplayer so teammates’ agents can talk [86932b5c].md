---
id: "86932b5c72e9eeb7"
title: "Google’s coding agents now /swarm for one developer. Cursor’s go multiplayer so teammates’ agents can talk."
url: "https://thenewstack.io/cursor-google-multiplayer-swarm"
link: "https://thenewstack.io/cursor-google-multiplayer-swarm"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-12T21:22:46Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Coding agents are pretty good at working in parallel : one writes a new API endpoint, another updates the tests, while a third fixes a bug elsewhere in the codebase. However, they’re not quite so adept at knowing what their coding counterparts are doing — put several on one project and they duplicate work, trip over each other’s changes, and leave the developer firefighting the fiasco that…"
tags: ["AI", "AI Agents", "AI Engineering", "Developer tools"]
orgs: ["Google", "Cursor", "Anthropic", "OpenAI", "Microsoft", "Amazon", "Tesla"]
topics: ["agents & coding", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 1306
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google’s coding agents now /swarm for one developer. Cursor’s go multiplayer so teammates’ agents can talk.

The New Stack · Paul Sawers · 2026-11-12

Coding agents are pretty good at working in parallel : one writes a new API endpoint, another updates the tests, while a third fixes a bug elsewhere in the codebase. However, they’re not quite so adept at knowing what their coding counterparts are doing — put several on one project and they duplicate work, trip over each other’s changes, and leave the developer firefighting the fiasco that follows. 

 That’s why the major AI labs and coding-tool makers have all been looking for ways to bring order to their agent fleets, albeit with slightly different approaches. 

 This week alone, Google and Cursor both debuted features designed to keep agents from tripping over each other, but at different scales. Google’s Swarm organizes the agents working for a single developer, while Cursor’s multiplayer Projects lets agents working for different colleagues coordinate with each other. 

 Cursor gets teammates’ agents talking 

 Cursor first debuted Projects back in September , giving developers a way to hand a larger job to a coordinator agent that breaks it into tasks and delegates them to worker agents. 

 Then on Tuesday, the company, which Elon Musk’s SpaceX acquired for $60 billion in August, unveiled multiplayer functionality for Projects. Developers can now invite teammates into a project, where each person gets their own coordinator and workers. 

 Cursor coordinators exchange messages across teammates’ tasks. 

 Everyone’s agents work from the same task board and project documents, and their coordinators can message each other directly to share plans, flag overlaps and more. 

 Ultimately, it’s all about cutting down on the coordination developers have to do themselves. 

 Ultimately, it’s all about cutting down on the coordination developers have to do themselves. If one teammate’s agents are changing a database schema and another’s are building a feature that depends on it, their coordinators can agree on which change needs to land first. 

 Antigravity , for its part, is Google’s counterpart to Cursor. It’s where Google has consolidated various other coding tools, having moved individual Gemini CLI users to Antigravity and begun winding down Jules , its background coding agent. 

 On the same day Cursor unveiled multiplayer Projects, Google rolled out Gemini 4 Carbon in Antigravity, alongside a preview of its own approach to coordinating coding agents. Dubbed Swarm (stylized as /swarm), it lets a developer hand one assignment to a coordinator that then splits it among worker agents and assigns a verifier to check their changes. The workers can message each other on a shared board, so they can coordinate their changes as they go. 

 For example, a company that wants to change how its online checkout system verifies authentication tokens could use Swarm to split the work. One agent updates the authentication middleware while another updates the token verifier. They can work in separate Git worktrees, use the board to agree on how their changes fit together, and hand them off to a verifier for testing. 

 Swarm agents split and verify a token migration. 

 Taking to X on Tuesday, Varun Mohan , director of software engineering at Google DeepMind, said Swarm gives developers a convenient way to put multiple agents on a complex task, adding that Google staff were already using Swarm to take on larger jobs internally. 

 “The alpha from using swarms is ridiculous,” Mohan writes . “We have folks using swarms of 100s of agents to build large systems and products from scratch with a single prompt.” 

 Logan Kilpatrick , a member of technical staff at Google DeepMind, said on X that seeing swarm outputs had been ‘really impressive,’ and that they offered ‘a new scaling dimension for AI!” 

 “A new scaling dimension for AI!” 

 This, ultimately, gets to the crux of how each of these companies has tackled agent coordination. 

 When agents work for different people 

 Antigravity’s Swarm takes one developer’s assignment and gives the agents handling it a way to talk as they work. Cursor’s multiplayer Projects, meanwhile, takes assignments from different teammates and lets their coordinators talk across those assignments 

 That’s the distinction Cursor product manager Aryaman Khandelwal is keen to draw in Tuesday’s announcement . 

 “Multi-agent systems have so far served one person. Projects is a multi-agent system built for a whole team.” 

 “Multi-agent systems have so far served one person,” Khandelwal writes. “Projects is a multi-agent system built for a whole team.” 

 A quick peek across the AI coding landscape shows how others have approached agent coordination — including Anthropic. Its still-experimental Claude Code Agent Teams gives agents working on a common assignment a shared task list and a way to message each other. And recently, the company added cross-session messaging to Claude Code , so sessions started separately can exchange findings or warn each other about changes. But those sessions still belong to the same developer. 

 In October, GitHub put Projects in the Copilot app into public preview, giving developers a way to hand Copilot a goal that spans repositories and have it distribute the work across agents. AWS’s Kiro Crew bots, meanwhile, which launched last week , can start several sessions, steer them as they run and pull their results together. 

 Separately, Anthropic and OpenAI have also built agents that teammates can use together. Anthropic introduced Claude Tag in June , letting people in a Slack channel delegate to a shared Claude. OpenAI’s ChatGPT workspace agents, announced in April , can be used and maintained by multiple colleagues. 

 Community concerns: Spreading mistakes 

 However, some in the community raised concerns that letting teammates’ agents talk could spread one agent’s mistakes across the whole team, especially if each person’s agents follow different rules, and that an agent could request information it shouldn’t have access to. Khandelwal, though, responded that multiplayer Projects lets teams define shared rules and skills for everyone in a project. On the access part, Cursor’s documentation says agents treat messages from teammates’ agents as untrusted input and ask before sharing a person’s private files or connector data. A teammate’s message is handled in a separate chat, which Cursor says never shares secrets or credentials. The Projects documentation doesn’t say whether admins can set different rules for those exchanges based on a teammate’s role. 

 Separately, fresh research suggests that teams of per-user agents can struggle. In a study published Wednesday , researchers in Anthropic’s Fellows Program tested what happens when multiple users each delegate to their own agent and those agents share a resource, in four simulated environments that included a code merge queue. In every environment, group outcomes were worse than when a single agent served everyone, by roughly 10 to 45 percentage points for Anthropic’s Claude models, even when each user’s agents could message each other. Agents stalled as teams grew, overrode other users’ requests, and made unsupported claims about what other people wanted. Some fixes helped, such as appointing a lead agent or blocking an agent from acting until it had read its messages, but which ones worked depended on the task. 

 All in all, these various launches this year show a push to make it easier for teams to delegate work and keep track of what their agents are doing. With multiplayer mode in Projects, Cursor is tackling a specific part of that problem. 

 Parker Smith , who works in engineering for Cursor’s parent company SpaceXSI, says the point is really just to keep agents moving without unnecessary delays. 

 “Agents move fast, having a blocker on peer context is too slow,” Smith writes on X . “Multiplayer projects allow your agent to grab all the context it needs from your coworkers agents without needing to involve you.” 

 Cursor’s multiplayer Projects is in beta now for users on a team account, while Google’s Swarm is in preview for Google AI Pro and Ultra subscribers. 
 The post Google’s coding agents now /swarm for one developer. Cursor’s go multiplayer so teammates’ agents can talk. appeared first on The New Stack .
