---
id: "e8c9c91d51007648"
title: "Flama: 8 years building a Python framework where ML models and LLMs are first-class, now written up on arXiv [P]"
url: "https://reddit.com/r/MachineLearning/comments/1x4zwp4/flama_8_years_building_a_python_framework_where"
link: "https://reddit.com/r/MachineLearning/comments/1x4zwp4/flama_8_years_building_a_python_framework_where"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T15:35:48Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["p3rdy"]
language: "en"
summary: "I started Flama in 2018 to take a trained model to a production API with as little ceremony as possible. With 2.0 LLMs became first-class alongside classic models, and together with Miguel Durán-Olivencia we've now written up the whole architecture in an 83-page paper on arXiv (2608.18733). A model is a file Every model, whether a scikit-learn pipeline, a PyTorch network or an LLM, is packaged…"
tags: ["r/MachineLearning"]
orgs: ["OpenAI", "Anthropic", "Apple"]
topics: ["models & research", "products & launches", "jobs & society", "agents & coding"]
content_source: "post"
word_count: 389
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1x4zwp4/flama_8_years_building_a_python_framework_where/"
score: null
comments: null
community: "r/MachineLearning"
---

# Flama: 8 years building a Python framework where ML models and LLMs are first-class, now written up on arXiv [P]

Reddit · p3rdy · 2026-10-13

I started Flama in 2018 to take a trained model to a production API with as little ceremony as possible. With 2.0 LLMs became first-class alongside classic models, and together with Miguel Durán-Olivencia we've now written up the whole architecture in an 83-page paper on arXiv (2608.18733). A model is a file Every model, whether a scikit-learn pipeline, a PyTorch network or an LLM, is packaged into a single .flm : the weights, the artifacts it needs at inference time (tokenizer, config) and its metadata, including the training metrics you record. The metadata sits ahead of the weights, so flama model <file> inspect reads it without loading anything, and a CI job can gate promotion on those metrics without standing up a server. flama model <file> run scores a reference set offline on the same code path the server uses. The inference engine isn't baked in either: the same LLM file runs on vLLM or MLX, depending on where you deploy it. One model, four protocols from flama import Flama app = Flama() app.models.add_model( path="/llm/", model="google_gemma-4-E2B-it.flm", name="assistant", serving=("native", "openai", "anthropic", "ollama"), ) That model answers OpenAI ( /llm/openai/v1/chat/completions ), Anthropic ( /llm/anthropic/v1/messages ) and Ollama ( /llm/ollama/api/chat ) routes at the same time, with a streaming chat UI at /llm/chat/ , next to your own endpoints and your classic models. https://i.redd.it/lq0plprg69vh1.gif Three independent layers A request goes through a dialect, a canonical transport and a backend (vLLM on Linux with CUDA, MLX on Apple Silicon). Because the layers only meet in the middle, any dialect works on any backend, which is also why tool calls and token usage come out right in every protocol. The rest of the framework Dependency Injection resolved from type hints Schemas with Pydantic, Marshmallow or Typesystem, and OpenAPI docs generated from your handlers CRUD APIs generated from SQLAlchemy tables DDD building blocks: repositories and workers (units of work) JWT authentication MCP: turn any app into an MCP server `flama upgrade`, codemods that migrate your code between versions A Rust core for routing, serialising, parsing, crypto and compressing The paper walks through each subsystem and compares Flama with web frameworks, model servers and LLM inference engines (Table 1). Paper: https://arxiv.org/abs/2608.18733 Code: https://github.com/vortico/flama If you find it useful, a star on GitHub helps more people find it, and I'm happy to answer anything about the design.
