---
id: "90dc49a53128ddb5"
title: "With High-Stakes AI, The Safest Answer Is Sometimes No Answer"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/20/with-high-stakes-ai-the-safest-answer-is-sometimes-no-answer"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/20/with-high-stakes-ai-the-safest-answer-is-sometimes-no-answer"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-20T10:30:00Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Murali Rajendran, Forbes Councils Member"]
language: "en"
summary: "In high-stakes work, providing a wrong answer can be dangerous."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["safety & ethics", "policy & regulation", "models & research"]
content_source: "fulltext"
word_count: 818
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6a68aa987256a101f6a2d4e1/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# With High-Stakes AI, The Safest Answer Is Sometimes No Answer

Forbes · Murali Rajendran, Forbes Councils Member · 2026-10-20

Murali Rajendran, Founder & CEO of PracticeVantage Consulting and co-founder/CTO of Ariv Health, building AI for regulated industries.
Software is built to be helpful, and helpful usually means always returning some kind of result, even when it’s only a recommendation or a best guess.
For most products, that instinct is correct. In high-stakes work, however, it can be dangerous.
I have spent most of my career building high-stakes systems in healthcare, financial services and government. In those settings, a confident wrong answer is often worse than no answer at all. Providing no answer at least makes a person stop and think, while a wrong answer that looks right makes them act.
To Answer Or Not To Answer
Engineers have a name for whether a system should provide an answer: fail-open or fail-closed. A system that fails open keeps running when something breaks, hoping for the best. A system that fails closed stops and refuses to continue when something goes wrong.
Physical locks have to pick one or the other when the power goes out, as do the systems we are now putting in front of people to help them make decisions.
AI has raised the stakes on that choice. Modern models are confident even when they are wrong, and confidence reads as authority.
An AI model will hand you a clean, well-worded, completely incorrect answer with the same confidence it uses for a correct one. The person on the other end has no easy way to tell the two apart.
Over time, they stop trying, which could lead to the slow erosion of the habit of checking, which is a much bigger risk than an occasional bad output.
What Building A Fail-Closed AI System Looks Like
When my company built a healthcare platform, we made refusal a feature. It sits on more than 120 million verified claims, and the operative word is verified. If a number cannot be traced to a source we trust, the platform does not estimate it. It shows nothing, and it says why.
Also, if a user is not entitled to see a piece of protected information, they do not get a redacted hint that something is there. They get nothing. That protection lives below the application layer, so a mistake in the interface cannot leak what the data layer already refused to release.
That point matters more than it sounds. A guardrail written into a prompt or bolted onto the front end is a guardrail you will eventually drive straight through.
If someone ships a new screen, an API changes or an edge case slips past, and the only thing between a user and the wrong answer is a line in a prompt, you do not have a real guardrail. The refusal has to be enforced in the part of the system that does not get rewritten every sprint.
I acknowledge that there are very real costs to designing systems this way. Saying “I do not know” feels like weakness, and there is always pressure to fill the silence with something. A system that refuses looks less impressive in a demo than one that answers everything.
While you may lose the demo, what you gain is the thing that compounds. People begin to trust what the system does say, because they have learned it will not bluff. Once an operator trusts that the platform will go quiet rather than guess, they will be more likely to hand it bigger decisions.
Trust earned that way lasts in a way that a high accuracy score on a slide never will.
Considerations When Building A Fail-Closed AI System
If you are building in this direction, a few things have held up for me:
• Decide what unsure means, and give the system a way to say it. Abstention should be a real answer your model is allowed to return, not an error you patch around after the fact.
• Verify the inputs before you reason over them. Garbage in no longer produces obvious garbage out. It produces confident, well-formatted garbage, which is far more expensive to catch.
• Measure the cost of a wrong answer, not only your accuracy. In regulated work, the gap between a miss and a false certainty is enormous, and a single accuracy number hides it.
• Put the refusal where the code is stable. If it lives where the product changes weekly, it will not last the year.
I do not think this is only a healthcare problem, or only an AI problem. Any time you place a system between a person and a decision that matters, you are choosing what it does when it is not sure.
Most teams make that choice by accident. In the work I care about, the systems worth trusting are willing to say nothing at all on purpose.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
