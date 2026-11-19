---
id: "b1b58dd398505291"
title: "AI found a hole in Java, and it starts with 'AAAAAAAA...'"
url: "https://engadget.com/2320797/ai-found-a-hole-in-java-and-it-starts-with-aaaaaaaa"
link: "https://engadget.com/2320797/ai-found-a-hole-in-java-and-it-starts-with-aaaaaaaa"
source: "Engadget"
domain: "engadget.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T17:59:47Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Will Shanklin", "staff@engadget.com (Will Shanklin)"]
language: "en"
summary: "The bug could let hackers take over systems at banks, hospitals and most Fortune 500 companies."
tags: ["News"]
orgs: ["OpenAI", "Microsoft", "Apple", "Oracle"]
topics: []
content_source: "fulltext"
word_count: 310
paywalled: false
image: "https://www.engadget.com/img/gallery/ai-found-a-hole-in-java-and-it-starts-with-aaaaaaaa/l-intro-1795024736.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# AI found a hole in Java, and it starts with 'AAAAAAAA...'

Engadget · Will Shanklin, staff@engadget.com (Will Shanklin) · 2026-11-18

AI found a hole in Java, and it starts with 'AAAAAAAA...'
The bug could let hackers take over systems at banks, hospitals and most Fortune 500 companies.
If the last week is any indication, the coming months and years will be a wild ride for digital infrastructure. After outages at Microsoft, the FAA, banks, Apple and... seemingly everything else, we've now learned that a bug in the programming language Java can be used to take over computer systems.
Researchers at cybersecurity startup Calif discovered the flaw with help from OpenAI's GPT-6 Cyber model, which isn't yet publicly available. On some machines, feeding Java's base64 decoder a string of 64 "A" characters followed by an equals sign triggers a memory error. Usually, that leads to a crash. But when finessed in specific ways, it can be used to gain full unauthorized access to the system.
Calif showed that the bug could be used to hack into Keycloak, a widely used login system protecting organizations like CERN and NASA. Java is everywhere, powering platforms for banks, hospitals, airlines and government agencies; it's used by about 90 percent of Fortune 500 companies.
Fortunately, Calif says the bug isn't easy to weaponize, which should give defenders some breathing room. Oracle shipped a critical patch update on Tuesday without specifically mentioning this bug, and the Cybersecurity and Infrastructure Security Agency (CISA) told organizations to patch their systems immediately. Still, some systems will inevitably go unpatched, and Calif estimates that the bug could linger for five to 10 years.
Taken alone, the incident is troubling enough. Although officials' public statements haven't linked the past week's outages to AI, the events paint a picture of aging digital infrastructure unprepared for what's next. It turns out that "AAAAAAAA..." isn't only the way into unpatched computers; it's also what we'll increasingly be saying as this 21st-century arms race unfolds.
