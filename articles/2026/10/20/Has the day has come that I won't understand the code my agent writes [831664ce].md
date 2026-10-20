---
id: "831664cec916bd41"
title: "Has the day has come that I won't understand the code my agent writes?"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xao9yg/has_the_day_has_come_that_i_wont_understand_the"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xao9yg/has_the_day_has_come_that_i_wont_understand_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T10:13:51Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["GianniMariani"]
language: "en"
summary: "I’ve been running a few experiments with DSLs and DSAPIs recently and noticed something counterintuitive. I fed an LLM some code targeting a generic compiler framework. It’s the kind of dense, abstract machinery that is brutal for human working memory to parse (at least without sinking hours I don't have into it). Yet with zero formal documentation—just the source of a few representative…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research", "business & funding", "agents & coding"]
content_source: "post"
word_count: 307
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xao9yg/has_the_day_has_come_that_i_wont_understand_the/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Has the day has come that I won't understand the code my agent writes?

Reddit · GianniMariani · 2026-10-20

I’ve been running a few experiments with DSLs and DSAPIs recently and noticed something counterintuitive. I fed an LLM some code targeting a generic compiler framework. It’s the kind of dense, abstract machinery that is brutal for human working memory to parse (at least without sinking hours I don't have into it). Yet with zero formal documentation—just the source of a few representative fixtures—the model grokked the meta-patterns and generating valid code. Naturally, this raises the question: should we be optimizing DSLs and APIs for the LLM or the human? I used to think good design for one meant good design for the other, but now I’m not so sure or is this a small class of DSL? In discussion with a colleague on concept graphs recently, I think it might be the norm. The experiments showed both sides of the coin: - In one task, it nailed the semantics and generated correct code within the constraints far faster than I could have. - In another, it ran into a semantic wall and immediately tried to rewrite the generic compiler itself to fit its needs. I had to explicitly declare the compiler toolchain out-of-bounds (funnily enough, it actually found a real edge-case bug in the compiler along the way, though that wasn't what I was testing). - As an unexpected bonus, the agent ended up drafting a full doc plan for the compiler, which I really need to review. The implications seem vast. DSLs and DSAPIs are the deterministic, symbolic side of neuro-symbolic architectures. A well-designed API eliminates whole classes of errors. But if an LLM can effortlessly navigate the hyper-dense abstractions of a generic compiler—constructs that push well beyond human cognitive limits—then building ergonomic, human-friendly surface syntax might just be legacy overhead. If that holds, the entire abstraction layer of future software interfaces looks completely different.
