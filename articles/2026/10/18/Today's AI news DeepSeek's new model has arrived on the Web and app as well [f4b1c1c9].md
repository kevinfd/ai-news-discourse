---
id: "f4b1c1c94efb0a83"
title: "Today's AI news: DeepSeek's new model has arrived on the Web and app as well"
url: "https://note.com/jk_ai_bu/n/nad70cba96891?hl=en"
link: "https://note.com/jk_ai_bu/n/nad70cba96891?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-18T00:18:00Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["ほうかごAi部"]
language: "en"
summary: "DeepSeek's new model has arrived on the Web and app as wellThe Chinese AI company DeepSeek has released a new AI model 'DeepSeek-V4.1-Flash-1017'. This was announced on DeepSeek's official X account ..."
tags: []
orgs: ["DeepSeek", "China", "Hugging Face", "Anthropic"]
topics: ["products & launches", "models & research", "search & media", "business & funding"]
content_source: "fulltext"
word_count: 2611
paywalled: false
image: "http://www.bing.com/th?id=ONUT.movDsTF-xPpNtAhU10tP0A&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Today's AI news: DeepSeek's new model has arrived on the Web and app as well

note · ほうかごAi部 · 2026-10-18

DeepSeek's new model 'V4.1-Flash-1017' is now on the Web and app. I looked into the API since its price halves depending on the time of day
Today's AI news: DeepSeek's new model has arrived on the Web and app as well
The Chinese AI company DeepSeek has released a new AI model 'DeepSeek-V4.1-Flash-1017'. This was announced on DeepSeek's official X account at 17:35 on October 17, 2026 (Japan Standard Time). The '1017' at the end of the name indicates that it is the version released on October 17.
- What is it?: An improved version of the 'DeepSeek-V4.1-Flash' released in September. The test scores published by DeepSeek are higher than the previous version, and the time taken to complete tasks and the length of the answers have been reduced
- Where?: The DeepSeek website, smartphone app, and API (the gateway for calling the AI from custom apps and development tools) all switched to the new model on the same day
- API price: Unchanged. The model name used when calling it remains 'deepseek-flash'
- What was released alongside it: The 'Search API' for searching the web and the 'Fetch API' for loading specified pages have been released to all users
- Model contents: The 'weights' files, which are the core of the AI, have been released on Hugging Face and ModelScope. The license is MIT, and commercial use is permitted
The official announcement is here. 
👉 DeepSeek official X post (2026-10-17)
Even if the screen of an AI app looks the same as yesterday, the model running inside may have been replaced. The recent DeepSeek update is an example of this; the web, app, and API all switched to the new version without the user having to do anything. I will verify what has changed and what has not based on official information as of today (October 18, 2026).
In the after-school PC lab
'Hey, did you hear that DeepSeek has a new model? The name ends in '1017''
'That means the October 17th version. According to the official update history, the web and app models were also updated to the new version on the same day'
'Wait, does that mean my smartphone app updated its internals without me doing anything? It's amazing that it's getting stronger without me even knowing!'
'The API price is reportedly staying the same. However, DeepSeek's API prices change depending on the time of day, and it's twice as expensive during busy hours compared to other times'
'...So the price changes by time. I wonder if it would be easier to understand if I drew it on a clock'
'Also, the data collected by DeepSeek is stored on servers in China. Let's check that out before using it'
There are three places where you can use DeepSeek
DeepSeek is a conversational AI provided by a company in Hangzhou, China (Hangzhou DeepSeek Artificial Intelligence Co., Ltd.). The new model is now available in the following three places as of the same day.
- Web version: Open the DeepSeek site in your browser, log in with your account, and start chatting.
- App: Chat from the official smartphone app.
- API: Call it from your own apps or development tools like Claude Code or Codex. Fees are deducted from your pre-charged balance based on usage.
Users of the web version and app do not need to change any settings. The official update history states that the web and app models have also been updated to V4.1-Flash-1017.
'The web and app are already using the new model once you open them. For API users, the model name can remain as 'deepseek-flash'.'
'Does releasing the weight files mean you're distributing the AI's internals?'
'Yes. If you get the files, you can run it on your own server. However, given the size of 763 billion parameters shown on Hugging Face, it's not something you'd run on a standard laptop.'
'I'll just quietly close my laptop... Chatting via the app is the easiest way after all!'
What changed in 1017
The changes noted in the official update history and model card are as follows:
- Scores: Scores improved over the previous version in all 11 tests published by DeepSeek. The 'DeepSWE v1.1' test for fixing programming bugs rose from 74.2 to 77.0, and the 'Terminal-Bench 4.0' test for working while typing commands rose from 31.2 to 42.3.
- Speed and Length: Reduced the time to complete tasks and the length of the answers.
- Creation: Improved the ability to complete a single project from start to finish, such as game development or 3D modeling. They explain it was trained using a method (reinforcement learning) that uses its own output evaluations to learn.
- Input: Can read text and images. The amount it can handle at once (context) is 1 million tokens.
The title of the announcement page is 'Wish-Driven Programming Made Real'. The name implies that you can create programs by expressing what you want to make like a wish, and it features examples such as a 3D model of the Forbidden City and a racing game you can play in your browser.
'The scores are values measured and published by DeepSeek itself. Let's read them separately from figures measured by other companies.'
'Being able to make a game just by stating a wish is such a dream! I wonder if it could make a shooting gallery game for a school festival?'
What changes when answers become shorter?
Hearing that answers have become shorter might sound like cutting corners. DeepSeek's explanation is the opposite: they improved the scores over the previous version while reducing task time and answer length. The official team explains this as an update where both performance and cost have improved simultaneously.
With the API, the length of the answer directly affects the cost. API pricing is determined by counting the amount the AI reads (input) and writes (output) in units called 'tokens,' so if you can finish the same task with a shorter output, the output cost decreases accordingly.
'If the quality is the same, it's easier to read if it answers briefly, right? And if it costs less money, even better!'
'API prices are determined by the cost per token. So, 'finishing briefly' directly translates to 'finishing cheaply.'
Here is a detailed explanation: Looking at it from a technical and financial perspective.
(The full text is free today)
Mechanism: API pricing is determined by 'tokens' and 'time slots'.
Tokens are small segments used when the AI reads and writes text. According to official explanations, they can be words, or sometimes just a single number or punctuation mark. Pricing is set as 'dollars per 1 million tokens'.
DeepSeek's API has another metric: time slots. Since the price revision in August, they have separated prices into busy time slots (peak) and others (off-peak), with off-peak being exactly half the price of peak. The prices for the new model (deepseek-flash) are as follows (per 1 million tokens).
- Input (if not a cache hit): Off-peak $0.15 / Peak $0.3
- Input (if a cache hit): Off-peak $0.003 / Peak $0.006
- Output: Off-peak $0.6 / Peak $1.2
Peak time slots are Monday to Friday, 01:00–04:00 and 06:00–10:00 UTC. Converted to Japan Standard Time, this is 10:00–13:00 and 15:00–19:00 on weekdays. On Chinese public holidays, it is off-peak all day, even on weekdays. Saturdays and Sundays are also off-peak all day.
'Let's think with hypothetical numbers. If you use 1 million input tokens and 1 million output tokens, it would be $0.15 + $0.6 = $0.75 during off-peak, and $1.5 during peak. Even for the same task, you can cut the cost in half just by shifting the time.'
'Since today is Sunday, it's off-peak all day! Does that mean we should do it now?'
'For large, non-urgent tasks, it's better to run them in batches at night or on weekends. This price list is for those using the API.'
Why change prices based on time slots?
DeepSeek wrote the reason during the August price revision. It is to allocate computing resources reasonably by halving the price during off-peak times, encouraging users to choose when to perform their tasks.
Pricing that is higher during busy times and lower during quiet times is not unique to AI. Time-of-use electricity plans and the difference between peak and off-peak travel seasons are based on the same concept. If usage concentrates at one time, facilities must be prepared to handle that peak. If usage is spread out, more tasks can be completed with the same facilities.
'From the seller's perspective, they don't have to leave facilities idle during quiet times. From the buyer's perspective, they can use it cheaply if they choose the time. It's a pricing method that has reasons for both sides.'
'...If I made a clock where only the two daytime peaks were painted in a dark color, would it be easy to tell at a glance? It's also interesting that there's a gap between the peaks only between 13:00 and 15:00.'
'If you hit the cache,' it becomes 1/50th of the price.
In the price list, only the input price is divided into two types. Input that hits the cache is $0.003 per 1 million tokens during off-peak hours. This is 1/50th of the $0.15 price when it doesn't hit.
Caching is a mechanism where DeepSeek saves the beginning (the start) of the text you sent previously, and it is turned on by default for all users. In the official documentation example, if you send 'A+B' the first time and 'A+B+C' the second time, the 'A+B' part of the second request hits the cache. The condition is that the beginning must be exactly the same.
'If you use it by attaching the same long instruction manual to the beginning and only changing the final question, the manual part becomes cheaper. Imagine a situation at a company where you have employees read the same internal manual every time before asking a question.'
'Keep the beginning consistent every time. If you change even one character in the middle, it won't hit from that point onward.'
'Search API' and 'Fetch API' released on the same day
On October 17th, the same day as the new model, DeepSeek released two web search components. Both can be used by anyone using the API and are used when building apps that have AI look up the latest information.
- Search API: A search engine built in-house by DeepSeek that searches the Web. Results return 1 to 50 items per request, including titles, URLs, and summaries.
- Fetch API: Loads the page at the specified URL and returns the body text in an easy-to-read format (Markdown).
- Pricing: Both cost $0.75 per 1,000 successful results. Requests are not counted if the result is empty, fails, or times out. The price is the same even if you increase the number of items retrieved.
- Free period: It is currently free if you use the DeepSeek API via DeepSeek Harness, Claude Code, or Codex, and search is called automatically within those tools. Billing begins at 1:00 AM JST on November 1st.
- Rate limits: Search and Fetch are separate, with a limit of 5 requests per second per account.
You can also write conditions in search terms such as 'site:' (only within this site) or 'after:' (only pages published after this date).
'$0.75 for 1,000 requests means it's $0.00075 per request. That's $7.50 for 10,000 requests. The rule that it only counts when a result is returned is also important.'
'When the free period ends, billing will start automatically. If you have search enabled in your development tools, make sure to review your settings before November 1st.'
'Being able to put search components into my own app sounds way too fun! I could even make a news-gathering tool for my club!'
Data storage locations and rules before use
Before using DeepSeek, you should check how data is handled. The official privacy policy, terms of service, and materials from Japan's Personal Information Protection Commission state the following.
- Storage location: Information collected by DeepSeek is stored on servers located in the People's Republic of China (Privacy Policy, updated February 10, 2026).
- Japanese documentation: The Personal Information Protection Commission issued 'Information Provision Regarding DeepSeek' on February 3, 2025 (updated March 5), indicating that data is stored on servers in China and that Chinese laws apply to that data.
- Age: The service is primarily for adults. Those under 18 should read the terms with a guardian and use it only with their consent.
- Use for training: Inputs and outputs may be used to improve the service after being processed to ensure individuals cannot be identified. You can opt out of this by turning off 'Improve the model for everyone' (English Terms of Service, updated March 27, 2026).
- When publishing outputs: Verify the content yourself and indicate that it was created by AI.
On the other hand, if you run the published weight files on your own company's servers, you can use them without sending inputs to DeepSeek's servers. This is a unique advantage of choosing a model with open weights.
'If you are under 18, start by reading the terms with your guardian before using it. If you are using a PC provided by your company or school, first check the internal or school rules.'
'If you are a new employee, make sure to check if it is a service allowed by your company before entering customer names or confidential figures.'
'...The rule about writing that it was created by AI is something I'm happy about as someone who draws. It saves viewers from confusion, doesn't it?'
Checkpoints before use
- Web and app: The new model V4.1-Flash-1017 is available upon opening. No settings changes are required.
- API: The model name remains 'deepseek-flash'. Prices also remain the same.
- Time slots: Prices are doubled during peak times on weekdays from 10:00 to 13:00 and 15:00 to 19:00 JST. Weekends are off-peak.
- Cache: If you send requests with the same prefix, the input cost becomes 1/50th of the price.
- Search API: $0.75 per 1,000 requests. The free period via development tools lasts until 1:00 AM JST on November 1st.
- Data: Storage is on servers in China. Those under 18 require guardian consent. Use for training can be opted out via 'Improve the model for everyone'.
'I want to read the terms with my guardian first, and then ask how to make a shooting gallery game for the school festival!'
'The price changing by time slot is about the API. Regardless of which day you use it, reading the terms first is the same.'
'...The name stays the same, but the content is new. When I open the app as usual, I wonder if it will look a little different today.'
Summary in one sentence
DeepSeek's new model V4.1-Flash-1017 has been rolled out across the Web, App, and API on the same day. While the API price remains the same, it can be used at half price during off-peak hours, excluding weekday daytime in Japan Standard Time.
Related links (Checked on: October 18, 2026)
- DeepSeek Official X Announcement (2026-10-17, English)
https://x.com/deepseek_ai/status/2111375640717033777
- DeepSeek-V4.1-Flash-1017: Wish-Driven Programming Made Real (DeepSeek API Docs, English)
https://api-docs.deepseek.com/news/news261017
- Change Log (DeepSeek API Docs, English)
https://api-docs.deepseek.com/updates
- Models & Pricing (DeepSeek API Docs, English)
https://api-docs.deepseek.com/quick_start/pricing
- Context Caching (DeepSeek API Docs, English)
https://api-docs.deepseek.com/guides/kv_cache/
- Search & Fetch (DeepSeek API Docs, English)
https://api-docs.deepseek.com/guides/search/
- DeepSeek-V4.1-Flash-1017 Model Card (Hugging Face, English)
https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- DeepSeek Privacy Policy (Japanese)
https://cdn.deepseek.com/policies/ja-JP/deepseek-privacy-policy.html
- DeepSeek Terms of Use (English)
https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html
- Information regarding DeepSeek (Personal Information Protection Commission)
https://www.ppc.go.jp/news/careful_information/250203_alert_deepseek/
