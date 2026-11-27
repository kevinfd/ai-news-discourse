---
id: "3634f2e6ee560a58"
title: "Preprint Says AI Model Rewrote Own Weights"
url: "https://riotimesonline.com/ai-model-rewrites-own-weights-preprint-study"
link: "https://riotimesonline.com/ai-model-rewrites-own-weights-preprint-study"
source: "The Rio Times"
domain: "riotimesonline.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-26T07:00:00Z"
published_date: "2026-11-26"
collected_at: "2026-11-27T13:04:05Z"
authors: ["Lachlan Williams", "Matthias Camenzind"]
language: "en"
summary: "A US preprint says an open AI model rewrote its own weights and gained up to 6.6 points on maths tests. It is unreviewed, and oversight questions remain."
tags: []
orgs: ["OpenAI", "Google", "Alibaba", "UK"]
topics: ["models & research", "business & funding", "agents & coding", "safety & ethics"]
content_source: "fulltext"
word_count: 1255
paywalled: false
image: "http://www.bing.com/th?id=ONUT.1G22qMRNpPdA7b8c3mdiGQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Preprint Says AI Model Rewrote Own Weights

The Rio Times · Lachlan Williams, Matthias Camenzind · 2026-11-26

Preprint Says AI Model Rewrote Own Weights
The authors call it a step toward AI that improves itself, yet their own paper asks for a person to approve every self-made model. The evidence so far is one model family and maths tests.
Technology: Artificial Intelligence
Researchers at the University of Illinois Urbana-Champaign and five other US universities say a freely downloadable AI model rewrote its own weights, the numbers that store what it learned. The preprint, a paper posted to the arXiv server before peer review, appeared on Monday 16 November 2026, and we found no independent replication.
The authors call this a first, which is their claim, not a settled fact. For firms that run AI agents, the open question is who checks a model that changes itself.
Key Facts
- Who. Jiajun Fan, Ge Liu and nine co-authors from six US universities, including Illinois Urbana-Champaign.
- What. A model with 27 billion weights rewrote some of them, without training; best gain 6.6 points.
- Status. Preprint posted on arXiv on 16 November 2026; not peer reviewed, no independent replication found.
- Limits. One model family and maths tasks; the three smaller versions made no edit or broke themselves.
- As of. Thursday 26 November 2026, 15:00 GMT
The authors call it a step toward AI that improves itself, yet their own paper asks for a person to approve every self-made model. The evidence so far is one model family and maths tests.
The computing pioneer Alan Turing said in 1947 that a machine altering its own instructions is a mechanism for learning, “but this of course does not get us very far.” The authors’ project page carries the full quote, from a lecture he gave to the London Mathematical Society, a UK maths body, on 20 February 1947. Earlier systems rewrote their own code, like the Darwin Gödel Machine from researchers Jenny Zhang, Jeff Clune and colleagues (arXiv, 29 May 2025).
Others, like SEAL by Adam Zweiger and colleagues (arXiv, 12 June 2025), have a model write its own training data and then train on it. The closest precedent is a blog post by Rikiya Takehi, Omar Khattab and colleagues at MIT CSAIL, the university’s computer-science research lab, published on 2 November 2026.
There, a large AI model called GPT-6 Astra edited 0.016% of a small model’s weights and lifted its score on MATH-500, a 500-problem maths test, from 7.9% to 48.1%. The Illinois authors write that “the wall between training and inference is a limit of our tools, not a property of intelligence.” Their result shows that a mid-sized open model can run such a loop on one graphics chip in a few hours, and larger systems were not tested.
Two Gains in Eight Reported Sessions
In each session the model received its own weights, graded answers on practice maths problems from a pool of 3,000, and a Python workspace with training tools switched off. It could run itself up to 20 times to test an edit, had no internet access, and then submitted or withdrew the edit (paper, Sections 2 and 3.1).
In the authors’ second protocol, eight reported sessions produced three submitted edits and five withdrawals, and two earlier sessions submitted nothing. The best edit lifted accuracy by 6.6 points, from 57.2% to 63.8%, on 490 held-out problems the model never saw, each answered eight times (paper, Table 13).
Another edit gained 4.0 points, while the first session’s edit (0.5 points) was not significant by the authors’ test. The authors say the model in use only gets better, but each session starts from the original weights, so each gain is measured against the original, not stacked.
In the authors’ first protocol, with no outside check before submission, the edit lifted accuracy by 1.1 points, from 57.2% to 58.3%, on the same problems. That gain passes their significance test, with a p-value of 0.038 (lower means luck is a less likely explanation), but it is small.
The second task damaged a copy of the model by overwriting part of one of its 64 processing layers with random noise until the copy solved almost nothing. Told only that some values were corrupted, the model found the faulty block of numbers and wrote new values, and the authors say it never opened the original weights.
The repair was found on text maths problems alone. Yet on six image benchmarks of 100 problems each, the repaired copy recovered 83% of the original model’s accuracy (paper, Table 12).
The smaller models did not manage this. In Alibaba’s Qwen3.5 family, the 2-billion-weight version made no edit, and the 4- and 9-billion versions broke themselves with random changes (paper, Figure 2).
The gains are measured on maths and image-maths problems in one model family, so they say little about everyday business tasks. The MIT group saw a similar limit: Astra cured endless repetition in one small model but could not improve Google’s tiny Gemma 3 270M, which rarely repeats itself.
Who Approves a Model That Edits Itself?
The authors’ own answer is human sign-off: they say the path to recursive self-improvement, a model upgrading itself again and again, “should be taken with people in the loop.” Every model a model makes of itself should be, in their words, “evaluated, for safety as well as for the task, and confirmed by a person before it is used.”Yet the paper measures accuracy and whether answers finish, and the word “safety” appears once, in its conclusion.
The edits are code the model wrote, which the authors say can be read and undone “like a commit” (a tracked software change), in a sandbox with no internet. For a company that runs AI agents, that commit comparison is the practical point: a self-edited model is no longer the version that passed review.
Cielo, a Brazilian payments processor that says AI agents prepare its features (our 18 November report), is a firm this could reach; nothing links it to this research. The paper and project page we read give no date for peer review.
Until outside groups repeat the experiment, the claim of a first rests on the results of one team.
More: Latin America news in English, every day from The Rio Times.
Frequently Asked Questions
Did an AI really train itself?
Not in the usual sense. The model edited its own weights through reasoning and code, without the retraining by repeated small numerical updates used to build models, and a human-built framework tested each edit.
Does this mean AI will improve itself without limits?
No. The study covers one model family and maths tasks, and its authors call for a person to confirm every self-made model before use.
What should companies that run AI agents take from it?
The study describes no deployed agent. It is an early signal that tracking changes to a model’s weights could become part of oversight.
Sources
Published Thursday 26 November 2026 · Fan et al., “Language Models Can Rewrite Their Own Weights”, arXiv 2611.21885 (16 November 2026) · authors’ project page · Takehi, Teoh, Zhang and Khattab, MIT CSAIL (2 November 2026) · Zweiger et al., arXiv 2506.10943 (12 June 2025) · Zhang et al., arXiv 2505.22954 (29 May 2025)
This article was produced by The Rio Times’ automated AI newsroom. Editorial responsibility: Matthias Camenzind, Publisher and Editor-in-Chief. The Rio Times also runs Ask Rio Times, which answers from 100,000+ of our own articles, the daily Latin America Power Map, and prediction-market odds on elections and markets.. How we use AI · Report an error
