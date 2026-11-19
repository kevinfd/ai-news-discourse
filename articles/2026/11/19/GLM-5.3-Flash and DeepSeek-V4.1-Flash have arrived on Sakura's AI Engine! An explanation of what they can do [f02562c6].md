---
id: "f02562c6df876d51"
title: "GLM-5.3-Flash and DeepSeek-V4.1-Flash have arrived on Sakura's AI Engine! An explanation of what they can do and how much they cost"
url: "https://note.com/masa_cloud/n/nd7635c4cf487?hl=en"
link: "https://note.com/masa_cloud/n/nd7635c4cf487?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-19T02:38:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["伊藤正章｜サバイバルDxクリエイター：荒野のPip-Boy設計局"]
language: "en"
summary: "This announcement in 3 linesOn November 18, 2026, Sakura Internet began offering public previews of two of the latest open models from China on its inference API service, \"Sakura's AI Engine.\" The ..."
tags: []
orgs: ["DeepSeek", "OpenAI", "China"]
topics: ["models & research", "agents & coding", "business & funding"]
content_source: "fulltext"
word_count: 1358
paywalled: false
image: "http://www.bing.com/th?id=ONUT.-jsbSLa94G4jY6Jh16S4pA&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# GLM-5.3-Flash and DeepSeek-V4.1-Flash have arrived on Sakura's AI Engine! An explanation of what they can do and how much they cost

note · 伊藤正章｜サバイバルDxクリエイター：荒野のPip-Boy設計局 · 2026-11-19

