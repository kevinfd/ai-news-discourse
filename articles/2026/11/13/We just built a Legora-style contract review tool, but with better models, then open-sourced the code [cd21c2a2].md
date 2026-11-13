---
id: "cd21c2a2e4f9f82e"
title: "We just built a Legora-style contract review tool, but with better models, then open-sourced the code"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xuzvwy/we_just_built_a_legorastyle_contract_review_tool"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xuzvwy/we_just_built_a_legorastyle_contract_review_tool"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T05:49:25Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["ladyofcode"]
language: "en"
summary: "Hey r/ArtificialInteligence ! I’m Tabs, a legal engineer at Isaacus. I built an open-source legal conflict detector that finds deviations and gaps between pairs of legal documents using only encoder models and natural language inference. Inspired by the explosion of interest in discriminative models like TypeSafe AI’s Jev, I wanted to see how far I could get using smaller, non-generative models…"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 625
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xuzvwy/we_just_built_a_legorastyle_contract_review_tool/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# We just built a Legora-style contract review tool, but with better models, then open-sourced the code

Reddit · ladyofcode · 2026-11-13

Hey r/ArtificialInteligence ! I’m Tabs, a legal engineer at Isaacus. I built an open-source legal conflict detector that finds deviations and gaps between pairs of legal documents using only encoder models and natural language inference. Inspired by the explosion of interest in discriminative models like TypeSafe AI’s Jev, I wanted to see how far I could get using smaller, non-generative models for the bulk of the legal document playbook review workflow. The theoretical benefits of a non-generative approach to this problem are enormous. As true clause-level pairwise review is a quadratic problem, it’s unfeasible to do at scale using a model like Opus or Astra. Comparing two average-sized documents with 133 clauses each would take 17,689 API calls, which is far too slow and expensive. Simply uploading the files directly to Claude or GPT is no remedy either. Decoders and agentic architectures don’t have fixed attention that lets them thoroughly analyse a document in one shot. Even with a multi-shot approach, they’re weak on recall and routinely hallucinate. My lawyer friends raise this problem constantly, and I couldn’t find an open-source solution to it, so I decided to build one myself. My pipeline pushes the bulk of the NLI, entailment and reasoning onto faster and more accurate legal encoder models. For the longest document pairs I sampled, the full pipeline ran in under 20 seconds. Unlike generative architectures, these models run a comprehensive pairwise comparison, and although they can still make false positive or false negative errors, those misses and misclassifications aren’t hallucinations (out-of-domain results introduced into the feature set). The pipeline works as follows: Enrich : we enrich each document into a hierarchical tree of sections, clauses and subclauses. Clauses are the key atoms that the pairwise comparisons run on downstream. Embed : we embed each clause as a vector. Filter : we use a legal zero-shot classifier to drop items that aren’t provisions, like footnotes or signature blocks. Shortlist : we keep each clause’s three most relevant pairs from the reference document, as long as their cosine similarity is at least 0.5. Score : we use a reranker and a classifier to score each shortlisted pair. Each answers a question in the format it’s built for: the reranker scores how relevant text is to a search query (relevance), and the classifier scores whether a statement is true (NLI/entailment). Sort : if a clause and its best match are on the same topic but have a high conflict score, it’s a deviation. If there’s no same-topic match, it’s a gap, i.e. the topic is in one document but not the other. That’s the whole conflict detection pipeline. On top of it, you can optionally plug in an LLM to summarise each finding in plain English or redraft a clause to favour the party you’re representing. Because the generative step only runs after the NLI and encoder stack has already decided what the conflicts are, it can’t hallucinate a conflict into existence. To demonstrate the pipeline’s power, we inputted Bob Iger’s 2011 and 2022 Disney employment agreements. The pipeline found many disparities and conflicts, and across most of them, the 2011 agreement was more favourable to Iger than the 2022 one. One interesting finding was a gap: the 2011 agreement had no intellectual property assignment clause, while the 2022 agreement makes Iger assign all work-related IP to Disney, with an exception for inventions he makes on his own time without company resources. The code is MIT-licensed, so it’s free for personal and commercial use. The guide walks through every step, so you can swap in your own models or make your own architectural changes wherever you like. Have fun, and let me know what you think! 😁 Write-up and static demo: https://isaacus.com/blog/build-a-legal-document-conflict-detector GitHub repo: https://github.com/isaacus-dev/cookbooks
