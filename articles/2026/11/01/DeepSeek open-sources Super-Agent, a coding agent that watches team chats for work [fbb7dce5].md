---
id: "fbb7dce5d33bba4c"
title: "DeepSeek open-sources Super-Agent, a coding agent that watches team chats for work"
url: "https://helpnetsecurity.com/2026/11/02/deepseek-dsh-superagent"
link: "https://helpnetsecurity.com/2026/11/02/deepseek-dsh-superagent"
source: "Help Net Security"
domain: "helpnetsecurity.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-01T23:09:00Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Anamarija Pogorelec"]
language: "en"
summary: "Deepseek released a research prototype of dsh-superagent, a coding agent that does work on a GitHub repository for you. Who can ask for work The agent ..."
tags: []
orgs: ["DeepSeek"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 269
paywalled: false
image: "http://www.bing.com/th?id=ONUT.RroILS_XfuAUj9ECSdeU5Q&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek open-sources Super-Agent, a coding agent that watches team chats for work

Help Net Security · Anamarija Pogorelec · 2026-11-01

DeepSeek open-sources Super-Agent, a coding agent that watches team chats for work
Deepseek released a research prototype of dsh-superagent, a coding agent that does work on a GitHub repository for you.
Who can ask for work
The agent gets to work in two situations: an allowed user asks for something, or a rule your team wrote covers it. You can also open up a chat or GitHub scope, and then anyone in it can request work just by mentioning the agent. A message, comment or quoted document can’t expand what the agent is allowed to do, since the host is the one enforcing the lists and rules.
By default, requests that aren’t explicit, such as an unaddressed message, a bot’s message or an unlisted person’s follow-up, are assessed and recorded as ones the agent would have accepted, but none is accepted. Explicit requests, such as an allowed user mentioning the agent, work in every mode. The advice is to switch to auto after you’ve reviewed those records.
Merging
A prompt called Delivery requirements controls auto-merge, and the host adds no merge logic of its own. By default the agent doesn’t turn on auto-merge under its own account, because GitHub credits the merge to whoever enabled it. Unless the prompt names another account for merging, people merge.
dsh-superagent is available for free on GitHub.
Must read:
- 20 open-source cybersecurity tools to keep your team ready for anything
- GitHub CISO on security strategy and collaborating with the open-source community
Subscribe to the Help Net Security ad-free monthly newsletter to stay informed on the essential open-source cybersecurity tools. Subscribe here!
