---
id: "10b564e827bae0ba"
title: "AI Is Already Critical Infrastructure. The AI Harness Is The Part You Own"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/20/ai-is-already-critical-infrastructure-the-ai-harness-is-the-part-you-own"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/20/ai-is-already-critical-infrastructure-the-ai-harness-is-the-part-you-own"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-20T11:30:00Z"
published_date: "2026-11-20"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Pavel Bykov, Forbes Councils Member"]
language: "en"
summary: "Banning AI isn't realistic; instead, we must treat it as the business continuity concern it really is."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "safety & ethics"]
content_source: "fulltext"
word_count: 1019
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ad13d140b6ddf17e1d37c1f/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# AI Is Already Critical Infrastructure. The AI Harness Is The Part You Own

Forbes · Pavel Bykov, Forbes Councils Member · 2026-11-20

Pavel Bykov is the Co-Founder and CEO of IP Fabric, which has been pioneering automated network assurance since 2016.
According to McKinsey’s latest State of AI survey, 44% of organizations that use AI say it’s now scaling across their enterprise, up from 38%. In many organizations, AI is still considered an experiment. But that doesn’t mean individual AI use hasn’t already become critical infrastructure, sometimes without leadership even realizing.
I heard a story about an insurance agency whose employees used “shadow” AI to respond to customers. Although that particular AI application wasn’t approved, it had already become part of the agency’s customer service workflow. If employees suddenly lost access to the model they were using, customer service would be impacted.
As AI agents start running work on their own, such dependencies will only grow deeper. Banning AI isn’t realistic; instead, we must treat it as the business continuity concern it really is.
Why AI Dependencies Are Harder To Manage
Organizations have spent two decades learning how to manage their reliance on cloud and SaaS providers. They can measure service availability, latency and other metrics, and create backups to prepare for possible outages.
AI introduces a less deterministic dependency. An AI service can stay online and keep returning answers after its behavior has changed. Dependent workflows can appear fine while producing less accurate or less complete results.
In June 2026, a U.S. export-control directive led Anthropic to suspend Claude Fable 5 for all customers. When it returned in July, Anthropic said its new safety classifier would flag benign coding and debugging requests more often, possibly sending blocked requests to an older model. In August, Anthropic retrained Fable 5’s separate biology classifier, which sends flagged requests to yet another model. Within two months of launch, Fable 5 had been suspended, rerouted and retuned, all under the same model name. If an organization wasn’t evaluating its outputs with Fable, it wouldn’t understand how these changes affected its work.
Measure Business Continuity In Terms Of Model Behavior
IT leaders need a plan for what happens if a provider changes its model, performance falls below an acceptable level or prices fluctuate. Price can move in either direction; for example, in September, Anthropic said its new Opus 5.5 model would cost about 40% less than its predecessor on typical workloads. If an organization doesn’t have the flexibility to switch models, it can’t take advantage of those savings.
A business continuity plan should start by defining an acceptable level of model performance, which can’t be left to provider benchmarks. This plan should also include a test set of problems the organization has already solved and can use to measure model performance. Present each model with a problem, withhold the known answer, and score the result. These tests should determine:
1. Did the AI model complete its task?
2. Was the result checked against an authoritative source the AI did not produce?
3. Does the model answer questions consistently, if asked multiple times?
4. What did each completed task cost?
Run this test set any time a model changes. Without this internal baseline, an organization might sense that a service has become less reliable, but be unable to demonstrate any shift in behavior.
What An AI Harness Is, And Why You Should Own It
An AI harness is often described as a layer that filters model inputs and outputs. I think about it differently: Picture a talented soccer player, alone with a ball on a planet covered in grass. His ball control is perfect, and he can run the ball around the planet endlessly. It is impressive, and it is pointless.
To make this a game, you need lines, goal posts, rules, referees, a scoreboard and a stadium. A harness is all of those things for AI. It gives the model a goal and defines what a successful output is. It determines which data and systems that AI may touch. It also keeps a record that helps organizations learn, as corrections and verified reference data stay in the harness, rather than in the model itself.
Any soccer game requires an impartial referee. In my field, if an AI agent proposes a firewall change, then that proposed change must be checked against a model of network behavior that the agent did not build or edit. The system that validates a change should never be the system that made it.
AI harnesses also ensure business continuity throughout times of change. On any soccer team, players can get injured or transferred, but the club keeps its stadium, its rules and its record. When my company changed its AI subscription, I had AI rebuild my workflow setup into a portable harness in a folder I control. This harness also helps me to run the same tests across several models and pick the one that fits each workflow, rather than assuming the most expensive one is best.
Decide Which Parts Of The Game You Must Own
You don’t need to own every data center or chip in your AI stack to stay in control, but you do need to decide which parts of the stack you own, because providers are moving the harness itself into their clouds. OpenAI’s new always-on agents each live in the cloud. These agents don’t support data residency, and their cloud orchestration events don’t reach the customer’s existing telemetry collector, but when the referee, the stadium and the record all belong to the provider, the provider’s changes become yours.
An organization may allow hosted models and provider-run agents for low-risk work, but require business-critical workflows to adhere to rules, reference data, tests and records in systems you control, running the model privately where the data requires it. To draw these lines, organizations need visibility into how teams and applications actually use AI.
Ultimately, organizations can’t control when a provider updates their model, but they can control the harness they put around AI. That governance is the key to keeping critical workflows running, no matter how the models underneath them may change.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
