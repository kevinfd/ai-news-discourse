---
id: "aa308abe3c92a212"
title: "Google DeepMind Uses AI Agents to Verify Signal’s Core Machine Code"
url: "https://unite.ai/google-deepmind-uses-ai-agents-to-verify-signals-core-machine-code"
link: "https://unite.ai/google-deepmind-uses-ai-agents-to-verify-signals-core-machine-code"
source: "Unite.AI"
domain: "unite.ai"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-10T04:37:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Jonas Reeve", "Cognitive AI", "AGI AI Research Agent"]
language: "en"
summary: "Google DeepMind introduced AlphaProof Code on November 10, 2026, using teams of AI agents to produce machine-checked Lean proofs for specified security properties of Signal’s compiled libsignal code."
tags: []
orgs: ["Google", "Anthropic"]
topics: ["agents & coding", "models & research", "business & funding", "jobs & society"]
content_source: "fulltext"
word_count: 795
paywalled: false
image: "http://www.bing.com/th?id=ONUT.pPfUoFktL8oEGoxHqJyz1w&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Google DeepMind Uses AI Agents to Verify Signal’s Core Machine Code

Unite.AI · Jonas Reeve, Cognitive AI, AGI AI Research Agent · 2026-11-10

AI Models & Platforms
Google DeepMind Uses AI Agents to Verify Signal’s Core Machine Code
Add Unite.AI to your preferred sources on Google
Google DeepMind introduced AlphaProof Code on November 10, 2026, using teams of AI agents to produce machine-checked Lean proofs for specified security properties of Signal’s compiled libsignal code. The five-person research team completed the proof work in four weeks and released its specifications and verification artifacts for outside review.
The work moved beyond an abstract model of Signal’s protocol design to its compiled implementation. Researchers wrapped the unmodified libsignal v0.105.4 and SPQR v1.6.0 crates in a small command-line harness, then used stock rustc to build a statically linked AArch64 Linux executable. The technical paper describes the result as the first protocol-level security proofs for the unmodified code of a widely deployed cryptographic protocol implementation.
How AlphaProof Code Divided the Work
Five researchers spent four weeks on the proof work, running agents continuously on their workstations while pursuing symbolic and computational proofs in parallel. The paper reports that the agents generated about 6.5 million lines of machine-checked Lean proof code, resting on roughly 26,000 lines of trusted specifications and AArch64 semantics.
Humans selected the properties, resolved ambiguities and security trade-offs, reviewed specifications and retained final approval. Agents powered by Gemini 4 Carbon and Claude Opus 5.5 drafted and reviewed those specifications, including review from a different model family. Gemini 4 Carbon agent teams then generated all the proof code; none of the authors wrote proof code. Typical campaigns used 40 to 80 agents on one machine for 24 to 72 hours, with an orchestrator and team leads coordinating proof workers while architect and integrator roles maintained the shared proof base.
A gatekeeper accepted a proof only after Lean’s kernel checked it and a comparator confirmed that it matched the held-out, human-approved specification, including every transitive definition, using only Lean’s standard axioms. Agents could propose small amendments when proofs exposed specification problems, but changes to trusted assumptions required human approval or a user-set policy and were logged with justifications. The control addresses a documented risk in agent-generated proofs: a specification can be weakened indirectly through one of its definitions.
Security Coverage and Historical Bug Tests
The verified target was one-to-one session code covering the PQXDH handshake and Triple Ratchet messaging. The researchers report two independent arguments: ten symbolic theorems under idealized cryptographic assumptions and a computational proof bounding an attacker’s advantage through cryptographic assumptions and statistical terms. Their properties include forward secrecy, which protects earlier messages after current state is stolen; authentication; post-compromise security, which concerns recovery after a compromise; and handshake secrecy. The symbolic argument additionally covers handshake secrecy after a later Diffie–Hellman break.
To test whether those specifications could catch real errors, the team reverse-applied the fixes for two previously repaired libsignal bugs, known as weak state and small subgroup, and recompiled the altered binaries. In both cases, it produced Lean proofs that the symbolic security theorem failed. The public verification repository separates the computational, symbolic, shared binary and AArch64-semantics material and documents how to rebuild and independently check the proofs.
Signal chief technology officer Ehren Kret said the work “gives us even greater confidence in our code’s privacy guarantees.”
Limits and Next Steps
The guarantees stop well short of certifying Signal’s complete applications. They concern the researchers’ libsignal-cli build running as a fresh process; key generation was not verified, group messaging was left for future work, and side channels and multi-device state fall outside the scenario. Low-level cryptographic primitives and selected output and library routines are represented by trusted contracts, so the result also depends on those contracts, the approved specifications, Lean’s kernel, the AArch64 semantics and assumptions about the primitives.
The paper states that neither argument proves the post-quantum healing that SPQR is designed to add: the computational theorem covers classical attackers, while the symbolic ratchet theorems let the attacker choose SPQR keys. The computational model also restricts several attacker actions and becomes vacuous at sufficiently large message and session scales. These boundaries define what an outside reviewer must trust before treating the machine-checked proofs as a security guarantee for a particular deployment.
The researchers’ stated next steps are to strengthen the theorems, reduce the trusted base by verifying more hooked routines and connecting cryptographic contracts to verified implementations, and expand coverage to group messaging, sealed sender and server-side protocols. Their objective of verifying new libsignal releases before shipment is a research goal, not an announced deployment.
The result’s immediate significance is the division of labor it demonstrates: agents handled the proof construction, while assurance still rests on human-reviewed specifications and explicit assumptions. Releasing the proofs and checking procedures gives outside reviewers a way to test that foundation as the researchers work to carry the workflow into continuing libsignal development.
