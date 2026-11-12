---
id: "a32e986b8587cd60"
title: "Decoding the Nature paper on DeepSeek-R1 without prior knowledge"
url: "https://note.com/nanalabo_ai/n/n67bf53025fb2?hl=en"
link: "https://note.com/nanalabo_ai/n/n67bf53025fb2?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-12T05:06:00Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["ナナラボ＠Ai解説"]
language: "en"
summary: "DeepSeek is that AI that was made cheaply, right? I heard it got smart on its own without humans teaching it, but what exactly is so impressive about it?”In this series, we will decode famous AI ..."
tags: []
orgs: ["DeepSeek"]
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1830
paywalled: false
image: "http://www.bing.com/th?id=ONUT.tgQt6oO37w6adlBqdDT7hg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Decoding the Nature paper on DeepSeek-R1 without prior knowledge

note · ナナラボ＠Ai解説 · 2026-11-12

SYSTEM NOTICE
Is it true that 'AI became smart without human teaching'? Verifying with the DeepSeek-R1 paper
“DeepSeek is that AI made on a budget, right? I heard it got smart on its own without humans teaching it, but what exactly is so impressive about it?”
In this series, we will break down famous AI research from overseas, starting from zero prior knowledge. The first installment is the DeepSeek-R1 paper published in Nature on September 17, 2025.
There are three questions.
- How far did an AI trained only by being told 'whether it is correct or not' improve in mathematics?
- What costs are included in the figure of '$300,000 to build'?
- What did the paper itself and the experts who reviewed it before publication cite as weaknesses?
Nice to meet you, this is Nana Lab. I gathered the numbers from the published text and supplementary materials, and redrew the diagrams myself.
1. First, let's grasp just 5 terms
- LLM (Large Language Model): An AI trained to read vast amounts of text and predict the next word. It is the foundation of chat AI.
- Reasoning Model: A type of LLM that writes out a long process of thinking before giving an answer. Imagine someone who doesn't answer immediately with mental math, but writes down intermediate steps on scratch paper.
- Reinforcement Learning: Learning that strengthens methods through rewards when things go well after trial and error. It is similar to training a pet: you give a treat if they get it right, but you don't teach them the method.
- Supervised Fine-Tuning (SFT): Learning that involves imitating examples written by humans. It is like calligraphy where you trace over a model.
- Benchmark: A common test for AI. In this paper, they use AIME (where answers are numbers), a math contest for high school students in the US. The rate of getting it right on the first try is pass@1, and the accuracy rate after having it answer 16 times and taking a majority vote is cons@16.
2. The content of the experiment: What happens if you only reward the correct answer?
The research team applied reinforcement learning to DeepSeek-V3 Base, which had already been trained on a massive amount of text. What resulted was DeepSeek-R1-Zero (hereafter, R1-Zero).
- They only specified the format of enclosing the thinking process in <think> and the answer in <answer>.
- The rewards are only based on "is it correct?" and "is the format correct?", which are automatically determined by rules
- No examples of how to solve problems written by humans are used
- The method is GRPO. It has the model answer the same problem in 16 different ways and reinforces the answers that score higher than the average
As a result, the average pass@1 on AIME 2024 rose from 15.6% to 77.9% as learning progressed. With majority voting (cons@16), it is 86.7% . The paper states that this significantly exceeds the average of contest participants (about 38% shown by the dashed line in the figure, and 37.8% as noted in the supplementary material). The figure above is a redraw of these four numbers.
The length of the answers also increased. The average length of a single response went from a few hundred tokens (the number of word fragments) to around 15,000 tokens. This is read from Figure 1b and is not an exact value. Note that the period when the maximum answer length was expanded at about 8,200 steps coincides with the period when performance and length jumped.
I will correct my opening statement. The precise meaning of "without human teaching" is "without providing examples of how to solve the problems." The rules for judging correctness were prepared by humans. Reinforcement learning was not learning by being taught, but learning by grading only the results.
3. Separating the "aha moment" into observation and interpretation
A well-known scene in this paper is the output of R1-Zero at an intermediate stage. While solving a math problem, the model wrote this:
After that, it re-checks the calculation from the beginning. The paper states that reflective words like "wait" increased during the learning process, and that "wait" in particular was prominent after 8,000 steps.
I will read the facts and interpretations separately.
- Observation: There is one example of output from an intermediate version. The frequency of words like "wait" increased
- Interpretation of the paper: It is a sign that the method of reasoning has changed, indicating a process of self-evolution
- Question (peer review): Table 1 of the paper itself writes "anthropomorphic style." One of the experts who reviewed it pointed out that human-like speech could lead to ungrounded trust. Another reviewer introduced both small-scale reproduction examples and research suggesting it might be a byproduct of the quality of the base model
There is no evidence in the paper to conclude that "the AI realized it on its own." What is certain is only that such output examples and an increase in word frequency were observed.
4. R1-Zero and R1 are different things. Recounting Table 2
DeepSeek-R1 is a "product version" created in the following four stages, and is not R1-Zero itself.
- A small amount of supervised learning (cold start) with thousands of data points that are easy for humans to read
- Reinforcement learning for reasoning. Adding "language consistency" to the reward as well
- Selecting good outputs from reinforcement learning, mixing in general text and Q&A, and performing supervised learning once more
- A second round of reinforcement learning that also includes helpfulness and harmlessness
Table 2 of the paper compares five models, including R1-Zero and R1, across 21 rows of benchmarks. I extracted only the R1-Zero and R1 columns and recounted which numbers were higher.
The result is that R1 is higher in 15 rows, and R1-Zero is higher in 6 rows (no ties). Two rows out of the 21 include Codeforces.
Examples where R1 significantly outperformed include IF-Eval (instruction following) from 46.6 to 83.3, AlpacaEval 2.0 (response preference) from 24.7 to 87.6, and Aider-Polyglot (code editing) from 12.2 to 53.3.
Conversely, among the 6 rows where R1-Zero was higher, the largest difference is in CNMO 2024 (a Chinese math competition) at 88.1 vs 78.8, followed by GPQA Diamond (graduate-level science) at 75.8 vs 71.5. Note that for the reasoning-based AIME 2024, although R1 is higher, the difference is slight at 77.9 vs 79.8.
In other words, R1 is not superior in everything. The areas that improved were mainly instruction following and response preference. I only looked at the magnitude of the numbers and did not judge statistical significance. The description "without human examples" only applies to R1-Zero.
5. "Distillation" was effective for small AI
Another experiment is distillation. Using approximately 800,000 answers created by a large AI (R1) as teaching material, existing small models are additionally trained. Reinforcement learning is not applied; only supervised learning is used.
There are figures comparing models with the same 32 billion parameters (a number representing the size of the AI).
- Small model directly subjected to large-scale reinforcement learning: AIME 2024 pass@1 is 47.0
- Distilled with R1 answers: 72.6 on the same metric72.6
The paper concludes that distillation is economical and effective for small models, but also notes that to exceed the limits of human intelligence, a more powerful base model and large-scale reinforcement learning may be necessary.
6. The contents of "made for $300,000"
I will verify the basis for "made cheaply." The Nature news article used "US$300,000" in its subtitle. The original figures are in the cost table in the supplementary materials.
- R1-Zero training: 101,000 GPU hours → $202,000
- Creation of data for supervised learning: 5,000 GPU hours → $10,000
- R1 training: 41,000 GPU hours → $82,000
- Total: 147,000 GPU hours → $294,000
GPUs are components for AI computation, and GPU hours refer to 'how many hours one unit was used.' The dollar amount is a conversion assuming a rental cost of $2 per hour. Adding them up again matches the total in the supplementary table.
This $294,000 does not include the pre-training costs for the base DeepSeek-V3 model. There is also no mention of small-scale experiments, unsuccessful attempts, labor costs, or equipment costs.
Saying it was 'made for about $300,000' is misleading. To be precise, 'assuming the base model already exists, the computational cost of the R1 reinforcement learning process, when converted to rental prices, is about $294,000.' I will correct the 'made cheaply' claim from the beginning here.
7. Limitations acknowledged by the paper and questions raised before publication
This paper has undergone peer review. It went through 3 rounds with 8 reviewers; it was received on February 14, 2025, and accepted on July 17, 2025.
I will list the main limitations as written by the paper itself.
- It may overthink even simple problems
- In tasks where it is difficult to judge correctness, such as writing, it is easy to exploit loopholes in the reward system
- Dangerous content can be generated through jailbreaking (attacks to elicit prohibited content)
During peer review, points were raised such as whether the answers became longer not because it became smarter but because it became verbose, whether the AIME problems overlapped with the training data, and that safety experiments only show it is 'on par with other models' and do not constitute proof of safety. Regarding the question of whether it was trained on the output of other companies' AI, the supplementary material acknowledges that while it was not intentionally included, there is a possibility it learned indirectly through the answers of other companies' AI on the web.
8. Summary: Observation and proof are different things
- The paper reports that in reinforcement learning where only correctness is rewarded, the accuracy rate on AIME 2024 increased from 15.6% to 77.9%
- 'No human examples' refers to R1-Zero, and the production version R1 also uses data refined by humans
- The approximately $300,000 is a conversion of the computational costs for the reinforcement learning process, excluding the pre-training costs of the base model
- The 'aha moment' is based on observed output examples and an increase in words, and cannot be considered evidence that the AI has achieved understanding
The paper is a report of results. If you read by separating what is an observation, what is an interpretation, and what is unverified, the view from the same paper changes. Other articles can be found on the NanaLab@AI Explanation profile.
Source: Guo, D. et al. "DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning." Nature 645, 633–638 (2025). https://doi.org/10.1038/s41586-025-09422-z License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The figures in this article were created by the author based on data from the paper's main text and supplementary materials, and differ from the original charts.
This article was researched and written with the help of AI. The figures were derived from the publicly available paper and its supplementary materials, and the charts were created by the author.
