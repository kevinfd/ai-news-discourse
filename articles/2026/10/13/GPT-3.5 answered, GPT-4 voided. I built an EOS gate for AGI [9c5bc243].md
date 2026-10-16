---
id: "9c5bc243ea8b3106"
title: "GPT-3.5 answered, GPT-4 voided. I built an EOS gate for AGI"
url: "https://getswiftapi.com"
link: "https://getswiftapi.com"
source: "SwiftAPI Labs"
domain: "getswiftapi.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T04:48:43Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["rayanpal_"]
language: "en"
summary: "Void measurements\nObserve noncontinuation.\nCondition-sensitive zero-visible-byte executions in frontier models.\nCross-vendor evidence →\nNew paper · September 23, 2026\nIdentical semantic requests. Identical settings. GPT-4 returned zero-visible-byte normal-stop responses on 30/30 null trials. GPT-3.5 returned visible text on all 30. Both models returned visible text on all matched controls.\n-…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "safety & ethics", "policy & regulation"]
content_source: "fulltext"
word_count: 780
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x4nn27/gpt35_answered_gpt4_voided_i_built_an_eos_gate/"
score: null
comments: null
community: "r/artificial"
---

# GPT-3.5 answered, GPT-4 voided. I built an EOS gate for AGI

SwiftAPI Labs · rayanpal_ · 2026-10-13

Void measurements
Observe noncontinuation.
Condition-sensitive zero-visible-byte executions in frontier models.
Cross-vendor evidence →
New paper · September 23, 2026
Identical semantic requests. Identical settings. GPT-4 returned zero-visible-byte normal-stop responses on 30/30 null trials. GPT-3.5 returned visible text on all 30. Both models returned visible text on all matched controls.
- GPT-3.5 · Null V0
- 0/30
- GPT-4 · Null V0
- 30/30
- Control V0 · Each model
- 0/30
V0: successful response, exactly empty text, normal stop. A pinned-snapshot comparison, not a same-date emergence study or a claim about the internal stopping mechanism.
PCCG-2 · Open weights, code, and evidence
Permission changed.
A frozen Qwen3-4B model supplies the answer. A learned 101-parameter gate changes only the native termination score, controlling whether that answer enters generation.
Recorded evidence · Paper Figure 2
The answer score stays at 53.0 in every arm. Only the native EOS score moves.
0 non-EOS logits changed.The complete non-EOS first-token vector is byte-identical across all five arms.
Inspect all five arms and their shared vector hash →
PCCG-2 · Frozen evaluation
- Combined FINAL
- 2,048/2,048
- Answer → native EOS
- 40/40
- Native EOS → correct answer
- 40/40
75 FINAL answer identities. 40 causal answer identities. 80/80 sham controls unchanged. 188/188 question-only controls unchanged.
A separate finite-precision certificate covers every accepted six-digit equality condition across the 188 frozen bank computations. Inspect the full-domain certificate →
Research progression
PCCG-1
Reverse GO versus EOS after a fixed correct reasoning prefix. Jacobian Lens supplies interpretability readouts.
PCCG-1 study →
PCCG-2
Frozen answer computation and a learned condition-only gate. Every non-EOS logit stays fixed.
PCCG-2 release →
Frontier-model research
A provider-aware classification of successful model executions with zero visible output bytes.
A Void is a model execution returning a successful provider response with exactly zero visible UTF-8 output bytes. Provider termination metadata determines its subtype. Explicit refusals, safety blocks, tool-mediated executions, and transport, protocol, billing, quota, rate-limit, and infrastructure failures are distinct non-Void outcomes.
VOID is not an error label. It is a precisely classified successful execution with zero visible output bytes, separated from refusals, safety events, tool calls, and operational failures.
Cross-vendor evidence
A frozen cross-vendor behavioral study of successful zero-visible-byte executions across 11 exact model identifiers and four providers.
31,430completed frozen trials
11exact model identifiers
4provider surfaces
11,658total Void outcomes
2,505matched null-arm Voids
0 / 4,290matched output-licensed control Voids
Exact frozen model identifiers
- gpt-4-0613
- gpt-5.2-2025-12-11
- gpt-5.5-2026-04-23
- gpt-5.6-luna
- gpt-5.6-sol
- gpt-5.6-terra
- claude-opus-4-6
- claude-fable-5
- claude-opus-5
- gemini-3.5-flash
- kimi-k3
Cross-script research
A frozen GPT-5.4 study documenting a reproducible prompt-conditioned Arabic-Hebrew hybrid Unicode output regime under two system prompts differing by one Hebrew code point.
12,160scheduled and retained trials
7,253exact primary artifacts
94.3359%dotted condition
47.3242%undotted condition
47.0117 pprisk difference
7,253 / 7,253condition-congruent exact artifacts
Research process
The laboratory uses a repeatable process for turning unusual model behavior into inspectable public records.
- 01Observation
- 02Frozen protocol
- 03Automated execution
- 04Raw preservation
- 05Classification
- 06Verification
- 07Publication
- 08Operationalization
Foundational work
Earlier empirical results, theoretical frameworks, and infrastructure specifications remain part of the public record.
The earlier cross-model convergence result that preceded the larger cross-vendor matrix.
- 180/180 null trials in the published two-model protocol
- GPT-5.2 and Claude Opus 4.6
- Matched non-null controls produced visible responses
This is a black-box behavioral result under the published protocol, not evidence of consciousness, intention, or a specific internal mechanism.
A proposed criterion defining AGI as the capacity to carry binding conditions across domains.
- AGI is the capacity to carry binding conditions across domains.
- A binding condition is the prerequisite that must hold for valid continuation.
This is a published theoretical framework, not a settled industry definition, regulatory standard, or result established solely by the VOID benchmark.
The initial public framework for observing high-order model behavior and the Void.
This publication records an early research framework and observation history.
The public specification for cryptographically signed execution attestations.
- Ed25519 signatures
- Offline verification
- Revocation and replay defense
This is an infrastructure specification, not an empirical model-behavior study.
From research to infrastructure
The laboratory's infrastructure exists to preserve, verify, and operationalize research findings. It is supporting evidence that the work can move from publication into real systems.
Ed25519 execution attestations with offline verification.
Immediate revocation checks, unique identifiers, and expiry.
Scoped keys, policy-deny behavior, grants, and audit records.
SDK, API, proxy, and runtime enforcement interfaces.
Enterprise evaluations
SwiftAPI Labs conducts paid, time-bounded evaluations for organizations deploying frontier models and autonomous agents. Evaluations reproduce model behavior through the customer's route, preserve raw provider metadata, classify terminal states, map retry and continuation behavior, and produce a written implementation decision.
Continue
