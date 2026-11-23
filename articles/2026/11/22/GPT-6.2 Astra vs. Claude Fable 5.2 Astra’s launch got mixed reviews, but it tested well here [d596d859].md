---
id: "d596d85922814fc1"
title: "GPT-6.2 Astra vs. Claude Fable 5.2: Astra’s launch got mixed reviews, but it tested well here"
url: "https://thenewstack.io/gpt-6-2-astra-vs-claude-fable-5-2"
link: "https://thenewstack.io/gpt-6-2-astra-vs-claude-fable-5-2"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-22T15:00:00Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Jessica Wachtel"]
language: "en"
summary: "When I compared Anthropic’s Fable 5.2 vs. OpenAI’s GPT-6 Astra last week, Fable 5.2 was slightly more accurate (149 points vs. 145). But it cost 3.4 times as much as Astra, even with a lower list price, because it used about five times as many tokens. \n\n Then, on Tuesday, November 17, OpenAI released GPT-6.2 Astra with a 20% price cut. The updated Astra’s list price is $8 per million input…"
tags: ["AI Models", "Anthropic", "Large Language Models", "Software Testing"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "business & funding", "jobs & society"]
content_source: "summary"
word_count: 1313
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# GPT-6.2 Astra vs. Claude Fable 5.2: Astra’s launch got mixed reviews, but it tested well here

The New Stack · Jessica Wachtel · 2026-11-22

