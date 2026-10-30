---
id: "24501a59a80bc482"
title: "W(2;3,21) = 416 - a van der Waerden number conjectured by Kullmann in 2010, now proved with a Lean 4 kernel-checked proof [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xivpue/w2321_416_a_van_der_waerden_number_conjectured_by"
link: "https://reddit.com/r/MachineLearning/comments/1xivpue/w2321_416_a_van_der_waerden_number_conjectured_by"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T20:46:25Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Rodriguez909"]
language: "en"
summary: "w(2;3,21) = 416 - today proved with a Lean 4 kernel- checked proof (preprint + 13.6 GB evidence package). Every red-blue colouring of {1, ..., 416} contains a red 3-term or a blue 21-term arithmetic progression, and some colouring of {1, ..., 415} contains neither. Kullmann conjectured the value in 2010; DeepMind's Formal Conjectures list still carried it as open this year. The proof is a Lean 4…"
tags: ["r/MachineLearning"]
orgs: ["Google"]
topics: ["models & research"]
content_source: "post"
word_count: 142
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xivpue/w2321_416_a_van_der_waerden_number_conjectured_by/"
score: null
comments: null
community: "r/MachineLearning"
---

# W(2;3,21) = 416 - a van der Waerden number conjectured by Kullmann in 2010, now proved with a Lean 4 kernel-checked proof [R]

Reddit · Rodriguez909 · 2026-10-29

w(2;3,21) = 416 - today proved with a Lean 4 kernel- checked proof (preprint + 13.6 GB evidence package). Every red-blue colouring of {1, ..., 416} contains a red 3-term or a blue 21-term arithmetic progression, and some colouring of {1, ..., 415} contains neither. Kullmann conjectured the value in 2010; DeepMind's Formal Conjectures list still carried it as open this year. The proof is a Lean 4 theorem over 209 cases and 38,661,140 leaf formulas, each refutation checked by cake_pr (the LRAT checker verified in CakeML) and bound by digest to its Lean term. It was produced with LPM (Large Proof Model), a neuro-symbolic system from Hupyy; nothing counted unless the Lean kernel or cake_pr accepted it. Paper : https://doi.org/10.5281/zenodo.23776306 Evidence package (Lean sources, checker records, replay kit): https://doi.org/10.5281/zenodo.23749222 To check : download it and run 'shasum -a 256 -c SHA256SUMS'