GLM-5.3-Flash and DeepSeek-V4.1-Flash have arrived on Sakura's AI Engine! An explanation of what they can do and how much they cost
This announcement in 3 lines
On November 18, 2026, Sakura Internet began offering public previews of two of the latest open models from China on its inference API service, "Sakura's AI Engine."
- The additions are GLM-5.3-Flash (Z.ai/Zhipu AI) and DeepSeek-V4.1-Flash-1017 (DeepSeek)
- Both are multimodal models capable of handling images and text, and are strong in code generation and agent use cases
- Free up to 3,000 requests per month; excess usage is 0.4 yen for input and 4.0 yen for output (per 10,000 tokens each, tax included)
In this article, we will explain what these two models are, how much they actually cost, and how to call them, in that order.
What is "Sakura's AI Engine" in the first place?
Sakura's AI Engine is a shared inference service that allows you to use generative AI models immediately via API. You can call open models using the same syntax as OpenAI without having to prepare your own GPUs.
Its biggest feature is that it is "completed domestically."
- All provided models are hosted by Sakura Internet itself
- Chat data is exchanged only between the user and Sakura, and is not used for model training (Manual)
- Input data is not shared with the model provider (Product Page)
In other words, the point of this announcement is that you can use high-performance models from China without sending data overseas. This makes it easier for companies that were hesitant to use the official APIs of DeepSeek or Z.ai to consider them.
The two added models
Both are "cheap and fast high-end models" with a MoE (Mixture of Experts) architecture that is "huge but only uses a portion of its parameters," capable of handling long texts in the 1-million-token class. On Sakura's AI Engine, they support all three: image input, tool calling, and reasoning.
Source: Sakura's AI Engine Chat Model Specifications, LM Studio, LLM Reference
GLM-5.3-Flash
This is the first "native multimodal" model in Z.ai's GLM-5 series. It did not add image capabilities later; it was trained on images and text together from the start.
By combining sparse and linear attention, Z.ai states that it reduces computational load by 3.0 times and KV cache by 4.4 times compared to the higher-end GLM-5.3. It is suitable for so-called "screen-viewing agents" that work while reading screenshots, documents, and charts.
DeepSeek-V4.1-Flash-1017
This is a low-cost version of the V4.1 family released by DeepSeek in September 2026. The "1017" at the end refers to the weight update version released on October 17th. The official DeepSeek API also switched to this 1017 version on the same day.
DeepSeek explains that it outperforms the previous generation's high-end model, V4 Pro, in both performance and speed (OpenRouter). It compresses the KV cache to about one-fourth of the previous generation, reducing costs for agent use cases that involve long conversations.
How should you choose between them?
These two models are very similar in terms of specifications. A good starting point is to use GLM if you need to process many screens or charts, and DeepSeek for text-based reasoning or long coding tasks. However, since the actual difference depends on the use case, it is best to compare them by sending the same prompt to both using the free tier.
Pricing: Free up to 3,000 requests per month
The pricing is the same for both models, at 40 yen for input and 400 yen for output per 1 million tokens. Since output is 10 times the input, the cost is determined almost entirely by how much you make the model write.
Rough estimate
Let's calculate for a common chat use case with 2,000 input tokens and 500 output tokens per request.
For internal verification or personal development, the free plan's 3,000 requests per month is a sufficient scale for testing.
How does it compare to overseas APIs?
In overseas inference services, GLM-5.3-Flash is offered at around $0.15 for input and $0.50 for output per 1 million tokens (LM Studio). At an exchange rate of 150 yen to the dollar, that is about 23 yen for input and 75 yen for output, so Sakura is more expensive in terms of unit price alone.
It is reasonable to consider that you are paying the difference for "domestic hosting," "not sharing data with the provider," and "yen-denominated billing." The more restricted your business is regarding data location, the less this price difference will matter.
Comparison with the official DeepSeek API
The official DeepSeek API runs the same DeepSeek-V4.1-Flash-1017 under the name deepseek-flash. Sakura's input price is cheaper than the peak price, while the output price is two to four times higher than the original.
The yen conversion is based on 1 dollar = 150 yen. DeepSeek's peak times are weekdays from 01:00 to 04:00 and 06:00 to 10:00 UTC, which corresponds to 10:00 to 13:00 and 15:00 to 19:00 JST. Prices are halved outside of these times and on weekends. Source: DeepSeek API Pricing Page, Sakura's AI Engine Specifications
A significant portion of Japanese business hours overlaps with DeepSeek's peak times. Therefore, for RAG or document summarization tasks with high input volume, the difference between the two is surprisingly small. Conversely, for agent use cases where the same long prompt is sent repeatedly, the original service is significantly cheaper due to cache discounts.
How to use: Just change the model name
Just like with existing models, simply specify preview/GLM-5.3-Flash or preview/DeepSeek-V4.1-Flash-1017 in the request's model field. Since the API is compatible with OpenAI Chat Completions, you can use the OpenAI SDK as is.
- Issue a Sakura AI Engine account token in the control panel
- Set the endpoint https://api.ai.sakura.ad.jp/v1 as the base_url
- Call by entering the new model name in model
Call via text (Python)
from openai import OpenAI
client = OpenAI(
    base_url="https://api.ai.sakura.ad.jp/v1",
    api_key="発行したアカウントトークン",
)
res = client.chat.completions.create(
    model="preview/DeepSeek-V4.1-Flash-1017",
    messages=[{"role": "user", "content": "FizzBuzzをPythonで書いて"}],
    max_tokens=1024,
)
print(res.choices[0].message.content)
Have it read images
res = client.chat.completions.create(
    model="preview/GLM-5.3-Flash",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "このグラフから読み取れる傾向を3点で"},
            {"type": "image_url", "image_url": {"url": "https://example.com/chart.png"}},
        ],
    }],
    max_tokens=1024,
)
The output length must be specified with max_tokens. Parameters not in the compatibility table, such as top_p, stop, and seed, will be ignored without throwing an error, so be careful not to use them under the assumption that they are working (specifications).
Points to note for "Public Preview"
It is explicitly stated that models with names starting with preview/ may have their specifications changed without notice and may be discontinued (specifications). It is safest to treat this as a "trial and evaluation phase" for now.
- If incorporating into a production service, make sure the model name can be switched via settings
- A 400 error will occur if the total of input tokens and max_tokens exceeds approximately 1.04 million tokens
- Since these are models originating from China, verify in advance for your intended business use whether there is a possibility of different response tendencies regarding political topics, etc.
- License information can be checked on the provided model license page
Summary
With this addition, Sakura's AI Engine can now use the latest generation of models capable of handling 1 million-token-class long text and images. While the unit price is higher than overseas APIs, it is a strong option for the need to "use the latest open models without moving data out of the country." First, try it out with the free 3,000 requests per month to see if it fits your use case.
Reference Links
- [Sakura's AI Engine] Notice of Public Preview Availability for "GLM-5.3-Flash" and "DeepSeek-V4.1-Flash-1017"
- Sakura's AI Engine Chat Generation Model Specifications
- Sakura Cloud Manual (AI Engine)
- Sakura's AI Product Page
- GLM-5.3-Flash (LM Studio)
- DeepSeek V4.1 Flash (LLM Reference)
- DeepSeek V4.1 Flash (OpenRouter)
▼ Learn, run, and use DeepSeek safely in Japanese. 
On the practical learning site "deepseek.ac", we have published materials that allow you to verify the contents of reference books through operation and implementation.
▼ Reference Books and Problem Sets 
"Guide to Safe DeepSeek Operation" 
"Guide to Safe DeepSeek Operation: 70-Question Problem Set"
