---
id: "3954037996af07a3"
title: "Best way to build an AI-powered codebase search across hundreds of private GitHub repos?"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xnmtfg/best_way_to_build_an_aipowered_codebase_search"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xnmtfg/best_way_to_build_an_aipowered_codebase_search"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T12:21:24Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["fresh_preserve"]
language: "en"
summary: "Hey folks, I've been asked to build something that indexes our private GitHub repositories so developers can ask questions like: Where is this method being called? What does this operation actually do? Where does this value come from? What are the dependencies between these services? We've got a mix of technologies across our repos, including Terraform, TypeScript, JavaScript, C#/.NET, Python…"
tags: ["r/ArtificialInteligence"]
orgs: ["Amazon", "Anthropic"]
topics: ["search & media", "agents & coding"]
content_source: "post"
word_count: 241
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xnmtfg/best_way_to_build_an_aipowered_codebase_search/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Best way to build an AI-powered codebase search across hundreds of private GitHub repos?

Reddit · fresh_preserve · 2026-11-04

Hey folks, I've been asked to build something that indexes our private GitHub repositories so developers can ask questions like: Where is this method being called? What does this operation actually do? Where does this value come from? What are the dependencies between these services? We've got a mix of technologies across our repos, including Terraform, TypeScript, JavaScript, C#/.NET, Python and others. The idea is to start with one repo for each tech stack and eventually scale this to hundreds of repos across the organisation. For a small POC, I've built a service hosted on AWS ECS that: Clones the GitHub repo. Indexes the code using tools like codebase-memory, scip-dotnet, scip-typescript, semantic-ts, etc. Stores the indexed data in PostgreSQL. Uses Claude via AWS Bedrock to query the PostgreSQL data and generate answers. It's working reasonably well for the POC, but I'm not sure if this is the right architecture to build on when scaling to hundreds of repositories and multiple languages. A few things I'm keen to get some feedback on: Is PostgreSQL a sensible choice for storing code indexes, embeddings and relationships? Is combining SCIP-based indexing with semantic search the right approach? Are there any existing tools or platforms that handle this well? How would you approach incremental indexing when repos change? What would you change architecturally to make this scalable and maintainable? Would love to hear from anyone who's built something similar or tackled codebase search at scale. Cheers!
