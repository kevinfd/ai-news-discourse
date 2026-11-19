---
id: "99c1b0f4830411b8"
title: "Jagged Intelligence: Why AI Is Brilliant One Minute and Clueless the Next"
url: "https://kdnuggets.com/jagged-intelligence-why-ai-is-brilliant-one-minute-and-clueless-the-next"
link: "https://kdnuggets.com/jagged-intelligence-why-ai-is-brilliant-one-minute-and-clueless-the-next"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-18T15:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Nate Rosidi"]
language: "en"
summary: "Why models ace Olympiad math and still fumble simple everyday tasks."
tags: []
orgs: ["OpenAI", "Apple", "Google", "Tesla"]
topics: ["models & research", "jobs & society", "health & science"]
content_source: "fulltext"
word_count: 1960
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/Rosidi-Jagged-Intelligence-Why-AI-Is-Brilliant-1.png"
discussion_url: null
score: null
comments: null
community: null
---

# Jagged Intelligence: Why AI Is Brilliant One Minute and Clueless the Next

KDnuggets · Nate Rosidi · 2026-11-18

Jagged Intelligence: Why AI Is Brilliant One Minute and Clueless the Next
Why models ace Olympiad math and still fumble simple everyday tasks.
AI systems from Google and OpenAI solved five of six problems at the International Mathematical Olympiad. Months later, chatbots told a user to walk his car to a repair shop 50 meters away. A person who can do the first would never make the second mistake, which is why the gap is so hard to anticipate.
Researchers call this pattern jagged intelligence. It matters to anyone who evaluates models, builds AI features, or decides whether to trust an output, because one benchmark score or one impressive demo says little about the next task.
What Jagged Intelligence Means
Andrej Karpathy, an OpenAI co-founder and former head of AI at Tesla, coined the term in July 2024. Models do some things extremely well and fail badly at others, and it is hard to tell in advance which is which.
Human abilities tend to be correlated and improve together from childhood to adulthood. Someone who solves Olympiad problems will not be confused by a 50-meter walk. In models, capabilities often don't move together.
People use one demonstrated skill to guess at others. A model that writes a working function looks like it can also count the words in a paragraph. That inference fails, which is why a demo predicts so little.
Some researchers frame the pattern as many separate skills with no general intelligence behind them.
Four Proposed Explanations for the Pattern
None is settled, and they may overlap.
Verifiable Rewards
Reinforcement learning with verifiable rewards (RLVR) became a major training stage in 2025.
It works where answers are clearly right or wrong, such as math and code that passes tests.
Karpathy argues that models spike near verifiable domains. Creative writing, philosophy, and parts of science have no automatic checker, so in this account progress is slower.
Data Coverage
The internet holds only a fraction of human knowledge and very little about the physical world. A model trained on digital patterns struggles with planning, new ideas, and unseen tasks.
Pattern Replication
The authors of Apple's GSM-Symbolic paper hypothesize that large language models (LLMs) replicate reasoning steps from training data instead of reasoning logically. A problem that matches a familiar template gets solved, and a small change to the template breaks the chain.
Incoherent Concepts
A separate "Potemkin understanding" paper from MIT, Harvard, and the University of Chicago traces failures to internally incoherent concept representations. A model can hold a correct definition and a faulty working version of the same concept, and nothing forces the two to agree.
Verifiable rewards may explain why models excel at certain tasks, while the other three theories offer possible explanations for their weaknesses.
For example, difficulties with clock-related tasks (e.g. reading the time from an analog clock image) might reflect gaps in training data. Failures caused by adding irrelevant information to a problem could suggest that models rely on familiar patterns rather than logical reasoning.
And cases where a model correctly defines a concept but fails to apply it could indicate inconsistent internal representations. These connections are plausible, but none has been established as a direct causal explanation.
Six Failures Documented by the Scientific Community
We use "jagged" broadly here: unevenness across tasks, across difficulty levels, and between test conditions and real use.
A Distractor Clause Breaks Grade-School Math
In Apple's GSM-NoOp test, researchers added an irrelevant sentence to grade-school word problems, such as "five of the kiwis were smaller than average." Models subtracted those kiwis from the total. One extra clause that looked relevant cut performance by up to 65% across state-of-the-art models. A student would read the sentence and ignore it.
Defining a Concept Versus Applying It
GPT-4o correctly defined an ABAB rhyme scheme, then wrote a poem that used a word that didn't rhyme. The Potemkin study tested seven models on concepts from poetry, game theory, and psychology. Models defined the concepts correctly about 94% of the time and failed classification tasks on the same concepts about 55% of the time.
If a model can recite a definition and still misapply it, a correct definition tells us little about understanding.
Reading an Analog Clock
On ClockBench (September 2025), humans read analog clocks with 89.1% accuracy. The best model then, Gemini 2.5 Pro, reached 13.3%.
Reading a clock means finding the hands, judging their angles, and mapping them to numbers. When a model read the time correctly, follow-up arithmetic was fine, so perception failed and the math held. ClockBench is a single-author benchmark and has not been peer reviewed, so we read the numbers as indicative.
Strong Medical Scores, Poor Results for Real Users
In a Nature Medicine trial from Oxford, 1,298 participants tried to identify medical conditions. LLMs alone identified them in 94.9% of cases.
People using the same LLMs identified them in at most 34.5% of cases, below the 47% of a control group that did its own research. On choosing the right next step, LLM users did no better than that control group.
The valley here sits in the model and user together, and we count it because any product built on the model inherits it. A model's solo score and its value to a real user can sit this far apart, and standard benchmarks did not show it.
Logic Puzzles and a Contested Result
Apple's Illusion of Thinking study tested Tower of Hanoi, River Crossing, and Blocks World at rising difficulty. Standard models beat reasoning models on easy puzzles, reasoning models won at medium difficulty, and both collapsed on hard ones, even when given the solution algorithm.
Which model was better changed with difficulty, so the unevenness showed up inside a single task family. A rebuttal argued that part of the collapse comes from the test setup, so we treat this result as open.
A New Benchmark Version Drops Scores Below 1%
ARC-AGI-3 is a benchmark launched on March 25, 2026, designed to evaluate how well artificial intelligence can learn, reason, and adapt to completely unfamiliar situations, rather than simply answer questions based on previously learned patterns.
Every frontier model scored below 1%, while humans solved all of its environments.
Gemini 3.1 Pro had already reached 77.1% on ARC-AGI-2, so a high score on one version did not carry over to the next.
The new version also switched to interactive environments, so the drop mixes format and difficulty. Scores are moving quickly, so check the current leaderboard before quoting a number.
Why One Benchmark Score Misleads
Karpathy has said he lost trust in benchmarks in 2025. Benchmarks are verifiable environments by construction, which is where RLVR works, so labs can train directly on tasks like them. The score can rise without general ability rising with it.
Benchmarks also assume that a few correct answers signal understanding, because human errors follow predictable patterns. A student who defines an ABAB rhyme scheme correctly will almost always apply it correctly, so an exam can sample a few questions and infer the rest. The Potemkin authors argue that a model's misunderstandings don't follow those patterns, so it can pass the test without understanding the concept.
Benchmarks such as GSM8K are vulnerable to contamination and don't measure sensitivity to small changes in wording. In the Oxford study, neither standard medical benchmarks nor simulated patients predicted what happened with real users. The authors recommend systematic human user testing before deployment.
Interview Question: A 3% Gain That Hides a Regression
This OpenAI question asks: "A new model version improves your primary metric by 3% overall but regresses performance for a specific user segment. How do you decide whether to ship it?"
This has the same shape as jaggedness at the product level: the average goes up and a valley opens for one group of users. It matches the model-capability version only if the regression traces to a skill the new model lost. A dashboard that tracks only the primary metric would report the 3%.
Example: if 90% of users improve by 4.4% and the other 10% drop by 10%, the average weighted by user share still rises by about 3%. The headline number never shows the 10%.
The official answer covers five points:
- Size and value the affected segment before deciding anything.
- Find the root cause of the gap.
- Consider a targeted fallback that routes that segment to the old model.
- Treat segments with fairness or legal stakes as a judgment call.
- Document the accepted regression so the next release is compared against it.
Each point assumes the aggregate number can't be trusted on its own.
Using AI Reliably in Real Applications
Users struggle to know what AI does well, and the answer changes each release. The emerging view works at the level of tasks: some tasks inside a job get automated and others don't. Scale AI's Remote Labor Index found that the best agents fully automated 2.5% of real freelance projects at launch, mostly creative audio and image work plus some data and writing tasks. Scale's leaderboard now shows 20.8% for the top model (October 7, 2026).
Five practices follow from the evidence:
Testing on Your Own Perturbed and Adversarial Cases
Take a real input, then add an irrelevant detail or reword it. An answer that changes when the correct answer shouldn't is a failure. This is the GSM-NoOp test applied to your own data.
Testing Application, Not Recall
A model that states a rule correctly can still misapply it. Ask it to classify new inputs or generate examples that follow the rule, and score those answers.
Reporting Results by Segment
One overall accuracy figure is how a regression hides, as in the 3% question above. Once a weak segment is known, route its requests to the previous model version and review that rule at each release.
Verifying by Hand Where No Automatic Check Exists
These are the domains RLVR can't train on. Oxford participants did worse with the LLM than the LLM did alone, so test the full workflow with real users and don't assume people will catch the errors.
Re-Evaluating After Every Model Update
The jagged edges move between releases, so last quarter's test results describe last quarter's model.
This OpenAI question asks how to build an evaluation set that catches regressions before each release.
The official answer builds the set from real production failures, separates blocking cases from tracked hard ones, and retires solved cases as new ones arrive. It also warns that a static set gets implicitly tuned against, which is the benchmark problem from earlier applied to your own tests.
Conclusion
Jagged intelligence means AI capability is uneven: Olympiad-level math sits next to a failed clock reading. Verifiable training rewards, thin data on the physical world, pattern replication, and incoherent concepts are four proposed explanations, and none is settled.
Distractor clauses, misapplied definitions, clock faces, and real users all exposed weaknesses that a headline score never showed.
For evaluation, that means perturbed tests, application-level checks, segment-level reporting, and testing with real users. For deployment, it means automating individual tasks, checking by hand where outputs are hard to verify, and testing again whenever the model changes. A score describes the tasks the test covered, and a slightly different input can land in a valley. The peaks are real, and so are the valleys, and only your own tests show where they fall for your use case.
 
Nate Rosidi is a data scientist and in product strategy. He's also an adjunct professor teaching analytics, and is the founder of StrataScratch, a platform helping data scientists prepare for their interviews with real interview questions from top companies. Nate writes on the latest trends in the career market, gives interview advice, shares data science projects, and covers everything SQL.
