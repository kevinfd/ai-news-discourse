---
id: "5ee1f52190fa8717"
title: "AI needs fresh data. Vector indexing is getting in the way"
url: "https://thenewstack.io/gpu-accelerated-vector-indexing"
link: "https://thenewstack.io/gpu-accelerated-vector-indexing"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T17:11:35Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Meredith Shubel"]
language: "en"
summary: "It’s not a revelation to say AI workflows are changing enterprise infrastructure. What gets less attention, though, is how they’re also shifting the fundamentals of data processing and search. \n\n The complication lies in the data. As organizations build generative AI (GenAI) applications, retrieval-augmented generation (RAG) systems, and AI agents, they’re generating an unwieldy number of…"
tags: ["AI", "AI Infrastructure", "Databases", "Hardware", "sponsor-elastic", "Sponsored", "sponsored-post"]
orgs: ["Nvidia"]
topics: ["search & media", "chips & infrastructure", "models & research", "agents & coding"]
content_source: "summary"
word_count: 1395
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AI needs fresh data. Vector indexing is getting in the way

The New Stack · Meredith Shubel · 2026-11-18

It’s not a revelation to say AI workflows are changing enterprise infrastructure. What gets less attention, though, is how they’re also shifting the fundamentals of data processing and search. 

 The complication lies in the data. As organizations build generative AI (GenAI) applications, retrieval-augmented generation (RAG) systems, and AI agents, they’re generating an unwieldy number of vectors from growing volumes of unstructured data. And with all that vectorized data comes a challenge: how to quickly find the right information to power AI applications and workflows.  

 “After all, a model can only reason over the context you can find and feed it.” 

 Whether it’s a RAG system answering a question or an AI agent taking action, enterprise AI applications succeed on retrieval. After all, a model can only reason over the context you can find and feed it. If those systems rely on wrong or outdated information, even the best model can’t fix the underlying context problem.  

 But finding the right context inside petabytes of enterprise data is a difficult search problem — one keyword search alone is no match.  

 Search has moved beyond keywords 

 In recent years, search has come a long way from basic keyword-based matching. For one, user behavior has spearheaded a push from simple keyword entries to natural language queries. Agent workloads, meanwhile, which query 10 to 100 times more than humans, bring a new dimension to search — and traditional databases are not prepared to keep up. 

 While full-text search uses analyzers and relevance tuning to find exact words and phrases that match the index, semantic search goes beyond keywords to focus on meaning and intent, letting users search with everyday language or synonyms instead of exact index terms. Vector search, meanwhile, enables similarity search, using vector embeddings (i.e., numerical representations of data) stored in vector fields to find items that are semantically similar rather than exact matches.  

 Hybrid search joins keyword and vector search, letting users combine exact keyword matches with meaning-based searches in a single result set.  

 In the new phase of AI adoption, where applications increasingly rely on swathes of unstructured data to retrieve context, traditional keyword search is no longer enough to surface the right information on its own. As a result, organizations are increasingly turning to high-performance vector databases, semantic search, and hybrid search to support new AI workloads.  

 Therein lies the next challenge: indexing all those vectors so they can be searched. 

 Why indexing is the new bottleneck 

 As organizations move from gigabyte-scale search to petabyte-scale AI workloads, the ability to quickly index vectors has become a major factor in determining whether AI applications have current information to work with.  

 The problem is, indexing is often a slow, compute-intensive process, which means it can take days or even weeks for incoming vectors to become searchable.  

 “For customers who want to search across petabytes of data, they may notice that it takes days to weeks to index.” 

 As Rachael Wade , global tech alliances manager at Elastic , tells The New Stack , “For customers who want to search across petabytes of data, they may notice that it takes days to weeks to index.” While a longer indexing timetable may work fine for smaller AI pilots, once it’s time to move those projects into production, indexing delays can significantly stall deployment timelines.  

 A big part of the challenge lies in building the vector index, or HNSW (Hierarchical Navigable Small World) graph, a layered data structure that connects similar vectors to enable efficient search. During construction, vectors must be compared to determine how they should connect in the graph. Because this process can involve millions or even billions of vectors, building a vector index at enterprise scale is compute-intensive and requires a dizzying number of mathematical operations.  

 What happens when enterprises don’t have the compute to keep up? Indexing is slow, so new information takes longer to become searchable, leaving RAG systems, queries, and agents potentially working on stale data.  

 “…the new constraint is getting vectors indexed fast enough to keep that search current.” 

 One example Wade points out to The New Stack is a product catalog, where e-commerce companies rely on fresh data to keep production information up to date and searchable. Manas Singh , technical product manager for accelerated ML and vector search at Nvidia , agrees, adding that, for many companies, “the new constraint is getting vectors indexed fast enough to keep that search current.” 

 It’s time for GPU-accelerated indexing 

 While CPUs have been the default for building vector indexes, IT leaders are starting to realize that CPU-based indexing can struggle to meet the scale and data-freshness requirements of modern AI workloads.  

 For one, indexing vectorized data at petabyte scale can be painstakingly slow, taking days or even weeks. It’s also costly; when you need to index hundreds of millions or billions of vectors, CPU hardware expenses can add up fast.  

 But where CPU-based indexing can be slow and expensive at scale, GPUs are designed for this very kind of large-scale, high-intensity work. For AI workloads with large data volumes and high ingest rates, that makes accelerated computing GPUs built for massive parallelism and high-throughput math ideally positioned for the job.  

 At least that’s the idea behind Elastic and Nvidia’s collaboration on GPU-accelerated vector indexing for Elasticsearch.  

 The integration is powered by Nvidia cuVS, an open-source NVIDIA CUDA-X TM library for GPU-accelerated vector search and data clustering that enables faster index building and embedding retrieval for AI and recommendation workloads. Elasticsearch accesses cuVS through cuvs-java, another open-source library maintained by Nvidia. 

 Elastic, for its part, brings semantic and hybrid search to the table via its enterprise-focused vector database — one of the most widely used in the world that powers semantic search, AI assistants, and recommendations for both startups and enterprises. Developers can trial Elasticsearch for free . 

 By accelerating vector indexing, the Elastic and Nvidia collaboration aims to help enterprises index massive volumes of vectorized data faster so it becomes available sooner for semantic search and AI workloads, including GenAI and AI agents, at speed and scale.  

 The payoff of faster indexing can be substantial. Per Elastic , moving indexing construction to GPU with Nvidia cuVS delivers nearly a 12x boost in indexing throughput and a 7x reduction in force-merge latency, i.e., the time it takes to consolidate small index segments. 

 To put the cost difference in perspective, Wade points to a cost-model example comparing a GPU-based setup with CPU infrastructure. As she tells The New Stack , one GPU, depending on the model, can index hundreds of millions of vectors within a roughly 10-minute SLA. Doing the same work with CPUs, she says, would take about 10 CPUs and require roughly two hours — amounting to what she says is a baseline total cost of ownership savings of 78%.  

 The benefits of GPU acceleration become even more pronounced as vector dimensions increase. Because CPUs take significantly longer to process vectors at higher dimensions, GPU acceleration — whether that’s 5x, 6x, 7x, or even 12x — becomes more valuable at larger scales.  

 Why faster indexing matters now 

 For on-premises deployments, Singh also highlights the indirect benefit of lower search latency.  

 By shifting indexing work from CPUs to faster, more efficient GPUs, enterprises can free up CPUs for other work, thereby allowing the same on-premises hardware to dedicate more resources to search operations. As Singh puts it: “You free up the CPU resources for other things,” which he says can ultimately lead to lower search latency.  

 Meanwhile, because GPU-accelerated vector indexing is available in self-managed Elasticsearch environments, including on-premises, developers can take advantage of faster indexing without having to move workloads off infrastructure they control.  

 Altogether, for IT leaders evaluating hardware with an eye on maximizing ROI and maintaining data sovereignty, that means moving indexing from CPUs to GPUs is a triple win: It can complete more indexing work in less time with less infrastructure, while also meeting self-managed, on-premises deployment requirements and freeing up CPU capacity for search.  

 In the bigger picture, the move toward GPU-accelerated indexing reflects how AI is changing data processing and search. For RAG systems, AI agents, and other retrieval-dependent applications, getting new data searchable quickly is critical to making those systems truly useful. And that starts with faster indexing.  
 The post AI needs fresh data. Vector indexing is getting in the way appeared first on The New Stack .
