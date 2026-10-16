---
id: "474d893b0dbadede"
title: "Datalab Releases OmniParseBench: An Open OCR Benchmark With 16,288 Pass/Fail Tests to Audit OCR Parsers"
url: "https://marktechpost.com/2026/10/14/datalab-omniparsebench-open-ocr-document-parsing-benchmark"
link: "https://marktechpost.com/2026/10/14/datalab-omniparsebench-open-ocr-document-parsing-benchmark"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T23:37:25Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Datalab has released OmniParseBench , an open OCR benchmark for document parsers. It scores parsers with 16,288 yes/no tests on 2,937 pages from 2,343 documents. The pages span 92 languages. The dataset and code are public. It helps engineers answer a sharper question than a leaderboard does: which parser handles documents like mine? Datalab sells a parser, and its own top setting, Datalab…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Embedding Model", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "New Releases"]
orgs: ["Google", "Anthropic", "OpenAI", "Microsoft", "Mistral"]
topics: ["models & research", "products & launches"]
content_source: "summary"
word_count: 1114
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Datalab Releases OmniParseBench: An Open OCR Benchmark With 16,288 Pass/Fail Tests to Audit OCR Parsers

MarkTechPost · Asif Razzaq · 2026-10-14

Datalab has released OmniParseBench , an open OCR benchmark for document parsers. It scores parsers with 16,288 yes/no tests on 2,937 pages from 2,343 documents. The pages span 92 languages. The dataset and code are public. It helps engineers answer a sharper question than a leaderboard does: which parser handles documents like mine? Datalab sells a parser, and its own top setting, Datalab accurate, ranks second on the launch leaderboard, behind Gemini 3.8 Flash. 

 Is it deployable? Yes. OmniParseBench is an evaluation harness, not a model. It installs with uv pip install omni-parse-bench, needs Python 3.11+, and scores outputs offline with no API keys. 

 TL;DR 

 Size: 16,288 tests, 2,937 pages, 2,343 documents, 22 suites, 92 languages. 

 Runs on: any machine with Python 3.11+. Scoring needs no network. Vendor runs need each vendor’s API key. 

 Performance: the top 3 reported systems sit within 1.3 headline points. 

 Best: Gemini 3.8 Flash leads at 92.9; Datalab accurate follows at 92.7.* 

 Bottom line: every score is a share of pass/fail tests, sliceable by tag. 

 * used in building some tests 

 What is OmniParseBench? 

 OmniParseBench is a document-parsing benchmark from Datalab where every test is a yes/no question about 1 page. A parser’s score is the share of tests it passes. Datalab built it to be clear, auditable and explorable. 

 Why build another OCR benchmark? 

 Datalab names two problems with existing benchmarks. olmOCR-bench showed that pass/fail unit tests work. Datalab now calls it saturated. In its view, top systems are separated by output conventions and overfitting, not reading. Each olmOCR-bench test also sits in 1 bucket, set by its page’s source. A handwritten table gets averaged into whichever bucket its page landed in. 

 ParseBench from LlamaIndex splits parsing into 5 capabilities, each with its own metric. Datalab argues those scores share no unit, so they cannot be compared or combined cleanly. 

 How does OmniParseBench scoring work? 

 The final score is the mean of 3 family scores: text, tables and layout. Five test types feed those families: 

 present: a text, number or equation appears (text) 

 order: text A comes before text B (text) 

 repeat: a line appears exactly N times (text) 

 table_cell: a cell sits under given headings and beside given neighbors (tables) 

 layout_kind: the block holding a line is a heading, text or table (layout) 

 Numbers must match digit for digit, though 1,240 matches 1240. Equations are compared by what KaTeX renders, so \frac{a}{b} equals \dfrac{a}{b}. Each decision is pass, fail, unsupported or error. The last 2 are left out of every score. No model judges the outputs; the scorer is open code . 

 What do tags and derivations add? 

 A test checks one or more args, each of which is the content at one place on the page. Each arg carries tags on 5 axes: structure, rendering, role, script and language. Scripts use ISO 15924 codes; languages use ISO 639-3 codes. Tags never decide a verdict or the headline. They only select tests, so any slice gets its own score. 

 The table tag covers 6,767 tests on 1,000 pages from 875 documents. English covers 10,089 tests. Non-English languages cover 1,931 tests on 529 pages from 321 documents. 

 Every test also records its derivation, meaning how its answer was established. There are 10 derivations . They include publisher JATS XML, the PDF text layer, authored pages, olmOCR-bench tests, model panels and human review. 

