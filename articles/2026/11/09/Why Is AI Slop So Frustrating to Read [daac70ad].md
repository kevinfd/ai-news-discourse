---
id: "daac70ad2b4ad644"
title: "Why Is AI Slop So Frustrating to Read?"
url: "https://zonderlabs.com/slop"
link: "https://zonderlabs.com/slop"
source: "Zonder Labs"
domain: "zonderlabs.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T23:21:45Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["joegibbs"]
language: "en"
summary: "AI slop is frustrating to read because language models are currently, ironically, bad at writing. The language aspect lags behind other capabilities like coding, for these other capabilities are 1) easier to optimize with straightforward rewards and 2) seemingly more economically appealing, at least in the short term.\nThere’s one type of slop that I casually refer to as casual slop, which…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 831
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50433799"
score: 19
comments: 5
community: "Hacker News"
---

# Why Is AI Slop So Frustrating to Read?

Zonder Labs · joegibbs · 2026-11-09

AI slop is frustrating to read because language models are currently, ironically, bad at writing. The language aspect lags behind other capabilities like coding, for these other capabilities are 1) easier to optimize with straightforward rewards and 2) seemingly more economically appealing, at least in the short term.
There’s one type of slop that I casually refer to as casual slop, which includes most AI-generated social media posts and short videos. They’re annoying to come across. But they’re casual enough that there is no significant consequence if I fail to understand what they intend to communicate (there often isn’t much intention behind them anyway).
But I’d like to focus on a different type of slop here. It happens at work, in things I cannot simply scroll past, like a Slack message that I can tell is AI slop but have to decipher to move things forward, or a PR description written in Claudish.
Unclear communication
This type of slop adds mental burden to readers. Oftentimes, the ideas involved are already complex, and AI obscures them even more with confusing language.
Clarity in communication has been studied long before LLMs. In the classic writing textbook Style: The Basics of Clarity and Grace1, Williams argues that clear writing is a responsibility we owe readers, and we should make our ideas no more difficult than they have to be. Today, AI owes clarity to the humans reading its outputs and pulling their hair out.
Clarity may seem subjective, but we found strong agreement among humans on what makes communication clear. This gives us a gold standard for measuring clarity. In this write-up, we use principles of clarity to identify and measure AI slop.
We compare AI and human writing across two types of communication: articles and coding discussions. The AI samples exhibit much higher rates of unclear communication than their human counterparts.
The 3 Faults of AI Slop
To understand what makes AI writing unclear, we identified three recurring faults.
1. Hidden characters and actions
Each sentence is a mini story, where there are characters performing actions. There are two levels in a sentence: the story level and the grammatical level. Usually, the clearest version aligns the character with the subject, and the action with the verb.
A duck walked up to a lemonade stand and asked, “Got any grapes?”
This alignment isn’t a strict rule. Sometimes, we intentionally move things around to achieve a different emphasis. However, AI writing often conceals characters and actions without a clear purpose.
A request for grapes was made upon the duck’s arrival at the lemonade stand.
In this sentence, we have to look past the grammatical subject, “request”, to identify the duck as the actual character of the story. Then, we also need to reconstruct the actions because “walked up” and “asked” are hidden in the nouns “arrival” and “request”.
2. Vague wording
Vague wording is the most common fault in Claude Code. It can take the form of ambiguous references, stacked nouns, or unsuitable word choices—all of which appear in human writing too. But AI has a particular failure mode, and that is strange combinations of words. AI seems to lack common sense about how people normally describe things.
The duck made a grape availability request as he arrived at the beverage retailer.
It sounds absurd to call a lemonade stand a “beverage retailer”. I constructed this sentence on purpose, but didn’t exaggerate the fault. We encounter this in real work, where the concepts are more specialized and complicated. Here’s the sentence from Claude Code that inspired my absurd rewrite.
The database readiness check sits at the user-session entry boundary, before the authentication handler runs.
3. Empty statements and misplaced emphasis
Sometimes, we understand every word in the sentence, but still struggle to find the point.
Nothing else depends on anything but the result, so I’ll report as soon as the poll returns.
This sentence is understandable, but takes more than 10 seconds to process when a quick skim should be enough.
I’ll report the result when the poll finishes. Nothing else is pending.
We can even omit “nothing else is pending” for more concision, but now that the emphasis is placed correctly, it becomes a stylistic choice.
Measuring Slop
These three faults form the basis of our clarity taxonomy, which we use to annotate writing. Below, we break down the same samples by fault to see how frequently each occurs.
While AI signatures like “delve” and em dashes are widely associated with “slop”, they are not what makes writing sloppy. Below, we compare our clarity measurements with AI detectors.
Below is an example of the clarity annotations. In the snippet, we are running LLM inference on GPUs. We ask Claude to examine the Triton code that speeds up inference, so we can reproduce it in CUDA. You can inspect the highlights to see what’s frustrating, or turn them off to read the response uninterrupted.
Get research updates
New findings on AI writing and language models.
