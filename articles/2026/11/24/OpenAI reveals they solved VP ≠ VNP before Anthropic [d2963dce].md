---
id: "d2963dce727becb7"
title: "OpenAI reveals they solved VP ≠ VNP before Anthropic"
url: "https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026"
link: "https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-24T18:55:12Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["iamronaldo"]
language: "en"
summary: "OpenAI · November 23, 2026 edition\nThe November 24 preprints in family 379, Euclidean tensor geometry and its applications to complexity and combinatorics, subsume the results of this preprint. Paths, trees and grids separate Valiant’s hierarchy proves the separation as part of the full arithmetic hierarchy over every field. Circuit lower bounds for Hamiltonian cycle and the permanent…"
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 182
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50632756"
score: 94
comments: 93
community: "Hacker News"
---

# OpenAI reveals they solved VP ≠ VNP before Anthropic

GitHub · iamronaldo · 2026-11-24

OpenAI · November 23, 2026 edition
The November 24 preprints in family 379, Euclidean tensor geometry and its applications to complexity and combinatorics, subsume the results of this preprint. Paths, trees and grids separate Valiant’s hierarchy proves the separation as part of the full arithmetic hierarchy over every field. Circuit lower bounds for Hamiltonian cycle and the permanent strengthens the quantitative lower bounds for both polynomials, with the same characteristic restriction for the permanent.
Theorem 1.1 gives a border arithmetic circuit size lower bound of
$\exp(\Omega((\log n)^{5/4}))$ for an explicit VNP family over every field.
Corollary 1.2 transfers the bound to the directed Hamiltonian cycle polynomial
over every field and to the permanent outside characteristic two.
The Lean proof of the exact VP–VNP separation
is also available in this repository.
The LaTeX source contains the full proof, with TikZ figures and an editable bibliography. To regenerate the PDF with Tectonic, run these commands from this directory.
cd build
tectonic Paper.tex
cp Paper.pdf ../paper.pdf@misc{OAI:VP-and-VNP-are-different-November-23-2026,
  author = {{OpenAI}},
  title = {{VP and VNP are different}},
  year = {2026},
  note = {November 23 edition}
}
