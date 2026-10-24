---
id: "4463f5602fe9cfe9"
title: "Hackers find a way to turn users own AI agents and Downloads folders against them"
url: "https://mashable.com/tech/hackers-ai-coding-agents-downloads-malware"
link: "https://mashable.com/tech/hackers-ai-coding-agents-downloads-malware"
source: "Mashable"
domain: "mashable.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T16:14:35Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Olivia Tauber"]
language: "en"
summary: "Your Downloads folder probably contains a few PDFs, forgotten screenshots, and several files named some variation of \"final.\" But according to a recent report by security company Forever, it could also contain instructions telling your AI assistant to install malware . In an Oct. 22 blog post , the company reported that they caught an AI coding assistant following those instructions on a…"
tags: []
orgs: ["Anthropic", "OpenAI", "Nvidia"]
topics: ["agents & coding", "search & media", "jobs & society"]
content_source: "fulltext"
word_count: 687
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Hackers find a way to turn users own AI agents and Downloads folders against them

Mashable · Olivia Tauber · 2026-10-23

Hackers find a way to turn users' own AI agents and Downloads folders against them
Your Downloads folder probably contains a few PDFs, forgotten screenshots, and several files named some variation of "final." But according to a recent report by security company Forever, it could also contain instructions telling your AI assistant to install malware.
In an Oct. 22 blog post, the company reported that they caught an AI coding assistant following those instructions on a customer's computer. The company blocked the installation, then traced the request to a text file in Downloads.
How does a text file get that kind of power? Tools like OpenAI's Codex and Anthropic's Claude Code can, depending on their permissions, edit files, run commands, and install software. Developers leave them instruction files called AGENTS.md or CLAUDE.md to explain how to work on a project. If you're building a website, those notes might tell the assistant which fonts to use or what to test before finishing.
You May Also Like
An attacker can leave instructions, too. In this case, the file told the assistant to install "function-color," a software package linked to the MALFEX malware campaign documented by Checkmarx.
Forever didn’t establish how the file reached the customer's computer, but its researchers demonstrated one possible route. Depending on browser settings, a website can drop a file into Downloads without asking for approval. If someone then launches their coding assistant in that folder, it could read the file and follow its orders.
When Forever tested the customer's file on an isolated computer, it said Codex downloaded and ran the malware. It also changed settings that could make the attacker’s software load in later sessions.
"Once it is written, every Codex session on the machine loads the attacker’s server at startup — in any folder, any project," the researchers wrote. "You can leave the folder. The poison stays."
The team separately devised a test targeting Claude Code. The attack worked about half the time, redirecting Claude's traffic to a server the researchers controlled. That exposed a login token and allowed them to send commands back for the assistant to execute, illustrating the risk of giving an assistant access to your computer when it can mistake a stranger's instructions for its own assignment.
Researchers have pulled off similar tricks before, showing what AI can really do in the wrong hands. In March 2025, Pillar Security researchers got AI coding assistants to slip harmful code into a project by hiding malicious instructions in their coding rules. In April 2026, NVIDIA’s researchers used a poisoned AGENTS.md file to get Codex to sabotage software and conceal the change. This time, though, Forever says it caught an actual attacker trying the trick on a customer's computer. Yikes.
How to protect yourself
Forever recommends keeping coding assistants out of your Downloads folder and checking unfamiliar AGENTS.md or CLAUDE.md files before letting an agent work in a project. Keep sandboxes enabled to restrict what the assistant can access, and leave approval requirements on so the agent has to ask permission before taking certain actions.
If you suspect an assistant has already followed malicious instructions, check its settings for unfamiliar servers or connections and revoke and replace potentially exposed login tokens. Deleting the original text file may not undo changes the assistant has already made.
"The thing to watch is not this file or this folder," the researchers wrote. "It is the agent itself — software that reads untrusted input, holds your credentials, and acts with your authority, sitting in a blind spot the old tools were never built to see."
Want more science and tech news delivered straight to your inbox? Sign up for Mashable's Light Speed newsletter or get Mashable push alerts today.
Topics Cybersecurity
Olivia Tauber is the deputy editor of digital culture, covering creators, media, movies, beauty, and more. Based in New York, her work has appeared in The New York Times, Vanity Fair, The Cut, Teen Vogue, Complex, and Interview Magazine. She holds a Master's degree in Journalism from NYU and a Bachelor's from the University of Michigan. She also runs Fan Mail, a weekly pop-culture newsletter.