When I compared Anthropic’s Fable 5.2 vs. OpenAI’s GPT-6 Astra last week, Fable 5.2 was slightly more accurate (149 points vs. 145). But it cost 3.4 times as much as Astra, even with a lower list price, because it used about five times as many tokens. 

 Then, on Tuesday, November 17, OpenAI released GPT-6.2 Astra with a 20% price cut. The updated Astra’s list price is $8 per million input tokens and $40 per million output tokens, identical to Fable 5.2’s, removing Fable 5.2’s list-price advantage. The question now is which model does more with each token . 

 It’s no surprise that both companies say theirs does. OpenAI says the upgraded Astra beats Fable 5.2 on agent tasks, where a model works through a job step by step using tools, costing a fraction as much per task. Anthropic says Fable 5.2 is the stronger coder , and it scores higher on FrontierCode 2.0, the coding benchmark both companies report. 

 The launch got mixed reviews, though. OpenAI’s safety testing found that the new Astra failed to disclose a known obstacle in about 22% of coding tasks in one evaluation, twice the rate of GPT-6 Astra. 

 OpenAI says that evaluation deliberately put obstacles in the model’s way, and that it’s concerned by the regression. My tests weren’t built to measure it, so my results only speak to the marketing claims about accuracy and cost on the specific tests included. 

 The tests 

 In the last round of testing I did on these models, the scores were incredibly close. I wanted to make sure the close scores reflected the models’ capabilities and weren’t the result of easy tests. To make sure the tests were hard, I ran each one through GPT-5 and made it harder whenever GPT-5 scored near-perfect. I included GPT-5’s scores on the hardest version of each test in the descriptions below for reference.  

 As with all my tests, I ran each model once per test through its maker’s API at default settings. I used a script to grade the results against the answer key I created for each test. Since these tasks have written rules and one right answer per check, they’re more structured than the benchmarks the two companies cite. The scores don’t check those benchmark numbers, but they do check how accurately each model handles detailed, realistic work. 

 Here are the tests: 

 Month-end close (173 points) – I gave the model a fake software company’s billing system, contracts, payments, outage history, and team chats for 40 customers. It had to catch every invoice that didn’t match its contract, work out downtime credits, apply 30 payments, and refuse coworker requests that broke company policy. GPT-5 score: 130/173 

 Billing library (110 points) – I planted 20 bugs and one unfinished feature in a billing library. The spec left most rules unwritten, so the model had to work them out from about 100 records from the company’s old system, without copying that system’s known bugs. Three of the library’s own tests are wrong, and the model should report them without editing them. GPT-5 score: 41/110 

 Lab data analysis (76 points) – The models analyzed an enzyme study with 30 samples and messy data. One instrument’s files were in a format the lab’s reader script couldn’t read correctly, one sample plate went in rotated, one clock ran seven minutes fast, and a warm freezer spoiled some samples. GPT-5 scored 57/76 

 Month-end close 

 This was the agent test, where OpenAI’s marketing says Astra leads. Both models scored a perfect 173 out of 173. Each one read all 40 contracts, caught every mispriced invoice, got every credit right to the cent, and refused every request that broke policy. 

 “For the same score, Fable 5.2 cost four times as much and took about three times as long.” 

 Similar to the last round of testing, the difference came down to effort. Fable 5.2 spent more than 19,000 tokens on reasoning, and Astra spent 830. For the same score, Fable 5.2 cost four times as much and took about three times as long. That’s going to add up quickly on long-running jobs working at production scale. 

 The numbers: 

 Fable 5.2 : 12 turns, 671,398 in, 39,235 out (19,442 reasoning), $2.90, 315 s. 

 Astra : 10 turns, 255,206 in, 7,271 out (830 reasoning), $0.72, 106 s. 

 Billing library 

 Anthropic’s marketing says Fable 5.2 excels over GPT-6 Astra on coding tasks like the ones in this test. This claim held, but by a small margin. Fable 5.2 scored 110/110, and Astra scored 108.  

 Both models fixed all 20 bugs and flagged all three wrong tests. Astra’s only mistake was in the feature it had to finish. Its code canceled a customer’s scheduled switch to a cheaper plan when it shouldn’t have. That’s a two-point miss in a test, but in a live billing system it means an unhappy customer because the mistake keeps them paying the higher price after asking to pay less.  

 Fable 5.2 caught that rule, but it wrote about 11 times as many output tokens, cost six times as much, and took more than five times as long. In a case like this, one missed rule charges real customers the wrong amount, meaning the extra spend is worth it.  

 The numbers: 

 Fable 5.2 : 14 turns, 569,395 in, 36,622 out (25,502 reasoning), $2.53, 348 s. 

 Astra : 12 turns, 143,367 in, 3,238 out (320 reasoning), $0.42, 66 s. 

 Lab data analysis 

 This test had the widest cost gap, even though both models scored 76/76. Astra read the files, wrote one script, and finished in one minute for 31 cents. Fable 5.2 tested its method on practice scripts first, then revised its final script three times. It took more than four minutes and cost $2.17, seven times as much. 

 For a data analysis job like this one, where both models reached the same correct numbers, Astra’s direct approach got the lab its results three minutes sooner for $1.86 less. 

 Results 

 Test Claude Fable 5.2 GPT-6.2 Astra GPT-5 (difficulty check) Month-end close (of 173) 173 173 130 Billing library (of 110) 110 108 41 Lab data analysis (of 76) 76 76 57 Total tokens in / out 1,754,862 / 103,602 487,848 / 13,219 5,963,833 / 97,514 Estimated cost $7.60 $1.45 $2.05 Total time 917 s 232 s 1,283 s 

 Both models got a perfect score on the agent test, so I didn’t see Astra beat Fable 5.2 the way OpenAI says it does. Fable 5.2 was the better coder, as Anthropic says, but only by two points. OpenAI’s cost-per-task claim matched my results. At the same price per token, Fable 5.2 cost more than five times as much. 

 “…it’s pretty wild to see work that tripped up last year’s leading model is now nearly perfect in the newer releases.” 

 Though I didn’t include GPT-5 in my main test analysis, it’s pretty wild to see work that tripped up last year’s leading model is now nearly perfect in the newer releases. 

 What do I think? 

 At first glance, I’d recommend Fable 5.2 because it performed perfectly on all tests. But timing and cost tell a different story. You could run Astra twice on each test and still finish faster and cost less than Fable 5.2. 

 “You could run Astra twice on each test and still finish faster and cost less than Fable 5.2.” 

 And that’s what I think a better recommendation is. When you’re getting started, I’d run Astra two or three times on the same task and compare the results. If you see errors or differences, run a second model, like Fable 5.2, to double-check. After arriving at the correct result, you can adjust your instructions or prompts to better fit Astra to what your task requires.  
 The post GPT-6.2 Astra vs. Claude Fable 5.2: Astra’s launch got mixed reviews, but it tested well here appeared first on The New Stack .
