---
id: "c3e82675d569c730"
title: "Grok Build coding agent leaks oodles of confidential info, some belonging to SpaceXSI"
url: "https://arstechnica.com/security/2026/11/grok-build-coding-agent-leaks-oodles-of-confidential-info-some-belonging-to-spacexsi"
link: "https://arstechnica.com/security/2026/11/grok-build-coding-agent-leaks-oodles-of-confidential-info-some-belonging-to-spacexsi"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T21:12:59Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Dan Goodin"]
language: "en"
summary: "Grok Build, the vibe-coding agent from SpaceXSI, is leaking data—some of it proprietary business information and other sensitive secrets—from thousands of its users, including the very same Elon Musk-owned company that offers the platform, new research shows. \n The information is revealed through links allowing Grok Build users to share their apps with others. Grok takes steps to randomize the…"
tags: ["AI", "Biz & IT", "Security", "grok build", "privacy", "vibe coding"]
orgs: ["xAI", "Tesla"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 390
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/11/grok-plugin-marketplace-1152x648.webp"
discussion_url: null
score: null
comments: null
community: null
---

# Grok Build coding agent leaks oodles of confidential info, some belonging to SpaceXSI

Ars Technica · Dan Goodin · 2026-11-10

Grok Build, the vibe-coding agent from SpaceXSI, is leaking data—some of it proprietary business information and other sensitive secrets—from thousands of its users, including the very same Elon Musk-owned company that offers the platform, new research shows.
The information is revealed through links allowing Grok Build users to share their apps with others. Grok takes steps to randomize the URLs so only people who know the exact URL can access the data stored there. A design decision by developers of the platform, however, completely torpedoes that objective and makes it possible for anyone to enumerate thousands of live Grok Build projects. Except in rare cases, clicking those links opens the app and reveals all data associated with it.
You had one job
Research from security firm Claroc shows that the exposed data includes things like internal business plans, ad proposals, medical exam results, galley checklists from a celebrity cruise line, and employee names and ID numbers. Ironically, some of the sensitive data comes from two-dozen apps built by SpaceXSI (the name of the now-merged SpaceX and xAI) itself. A small sampling of the documents revealed in the SpaceXSI apps—Claroc found 24 of them—include an onboarding plan, marked confidential, for a new member of SpaceXSI’s enterprise sales team, a sales territory map of 594 accounts, internal system addresses for sales team tools, and advertising proposals.
“We were shocked,” Claroc said in a Tuesday post. “The company that makes Grok had its own internal material open to anyone holding the link, and we had never been given it. Had the sales team bought a tool for this, it would have sat behind company sign-in, open only to the team. Built with AI, it went live open to anyone with the link.
Claroc notified SpaceXSI of the privacy spill on Sunday. When no one responded, a Claroc official took to X to tag both Musk and Grok Manager Matt Palmer about the threat. At the time this post went live almost all data remained available with one notable exception: the contents from the 24 SpaceXSI apps. All of them were exposing the information on Monday evening. SpaceXSI began removing the links within a few hours of Ars sending an email with questions for this article. At the time this post went live, links for all 24 apps returned an “app not found” error.
