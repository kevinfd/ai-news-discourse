---
id: "df7a3c250cf65cee"
title: "Show HN: Pidgeon – Email inboxes for AI agents"
url: "https://pidgeon.ai"
link: "https://pidgeon.ai"
source: "Pidgeon"
domain: "pidgeon.ai"
source_type: "community"
collector: "hackernews"
date: "2026-10-29T12:55:12Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["patrickcneuhaus"]
language: "en"
summary: "Send mail at volume\nFig001\nNotifications, outreach and follow-ups, each sent from the agent’s own address.\n- Residency\n- Hosted in the EU\n- Training\n- We never train on the content of your mail\nProduct\nPidgeon equips your agents with powerful, programmatic inboxes.\nExplore the product\nRead what comes in, answer in the same thread, and hand it to a person when it needs one.\nSet up meetings,…"
tags: []
orgs: ["EU"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 392
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50288172"
score: 10
comments: 2
community: "Hacker News"
---

# Show HN: Pidgeon – Email inboxes for AI agents

Pidgeon · patrickcneuhaus · 2026-10-29

Send mail at volume
Fig001
Notifications, outreach and follow-ups, each sent from the agent’s own address.
- Residency
- Hosted in the EU
- Training
- We never train on the content of your mail
Product
Pidgeon equips your agents with powerful, programmatic inboxes.
Explore the product
Read what comes in, answer in the same thread, and hand it to a person when it needs one.
Set up meetings, confirm bookings and deal with changes, all by email.
Pull the details out of invoices, forms and attachments.
Pass on tasks, share results and keep the whole exchange in one thread.
Register for third-party tools with its own address, never your credentials, and every code comes with a Firewall verdict.
A person takes the thread; the agent stops, and picks up again when it is handed back.
Features
Send and receive, read whole threads, and start your workflows when mail arrives.
Read more
Give any agent its own inbox with a single API call.
Every reply, forward and follow-up kept together in one conversation.
Send and receive mail from code, formatted the way people expect to read it.
Files and documents go in and out with the message itself.
Get started
From your own code, or from the agent you already use.
Read the quickstart
TypeScriptquickstart.ts
npm install @pidgeon-ai/sdkimport { client, identitiesCreate } from '@pidgeon-ai/sdk'; client.setConfig({ auth: () => process.env.PIDGEON_API_KEY! }); const { data } = await identitiesCreate({  body: { address: 'scout@pidgeon.email', type: 'agent' },  throwOnError: true,});console.log(data.data.email);
Outputscout@pidgeon.email
Security and control
Screened, scoped, kept in the EU, and logged.
Read about security
01Firewall
Every inbound message is read first. Hidden instructions are named; your agent reads the clean copy.
02EU residency
Mail, the API and your data are stored and processed in the EU, on every plan.
03Scoped keys
One address, one level of access. A key can only make keys narrower than itself.
0490-day audit trail
Every event logged, to read and replay. It cannot be deleted earlier.
- DPA
- Applies automatically
- SOC 2
- In progress
- In transit
- TLS everywhere
- At rest
- Encrypted, KMS
Paste one prompt, or make the call yourself. It is free to start.
Any agentprompt
Read https://pidgeon.ai/skill.md and follow the instructions to get your own inbox.
The full API reference is at https://pidgeon.ai/openapi.json
SignupTwo calls, and one code emailed to you
