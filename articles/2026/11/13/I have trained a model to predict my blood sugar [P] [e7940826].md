---
id: "e794082680bd704a"
title: "I have trained a model to predict my blood sugar [P]"
url: "https://reddit.com/r/MachineLearning/comments/1xvja5n/i_have_trained_a_model_to_predict_my_blood_sugar_p"
link: "https://reddit.com/r/MachineLearning/comments/1xvja5n/i_have_trained_a_model_to_predict_my_blood_sugar_p"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T20:48:25Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["0xdeadf1sh"]
language: "en"
summary: "I have trained a custom 31,253 parameter encoder-only transformer on a pregenerated synthetic CGM dataset and fitted it to my own personal data using LoRA. It is competitive among other published models. I used 115 days of CGM data, of which 80 was used for training the adapter and 35 for testing. The model began with a pretraining stage where it consumed ~19,200 CGM-years worth of synthetic…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "business & funding"]
content_source: "post"
word_count: 289
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xvja5n/i_have_trained_a_model_to_predict_my_blood_sugar_p/"
score: null
comments: null
community: "r/MachineLearning"
---

# I have trained a model to predict my blood sugar [P]

Reddit · 0xdeadf1sh · 2026-11-13

I have trained a custom 31,253 parameter encoder-only transformer on a pregenerated synthetic CGM dataset and fitted it to my own personal data using LoRA. It is competitive among other published models. I used 115 days of CGM data, of which 80 was used for training the adapter and 35 for testing. The model began with a pretraining stage where it consumed ~19,200 CGM-years worth of synthetic data, consisting of 1 million simulated type 1 diabetics at 7 days each. The simulator is designed to aid in counterfactual reasoning, but I don't yet have a benchmark to test these capabilities downstream. Simply using these models on my phone gives me the impression that they do indeed react appropriately when forced to consider future insulin & carbs. In addition to time series input, two additional inputs are provided: insulin (U) and carbs (G, GI) as action curves where U = units of insulin, G = carbs in grams, GI = glycemic index. U is exact, while (G, GI) is my best estimate. The model is trained to output BG in Kovatchev risk-space using {DILATE,MSE} and pinball loss combined with learned Kendall-Gal weights. The figures above show models trained using DILATE. It can predict 2 hours into the future, infill missing traces, and do backcasts (predictions into the past). Source code: https://github.com/0xdeadf1sh/T1DMAI The model is also trained to predict time-of-day given past blood sugar, in contrast to other models that consume time-of-day as input feature. This capability emerges in >=48h context windows (i.e. 48 hours of past CGM trace). Natively the model has a variable context window size of 3.5 - 7.0 days. The model is still worse than me when it comes to predicting hypoglycemia in the next ~30 minutes.
