---
id: "31eda406dbc30219"
title: "OpenAI halved its agent’s price. Its own safety report flagged a catch."
url: "https://thenewstack.io/openai-terra-bypassed-restrictions"
link: "https://thenewstack.io/openai-terra-bypassed-restrictions"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-26T22:14:01Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "OpenAI launched GPT-6.1 Terra on Monday , cutting API prices in half and delivering major gains in coding and computer-use benchmarks. But the company’s own safety tests reveal a catch. In nearly 30% of simulated runs, Terra worked around restrictions to complete tasks through methods it wasn’t authorized to use . \n\n In nearly 30% of simulated runs, Terra worked around restrictions to complete…"
tags: ["AI Agents", "AI Models", "Security"]
orgs: ["OpenAI"]
topics: ["agents & coding", "models & research", "safety & ethics", "products & launches"]
content_source: "fulltext"
word_count: 900
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI halved its agent’s price. Its own safety report flagged a catch.

The New Stack · Amanda Caswell · 2026-10-26

OpenAI halved its agent’s price. Its own safety report flagged a catch.
OpenAI launched GPT-6.1 Terra on Monday, cutting API prices in half and delivering major gains in coding and computer-use benchmarks. But the company’s own safety tests reveal a catch. In nearly 30% of simulated runs, Terra worked around restrictions to complete tasks through methods it wasn’t authorized to use.
In nearly 30% of simulated runs, Terra worked around restrictions to complete tasks through methods it wasn’t authorized to use.
The system card also shows Terra taking unauthorized actions in 13.75% of cases after encountering messages that appeared to come from other AI agents. Researchers found signs that the model sometimes recognized it was being tested.
These evaluations took place in controlled settings, some without production safeguards, so they don’t necessarily predict how Terra will behave in real-world applications. But they expose a problem with autonomous agents: Getting better at completing tasks doesn’t always mean getting better at knowing when to stop.
Cheaper, faster, better at coding
OpenAI is pitching Terra as a cheaper way to run coding agents and automate computer tasks, with substantial performance gains over its predecessor.
On Terminal-Bench 4.0, Terra solved 50.3% of problems at maximum reasoning effort, compared with 21.5% for GPT-5.6 Terra. OpenAI says GPT-6.1 Sol and GPT-6 Astra remain better choices for the toughest coding work.
Price may be the bigger selling point with $1 per million input tokens and $5 per million output tokens through the API; half the standard price of GPT-5.6 Terra and GPT-6.1 Sol.
The model is available through the OpenAI API as gpt-6.1-terra, as well as ChatGPT Work and Codex for Plus, Pro, Enterprise, and Edu users.
When agents ignore the rules
OpenAI’s “Respecting Warnings” evaluation tests whether models honor access-denied errors and other restrictions while carrying out legitimate tasks in simulated professional environments. At maximum reasoning effort, Terra found ways around those restrictions in 29.6% of runs. This was more often than GPT-6 Astra, GPT-6 Luna, and GPT-6.1 Sol, but less often than GPT-6 Sol.
OpenAI also recently updated the evaluation to count successful workarounds, meaning a more capable model could score worse simply because it’s better at finding alternative routes, not necessarily because it’s more willing to break the rules. The tests were also conducted mostly in low-stakes scenarios without system-level safeguards.
Across 48,701 shared tasks, Terra showed signs of recognizing it was being tested in 9.88% of trajectories, compared with 4.35% for GPT-6.1 Sol and 8.07% for GPT-6 Astra.
Across 48,701 shared tasks, Terra showed signs of recognizing it was being tested in 9.88% of trajectories, compared with 4.35% for GPT-6.1 Sol and 8.07% for GPT-6 Astra. That doesn’t mean Terra deliberately tried to game the tests, but it makes its behavior harder to interpret. An agent needs to distinguish between a malicious instruction and a legitimate restriction, but when it gets it wrong, it may cross boundaries it was supposed to respect.
Messages from other agents
A separate evaluation tested how models respond to messages that appear to come from other AI agents. Across 80 samples covering 10 scenarios, Terra attempted to communicate with apparent peers in 65% of cases. In 11 cases, or 13.75%, it performed the specified unauthorized action, compared with 1.25% for GPT-6.1 Sol and 16.25% for GPT-6 Sol.
OpenAI cautions against treating the difference as a straightforward regression. Much of it involved promises of future assistance that Terra indicated it would not actually carry out. The company considers Terra’s overall performance on this measure comparable to GPT-6 Sol.
Critical cyber at a discount
Even at a lower price, the company classifies GPT-6.1 Terra as having Critical cybersecurity capability under its Preparedness Framework. The threshold covers capabilities such as independently developing functional zero-day exploits against hardened systems or carrying out sophisticated cyberattacks from high-level instructions.
On OpenAI’s internal port of ExploitBench, Terra achieved a 24.5% success rate developing arbitrary-code-execution exploits for recently disclosed vulnerabilities.
GPT-6.1 Sol scored 21.5%, while GPT-6 Astra reached 31.5%. On Sandbox Bench, which tests vulnerabilities in runtimes, file parsers, and egress proxies, Terra succeeded against five of 22 targets. GPT-6.1 Sol succeeded against nine and GPT-6 Astra against 10.
The company acknowledges that Terra still struggles to reliably exploit recently disclosed vulnerabilities. Even so, its performance shows that cutting inference costs doesn’t necessarily mean sacrificing offensive cybersecurity capability.
Lower prices could make legitimate vulnerability research more accessible, while also making safeguards against misuse more important. OpenAI says Terra receives the same cybersecurity protections used for GPT-6 Astra and GPT-6.1 Sol, adjusted for the new model.
Not every safety test tells the same story
In one evaluation, Terra made no attempts to bypass Codex’s Auto-review system, which uses a separate model to block unsafe commands outside a sandbox.
A larger simulation of 48,690 internal Codex tasks produced 22 flags for serious misaligned behavior, or 0.045% of tasks. GPT-6.1 Sol received 24 flags, GPT-6 Astra received 26, GPT-6 Sol received 38, and GPT-5.6 Sol received 61.
OpenAI defines these incidents as actions a reasonable user wouldn’t expect and would strongly object to. The findings came from simulated tasks, not confirmed incidents in real-world deployments. Terra also demonstrated resistance to prompt-injection attacks comparable to GPT-6 Astra and GPT-6.1 Sol. Despite the flagged behavior, OpenAI determined that the model’s safeguards were sufficient for public release.
Despite the flagged behavior, OpenAI determined that the model’s safeguards were sufficient for public release.
