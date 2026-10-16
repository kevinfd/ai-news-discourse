---
id: "22016dd971a85912"
title: "Consistency is not a localized property"
url: "https://n-the-loop.com/blog/consistency-is-not-a-localized-property"
link: "https://n-the-loop.com/blog/consistency-is-not-a-localized-property"
source: "Lobsters"
domain: "n-the-loop.com"
source_type: "community"
collector: "rss"
date: "2026-10-11T00:51:28Z"
published_date: "2026-10-11"
collected_at: "2026-10-13T20:17:27Z"
authors: ["n-the-loop.com by b--man"]
language: "en"
summary: "Comments"
tags: ["databases", "programming", "ai"]
orgs: []
topics: []
content_source: "fulltext"
word_count: 225
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Consistency is not a localized property

Lobsters · n-the-loop.com by b--man · 2026-10-11

Consistency is not a localized property
It is a common pattern for developers to assume that consistency is something they can achieve inside a single component. Apache Kafka is the cautionary tale. Making writes exactly-once took a team of distributed systems engineers years and several new components and a complete rewrite of older components (Gustafson et al. 2016).1
And after all of that, the people who built it are blunt about what you get:
Exactly-once processing is an end-to-end guarantee and the application has to be designed to not violate the property as well.(Narkhede and Wang 2017)
If the component cannot promise the property, the promise has to live somewhere else. Two practical consequences:
- Someone has to understand the system end to end. Since no component can confirm it, something outside the components has to keep it all consistent.
- Someone has to own it. Component owners will each correctly say their part works. A global property needs a person who is liable for the whole thing, with some guarantee that it makes sense.
The lesson: do not hand global, valuable properties to machines and assume they are held. Such guarantees are grounded in understanding, not code.
References
- Eight years after it shipped, the protocol still had to be redesigned to close correctness holes that could violate EOS (Olshan and Liu 2022). ↩︎
