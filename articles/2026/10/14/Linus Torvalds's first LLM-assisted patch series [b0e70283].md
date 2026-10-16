---
id: "b0e702832e00df4e"
title: "Linus Torvalds's first LLM-assisted patch series"
url: "https://lwn.net/Articles/1100449"
link: "https://lwn.net/Articles/1100449"
source: "LWN.net"
domain: "lwn.net"
source_type: "community"
collector: "hackernews"
date: "2026-10-14T16:55:07Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["janvdberg"]
language: "en"
summary: "Linus Torvalds's first LLM-assisted patch series\n\tThe fairly short series of ten patches basically enhances folio\n\tlookup by noticing when folios are hot, and setting a \"delay\n\treleasing this folio until after a RCU period\", and then using that\n\tRCU delay it does not just the folio lookup itself under RCU (which\n\twe've done forever), but also the actual folio data accesses\n\tthemselves under RCU.…"
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 123
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50090842"
score: 116
comments: 98
community: "Hacker News"
---

# Linus Torvalds's first LLM-assisted patch series

LWN.net · janvdberg · 2026-10-14

Linus Torvalds's first LLM-assisted patch series
	The fairly short series of ten patches basically enhances folio
	lookup by noticing when folios are hot, and setting a "delay
	releasing this folio until after a RCU period", and then using that
	RCU delay it does not just the folio lookup itself under RCU (which
	we've done forever), but also the actual folio data accesses
	themselves under RCU. No refcount taking needed for the fastpath
	where we can just read the data from the folio entirely in an
	RCU-protected region when the user copy doesn't cause page faults.
The end result is an order-of-magnitude speedup for a read()-heavy
benchmark.  Review has already identified a race
condition in the code, though, so further work will be needed.