&&&

 What are the OmniParseBench launch results? 

 Parser Headline Text Tables Layout Gemini 3.8 Flash* 92.9 91.3 95.2 92.2 Datalab accurate 92.7 90.8 91.8 95.6 Datalab balanced 91.6 90.0 89.2 95.5 Reducto 90.8 85.4 91.2 95.8 LlamaParse 90.4 88.2 92.6 90.4 Mistral OCR 89.5 82.8 91.9 93.8 Claude Sonnet 5.5* 88.7 93.1 95.4 77.5 GPT-5.6 Sol 87.8 85.4 91.6 86.5 Extend 83.3 64.1 92.5 93.4 Azure 83.0 74.6 81.7 92.8 Tesseract none 17.6 0.0 unsupported 

 *Used in creating and verifying at least some tests, per Datalab . 

 Claude Sonnet 5.5 posts the top text (93.1) and tables (95.4) scores. Its layout score of 77.5 pulls its headline to 88.7. Reducto leads layout at 95.8. Datalab also plotted each headline against median latency and price per 1,000 pages. Latency was measured on 200 sampled pages, sent 8 at a time. 

 Datalab does not top its own benchmark. It flags the two models that helped build tests, and it tells readers to weigh the fact that it sells a parser. It commits to reporting OmniParseBench scores for future releases. Its advice: the best benchmark is your own documents. 

 How do you run OmniParseBench? 

 Copy Code Copied Use a different Browser uv pip install omni-parse-bench # score(): no network, no API keys
uv pip install 'omni-parse-bench[harness]' # + vendor adapters, to predict
uv pip install 'omni-parse-bench[benchmark]' # + dataset access, to run the benchmark
opb benchmark --out runs/ --limit 5 --providers datalab openai/gpt-5.6-sol 

 Vendors need keys such as DATALAB_API_KEY or OPENROUTER_API_KEY. The CLI shows its plan and asks before calling any vendor. Runs are resumable. The query guide shows how to compare runs by tag, suite or test type. 

 OmniParseBench vs olmOCR-bench vs ParseBench vs OmniDocBench 

 Feature OmniParseBench olmOCR-bench ParseBench OmniDocBench Maintainer Datalab Ai2 LlamaIndex OpenDataLab Scale 16,288 tests, 2,937 pages, 2,343 docs 7,010 tests, 1,403 PDFs 169,011 rules, 2,078 pages, 1,211 docs 1,651 PDF pages Languages 92 English Not disclosed 5 language types Scoring unit Pass/fail test; headline = mean of 3 families Pass/fail unit tests 5 dimensions, each with its own metric Overall from text edit distance, table TEDS, formula CDM Model judge None Not used for scoring None by default (opt-in for charts) Not used for scoring Content tags Per arg: structure, rendering, role, script, language 7 source categories 5 capability dimensions Page, text and table attributes Per-test provenance Yes, derivation on every test Extraction method per category Human-verified pages Not per test Latency and cost Median s/page, $ per 1,000 pages Not in dataset card ¢ per page on leaderboard Not disclosed License Code Apache 2.0; tests CC BY 4.0 with exceptions; page data licensed per source Dataset ODC-BY 1.0 Apache 2.0 Code Apache 2.0; data research only 

 Key Takeaways 

 16,288 yes/no tests on 2,937 pages in 92 languages. 

 Headline = mean of text, tables and layout pass rates. 

 Tags slice results; they never change a verdict. 

 Datalab built it and ranks second: Gemini 3.8 Flash 92.9*, Datalab accurate 92.7. 

 Apache 2.0 code; scoring runs offline without API keys. 

 * used in building some tests 

 Check out the blog post , dataset and GitHub repo . 

 Thanks to the Datalab team for the resources behind this article. Datalab supported and sponsored this content. 
 The post Datalab Releases OmniParseBench: An Open OCR Benchmark With 16,288 Pass/Fail Tests to Audit OCR Parsers appeared first on MarkTechPost .
