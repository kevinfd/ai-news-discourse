---
id: "b9aecad1fb27c9a9"
title: "OpenAI’s COBOL migration score has made a striking leap"
url: "https://thenewstack.io/penai-cobol-migration-benchmark"
link: "https://thenewstack.io/penai-cobol-migration-benchmark"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T15:34:58Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Meredith Shubel"]
language: "en"
summary: "This week, OpenAI put COBOL in the spotlight. It announced benchmark results suggesting its latest models are getting much better at migrating COBOL programs and building software in languages with less code and documentation for models to learn from. \n\n On OpenAI’s own COBOL migration test, GPT-6.1 Sol reached 86.6% accuracy at low reasoning effort, up from GPT-5.6 Sol’s 5.4%, while costing 39%…"
tags: ["AI Engineering", "Software Development", "Software Testing"]
orgs: ["OpenAI", "Anthropic", "Amazon", "IBM"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 681
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI’s COBOL migration score has made a striking leap

The New Stack · Meredith Shubel · 2026-10-22

OpenAI’s COBOL migration score has made a striking leap
This week, OpenAI put COBOL in the spotlight. It announced benchmark results suggesting its latest models are getting much better at migrating COBOL programs and building software in languages with less code and documentation for models to learn from.
On OpenAI’s own COBOL migration test, GPT-6.1 Sol reached 86.6% accuracy at low reasoning effort, up from GPT-5.6 Sol’s 5.4%, while costing 39% less. At higher reasoning effort, the newer model reached 97.9%.
But the evidence behind the two evaluations is uneven.
OpenAI has not published the details of its evaluation of COBOL (“Common Business-Oriented Language”; the programming language that AI coding tools may help maintain or migrate). It has released the MultiLangBench setup and test suite on GitHub. That benchmark tests whether models can build a SQLite-compatible database engine from scratch across 20 programming languages.
OpenAI’s announcement calls the results “substantial improvements across both evaluations, delivering much higher accuracy at lower cost.”
Those results could matter to teams maintaining and modernizing legacy software. But without public COBOL test cases, developers cannot independently inspect that evaluation.
Is there finally some hope for modernizing COBOL?
Per OpenAI, its new COBOL migration evaluation “tests whether a model can migrate existing programs to another language while preserving their behavior.” Specifically, it’s testing migrations from COBOL to C++, Java, Kotlin, Python, and Rust.
To succeed, each migration must pass a series of hidden tests that require “byte-for-byte parity on observable outputs.” And with markedly greater accuracy than its predecessor, GPT-6.1 Sol is, indeed, showing substantial progress.
The measured gains are striking, though OpenAI is not the first company to bring AI to COBOL modernization.
Even though COBOL underpins much of the world’s financial transactions and business records — IBM reports COBOL underpins over 40% of all online banking systems, supports 80% of in-person credit card transactions, and handles 95% of all ATM transactions — it remains a difficult target for AI coding tools.
Compared with Python and JavaScript, models have less COBOL code and documentation to learn from. Experienced COBOL developers can also be hard to find, and documentation often lags behind the systems they maintain.
AI coding gains across 20 languages
Alongside its COBOL migration tests, OpenAI developed a second evaluation to measure models’ ability to build software from scratch, MultiLangBench. This benchmark “tests whether a model can build a SQLite-compatible database engine across 20 different programming languages.”
First, the program gets a database and SQL query. Then, it produces a modified database. The reference SQLite implementation serves as the ground truth to check if the resulting database contains the expected data.
On average, GPT-6 Astra — OpenAI’s flagship model — achieved an 87.4% test pass rate across 20 programming languages, a hefty jump from GPT-5.6 Sol’s modest 26.8%. It scored above 83% on 19 out of 20 languages and made improvements on all of them.
GPT-6 Luna, predictably, didn’t do as well as Astra, with the lower-cost option only achieving an average pass rate of 40.3%. That said, it did manage to outperform GPT-5.6 Sol on every language tested, with an approximate 78% lower estimated API cost.
All right, then. Keep your secrets.
OpenAI reports promising results from its COBOL migration evaluation and MultiLangBench, but benchmarks don’t tell the whole story. As of Thursday, Real-SWE 1.1, which uses private codebases, lists Claude Opus 5.5 in first place at 56.8% resolution. An earlier Real-SWE run covered by The New Stack had a different leader and lower scores.
Plus, developers still can’t inspect OpenAI’s COBOL migration benchmark. The announcement credits feedback from developers and enterprise customers for guiding the work, but without the underlying tests and dataset, outsiders can’t independently check the results.
OpenAI acknowledges a key limitation, noting that “applying it to production software still requires expert review and testing against the system’s business rules and dependencies.”
OpenAI is entering a field others have been working on for some time. Anthropic outlined how Claude Code could assist COBOL modernization on February 23. As The New Stack reported, AWS introduced AI agents for mainframe migrations in 2024.
