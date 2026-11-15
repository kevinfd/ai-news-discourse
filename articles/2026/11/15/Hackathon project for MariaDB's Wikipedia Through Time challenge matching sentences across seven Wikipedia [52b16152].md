---
id: "52b1615201d400a3"
title: "Hackathon project for MariaDB's Wikipedia Through Time challenge: matching sentences across seven Wikipedia editions at any past date [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xwttxo/hackathon_project_for_mariadbs_wikipedia_through"
link: "https://reddit.com/r/MachineLearning/comments/1xwttxo/hackathon_project_for_mariadbs_wikipedia_through"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T12:03:27Z"
published_date: "2026-11-15"
collected_at: "2026-11-15T13:03:31Z"
authors: ["Loxbey"]
language: "en"
summary: "Built at Junction, a hackathon in Espoo, this weekend. Parallax takes an article and lines up its Finnish, Swedish, German, English, Russian, Estonian and Ukrainian editions statement by statement. For any past date it shows where the editions tell something differently. We store every revision. 875,572 so far. Each revision is split into sentences. A sentence that appears in revision A and…"
tags: ["r/MachineLearning"]
orgs: ["Google"]
topics: ["search & media"]
content_source: "post"
word_count: 391
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xwttxo/hackathon_project_for_mariadbs_wikipedia_through/"
score: null
comments: null
community: "r/MachineLearning"
---

# Hackathon project for MariaDB's Wikipedia Through Time challenge: matching sentences across seven Wikipedia editions at any past date [P]

Reddit · Loxbey · 2026-11-15

Built at Junction, a hackathon in Espoo, this weekend. Parallax takes an article and lines up its Finnish, Swedish, German, English, Russian, Estonian and Ukrainian editions statement by statement. For any past date it shows where the editions tell something differently. We store every revision. 875,572 so far. Each revision is split into sentences. A sentence that appears in revision A and disappears in revision B becomes one row in a system-versioned table. Its system-time period is the time the edition said it. Edits undone within 24 hours or by a revert are filtered out so vandalism doesn't cut a sentence's life short. Each distinct sentence is embedded once with bge-m3 (1024 dimensions), however many revisions it shows up in. That's 90,070 vectors, embedded on an A100 at about 4,555 sentences a second. One SQL statement does the time travel and the matching: both sides of a self-join read FOR SYSTEM_TIME AS OF the chosen date and VEC_DISTANCE_COSINE ranks the five closest sentences in each other edition. Inside one article exact search is faster than the HNSW index (4 ms median), so the comparison uses that. Across the whole database the index takes over with recall@10 of 0.997 against exact search at ef_search 1000. Retrieval alone isn't good enough. On 28 pairs we checked by hand the right sentence was top-1 only 57% of the time but in the top 5 for 89%. So Gemini 3.8 Flash judges each candidate pair as same, partial, contradicts or different, pulls out the numbers and terms that differ and translates the statement into English. Verdicts are cached with model and prompt version. The same pipeline checks a chatbot answer. It's split into statements and each one is looked up in the editions. If Gemini is slow, vector similarity decides on its own and the result says so. We asked Gemini how the Winter War started and got 17 statements back. 11 are in at least one edition, 5 in none and the Hanko lease is disputed because the Estonian article removed it in 2009. The weak spot is the judge. 28 hand-checked pairs is a small set to judge a judge by, especially across seven languages. If you've evaluated an LLM judge on cross-lingual sentence pairs, how did you build the gold set? Demo (Winter War preloaded): https://135.181.63.238.sslip.io/t/Q134949 Code and the full query: https://github.com/timkicker/attention-is-all-we-have/tree/main/parallax
