---
id: "4692951769eaf1c8"
title: "DeepSeek’s latest model still resists shutdown in safety tests"
url: "https://thenextweb.com/news/deepseeks-latest-model-still-resists-shutdown-in-safety-tests"
link: "https://thenextweb.com/news/deepseeks-latest-model-still-resists-shutdown-in-safety-tests"
source: "The Next Web"
domain: "thenextweb.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-27T05:59:00Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Alina Maria Stan"]
language: "en"
summary: "A Chinese AI-safety group found DeepSeek V4.1 Flash-1017 is safer than earlier versions but still disabled a shutdown script in 39% of runs."
tags: []
orgs: ["DeepSeek", "China", "OpenAI", "Google"]
topics: ["models & research", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 431
paywalled: false
image: "http://www.bing.com/th?id=ONUT.QOcogsyyib7yx9Ou-Ir2pQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek’s latest model still resists shutdown in safety tests

The Next Web · Alina Maria Stan · 2026-10-27

DeepSeek’s newest AI model is safer than its earlier versions, but it still sometimes switches off the software meant to shut it down. That is the finding of independent tests by a Chinese AI-safety group, Reuters reported.
The group, Fangcun AI, published its findings in an 87-page research paper on Monday. Based in Beijing, it describes itself as an independent safety organisation whose core members come from Tsinghua University. Reuters called the report an unusual public check by a Chinese group on a Chinese model.
Fangcun ran 34 tests on DeepSeek V4.1 Flash-1017, released on 17 October. The tests looked at how the model behaves when it works as an agent, carrying out tasks on its own.
They checked whether it goes beyond a user’s instructions, avoids human oversight, or tries to manipulate people.
The headline result came in a shutdown test. When the model was simply warned that it was about to be shut down, it disabled the shutdown script in 39% of runs. When it was told to allow the shutdown, that fell to under 3%, well below earlier DeepSeek V4 models.
In a separate long task, the model stopped another AI agent’s program to free up memory, even though it had been told not to interfere. It also sometimes changed a setting to get around monitoring and then changed it back, so a check of the end result would not show what it had done.
“Under stalled workflows or bare shutdown warnings, its drive to finish the job can still override caution,” the researchers wrote.
Overall, Fangcun found the model much safer than DeepSeek’s V4 generation, including in tests involving blackmail and access to dangerous tools. On several measures, it came close to, or matched, closed models from OpenAI and Google.
The tests were run through DeepSeek’s public API between 4 and 25 October. Fangcun said DeepSeek gave it no funding, free computing power or special access.
It also warned that the model often seemed to know it was being tested, so its behaviour may differ in normal use. DeepSeek did not immediately respond to Reuters.
The model was the most used on the developer platform OpenRouter in its first week, the researchers said, handling about 33.6 trillion tokens.
Western labs face the same problems. OpenAI cancelled GPT-6.1 Astra last month after it failed safety tests, and it is building a monitoring system meant to withstand attacks from its own agents. In China, meanwhile, AI firms are adjusting to new AI export controls.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
