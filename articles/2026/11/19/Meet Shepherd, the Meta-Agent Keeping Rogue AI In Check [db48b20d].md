---
id: "db48b20db167e68c"
title: "Meet Shepherd, the Meta-Agent Keeping Rogue AI In Check"
url: "https://spectrum.ieee.org/ai-agent-manager"
link: "https://spectrum.ieee.org/ai-agent-manager"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T15:00:03Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Rina Diane Caballar"]
language: "en"
summary: "AI agents are running amok on the internet, armed with commands to accomplish certain tasks but often acting in undesirable or unexpected ways. These rogue incidents run the gamut from deleting an entire email inbox to hacking websites and even launching cyberattacks . Much like human workers need managers, Weiyan Shi , an assistant professor at Northeastern University , believes AI agents…"
tags: ["Agentic-ai", "Alignment", "Software-engineering", "Algorithmic-management"]
orgs: ["Meta"]
topics: ["agents & coding", "jobs & society", "models & research"]
content_source: "fulltext"
word_count: 803
paywalled: false
image: "https://spectrum.ieee.org/media-library/illustration-of-an-ai-agent-supervising-and-designating-tasks-to-smaller-ai-agents.jpg?id=68511562&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Meet Shepherd, the Meta-Agent Keeping Rogue AI In Check

IEEE Spectrum · Rina Diane Caballar · 2026-11-19

AI agents are running amok on the internet, armed with commands to accomplish certain tasks but often acting in undesirable or unexpected ways. These rogue incidents run the gamut from deleting an entire email inbox to hacking websites and even launching cyberattacks.
Much like human workers need managers, Weiyan Shi, an assistant professor at Northeastern University, believes AI agents require oversight. “They are running potentially for a long time. However, the longer they run, they may have some errors, and they may make some dangerous, unsafe actions. We feel like there should be a middle layer,” she says.
This middle layer comes in the form of meta-agents that oversee behavior, provide quality control, and kick issues up the chain of command to a human when appropriate. “Worker agents are like the sheep wandering around, and the meta agent is like this shepherd trying to get them back on track,” Shi says.
As such, Shi and her colleagues at Northeastern University and Stanford University named their framework Shepherd, an intelligent guide for agentic sheep. To arm meta-agents with power, the team borrowed a concept from software development: version control. The accompanying paper will be presented at the 2026 NeurIPS conference to be held in December.
Version control for AI agents
Version control systems, such as the popular GitHub, track and manage changes to source code over time. These tools allow software engineers to collaborate on the same codebase without losing work. They can “fork” or create a copy of the codebase that they develop independently, “commit” to save a new version with changes, review revisions, and roll back to a previous version when an error or failure occurs.
Similarly, Shepherd serves as a version control system for AI agents. It’s built using the Python programming language and rooted in functional programming principles. Each agent action, along with the AI agent’s state and its relevant environment (such as an email inbox, a file system, or other) is stored as a commit, with a commit graph consisting of a series of actions. Meta-agents traverse the graph to navigate to any commit, enabling them to observe worker agents, intercept a buggy action, revert the worker to its previous step, and fork it to try another direction.
“There’s a subtlety because it looks to [worker] agents like they’re in the regular world where they can do things like send emails. But in actuality, the action of sending the email has been caught by a Shepherd sandbox, so a meta-agent or a human can come in and decide to actually send it,” says Derek Chong, a researcher at Stanford University’s Natural Language Processing Group who’s part of the Shepherd team. This sandboxing, he adds, functions as a guardrail or governance component.
“If there is a middle layer to help govern these worker agents, then that will help humans have better control,” Shi says. “Humans will still, eventually, have a say, and they can intervene with the meta-agent. They can also help steer these meta-agents.”
To demonstrate Shepherd’s feasibility, the team created three use cases. One used a supervisor meta-agent that intervened when conflict happened between parallel programming agents, helping lift their pair coding pass rate on a particular benchmark. Another developed an optimization meta-agent that proposed targeted edits to a worker agent’s finished workflow and tested them by replaying only parts of the run affected by the edits, helping improve performance. Finally, a training meta-agent during reinforcement learning picked points or steps at which to fork so the worker agent takes a better path, rewarding it along the way.
Shepherd is available as an open-source project, but Chong notes that the team is still in the process of building it from alpha to full production readiness. The Shepherd framework is part of the broader Agent Sciences Research Initiative (ASRI) cofounded by Chong and Shi. This collaboration of researchers from Northeastern, Stanford, and UC Berkeley aims to explore how to make AI agents more reliable and robust, how to evaluate them better, and how to ensure they’re safer.
“It’s becoming more and more clear that agent management is really important,” Chong says. “Agents should be able to inspect other agents and operate on them, just the way that management in real life can happen. We think Shepherd is the way we can build toward that and enable agent management to be democratized. And if you can democratize that, then humans can be empowered to build AI systems that support human flourishing.”
- Attempts to Keep Humans in the AI Loop May Actually Push Them Out ›
- Are You Ready to Let an AI Agent Use Your Computer? ›
Rina Diane Caballar is a writer covering tech and its intersections with science, society, and the environment. An IEEE Spectrum contributing editor, she's a former software engineer based in New Zealand.
