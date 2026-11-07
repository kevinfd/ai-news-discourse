---
id: "378167865e661ad9"
title: "Business AI Agents with DeepSeek API: Optimizing API Costs by Selecting Models"
url: "https://note.com/bynalize_dx/n/n0c8c806c8dc2?hl=en"
link: "https://note.com/bynalize_dx/n/n0c8c806c8dc2?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-07T01:11:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["らい｜Ai活用ワーカー・営業×Ai駆動開発"]
language: "en"
summary: "I built a business AI agent using the DeepSeek API. I have integrated it into routine tasks like inquiry handling and information classification, and I optimize API costs by selecting different models ..."
tags: []
orgs: ["DeepSeek", "OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 1389
paywalled: false
image: "http://www.bing.com/th?id=ONUT.AJfN13ICJR-7SgUztFyiwA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Business AI Agents with DeepSeek API: Optimizing API Costs by Selecting Models

note · らい｜Ai活用ワーカー・営業×Ai駆動開発 · 2026-11-07

Business AI Agents with DeepSeek API: Optimizing API Costs by Selecting Models
I built a business AI agent using the DeepSeek API. I have integrated it into routine tasks like inquiry handling and information classification, and I optimize API costs by selecting different models depending on the use case.
The motivation was that I had several tasks left on my desk that involved repeating almost the same judgment every time. Even though I wanted to leave them to AI, if I threw everything at the smartest model, I wouldn't be able to predict the end-of-month bill.
In this article, I will summarize how I set up inquiry handling and information classification with the DeepSeek API, as well as my approach to selecting models for different purposes. As written on the cover, the main point is that "DeepSeek models should be selected based on the use case."
I tried building a business AI agent with the DeepSeek API
The AI agent referred to here is a small program that reads incoming text, makes judgments according to a fixed procedure, and passes it on to the next process. It is not a large-scale autonomous system.
What I built handles receiving inquiries, identifying their type, determining the person in charge, and creating a draft reply. Sending and final judgment are performed after a human reviews it.
My policy is to use AI as a drafting assistant. I leave classification and drafting to the AI, and I always review it myself before it goes out.
What you can do with the DeepSeek API (facts confirmed from official sources)
This content was verified on 2026-11-06 via the official DeepSeek documentation (api-docs.deepseek.com).
The official documentation states that the API format is compatible with both OpenAI and Anthropic. If using the OpenAI SDK, you can call it by setting the base URL to https://api.deepseek.com . The Anthropic format is https://api.deepseek.com/anthropic .
Two model names were listed: deepseek-flash and deepseek-v4-pro. It is stated that deepseek-flash is currently provided as DeepSeek-V4.1-Flash-1017.
You can also adjust the depth of reasoning. You can toggle the thinking process on and off with the "thinking" parameter, and choose the depth from "low", "high", or "max" using "reasoning_effort". According to the official explanation, thinking is on by default, and the default depth is "high".
There is also a mode to receive results in JSON. The official documentation states to set "response_format" to "json_object" and include the word "json" and a JSON example in the prompt.
Regarding pricing, I will not write it here because I could not confirm the figures on the official pricing page at the time of writing this article. Since amounts on third-party sites vary by time, please check the official Models & Pricing page before using it.
Integrating into routine tasks for inquiry handling and information classification
From here on is my experience. The first things I integrated were inquiry handling and information classification. In both cases, the input format is mostly fixed, and the types of answers I want to output are limited.
The diagram below shows the flow from receiving an inquiry to information classification, sorting, and human confirmation.
The instructions I use for classification are in the following format. These are sentences to be pasted into the system prompt, and the classification names should be rewritten to match your own business.
あなたは問い合わせの仕分け担当です。
受け取った文章を読み、次のjson形式だけで返してください。
categoryは「料金」「使い方」「不具合」「その他」のどれか1つにします。
判断に迷うときは、confidenceを"low"にしてください。
{"category": "使い方", "confidence": "high", "summary": "30字以内の要約"}
I added the "confidence" field so that only inquiries where the AI is uncertain are routed to a higher-tier model. This serves as a gateway to avoid throwing everything at the same model.
When calling it with Python, you can use the OpenAI SDK as is. Since classification is a short process, I have disabled thinking.
from openai import OpenAI
client = OpenAI(api_key="DeepSeek API Key", base_url="https://api.deepseek.com")
res = client.chat.completions.create(
model="deepseek-flash",
messages=[
{"role": "system", "content": "Instructions for the classification above"},
{"role": "user", "content": "Body of the inquiry"},
],
response_format={"type": "json_object"},
max_tokens=300,
extra_body={"thinking": {"type": "disabled"}},
)
print(res.choices[0].message.content)
Please do not write the API key directly in the code; read it from environment variables instead. The example above has been replaced for readability.
Optimizing API costs by selecting models according to the use case
The axes for selection are the type of processing and how much you want the model to think. Processes with predetermined answer candidates are run lightly, while only processes that require reading context and making judgments are run deeply.
When you deepen the reasoning, the amount of thinking the AI does increases. In my assessment, this increases the time until a response is returned and also increases the tokens used. Tokens are the units of characters the AI reads and writes, and they form the basis for calculating API costs.
The table below is a quick reference guide I use when choosing models for each use case.
By structuring it this way, you can limit the number of times the more expensive process is called to only those cases where confidence is low. It has become easier to forecast billing amounts compared to running all cases with deep reasoning.
Please check the unit price for each model on the official pricing page before applying it. Once you know the unit price, you can estimate monthly costs based on the number of daily cases and the percentage that escalate to the higher-tier model.
Things that were different from what I expected and the line drawn to avoid including company information
What was different from what I expected was how the JSON mode is handled. The official warning states that when the output does not result in valid JSON, the content may return as just whitespace. Apparently, this can happen even if the finish_reason is stop.
Therefore, it is safer to include a process on the program side to "retry once if empty." Checking if the word "json" and a JSON example are included in the prompt is also the first place to review. If max_tokens is too small, it will cut off midway, so I set short limits, such as keeping classification summaries under 30 characters.
Another point is that the official documentation states that some parameters like temperature do not work when deep reasoning is enabled. It is better not to assume that the same settings will work for both on and off states.
The thing I was most careful about was the line drawn regarding the information I input. The DeepSeek Privacy Policy (updated February 10, 2026) states that collected information is stored on servers located in the People's Republic of China.
I do not input customer names, personal information, or internal company documents and figures. If you are using it for company business, you should first check your internal rules and AI usage policies. For personal verification, I believe it is best to observe how it works using fictional inquiry text you have created yourself.
Who the DeepSeek API is and isn't for, and what you can try this week
It is suitable for those who have called APIs using the OpenAI SDK and want to run fixed processes like classification or drafting at a low cost. Since you can try it just by changing the base URL and model name, the effort to switch is minimal.
It is not suitable for tasks that cannot be performed without inputting customer information or internal company documents directly. In that case, it is better to use an AI service that your company has contracted with.
There are two next actions.
The first step is to open the Models & Pricing page in the official DeepSeek documentation and note the unit prices for deepseek-flash and deepseek-v4-pro. This will take about 10 minutes.
The second step is to prepare the classification prompt mentioned above along with three sample inquiry texts, and have deepseek-flash classify them with thinking turned off. You can test this in about 30 minutes, including checking whether it returns JSON and identifying which items have low confidence.
On the same theme, I also wrote about "How to make Notion your second brain and get consistent answers from any AI."
This note is a record of patterns and failures from testing AI in actual sales and development work. I aim to update it once a day, so if you would like to read other articles, please follow me on note to receive new posts.
