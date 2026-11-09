---
id: "cc7c2a8b88b4f30c"
title: "Reading DeepSeek's Inference through Resource Allocation and Pricing Systems: A Verification of Disclosures"
url: "https://note.com/yukio__takagi/n/n1db1aa4798f1?hl=en"
link: "https://note.com/yukio__takagi/n/n1db1aa4798f1?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-09T00:38:00Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["ガリ納豆"]
language: "en"
summary: "Series: \"The Economics of Open Weight Models\" Part 2IntroductionIn Part 1, we saw that even if open weights are free to copy, running them requires GPUs and incurs costs. So, how much can the party ..."
tags: []
orgs: ["DeepSeek", "China"]
topics: ["chips & infrastructure", "business & funding", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 2987
paywalled: false
image: "http://www.bing.com/th?id=ONUT.DY5xvHJwHDHSJ36LlKacPg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Reading DeepSeek's Inference through Resource Allocation and Pricing Systems: A Verification of Disclosures

note · ガリ納豆 · 2026-11-09

Reading DeepSeek's Inference through Resource Allocation and Pricing Systems: A Verification of Disclosures
Series: "The Economics of Open Weight Models" Part 2
Introduction
In Part 1, we saw that even if open weights are free to copy, running them requires GPUs and incurs costs. So, how much can the party that released them earn by running them?
On October 20, 2026, DeepSeek released part of its inference framework, "DeepInfer," and simultaneously revealed figures for its own services. It claims to process 155 trillion tokens per day on a single cluster, with revenue per GPU per hour at $38 (calculated at off-peak prices) [Note 1] [Note 2]. This article verifies these figures using disclosed prices and measured values, and organizes what can and cannot be said.
- The revenue calculated from the disclosed figures is approximately $39 per GPU per hour, which is close to the disclosed $38. However, both are DeepSeek's own figures and not an independent verification.
- The gross margin, looking only at GPU time costs, is approximately 82–95% assuming GPU costs are 2–7 dollars. This does not include storage, bandwidth, or labor costs.
- A major factor supporting the low price appears to be the cache. Approximately 95% of processed tokens are cache-hit inputs (reused inputs), and their price is 1/50th of that for non-hits. About 80% of revenue is generated from newly calculated non-hit inputs and outputs.
All figures are based on DeepSeek's own disclosures and the author's calculations. What has not been measured is summarized at the end.
1 What DeepSeek Disclosed
There are two types of disclosures used for this verification. One is the API pricing. For inputs, the portion where previously processed content can be reused (cache hit) is priced at 1/50th of the portion that is newly calculated (non-hit) [Note 3].
Unit: USD/million tokens (deepseek-flash = DeepSeek-V4.1-Flash-1017)
Items: Cached input, Uncached input, Output. Off-peak, Peak.
\[\large \newcommand{\arraystretch}{1.6} % \begin{array}{l|r|r} \textbf{Item} & \textbf{Off-peak} & \textbf{Peak} \cr \hline \text{Cached input} & \text{0.003} & \text{0.006} \cr \text{Uncached input} & \text{0.15} & \text{0.30} \cr \text{Output} & \text{0.60} & \text{1.20} \cr \end{array}\]
Source: DeepSeek API Docs "Models & Pricing," retrieved November 7, 2026. Peak times are Monday to Friday, 01:00 to 04:00 and 06:00 to 10:00 UTC (9:00 to 12:00 and 14:00 to 18:00 Beijing time), excluding Chinese statutory holidays. All other times are off-peak.
The other is actual production measurements. A prefill GPU (processing to read input) processes 1.5 million tokens per second including cache hits, and 60,000 tokens per second excluding them. A decode GPU (processing to generate output token by token) processes 14,000 tokens per second. The average input per request is 77,000 tokens, and the input cache hit rate is 96%. DeepSeek operates roughly the same number of prefill and decode GPUs [Note 2].
2 Verifying the Disclosed Figures
Multiplying these measured values by the prices above (off-peak) yields the revenue per GPU per hour. Prefill GPUs earn revenue from non-hit inputs and hit inputs, while decode GPUs earn revenue from outputs.
Unit: USD/GPU-hour (Revenue per GPU per hour, off-peak prices)
Items: Uncached input, Cached input, Output, Total (sum of one prefill and one decode GPU), Per GPU (total divided by 2), Disclosed (DeepSeek's disclosed value).
Calculation basis: Processing volume per second (tokens) is 60,000 non-hit and 1.44 million hit (1.5 million total) for prefill GPUs, and 14,000 output for decode GPUs. Prices are from Table 1.
\[\large \newcommand{\arraystretch}{1.6} % \begin{array}{l|r} \textbf{Item} & \textbf{Revenue} \cr \hline \text{Uncached input} & \text{32.40} \cr \text{Cached input} & \text{15.55} \cr \text{Output} & \text{30.24} \cr \text{Total / Per GPU} & \text{78.19 / 39.10} \cr \text{Disclosed} & \text{38} \cr \end{array}\]
Source: Calculated by the author based on measured values from DeepSeek's Zhihu post (October 20, 2026) and the prices in Table 1. Does not include image encoder GPUs.
At approximately 39 dollars per unit, this is close to the 38 dollars disclosed. However, since both the measured value and the 38 dollars are DeepSeek's own figures, we can only confirm that the calculations are consistent. It has not been independently verified by a third party. Note that the 'approximately 39,000 dollars per month to keep 8 GPUs rented' estimated in the first installment is the cost for the renter, while the 'approximately 39 dollars' in this article is the revenue per GPU per hour. These are different quantities.
Subtracting GPU costs
Subtracting GPU costs from revenue yields the gross profit margin. Since DeepSeek has not disclosed its GPU costs, we will set two hypothetical values. The 2 dollars is a value calculated by DeepSeek itself in its February 2025 disclosure, assuming an H800 rental cost of 2 dollars per hour [Note 4]. The 7 dollars is a value estimated by Yuchen Jin in a post on X, assuming a B300 is rented for 7 dollars per hour, resulting in a gross profit margin of approximately 82% [Note 5]. Neither is the actual cost of V4.1-Flash.
If the GPU cost is 2 dollars per hour, the gross profit margin is (38-2)÷38, or approximately 95%; if it is 7 dollars, it is approximately 82%.
This gross profit margin is viewed solely in terms of GPU time costs. It does not include cache storage, inter-node bandwidth, R&D, or labor costs, which will be discussed later. It does not represent the actual profit margin.
4 Cache supporting low prices
Returning to Figure 1, among the tokens processed, cache-hit inputs account for approximately 95%, but only about 20% of revenue. This is because the price is 1/50th of that for non-hits. About 80% of revenue comes from the remaining approximately 5% of newly calculated tokens (non-hit inputs and outputs).
In usage patterns where conversation history is resent each time, previous exchanges can be reused, increasing hits. The long average input of 77,000 tokens suggests that such usage is common (speculation). If it were a short, one-time question, the reusable first half would be short, and this configuration would not occur.
The effectiveness of reuse is also reflected in processing volume. A single prefill GPU processes 1.5 million input tokens per second including cache hits, and 60,000 tokens if only non-hits are counted; the former is 25 times the latter (1.5 million ÷ 60,000). DeepSeek explains that the goal of keeping the cache for a long time is to avoid repeating prefill calculations when hits occur [Note 1].
DeepSeek also revealed figures for V3 and R1 inference in February 2025, at which time the input cache hit rate was approximately 56% [Note 4]. While the model and measurement methods may not be the same as the current 96%, the figure has increased significantly. Prices and revenue per unit are not listed here because their definitions differ.
On the other hand, reuse incurs storage costs. DeepSeek states that it uses approximately 100 PiB (pebibytes) of SSD for cache storage, and retains data for 3 days for agent-type usage and 7 days for chat [Note 1]. This storage cost is not disclosed and is not included in the gross profit margin in the previous section.
5 GPU allocation and pricing system
As seen in the first installment, weights can be replicated for free, and one person's use does not reduce another's. However, GPUs are rivalrous. If used for prefill, they cannot be used for decoding. DeepSeek's operation is an example of this allocation problem.
Let s be the proportion of GPUs allocated to prefill. When the amount to be processed (non-hit inputs and outputs) is determined, 'non-hit inputs ÷ processing capacity per unit' units are needed for prefill, and 'outputs ÷ processing capacity per unit' units are needed for decoding. If s deviates, the processing for the side that is short will clog, and the other GPU will be left idle. The total number of required GPUs is minimized at the s where both are just sufficient.
Figure 3 shows the number of GPUs required when s is varied, in an example where demand is set at '60,000 non-hit input tokens per second and 14,000 output tokens per second.' This amount is what one prefill GPU and one decoding GPU can each process per second, so two 1-to-1 units are just enough. If s is 0.5 (1-to-1), 2 units are sufficient. Just by shifting to 0.4 or 0.6, the required number increases to 2.5 units. However, since this demand is based on 1-to-1 processing volume, the fact that the minimum is at 1-to-1 depends on how it is set. What can be said is that if the ratio of demand changes, the s that minimizes the number also shifts. If output doubles, s becomes approximately 0.33, and the required number becomes 3 units.
DeepSeek states that it adjusts the number of GPUs for prefill and decoding respectively in response to this movement. It says that because fixing the ratio does not match resources, leading to waiting or idling, it automatically changes the ratio of prefill to decoding according to traffic [Note 1] [Note 2]. Therefore, 1-to-1 is not a fixed design. DeepSeek states that it operates at 'almost 1-to-1,' but since the composition of demand is not disclosed, it cannot be verified whether this is the allocation that minimizes costs. Both the configuration in Figure 1 and the demand in Figure 3 are based on 1-to-1 processing volume and are not evidence of optimality.
DeepSeek's pricing system is such that cache hits are 1/50th of non-hits, outputs are 4 times non-hits, and peak is twice off-peak (Table 1). Among these, the price difference between output and non-hits shows a correspondence in the same direction as the cost difference. Here, we assume that the hourly cost of prefill and decoding GPUs is the same, and we attribute the prefill cost entirely to newly calculated inputs (excluding hit inputs). Then, the cost to produce one token of output is approximately 4.3 times that of a newly calculated input (processing capacities of 14,000 and 60,000). The prices are 0.60 dollars and 0.15 dollars, which is a 4-fold difference. The value of price divided by cost is 16.2 for non-hit inputs and 15.1 for outputs (if GPU cost is 2 dollars), a difference of only about 7% [Note 6]. The prices for prefill and decoding each appear to reflect the difference in costs. Whether this was intentionally designed is unknown.
6 Weights are public, transport is only partially so
DeepInfer, released by DeepSeek, includes offline inference. The README lists three items that are necessary for a complete inference service but are not included in this release [Note 1]: a caching system, the separation of prefill and decode (though it states that most of the necessary engine functionality is already implemented), and load balancing across multiple replicas.
In other words, while the weights and some of the inference code have been released, the core of the operations required to run it as a service has not. This is a concrete example of the difference in the scope of disclosure, as seen in the first installment. The costs for the operator and the prices at which providers offer the service are separate issues. I will investigate provider pricing separately in the future.
Summary
The revenue calculated from DeepSeek's disclosures is approximately $39 per GPU per hour, which is consistent with their disclosed figure of $38. Looking only at GPU time costs, if we assume a cost of $2 to $7, the gross margin is approximately 82–95%. A major factor supporting the low price appears to be caching. Approximately 95% of the tokens processed are reused inputs, and their price is 1/50th of that for a cache miss. About 80% of revenue is generated from newly calculated cache-miss inputs and outputs.
From an economic perspective, GPUs are rivalrous, and the problem of allocation—how to divide them between prefill and decode—remains. The ratio that minimizes the total number of required GPUs shifts based on the composition of demand, and DeepSeek states that it automatically adjusts the ratio accordingly. Whether the current nearly 1:1 ratio is the minimum allocation cannot be verified because the composition of demand has not been disclosed. Furthermore, if we assume the GPU costs are the same, the prices for prefill and decode appear to largely reflect the difference in costs.
However, these figures are based on DeepSeek's own disclosures and are not an independent verification. They do not include storage costs or other expenses and are not actual profit margins. While the weights were released, the core of the operations was not. The benefits and costs of the disclosure cannot be discussed based on these numbers alone.
Appendix
Appendix A: What these figures are 'not'
- The $38 and 155 trillion figures are DeepSeek's own disclosures. The measured values also come from the same source and are not an independent verification. The $38 is a conversion based on off-peak pricing and is an average that does not account for peaks and valleys in traffic (if peak pricing were used, revenue could be up to twice as high). It is not explicitly stated whether the 'total revenue' is an average across all GPUs for prefill, decode, and image encoders, and the image showing the measured values includes a note stating that the machines are kept with excess capacity to prepare for traffic fluctuations. It is also not specified whether the 155 trillion tokens include cache-hit inputs.
- The gross margin is viewed only in terms of GPU time costs. It does not include cache storage, inter-node bandwidth, a portion of depreciation, R&D, or labor costs. The approximately 84–96% figure cited by third parties was also calculated using the same formula (subtracting GPU costs from $38) and is not a verification using a different method.
- Whether the allocation is optimal cannot be verified. Price divided by cost also depends on the assumptions made. The demand in Figure 3 is based on a 1:1 processing volume, and whether 1:1 is the minimum depends on the assumptions. It is assumed that processing capacity per unit is constant regardless of allocation, and the composition of demand and GPU utilization rates are not disclosed. Price divided by cost is based on the assumptions in Section 5 (GPU costs are the same, excluding hit revenue). DeepSeek writes that it uses 8 standard machines for prefill and 64–128 standard supernodes for decode, but it does not disclose the cost per unit. If hit revenue is included, the revenue per prefill GPU is about 1.6 times that of a decode GPU. Neither the allocation calculation nor the price-to-cost correspondence is evidence of design intent.
- The 96% and 95% figures have different denominators. 96% is DeepSeek's disclosed value (input cache hit rate), where the denominator is only input tokens and does not include output (1.44 million / 1.50 million). 95% is my own calculation, where the denominator is the sum of input and output (1.44 million / 1.514 million). The ratio of output and the breakdown of revenue in Figure 1 depend on the assumption that the number of prefill and decode GPUs is 1:1 (if the number of prefill GPUs is increased by 1.2x, the revenue breakdown becomes approximately 21%, 44%, and 34%. The 95% figure barely changes). Figure 1 is not a disclosure of the composition ratio of usage.
- The 2025 cache hit rate (approx. 56%) may not be measured in the same way as the 96% figure here. The 2025 figure is for the 24-hour period across the entire V3 and R1 web, app, and API, while the 2026 figure is the average input cache hit rate for V4.1-Flash (no period specified).
- Prices are subject to change. Table 1 was retrieved on November 7, 2026, and I confirmed there were no changes on November 8.
Appendix B: Measurement Methods
- Revenue calculation (Table 2): Processing volume × 3,600 seconds × price; the total of $78.19 per hour for prefill and decode is divided by two (the basis for the calculation is the row before Table 2).
- Required number of GPUs (Figure 3): The greater of (processing volume of cache-miss inputs ÷ prefill processing capacity ÷ s) or (processing volume of output ÷ decode processing capacity ÷ (1−s)). DeepSeek's decode adjustment is based on the number of requests being processed. Figure 3 is simplified using the number of output tokens.
- Price ÷ Cost (Note 6): Cost (USD/million tokens) = G ÷ (processing volume per second × 3,600 ÷ 1,000,000). With G = $2, cache-miss input is 2 ÷ 216 ≈ $0.0093, and the ratio to the price of 0.15 is 16.2; output is 2 ÷ 50.4 ≈ $0.0397, and the ratio to the price of 0.60 is 15.1 (the ratio of ratios is approx. 1.07). Since G is included in both costs in the same way, this ratio does not depend on G (with G = $7, it is 4.6 and 4.3).
- 2025 cache hit rate [Note 4]: Out of 608B input, 342B were cache hits (342 ÷ 608 ≈ 56%).
Notes and References
[Note 1] DeepSeek, DeepInfer README and Q&A (v0.2, revised 2026-11-03. Original checked on GitHub on 2026-11-07, re-verified on 11-08. README unchanged since initial commit on 2026-10-20). https://github.com/deepseek-ai/DeepInfer, https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md
[Note 2] DeepSeek Zhihu post (2026-10-20) "Practice of DeepSeek V4.1 Flash Large-Scale Inference Deployment." Actual measured values (per GPU per second; image "Actual Online Operation Data") are also here. https://zhuanlan.zhihu.com/p/2095560295930508953
[Note 3] DeepSeek API Docs "Models & Pricing" (retrieved 2026-11-07, re-verified 2026-11-08). deepseek-flash is DeepSeek-V4.1-Flash-1017. Off-peak is half the price of peak. https://api-docs.deepseek.com/quick_start/pricing/
[Note 4] DeepSeek, Open Source Week Day 6 "One More Thing: DeepSeek-V3/R1 Inference System Overview" (2025-02). The description assuming an H800 rental cost of $2 per hour is also here. The 2025 figures are for 24 hours starting from 12:00 UTC+8 on 02-27. https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md
[Note 5] X post by Yuchen Jin (@Yuchenj_UW) (2026-10-21). "Even assuming a B300 is rented at $7 per hour, the gross margin is approximately 82%." https://x.com/Yuchenj_UW/status/2112591074409742733
[Note 6] The calculation of price divided by cost is shown in Appendix B.
