---
id: "d8fa341b96c36837"
title: "Agile Deliberation: How AI helps humans define the gray areas"
url: "https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas"
link: "https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas"
source: "Google Research"
domain: "research.google"
source_type: "research"
collector: "rss"
date: "2026-11-04T18:07:05Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: []
language: "en"
summary: "Data Mining & Modeling"
tags: ["Data Mining & Modeling", "Generative AI", "Human-Computer Interaction and Visualization", "Machine Intelligence"]
orgs: ["Google"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1528
paywalled: false
image: "https://storage.googleapis.com/gweb-research2023-media/original_images/AgileDeliberation1_Thumbnail.png"
discussion_url: null
score: null
comments: null
community: null
---

# Agile Deliberation: How AI helps humans define the gray areas

Google Research · 2026-11-04

November 4, 2026
Otilia Stretcu, Research Scientist, and Leijie Wang, Student Researcher, Google Research
Agile Deliberation addresses the challenges of building AI image classifiers for subjective categories by guiding users through an interactive deliberation workflow, from scoping sub-categories to resolving edge cases, using an LLM-driven optimization loop to automatically build an accurate, aligned classifier.
Machine learning models learn to recognize the world around us from examples labeled by humans. Underlying this process is an assumption that the person doing the labeling has a clear and stable definition of the category in mind before they begin. This assumption holds well when training a model on objective categories, like a stop sign or a golden retriever, where boundaries are clear and universally recognized. In practice, however, real-world applications often require vision systems to navigate the subjective "gray areas" of human experience. For example, consider training a vision classifier to identify "healthy food", curate "inspiring artwork”, or assist in content moderation. In such domains, category boundaries may not be universal or static, since they can shift with cultural context, personal philosophies, or evolving operational policies. Furthermore, people rarely start with a complete specification for subjective concepts, even in their own minds. Instead, they begin with an intuitive idea of a concept and only discover the concept’s true boundaries, exceptions, and nuances as they encounter real-world examples. Traditional training workflows don’t account for this concept evolution, forcing users to provide rigid labels to an AI system even when their own mental model is still shifting.
To bridge this gap, we introduce Agile Deliberation, a framework that treats the creation of subjective AI classifiers as an iterative conversation. Rather than requiring humans to act as static data labelers, Agile Deliberation turns the AI system into a collaborative partner that helps users "deliberate" and sharpen their own definitions. By resolving human ambiguity first, the framework systematically builds more effective, robust, and aligned AI systems. To support the wider research community, we have also open-sourced the underlying code and algorithms on GitHub.
A key differentiator of this work is its focus on the live user experience. Because standard, static AI benchmarks can’t capture subjective concepts, we bypassed simulated testing and evaluated Agile Deliberation across 18 live, 1.5-hour sessions with human participants. This allowed us to directly observe and measure how a person's intent dynamically evolves when paired with an intelligent system. We found that Agile Deliberation drastically reduced user fatigue and anxiety by replacing manual prompt engineering with direct feedback on borderline images, which resulted in more consistent, higher-performing AI models that outperform standard baselines.
Agile Deliberation splits the complex task of defining a subjective concept into two structured stages: concept scoping and concept iteration. Together, these two phases transform a fuzzy idea into a highly precise instructional blueprint for an AI model.
When confronted with a broad topic like "Healthy Food," human intuition naturally struggles to list every rule upfront. In the concept scoping stage, the system guides the user to break down their overarching concept into a structured hierarchy of sub-concepts and explicit exclusions.
For instance, instead of just using a single broad label, a user might decompose "Healthy Food" into positive sub-categories like "Salads," "Grain Bowls," and "Lean Proteins." Simultaneously, they might define explicit exclusions, such as "Processed Foods" or "Raw, Unprepared Ingredients." This creates an initial structured baseline that grounds the model's understanding.
With the initial structure established, the framework moves from static planning to active testing. Traditional machine learning assumes the human annotator is an "oracle" with a complete set of fully defined rules already in mind. Agile Deliberation upends this premise, focusing instead on collaborative refinement.
This stage draws inspiration from active learning, a method traditionally used to retrieve informative data points to maximize a machine's training efficiency. However, instead of selecting examples purely to minimize machine uncertainty as in active learning, Agile Deliberation uses vision-language models (VLMs) to actively mine and surface semantically borderline images that challenge the current text-based definitions.
For instance, the system might present an image of a fruit smoothie to challenge a "healthy diet" concept, forcing the user to decide: Is this a healthy beverage because it contains raw fruit, or is it an excluded processed food due to high sugar content?
Confronting these ambiguous edge cases drives users to reflect on their own hidden assumptions, clarify their true intent, and update the policy rules accordingly. This human feedback is then routed directly into an automatic prompt optimization loop, ensuring the VLM's classification boundaries shift in tandem with the user’s refined definitions.
Evaluating subjective visual classifiers presents a fundamental challenge: there is no static, objective ground truth to measure performance against and therefore, offline evaluation on pre-labeled datasets can’t measure how well the framework adapts as a person's mental model of a concept shifts during the deliberation process.
To capture this dynamic, we built a functional prototype and evaluated it through a live user study. We conducted 18 live user sessions, each lasting 1.5 hours, where participants interacted with our system and alternative baselines in a randomized order to prevent learning bias.
We chose two complex, highly subjective domains to test the limits of these systems:
- Healthy Food: A domain where personal health philosophies, dietary restrictions, and cultural backgrounds can produce highly diverse, subjective viewpoints.
- Pay-to-Play: A real-world content moderation challenge that requires capturing expert-level nuance and specific context. This involves identifying clickbait images in online entertainment or gaming that promise misleading financial or digital rewards.
We evaluated Agile Deliberation against three common distinct paradigms:
- Zero-shot classifiers: The standard "one-and-done" approach. Users write an initial prompt, but have no way to see edge cases or adapt when the model misinterprets the boundary.
- Modeling collaborator: An automated, top-down approach where an AI agent tries to decompose the concept on its own. While it generates criteria automatically, it removes the user from the loop, leaving no way to guide or correct its logic.
- Manual deliberation: The tedious, brute-force status quo process, where users examine data in spreadsheets, guess search queries to find anomalies, and rewrite raw prompts by hand.
The live user sessions revealed that Agile Deliberation yields higher-performing classifier models, while substantially improving the user experience.
We found that study participants who went through the structured deliberation process demonstrated significantly higher labeling consistency over time. By resolving boundary ambiguities early on, they built classifiers that substantially outperformed all standard baselines. These performance gains were most dramatic on the most challenging subjective images — the exact areas where traditional classifiers typically fail because they rely on default, generic AI assumptions rather than the user's explicit, nuanced intent.
Expert participants reported that the system acted as an effective diagnostic tool. By intentionally serving up confusing, borderline images, the AI system helped them uncover "blind spots" in their initial definitions — uncovering scenarios they hadn't anticipated until presented with ambiguous real-world examples.
A key finding of our live study was the cognitive toll of manual prompt engineering. Our study showed that users experienced pronounced cognitive fatigue when trying to predict search terms that might uncover edge cases during manual concept deliberation. Furthermore, they reported experiencing persistent anxiety that manually tweaking a text prompt to fix one mistake might unintentionally degrade performance for other parts of the classifier they had already fixed.
Agile Deliberation addresses this friction by handling the heavy computational lifting. Users don't need to be prompt engineers; they simply look at a curated gallery of borderline images and provide natural feedback. The system seamlessly absorbs their intent and updates the underlying model automatically.
As a result, participants using Agile Deliberation reported feeling significantly less stressed, less frustrated, and less mentally drained, with every participant expressing a preference for Agile Deliberation over the manual methods.
Ultimately, Agile Deliberation shifts the paradigm of human-in-the-loop machine learning from a one-way street — where the AI system simply learns from human labels — to a two-way collaboration where humans and AI refine concepts together.
As machine learning systems are increasingly deployed to handle complex, real-world societal tasks, ensuring that their boundaries reflect nuanced subjective concepts is essential. Whether empowering trust and safety teams to build safer content moderation filters, helping curators shape digital collections, or assisting scientists in categorizing complex visual data, Agile Deliberation provides a foundation for human-AI alignment.
To learn more about the underlying active learning techniques and the technical implementation of our scoping and clustering algorithms, read our paper and check out the open-source implementation on GitHub. To get started, see our interactive Colab/Jupyter demo to walk through the "Healthy Food" example featured in this post. From there, you can adapt it to any domain where you are a subject-matter expert (e.g., flagging misleading clickbait) or use it to build a personalized classifier around your own subjective taste and standards (e.g., curating "inspiring artwork”).
We would like to thank our collaborators — Wei Qiao, Thomas Denby, Krishnamurthy Viswanathan, Enming Luo, Chun-Ta Lu, Tushar Dogra, Ranjay Krishna, and Ariel Fuxman — for their valuable insights and contributions to this work and the accompanying paper. This research was made possible through a close partnership between Google Research and Google Ads.
    ×
    ❮
    ❯
    
  
  ×
