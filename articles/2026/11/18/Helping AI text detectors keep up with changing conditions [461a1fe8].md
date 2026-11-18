---
id: "461a1fe87414da12"
title: "Helping AI text detectors keep up with changing conditions"
url: "https://news.mit.edu/2026/helping-ai-text-detectors-keep-up-with-changing-conditions-1118"
link: "https://news.mit.edu/2026/helping-ai-text-detectors-keep-up-with-changing-conditions-1118"
source: "MIT News"
domain: "news.mit.edu"
source_type: "research"
collector: "rss"
date: "2026-11-18T05:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Adam Zewe | MIT News"]
language: "en"
summary: "A teacher who believes a student’s term paper may have been written by a large language model (LLM) can use a tool for detecting artificial intelligence-generated text to help confirm their suspicions. But the teacher may want to think twice before putting all their trust in the detector.  Researchers from MIT and Cornell University showed that such detection tools, which are AI models…"
tags: ["Research", "Artificial intelligence", "Machine learning", "Human-computer interaction", "Writing", "Language", "Laboratory for Information and Decision Systems (LIDS)", "Electrical engineering and computer science (EECS)", "School of Engineering", "MIT Sloan School of Management", "MIT Schwarzman College of Computing"]
orgs: []
topics: ["models & research", "jobs & society", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1051
paywalled: false
image: "https://news.mit.edu/sites/default/files/styles/news_article__cover_image__original/public/images/202611/MIT-movingtarget-01-press.jpg?itok=As8TOTUK"
discussion_url: null
score: null
comments: null
community: null
---

# Helping AI text detectors keep up with changing conditions

MIT News · Adam Zewe | MIT News · 2026-11-18

A teacher who believes a student’s term paper may have been written by a large language model (LLM) can use a tool for detecting artificial intelligence-generated text to help confirm their suspicions. But the teacher may want to think twice before putting all their trust in the detector.
Researchers from MIT and Cornell University showed that such detection tools, which are AI models themselves, can be fooled by AI-generated text disguised to appear as if it were written by a human. Detectors can also fail to identify AI text due to natural shifts in writing habits over time or the emergence of new LLMs.
In a new paper, the researchers demonstrated how a special training technique makes an AI detector more accurate and resilient to deception, even as human and AI writing constantly changes.
They employed a method called test-time adaptation, which allows a deployed detection model to learn from new, unlabeled data by adjusting its inner workings on the fly. In this way, the model adapts to unseen inputs without being retrained from scratch.
In experiments, a commercial detector could only identify about 27 percent of AI-generated text that had been disguised, while the new approach achieved 93 percent accuracy.
This method could help educators, editors, publishers, and hiring managers flag LLM-generated writing that people try to pass off as human-written. It could also be used by cybersecurity experts to prevent email phishing scams or identify search engine optimization fraud.
“There are many high-stakes contexts where people really care about the identity of the author, from scientific publishing to short story competitions. We’ve shown that test-time adaptation allows your AI detector to be much more robust, even with continual adversarial behavior by AI users,” says study co-author Manish Raghavan, the Drew Houston (2005) Career Development Professor at the MIT Sloan School of Management, who also holds an MIT Schwarzman College of Computing shared position in the Department of Electrical Engineering and Computer Science (EECS), and is a principal investigator in the Laboratory for Information and Decision Systems (LIDS).
He is joined on the paper by lead author Kevin Ren, graduate student at Cornell Tech, and senior author Nikhil Garg, an assistant professor at Cornell Tech. The research will be presented at the Conference on Neural Information Processing Systems.
Duping the detectors
The proliferation of LLMs that generate human-like text has led to a plethora of commercial AI-detection tools to help people identify whether a piece of writing was authored by a human.
But these detection tools can fail when the text they evaluate significantly differs from the text they were taught to identify. This is known as a distribution shift.
Detector developers typically train their models by gathering text from the internet that they know to be either AI- or human-generated. They train the model to tell the difference.
However, once the detector is released, people might change the way they write or the way they use AI to generate text.
For instance, a human in 2030 may write about different topics using new analogies that weren’t common for someone writing in 2010. A detector trained with 2010 data might be unfamiliar with this new writing style and incorrectly mark human-written text as AI-generated.
The release of a detection model also creates a cat-and-mouse game between its developers and users who want to bypass it. These individuals can run AI-generated text through an automated “humanizer” software tool that modifies it to appear human-written to the detector.
“After the company releases a model, a bunch of ‘humanizers’ pop up to try to beat it, so the company tries to incorporate this humanized text into their training so the detector can identify it, and so on. It’s like rinse-and-repeat. The cycle can go on forever,” says Ren.
The researchers explored whether test-time adaptation (TTA) can make an AI detector resilient to these distribution shifts.
Adaptation in action
In TTA, instead of freezing the model so it can’t change during deployment, researchers allow that model to adapt itself to incoming data after it has been released. For an AI text detector, these data are new pieces of text uploaded by users.
These data are unlabeled, so the detector developers don’t know which data were written by humans versus AI models. But these new data represent contemporary human and AI writing — exactly what the developers want the model to be able to predict.
With enough examples, the detector learns to identify patterns to determine which data are AI-generated and which are human-generated.
The researchers studied TTA by creating datasets to contain a certain amount of AI-generated and human-generated text, but they don’t provide those labels to the model. They also used LLMs to generate some examples that resemble text written by AI to specifically evade a detector.
Then they performed the TTA training process and tested the model on ground-truth data.
In experiments designed to mimic the natural shift in human language over time, a detector that used TTA was 85 percent accurate, while traditional methods only achieved 73 percent accuracy.
And when it came to writing designed to thwart detection tools, existing methods could only identify about 27 percent, while TTA enabled the model to catch more than 93 percent of disguised text.
“TTA has the potential to really help deployed AI-detection models in terms of being able to proactively address this iterative ‘gaming’ behavior by adversarial AI users,” Ren says.
Adapting to shifts in human writing behavior is a more difficult TTA problem, since the shifts are slower and occur in more subtle ways, he adds.
The researchers caution that TTA may not always be an effective solution as future LLMs produce more natural-sounding language and it becomes harder to find verifiable human text to use for training.
“It isn’t entirely clear if this will be a solvable problem,” Raghavan says. “There are some big, open questions about how you should think about science, writing, and art in a world where it is infeasible to tell the difference between human-generated content and AI content.”
In the future, the researchers want to explore similar strategic domains where TTA could be useful and build better benchmarking tools to help engineers improve these AI detection models in a dynamic fashion.
This project used API credits provided by Pangram to use their AI text detectors.
