---
id: "1d78f09c640d45a5"
title: "Claude Haiku 5.5"
url: "https://anthropic.com/claude-haiku-5-5"
link: "https://anthropic.com/claude-haiku-5-5"
source: "Anthropic"
domain: "anthropic.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-07T18:01:32Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["sfkgtbor"]
language: "en"
summary: "Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.\nClaude Haiku 5.5 is designed for high-volume, cost-sensitive tasks. It reliably handles quick and repetitive workloads (like summaries, compactions, database queries, and classification requests). It pairs well with Opus 5.5 and Sonnet 5.5 as a subagent on coding work. And, since it’s also our…"
tags: []
orgs: ["Anthropic", "Microsoft", "Google", "Amazon"]
topics: ["models & research", "agents & coding", "safety & ethics", "health & science"]
content_source: "fulltext"
word_count: 895
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49996437"
score: 1047
comments: 488
community: "Hacker News"
---

# Claude Haiku 5.5

Anthropic · sfkgtbor · 2026-10-07

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.
Claude Haiku 5.5 is designed for high-volume, cost-sensitive tasks. It reliably handles quick and repetitive workloads (like summaries, compactions, database queries, and classification requests). It pairs well with Opus 5.5 and Sonnet 5.5 as a subagent on coding work. And, since it’s also our fastest model to date, it works especially well for speed-sensitive tasks like live customer support and browser use.¹
Haiku 5.5 is available at a much lower price than Haiku 4.5. On average, it now costs around 75% less to run.²
Along with this launch, we’re making improvements to the value of our model range. We’re halving the price of Claude Sonnet 5.5’s cache reads, which means Sonnet 5.5 now runs around 20% cheaper on most agentic work. And we’re introducing a new monthly API credit for our Claude Max and Team subscribers, designed to support our users in building new agents and applications that run on the Claude Platform.
Performance
Here’s how Claude Haiku 5.5 performs across a range of benchmarks:
Haiku 5.5 is our first Haiku-class model to come with an adjustable effort setting. This means that, as with our other models, users can decide whether to optimize for cost or intelligence. The charts below show how Haiku 5.5 performs on three benchmarks at each effort setting:
In early testing, our customers reported results consistent with the performance and cost improvements shown above. Here’s what they told us about the new model:
Pricing
The table below shows how Claude Haiku 5.5’s pricing compares to our other models. Haiku 5.5 is especially good value when used for tasks with prompts up to 100,000 tokens, which make up around 90% of requests to our previous Haiku model.
Safety
Alignment. Claude Haiku 5.5 shows major improvements across almost all of our alignment evaluations relative to Haiku 4.5. In particular, we found far fewer instances of misaligned behavior, and a lower willingness to cooperate with misuse. The model’s system card describes our evaluation process and results in more detail.
Safeguards. Consistent with its capabilities, Haiku 5.5’s cybersecurity safeguards are more restrictive than Haiku 4.5’s, but somewhat less restrictive than those we’ve applied to other recent models. In cybersecurity, they permit a wider range of defensive tasks than our safeguards for Sonnet 5.5, but they still block penetration testing and other techniques more likely to be used by attackers.
Haiku 5.5’s biology safeguards are the same as for Sonnet 5, Sonnet 5.5, and Opus 5. They allow research biology questions but restrict access to requests that we judge as likely to cause harm. Organizations working on wider-ranging biology and cyber activities can apply to our Life Sciences Verification Program and Cyber Verification Program.
Availability
Claude Haiku 5.5 is available now on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. On the Claude Platform, developers can get started with claude-haiku-5-5. 
See our migration guide for details.
Further updates
Alongside our new pricing for Claude Haiku 5.5, we’re making further improvements to the value of our models and products.
First, starting today, we’re lowering the price of cache reads on Claude Sonnet 5.5. Cache reads now cost 50% less: $0.10 per million tokens rather than $0.20. Because cache reads make up a large share of models’ token consumption, this reduces the cost of Sonnet 5.5 on most agentic tasks by around 20%.
For instance, here’s what the price cut means for Sonnet 5.5’s performance relative to cost on Terminal-Bench 4.0:
This chart illustrates an important difference between Haiku 5.5 and our larger models. Sonnet 5.5 and Opus 5.5 remain better choices for complex agentic coding tasks like those measured by Terminal-Bench 4.0. By contrast, Haiku 5.5 is best suited to more narrowly scoped tasks that might otherwise have been cost-prohibitive with previous versions of Claude—like compaction, summarization, or subagent work.
Second, this week, we’ll roll out a new monthly API credit to all Max and Team subscribers for use on the Claude Platform. Max 5x users will get $100 in credits per month, Max 20x users will get $200, and Team subscribers will receive up to $500, pooled across their users. These credits are designed to allow our users to experiment with building tools, apps, and agents that call our API. They can be used on any of our models. For more information, see our Help Center article.
For developers, we’re also updating our Claude Python and TypeScript SDKs to add support for computer use and browser use in beta. Haiku 5.5 is especially well-suited to these tasks, given its combination of speed, capability, and price. You can read more about this in our Claude Platform docs.
Footnotes
1 Claude Haiku 5.5 is our fastest model to date at each model’s standard speed, although it runs less quickly than our Opus models in Fast Mode.
2 Claude Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens, and 50% lower for requests over 100,000 tokens. On Haiku 4.5, 90% of requests fell into the former category. This calculation also accounts for changes between Haiku 4.5 and Haiku 5.5 in how many tokens are used to complete a given piece of work: Haiku 5.5 has an updated tokenizer (similar to Sonnet 5.5’s and Opus 5.5’s), which means it uses slightly more tokens per task.
