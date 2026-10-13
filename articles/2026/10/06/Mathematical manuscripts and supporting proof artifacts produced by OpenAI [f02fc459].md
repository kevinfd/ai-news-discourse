---
id: "f02fc4590b9cd78f"
title: "Mathematical manuscripts and supporting proof artifacts produced by OpenAI"
url: "https://github.com/openai/math"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-06T22:22:48Z"
published_date: "2026-10-06"
collected_at: "2026-10-13T20:17:27Z"
authors: ["vikas-sharma"]
language: "en"
summary: "This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model.\nAs part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated. Some outputs build upon earlier results produced by the models.\nThis collection includes results at…"
tags: []
orgs: ["OpenAI"]
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 382
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49984976"
score: 45
comments: 0
community: "Hacker News"
---

# Mathematical manuscripts and supporting proof artifacts produced by OpenAI

GitHub · vikas-sharma · 2026-10-06

This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model.
As part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated. Some outputs build upon earlier results produced by the models.
This collection includes results at different stages of verification. Not all have accompanying Lean formalizations. We will continue to update this repository with Lean formalizations as we obtain them.
Some of the unformalized results could have issues. We will endeavor to fix any such issues quickly. We are also exploring community-hosted repositories for these materials.
The current catalogue contains 719 manuscripts organized into 372 families. A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs. Each family is classified by mathematical discipline.
- Start with the overview for descriptions of the families.
- Use the manuscript map to find individual papers and their supporting materials.
- The preprints/ directory contains PDFs, source files, and manuscript-specific citation and build instructions.
- The Lean library and formalization catalogue describe the available formal proofs, their associated papers, and verification configurations. See the Comparator instructions for additional checking instructions. The repository has ~42% top-line results formalized.
- Updates to the repo are described in the history.
We are also releasing abridged summaries of the model's reasoning, covering the following results:
The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model. On average, each result used three hours of ChatGPT Pro thinking compute with that model. Over the course of the evaluation, the model was posed approximately 4,000 problems. Aggregating the output into result families and manuscripts and requiring an appropriate level of significance led to the catalog outlined above.
Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties. Additionally, the writeup for the Re(s) > 11/12 zero-free region for the Riemann zeta function was human edited for readability.
We will preserve the public release history of this collection. Corrections and revisions will be recorded as new versions, with previously released versions remaining accessible.
To cite the individual manuscript, use the BibTeX block in its directory.
