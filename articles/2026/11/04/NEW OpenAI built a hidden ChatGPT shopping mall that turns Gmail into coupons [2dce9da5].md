---
id: "2dce9da587310063"
title: "NEW: OpenAI built a hidden ChatGPT shopping mall that turns Gmail into coupons"
url: "https://runtimewire.com/article/scoop-openai-built-a-hidden-chatgpt-shopping-mall-that-turns-gmail-into-coupons"
link: "https://runtimewire.com/article/scoop-openai-built-a-hidden-chatgpt-shopping-mall-that-turns-gmail-into-coupons"
source: "RuntimeWire"
domain: "runtimewire.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T22:22:10Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["ryanmerket"]
language: "en"
summary: "SCOOP: ChatGPT hides a gated Gmail shopping tab that turns your inbox into a store\nLast year you had to prompt Gmail-connected ChatGPT to \"find my Black Friday codes\" [Domaine guide, Nov 2025]. Now OpenAI is productizing it. A hidden Email Offers tab in the Windows package adds offer cards with \"Not verified - Email source\" labels, expiry dates, coupon codes, source email links, retailer links,…"
tags: ["r/OpenAI"]
orgs: ["OpenAI"]
topics: ["products & launches"]
content_source: "fulltext"
word_count: 339
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xo1t8f/new_openai_built_a_hidden_chatgpt_shopping_mall/"
score: null
comments: null
community: "r/OpenAI"
---

# NEW: OpenAI built a hidden ChatGPT shopping mall that turns Gmail into coupons

RuntimeWire · ryanmerket · 2026-11-04

SCOOP: ChatGPT hides a gated Gmail shopping tab that turns your inbox into a store
Last year you had to prompt Gmail-connected ChatGPT to "find my Black Friday codes" [Domaine guide, Nov 2025]. Now OpenAI is productizing it. A hidden Email Offers tab in the Windows package adds offer cards with "Not verified - Email source" labels, expiry dates, coupon codes, source email links, retailer links, and a local reference that auto-expires after 30 days or the stated expiry.
By Ryan Merket · Published · Updated
RUNTIMEWIRE INVESTIGATION — Original analysis
Original reporting by RuntimeWire, based on reverse engineering, testing.
Why it matters
OpenAI is moving Gmail deal hunting out of one-off prompts and into a dedicated shopping destination inside ChatGPT. That gives promotional email a persistent place in the client, with search, filters, coupon copying and saved offers built around the inbox.
Reporting record
Finding
ChatGPT's Windows package contains a gated shopping page with an Email offers tab for promotions from a connected Gmail account.
How we verified
Methods: reverse engineering, testing.
The signed Windows package contains the shopping interface, route controls and request handlers; a comparison with an earlier package found the endpoints, offer-screen identifiers and route gate absent from that build.
RuntimeWire statically inspected package 26.1029.7803.0 and compared it with preserved package 26.1027.6604.0. It did not install or launch the build, enable hidden features, connect Gmail or call the shopping endpoints.
Reproduction
RuntimeWire independently reproduced the core finding.
OpenAI has built a hidden shopping mall inside ChatGPT, with a gated Email offers tab that turns a connected Gmail inbox into a feed of promotions and coupon codes. RuntimeWire traced the interface, route controls and request handlers in signed Windows package 26.1029.7803.0, downloaded on November 4th. The code implements the client feature. It does not establish that the page is enabled for users, that the backend returns offers, or that OpenAI has set a launch date.
…
When you purchase through links in our articles, we may earn a small commission. This doesn’t affect our editorial independence.
