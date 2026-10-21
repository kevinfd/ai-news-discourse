---
id: "09ae1bea99c0f7bb"
title: "DeepSeek open-sources DeepInfer, the inference framework behind its production services"
url: "https://siliconangle.com/2026/10/20/deepseek-open-sources-deepinfer-the-inference-framework-behind-its-production-services"
link: "https://siliconangle.com/2026/10/20/deepseek-open-sources-deepinfer-the-inference-framework-behind-its-production-services"
source: "SiliconANGLE"
domain: "siliconangle.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-20T16:11:00Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Duncan Riley"]
language: "en"
summary: "DeepInfer’s Ascend support follows a Sept. 30 release in which DeepSeek brought the TileLang kernel programming language to Huawei’s chips with the chipmaker’s help. The startup plans to deploy at ..."
tags: []
orgs: ["DeepSeek", "Nvidia", "Amazon", "China"]
topics: ["chips & infrastructure", "models & research", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 728
paywalled: false
image: "http://www.bing.com/th?id=ONUT.Et8yB3M0x9BAdoHQP6DmFw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# DeepSeek open-sources DeepInfer, the inference framework behind its production services

SiliconANGLE · Duncan Riley · 2026-10-20

DeepSeek open-sources DeepInfer, the inference framework behind its production services
Chinese artificial intelligence startup Hangzhou DeepSeek Artificial Intelligence Basic Technology Research Co. Ltd. today open-sourced DeepInfer, the inference framework behind its own production services.
The release takes on the cost of serving large models to the public. DeepSeek calls reaching a massive user base at a reasonable price “the core problem an inference framework has to solve” in a deployment Q&A posted with the code. One cluster now serves 155 trillion tokens a day, according to the same document, and revenue at off-peak pricing works out to $38 per graphics processing unit per hour.
For now DeepInfer supports a single model, DeepSeek-V4.1-Flash, and by default it loads the updated 1017 version DeepSeek released over the weekend. Nvidia Corp.’s SM100 Blackwell GPUs can run the framework, as can Ascend 950 neural processing units from Huawei Technologies Co. Ltd. Hopper and other older Nvidia architectures are not on the list.
Two features that keep outputs identical from run to run work only on Nvidia hardware. All of the published performance benchmarks ran on Nvidia chips too, and the figures are DeepSeek’s own.
Speculative decoding in DeepInfer runs through DSpark, a system in which a draft model proposes five tokens at a time and a confidence head predicts which of them the main model will accept. Verification compute goes only to the likeliest candidates. That trims the number of draft tokens checked per step by about 30%, and DeepSeek estimated a 4% to 7% throughput gain at its production load. A second technique, which the company says nearly halves total prefill computation, runs only the last 128 tokens of each prompt back through the model’s decoder layers.
DeepSeek has not yet released its key-value cache management and load-balancing code, saying the two are tightly coupled to internal infrastructure. A blog post the company published on Zhihu lays out how both work. Splitting prefill and decode across separate machines is also left to operators, with the README noting that most of the engine work for it is already in place. The smallest deployment DeepSeek describes as efficient uses 64 GPUs for prefill and another 64 for decoding.
The same coupling kept DeepSeek from releasing its full engine in April 2025, when it described the software as an early fork of vLLM built around its cluster management tools. Maintaining a large open-source project was also more than “a small research team focused on developing better models” had bandwidth for, the company wrote at the time.
DeepSeek had already released components such as the FlashMLA, DeepGEMM and DeepEP kernel libraries, which DeepInfer now uses. The new README names vLLM as its original foundation.
DeepInfer’s Ascend support follows a Sept. 30 release in which DeepSeek brought the TileLang kernel programming language to Huawei’s chips with the chipmaker’s help. The startup plans to deploy at least 160,000 Ascend 950DT accelerators at a new data center in Inner Mongolia, Bloomberg reported in September.
The framework arrived a day after the U.S. Department of Homeland Security ordered federal civilian agencies to remove DeepSeek products from their systems, including third-party services built on its technology.
DeepInfer is available on GitHub under the Apache 2.0 license, and the companion deepseek-recipe library released with it converts requests into token sequences using the same logic as DeepSeek’s official application programming interface. DeepSeek said inference code for future models will go into the same repository.
Image: DeepSeek
A message from John Furrier, co-founder of SiliconANGLE:
Support our mission to keep content open and free by engaging with theCUBE community. Join theCUBE’s Alumni Trust Network, where technology leaders connect, share intelligence and create opportunities.
- 15M+ viewers of theCUBE videos, powering conversations across AI, cloud, cybersecurity and more
- 11.4k+ theCUBE alumni — Connect with more than 11,400 tech and business leaders shaping the future through a unique trusted-based network
Are you an AWS customer? Support SiliconANGLE financially by buying your AWS services from our Marketplace portal page and links: https://siliconangle.com/aws-marketplace/
About SiliconANGLE Media
Founded by tech visionaries John Furrier and Dave Vellante, SiliconANGLE Media has built a dynamic ecosystem of industry-leading digital media brands that reach 15+ million elite tech professionals. Our new proprietary theCUBE AI Video Cloud is breaking ground in audience interaction, leveraging theCUBEai.com neural network to help technology companies make data-driven decisions and stay at the forefront of industry conversations.
