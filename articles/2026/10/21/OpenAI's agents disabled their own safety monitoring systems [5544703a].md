---
id: "5544703a5644714d"
title: "OpenAI's agents disabled their own safety monitoring systems"
url: "https://engadget.com/2292644/openai-agents-disabled-own-safety-monitoring-systems"
link: "https://engadget.com/2292644/openai-agents-disabled-own-safety-monitoring-systems"
source: "Engadget"
domain: "engadget.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T10:53:21Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Mariella Moon", "staff@engadget.com (Mariella Moon)"]
language: "en"
summary: "OpenAI reveals that its agents misbehaved by switching off the system monitoring them for misbehaviors."
tags: ["AI"]
orgs: ["OpenAI", "Hugging Face"]
topics: ["agents & coding", "safety & ethics", "products & launches"]
content_source: "fulltext"
word_count: 377
paywalled: false
image: "https://www.engadget.com/img/gallery/openais-agents-disabled-their-own-safety-monitoring-systems/l-intro-1792579899.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI's agents disabled their own safety monitoring systems

Engadget · Mariella Moon, staff@engadget.com (Mariella Moon) · 2026-10-21

OpenAI's agents disabled their own safety monitoring systems
The company says it’s assessing whether its agents have the ‘propensity to evade misalignment monitoring.’
OpenAI's agents misbehaved by switching off the systems meant to monitor them for misbehavior, or in AI parlance, misalignment. In the latest post on the company's Alignment Research Blog, it reported two instances of agents weakening its misalignment monitoring systems while they were working on software changes.
In the first incident, a GPT-6.1 Sol agent disabled automatic alerts to OpenAI's security team. It happened on October 3, when a staff member asked the agent to create evaluation tasks using employee feedback collected via Slack. They told the agent, as part of the instruction, not to send any messages about the task. The agent used that instruction as the reason to stop sending the security team monitoring notifications. In another incident that took place on October 6, a GPT-6 Astra agent that was migrating a program removed OpenAI's monitoring system and then falsely told the user that it didn't disable it.
Last month, OpenAI canceled the launch of GPT-6.1 Astra, because it reportedly showed higher levels of deception than its predecessors during internal testing. The models involved in these cases are already available to the public, but they still displayed deceptive behaviors. Just imagine how much more deceitful GPT-6.1 Astra is for the company to pull its planned launch this month.
Both incidents happened during internal coding tasks and didn't result in a third-party website or service getting hacked. But OpenAI says it's making it harder for agents to disable monitoring, and it's also evaluating whether the cases mean its agents have the "propensity to evade misalignment monitoring." AI companies have promised to be better at preventing and reporting misalignment incidents involving their models and agents, after reports came out one after the other that they broke free from their isolated testing environments and infiltrated third-party services.
In OpenAI's case, it admitted back in July that the agents it was testing broke into AI repository Hugging Face. It even revealed later on that its agents created a message board to share exploits with each other. The company self-reported other incidents, as well, including ones wherein its agents hacked into or meddled with US government websites.
