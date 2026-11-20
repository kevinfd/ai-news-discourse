---
id: "799e27214d566530"
title: "Groundcover Investigations lets engineers steer AI SRE agents"
url: "https://thenewstack.io/groundcover-ai-incident-investigations"
link: "https://thenewstack.io/groundcover-ai-incident-investigations"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T14:00:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Meredith Shubel"]
language: "en"
summary: "Groundcover, the eBPF-based observability startup , has introduced Investigations, giving agents and engineers one place to collaborate on incident response in real time.  \n\n In the shared workspace, groundcover ’s investigator and moderator agents work with on-call engineers and their preferred coding agents to investigate production incidents together, analyzing behavior across applications…"
tags: ["AI", "AI Agents", "DevOps", "Observability", "sponsor-groundcover", "Sponsored", "sponsored-post"]
orgs: ["Anthropic", "Salesforce"]
topics: ["agents & coding", "business & funding"]
content_source: "summary"
word_count: 1356
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Groundcover Investigations lets engineers steer AI SRE agents

The New Stack · Meredith Shubel · 2026-11-19

Groundcover, the eBPF-based observability startup , has introduced Investigations, giving agents and engineers one place to collaborate on incident response in real time.  

 In the shared workspace, groundcover ’s investigator and moderator agents work with on-call engineers and their preferred coding agents to investigate production incidents together, analyzing behavior across applications and infrastructure to create a shared record of evidence.  

 Rather than handing full control to agents, the idea is to help engineers and agents work together on incident investigations. 

 “Most AI SRE tools ask engineers to step back and let the agent take over. We built Investigations for engineers to step in.” 

 Shahar Azulay , CEO and co-founder at groundcover, tells The New Stack that “Most AI SRE tools ask engineers to step back and let the agent take over. We built Investigations for engineers to step in.”  

 Everyone has their favorite agent. That’s a problem  

 AI agents are flooding daily software engineering workflows. Already, Salesforce reports that organizations use an average of 12 agents — a number that’s expected to grow by 67% within two years. But half of those agents are working in silos. 

 This presents a particular problem in incident response. Individual agents, like Claude Code or Codex, may be able to troubleshoot on their own, but how can engineers aggregate their findings? They don’t — or at least, it’s very tricky. More often than not, Azulay says agents’ varying conclusions are spread across chats and tickets.  

 As he describes it: “Every engineer now has an agent, but each of those agents investigates on its own and findings end up in a chat window.”  

 How groundcover wants engineers and agents to work together 

 With its Investigations, groundcover aims to eliminate fragmented incident response and create a single source of truth for every engineer and agent. Here, agents can lead collaborative, evidence-driven investigations, testing hypotheses against production data, validating findings, and backing every conclusion with evidence. Engineers, for their part, get real-time visibility into the investigation and can step in to steer it as they see fit.  

 It all starts when a monitor issue fires and an engineer opens an investigation from groundcover or Slack. groundcover says automatically opening an investigation when a monitor fires is coming next. 

 The investigator agent builds a graph with a question (e.g., Why is checkout latency spiking in the US?) and then opens several hypotheses to explain it. From there, it turns to production telemetry to query the traces, logs, metrics, and Kubernetes events the groundcover eBPF sensor is already collecting, testing each one and recording what it finds as evidence.  

 Importantly, Azulay tells The New Stack , “the investigator can’t mark its own work as correct. When it thinks a hypothesis is supported, it submits a proposal that cites specific findings, and a separate agent, the moderator, acts as an LLM-as-a-judge and checks whether that evidence backs up the claim. No findings, no closure.” 

 “Separating the agent that does the work from the agent that judges it gives you a conclusion you can trust without redoing every step.” 

 Given the speed at which agents reach conclusions — and the risk that they act beyond scope — Azulay says this separation of hypothesis and conclusion is crucial to arriving at a trustworthy conclusion: “Separating the agent that does the work from the agent that judges it gives you a conclusion you can trust without redoing every step.”  

 According to groundcover, the investigator agent also learns from each investigation so it can understand which hypotheses tend to hold up and where to look first when similar problems arise. 

 External coding agents are invited to the party, too 

 While groundcover’s investigator and moderator agents lead investigations, the startup recognizes that most engineers already bring a slew of third-party agents to the table, whether for business intelligence, coding, product roadmapping, etc. Those agents are welcome in Investigations, too. 

 Using groundcover’s MCP server, engineers can connect Claude Code, Codex, and other agents to the shared workspace to read and add to the same investigation. That builds on groundcover’s October launch, which let outside coding agents query its telemetry over MCP and hand off investigations to groundcover’s own agent.  

 For Azulay, this lets each agent shine in what it does best. As he tells The New Stack :  

 “Coding agents and groundcover’s agents are good at different things. Our agents know your telemetry and how to query it fast. Your coding agents know your code. Neither has the full picture.”  

 Working together, then, via Investigations, the different agents can lean on each other depending on the task at hand. If a hypothesis points to a code problem, for example, the investigator agent may bring in Claude Code or Codex to check it. When engineers’ coding agent needs telemetry, groundcover’s agent fetches the data.  

 “Our agents know your telemetry and how to query it fast. Your coding agents know your code. Neither has the full picture.” 

 What matters is that every agent publishes its findings in the same investigation tree, preventing engineers from going on a wild goose chase trying to connect the dots across five different private chat sessions.  

 “Everyone can see what’s been checked, what’s still open, and why anyone believes what they believe,” says Azulay. “Every contribution is attributed, so you know a finding came from a specific engineer’s Claude session at a specific time.”  

 Does this mean agents and engineers are on even footing?  

 Not quite. Per Omer Mayer , senior product manager, groundcover, engineers can “watch each hypothesis get supported or ruled out in real time” — and they can “step in and steer it” at any time.  

 In other words, engineers can immediately see what groundcover agents are investigating. If they think the agents are off the mark, they can easily take over. 

 Azulay offers  The New Stack an example: Suppose a checkout latency monitor fires, and an automated investigation kicks off, generating three hypotheses, one of which is a slow query from a recent deploy. 

 But the on-call engineer knows something the investigator agent doesn’t: The deploy was rolled back 10 minutes earlier and latency didn’t recover. Easy — they can stop that hypothesis, which closes everything under it and tells the agent to stop spending time and tokens there.  

 “The engineer might also add context the agents don’t have, like ‘the payments team changed their retry policy this morning,’” adds Azulay. “That opens a new line of inquiry nobody would have found in the telemetry alone.” 

 What’s also important is engineers’ right to override where agents can’t. Remember, the investigator agent is forbidden from closing anything without the moderator agent’s okay. But engineers don’t need the moderator’s permission to steer the investigation, Azulay says. 

 “The moderator is there to keep the agents honest, not to slow down the people responsible for the incident,” says Azulay.  

 More agents are teaming up 

 Earlier this year, more vendors made moves to bring individual agents out of isolated workflows and into a shared space.  

 On the coding side, Cognition, Microsoft, and Augment Code all launched team-layer coding agent platforms , pushing coding agents past the single-developer loop.  

 Last month, Harness acquired select Augment Code assets , including Cosmos, to link AI coding agents to its delivery platform. This way, teams writing code in Cosmos will have context from across the software development lifecycle available to the agent as it works. 

 Now, groundcover’s Investigations brings a similar shared-space principle to incident response. More work is happening elsewhere, too. Slack Code has given coding agents their own temporary channels for plans, diffs, and live previews, which Katie Steigman , vice president of product at Slack, told The New Stack is already being used for incident response. 

 Other companies are also building tools for collaborative incident investigations, including shared workspaces for engineers and agents and handoffs to coding agents over MCP. 

 So far, conversations have focused on agents’ individual prowess and what they can do. But as agents move deeper into software engineering workflows, agent-engineer teamwork looks like what will make incident response work best.  
 The post Groundcover Investigations lets engineers steer AI SRE agents appeared first on The New Stack .
