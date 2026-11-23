---
id: "7d97027286acb74e"
title: "AI Model Retirement and Price Hike Calendar: 11/30 to 1/14"
url: "https://note.com/cute_oxalis223/n/n5cf2e3fae408?hl=en"
link: "https://note.com/cute_oxalis223/n/n5cf2e3fae408?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-22T23:25:00Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["かんざき"]
language: "en"
summary: "You cannot always rely on the same AI model forever. From Monday, November 30, to Thursday, January 14, of next year, major AI model retirements and price hikes will occur across six different ..."
tags: []
orgs: ["OpenAI", "Google", "Anthropic", "Microsoft", "Amazon", "xAI"]
topics: ["models & research", "policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 1183
paywalled: false
image: "http://www.bing.com/th?id=ONUT.BY3L2hnI0P8q0NCj3xVSag&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# AI Model Retirement and Price Hike Calendar: 11/30 to 1/14

note · かんざき · 2026-11-22

AI Model Retirement and Price Hike Calendar: 11/30 to 1/14
You cannot always rely on the same AI model forever. 
From Monday, November 30, to Thursday, January 14, of next year, major AI model retirements and price hikes will occur across six different deadlines. Some models will return errors upon calling, some will be silently swapped for other models, and some will remain the same model but with their prices doubled. 
These changes primarily affect APIs and developer-focused models; there is little direct impact on conversations within the ChatGPT or Gemini apps. However, for those who use APIs for work, it is worth checking these details now. 
Dates are based on announcements from each company. Please check the respective retirement pages for each company for exact times and time zones.
November 30: Claude Sonnet 4.5 removed from API
On September 30, Anthropic marked Claude Sonnet 4.5 as "deprecated." On November 30, it will be retired from the API, and requests to that model ID will return errors. It will not automatically switch to another model. 
The successor is Claude Sonnet 5.5, and the price will drop from $3/$15 to $2/$10. However, specifying temperature, top_p, or top_k will return a 400 error. Since the token count increases by about 30% even for the same text, the bill may not decrease as much as expected. 
Deadlines also vary by route. It can be used via Amazon Bedrock until April 8, 2027. Checking the deadline for your specific route is the first priority.
December 1: Gemini faces both price hikes and "swaps"
December 1 is the day when both price hikes and swaps occur. 
Google is doubling the price of Gemini 4 Carbon and Argon from $2/$10 to $4/$20. There are no plans to raise the price of Hydrogen ($1.50/$7.50) in the same generation, making it an alternative for switching. 
On the same day, requests to 2.5 Pro will be automatically sent to 3.8 Flash, and requests to 2.5 Flash will be automatically sent to 3.5 Flash-Lite. It will not result in an error, and the code will continue to run. However, the model providing the answers will change. 
This is the pitfall. Those who were using Pro will find themselves downgraded to Flash-level performance despite intending to choose a model with strong reasoning capabilities. While the cost will actually decrease during December ($1.25/$10 → $0.75/$3.75), the price of 3.8 Flash itself will double on January 1. The low price in December is only for a limited time. 
Note that 2.5 Flash-Lite is not subject to retirement, and new users are already unable to select the 2.5 series.
December 11: OpenAI to end GPT-5 and o3 via API
As notified on June 11, OpenAI will end the provision of the GPT-5 and o3 series via API on December 11. This affects six models: gpt-5, gpt-5-mini, gpt-5-nano, gpt-5-pro, o3, and o3-pro. Snapshot versions with specified dates will also end on the same day. 
Successors are GPT-6.1 Sol, GPT-6.1 Terra, and GPT-6 Luna. Some prices will increase, such as gpt-5 from $1.25/$10 to Sol at $2/$10, and gpt-5-mini from $0.25/$2 to Terra at $1/$5. 
This concerns the API and is separate from usage on the ChatGPT screen. Services that call the API behind the scenes must update their model IDs by December 11, or they will stop working from that day on.
December 14: GitHub Copilot to retire 6 models
On November 13, GitHub announced that it would retire six models from Copilot on December 14. The affected models are Claude Fable 5, Claude Haiku 4.5, Gemini 3.8 Flash, Gemini 4 Argon, Grok 4.6, and Kimi K3. Successors are Fable 5.2, Haiku 5.5, Gemini 4 Hydrogen, Gemini 4 Carbon, and Grok 4.7, respectively; the successor for Kimi K3 has not been announced. 
Argon, which will see a price hike on December 1, will disappear from Copilot two weeks later.
January 1: Gemini 3.8 Flash price to double
Gemini 3.8 Flash will be available at an introductory price of $0.75/$3.75 starting December 1, but will double to $1.50/$7.50 starting January 1. 3.6 Flash will also double on the same day. 
Those who switched from 2.5 Pro to 3.8 Flash may feel it is cheap in December, but their bill will double in January. From January, 3.8 Flash will cost the same as Hydrogen.
January 14: OpenAI to end GPT-4o series snapshots
On January 14, OpenAI will end the provision of snapshots for GPT-4o, GPT-4o-mini, GPT-4.1, and GPT-4.1-mini via API. Affected models are gpt-4o-2024-08-06, gpt-4o-2024-11-20, gpt-4o-mini-2024-07-18, gpt-4.1-2025-04-14, and gpt-4.1-mini-2025-04-14, with the successor being GPT-6 Luna. 
This also concerns the API and is separate from usage on the ChatGPT screen. Code that continues to specify old snapshots will stop working from January 14.
Categorizing into three patterns
The six deadlines can be divided into three types based on what happens.
- Errors occur: Sonnet 4.5, GPT-5/o3, GPT-4o series. Calls will simply fail. They will not work unless you migrate.
- Silent model swaps: Gemini 2.5 Pro/Flash. Because they do not return errors, they are harder to notice. The quality of answers and behavior will change.
- Price changes only: Gemini 4 Carbon/Argon, Gemini 3.8 Flash. The model remains the same, but the bill will double.
The scariest thing is not the ones that "return errors," but the ones that "change without you noticing." Swaps keep running while only the content changes, and the bill will double just as you get used to the low prices in December.
What should I do?
There are five main things to do.
- List the model IDs you are using. This includes code, configuration files, and settings in no-code tools.
- Check the deadlines for your specific path. It differs depending on whether you are using direct API access or going through Bedrock, Vertex AI, or Azure.
- Test with successor models. You won't know how Gemini 2.5 replacements and Claude parameter limits behave until you actually run them.
- Estimate your costs for December and January. Carbon and Argon will double in price starting December 1st, and 3.8 Flash will double starting January 1st.
- For models that can be switched, manually update the model IDs yourself. If you rely on automatic switching, you won't know which model is providing the answers.
Summary
From November 30th to January 14th, there are 6 deadlines and 3 patterns. The dividing line is whether you get an error or if things change without you noticing. 
If you leave the December 1st switch and the January 1st price hike alone, both your billing and your answers will change. Start by listing the model IDs you are currently using. Deadlines only favor those who are aware of them. 
(Prices and deadlines are based on company announcements as of November 23, 2026. Rates are in USD per 1 million tokens; JPY conversions will fluctuate with exchange rates. Please check the official pages of each company for final confirmation.) 
Sources: Anthropic "Model deprecations", Google "Gemini API pricing", "Gemini API deprecations", "Gemini API changelog (2026-11-02)", "Introducing Gemini 4 Hydrogen", OpenAI "Deprecations | OpenAI API", GitHub Changelog (2026-11-13). Verification date: November 23, 2026.
