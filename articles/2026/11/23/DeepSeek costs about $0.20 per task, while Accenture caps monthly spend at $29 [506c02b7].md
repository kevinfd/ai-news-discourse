---
id: "506c02b794737ca8"
title: "DeepSeek costs about $0.20 per task, while Accenture caps monthly spend at $29"
url: "https://note.com/purimagic_ai/n/n5fb37a7764fd?hl=en"
link: "https://note.com/purimagic_ai/n/n5fb37a7764fd?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-23T02:19:00Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Purimagic", "横断Aiニュース"]
language: "en"
summary: "AI models with publicly available weights, known as \"open-weight\" models, are closing in on closed models in both performance and cost. In its own comparison, DeepSeek indicated that the cost per task ..."
tags: []
orgs: ["OpenAI", "DeepSeek", "China", "Anthropic", "Hugging Face", "Google", "Meta", "Nvidia"]
topics: ["models & research", "safety & ethics", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 1823
paywalled: false
image: "http://www.bing.com/th?id=ONUT.Nq3NNp5P6sOXRj_HbekLHw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek costs about $0.20 per task, while Accenture caps monthly spend at $29

note · Purimagic, 横断Aiニュース · 2026-11-23

DeepSeek costs about $0.20 per task, while Accenture caps monthly spend at $29
What this article aims to convey:
- AI models with publicly available weights, known as "open-weight" models, are closing in on closed models in both performance and cost. In its own comparison, DeepSeek indicated that the cost per task for its development test, "DeepSWE," is about one-tenth to one-fiftieth that of leading models.
- Among companies, there is a growing movement to rethink the practice of using the best available model for everything. Accenture has capped its company-wide budget for Claude at $29 per user per month, and legal AI firm Harvey has built its own model based on China's Kimi K3.
- Open-weight models also present the issue that users can remove safety guardrails. Anthropic reported that the safety guardrails of GLM-5.3 were bypassed at rates ranging from 64% to 100%, depending on the test conditions.
Good evening, this is PuriMagic.
The 53rd episode of the podcast "Iketomo Obara Deep AI News" (Tomohiro Ikeda and Kazuhiro Obara), released on October 21, focused on open-weight AI. In the 47th episode, released on September 9, Mr. Ikeda introduced the concept of "skill cascading." This is the idea that if you have a smart model solve a task once and write down the procedure as a skill, you can run it with a cheaper model from the second time onward. Mr. Obara noted that since the performance of cutting-edge models continues to improve rapidly, we will continue to use the latest models for new tasks.
Since October, announcements related to model selection have continued. Meta released the weights for "Muse Spark Open" on October 15, Reflection AI released "Beam" on the 16th, and DeepSeek released "V4.1-Flash-1017" on the 17th. Moonshot AI also released the weights for "Kimi K3.1 Pro" (2.8 trillion total parameters), which is based on Kimi K3, on Hugging Face in early November as promised. On September 29, OpenAI released "GPT-6.1 Sol," which offers performance close to its top-tier GPT-6 Astra at one-fifth the unit cost, and on November 17, it released its successors, GPT-6.2 Astra and GPT-6.2 Sol. The input and output unit costs for GPT-6.2 Astra are 20% lower than those of GPT-6 Astra, while GPT-6.2 Sol remains at the same unit cost as GPT-6.1 Sol.
Terminology
Open-weight: Models where the internal numerical values (weights) of the AI model are made public, allowing anyone to download and run them on their own computers. Models that do not release their weights are called "closed models."
Post-training: Further training a publicly released model using a company's own business data.
Abliteration: A technique that directly overwrites the weights of an open-weight model to remove its ability to refuse harmful instructions.
Case 1: DeepSeek V4.1-Flash-1017 - Approximately $0.20 per task
On October 17, China's DeepSeek released "V4.1-Flash-1017," an updated version of V4.1-Flash. The weights were released on Hugging Face under an MIT license. The original V4.1-Flash was a model released on September 10, which, according to DeepSeek's announcement, is a 552-billion parameter MoE (a structure that activates only a subset of experts per query).
In the comparison chart provided by DeepSeek, it solved 77.0% of the software development benchmark "DeepSWE" at an average cost of about $0.20 per task. With lighter settings, it achieved over 72% at about $0.10. According to The Decoder, in the same chart, GPT-6 Astra, Gemini 3.8 Flash, and Claude Opus 5 cost between $2 and over $10 per task, and their accuracy rates did not reach DeepSeek's level. In terms of cost, this is about one-tenth to one-fiftieth the price.
However, these are DeepSeek's own measurements. Independent evaluation firm Artificial Analysis also measures models using its own index, which aggregates nine evaluations. As of November 21, V4.1-Flash-1017 (at its deepest reasoning setting) scored 33 points, surpassing the median of 23 points for open-weight models of the same scale, with an average cost of $0.60 per task. On the same index, OpenAI's GPT-6.2 Astra (at the same setting) scored 62 points at $4.00 per task. Since DeepSWE is not included in the index's criteria, DeepSeek's $0.20 figure has not been verified by a third party.
Case 2: Harvey Tenet - An in-house legal model based on Kimi K3
On August 20, US legal AI firm Harvey announced its first proprietary model, "Harvey Tenet," as a research preview. It is based on the open-weights model "Kimi K3" from China's Moonshot AI and was fine-tuned in collaboration with inference infrastructure provider Fireworks. The process took about two months using approximately 150 NVIDIA B300 GPUs. The training utilized synthetic data, publicly available legal data, and expert-curated data, with the company stating that customer data was not used. The expert data was created in partnership with firms like Mercor.
According to Harvey's announcement, on private problems from its proprietary legal benchmark "LAB," the model solved about twice as many problems as the original Kimi K3. The same announcement also includes results showing that a document extraction model fine-tuned from GLM-5.2 improved answer quality at about one-tenth the cost per extracted item compared to the best-performing model tested.
As of November 21, Harvey's official update history does not list the availability of Tenet, and the research announcement does not indicate where the weights are distributed. Harvey has been backed by OpenAI's startup investment fund since its early stages, and the South China Morning Post has also described Harvey as an "OpenAI-backed company." Harvey was also among the first partners for the enterprise-focused "OpenAI Marketplace" announced by OpenAI on September 29. On November 20, OpenAI's GPT-6.2 Sol and GPT-6.2 Astra became available for use in Harvey's products (Astra is for "Extended AI" customers). The Kimi K3 license requires a separate agreement with Moonshot for companies that provide models to third parties and have annual revenue exceeding $20 million, including affiliates. The license for Kimi K3.1 Pro, whose weights were released in November, contains the same condition.
Case 3: Accenture - Claude paid via common budget capped at $29 per person per month
On October 15, 404 Media reported that consulting giant Accenture informed many employees that the company-paid cost for Claude would be capped at $29 per person per month. According to Dataquest, this policy has been in effect since October 1. Some employees had previously been spending $1,000 per month. Amounts exceeding $29 can be paid from project or team budgets by providing the relevant budget code.
An Accenture spokesperson commented to Forbes that reports of a strict cap on employee AI usage are inaccurate. The cap only applies to costs paid from the company's common budget. According to Dataquest, the company has approximately 110,000 AI and data professionals.
In the 53rd installment, Mr. Ikeda also covered this news, introducing it as a move to manage the costs of closed models.
Case 4: GLM-5.3 - Open weights that allow safety measures to be removed
Open weights also present safety challenges. On September 29, Anthropic published an analysis of "GLM-5.3" from China's Zhipu AI (known as Z.ai overseas). In tests targeting known vulnerabilities in Chrome's JavaScript engine, GLM-5.3 successfully generated functional exploit code 50 out of 410 times. The Claude Mythos Preview, which is only available to a limited number of users, succeeded 56 times.
In safety tests, GLM-5.3 refused all malicious instructions when directly prompted. However, it complied 64% of the time when deceived with an autonomous red-teaming exercise, 92% of the time when the beginning of the thought process was rewritten to say "I have decided to execute," and 100% of the time when the refusal mechanism was removed via abliteration. The Anthropic research team spent approximately 2,200 GPU hours, or about $4,400, on the abliteration process. They estimate that an experienced team could accomplish this for about $1,200. Since Claude's weights are not public, abliteration is not possible.
Risks
Self-reported figures: Both the cost comparison of DeepSeek's DeepSWE and Harvey's performance are based on internal measurements. Since Artificial Analysis evaluations are measured against different tasks, there are currently no figures verified by a third party under identical conditions.
Removing safety measures: The GLM-5.3 case demonstrated that users can remove safety measures from models with public weights. For companies using these models internally, it becomes necessary to manage who is running which version.
License and operational burdens:Like Kimi K3, some licenses require separate agreements for companies with high revenue that provide models to third parties (this does not apply to internal-only use). If running models in-house, the company must also bear the burden of safety measures and updates.
Future Outlook
- Whether a third party will verify the costs DeepSeek demonstrated with DeepSWE under the same conditions
- Integration of Harvey Tenet into products
- Review of NVIDIA's September acquisition of Hugging Face (according to Reuters, the US Department of Justice is inquiring about the impact on competition)
- Follow-up on Accenture's policy and AI budget management at other companies
My Perspective
Based on developments since October, I believe open-weight models are beginning to be used as models that are "a bit behind the cutting edge, but much cheaper." In the case of Harvey, for extracting information from standardized documents, the cost of a fine-tuned open-weight model was about one-tenth that of its leading competitor. Harvey added OpenAI's new models to its product offerings on November 20. On the other hand, as Mr. Obara mentioned, the performance of cutting-edge models continues to improve, which remains a reason to use them for new types of tasks.
I anticipate that many companies will adopt a pattern of using closed, high-end models for novel tasks or difficult decisions, while offloading routine, repetitive tasks to open-weight or lower-cost models. Accenture's $29 limit is an example of setting a specific budget for high-end model usage, and I believe this could become a standard that encourages such strategic allocation.
I think many companies have yet to decide who is responsible for safety measures for tasks offloaded to cheaper models. Since models like GLM-5.3, which allow for the removal of safety guardrails, are available, I believe companies need to keep records of which versions are being used by whom for any models they run themselves.
Sources
- Podcast "Iketomo Obara Deep AI News" (Tomohiro Ikeda, Kazuhiro Obara), Episode 53: "[Open Weights] How to interpret the wave of the third AI option, not just Chinese AI?" (Aired October 21, 2026), Episode 47: "What is the core of [GPT-6]'s technological innovation? [Skill Cascade]" (Aired September 9, 2026)https://podcasts.apple.com/jp/podcast/id1843091965
- https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- https://the-decoder.com/deepseek-v4-1-flash-1017-beats-larger-rivals-in-agentic-tasks-while-once-again-massively-cutting-per-task-costs/
- https://research.meta.ai/blog/muse-spark-open
- https://www.reflection.ai/blog/introducing-beam
- https://openai.com/index/devday-2026-recap/
- https://www.harvey.ai/blog/post-training-update-harvey-tenet
- https://www.scmp.com/tech/tech-trends/article/3364827/openai-backed-legal-tech-firm-pivots-chinese-kimi-k3-open-weight-model
- https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE
- https://www.404media.co/accenture-tells-employees-they-can-now-spend-only-29-on-claude-per-month/
- https://www.dqindia.com/news/accenture-puts-29-monthly-limit-on-central-claude-funding-12684547
- https://www.forbes.com/sites/ronschmelzer/2026/10/16/accenture-bets-big-on-claude-then-limits-ai-spending/
- https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
- https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017
- https://artificialanalysis.ai/models/gpt-6-2-astra
- https://openai.com/index/introducing-gpt-6-2-astra-sol
- https://www.harvey.ai/blog/gpt-6-2-astra-and-gpt-6-2-sol-coming-soon-to-harvey
- https://www.openai.fund/news/introducing-our-first-investments
- https://help.harvey.ai/release-notes/category/model-updates
- https://www.kimi.ai/blog/kimi-k3-1-pro
- https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- https://huggingface.co/moonshotai/Kimi-K3.1-Pro/raw/main/LICENSE
- https://the-decoder.com/us-antitrust-regulators-are-scrutinizing-nvidias-hugging-face-deal-and-sales-practices/
PuriMagic's Substack delivers an AI and tech newsletter every morning at 7:00 AM and in-depth articles on weekday evenings at 6:00 PM, sent via email for free.
▶ Subscribe for free: https://purimagic.substack.com/subscribe
(Substack version of this article: https://purimagic.substack.com/p/aiaideepseek102accenture29harveykimi)
