---
id: "3b8fe720d989fd3e"
title: "First Match Wins Is Paid Guesswork, Here's What Real Data Quality Actually Requires"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/30/first-match-wins-is-paid-guesswork-heres-what-real-data-quality-actually-requires"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/30/first-match-wins-is-paid-guesswork-heres-what-real-data-quality-actually-requires"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-30T11:00:00Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Filip Popovic, Forbes Councils Member"]
language: "en"
summary: "An AI agent can act on whatever context it receives without the human sanity check that historically caught ambiguity before execution."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["agents & coding", "models & research", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 1002
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ae383b338a3fc440f27816c/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# First Match Wins Is Paid Guesswork, Here's What Real Data Quality Actually Requires

Forbes · Filip Popovic, Forbes Councils Member · 2026-10-30

Filip Popovic is CTO at ZoomInfo, leads engineering for its GTM knowledge graph, built on GTM.AI for agentic workflows.
When enterprise engineering teams build AI features, massive resources go toward preventing models from hallucinating answers. But when evaluating the data infrastructure powering autonomous sales and revenue workflows, I’ve found the far more dangerous failure mode is identity hallucination.
Historically, go-to-market (GTM) software depended on an unwritten safety net: the human sanity check. If a database returned a contact match or account mapping that was slightly off, the sales rep or manager recognized the flaw before launching outreach. The human acted as a contextual filter, quietly absorbing data ambiguity.
Agentic workflows, however, can remove that filter entirely. An AI agent can act on whatever context it receives without the human sanity check that historically caught ambiguity before execution. So when an agent trusts an unscored first-match guess, that error compounds down the execution stack. A bad company match leads to the wrong contact, driving incorrect enrichment, flawed personalization and an automated CRM update or sequence delivered to someone who should have never been targeted.
In an agentic GTM stack, accepting an unscored first match is no longer a minor shortcut—it is paid guesswork executing at machine speed.
The Fallacy Of Binary Matching
The core flaw of first-match and match-rate-optimized enrichment architectures is that they collapse identity resolution into a binary answer: this record matches or it doesn’t. But in a living commercial ecosystem where companies reorganize, executives switch roles and digital signals decay, identity is inherently probabilistic. By weighing a broad range of data points to resolve to the right entity, we deliver more accurate outcomes for our customers. Ignoring these signals and falling back on traditional attribute-based matching hard-codes ambiguity directly into your GTM infrastructure.
Real data quality requires treating identity resolution as an accumulation of weighted evidence. Signals carry vastly different diagnostic weight. An exact corporate domain match offers far stronger proof than a similar company name, just as a verified direct email carries more weight than a job title. And sometimes, the explicit absence of a contradictory signal can provide as much clarity as a matching attribute.
Solving identity at scale means evaluating competing hypotheses across candidate entities simultaneously. The challenge lies in determining, across all plausible candidates, how much stronger the evidence is for Company A compared to Company B or C. Infrastructure shouldn’t simply tell an agent “this is Filip Popovic”—it should communicate a confidence estimate backed by the specific signals and sources supporting that conclusion. Without that supporting reasoning chain, a confidence score is just another black box.
Temporal Reasoning And The “I Don’t Know” Threshold
Beyond weighting signals, identity resolution must account for time, because identity in the commercial world is temporal.
Consider job transitions, for example: when an executive leaves Company A for Company B, historical records associate them with their former employer while newer signals point to their new role. A first-match system grabs the first record meeting basic criteria and declares victory. Meanwhile, real data infrastructure applies temporal reasoning, asking not just who an entity is, but precisely when that information was valid. In real-world GTM data, two contradictory facts can both be accurate—they’re just often true at different points in time.
An infrastructure’s willingness to declare uncertainty is equally vital. Traditional vendor evaluations reward platforms that maximize match rates, encouraging systems to force low-confidence records into identities simply to return an answer. The way I see it, delivering “I don’t know” stands among the most critical outputs a trustworthy data system can produce. Just as we train language models not to hallucinate answers, data infrastructure must not hallucinate identity. When evidence falls below a required confidence threshold, leaving a record unresolved is the correct engineering response.
Reconciling Reality Beyond Vendor Plumbing
To solve data quality at scale, many engineering teams assemble waterfall pipelines that query 25 or more vendors. But stringing vendor APIs together in a sequential waterfall is merely plumbing. The real engineering challenge begins after collecting the answers.
Every provider operates on distinct schemas, coverage profiles and freshness cycles. Reconciling competing visions of reality depends on continuously normalizing disparate vendor inputs into a unified GTM data model, scoring source reliability, assessing recency and maintaining complete lineage tracking. When providers disagree, the system must reason over conflicting claims to output a scored, attributed result.
As our infrastructure processes hundreds of millions of entities and billions of daily signals, we treat data as an ecosystem rather than a static repository. Operating at that scale clarifies the real cost of paid guesswork: you aren’t just paying a vendor for a guess; you pay for the cascading operational costs downstream in corrupted CRMs, misallocated territories and broken sales workflows.
Aligning System Confidence With Action Consequence
As AI agents assume greater operational authority across revenue workflows, system confidence must serve as the primary control plane for agent behavior. Confidence thresholds must align directly with the consequences of the action being taken.
If an agent recommends three accounts for a sales rep to review, a lower confidence threshold is acceptable because human oversight remains intact. But when an agent automatically modifies customer CRM data, alters territory assignments or launches an outreach sequence, the required confidence bar must be exceptionally high because autonomy should scale strictly in proportion to verified evidence.
To prepare for an agentic future, technical leaders must re-evaluate how they audit data infrastructure. Instead of evaluating vendors on simple match rates, teams must build evaluation data sets filled with real-world edge cases—job transitions, corporate acquisitions and subsidiary hierarchies—to test system precision across varying confidence thresholds.
When software is granted the authority to execute decisions autonomously, the underlying infrastructure can no longer rely on guesswork. True agentic readiness comes down to architectural rigor: exposing underlying evidence, calibrating autonomy against consequence and distinguishing precisely between what the system knows, what it infers and what it simply does not know.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
