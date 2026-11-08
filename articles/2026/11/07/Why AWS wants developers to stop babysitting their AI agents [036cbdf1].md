---
id: "036cbdf195122538"
title: "Why AWS wants developers to stop babysitting their AI agents"
url: "https://thenewstack.io/kiro-bots-agent-memory"
link: "https://thenewstack.io/kiro-bots-agent-memory"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-07T15:30:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Adrian Bridgwater"]
language: "en"
summary: "AWS first introduced Kiro , its agentic, spec-driven development environment, in July 2025. It also introduced Kiro Crew in August of this year, its persistent, open-source development workspace that remembers context. Now, to help developers juggle more complex tasks executed in parallel,  AWS introduced Kiro bots  on Thursday, adding persistent agent memory and delegated workflow management to…"
tags: ["AI", "AI Agents", "Developer tools", "Software Development"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "jobs & society", "products & launches"]
content_source: "summary"
word_count: 1299
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Why AWS wants developers to stop babysitting their AI agents

The New Stack · Adrian Bridgwater · 2026-11-07

AWS first introduced Kiro , its agentic, spec-driven development environment, in July 2025. It also introduced Kiro Crew in August of this year, its persistent, open-source development workspace that remembers context. Now, to help developers juggle more complex tasks executed in parallel,  AWS introduced Kiro bots  on Thursday, adding persistent agent memory and delegated workflow management to the toolset. Kiro Crew already carried memory across sessions; bots give each agent its own. 

 Described as a “named, long-running agent that you define and customize for a specific part of your work” (such as reading new issues in a ticket queue), Kiro bots retain their own memory and start with only the tools provided to them at creation.  

 The bot function also runs its own sessions (by which AWS means parallel worker sessions the bot launches and monitors), so software engineers don’t have to track them one by one or weave them together. 

 According to AWS, the arrival of Kiro bots heralds the shift from delegating tasks to delegating processes. 

 Babysitting vs. bots building better 

 AWS Agentic AI director of engineering Kathy Kam tells The New Stack that agents are only useful when developers can trust them to act on their own, but when a session ends, nobody owns the work anymore.  

 “Developers end up as the go-between, carrying context from one session to the next. Kiro bots take that job off their plate, so developers can now spend the day deciding what’s worth building instead of babysitting sessions,” Kam says. 

 “Developers can now spend the day deciding what’s worth building, instead of babysitting sessions.” 

 Up to now, if this babysitting to carefully shepherd agents from one point to the next with more durable memory isn’t there, then the negative consequences show up pretty fast. 

 “You get what a lot of developers now call context rot , which can make it feel like nagging an agent to redo what you told it yesterday,” Kam explains. “It spreads fast when parallel tasks each hold their own drifting version of reality. So we gave every Kiro bot its own durable memory , with a notes [.md] file it reads and writes, and that developers can edit directly. Fix a mistake once – and it stays fixed, instead of resurfacing across every task in flight.” 

 Each Kiro bot works with only the tools and permissions its job needs.  

 For example, a research bot can search the web and read files, but it can’t change them. A deployment bot can run deployment scripts and ask for approval before each change. A bot can ask developers for more tools, but nothing changes until the software engineer actually approves the request. Because each bot has its own memory, what the deployment bot learns about the release process does not mix with what the research bot learns. Separate lessons keep each bot aligned to its own responsibility, as judged by the developer at the outset. 

 Trust comes from track record 

 If this feels like bots and agents are developing more of their own personalities and being anthropomorphized into some sort of hierarchy, with some acting in a more senior capacity than others, then AWS’s Kam says that’s the wrong way to think about it. 

 “A hierarchy of agents based purely on IQ is the wrong measure. What matters is what an agent is allowed to touch, and a Kiro bot earns trust by building a track record,” underlines Kam. 

 “A hierarchy of agents based purely on IQ is the wrong measure. What matters is what an agent is allowed to touch, and a Kiro bot earns trust by building a track record.”  

 No anthropomorphization as yet, but still, each Kiro bot has a name, an avatar, its own memory, and one ongoing chat channel where developers set its direction and come back for results.  

 Behind that chat, the bot starts sessions in parallel and monitors them. It can redirect a session that drifts from the plan and combine the results when the sessions finish. If one task needs a human decision, the bot can ask the engineer while it keeps working on parts that don’t depend on an answer. Developers can set up routines in the chat, so a bot can investigate overnight build failures before the coding team even starts its day. 

 Yes, AWS, but what if…? 

 There still feels like a lot of yes, but what if… questions to surface here. What happens when bots are instructed to wait for human developer decisions, but the bot and wider agent framework already has enough institutional or historical knowledge to tell it the human doesn’t need to be involved? Doesn’t this mean the human coder should be overridden with an automation to reduce time-wasting? 

 “As more companies shift toward software factories , agents can end up remembering more information and context across a team than an individual developer, but that doesn’t put the agent in charge,” clarifies AWS’ Kam. “The human is still the one accountable, while the agent is responsible for executing the work. The software engineer sets how much access each Kiro bot gets for its job, so a deployment bot can require approval before every change while a research bot runs with fewer checkpoints.” 

 Kam further notes that a Kiro bot can “ask for more authority, but it can never take it” unmanaged. However, as already emphasized, while it waits for an answer, it keeps moving on everything that doesn’t need the human-in-the-loop. 

 Each Kiro bot understands its specialty, outcome, trade-offs, limits & decisions 

 In its official launch blog, AWS said developers using Kiro bots will find the direction given to the bot stays visible and revisable. It is set through ongoing conversation and feedback, and Kiro Crew’s learning builds within each bot. This lets the developer hand off an ongoing responsibility, not a single task. Each bot understands, for its specialty, the outcome it should aim for, the reason behind a trade-off, the limits around a change, and decisions already made.  

 One Kiro bot can own issue intake while another owns release readiness, and each follows the rules set for that work. AWS noted that taken together, each developer’s “crew of bots” supports the programmer’s unique approach to development and work requirements without flattening into one generic workflow. 

 “Bots can’t delegate work to other bots — and that’s by design to prevent context rot and ensure Kiro bots can remain independent.” 

 “Bots can’t delegate work to other bots — and that’s by design to prevent context rot and ensure Kiro bots can remain independent,” highlights Kam. “A Kiro bot splits big jobs across its own parallel workstreams and pulls the results into one recommendation. Developers stay the one defining each’s boundaries and connecting Kiro bots to each other, so no decision that you want to provide input on moves between them without you being involved.” 

 AWS also explained that over time, a developer’s bot crew “reflects how you actually develop”, because each bot carries the requirements and boundaries for its part of the work needed. The software engineer still decides how those processes change and where judgment belongs. 

 To get started, AWS has encouraged developers to open the bots workspace in the Kiro Crew sidebar, add a bot, and choose the default or a custom agent as its base. A custom agent supplies the prompt, model, tools, and skills, so users can build on a setup they already use without changing existing chats. In summary, with all the autonomy swirling around here, we might suggest that AWS isn’t asking developers to give up the steering wheel, but perhaps it’s asking them to sit further away from the passenger seat when AI is doing the driving. 
 The post Why AWS wants developers to stop babysitting their AI agents appeared first on The New Stack .
