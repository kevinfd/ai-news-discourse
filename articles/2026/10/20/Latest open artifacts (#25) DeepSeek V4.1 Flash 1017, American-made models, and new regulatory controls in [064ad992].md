---
id: "064ad9927d51a30c"
title: "Latest open artifacts (#25): DeepSeek V4.1 Flash 1017, American-made models, and new regulatory controls in the US & China"
url: "https://interconnects.ai/p/latest-open-artifacts-25-deepseek"
link: "https://interconnects.ai/p/latest-open-artifacts-25-deepseek"
source: "Interconnects"
domain: "interconnects.ai"
source_type: "newsletter"
collector: "rss"
date: "2026-10-20T17:04:21Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Florian Brand"]
language: "en"
summary: "The geopolitics of open-weight AI are accelerating again this fall, as we would expect with the risks of all AI systems (open and closed) rising rapidly. We’ve seen many news items in the last week showing both the U.S. and Chinese governments positioning themselves for some controls on open models. MOFCOM, the Ministry of Commerce of the People’s Republic of China, released a policy proposal…"
tags: []
orgs: ["DeepSeek", "China", "Nvidia", "OpenAI"]
topics: ["models & research", "policy & regulation", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 905
paywalled: false
image: "https://substackcdn.com/image/fetch/$s_!ptGw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd500e8ff-94e8-4cf5-b99d-5d9aac7f0a8a_1024x768.png"
discussion_url: null
score: null
comments: null
community: null
---

# Latest open artifacts (#25): DeepSeek V4.1 Flash 1017, American-made models, and new regulatory controls in the US & China

Interconnects · Florian Brand · 2026-10-20

The geopolitics of open-weight AI are accelerating again this fall, as we would expect with the risks of all AI systems (open and closed) rising rapidly. We’ve seen many news items in the last week showing both the U.S. and Chinese governments positioning themselves for some controls on open models.
- MOFCOM, the Ministry of Commerce of the People’s Republic of China, released a policy proposal (it’s not yet a law) that would require frontier AI models and some other technologies to get pre-approval from the government before they can be shared internationally. We found the reaction to this to be overblown – as the document states that open-source technologies will be set up for automatic approvals – but many in geopolitical circles say this is a big deal because it proposes a regulatory framework that could be used in the future to regulate China’s AI industry. 
Others we trust on this issue say this proposal could be more about preventing issues like the sale of Chinese startup Manus to Western companies, rather than being about frontier AI models. Either way, the wheels of control are moving around AI, and open-weight models are not free from any influence.
- The Department of Homeland Security (DHS) released an order on DeepSeek, which restricts DeepSeek itself, as a company, and DeepSeek’s models, as a technology platform, from being a vendor in federal civilian procurement. It is not clear how this will relate to finetuned models or models trained on the outputs of DeepSeek (e.g., Nvidia’s Nemotron models have long relied heavily on DeepSeek models in their training recipes – will they be banned?), but this is an expected action and reinforces the need for a domestic open model ecosystem. 
Other model makers in China, such as Zhipu AI, makers of GLM, are already on the Entity List under Commerce/BIS, which restricts their access to American technology.
DeepSeek followed the above news up by releasing their internal inference stack publicly, DeepInfer, which is likely far more efficient than existing open-source tools like vLLM/SGLang for their models. Estimates point to DeepSeek making up to 90% gross margin when selling tokens on this inference stack. It is well-known that the top AI labs have much more inference-efficient tools internally, and this is the first time we’ve seen a leading lab share them. Inference companies will be quick to adopt these tools, which will drive prices for DeepSeek’s models down across the ecosystem (or margins up). While not an open model or dataset, we consider this release to be one of the bigger open-source AI artifacts in the last few months.
As of writing this, Kimi K3.1 is rumored to be released very soon, with metadata associated with it starting to appear in public libraries. Exciting times!
You can view the models in this email, and all previous issues, on our Artifacts Hub. It includes commentary and other ecosystem metadata.
Our Picks
- MiMo-V2.6-Pro-RL by XiaomiMiMo: an update for Mimo, which reuses the same bases as MiMo V2.5, but used a lot more resources on RL training. They also release an in-depth tech report, as well as some of the used environments, which is rare at this scale. The final model from this recipe, V2.6-Pro, is the top open model on Artificial Analysis’s ranking today, and the scaled RL runs came with a fun live dashboard of training. We’ve been fans of Xiaomi for months now, and their efforts are bearing fruit.
- DeepSeek-V4.1-Flash-1017 by deepseek-ai: Since the latest Artifacts, the whale has not released one, but two new model iterations with a new size (552B-A16B) which also support image inputs. The model has gained a lot of (well-deserved) attention for its performance at a small price. It also carries the MIT license, continuing the trend established by DeepSeek themselves. This is notable in times where licenses seem to become more bespoke and exclusionary. Below is the Pareto of performance vs price on DeepSWE, a favorite agentic software engineering benchmark today, which DeepSeek dominates.
- clef by Cloudflare: Decision models are all the rage after being introduced by the startup Typesafe. In short, they are general classification models that output few tokens with their probabilities. Its usefulness has led to quick adoption and also a lot of open model finetunes such as Clef.
- NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 by nvidia: The mid-sized model of the Nemotron family got its long awaited update. It is strong for its size and can be run at home (given you own a beefy laptop or RTX Spark). As usual, NVIDIA releases the vast majority of the data and an in-depth tech report.
- Beam-1.0-501B-A23B by reflection: The long awaited open model by Reflection, making it the strongest open American model released under a permissive license (Apache 2.0). While not the smartest open model available, Beam is very impressively token efficient (second to only GPT-6-Astra below). This is a sign of a well-developed post-training stack.
Models
General Purpose
- Ternary-Bonsai-2-27B-gguf by prism-ml: A ternary version of Qwen3.8-27B for on-device deployments.
- Ornith-1.5-397B by ornith-ai: A series of Qwen3.5 and Gemma 4 finetunes that gained attention in the local AI community for its strong performance over the respective (strong) baselines.
- Ling-3.0-flash-VL-fp4 by inclusionAI: A 124B-A5.5B model by Ant Ling (within Ant Group), which continues to churn out models consistently.
- Muse-Spark-Open-816B-A42B by meta-models: META has released their open version of Muse, which we have written about in more detail!
