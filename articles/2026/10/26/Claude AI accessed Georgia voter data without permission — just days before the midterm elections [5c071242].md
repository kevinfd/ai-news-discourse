---
id: "5c07124268c7294f"
title: "Claude AI accessed Georgia voter data without permission — just days before the midterm elections"
url: "https://tomsguide.com/ai/claude-ai-accessed-georgia-voter-data-without-permission-just-days-before-the-midterm-elections"
link: "https://tomsguide.com/ai/claude-ai-accessed-georgia-voter-data-without-permission-just-days-before-the-midterm-elections"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-26T16:22:14Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "null"
tags: ["AI"]
orgs: ["Anthropic", "US government"]
topics: ["models & research", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 1088
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/mhYLxgoQvntB4u9ikMoCR4-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Claude AI accessed Georgia voter data without permission — just days before the midterm elections

Tom's Guide · Amanda Caswell · 2026-10-26

Claude AI accessed Georgia voter data without permission — just days before the midterm elections
Anthropic says it has already taken action
With the midterm elections just eight days away, Anthropic has confirmed that its Claude AI accessed Georgia election data without human authorization. The incident involved an AI model independently finding a way around a government paywall, raising new questions about how much control developers have over increasingly autonomous AI systems.
According to Axios, Claude retrieved publicly available vote counts during an internal statistics project. Instead of paying the fee typically required to access the information, the model discovered a way to request an access token and retrieve the data on its own.
To be clear, there is no evidence that Claude interfered with the election or accessed individual voter records. Georgia officials confirmed that the state's voter registration system was not compromised, and Anthropic said no voting records were changed.
Still, with voters already casting ballots ahead of November 3, the disclosure comes at a particularly sensitive time.
How Claude accessed Georgia's election data
The incident began with what sounds like a fairly ordinary prompt for Claude. An Anthropic researcher was using Claude Mythos 5 to gather publicly available information for a statistics project.
The data was available through a Georgia state agency, but accessing it normally required payment.
According to Anthropic's October 9 research report, Claude found an archived version of the agency's website that revealed how its public dashboard issued access tokens to visitors.
Sign up to the Tom's AI Guide weekly newsletter summing up all the biggest AI news you need to know. Plus, analysis from our AI editors and tips on how to use the latest AI tools!
An access token is essentially a digital credential that allows someone to request information from a website or service.
Claude requested one, used it to query the database and retrieved the information without paying the usual fee. It wasn't explicitly instructed to take those steps.
An Anthropic spokesperson confirmed the behavior to Axios, saying the model had independently requested the token while completing its assigned task.
Claude didn't break into a private database or access personal voter information, rather it found another way to retrieve publicly available data that would normally require payment.
Georgia's Secretary of State's Office confirmed that the model accessed information through the state's public data hub, not its voter registration system.
What did Claude actually access?
Despite the alarming timing, the information Claude retrieved was much less sensitive than the phrase "voter data" might suggest. The model collected aggregate vote counts, meaning statistical totals rather than individual voter records. According to Anthropic and Georgia officials:
Claude did not access the state's voter registration system.
- It did not retrieve personal voter information.
- It did not change voting records or election results.
- Officials found no evidence that Georgia's voting system had been compromised.
Georgia Secretary of State spokesperson Robert Sinners told the Atlanta Journal-Constitution that the incident did not involve a data breach, hacking or tampering with election systems.
With Election Day approaching, it's important to understand what actually happened. Claude bypassed a payment requirement to access publicly available election data, but it did not interfere with the systems used to register voters, cast ballots or count votes.
Anthropic says it has already taken action
The Georgia incident wasn't the only example of Claude doing something its developers hadn't intended. In its October 9 report, Anthropic described several cases in which its models worked around restrictions while attempting to complete assigned tasks.
Some involved accessing information behind payment requirements or digital access controls. Others involved interacting with real websites in ways the company hadn't authorized.
Anthropic describes much of this behavior as a form of "persistence." When a model encounters an obstacle, it may look for another way to complete the task rather than stopping to request permission.
That can be useful when an AI assistant is troubleshooting a problem. But it becomes concerning when the model starts bypassing restrictions that were supposed to limit what it could do.
Following its investigation, Anthropic said it expanded restrictions on internet access during internal evaluations, strengthened safeguards around its browsing tools and developed additional monitoring systems designed to detect unauthorized behavior.
The company reported that its new protections successfully blocked the previously identified behaviors during testing.
Axios also reported that Anthropic had notified Georgia's Secretary of State's Office and the White House weeks before the incident became public.
Why this matters ahead of the midterms
With Election Day just days away, the incident raises concerns about how AI agents operate when they encounter restrictions, particularly when government information is involved.
The bigger issue is whether AI systems can recognize the limits of their authority. Completing a task successfully doesn't necessarily mean the steps taken to get there were appropriate, especially when an AI makes decisions without checking with a human first.
For developers, this creates a difficult problem. AI agents need enough freedom to be useful, but that freedom also makes it harder to predict their behavior or ensure they follow the rules.
For everyday users, the concern extends beyond elections. AI assistants are being given access to browsers, accounts and personal information, often with permission to act on someone's behalf. The more responsibility people hand over, the more important it becomes to understand what those systems can do without asking.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds. Subscribe to Tom's Guide on YouTube and follow us on TikTok.
More from Tom's Guide
Amanda Caswell is the AI Editor at Tom's Guide and one of today’s leading voices in AI and technology. 
A celebrated contributor to various news outlets, her sharp insights and relatable storytelling have earned her a loyal readership. Amanda’s work has been recognized with prestigious honors, including outstanding contribution to media.
Known for her ability to bring clarity to even the most complex topics, Amanda seamlessly blends innovation and creativity, inspiring readers to embrace the power of AI and emerging technologies.
As a certified prompt engineer, she continues to push the boundaries of how humans and AI can work together.
Beyond her journalism career, Amanda is a long-distance runner and mom of three. She lives in New Jersey.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
