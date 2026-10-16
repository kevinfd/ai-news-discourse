---
id: "7338cb1ff5127dff"
title: "Qdrant tests Perplexity’s PDF embeddings: 21× smaller compressed vectors, with originals still stored"
url: "https://reddit.com/r/artificial/comments/1x7dxuw/qdrant_tests_perplexitys_pdf_embeddings_21"
link: "https://reddit.com/r/artificial/comments/1x7dxuw/qdrant_tests_perplexitys_pdf_embeddings_21"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T11:41:47Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jrxna"]
language: "en"
summary: "Qdrant tested Perplexity’s new visual document embeddings on 11,609 pages across four ViDoRe v3 datasets. The models search pages as images, so tables and layout can stay intact. Their result: 1-bit TurboQuant reduced the compressed vectors from 856 KB to 40 KB per page while retaining 96.5% of the float32 retrieval score. Rescoring against the originals brought that to 99.9%. The important…"
tags: ["r/artificial"]
orgs: ["Perplexity"]
topics: ["business & funding", "search & media", "models & research"]
content_source: "post"
word_count: 117
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x7dxuw/qdrant_tests_perplexitys_pdf_embeddings_21/"
score: null
comments: null
community: "r/artificial"
---

# Qdrant tests Perplexity’s PDF embeddings: 21× smaller compressed vectors, with originals still stored

Reddit · jrxna · 2026-10-16

Qdrant tested Perplexity’s new visual document embeddings on 11,609 pages across four ViDoRe v3 datasets. The models search pages as images, so tables and layout can stay intact. Their result: 1-bit TurboQuant reduced the compressed vectors from 856 KB to 40 KB per page while retaining 96.5% of the float32 retrieval score. Rescoring against the originals brought that to 99.9%. The important catch is storage: those 40 KB exclude the original vectors, which Qdrant still keeps. The million-page figures are projections, not a million-page benchmark. This is Qdrant’s own test. For anyone working with document search, where does this tradeoff stop being worthwhile: disk reads for rescoring, indexing cost, or errors on your actual queries? Source: https://qdrant.tech/blog/pplx-embed-v2/
