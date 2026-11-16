---
id: "7afedf3465a158df"
title: "Meet Meta’s JiTTests: LLM-Generated Tests Designed to Fail Before Risky Code Lands"
url: "https://marktechpost.com/2026/11/16/meta-jittests-llm-catching-tests-privacy-bugs"
link: "https://marktechpost.com/2026/11/16/meta-jittests-llm-catching-tests-privacy-bugs"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T10:39:41Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Meta has moved Catching Just-in-Time Tests (JiTTests) from research prototype into its production infrastructure . Meta JiTTests is an LLM-based system that writes executable tests designed to fail on a risky code change. A failing test is concrete evidence that a diff changed behavior. Meta team reports that JiTTests caught 74 privacy SEVs at the diff stage in the first half of 2026. The method…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "Machine Learning", "Security", "Software Engineering"]
orgs: ["Meta", "Anthropic", "Google"]
topics: ["models & research", "agents & coding"]
content_source: "summary"
word_count: 1037
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Meta’s JiTTests: LLM-Generated Tests Designed to Fail Before Risky Code Lands

MarkTechPost · Michal Sutter · 2026-11-16

Meta has moved Catching Just-in-Time Tests (JiTTests) from research prototype into its production infrastructure . Meta JiTTests is an LLM-based system that writes executable tests designed to fail on a risky code change. A failing test is concrete evidence that a diff changed behavior. Meta team reports that JiTTests caught 74 privacy SEVs at the diff stage in the first half of 2026. The method is described in the FSE 2026 research paper ‘Just-in-Time Catching Test Generation at Meta ‘. 

 TL;DR 

 Scale: Runs on Meta backend code with hundreds of millions of lines. The research paper analyzes 22,126 generated tests. 

 Runs on: Meta’s internal infrastructure, overnight on spare capacity. Judge models in the paper: Llama3.3-70B, Gemini 3 Pro, Claude Sonnet 4. Not publicly available. 

 Performance: Engineers report a 60% true-positive rate at full scale (self-reported). 

 Best: 74 privacy SEVs caught before landing in H1 2026; privacy SEV occurrence down 20%. 

 Worst: The initial deployment confirmed only 8 of 41 reported catches (19.5%). 

 Bottom line: Best: executable proof of a bug before merge. Worst: internal only, with self-reported numbers. 

 What are Catching JiTTests? 

 Catching JiTTests are LLM-generated tests that should fail when a diff introduces a bug. Traditional hardening tests pass when written and guard against future regressions. Catching tests target the change under review, before it lands. Meta formalized the details in its 2025 paper ‘Harden and Catch’ . 

 Most AI bug tools act like faster human reviewers. They read the diff and leave comments. JiTTests instead execute code and show a concrete behavioral difference. Meta team concedes this takes more computational steps. It argues the approach catches bug classes that LLM or agent review can miss. 

 How does the JiTTests pipeline work? 

 The production pipeline has 5 stages: 

 Targeting: Runs overnight on spare capacity. It selects the previous day’s risky diffs, using a mechanism similar to Meta’s Diff Risk Score. 

 Test generation: 2 diff-aware workflows produce candidate tests (explained below). 

 LLM-as-Judge ensemble: Several LLMs score each failing test using the test code, failure trace, diff and inferred intent. 

 RubFake: The Rule-Based False-Positive Killing Environment adds deterministic checks. Its rules flag patterns like reflection, broken mocks and not-implemented exceptions. 

 Human-on-the-loop: The system decides whether to contact an engineer, based on the combined ranking. 

 Dodgy diff vs intent-aware: what is the difference? 

 The dodgy diff workflow assumes every diff is buggy. It treats the diff as a mutant of its parent and generates tests that tell them apart. 

 The intent-aware workflow first infers what the diff should do from its code, title and summary. It lists risks, builds a mutant for each, and writes tests to kill them. Tests that then fail on the real diff become ‘weak catches.’ 

 What do the benchmarks show? 

 The research team analyzes 22,126 generated tests. Diff-aware methods produced 4x more candidate catches than hardening tests. They produced 20x more than tests that failed by coincidence. 

 The intent-aware workflow produced weak catches in 6.4% of its tests and on 7.9% of diffs. Dodgy diff scored 2.5% and 4.0%. Meta’s earlier ACH mutation-guided hardening scored 0.8% and 1.6%. The rule-based and LLM assessors cut human review load by 70%. 

 &&&

 Feature Catching JiTTests, intent-aware Catching JiTTests, dodgy diff ACH mutation-guided TestGen-LLM Org / first published Meta, 2026 Meta, 2026 Meta, 2025 Meta, FSE 2024 Goal Catch bugs in the diff under review Catch bugs in the diff under review Harden code against specific fault classes Improve existing human-written tests Generated test should Fail on a buggy diff Fail on a buggy diff Pass when generated Pass when generated Aware of the diff Yes, infers intent and risks Yes, intent-unaware No No Weak catches per test* 6.4% (52 of 811) 2.5% (41 of 1,621) 0.8% (6 of 754) 2.0% (89 of 4,499) Diffs with a weak catch* 7.9% 4.0% 1.6% 3.6% False-positive filter LLM judge ensemble + RubFake rules LLM judge ensemble + RubFake rules Not disclosed Build, pass and coverage filters Public availability Internal only Internal only Internal only Internal only 

 *Figures from Table 1 of the JiTTests paper (self-reported, Meta codebase). TestGen-LLM row uses the “need not add coverage” setting. A weak catch is a candidate failure, not a confirmed bug. 

 What changed at full scale? 

 The initial deployment was modest. Meta reported 41 candidate catches to engineers. 8 were confirmed true positives, a 19.5% rate. 4 of those would have caused serious failures in production. 

 The October 2026 engineering post reports much stronger production numbers: 

 589 engineers engaged with JiTTests, 64% of those contacted. 

 Engineers reported a 60% true-positive rate. 

 74 privacy SEVs were caught at the diff stage in the first half of 2026. 

 Overall privacy SEV occurrence fell 20% in the same period. 

 What does human-on-the-loop mean? 

 Human-in-the-loop means a person reviews every output. Human-on-the-loop means engineers set criteria and monitor results in aggregate. They intervene at the policy level, not on each test. Meta team rarely need to read test code. They only confirm whether an observed behavior change was intended. 

 Can developers use JiTTests? 

 The answer is No. JiTTests is internal Meta infrastructure. Meta has not released code, models or an API. Teams can still copy the pattern: diff-aware mutation-guided test generation, an LLM judge ensemble, deterministic filters and aggregate human oversight. 

 Key Takeaways 

 Meta’s JiTTests writes LLM tests meant to fail on buggy diffs. 

 74 privacy SEVs caught pre-merge in H1 2026; privacy SEVs down 20%. 

 Engineers report a 60% true-positive rate, up from 19.5% in the paper. 

 Intent-aware tests hit weak catches at 6.4%, vs 0.8% for ACH hardening. 

 Internal only: no code, model or API released. 

 Check out the engineering post , the FSE 2026 paper and Meta’s announcement on X . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meet Meta’s JiTTests: LLM-Generated Tests Designed to Fail Before Risky Code Lands appeared first on MarkTechPost .
