---
id: "ab03e916a10935cc"
title: "Is the mechanism by which generative AI forgets the past the same as the human brain?"
url: "https://note.com/hr_koyama/n/nc7ff32dd1296?hl=en"
link: "https://note.com/hr_koyama/n/nc7ff32dd1296?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-11T17:00:00Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["Koyamarium"]
language: "en"
summary: "To start with the conclusion, the mechanism by which generative AI (large language models) \"forgets\" past information and the mechanism by which the human brain forgets are completely different in ..."
tags: []
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 573
paywalled: false
image: "http://www.bing.com/th?id=ONUT.ITaD3QN_mGOxbsVzCGqSFQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Is the mechanism by which generative AI forgets the past the same as the human brain?

note · Koyamarium · 2026-11-11

SYSTEM NOTICE
Is the mechanism by which generative AI forgets the past the same as the human brain?
To start with the conclusion, the mechanism by which generative AI (large language models) "forgets" past information and the mechanism by which the human brain forgets are completely different in both fundamental mechanism and purpose.
While the AI's "way of forgetting" is based on physical capacity limits or architectural specifications, forgetting in the human brain is an active and biological function for optimizing life maintenance and learning efficiency.
Let's compare the differences between the two from the perspectives of structure and principle.
---
1. "Forgetting" in Generative AI: Structural and Mathematical Constraints
The phenomenon where generative AI loses past context or knowledge occurs mainly at the following three layers.
• Limits of context window and KV cache (forgetting during conversation)
• During inference such as with chatbots, AI has an upper limit on the number of tokens it can process at once (context length). Older inputs that exceed this are either excluded from the calculation of the attention mechanism or pushed out of the KV cache. This is not the AI "forgetting" itself, but rather a state where it has **"fallen out of the field of view (data has been truncated)."**
• Static parameters during inference (fixed after training)
• Standard LLMs do not update their own neural network connection weights during inference (chat). In other words, they do not have the function to rewrite newly acquired information during a conversation as long-term memory like synapses in the brain (they return to their initial state once the session is reset).
• "Catastrophic Forgetting" in fine-tuning
• When AI is made to learn new data or tasks (fine-tuning), the weight vectors of old tasks are overwritten during the optimization process, leading to a phenomenon where it **"can no longer do what it could do before."** This is similar to "overwriting new memories" in the human brain, but it differs in that it is not abstracted or integrated like the brain, but rather old information is simply destroyed as a result of gradient descent.
---
2. "Forgetting" in the human brain: Adaptive and active optimization
On the other hand, forgetting in the human brain is not merely an "error due to insufficient capacity," but rather sophisticated information processing actively performed by the brain to enhance survival and learning efficiency.
• Synaptic plasticity and LTD (Long-Term Depression)
• Synaptic connections in unused neural circuits are physically weakened and dismantled through LTD and synaptic pruning. This reduces noise in the neural circuits within the brain and increases the efficiency of signal transmission for important information.
• System-level memory consolidation and abstraction
• During sleep, in the process of transferring information from the hippocampus to the neocortex, detailed episodic memories are stripped away and converted into **"general rules and concepts (schemas)."** Humans "forgetting" details is an inevitable process for discarding noise and extracting the essence.
• Active Forgetting
• Recent neuroscience has revealed that there are mechanisms within the brain's molecular machinery that actively erase or suppress old information that hinders new learning, as well as traumatic or excessive memories that are unnecessary for survival.
---
3. The decisive difference between AI and human "forgetting"
For AI, "forgetting" is often a weakness due to computational resource constraints, but for the human brain, "forgetting" can be said to be its greatest strength for maintaining high intelligence within limited energy and resources.
