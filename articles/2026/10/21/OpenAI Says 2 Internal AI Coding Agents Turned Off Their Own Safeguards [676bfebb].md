---
id: "676bfebb66008a62"
title: "OpenAI Says 2 Internal AI Coding Agents Turned Off Their Own Safeguards"
url: "https://pcmag.com/news/openai-says-2-internal-ai-coding-agents-turned-off-their-own-safeguards"
link: "https://pcmag.com/news/openai-says-2-internal-ai-coding-agents-turned-off-their-own-safeguards"
source: "PCMag"
domain: "pcmag.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T12:09:51Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["James Peckham"]
language: "en"
summary: "In two separate internal coding tasks, GPT-powered agents weakened their own monitoring systems to help accomplish tasks."
tags: []
orgs: ["OpenAI", "Hugging Face"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 461
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI Says 2 Internal AI Coding Agents Turned Off Their Own Safeguards

PCMag · James Peckham · 2026-10-21

OpenAI has confirmed two new rogue-agent incidents involving its powerful agentic technologies, in which the agents disabled safety monitoring tools to complete projects more effectively.
The issues occurred during internal coding tasks in early October with GPT-6- and GPT 6.1-powered agents. “In both cases, the agents considered whether monitoring safeguards should be preserved, but interpreted routine coding instructions as permission to weaken them," OpenAI says.
One of the two incidents saw a GPT-6 Astra agent remove its own misalignment restrictions to help complete a coding task. In a previous conversation between two agents, one was instructed not to disable any monitors. The instructed agent then mistakenly interpreted another command, where it was told to preserve monitoring "as appropriate," as a reason to bypass the safeguard.
It then lied to a user who asked whether it had removed any safeguards to complete the task, even though there was clear evidence it had. “No […] I did not remove an enabled monitor from it,” the agent responded. OpenAI has yet to note whether the agent later acknowledged the error.
The misalignment report also details another incident involving a GPT-6.1 Sol-powered agent that disabled automatic alerts to OpenAI's security team during a particular project. It misconstrued an earlier instruction in which a user told it "don't send any messages" and decided to implement that instruction in its monitoring system, despite the two projects being separate.
OpenAI says both incidents were helpful in strengthening its security protocols, including better surfacing attempts by agents to disable misalignment monitoring during its own review process. “In addition to making it harder for models to disable monitoring, we are looking to understand why models might seek to do so in the first place," OpenAI says.
OpenAI doesn’t yet have an explanation for the behavior. "It is possible that this behavior is simply an example of 'benign' overpersistence, with models not understanding why monitoring is important or insisting that instructions be executed beyond what a reasonable person might expect," it says.
This report comes after numerous security incidents in recent months involving agentic AI technologies, many of which have been linked to OpenAI's technology. The first major report involved OpenAI's models going rogue and attempting to access an AI database called Hugging Face.
Disclosure: Ziff Davis, PCMag's parent company, filed a lawsuit against OpenAI in April 2025, alleging it infringed Ziff Davis copyrights in training and operating its AI systems.
About Our Expert
I’ve been a journalist for over a decade after getting my start in tech reporting back in 2013. I joined PCMag in 2025, where I cover the latest developments across the tech sphere, writing about the gadgets and services you use every day. Be sure to send me any tips you think PCMag would be interested in.
