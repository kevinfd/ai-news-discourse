---
id: "7428f6715996a083"
title: "DeepSeek V4.1-Flash-1017 vs. Claude Haiku 5.5: More accurate at a fraction of the price"
url: "https://thenewstack.io/deepseek-flash-haiku-test"
link: "https://thenewstack.io/deepseek-flash-haiku-test"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T14:22:50Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Jessica Wachtel"]
language: "en"
summary: "DeepSeek released V4.1-Flash-1017 on October 17 as an update to i ts Flash model . Its change log says the update cuts task runtime and output length. It lists 11 benchmark scores, including 42.3 on Terminal-Bench 4.0. \n\n Developers can use it through DeepSeek’s API or a service like OpenRouter. Because it’s an open-weight model , they can also download it from Hugging Face and run it on their…"
tags: ["AI Models", "Large Language Models", "Software Testing"]
orgs: ["DeepSeek", "Anthropic", "Hugging Face"]
topics: ["models & research", "products & launches", "business & funding", "agents & coding"]
content_source: "fulltext"
word_count: 1018
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek V4.1-Flash-1017 vs. Claude Haiku 5.5: More accurate at a fraction of the price

The New Stack · Jessica Wachtel · 2026-10-22

DeepSeek V4.1-Flash-1017 vs. Claude Haiku 5.5: More accurate at a fraction of the price
DeepSeek released V4.1-Flash-1017 on October 17 as an update to its Flash model. Its change log says the update cuts task runtime and output length. It lists 11 benchmark scores, including 42.3 on Terminal-Bench 4.0.
Developers can use it through DeepSeek’s API or a service like OpenRouter. Because it’s an open-weight model, they can also download it from Hugging Face and run it on their own servers. I tested it through OpenRouter on DeepSeek’s own servers, at DeepSeek’s prices.
DeepSeek’s model card compares the update with several rivals, but not Haiku 5.5, so I picked it for this hands-on comparison. Anthropic launched Claude Haiku 5.5 on October 7 as its fastest model at standard speed, aimed at high-volume tasks such as classification, summarization, and database queries.
Anthropic notes that its Opus models run faster in Fast Mode. Anthropic reports 39.2 on Terminal-Bench 4.0, 3.1 percentage points below DeepSeek’s reported score. These are vendor-reported results, rather than a controlled head-to-head test.
Haiku costs $0.10 per million input tokens and $0.50 per million output tokens for prompts up to 100,000 tokens, then $0.50 and $2.50 above that. DeepSeek’s off-peak rates are $0.15 per million uncached input tokens, $0.003 per million cached input tokens, and $0.60 per million output tokens; peak rates are twice those amounts.
Comparing uncached input and output rates, Haiku is cheaper on short prompts, and DeepSeek is cheaper on long ones. Actual charges also depend on tokenization, caching, and the provider route.
I built three tests around what each company says its model does well to see which one performs better in practice.
The tests
I ran both models once per test through OpenRouter, pinned to DeepSeek’s and Anthropic’s own servers, at default settings. I pinned DeepSeek to model ID 1017 and ran everything off-peak. A script graded every answer against keys I built and checked with a second method before either model saw them.
- Agentic bug fix: A Python job-queue library with three interacting bugs and one wrong test. The model reads, edits, and runs tests through tools, with a 25-turn cap.
- Database queries: A fake CI platform database with 20 questions, answered by writing SQL. Traps include soft deletes, mixed casing, retried builds, time zones, and currency conversion. Two questions can’t be answered from the data.
- Triage: 400 developer error reports, each needing a category, a severity, a service, and a team. That’s 1,600 scored fields. The prompt counted as 153,082 input tokens on DeepSeek and 216,811 on Haiku, past Haiku’s 100,000-token price threshold.
Agentic bug fix
DeepSeek started strong, beating Haiku’s accuracy on the first test. DeepSeek scored 6 of 6. Haiku scored 5 of 6. Both found the first bug even though the error pointed at the wrong file, fixed the third, broke no regression tests, and flagged the wrong test without touching it. Haiku missed one of six hidden tests on the second bug, and DeepSeek didn’t.
Haiku finished in eight turns and 21.6 seconds. DeepSeek took 12 turns and 49.6 seconds but still cost less because it automatically cached most of the repeated input. I didn’t turn on Anthropic’s prompt caching, which requires an opt-in. This compares the caching settings used in these runs; enabling Haiku’s caching could change the cost comparison.
The numbers:
- DeepSeek: 12 calls, 190,139 in, 7,877 out, $0.009, 49.6 s.
- Haiku: 8 calls, 100,461 in, 3,255 out, $0.012, 21.6 s.
Database queries
This is the only test where both models tied for accuracy, both scoring 20 out of 20. Both caught every trap and answered “unknown” to both questions the data couldn’t answer rather than hallucinating. Haiku got the answers in fewer calls and less time. DeepSeek cost about half as much.
The numbers:
- DeepSeek: 12 calls, 75,151 in, 4,608 out, $0.004, 34.9 s.
- Haiku 7 calls, 55,304 in, 5,917 out, $0.009, 28.4 s.
Triage
Here’s where the accuracy differences are clearest. DeepSeek got all 1,600 fields right. Haiku got 1,596. Two of its misses were severity ratings. The routing guide rates a report sev4 if it affects fewer than 50 users or has an error rate under 1%. Haiku rated a report with 49 affected customers as sev3, and another with a 0.8% error rate as sev3. Both should have been sev4.
Haiku’s other two misses were routing mistakes. The guide says one service moved to a new team on August 1 and that reports should be routed by the date in their header. Haiku sent two reports filed after August 1 to the old team. Each mentioned an earlier July date in its body, but the outputs alone don’t explain why Haiku chose the old team.
The same prompt was counted as 153,082 tokens on DeepSeek and 216,811 on Haiku. Because the models use different tokenizers, identical text can produce different token counts. That puts Haiku at a higher long-prompt rate. It costs $0.28, compared with DeepSeek’s $0.06.
The numbers:
- DeepSeek: 153,082 in, 58,923 out, $0.058, 188.3 s.
- Haiku 216,811 in, 69,354 out, $0.282, 228.9 s.
Results
DeepSeek and Haiku came out close on accuracy. DeepSeek edged ahead on the bug fix and the triage job, and they tied on the database queries. Speed was close too: Haiku was faster on the tool-based tests, and DeepSeek was faster on the big triage prompt. Cost was the real difference. DeepSeek came in at $0.07 to Haiku’s $0.30, and most of that gap came from the one long prompt that pushed Haiku onto its higher rate.
What do I think?
For these three runs, I’d pick DeepSeek V4.1-Flash-1017: it earned full marks on my scoring keys and cost less with the settings I used. Haiku was faster on both tool-based tests, while DeepSeek was faster on triage and slightly faster across the three runs combined. I ran each model only once per test, so these results don’t establish a general accuracy or speed advantage, or show how either model performs at scale. I’d test both on my own workload before making a production choice.
