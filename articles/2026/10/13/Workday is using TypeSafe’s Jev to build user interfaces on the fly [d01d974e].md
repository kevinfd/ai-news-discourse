---
id: "d01d974e70c13005"
title: "Workday is using TypeSafe’s Jev to build user interfaces on the fly"
url: "https://thenewstack.io/workday-is-using-typesafes-jev-to-build-user-interfaces-on-the-fly"
link: "https://thenewstack.io/workday-is-using-typesafes-jev-to-build-user-interfaces-on-the-fly"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T13:00:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Workday on Tuesday made Sana, its AI assistant, the new home screen for its HR, finance, and IT software. If you’re not an HR pro, that may not be all that exciting for you, but the way the team built this is maybe one of the most interesting use cases of Jev, TypeSafe’s decision model . Workday is building the user interface on the fly — and all of that is managed by Jev. \n\n In a demo during a…"
tags: ["AI"]
orgs: ["Anthropic", "OpenAI", "Google", "Microsoft", "Amazon", "Perplexity"]
topics: ["models & research", "agents & coding", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 925
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Workday is using TypeSafe’s Jev to build user interfaces on the fly

The New Stack · Frederic Lardinois · 2026-10-13

Workday is using TypeSafe’s Jev to build user interfaces on the fly
Workday on Tuesday made Sana, its AI assistant, the new home screen for its HR, finance, and IT software. If you’re not an HR pro, that may not be all that exciting for you, but the way the team built this is maybe one of the most interesting use cases of Jev, TypeSafe’s decision model. Workday is building the user interface on the fly — and all of that is managed by Jev.
In a demo during a press briefing ahead of the announcement, a question about a paycheck brought up a card with the amount hidden behind a click, for example, while a request for time off produced a date picker, with Sana filling in the rest of the form.
Sana, which Workday bought for $1.1 billion last year, is available now, and admins can roll it out to their users without making it the default.
Picking components instead of writing them
Joel Hellermark, Workday’s chief AI officer and Sana’s founder, said in a press briefing that the usual approach to generative UI, in which a model generates the full interface, is “quite slow.”
“If you use a classification model instead and you just give it all of the design components to pick from, you can literally do it instantly,” he said.
Workday gave Jev every atomic component in its design system and hard-coded none of the selection logic, Hellermark said, though the team also had to get data preloading right. In the demo, the paycheck card appeared before he finished typing, for example.
TypeSafe claims Jev answers in 70 to 500 milliseconds, which makes it ideal for this kind of real-time use case.
In many cases, Hellermark said, AI that works through real interface elements does significantly better than pure back-and-forth chat.
A model built to choose
According to TypeSafe, developers send Jev application data and a set of typed questions, and it returns a pick from a list of up to 255 options, a score, or a yes-or-no answer, each with a probability attached. It doesn’t generate text.
TypeSafe launched Jev on Sept. 15 with a $40 million seed round led by DCVC. On Friday, it said it raised an $870 million Series A, led by Andreessen Horowitz, at a $7.5 billion valuation. TypeSafe says a third of the Fortune 500 already use Jev but hasn’t named them. Andreessen Horowitz’s own announcement puts the figure at 25 percent, and TypeSafe’s only published case study features Jack & Jill, an AI recruiting marketplace.
There is no dearth of competition in this field, of course. OpenAI, Amazon, Cloudflare, and Perplexity have already shipped their decision models too, with Microsoft following on last week.
A pattern developers are already testing
Using Jev and similar models for building user interfaces isn’t completely new, though. CopilotKit, an open source framework for adding AI copilots to apps, published a recipe in which Jev picks which prebuilt panel to show, with an OpenAI model as the fallback.
Vercel Labs is testing a Jev mode in json-render, its framework for rendering AI-generated UIs from developer-defined components.
Andrew King, who leads solutions architecture at app developer Very Good Ventures, wrote last month that handing every closed question (one with a fixed set of answers) to Jev cut his generative dashboard’s median render time to 3.8 seconds, from 29 seconds with a frontier model composing it. His tests ran on synthetic data.
“A shape nobody anticipated cannot appear on screen,” King writes. Anything Jev answers with less than 50 percent confidence goes to a language model instead, a setup he calls “a cage with a door.”
In a test on OpenRouter’s blog using the Banking77 intent-classification set, Jev answered in a median 175 milliseconds and scored 81 percent accuracy. Claude Opus 5 scored 84.4 percent but took 2.3 seconds and cost about 22 times as much.
TypeSafe’s own documentation says Jev struggles with counting, arithmetic, and dates, leans toward whichever option is listed first, and doesn’t treat injected content as hostile by default.
Workday hasn’t said how large its design system is or what Sana does when no combination of components fits. King wrote in September that he was keeping client data off Jev because the vendor was “weeks old with no published security certification yet.” TypeSafe now offers a SOC 2 Type II report on request.
What leaves Workday
Workday recently added TypeSafe to its list of subprocessors, the outside companies that can process customer data (the ones you only think about when a SaaS service you subscribe to emails you about a change of subprocessors that you promptly forget). This entry, it’s worth noting, covers all of Workday’s product lines, not just Sana, for natural language processing, intent classification, and confidence scoring.
According to TypeSafe, Jev runs only on its hosted API and processes data in the U.S., and the company offers zero data retention to enterprise customers.
Staying inside Workday
Hellermark also showed Sana working inside Anthropic’s Claude. That’s an AI-to-AI integration, Gerrit Kazmaier, Workday’s president of product and technology, said in the briefing, and users lose the Jev-driven interface and some context along the way.
Workday’s May partnership with Google Cloud already covers A2UI, Google’s spec for agents to describe interfaces that host apps then render. MCP Apps, a Model Context Protocol extension, brings interactive UI into Claude and ChatGPT. Neither shows up in Workday’s announcements this week, so for now, it seems, employees who reach Sana through Claude get the conversation without the date picker.
