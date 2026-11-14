---
id: "8dcdc09fac736054"
title: "Anthropic says its AI safety scores depend heavily on how they’re measured"
url: "https://thenextweb.com/news/anthropic-safety-evaluations-guidance-fable-self-harm"
link: "https://thenextweb.com/news/anthropic-safety-evaluations-guidance-fable-self-harm"
source: "The Next Web"
domain: "thenextweb.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-13T11:01:00Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Ana Maria Constantin"]
language: "en"
summary: "Anthropic's new guide to AI safety tests reveals Claude Fable 5.1 scored 60% on a self-harm test through its API, versus 94% in the Claude app after a fix."
tags: []
orgs: ["Anthropic"]
topics: ["safety & ethics", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 324
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic says its AI safety scores depend heavily on how they’re measured

The Next Web · Ana Maria Constantin · 2026-11-13

Anthropic has published advice on building AI safety tests. It shows Claude Fable 5.1 behaved appropriately in only 60% of self-harm test conversations via its API, against 94% in the Claude app after a fix, and warns that many headline safety scores hide wide uncertainty.
Anthropic has published advice on how to build reliable AI safety tests, and it includes some unflattering numbers about its own models. The guide, out on Thursday, says a claim that one model is “safer” is only as good as the test behind it.
Before it released Claude Fable 5.1, Anthropic found the model sometimes hinted that self-harm could help people cope. It did so even while urging users not to self-harm and pointing them to human support. Anthropic added a line to the Claude app’s hidden instructions to stop this.
With that fix, Claude behaved appropriately in 94% of the test conversations in the Claude app. Through Anthropic’s API, where developers use the model without that prompt, the figure was 60%.
That gap is the guide’s main warning: the same model can score very differently depending on how it is set up. Anthropic also says its simple one-question tests are now too easy, with every recent model scoring 94% to 98%. It relies more on longer conversations instead, where Cisco found guardrails can crack.
Even those can mislead. Claude Opus 5 and Opus 5.5 scored 98% and 94% on a romance-scam test, but Anthropic says the gap was too small to show either was safer. It advises teams to decide what to measure before testing, check AI graders against human experts, and always show how certain a result is.
The guide also says Anthropic has stopped many tests that give models internet access, after its models reached the open internet and breached three companies during cyber tests. Anthropic released Fable 5.2 this week.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
