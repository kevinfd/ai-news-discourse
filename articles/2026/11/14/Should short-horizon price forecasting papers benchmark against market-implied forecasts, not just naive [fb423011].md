---
id: "fb423011ee4685dd"
title: "Should short-horizon price forecasting papers benchmark against market-implied forecasts, not just naive baselines? [D]"
url: "https://reddit.com/r/MachineLearning/comments/1xw6fk9/should_shorthorizon_price_forecasting_papers"
link: "https://reddit.com/r/MachineLearning/comments/1xw6fk9/should_shorthorizon_price_forecasting_papers"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-14T16:23:34Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["happypeanut-t"]
language: "en"
summary: "been reading a bunch of papers on short term crypto and commodity price forecasting (transformers, LSTMs, the usual). almost all of them compare against ARIMA, a random walk, maybe a simple LSTM, and report a better RMSE. what i rarely see is a comparison against what the market already expects. options implied vol for the range, or a crowd forecast where people put money on outcomes. those…"
tags: ["r/MachineLearning"]
orgs: []
topics: []
content_source: "post"
word_count: 135
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xw6fk9/should_shorthorizon_price_forecasting_papers/"
score: null
comments: null
community: "r/MachineLearning"
---

# Should short-horizon price forecasting papers benchmark against market-implied forecasts, not just naive baselines? [D]

Reddit · happypeanut-t · 2026-11-14

been reading a bunch of papers on short term crypto and commodity price forecasting (transformers, LSTMs, the usual). almost all of them compare against ARIMA, a random walk, maybe a simple LSTM, and report a better RMSE. what i rarely see is a comparison against what the market already expects. options implied vol for the range, or a crowd forecast where people put money on outcomes. those already use alot of public info, so beating a random walk doesnt say much if you cant beat the market's own forecast. also most papers only score the point forecast. for something like btc the interval matters way more, and coverage of an 80% interval tells you more than RMSE does. is there a reason this isnt standard? data access? or am i missing papers that do it
