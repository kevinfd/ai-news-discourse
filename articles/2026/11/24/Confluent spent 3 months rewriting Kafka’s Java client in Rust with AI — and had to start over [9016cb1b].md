---
id: "9016cb1b7322bac8"
title: "Confluent spent 3 months rewriting Kafka’s Java client in Rust with AI — and had to start over"
url: "https://thenewstack.io/confluent-kafka-rust-agents"
link: "https://thenewstack.io/confluent-kafka-rust-agents"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T19:26:18Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Confluent spent nearly three months using AI coding agents to translate Apache Kafka’s Java client into Rust. The engineers discarded their first implementation, uncovered performance problems that slipped past automated tests, and eventually settled on a multi-agent workflow they believe could keep non-Java clients in step with Kafka as it evolves. \n\n The work, detailed Tuesday in a technical…"
tags: ["AI Agents", "Data Streaming", "Rust"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "summary"
word_count: 691
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Confluent spent 3 months rewriting Kafka’s Java client in Rust with AI — and had to start over

The New Stack · Amanda Caswell · 2026-11-24

Confluent spent nearly three months using AI coding agents to translate Apache Kafka’s Java client into Rust. The engineers discarded their first implementation, uncovered performance problems that slipped past automated tests, and eventually settled on a multi-agent workflow they believe could keep non-Java clients in step with Kafka as it evolves. 

 The work, detailed Tuesday in a technical blog post by Confluent principal engineer and Apache Kafka committer Andrew Schofield , began with Anthropic’s Claude Opus 4.6 and progressed through several model upgrades. Confluent has since released its first generally available Rust client translated from Apache Kafka 4.4.0 alongside a preview of a new Python client. 

 The engineers applied 191 upstream Kafka commits representing several months of development to the translated codebase in less than two working days. 

 The engineers applied 191 upstream Kafka commits representing several months of development to the translated codebase in less than two working days. Confluent plans to build a continuous translation pipeline to keep its non-Java clients aligned with future Kafka releases. 

 Kafka’s Java client problem 

 Apache Kafka provides only a Java client, yet Confluent Cloud handles nearly as many connections from non-Java clients. Confluent’s existing non-Java clients rely on librdkafka, whose threading and memory management differ from the Java implementation. 

 With more than 100 active Kafka contributors and typically more than 20 Kafka Improvement Proposals per release, Confluent wants to derive its non-Java clients directly from the Java source through AI-assisted translation and maintain feature parity through a shared Rust core. 

 Three agents, one translation 

 Two engineers each devoted about 75% of their time to the experiment. Within two weeks, they had a working Rust producer without secure connections. TLS and authentication followed by week four, and a basic consumer was running by week six. 

 After several weeks, the team scrapped its original translation and started over with more specific instructions. 

 The agents frequently turned to engineers for guidance on Kafka’s architecture. After several weeks, the team scrapped its original translation and started over with more specific instructions. 

 Under Confluent’s translation workflow, a Project Manager agent coordinates the Actor and Critic. Engineers approve both milestone and phase plans and weigh in on architectural decisions, such as mapping Java threads to Tokio tasks. 

 The Actor and Critic communicate through Git. The Actor commits translated code and addresses the Critic’s findings until no further issues are raised. Schofield says the review cycle typically takes about five iterations. 

 When tests pass anyway 

 Although the generated code passed the translated Kafka tests, performance testing revealed a sleep operation on every iteration of the networking loop. 

 Confluent subsequently refined its translation instructions to specify the intended behavior rather than rely solely on the original source code and translated tests. Passing tests alone was insufficient to verify the quality of agent-generated code . 

 While the agents translated the code, engineers worked with Rust experts to design interfaces that preserved Kafka compatibility without imposing Java conventions on Rust developers. The team went through six candidate designs to ensure the Rust core could handle timeouts without interfering with signal handling in other language runtimes. 

 Toward continuous Kafka translation 

 When Apache Kafka 4.4.0 came out, the team opted to bring its existing Rust implementation up to date instead of starting from scratch. It took less than two working days to incorporate 191 upstream commits. 

 Confluent has yet to show whether it can keep multiple client implementations in sync as Kafka evolves or how much work engineers will need to do along the way. Schofield expects the continuous translation pipeline to begin doing that work in mid-2027. 

 The source code is available under the Apache License 2.0 . While Confluent joins a broader wave of agent-driven Rust rewrites , its goal is to maintain the translated code over successive Kafka releases. 

 “Getting code quickly was only the beginning; making it useful across languages was the real engineering work.” 

 “Getting code quickly was only the beginning; making it useful across languages was the real engineering work,” Schofield wrote. 
 The post Confluent spent 3 months rewriting Kafka’s Java client in Rust with AI — and had to start over appeared first on The New Stack .
