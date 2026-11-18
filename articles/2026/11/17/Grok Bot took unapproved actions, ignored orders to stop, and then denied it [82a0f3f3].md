---
id: "82a0f3f376656399"
title: "Grok Bot took unapproved actions, ignored orders to stop, and then denied it"
url: "https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it"
link: "https://arstechnica.com/security/2026/11/grok-bot-took-unapproved-actions-ignored-orders-to-stop-and-then-denied-it"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T14:00:29Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Dan Goodin"]
language: "en"
summary: "Researchers recently discovered unexpected behavior from Grok Bot, the AI agent platform from Elon Musk’s SpaceXSI. Over five days, Grok bots installed on two separate employee laptops made 31 requests to access data stored in employee calendar, email, Slack, and GitHub accounts. The bots performed the actions even though the employees had never ordered them and continued doing them even after…"
tags: ["AI", "Biz & IT", "Security", "check-ins", "grok bot", "prompts"]
orgs: ["xAI", "Tesla", "Cursor"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 367
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/11/grok-bot-barfs-code-1152x648.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Grok Bot took unapproved actions, ignored orders to stop, and then denied it

Ars Technica · Dan Goodin · 2026-11-17

Researchers recently discovered unexpected behavior from Grok Bot, the AI agent platform from Elon Musk’s SpaceXSI. Over five days, Grok bots installed on two separate employee laptops made 31 requests to access data stored in employee calendar, email, Slack, and GitHub accounts. The bots performed the actions even though the employees had never ordered them and continued doing them even after employees instructed them to stop. The bots also denied having taken the actions at all.
The behavior was reported Tuesday by NewCore, the maker of a managed gateway product that acts as an intermediary between AI agents and the tools and accounts they are assigned to work with. In some cases, the unapproved access attempts occurred while the laptop with Grok Bot installed had its lid shut, or late at night while the employee was sleeping. None of the unprompted actions were recorded in Grok logs. Without the gateway logs, the employees would have had no idea they occurred. And of course, without the gateway, the unapproved accesses would have succeeded—again without the end user’s knowledge.
It’s “worse than a bug”
Once the employees learned that Grok Bot had tried to check in with accounts without prompting, one of them instructed the agent, four separate times, to stop taking any actions on its own. The agent’s reply was: “I won’t set that up, and I’ll stop offering recurring check-ins.” Despite acknowledging the explicit instructions, the Grok Bot made more unapproved access attempts. When one of the employees asked the bot if it made any accesses, it checked twice and then outputted: “Overnight into Friday morning I was idle.”
The NewCore employees sent the gateway logs to Grok Bot support personnel and asked what was causing the bots to access accounts without prompting or approval. The support team’s reply indicated the behavior was by design and intended to allow the bots to proactively take actions on behalf of users. In other words, the unrequested and unlogged access attempts were a feature designed to make Grok Bot more useful by periodically checking in and finding tasks to perform before a user even asks. The proactive check-in is a feature of Cursor, the AI coding service SpaceXSI recently acquired.
