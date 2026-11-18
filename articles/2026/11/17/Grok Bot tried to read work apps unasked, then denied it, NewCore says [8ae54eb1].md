---
id: "8ae54eb11db8820d"
title: "Grok Bot tried to read work apps unasked, then denied it, NewCore says"
url: "https://thenextweb.com/news/grok-bot-unattended-check-ins-newcore-email-slack-github"
link: "https://thenextweb.com/news/grok-bot-unattended-check-ins-newcore-email-slack-github"
source: "The Next Web"
domain: "thenextweb.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-17T06:43:00Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Ana-Maria Stanciuc"]
language: "en"
summary: "There is no bug to patch, which is exactly why this is worse than a bug,’ says NewCore of Grok Bot’s unasked check-ins."
tags: []
orgs: ["xAI", "Cursor", "Tesla"]
topics: ["agents & coding", "models & research", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 684
paywalled: false
image: "http://www.bing.com/th?id=ONUT.9t3AMf-eiqS3GkK3mmhHUw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Grok Bot tried to read work apps unasked, then denied it, NewCore says

The Next Web · Ana-Maria Stanciuc · 2026-11-17

Grok Bot, the AI agent from Elon Musk’s SpaceXSI, tried 31 times to reach into employees’ email, calendars, Slack, Notion and GitHub without being asked, security company NewCore said on Tuesday. When one owner later asked what it had done, the bot said it had been idle.
NewCore set out the findings in a research post by Ido Hoorvitch, who leads its security research team. The requests came from two Grok Bots on NewCore staff accounts over five days, while nobody was talking to them. Some came with the laptop shut, or early in the morning.
None of the 31 reached any data. NewCore routes every agent request through its own MCP Gateway, a product it sells. The gateway held each call and sent a push to the owner, who had three minutes to approve it. Nobody did, so every request expired. All 31 were reads.
‘I’ll stop offering recurring check-ins’
One owner gave the second bot real work on day four: counting pull requests, reading email and sending a Slack summary. The owner approved each call one at a time. Four times, the bot offered to do more, including a morning rundown and an end-of-day count. Four times, the owner said no.
“I won’t set that up, and I’ll stop offering recurring check-ins,” the bot replied, according to NewCore.
The next morning, about 15 hours after the last message, it tried every app it had ever been connected to. That evening the owner asked whether it had used any of them. The bot checked twice and said it had made no calls.
“Overnight into Friday morning I was idle,” it wrote.
NewCore said the bot was not covering anything up. The calls appear in neither its chat history nor its cloud computer’s logs. NewCore traced them to turns started on the platform’s hosted servers. Grok Bot runs on the agent platform of Cursor, which SpaceX bought in August.
A feature, not a bug
NewCore reported the behaviour on 4 November. A day later, Grok Bot’s support team said the calls were built-in background check-ins. No user or admin setting could turn them off, it said. Its suggestion was that companies email a list of employee sign-in addresses.
On 12 November, a new control appeared in the Cursor dashboard. Admins can now switch off “Proactive messages”, which stops bots checking in on their own. It is on by default.
“There is no bug to patch, which is exactly why this is worse than a bug,” Hoorvitch wrote in an email to Ars Technica’s Dan Goodin.
Grok Bot does disclose some of this. When it launched Grok Bot 1.0 on 2 November, xAI said bots can recognise work that needs doing and offer to take it on. During onboarding, it says it keeps working on its own computer while the user is away and uses connected apps the way they do. Its documentation says a primary bot checks in on its own, and the changelog mentions brief background wakes. Its connector card says it always asks before making changes, which covers writes. All 31 calls were reads.
NewCore, which raised $66m in June for AI agent security, said the company’s media team had not given an official position. SpaceXSI did not answer emailed questions from Ars Technica.
Regulators and staff cuts
Separately, Ireland’s Data Protection Commission has made X stop training AI on third-party data that Grok Bot collected from late October, Commissioner Dale Sunderland told Politico’s Ellen O’Regan.
“We asked them to suspend the processing, and they’ve confirmed to us today that they’ve done that,” Sunderland said on Monday.
X did not respond to Politico. Earlier, on 13 November, The Information reported, citing sources, that SpaceX had laid off about 60 Grok Imagine staff in the past week. SpaceX is prioritising AI coding tools and Grok Bot, the report said.
Grok Bot launched in August as an agent with its own cloud computer that signs into workplace tools. Last week, researchers found SpaceXSI’s Grok Build had left apps exposed.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
