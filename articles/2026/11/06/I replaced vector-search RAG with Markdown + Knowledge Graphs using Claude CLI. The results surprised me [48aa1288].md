---
id: "48aa1288f42b0b1d"
title: "I replaced vector-search RAG with Markdown + Knowledge Graphs using Claude CLI. The results surprised me."
url: "https://reddit.com/r/ClaudeAI/comments/1xpjadb/i_replaced_vectorsearch_rag_with_markdown"
link: "https://reddit.com/r/ClaudeAI/comments/1xpjadb/i_replaced_vectorsearch_rag_with_markdown"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T17:51:15Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Shivam__kumar"]
language: "en"
summary: "I want to share something I've been experimenting with recently. Not claiming this is some revolutionary architecture or that I've solved RAG. I'm just curious if anyone else has tried something similar. I was building an AI system for a fairly complex ERP application. Initially, I used the usual RAG approach: embeddings, vector search, retrieving relevant chunks, and passing them to the LLM.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media", "models & research", "agents & coding"]
content_source: "post"
word_count: 596
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpjadb/i_replaced_vectorsearch_rag_with_markdown/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I replaced vector-search RAG with Markdown + Knowledge Graphs using Claude CLI. The results surprised me.

Reddit · Shivam__kumar · 2026-11-06

I want to share something I've been experimenting with recently. Not claiming this is some revolutionary architecture or that I've solved RAG. I'm just curious if anyone else has tried something similar. I was building an AI system for a fairly complex ERP application. Initially, I used the usual RAG approach: embeddings, vector search, retrieving relevant chunks, and passing them to the LLM. But honestly, I wasn't happy with the results. The problem wasn't always the LLM. Sometimes the retrieved information itself was incomplete. The model could understand individual database tables, but understanding how those tables, modules, and business rules connected was a different challenge. So I thought, what if I stopped relying on vector search for understanding the application and gave Claude a properly structured knowledge base instead? Here's what I did. I started creating Markdown files for almost everything in the application. How each module works, business logic, workflows, relationships between modules, conditions, exceptions, and so on. I also created separate documentation for the database. Not just table names and column definitions. I documented what each table actually represents, why it exists, how its columns are used, and how it relates to other tables from a business perspective. I was very particular about how these files were written and organized. I didn't want hundreds of random MD files. I wanted every file to have a clear purpose, with proper references and connections to related documentation. Once that documentation was ready, I asked Claude to read the files and generate graphs showing how everything was connected. The idea was to give Claude a way to understand and navigate the application's knowledge instead of depending on semantic similarity between text chunks. After that, I built a custom MCP server that executes database queries in read-only mode. This gives Claude access to actual database records whenever it needs dynamic information. Finally, I connected everything through Claude CLI. I spent quite a bit of time writing custom rules and instructions for how Claude should handle user questions, understand business logic, query the database, format answers, generate charts, and even create visualizations. And this is where things got interesting. I was expecting decent results, but honestly, they're much better than what I was getting from my previous RAG implementation. Even complicated questions involving multiple modules and business rules are being handled surprisingly well. My estimated hallucination reduction is around 95%, although I haven't done a proper benchmark yet, so take that number with a grain of salt. One thing I particularly like is that I don't have to manually build a separate handler for every possible user question. Claude is capable of understanding the request and deciding what information or tools it needs. I'm currently experimenting with multi-user support, which is another challenge altogether. I need to make absolutely sure that one user's conversation, session, or database access can never expose another user's information. I'm working on enforcing this at the application and MCP server levels, not just through prompts. This is still an experiment. I haven't taken it to production, and I know there are probably things I haven't considered yet. I'm not saying vector databases or traditional RAG are useless. They clearly have their place. But for this particular enterprise use case, my documentation-first approach is giving me better results so far. I'm curious if anyone here has experimented with something similar. Am I approaching this in the right direction, or am I overlooking some obvious architectural problems? Would genuinely appreciate feedback from people who have built production AI agents or worked with complex enterprise RAG systems.
