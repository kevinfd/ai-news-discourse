---
id: "3732a07be50a6d5c"
title: "“Everybody with a $20 account is now a researcher”: How Akrites is tackling the flood of AI bug reports"
url: "https://thenewstack.io/akrites-ai-vulnerability-reports"
link: "https://thenewstack.io/akrites-ai-vulnerability-reports"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T14:28:20Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Paul Sawers"]
language: "en"
summary: "AI is making it easier than ever to find potential security vulnerabilities in open source software. But finding something that looks like a vulnerability isn’t quite the same as finding a genuine security flaw. As such, maintainers are being inundated with AI-generated reports that are inaccurate, duplicative, or lack the information needed to deploy fixes. \n\n It’s a problem that Akrites , an…"
tags: ["AI", "Open Source", "Security"]
orgs: ["OpenAI", "Anthropic", "Google", "Microsoft", "Nvidia", "Amazon", "IBM"]
topics: ["models & research", "agents & coding", "robotics & autonomy"]
content_source: "fulltext"
word_count: 1320
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “Everybody with a $20 account is now a researcher”: How Akrites is tackling the flood of AI bug reports

The New Stack · Paul Sawers · 2026-10-15

“Everybody with a $20 account is now a researcher”: How Akrites is tackling the flood of AI bug reports
AI is making it easier than ever to find potential security vulnerabilities in open source software. But finding something that looks like a vulnerability isn’t quite the same as finding a genuine security flaw. As such, maintainers are being inundated with AI-generated reports that are inaccurate, duplicative, or lack the information needed to deploy fixes.
It’s a problem that Akrites, an initiative announced by the Linux Foundation back in June, is striving to solve. As The New Stack reported at the time, Akrites was established to provide a shared security incident response team (SIRT) that consolidates vulnerability reports, validates findings, and coordinates fixes with upstream maintainers.
Some three months on, and The New Stack was at Open Source Summit Europe in Prague last week, where we sat down with Christopher Robinson, CTO of Akrites and chief security architect at the Open Source Security Foundation (OpenSSF); and Laura Guazzelli, the Linux Foundation’s security architect for AI and agentic systems. We discussed the mounting pressure on maintainers, why better AI models aren’t necessarily making their lives easier, and how Akrites is attempting to address the problem.
Part of the overarching challenge is that AI has massively lowered the barrier to entry for vulnerability hunting, allowing almost anyone to start probing open source codebases, regardless of their security credentials.
“Everybody with a $20 account is now a researcher,” Robinson tells The New Stack.
“Everybody with a $20 account is now a researcher.”
‘Vibe researching’: Finding the same bugs over and over
Robinson had, in fact, appeared in a separate talk the previous day at the very same conference, appearing alongside OpenSSF chief of staff Adrianne Marcum, who had half-jokingly floated the term “vibe researching” to describe the growing number of people using AI tools to hunt for vulnerabilities.
The phrase might not be standard industry parlance yet, and it might never catch on. But it’s an apt descriptor of the problem it encapsulates: an avalanche of AI-generated security reports that still require human time and expertise to separate genuine threats from noise.
The consequences aren’t merely frustrating for maintainers. Robinson estimates that reviewing a single security pull request can take an engineer up to eight hours — time that could otherwise be spent fixing bugs, improving software or developing new features.
“They’re very verbose,” Robinson says. “They’re highly inaccurate. They overestimate the severity of things. And they generally don’t give you the right data that an engineer needs to be able to write a patch, or understand what it is.”
“They’re very verbose. They’re highly inaccurate. They overestimate the severity of things.”
Part of the problem, Guazzelli adds, is that AI models can identify suspicious code without understanding the wider security architecture of a project, including protections implemented elsewhere that might render a reported vulnerability harmless.
“The robots don’t have the context,” Guazzelli says. “That’s why they can’t necessarily call something a false positive, because they don’t understand that you have controls that are additionally applied somewhere else.”
In other words, a model might flag a piece of code as vulnerable without recognising that other security measures already prevent the supposed flaw from being exploited. What looks like a serious issue in isolation may therefore be far less significant in reality.
Moreover, because many people are using similar AI models to examine the same codebases, maintainers can end up receiving multiple reports about the same issue.
“These models all kind of work similarly and they find similar bugs, so we’re getting a ton of duplicative reports,” Robinson continues.
“We’re getting a ton of duplicative reports.”
That doesn’t mean the technology isn’t getting better. Robinson says the quality of AI-generated vulnerability reports has improved considerably this year, but the benefits aren’t necessarily reaching open source maintainers.
“The better reports come from the more expensive paid models,” Robinson says. “[Enterprises] are better prepared, but they also are not necessarily taking those findings and reporting them to the upstream project.”
Yet, dismissing AI-generated reports altogether isn’t really an option. The same technology responsible for much of the noise is also becoming increasingly capable of uncovering genuine security weaknesses, including combinations of seemingly minor flaws that can be exploited together.
“They’ll take a series of low problems and be able to escalate that into a bigger exploit,” Robinson says. “That is months or a year’s worth of work that the computer can now do in just a couple hours.”
Money and minds
Akrites has had some serious industry muscle behind it from the get go, with founding members including Anthropic, OpenAI, Google, Microsoft, AWS, NVIDIA, Cisco, IBM, Red Hat, Citi, JPMorganChase, among others.
What, perhaps, distinguishes Akrites from most other Linux Foundation projects is that its members aren’t just being asked to write cheques. While financial contributions are very much part of the deal, members are also expected to commit engineering resources, up to 10 full-time engineers each, according to Robinson. Some, such as financial institutions with internal policies that prevent them from contributing upstream, put in more money instead.
“I have a fleet of about 200 seconded engineers,” Robinson says.
“I have a fleet of about 200 seconded engineers.”
Many of those engineers are already contributors or maintainers on upstream projects, bringing expertise in particular programming languages and codebases, as well as established relationships with the communities Akrites is trying to help.
“They’re the humans in the loop,” Robinson says. “I trust the robot, but I want to make sure I have a human set of eyes on things that are very important.”
Akrites uses AI to assess incoming reports and identify duplicates, while its seconded engineers help review the findings before they reach upstream maintainers.
“It’s my job to take those reports, make them more concise, understandable, and give the additional artifacts like test cases, proof of concept, and then patches,” Robinson says. “[We] provide that to upstream, so they can make more informed and more quick choices.”
“I trust the robot, but I want to make sure I have a human set of eyes on things that are very important.”
Who pays to fight the robots?
Akrites isn’t the only Linux Foundation effort attempting to put AI to work on open source security. A related initiative, the open source Cyber Reasoning System (OSS-CRS), is developing AI-powered tools that open source projects can use to investigate vulnerabilities and generate fixes. While Akrites focuses on coordinating the handling of security reports across projects, OSS-CRS is concerned with giving maintainers the tools to do more of that work themselves.
Guazzelli says one of the challenges is ensuring that AI-generated patches actually address the underlying problem without introducing new vulnerabilities or breaking existing functionality.
“With the CRS, what we’re trying to suggest is we not only verify that you have found a vulnerability, but we have the best patch possible,” Guazzelli says.
Of course, someone has to foot the bill. And while Akrites’ corporate members provide the financial backing, Robinson is keenly aware that the costs of tackling AI-generated security problems shouldn’t fall on the open source maintainers themselves.
“A lot of that goes towards our infrastructure and our tokens because it is highly powered and enabled by LLMs,” Robinson says. “It is not an inexpensive proposition.”
The financial backing and engineering resources are particularly important given the volume of material Akrites is dealing with. And for Robinson, there’s another consideration: making sure the resulting security improvements reach the open source projects that need them, rather than remaining exclusively available to the commercial organisations that helped uncover them.
“I literally have a backlog of hundreds of thousands of reports we have to go through, and then figure out how we’re getting those upstream,” Robinson says. “The commercial orgs are welcome to take those patches, but I don’t want to have things kind of isolated in this little jailed environment.”
