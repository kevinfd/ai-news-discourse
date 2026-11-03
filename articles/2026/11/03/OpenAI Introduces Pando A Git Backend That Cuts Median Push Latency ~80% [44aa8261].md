---
id: "44aa8261582a90f8"
title: "OpenAI Introduces Pando: A Git Backend That Cuts Median Push Latency ~80%"
url: "https://marktechpost.com/2026/11/02/openai-pando-git-backend-monorepo"
link: "https://marktechpost.com/2026/11/02/openai-pando-git-backend-monorepo"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T05:51:06Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Michal Sutter"]
language: "en"
summary: "OpenAI has introduced Pando , a new Git backend that now serves all development in its monorepo. The OpenAI Pando Git backend keeps the standard Git client and protocol. Engineers and Codex agents still run git push and git fetch as before. Only the server changed. OpenAI team reports median push latency fell nearly 80%. Pando now delivers nearly a petabyte of Git data per day. \n\n TL;DR \n\n…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Machine Learning", "New Releases", "Python", "Software Engineering", "Staff"]
orgs: ["OpenAI", "Anthropic"]
topics: ["agents & coding", "models & research", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 1007
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI Introduces Pando: A Git Backend That Cuts Median Push Latency ~80%

MarkTechPost · Michal Sutter · 2026-11-03

OpenAI has introduced Pando , a new Git backend that now serves all development in its monorepo. The OpenAI Pando Git backend keeps the standard Git client and protocol. Engineers and Codex agents still run git push and git fetch as before. Only the server changed. OpenAI team reports median push latency fell nearly 80%. Pando now delivers nearly a petabyte of Git data per day. 

 TL;DR 

 Scale: Nearly 1 PB of Git data per day; peak above 57 TB in 1 hour. 

 Runs on: Commodity hardware; standard cloud VMs saturate 10 Gbps links on clone and fetch. 

 Performance: Thousands of concurrent pushers without degradation, per OpenAI’s own testing. 

 Best: Median push latency down nearly 80% (about 5x). 

 Worst: Not open source; repeat branch pushes resend non-trunk history (p99 pack under 3 MiB). 

 What is OpenAI Pando? 

 Pando is a Git-compatible server backend from OpenAI that scales concurrent pushes and fetches for a monorepo. It was written in Rust and reached production in 10 weeks. One engineer designed the core and teams of Codex agents implemented it. It has served production traffic since April 2026. 

 Why did OpenAI need a new Git backend? 

 Codex multiplied parallel work. OpenAI’s commit chart shows commits landed on master up 1,378% in Q3 2026 versus Q1 2024. Its Q4 2026 estimate is +2,442%. Each push now triggers many CI fetches. By late 2025, fetches and pushes slowed, merges failed, and reliability at times fell below 90%. OpenAI concluded the bottleneck was how it served Git, not Git itself. 

 How does Pando work? 

 Pando drops 2 assumptions that most Git servers treat as requirements: 

 1. Repository-wide consistency : Conventional servers order every ref update repo-wide, so unrelated pushes wait. Pando uses causal consistency instead. Each branch is serialized on its own, and clients only conflict when pushing the same ref. The tradeoff: a reader viewing several branches may see them at different points in time. 

 2. A unique packfile per client : Standard servers build a fresh pack per fetch. Pando stores each pushed pack as an immutable blob. A “ref version” goes into a scalable metadata store. A push needs O(1) metadata reads and writes. A fetch needs O(log Δ) reads, where Δ is the ref-version gap to close. 

 How are pushes kept small and reusable? 

 With millions of branches, a full ref advertisement can exceed 100 MiB. Pando advertises only the trunk branch as the base for new feature-branch pushes. Any reader with trunk history can then fetch that branch from 1 stored pack. In OpenAI’s monorepo, the median pack was under 20 KiB. 

 How are fetches served at line rate? 

 Pando returns download links via packfile-uri , an existing Git protocol feature. It sends an empty inline pack. A delivery service called Express caches packs regionally, using consistent hashing, with hit rates above 99%. 

 What replaces garbage collection? 

 Each push creates an “L0” pack. Background workers group packs into geometrically larger covers, similar to LSM-tree compaction. The monorepo currently uses covers up to L4. Covers act as a skip list, so pack selection runs in logarithmic time. 

&
 -->

 What are the production numbers? 

 All figures below are self-reported by OpenAI. 

 Median push latency reduced by nearly 80%. 

 Nearly 1 PB of Git data per day, using only a handful of CPU cores. 

 Over 57 TB of packs served in a single hour, more than 99% from local disk cache. 

 Clones and fetches saturate 10 Gbps links on standard cloud VMs. 

 OpenAI also ran a 1,000-writer simulation against 3-phase-commit and write-ahead-log designs. It labels these teaching models, not benchmarks. 

 How does Pando compare with other approaches? 

 OpenAI Pando GitHub Spokes Anthropic Scion Git client compatible Yes Yes No, own scn client Write coordination Per-branch, causal consistency Three-phase commit with quorum Server-side commits; refs via compare-and-swap Default replicas Not disclosed (blob + metadata stores) 5 full copies No fully materialized repo copy Read path Reused packs via packfile-uri, Express cache Closest in-sync replica Tiered tree/blob caches Cache hit rate Over 99% Not disclosed Over 99% per tier Headline result Median push latency down ~80% Serves ~1 billion repositories 200x smaller CPU/memory footprint Build effort 10 weeks, Rust Not disclosed 7 people, 5 months Available to others No Yes, powers GitHub No 

 How was Pando built and deployed? 

 OpenAI wrote a Git conformance suite for agents and added deterministic simulation testing. Agents using GPT-6 Astra wrote Lean and TLA+ specs to find bugs. 

 Pando first ran as a read- and write-through proxy, so traffic moved without downtime. OpenAI ships its own Git build to developer machines and the ChatGPT desktop app. 

 What goes back to upstream Git? 

 OpenAI fixed client handling of concurrent, interrupted and resumed pack downloads, and added packfile-uri tracing. Its build adds parallel pack indexing and “explicit haves.” Several fixes are upstream. The rest sit in a public patch tracker . 

 What are the limitations? 

 Pando is not open source; OpenAI team states that it is exploring ways to share the technology. 

 Cross-branch reads have no single point-in-time snapshot. 

 Repeat or stacked branch pushes resend everything outside trunk. The p99 pack was under 3 MiB. 

 Every performance number is self-reported, with no independent benchmark yet. 

 Key Takeaways 

 Pando keeps Git, but rebuilds the server for parallel agent traffic. 

 Per-branch causal consistency removes repository-wide write contention. 

 Stored, reusable packs replace per-client pack generation. 

 Median push latency dropped nearly 80%; daily traffic nears 1 PB. 

 Client fixes go upstream; the backend stays internal for now. 

 Check out the full OpenAI engineering post , the OpenAI Git repository and the patch tracker . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post OpenAI Introduces Pando: A Git Backend That Cuts Median Push Latency ~80% appeared first on MarkTechPost .
