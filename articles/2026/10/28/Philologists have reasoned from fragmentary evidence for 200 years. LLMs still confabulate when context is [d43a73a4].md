---
id: "d43a73a403644005"
title: "Philologists have reasoned from fragmentary evidence for 200 years. LLMs still confabulate when context is missing."
url: "https://reddit.com/r/artificial/comments/1xhj4rf/philologists_have_reasoned_from_fragmentary"
link: "https://reddit.com/r/artificial/comments/1xhj4rf/philologists_have_reasoned_from_fragmentary"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-28T09:12:46Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["vasilisvj"]
language: "en"
summary: "Of everything Thales supposedly wrote, not one authenticated word survives. Anaximander wrote the first prose treatise in the Greek tradition. Today it exists as roughly one sentence, preserved only because Aristotle quoted it and Simplicius, almost a thousand years later, copied that quotation. Heraclitus comes down in scattered aphorisms, most of them embedded in sermons of church fathers who…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 646
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xhj4rf/philologists_have_reasoned_from_fragmentary/"
score: null
comments: null
community: "r/artificial"
---

# Philologists have reasoned from fragmentary evidence for 200 years. LLMs still confabulate when context is missing.

Reddit · vasilisvj · 2026-10-28

Of everything Thales supposedly wrote, not one authenticated word survives. Anaximander wrote the first prose treatise in the Greek tradition. Today it exists as roughly one sentence, preserved only because Aristotle quoted it and Simplicius, almost a thousand years later, copied that quotation. Heraclitus comes down in scattered aphorisms, most of them embedded in sermons of church fathers who quoted him to refute him. And yet classical philology built a rigorous discipline on top of this wreckage. Two and a half centuries of fragment scholarship produced methods for reasoning honestly from partial evidence. I think this is one of the most underrated bodies of technique in existence, and almost nobody in ML knows it. The core move is simple to state and hard to practice: never let inference masquerade as attestation. When a philologist reconstructs a lacuna in a papyrus, the reconstruction is printed in brackets or in a different typeface. The reader always sees where the evidence stops and where the scholar's judgment begins. Diels-Kranz, the standard edition of the Presocratics, physically separates the fragments (ipsissima verba, what the philosopher actually wrote) from the testimonia (what later authors say about him). Two thousand years of interpretation get sorted into a different column than twenty surviving sentences. Aristotle made the distinction theoretical. In the Rhetoric and the Analytics he separates τεκμήριον from mere sign: a τεκμήριον is necessary evidence, it compels the conclusion and cannot be refuted. A probable sign supports a claim but leaves it open. The whole epistemic weight of an argument depends on knowing which one you hold. Confuse them and you get rhetoric instead of knowledge. Now compare this with how a modern LLM behaves when context runs out. Ask it about a fragmentary source, a lost work, a gap in the record, and it fills the gap fluently. No brackets. No typeface change. No column separating what is attested from what is generated. The output carries the same surface confidence whether it stands on a direct quotation or on nothing at all. The model does not have a register for "here the evidence stops." This is not only a hallucination problem. Hallucination discourse treats the failure as accidental, something better training or retrieval will fix. The philological tradition suggests the failure is structural: the system has no internal representation of evidential weight. It cannot distinguish attestation from inference because nothing in its output format, and arguably nothing in its training signal, requires the distinction. Preference raters reward fluent completeness. Nobody upvotes a bracket. There are partial fixes. Citation-grounded generation, RAG with source attribution, confidence calibration. But notice these are all bolted on externally. The brackets come from the retrieval layer, not from the reasoning itself. A philologist carries the distinction inside the method. Every claim is tagged by its evidential status before it is written down. I work with classical corpus AI and this contrast shapes a lot of my thinking. The interesting question is not "how do we stop models inventing facts." It is "how do we make evidential status a first-class object inside the reasoning process, the way two centuries of German philology made it first-class inside the edition." Some will say the analogy fails because humans also confabulate. True. But human scholarship built institutions, conventions, and notational systems that catch confabulation socially. The bracket, the apparatus criticus, the separation of fragment from testimony: these are alignment techniques for human reasoners, developed over generations, and they work. We are trying to solve a problem in 2026 that Anaximander's editors solved in 1903, and we keep ignoring the solution because it looks like dusty bookkeeping instead of intelligence. Maybe honest reasoning under incomplete information is less about more parameters and more about better brackets. What would an evidential-status-aware architecture look like to you: something learned end-to-end, or something structural like the philological apparatus, enforced by format rather than by weights?
