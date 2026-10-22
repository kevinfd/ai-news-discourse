---
id: "790313ac5aeace30"
title: "Evals, And How They Help Build Good AI Agents For Enterprises​"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/22/evals-and-how-they-help-build-good-ai-agents-for-enterprises"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/22/evals-and-how-they-help-build-good-ai-agents-for-enterprises"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-22T11:00:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Rohit Patel, Forbes Councils Member"]
language: "en"
summary: "My core rule for enterprise AI is simple: Build your evals first.​"
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["models & research", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 976
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/69273f54c80df92a6c936a76/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Evals, And How They Help Build Good AI Agents For Enterprises​

Forbes · Rohit Patel, Forbes Councils Member · 2026-10-22

Rohit Patel, Founder and CEO of ndoc.ai.
Every executive today feels the urgency to deploy generative AI. Boardrooms want autonomous agents that can resolve customer inquiries, synthesize contracts and automate multistep operational workflows. Early prototypes look dazzling: Within hours, an engineering team can connect a foundation model to internal APIs and produce a demo that feels like magic.
Yet a familiar pattern has emerged across industries: Promising pilots stall before reaching production, or stumble once exposed to real users. Up to 95% of enterprise AI programs fail to deliver measurable value. While leaders often blame hallucinations or edge cases, RAND Corporation research shows the real root cause lies in how we build, with failure rates doubling those of conventional IT projects.
Agentic Performance: The Measurement Challenge
Why is measuring AI agent performance so difficult? Unlike traditional enterprise software, evaluating agentic systems presents two fundamental hurdles:
First, AI is non-deterministic. Traditional software is deterministic: Developers write explicit rules and unit tests, asserting that input X always yields exact output Y. Generative AI breaks this paradigm. At its core, an LLM is an intuition machine calculating statistical probabilities. Because agents produce open-ended language and multistep decisions, you cannot check for an exact match. A customer service response can be phrased in dozens of valid ways while remaining accurate and compliant, yet it can also sound completely fluent while being subtly incorrect.
Second, AI operates along a “jagged intelligence frontier.” In humans, capability scales predictably: Someone who can synthesize a 50-page regulatory filing can easily perform basic arithmetic. In AI, that assumption fails. A model might draft brilliant corporate strategy one moment, yet fail at elementary math or hallucinate a basic company policy the next. Superior performance on one task doesn’t guarantee reliability on another.
Because of these twin challenges, too many organizations fall back on “vibe checks.” Teams test a few cherry-picked prompts, nod at impressive demos and green-light deployment. In an enterprise environment, launching mission-critical software on subjective impressions invites severe brand, legal and operational risks.
This is why AI evaluations (“evals”) are the single most critical foundation of any enterprise AI initiative.
What Is An AI Eval?
An eval is the AI counterpart to an automated software test suite. In concrete terms, an eval is an automated testing harness that subjects an AI model to a standardized battery of real-world tasks, scores the outputs against explicit criteria and measures performance over time. Think of it like a standardized professional licensing exam for your AI: Instead of guessing whether a model is ready, an eval systematically tests how it answers hundreds of representative questions, handles edge cases or calls internal software tools.
An eval is fundamentally a statistical tool for a non-deterministic world that works by exposing the agentic system under test to a representative sample of tests and then using automated means to check the responses against pre-written ground-truth answers. The design of an eval (described below) is deceptively simple, and the quality depends almost entirely on the care put in gathering a representative sample and manually writing golden responses.
In business terms, an eval serves as your operational proxy for business value. It bridges the gap between unpredictable model intuition and predictable enterprise outcomes, translating subjective goals like “helpful support” or “accurate financial reporting” into verifiable metrics your team can engineer against.
How To Build An Enterprise Eval Suite
While measuring non-deterministic agents may seem complex, building an effective enterprise eval framework comes down to four foundational components:
1. A Representative Dataset: Gather 500 to 1,000 authentic examples from historical operations (such as real customer inquiries or actual past deliverables) rather than synthetic prompts.
2. Curated Standards and Rubrics: Establish vetted “golden responses.” These are multi-pass, expert-reviewed benchmarks that reflect your standards for accuracy, tone and compliance, paired with clear rubrics that define acceptable output.
3. A Scalable Scoring Mechanism: While human evaluators provide high nuance, they are too slow and expensive for continuous deployment. The modern standard is LLM-as-a-judge: using an advanced frontier model programmed with your rubrics to evaluate candidate outputs against golden standards at scale, calibrated periodically by human reviewers.
4. An Aggregate Metric: Consolidate evaluation scores into an executive composite number (such as an overall accuracy rate or weighted rubric index) to guide product decisions.
From Measurement To Strategic Advantage
Consider a customer service deployment. When you extract 1,000 authentic customer dialogues, define verified standards and package the flow into an automated harness, your operational posture transforms. Instead of spending weeks manually reviewing sample chats, your team can benchmark an updated prompt, tool integration or model version across all 1,000 scenarios in minutes. You gain concrete statistical confidence that your system matches or even surpasses human baseline performance before a customer ever sees it.
Crucially, an established eval harness unlocks a disciplined strategy for selecting models. Rather than running every workflow on an expensive frontier model, you can use the strongest model to set your baseline score. Once that benchmark is secured, you can methodically swap out routine, low-reasoning subtasks for smaller, cheaper specialized models or even deterministic code, verifying at each step that your eval score does not regress. This drives down latency and operational costs without sacrificing quality.
Build Evals First
My core rule for enterprise AI is simple: Build your evals first.
Before your team writes a single line of agent orchestration or application code, insist on defining the evaluation dataset and scoring rubric. If a team struggles to articulate how an eval will measure success, it is a glaring signal that the business requirements are not yet mature enough for implementation. Objective, quantitative measurement of AI performance is going to be a critical differentiating factor between organizations that succeed in unlocking efficiencies and capabilities through AI, and those who struggle.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
