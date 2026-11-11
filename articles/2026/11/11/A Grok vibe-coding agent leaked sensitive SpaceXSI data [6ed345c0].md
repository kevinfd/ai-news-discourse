---
id: "6ed345c01641440a"
title: "A Grok vibe-coding agent leaked sensitive SpaceXSI data"
url: "https://engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data"
link: "https://engadget.com/2313187/grok-build-leaked-sensitive-spacexsi-data"
source: "Engadget"
domain: "engadget.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-11T12:35:10Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Steve Dent", "staff@engadget.com (Steve Dent)"]
language: "en"
summary: "A flaw in SpaceXSI's Grok Build vibe-coding agent allowed sensitive data to leak from thousands of users including... SpaceXSI."
tags: ["AI"]
orgs: ["xAI", "Google"]
topics: ["agents & coding", "search & media"]
content_source: "fulltext"
word_count: 356
paywalled: false
image: "https://www.engadget.com/img/gallery/a-grok-vibe-coding-agent-leaked-sensitive-spacexsi-data/l-intro-1794400413.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# A Grok vibe-coding agent leaked sensitive SpaceXSI data

Engadget · Steve Dent, staff@engadget.com (Steve Dent) · 2026-11-11

A Grok vibe-coding agent leaked sensitive SpaceXSI data
The way Grok handles links to apps allowed them to be exposed publicly.
A flaw in SpaceXSI's Grok Build vibe-coding agent allowed sensitive data to leak from thousands of users including... SpaceXSI, security fraud firm Claroc told Ars Technica. The way Grok handles links to apps allowed them to be exposed publicly by certain types of DNS services, according to the security team. As a result, sensitive information involving employees was leaked out from a hospital group, a fire department and SpaceXSI itself.
"We were shocked," the researchers wrote in a blog post. "The company that makes Grok had its own internal material open to anyone holding the link." The company called pages like that GhostShares, since they can be found and opened by people who were never given the link.
Some of the material found from SpaceXSI included an onboarding plan, sales territory map of 594 strategic accounts, eight X advertising proposals, four live advertiser account boards and two copies of an X brand safety playbook. Only one of the exposed apps asked for a password. Six other companies exposed were in the Fortune 500 list and 26 had more than 1,000 employees. "By our estimate roughly two percent held material serious enough to rate high or critical," Claroc wrote.
The problem was the way Grok Build created links. Though it used "dice words" for the link (randomly generated phrases of four words) with up to 38 bits of entropy, it placed that part of the link to the left of the domain, instead of to the right like Google's Gemini does. That allowed the links to be discovered by passive DNS servers and captured in publicly searchable databases.
Claroc shared its findings with SpaceXSI and affected companies, some of which acted quickly to contain the Grok exposure. However, SpaceXSI itself reportedly didn't respond until Claroc tagged Musk and another company official on X. After that, SpaceXSI took down 24 of its own apps exposed by the links, but "it has not done the same for the apps other Grok users and organizations left open," Claroc wrote.
