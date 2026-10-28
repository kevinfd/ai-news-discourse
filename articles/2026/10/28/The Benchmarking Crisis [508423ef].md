---
id: "508423ef7ad4cdeb"
title: "The Benchmarking Crisis"
url: "https://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html"
link: "https://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html"
source: "Lobsters"
domain: "databasearchitects.blogspot.com"
source_type: "community"
collector: "rss"
date: "2026-10-28T08:32:09Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["databasearchitects.blogspot.com via timschumi"]
language: "en"
summary: "Comments"
tags: ["databases", "performance", "ai"]
orgs: []
topics: ["models & research", "products & launches", "policy & regulation"]
content_source: "fulltext"
word_count: 740
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# The Benchmarking Crisis

Lobsters · databasearchitects.blogspot.com via timschumi · 2026-10-28

Goodhart’s law, that any measurable target stops being useful when people start optimizing for it, very much holds in database benchmarking. That is not new, of course. Famously, TPC-D got retired when people optimized so much for it that the query runtimes converged towards zero due to excessive caching. TPC-H fixed that by declaring itself to be an ad-hoc benchmark, and explicitly forbidding things like exploiting knowledge about the workload or caching results (and a number of other optimizations).
We now see the same problem with the ClickBench benchmark, heavily accelerated by today’s use of AI code generation. If you tell an AI to make the queries faster, it will make the queries faster, regardless of whether this is a generally plausible approach or not. For example, the pgrust implementation performs group-by aggregations on string columns purely on the hash value, ignoring the long string content. That is a great performance boost, of course, and works for this benchmark, but can produce wrong results. Is it faster? Yes. Is it a plausible optimization? Probably not. And it does many other things: For example, ClickBench repeats certain predicates across queries, and thus pgrust caches the predicate, completely eliminating the query cost the second time. Or for query Q17, which returns tuples grouped by userid, it makes use of the fact that a) tuples are roughly clustered by userid, and b) the query specifies a limit clause without order by. Thus any userid will do, and it never reads most of the data. A human would not do these tiny micro-optimizations, because they are unlikely to be relevant in general use cases, but an AI can of course look at each query in detail and tune for it.
Part of the problem is, of course, ClickBench itself. The benchmark is not well specified in what is permitted and what is not, there is no update stream, the queries are very simple, share predicates, are underspecified, etc. But the fundamental problem is independent of that concrete benchmark: The moment we start aggressively optimizing for a specific benchmark, the benchmark stops being very useful. Historically, that pressure was reduced a bit by the requirement that systems be generally useful. That is, they did not just want to perform well in benchmarks but also to be useful for their customers. That is, of course, not a concern for vibe-coded execution engines.
It is not clear what to do about it. Our SQLStorm proposal tried to address this by having tens of thousands of queries, which makes overfitting harder. No human would fine-tune their system to such a huge workload. But with AI tools we could even investigate ten thousand queries in detail if needed, so that is not a real defense.
I think that to be meaningful, a benchmark has to a) like TPC-H, be ad-hoc, and forbid exploiting prior knowledge and any form of intermediate result caching. If we don’t do that, execution times converge towards zero. And b) the benchmark has to include some form of update stream, as otherwise overly aggressive read-only or read-mostly systems will always outperform systems that offer full transactional support. And c) the benchmark has to be truly ad-hoc, in the sense that the systems tested have to be older than the benchmark. One way to fight Goodhart’s law would be to (automatically) come up with a new benchmark from time to time, and then measure the systems that existed before the benchmark. The caching/pre-computation problem still remains, of course, but at least that would prevent the over-aggressive adjustment to just one specific benchmark.
Interestingly, the machine learning community has struggled with exactly the same problem for years, and we should probably borrow some of their ideas. Kaggle competitions, for example, rank submissions on a hidden test set that participants never see, which makes overfitting on the public data pointless. Similarly, benchmarks like LiveBench regularly release new questions to make sure that models cannot have seen them during training. For database benchmarking that could mean keeping the actual benchmark queries secret and only publishing a representative sample for development, or, even better, generating a fresh workload for every evaluation round. SQLStorm already uses generated queries, so producing a new query set from time to time would be fairly easy. We would probably want a more generic approach (higher variety in schemas, update streams, transactions, etc.), but that seems to be a direction that would help keep benchmarks meaningful.
