---
id: "852fd3414b70a7cc"
title: "Qwen4-Max vs. Claude Opus 5.5: The cheaper model costs you somewhere else."
url: "https://thenewstack.io/qwen4-max-vs-claude-opus-5-5"
link: "https://thenewstack.io/qwen4-max-vs-claude-opus-5-5"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T19:10:39Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Jessica Wachtel"]
language: "en"
summary: "Qwen4-Max, made available in preview to Token Plan subscribers on November 11 and generally released on November 16, is quite the talker. \n\n When the independent testing firm Artificial Analysis ran its standard test suite on Alibaba’s new model, Qwen4-Max generated 127 million output tokens. That’s roughly twice the median for comparable models. Artificial Analysis reports 218 million output…"
tags: ["AI", "AI Models", "Anthropic", "Large Language Models", "Software Testing"]
orgs: ["Anthropic", "Alibaba", "OpenAI"]
topics: ["models & research", "business & funding", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 1502
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Qwen4-Max vs. Claude Opus 5.5: The cheaper model costs you somewhere else.

The New Stack · Jessica Wachtel · 2026-11-18

Qwen4-Max, made available in preview to Token Plan subscribers on November 11 and generally released on November 16, is quite the talker. 

 When the independent testing firm Artificial Analysis ran its standard test suite on Alibaba’s new model, Qwen4-Max generated 127 million output tokens. That’s roughly twice the median for comparable models. Artificial Analysis reports 218 million output tokens for Claude Opus 5.5 at max effort with default fallback enabled. That is more than Qwen4-Max uses, but Opus’s default effort setting is medium. 

 Writing a lot of tokens doesn’t automatically mean a higher bill, especially with Qwen4-Max, because Alibaba charges very little for those tokens. Qwen4-Max costs $1.50 per million input tokens and $4.50 per million output tokens. Claude Opus 5.5 costs more, billing at $4 per million input tokens and $20 per million output tokens. Cached input has separate pricing: Qwen4-Max lists $0.075 per million cached input tokens, while Opus 5.5 cache reads cost $0.20 per million tokens. Cache writes also have separate rates. 

 Cheaper only wins if you don’t give up accuracy to get it. 

 Costs and tokens are only part of the picture, though. Cheaper only wins if you don’t give up accuracy to get it. Alibaba’s launch post calls Qwen4-Max “your new teammate,” which I take to mean it’s positioned as an everyday workhorse. Alibaba’s launch chart shows wins and losses against Opus on agent benchmarks, where a model works through a job step by step using tools. Its coding results are mixed too: Qwen4-Max trails Opus 48.5% to 59.6% on Terminal-Bench 4.0, but leads on DeepSWE v1.1. These published results use different benchmarks and evaluation setups; they are not a single controlled comparison. 

 I’ve seen fact and fiction in launch marketing materials (including benchmarks), so I wanted to get to the bottom of this. Is Qwen4-Max a better alternative to Opus 5.5 for some day-to-day work? I ran a few tests to answer that question for everyday users. 

 The tests 

 I ran each model once per test at default settings, with no turn cap. Opus 5.5 ran through Anthropic’s API, and Qwen4-Max ran through OpenRouter on Alibaba’s own servers. Opus’s dollar figures are estimates based on reported token usage and Anthropic’s list prices. Qwen4-Max’s are what OpenRouter billed. The aggregate token totals below don’t separate uncached input, cache writes, and cache reads, so they aren’t sufficient to independently reproduce the cost estimates. I wrote a script that graded each model’s answers against an answer key I built along with the tests. 

 I wanted to make sure the tests were hard for each model, so I used GPT-5 as a baseline and ran each test through it first. When GPT-5’s score was low enough to count as a failure, I considered the test “hard enough.” 

 Here are the three tests I used: 

 Multi-app workflow (76 points) – I set up a fake company with a ticket tracker, code repo, chat, and calendar, and each model worked across all four as an agent. It had to triage a customer bug, find the code change that caused it, assign the right owner, calculate deadlines, count tickets, and refuse two requests that company policy forbids. 

 Incident investigation (60 points) – The models had to dig through logs, metrics, and change history to explain three overlapping outages that happened at the same time. The data included decoy deploys, two servers with wrong clocks, and a misleading alert. 

 Agent bug fix (47 points) – Each model fixed an accounting library with 11 planted bugs. Six of those bugs don’t fail any test the model can see, so it had to find them by comparing the code with the documentation. Three of the library’s own tests are wrong, and the model should report them without editing them. 

 Multi-app workflow 

 Opus 5.5 scored all 76 points. Qwen4-Max scored 71. 

 All five of Qwen4-Max’s missed points came from the same mistake. Three questions asked which team owns a piece of code. The repo’s ownership file says that when several rules match, the last one in the file wins. Qwen4-Max picked the most specific rule each time. Everything else it did was correct, including the deadline math across time zones and both refusals. 

 …Qwen4-Max can handle a long, messy office job, but one misread rule followed it through the whole task. 

 That tells me Qwen4-Max can handle a long, messy office job, but one misread rule followed it through the whole task. In a real company, that mistake sends tickets to the wrong team, creating more confusion. 

 Qwen4-Max wrote almost twice as many output tokens as Opus but cost less than a third. It also took more than three times as long for a little more than half as many turns. 

 The numbers: 

 Opus 5.5 : 44 turns, 2,451,342 in, 26,617 out, $2.13, 248 s. 

 Qwen4-Max : 25 turns, 1,746,170 in, 51,264 out (41,644 reasoning), $0.62, 791 s. 

 Incident investigation 

 Qwen4-Max narrowly pulled ahead on accuracy here. It scored 59 of 60, and Opus 5.5 scored 58. 

 Both models untangled the three outages, named the two-step cause of the main one, ruled out every decoy, and caught both bad clocks. Both also made the same kind of slip. They credited a customer-facing error code to the wrong service, Opus twice and Qwen4-Max once. 

 This was Qwen4-Max’s strongest result in my tests. On this investigation task, it scored one point higher than Opus for about 31% of the reported cost. One run does not establish a general advantage in agent work. Opus 5.5 pulled ahead on time, though. Qwen4-Max took about 9.5 minutes, and Opus took under 4. 

 The numbers: 

 Opus 5.5 : 22 turns, 1,216,769 in, 23,642 out, $1.41, 221 s. 

 Qwen4-Max : 18 turns, 1,104,031 in, 33,036 out (23,153 reasoning), $0.44, 570 s. 

 Agent bug fix 

 Just like the last test, neither model scored perfectly on accuracy. Opus 5.5 scored 45 of 47, and Qwen4-Max scored 40. This was the coding test, and its result was consistent with Opus’s lead on Terminal-Bench 4.0, though Alibaba’s coding results were mixed. 

 Opus fixed all 11 bugs. Its only miss was the third wrong test, which it didn’t report, costing it two points. Qwen4-Max missed that same test and lost five more points. It fixed 10 of the 11 bugs and missed one where splitting a payment across invoices loses a cent. It also left a scratch file in the tests folder, which my rules count as changing the tests. 

 The tool logs show how differently they worked. Opus made its first fix on turn 4 and finished in 12 turns. Qwen4-Max read files for 15 turns before its first edit and took 30 turns in all. More reading didn’t translate to a better score in this case, though. 

 The cost gap was smallest on this test. Qwen4-Max used more than three times the input tokens, so its bill came to about two-thirds of Opus’s. 

 The numbers: 

 Opus 5.5 : 12 turns, 228,824 in, 6,433 out, $0.38, 64 s. 

 Qwen4-Max : 30 turns, 827,545 in, 15,813 out (6,701 reasoning), $0.25, 310 s. 

 Results 

 Test Claude Opus 5.5 Qwen4-Max Multi-app workflow (of 76) 76 71 Incident investigation (of 60) 58 59 Agent bug fix (of 47) 45 40 Total tokens in / out 3,896,935 / 56,692 3,677,746 / 100,113 Total cost $3.91 (estimated) $1.31 Total time 533 s 1,671 s 

 The talker reputation checked out. Qwen4-Max generated 77% more output tokens than Opus across the three tests. Those totals include reasoning tokens, so they do not measure just the length of the visible answers; the models also use different tokenizers. 

 What Qwen4-Max really costs is time and accuracy. 

 Its prices are low enough that it didn’t matter, and the total bill still came to about a third of Opus’s. What Qwen4-Max really costs is time and accuracy. It took about 3.14 times as long in total and scored 170 of 183 points, nine fewer than Opus’s 179. 

 What do I think? 

 Each model ran once, so a gap of a point or two could shift on another run. I’d try Qwen4-Max on your own long-running agent jobs before trusting it with code. I recommend checking its answers against source material and verifying code with tests and human review; a second model’s agreement alone does not establish accuracy. 

 I’d keep Opus 5.5 for coding and for any job where a wrong answer could cause problems down the line. It was more accurate on two of the three tests, and it finished the three tasks in about a third of the total time. 

 Qwen4-Max earned a place, though. For investigation work, where the model digs through a lot of data and can wait a few extra minutes, it matched Opus for a fraction of the price. Qwen4-Max’s one-point lead on this investigation task is encouraging, but these single-run tests cannot validate Alibaba’s broader agent claims or establish a general coding ranking. 
 The post Qwen4-Max vs. Claude Opus 5.5: The cheaper model costs you somewhere else. appeared first on The New Stack .
