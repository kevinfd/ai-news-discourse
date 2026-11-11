---
id: "4afdd91ba02f9082"
title: "Google DeepMind's AlphaProof Code proved Signal's actual compiled code secure in 4 weeks, with humans reviewing only 1%"
url: "https://reddit.com/r/artificial/comments/1xsoqnj/google_deepminds_alphaproof_code_proved_signals"
link: "https://reddit.com/r/artificial/comments/1xsoqnj/google_deepminds_alphaproof_code_proved_signals"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T14:47:04Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["javimbuilds"]
language: "en"
summary: "The part that got me is that this covers the implementation, not just the protocol design. Most protocol verification stops at the spec, and real bugs tend to live in the gap between spec and code. Gemini-powered agents wrote over six million lines of Lean proofs, Lean checked them, and human experts only reviewed the roughly 1% the agents flagged. As a sanity check, they reintroduced two old,…"
tags: ["r/artificial"]
orgs: ["Google"]
topics: ["agents & coding", "business & funding"]
content_source: "post"
word_count: 130
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xsoqnj/google_deepminds_alphaproof_code_proved_signals/"
score: null
comments: null
community: "r/artificial"
---

# Google DeepMind's AlphaProof Code proved Signal's actual compiled code secure in 4 weeks, with humans reviewing only 1%

Reddit · javimbuilds · 2026-11-10

The part that got me is that this covers the implementation, not just the protocol design. Most protocol verification stops at the spec, and real bugs tend to live in the gap between spec and code. Gemini-powered agents wrote over six million lines of Lean proofs, Lean checked them, and human experts only reviewed the roughly 1% the agents flagged. As a sanity check, they reintroduced two old, already fixed Signal bugs, and the system produced machine-checked proofs that those versions were insecure. The catch for me as a builder is that humans still wrote and reviewed every spec, so the proof is only as good as what you decided to prove. Would you trust this on your own codebase, or is writing correct specs still the real bottleneck? https://deepmind.google/blog/introducing-alphaproof-code/
