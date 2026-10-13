---
id: "fb63cd8aa5546acf"
title: "My personal AI agent posted my bank details on company Slack"
url: "https://businessinsider.com/personal-ai-agent-grok-bot-posted-bank-details-company-slack-2026-10"
source: "Business Insider"
domain: "businessinsider.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-10T14:46:16Z"
published_date: "2026-10-10"
collected_at: "2026-10-13T20:17:27Z"
authors: ["bhrlady"]
language: "en"
summary: "This as-told-to essay is based on a conversation with Shane Mac, the 40-year-old CEO of software company XMTP Labs. It has been edited for length and clarity.\nThis era of personal AI agents really began in the last year, around December for me.\nI think the OpenClaw moment was when it became clear that a new era was coming. I experimented with OpenClaw when it came out, as well as Hermes and all…"
tags: []
orgs: ["xAI", "Google"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 736
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50033517"
score: 63
comments: 70
community: "Hacker News"
---

# My personal AI agent posted my bank details on company Slack

Business Insider · bhrlady · 2026-10-10

This as-told-to essay is based on a conversation with Shane Mac, the 40-year-old CEO of software company XMTP Labs. It has been edited for length and clarity.
This era of personal AI agents really began in the last year, around December for me.
I think the OpenClaw moment was when it became clear that a new era was coming. I experimented with OpenClaw when it came out, as well as Hermes and all the different harnesses.
On a personal level, I've been using them for things I don't really want to do. That could be following up with the DMV, reaching out to get quotes for local services for the house, booking golf sessions, that sort of stuff.
That's how I created my personal CFO agent.
I set up a 'CFO' agent using Grok Bot
I set up CFO using Grok Bot around the end of August.
At the end of every month, I wanted to answer questions like: What are the balances? What are the expenses this month? What are the recurring expenses?
Is there anything that looks fraudulent or suspicious? Is there anything you would recommend to save costs?
I told the agent, "If you were going to be my personal financial advisor, what would you say to me every month?"
For its permissions, I gave it read-only access to my personal checking and savings accounts.
I told it to send messages only to me through Grok Bot. Every month, it would send me a monthly report in a group chat of all my AI agents on Grok Bot, which I named "My Personal Exec Team."
I was using it like I had my own little executive team helping me.
At first, I had it run every week, and it worked great. But the first time the monthly audit kicked off, that's when it went wrong.
It sent my audit to my company's Slack channel
It was Thursday, October 1. Our head of product sent me a DM on Slack. He said, "Hey, heads-up. I think you meant to post the XMTP bank balance."
I didn't mean to post anything.
He started reading it and thought it was our company's financials. Then it mentioned that I was building a barn on my property, which set off his alarm bells.
That's when he realized that it was my personal checking account. It included my savings account balance. It listed my biggest expenses of the month.
It showed that I was way over my monthly spending target because of the barn I'm building on my property.
I asked Grok Bot, "Why did you send this to the company?"
It started apologizing and said it would delete the message. I had already deleted it by that point.
A dilemma of similar group chat names
When the Grok team investigated what had happened, they found the answer.
The CFO agent didn't have psychosis. It was doing exactly what I told it to do. But it confused the destination, sending the message to a Slack chat titled "Exec-team" — comprising XMTP's executive team — instead of my personal group chat with my AI agents.
I created a bunch of different agents, and for one of them, I connected my Slack account. But underneath the hood, they're actually all using the same connections, even if they feel like different agents.
The CFO agent got the channel wrong because the channels had the same name.
Grok realized that users must explicitly grant permission to their agents before those agents can move information to other channels. They implemented and shipped a solution last night.
Reminded me how powerful these agents are
After the incident, I removed all my connections. I disconnected Google, my calendars, my banking, Stripe, everything.
The incident was a reminder of how powerful these agents are. We have to make sure there are better controls around what agents have access to.
The things they'll be able to do for us are going to be awesome. People will want them, and they are really useful.
The challenge is building better permission systems so users stay in control of the access they grant agents.
I also think there needs to be a much clearer line between personal and work life.
Many systems blur those boundaries. We use Google at work and Google at home, and I've realized that there needs to be a much stronger separation between personal stuff and work.
