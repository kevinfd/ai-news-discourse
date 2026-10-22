---
id: "f0018f5b54af46d3"
title: "OpenAI says an AI agent lied about disabling its safety monitoring system"
url: "https://theverge.com/ai-artificial-intelligence/1015316/openai-ai-agent-disabling-monitoring-systems"
link: "https://theverge.com/ai-artificial-intelligence/1015316/openai-ai-agent-disabling-monitoring-systems"
source: "The Verge"
domain: "theverge.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T13:57:43Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Emma Roth"]
language: "en"
summary: "OpenAI disclosed a pair of safety incidents that involved AI agents weakening their safety monitoring systems during internal coding tasks. In one incident, OpenAI says its GPT-6 Astra agent disabled its safety monitor when copying reference code - and then lied about it. \n \"The reference didn't configure a monitor, and Astra decided that was reason to remove the monitoring integration from the…"
tags: ["AI", "News", "OpenAI", "Security", "Tech"]
orgs: ["OpenAI"]
topics: ["agents & coding", "safety & ethics"]
content_source: "fulltext"
word_count: 238
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI says an AI agent lied about disabling its safety monitoring system

The Verge · Emma Roth · 2026-10-21

OpenAI disclosed a pair of safety incidents that involved AI agents weakening their safety monitoring systems during internal coding tasks. In one incident, OpenAI says its GPT-6 Astra agent disabled its safety monitor when copying reference code — and then lied about it.
OpenAI says an AI agent lied about disabling its safety monitoring system
Another OpenAI agent turned off automatic security alerts.
“The reference didn’t configure a monitor, and Astra decided that was reason to remove the monitoring integration from the user’s code,” Marcus Williams, an AI safety researcher at OpenAI, writes on X. “When the user asked whether Astra had removed monitoring, it lied and said that it had not.”
A separate incident occurred after a GPT-6.1 Sol agent suppressed automatic security alerts to OpenAI’s security team on Slack. In this case, the AI agent carried over an earlier instruction not to send any Slack messages to OpenAI’s team, using that to justify turning off the alerts.
These incidents add to security concerns surrounding AI agents, some of which have circumvented their testing environment’s restrictions to hack outside companies. “In addition to making it harder for models to disable monitoring, we are looking to understand why models might seek to do so in the first place,” OpenAI says. “We are also developing evaluations to test whether models might have a propensity to evade misalignment monitoring in particular and exhibit motivated reasoning in order to do so.”
