---
id: "722ac7382cf5ac3b"
title: "We have LLMs now. Why are the docs still wrong?"
url: "https://amendary.com/blog/keeping-docs-in-sync-with-code"
link: "https://amendary.com/blog/keeping-docs-in-sync-with-code"
source: "Amendary"
domain: "amendary.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-08T19:38:41Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["higeorge13"]
language: "en"
summary: "Documentation\nWe have LLMs now. Why are the docs still wrong?\nKeeping documentation in sync with code takes more than generating text. My take on LLMs, stale docs, and what I am building with Amendary.\nYou change a default, merge the PR, and move on to the next thing. The tests pass. Someone even remembers to update the README. A week later, someone else follows the setup guide in Notion and…"
tags: []
orgs: []
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1466
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50010936"
score: 12
comments: 11
community: "Hacker News"
---

# We have LLMs now. Why are the docs still wrong?

Amendary · higeorge13 · 2026-10-08

Documentation
We have LLMs now. Why are the docs still wrong?
Keeping documentation in sync with code takes more than generating text. My take on LLMs, stale docs, and what I am building with Amendary.
You change a default, merge the PR, and move on to the next thing. The tests pass. Someone even remembers to update the README. A week later, someone else follows the setup guide in Notion and asks why the application behaves differently. There is another page in the wiki saying something slightly different as well. Which one is correct?
This is the kind of documentation problem I want to spend time on. We have tools that can write a whole guide in seconds, but the small sentence that became wrong last Tuesday is still there. And it looks perfectly reasonable until someone relies on it.
Writing the first version is much easier now
Give an LLM some code and ask it to explain how a service works. You can get a useful starting point: installation steps, configuration options, an explanation of a function that nobody wanted to document. You still need to check it, but getting past the empty page is much easier.
So it is reasonable to ask why we cannot just do the same whenever the code changes. Give the agent the diff, tell it to update the docs, and let it open a PR. If the relevant documentation is in the same repository and the task is clear, that can be a useful workflow. I would not dismiss it.
But which docs should it update? The README, the deployment runbook, the customer guide in Notion, or all of them? Does the person asking even remember that all these pages exist? The quality of the generated paragraph matters, but there is quite a bit of work before we get to that paragraph.
One code change, several different readers
Take a simple example. A timeout changes from 30 to 60 seconds. The code is clear, the diff is small, and changing a number in a document sounds easy enough.
The engineering reference might need the new default as soon as the change lands. A customer guide might need to wait for the release. A runbook might describe an explicit override that is still 30 seconds and should not change at all. A historical incident report should probably keep the value that was true during the incident.
Now imagine asking an agent to find every mention of 30 seconds and fix it. It might produce a very convincing set of edits. You still have to understand which statements became wrong, which were always about something else, and which are supposed to describe the past.
This is why I think the relationship between a document and the code matters so much. Who reads this page? Which repository does it describe? Does it explain what is on the default branch or what customers have received? Without that context, even a small correction can be the wrong correction.
An index gets you candidates, not an answer
You could put the documentation in a vector index and retrieve the chunks closest to a code change. That sounds like a reasonable way to reduce the amount of text you send to the model. But the chunk about timeouts being similar to the diff does not mean its claim is wrong. It might describe a different service, an explicit override, or an older version that is still supported.
A text search has its own problems. A customer page might say that exports finish within a minute, while the changed function is called build_customer_archive. Searching for the function name will not find that sentence. Searching for every mention of exports might return half the help center. Someone, or some model, still needs to decide which relationship matters.
Then there is freshness. If your index still contains yesterday's version of the page, you may draft a correction against text someone has already fixed. You need to retrieve the current source before writing, check that the passage you intend to replace is still there, and have a way to deal with a conflicting edit. Otherwise you can get the reasoning right and still overwrite the wrong thing.
I think retrieval is useful when we treat it as a way to find places worth checking. Evidence has to come from the actual change and the current document. A similarity score cannot replace that check.
Someone still has to check the answer
There is another part I find easy to underestimate: reviewing the result. An agent can return three polished paragraphs where you expected one number to change. They read well. They might also introduce a configuration option that does not exist, remove a useful exception, or describe a future behavior as if it already shipped.
I do not want to spend twenty minutes comparing a rewritten page with the repository to work out whether I can trust it. I want to see the old passage, the proposed correction, and the change supporting it. If only one claim became wrong, a small edit is much easier to reason about.
Even the diff needs some care. A changed line might be in a test fixture rather than the implementation. A new default might apply only when a particular flag is enabled. If we cut the context too aggressively, the model sees the number changing without the condition around it. Sending more context can help, but it also gives the model more unrelated things to explain. There is no single prompt that makes these choices disappear.
And sometimes the right outcome is no edit. A refactor can touch plenty of files without changing anything the reader needs to know. If every code change produces documentation work, we have created another queue that people will eventually stop looking at.
Where Amendary fits in this
I am building Amendary around this maintenance work. You connect GitHub and the places where your documentation already lives, in Notion or GitHub. You choose the pages to watch and map them to the repositories they describe. That choice is important: connecting a destination should not mean every page suddenly becomes something an agent can rewrite.
Amendary checks the mapped documentation against code changes or the release signal you choose for customer-facing pages. When it finds a supported mismatch, it drafts a correction with the source attached. You can inspect it in the review queue before applying it. For GitHub folder destinations, you can have the docs changes delivered through a pull request that you merge.
The model is part of this, of course. It helps understand whether a change affects a passage and how to express the correction. But the mapping, the evidence, the review, and delivering the change back to the right document all need to work as well. Generating a good sentence alone does not finish the job.
It still needs an owner
I would love to say that you connect Amendary and never think about documentation again. I do not think that would be an honest promise.
A page can be mapped to the wrong repo. A release can explain too little. The reason behind a product decision might exist only in a conversation, not in the code. The model can miss something, or propose a correction that needs more context. An automated check cannot tell you everything your customer needs to understand.
On a paid plan, owners can enable automatic application for eligible corrections. That can reduce the routine work, but it does not turn uncertain changes into facts. Some edits still need review. And if you use a GitHub PR destination, someone still needs to merge the docs PR before the target branch changes.
There is also a difference between accurate and useful. A guide can have all the right numbers and still be impossible to follow. It can explain the implementation perfectly and never answer the reader's actual question. Someone on the team still needs to care about that.
What I would like to stop doing
I want fewer moments where someone has to ask in Slack whether a page is still correct. I want the person reviewing a correction to understand why it exists without doing the whole investigation again. And I want a small change in the product to lead to a small, explainable change in the docs when one is needed.
LLMs help with this. Amendary is my attempt to put that help into a workflow that runs as the product changes, with boundaries around what gets read and edited. Neither removes the need to decide what we want our documentation to say.
For me, that is a useful goal already. Less time hunting for stale sentences, more time making sure the explanation actually helps the next person who reads it.
