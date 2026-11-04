---
id: "85bf39320aead60f"
title: "Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)"
url: "https://reddit.com/r/ClaudeAI/comments/1xn8gpz/hardwareintheloop_for_claude_ai_builds_the_pcb"
link: "https://reddit.com/r/ClaudeAI/comments/1xn8gpz/hardwareintheloop_for_claude_ai_builds_the_pcb"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T23:19:01Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Kemerd"]
language: "en"
summary: "Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 312
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xn8gpz/hardwareintheloop_for_claude_ai_builds_the_pcb/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Hardware-in-the-loop for Claude: AI builds the PCB, firmware, picks the sensors, SoCs; designs the CAD, and then iterates the designs against a virtual twin (Isaac Sim / Unreal)

Reddit · Kemerd · 2026-11-03

Spent the last few weeks letting Claude Code do actual high-level hardware work: boards, enclosures, firmware, wiring harnesses, sensors, motors, etc. Boards are Python scripts that go all the way to fab files, but only if ERC/DRC come back clean and every part checks out live against LCSC. Firmware runs against a virtual twin on the PC before you ever need to spend any dollars on components. In my own project—a multi-board project with motors, dozens of sensors and a custom enclosure—it ran for weeks across several iterations, including the PCB(s), the mechanical assemblies, the control firmware, tooling, and more—with weight and balance checked on every CAD change. Since you can make decisions based on a simulation that closely simulates the physics of reality (I would say within one order of magnitude of deviation), it can easily hyper optimize for specific use cases, such as weight, power saving, functionality or precision, all at your direction. You can have it generate hundreds of different variations for a part, run them all (sometimes overnight) to get the data you need, and make the decision based on that. In my personal project I currently have around 800GB of simulation data archived after only a few weeks, but a lot of work to show for it. Stripped out my project stuff and open sourced the method + a Claude Code skill that sets it up for you. You do not need to keep using the skill, it simply is a good starting point. https://github.com/Kemerd/claude-hardware-in-the-loop With this, you can essentially create anything you'd like, test it in a virtual world, then order the parts, CNC what you need to, print what you need to, assemble it, and have it closely resemble the simulation results. Fair warning, this process can use a LOT of tokens. Make those projects you've wanted to create but haven't had the time real!
