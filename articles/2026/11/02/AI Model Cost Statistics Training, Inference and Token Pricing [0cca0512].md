---
id: "0cca05124986f23f"
title: "AI Model Cost Statistics: Training, Inference and Token Pricing"
url: "https://coincentral.com/ai-model-cost-statistics-2026"
link: "https://coincentral.com/ai-model-cost-statistics-2026"
source: "CoinCentral"
domain: "coincentral.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-02T02:23:00Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Trader Edge"]
language: "en"
summary: "AI model cost statistics for 2026: training costs from $670 to $192 million, token prices, and why the cost of AI capability falls about 13x a year."
tags: []
orgs: ["DeepSeek", "OpenAI", "Anthropic", "Google", "Meta", "Nvidia", "xAI"]
topics: ["models & research", "business & funding", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 2228
paywalled: false
image: "http://www.bing.com/th?id=ONUT.FfUGyuMn1BVIVnQf7VtMTw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# AI Model Cost Statistics: Training, Inference and Token Pricing

CoinCentral · Trader Edge · 2026-11-02

Artificial intelligence is getting more expensive to build and much cheaper to use. Both trends are happening at the same time.
Training a frontier AI model can cost tens or hundreds of millions of dollars in computing. Epoch AI estimates that the hardware and energy cost of these training runs has grown about 2.4 times per year.
After a model is trained, the picture flips. Epoch AI estimates that the price of reaching a fixed level of AI performance has fallen about 47% every quarter since 2023, which is roughly 13 times per year.
This article collects the main figures on training costs, inference costs and token pricing. The data comes from Epoch AI, Stanford, DeepSeek, OpenAI, Anthropic and Google. Prices are standard published rates as of October 2026.
AI Model Cost Statistics at a Glance
These are the main figures covered in this article.
- Frontier AI training costs have grown about 2.4 times per year.
- Epoch AI says the largest training runs could pass $1 billion around 2027 if the trend continues.
- GPT-4 training compute is estimated at about $79 million.
- Gemini 1.0 Ultra is estimated at about $192 million.
- Llama 3.1 405B is estimated at about $170 million.
- Grok-2 is estimated at about $107 million.
- DeepSeek reported $5.576 million for the official DeepSeek-V3 training run, which left out earlier research and staff costs.
- Hardware makes up about 47% to 67% of frontier model development costs.
- Research and development staff make up another 29% to 49%.
- Energy accounts for only about 2% to 6%.
- The cost of equal AI performance falls about 47% per quarter, or about 13 times per year.
- GPT-3.5-level inference fell more than 280 times in cost between late 2022 and late 2024.
- GPT-6 Luna and Claude Haiku 5.5 cost $0.10 per million input tokens and $0.50 per million output tokens.
- Cached tokens can be 90% to 95% cheaper than ordinary input tokens on some APIs.
The gap between rising training costs and falling usage costs sits at the center of AI economics. The rest of this article looks at each side in turn.
How Much Does It Cost to Train an AI Model?
There is no single answer. Costs run from a few hundred dollars for early research models to hundreds of millions of dollars for frontier systems.
Stanford’s AI Index, using estimates developed with Epoch AI, tracks how training costs have changed. The table below shows selected models.
Stanford points out that these figures mostly estimate the computing resources used. They do not capture the full economic cost of building each model.
Even so, the change over seven years is large. The original Transformer cost less than $1,000 in estimated compute to train. GPT-4 cost about $79 million, which is more than 100,000 times as much.
Not every model follows the upward line. Llama 2 70B, at about $3 million, cost less than GPT-3 at $4 million and far less than PaLM 540B at $12 million. Model size, chip type and training method all change the bill.
Frontier Training Costs Grow 2 to 3 Times Per Year
Epoch AI studied dozens of major AI systems. It estimates that the amortized hardware and energy cost of frontier training runs has grown about 2.4 times per year since 2016.
A separate method based on cloud-compute prices found a similar rate of 2.6 times per year. Two different approaches pointing to the same range gives the estimate more weight.
If the trend continues, Epoch projects that the largest frontier models could cross $1 billion per training run around 2027. Stanford noted in 2026 that industry estimates for new frontier systems now range from hundreds of millions of dollars toward $1 billion per iteration.
That does not mean every future leading model will cost a billion dollars. Mixture-of-experts designs, better data, improved algorithms and cheaper hardware can all cut the compute needed for a given level of performance.
DeepSeek showed how large that difference can be, as the next section explains.
DeepSeek-V3 Training Cost
DeepSeek drew wide attention after it reported a training compute cost of about $5.576 million for DeepSeek-V3. Its technical report says the full official training process used about 2.788 million Nvidia H800 GPU-hours.
At an assumed rental price of $2 per GPU-hour, that works out to the $5.576 million figure. The table shows how the cost was split.
This number is often misread. It is not the total cost of developing V3. DeepSeek said it left out earlier research, architecture experiments, ablation studies, data work and other development costs.
For that reason, the figure cannot be compared directly with estimates that include wider R&D spending. A fair comparison needs the same scope on both sides.
What the figure does show is that design and engineering choices can sharply cut the cost of a final large training run. That finding matters for the whole industry.
Compute Is Only Part of the Cost
Building a frontier model takes more than GPUs. Epoch AI estimates how the total development cost splits across three main areas.
Energy is the smallest share in Epoch’s analysis. Hardware and people make up most of the bill.
Other costs can include data acquisition, data cleaning, failed experiments, post-training and reinforcement learning. Safety testing, model evaluations, networking, storage and data-centre facilities add to the total.
Because of this, the headline cost of a final training run can understate what it takes to build a competitive frontier model. The gap between the two numbers can be large.
Inference and Token Pricing
Training vs inference
Training creates a model. Inference runs it. Companies pay for inference each time someone uses the model.
If millions of people use a model every day, total inference spending can pass the cost of the original training run. This matters more as AI moves into coding agents, AI search, customer service, voice assistants, video analysis and business automation.
A chatbot reply of a few hundred tokens is cheap. A coding agent that reads millions of tokens, calls tools many times and runs for hours uses far more computing.
Current token prices
Most commercial AI APIs charge by the token. A token is a small piece of text, and one million tokens equals hundreds of thousands of English words, although the exact ratio varies.
*Gemini 4 Argon’s $2 and $10 pricing is introductory through November 30, 2026. Google says standard pricing rises to $4 input and $20 output afterward.
These are list prices. They are not the providers’ own cost of running the models.
Small Models vs Frontier Models
OpenAI’s GPT-6 Luna charges $0.10 per million input tokens and $0.50 per million output tokens. Anthropic’s Claude Haiku 5.5 has the same headline price for prompts under 100,000 tokens.
Anthropic released Haiku 5.5 in October 2026. It says the model costs about 75% less to run than Haiku 4.5 on average.
At these rates, a business that sends 100 million input tokens to a $0.10 model pays only $10. Ten million output tokens at $0.50 per million cost another $5. Output costs more because models create tokens one at a time, which takes more compute.
Cheap models do not suit every task. Frontier reasoning systems need much more compute, and providers charge more for them.
Anthropic lists Claude Opus 5.5 at $4 per million input tokens and $20 per million output tokens. That is 40 times the output price of Haiku 5.5.
This gives AI agents a clear reason to route simple tasks to small models. The expensive models can then be saved for hard reasoning.
AI Inference Costs Have Fallen Sharply
Stanford’s AI Index gives a clear example. In November 2022, GPT-3.5-level performance on the MMLU benchmark cost about $20 per million tokens.
By October 2024, Gemini 1.5 Flash-8B reached the same benchmark level for $0.07 per million tokens. That is a drop of more than 280 times in under two years.
Stanford found that inference prices fell between 9 times and 900 times per year, depending on the task measured. The range is wide because each benchmark and each performance level has its own price history.
The cause is not only lower profit margins. AI models and the hardware that runs them have become far more efficient.
The Price of Equal AI Capability Falls 13 Times Per Year
Epoch AI’s September 2026 research goes beyond raw token prices. It measures what it costs to reach a fixed level of model performance.
Epoch estimates that this cost has fallen about 47% every quarter since 2023. Over a full year, that adds up to a drop of about 13 times.
The math is simple. If the price falls 47% each quarter, 53% of it remains. After four quarters, about 7.9% remains, which is close to one thirteenth.
Epoch says this decline is faster than earlier major technology cost curves. Those include DNA sequencing, general computing, lithium-ion batteries and electricity costs.
The rate differs by task, as the table shows.
Hardware and Software Make AI Cheaper to Run
AI inference benefits from steady gains in chip economics. Stanford reports three yearly trends for machine-learning hardware.
Modern GPUs also use lower-precision number formats, better memory systems and faster links between chips. Each change lets a data centre do more work for the same money.
Software adds to the gains. Techniques such as quantization, distillation, sparsity, mixture-of-experts designs, speculative decoding, continuous batching and better compilers all reduce the compute needed per answer.
As a result, the same amount of AI capability can be delivered with fewer computing resources over time.
Caching and Batch Processing Cut Costs Further
Modern APIs increasingly discount repeated information. Picture an AI agent that sends the same 100-page company handbook with every request. A provider can cache that text instead of processing it again each time.
OpenAI charges $0.20 per million cached input tokens for GPT-6 Sol, compared with $2 for ordinary input. That is a 90% discount. Google’s Gemini 4 Argon currently discounts eligible implicitly cached input by 95%.
Users who do not need instant answers can also pay less. OpenAI prices Batch and Flex processing for GPT-6 Sol at about 50% of standard rates.
Batch processing suits document classification, overnight analysis, data extraction, large-scale summarization and offline evaluations.
AI pricing is starting to look like cloud computing. Customers pay different rates depending on speed, reliability and how flexible the workload is.
Cost per Task and Total AI Spending
Why price per token can mislead
A model that costs $1 per million tokens is not always cheaper than one that costs $2. Suppose the first model needs 5 million tokens to finish a task, while the second finishes it with 1 million.
The first model costs $5 for the task and the second costs $2. Reasoning models make this check more important because they can produce large numbers of internal thinking tokens, and some of those are billed.
Anthropic says Claude Sonnet 5.5 uses fewer tokens per task than Sonnet 5. That can make it cheaper in real workflows, even where list prices look similar. Businesses increasingly track the cost per successfully completed task instead of only the cost per million tokens.
What keeps prices falling
Three forces push inference costs down. They are more efficient hardware, more efficient model designs and strong competition between providers.
OpenAI cut GPT-6 Sol and Luna API prices by about 50% compared with their GPT-5.6 promotional counterparts, while also improving capability. Anthropic says Haiku 5.5 costs about 75% less per typical workload than Haiku 4.5. Google is also competing on token pricing.
The result is that uses of AI that were too costly two or three years ago can now fit inside ordinary products.
Falling costs can raise total spending
Cheaper AI does not always mean lower industry spending. A company might not automate one million customer chats if each one costs $1. At one cent each, it might automate all of them.
This looks like the Jevons paradox, where more efficient use of a resource leads to more total use. It may help explain why the largest cloud companies keep spending hundreds of billions of dollars on AI data centres while the cost of each query falls.
The Bottom Line
AI economics are moving in two directions at once. At the frontier, training costs have grown fast.
GPT-4 needed an estimated $79 million of training compute. Gemini 1.0 Ultra needed about $192 million and Llama 3.1 405B about $170 million. Epoch AI estimates that frontier training costs have grown about 2.4 times per year.
Once models are available, the cost of using them is falling quickly. GPT-3.5-level inference dropped from about $20 per million tokens in 2022 to $0.07 in 2024.
Newer Epoch research puts the fall in the cost of a fixed level of AI performance at about 47% per quarter, or about 13 times per year. By October 2026, small commercial models cost as little as $0.10 per million input tokens and $0.50 per million output tokens.
In short, the most advanced models cost more to build, while the output of those models costs less to use. If that continues, the effect of AI may depend less on what one model costs to train and more on what happens when billions of people and businesses can reach capable AI at prices near ordinary cloud software.
