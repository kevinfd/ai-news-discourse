---
id: "219132d2427ef463"
title: "AI-Generated Insurance Fraud Is Getting Better, And No Single Test Will Catch It"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/16/ai-generated-insurance-fraud-is-getting-better-and-no-single-test-will-catch-it"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/16/ai-generated-insurance-fraud-is-getting-better-and-no-single-test-will-catch-it"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-16T11:45:00Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Marcin Nowak, Forbes Councils Member"]
language: "en"
summary: "Insurers have entered an arms race, and the first step is admitting it. The second is accepting that no single tool will win it for them."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: []
topics: ["models & research", "policy & regulation", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 991
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6af604eda3c8f3090129fcdc/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# AI-Generated Insurance Fraud Is Getting Better, And No Single Test Will Catch It

Forbes · Marcin Nowak, Forbes Councils Member · 2026-11-16

Marcin Nowak, board member at Decerto, has 20+ years in insurance, focusing on automation, technology impact and software solutions.
A few years ago, faking a car accident photo required real skill with editing software. Today, it takes a free app and a one-sentence prompt, and the results improve with every model release.
U.K. insurer Aviva detected a record £233 million in suspected claims fraud in 2025 and said a growing number of claims now arrive with AI-generated images and manipulated documents. In the U.S., a 2022 report from the Coalition Against Insurance Fraud estimated that insurance fraud was costing $308.6 billion a year.
Insurers have entered an arms race, and the first step is admitting it. The second is accepting that no single tool will win it for them. Most insurers respond by shopping for a deepfake detector, but that’s the least important part of the fix. What decides the outcome is what happens after a claim gets flagged.
The obvious check is the easy part.
When claims leaders first hear about AI-generated fraud, the natural reaction is to look for a detector: a model that looks at a photo and says “generated” or “genuine.” Such tools exist, and they’re worth using.
It’s also a moving target. A detector learns the traces that current generators leave behind. However, every new generator removes some of those traces, and the detector has to catch up again. It will, but there’s always a gap.
We have a public test page that allows users to upload a claim-style photo and see which areas a detector flags as edited. A good detector will often provide an honest answer of “inconclusive,” and an inconclusive answer gives you no verdict on the claim. The detector is one input among many.
Fraud shows up as small anomalies.
In my experience working with carriers on claims automation, a fraudulent claim rarely contains one smoking gun. It contains several small things that don’t quite fit. The photo metadata says one date, while the loss report says another. The repair invoice comes from a shop that was registered last month. The damaged laptop looks a lot like the one in a claim filed elsewhere a year ago. The policy was increased three weeks before the loss.
Notice that only one of these signals lives inside the image, and as generators improve, it’s the one to trust least. A policy history, a repair shop’s registration date and your own claims archive can’t be produced with a prompt.
None of these signals proves anything on its own. People mistype dates, phones reset their clocks and honest customers buy coverage right before a move. If you treat each anomaly as fraud, you’ll accuse honest customers on a regular basis.
The approach I suggest is to collect these weak signals from every source you have—the documents, the images, the policy history and external registries—and to look at them together. One anomaly is noise. Five anomalies on one claim are a pattern worth an investigator’s time.
You can also train models on your own claims data to find unusual combinations of amounts, timing, parties and repair shops that no single rule describes. However, a model learns only from the outcomes you give it.
Every false positive is a customer waiting.
In my experience, the step carriers skip most often comes after the investigation. When an investigator concludes that a flagged claim was legitimate, that outcome has to flow back into the system. Which signals fired? Why did they fire? Should a threshold move, or should one check carry less weight for a given line of business?
If cleared claims never come back labeled “not fraud,” the model keeps learning from suspicions instead of verified outcomes, and it keeps flagging the same honest patterns with growing confidence.
Without that loop, a fraud program drifts in one of two directions. Either it floods investigators with false positives, and they start ignoring the flags, or it’s tuned so loosely that real fraud passes through. Both failures are quiet. Neither shows up in a dashboard unless you look for it.
The first failure has a cost that most fraud reports leave out. Every honest claim held for investigation is a customer waiting for a payment, an adjuster’s hours spent on the wrong file and a decision someone may later have to explain.
That’s why I’d recommend auditing your fraud rules on a fixed schedule, the same way you would audit a pricing model. Track how many flagged claims turned out to be fraud, how many were honest and how many confirmed fraud cases were never flagged at all.
Regulators expect this discipline, too. The December 2023 “NAIC Model Bulletin: Use of Artificial Intelligence Systems by Insurers”—adopted in 25 jurisdictions as of April 2026—asks insurers to govern and monitor AI systems that affect consumers, and it names fraud detection among the uses it covers. In my reading, a fraud model that wrongly flags honest claimants is exactly such a system.
This is a process, not a project.
Fraud detection can be automated, and it should be, but automation doesn’t mean “set and forget.” Fraudsters change tactics in weeks, and generators improve every few months.
The people closest to fraud—your investigators and claims handlers—need to be able to adjust rules and weights themselves instead of waiting for an IT release. The final decision on a suspicious claim should stay with a person, with the system showing which signals led to the flag, and the budget should treat fraud detection as an ongoing operation with time reserved for tuning rather than as a one-time implementation.
Here’s the question worth asking in your next leadership meeting: When your fraud team last cleared a flagged claim as legitimate, what changed in your system as a result? If the answer is “nothing,” your automation isn’t learning, and the fraudsters are.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
