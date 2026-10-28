---
id: "843f65c8e8733c45"
title: "Meet LEANN: An Open-Source Vector Index that Shrinks a 60M-Chunk RAG Index from 201 GB to 6 GB"
url: "https://marktechpost.com/2026/10/27/leann-vector-index-mlsys-2026"
link: "https://marktechpost.com/2026/10/27/leann-vector-index-mlsys-2026"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T21:54:37Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "UC Berkeley’s Sky Computing Lab built LEANN , an open-source vector index that stores almost no embeddings. The LEANN vector index recomputes embeddings at query time instead of saving them to disk. The repo benchmark shows a 60 million chunk Wikipedia index dropping from 201 GB to 6 GB. The research paper won the Best Research Paper award at MLSys 2026 . So, it brings semantic search and RAG…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Artificial Intelligence", "Editors Pick", "Language Model", "Machine Learning", "New Releases", "Open Source", "Staff", "Tech News"]
orgs: ["Anthropic", "OpenAI", "Apple", "Hugging Face"]
topics: ["models & research", "search & media", "agents & coding", "business & funding"]
content_source: "summary"
word_count: 981
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet LEANN: An Open-Source Vector Index that Shrinks a 60M-Chunk RAG Index from 201 GB to 6 GB

MarkTechPost · Asif Razzaq · 2026-10-27

UC Berkeley’s Sky Computing Lab built LEANN , an open-source vector index that stores almost no embeddings. The LEANN vector index recomputes embeddings at query time instead of saving them to disk. The repo benchmark shows a 60 million chunk Wikipedia index dropping from 201 GB to 6 GB. The research paper won the Best Research Paper award at MLSys 2026 . So, it brings semantic search and RAG over personal data, on a laptop. 

 TL;DR 

 Size: 6 GB for 60M chunks ( repo ); 4 GB in the paper’s 76 GB Wikipedia setup. Default embedder: Contriever (110M params). It is an index, not an LLM, so no context length applies. 

 Runs on: laptops and workstations. The paper tested an RTX 4090 box with 32 GB RAM and an M1 Ultra Mac. A CPU-only Linux install exists, with no published CPU latency. 

 Performance: matches HNSW downstream accuracy at 90% recall, using under 5% of raw-data storage. 

 Best: 25.5% NQ accuracy, identical to HNSW, using 4 GB instead of 188 GB. 

 Worst: HotpotQA retrieval takes 44.80 s on the Mac, 50.1% of total pipeline time. 

 What is LEANN? 

 LEANN is a low-storage approximate nearest neighbor (ANN) index built on top of FAISS . It targets one problem: vector indexes are often bigger than the data they index. The research paper shows a 76 GB corpus needs 173 GB of embeddings plus a 15 GB HNSW graph. That more than doubles the raw data. 

 LEANN keeps a pruned graph, drops the full vectors, and rebuilds them on demand. The code is MIT licensed and installs with uv pip install leann . 

 How does LEANN recompute embeddings without stalling search? 

 Graph indexes like HNSW visit only a small set of nodes per query. LEANN exploits that. It stores the graph plus a compact product quantization (PQ) table. At query time, it re-embeds only nodes on the search path. 

 3 techniques keep this practical: 

 Two-level search: cheap PQ distances rank neighbors first. Only top candidates get exact recomputation. 

 Dynamic batching: candidates from several hops are grouped, for example 64 at once, for GPU efficiency. 

 High-degree preserving pruning: most nodes keep few edges, while the top 2% “hub” nodes keep more. 

 In ablations, two-level search gives an average 1.4x speedup. Adding batching raises it to 1.8x. Embedding recomputation still accounts for about 76% of query latency. 

&&

 How does LEANN perform on benchmarks? 

 The research team tested NQ, TriviaQA, GPQA and HotpotQA against a 60M-passage RPJ-Wiki datastore. Latency is measured at 90% Recall@3. All figures below are self-reported in the research paper . 

 On NQ, with Qwen3-4B on an RTX 4090, LEANN and HNSW both reach 25.5% downstream accuracy. LEANN uses 4 GB of storage. HNSW uses 188 GB. BM25 scores 18.3%, and PQ compression scores 17.9%. 

 The cost is search time. LEANN retrieval takes 2.48 s on NQ, versus 0.05 s for HNSW. Generation takes about 20 s, so end-to-end latency rises from 20.95 s to 23.34 s. 

 Across datasets on the RTX 4090, LEANN retrieval ranges from 1.12 s (GPQA) to 7.12 s (HotpotQA). The IVF-based recomputation baseline, inspired by EdgeRAG , is up to 200x slower. LEANN improves exact match by up to 11.8% over BM25. 

 The GitHub repo reports similar savings on personal data. 400K chat messages shrink from 1.8 GB to 64 MB. 38K browser entries shrink from 130 MB to 6.4 MB. 

 LEANN vs other vector indexes 

 Feature LEANN HNSW (FAISS) DiskANN IVF-Recompute (EdgeRAG-style) PQ compression Approach Pruned graph, recompute on demand Graph plus all vectors in RAM Graph and vectors on SSD, PQ in RAM IVF clusters, recompute on demand Compressed vectors plus graph Storage, 76 GB corpus 4 GB 188 GB 270 GB Below 5% of raw data 20 GB NQ retrieval at 90% recall (RTX 4090) 2.48 s 0.05 s 0.03 s 307.61 s Fails to reach 90% HotpotQA retrieval at 90% recall (RTX 4090) 7.12 s 0.05 s 0.11 s 429.46 s Fails to reach 90% NQ downstream accuracy (Qwen3-4B) 25.5% 25.5% Not disclosed Not disclosed 17.9% Fits 32 GB RAM workstation Yes No (OOM) Yes Yes Yes License MIT MIT MIT Not disclosed Varies by implementation 

 Storage, latency and accuracy figures come from the LEANN paper v2 , Tables 1 and 2 and Section 7.2 (self-reported). License and design rows link to each project’s own source. 

 Where can developers use LEANN? 

 The repo ships ready apps for documents, Apple Mail, Chrome history, WeChat, iMessage, and ChatGPT or Claude exports. MCP readers pull live data from Slack and Twitter bookmarks. LEANN also runs as a semantic search MCP server for Claude Code . 

 On 30 SWE-Bench Pro tasks from ContextBench, the team reports 24.2% initial relevant-code recall versus 11.4% for BM25. The agent also used 8.4% fewer tokens. 

 HNSW is the default backend, with DiskANN for faster search. Generation works with Ollama, Hugging Face, Anthropic, or any OpenAI-compatible API. It supports Ubuntu, Arch, WSL, macOS and Windows. Some apps, like Apple Mail search, are macOS only. 

 Key Takeaways 

 LEANN stores a pruned graph and recomputes embeddings at query time. 

 60M chunks: 201 GB down to 6 GB in the repo benchmark. 

 Matches HNSW accuracy (25.5% on NQ) at 90% recall. 

 Search costs seconds: 2.48 s vs 0.05 s for HNSW on NQ. 

 MIT licensed and an MLSys 2026 Best Research Paper. 

 Check out the Paper , GitHub Repo and PyPI package . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meet LEANN: An Open-Source Vector Index that Shrinks a 60M-Chunk RAG Index from 201 GB to 6 GB appeared first on MarkTechPost .
