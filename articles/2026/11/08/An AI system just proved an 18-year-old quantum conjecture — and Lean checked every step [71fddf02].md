---
id: "71fddf02e2ce58cf"
title: "An AI system just proved an 18-year-old quantum conjecture — and Lean checked every step"
url: "https://reddit.com/r/artificial/comments/1xqlg8p/an_ai_system_just_proved_an_18yearold_quantum"
link: "https://reddit.com/r/artificial/comments/1xqlg8p/an_ai_system_just_proved_an_18yearold_quantum"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T00:38:24Z"
published_date: "2026-11-08"
collected_at: "2026-11-08T13:03:58Z"
authors: ["winer666"]
language: "en"
summary: "Physical Superintelligence (PSI) announced on November 6 that an internal research system running instances of a non-public Anthropic model produced a complete proof of the Aaronson–Ambainis conjecture — a quantum-computing question open since 2008 — on the third day of a run. The Lean proof assistant accepted the proof, and the system then improved the result twice, with Lean re-checking each…"
tags: ["r/artificial"]
orgs: ["Anthropic"]
topics: ["models & research", "safety & ethics"]
content_source: "post"
word_count: 232
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xqlg8p/an_ai_system_just_proved_an_18yearold_quantum/"
score: null
comments: null
community: "r/artificial"
---

# An AI system just proved an 18-year-old quantum conjecture — and Lean checked every step

Reddit · winer666 · 2026-11-08

Physical Superintelligence (PSI) announced on November 6 that an internal research system running instances of a non-public Anthropic model produced a complete proof of the Aaronson–Ambainis conjecture — a quantum-computing question open since 2008 — on the third day of a run. The Lean proof assistant accepted the proof, and the system then improved the result twice, with Lean re-checking each version. The paper and the Lean 4 formalization are public. The conjecture is about the limits of quantum speedups: roughly, whether a quantum computer can be exponentially faster than a classical one on unstructured problems. PSI's repo audit says the formalization contains 648 machine-checked theorems with no placeholders and no added axioms, and the declarations were replayed through Lean's kernel and lean4lean, an independent checker. The caveats matter: human mathematicians still need to confirm the formal statement matches Aaronson and Ambainis's original conjecture, the prose paper itself isn't machine-checked, and the model behind the discovery is non-public, so the three-day run can't be reproduced — only the proof can be verified. Source: https://www.unite.ai/psi-reports-machine-checked-proof-of-aaronson-ambainis-conjecture/ If this holds up, it's a striking case of AI doing real mathematics rather than just assisting with it. But it also raises a question: when the discovery process can't be inspected or repeated, and only the final proof is checkable, what does that do to how mathematics is done — and trusted? Curious what people here think.
