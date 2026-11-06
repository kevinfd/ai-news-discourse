---
id: "513dfed9debcff88"
title: "AI Text Watermarking May Not Be Able to Meet the E.U.’s New Rules"
url: "https://spectrum.ieee.org/ai-watermark-openai-textgrain-europe"
link: "https://spectrum.ieee.org/ai-watermark-openai-textgrain-europe"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-05T15:00:03Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Anna Desmarais"]
language: "en"
summary: "The European Union now requires AI-generated text to be watermarked so that it can be identified as such. But tests on OpenAI’s new textGrain watermark, released in October and developed to comply with the new E.U. law , show that these watermarks often do not survive additional editing of the text or when it’s under 150 words. With no clear legal benchmark for how well watermarks should work,…"
tags: ["Watermark", "Artificial-intelligence", "European-union", "Openai"]
orgs: ["OpenAI", "Google", "EU"]
topics: ["models & research", "policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 1052
paywalled: false
image: "https://spectrum.ieee.org/media-library/conceptual-illustration-of-the-european-union-flag-with-its-stars-replaced-by-logos-for-open-ai.jpg?id=68564327&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# AI Text Watermarking May Not Be Able to Meet the E.U.’s New Rules

IEEE Spectrum · Anna Desmarais · 2026-11-05

The European Union now requires AI-generated text to be watermarked so that it can be identified as such. But tests on OpenAI’s new textGrain watermark, released in October and developed to comply with the new E.U. law, show that these watermarks often do not survive additional editing of the text or when it’s under 150 words. With no clear legal benchmark for how well watermarks should work, it’s uncertain whether textGrain will meet Europe’s transparency rules, which could cost the company significantly and make it difficult to detect AI-generated text as models grow more sophisticated.
AI models calculate the probabilities of different possible next “tokens” (the next word or word fragment it generates) based on the text already written, then select one and repeat that process until the response is complete. After the prompt “today the weather is…,” for example, says Xiang Li, coauthor of the textGrain technical report and a postdoctoral researcher at the University of Pennsylvania, the model might weigh “warm” or “cool” as possible next words.
A watermark uses a secret key to generate pseudorandom values—numbers produced by a mathematical process that influence which token the model suggests. This creates a statistical pattern in the text that a detector with the same secret key can look for, Li says.
What makes textGrain different from other watermarks is that it uses entropy, a measure of how unpredictable a model’s word choices are, as a resource that can be budgeted when embedding a watermark. Developers specify how much entropy or unpredictability they want to allow, and textGrain adjusts to that target.
This gives developers more control over the balance between embedding a detectable signal and preserving variation in the model’s output, Li says. “We can think of entropy as a resource, a kind of money.… In our approach, we can accurately determine how much of that resource we want to consume.”
Limits of AI Watermark Detection
The watermark is invisible to readers. But a positive result does not show how much a person contributed to a passage, and a negative result does not prove that a text was human-written.
OpenAI’s false-positive rate is 1 percent, meaning the detector is designed to wrongly flag about one in 100 unwatermarked passages. In tests on psychology questions from the ELI5 database, which gathers questions and answers from the r/explainlikeimfive subreddit, the model detected watermarks in about 80 percent of 200-token text (approximately 150 words) compared to 95 percent of 400-token text (approximately 300 words).
Li says this is a “basic limitation” of text-watermarking technologies and would be complicated to solve. Short passages may not contain enough watermark evidence for reliable detection, even with additional computation, he adds, while longer passages generally provide more.
Editing also weakens the signal. In an evaluation of 400-token passages, replacing just 10 percent of words with synonyms reduced detection from 92 percent to 66 percent; replacing up to 25 percent cut the detection rate to 17 percent, according to OpenAI. Because the watermark depends on preceding tokens, changing one word can disrupt the signal at several positions, Li says.
OpenAI says watermarking alone is not enough to determine whether content is AI-generated.
TextGrain will “complement” other provenance tools, such as content credentials in the metadata and SynthID watermarks developed by Google DeepMind for images and audio outputs. OpenAI did not respond to a request for comment.
E.U. AI Act Transparency Obligations
The transparency obligations in Article 50 of the E.U. AI Act went into effect on 2 August. The law requires providers of systems generating synthetic audio, images, video, or text to mark outputs in a machine-readable format so they can be detected as artificially generated or manipulated. Technical solutions must be “effective, interoperable, robust and reliable as far as this is technically feasible,” according to the law.
The E.U.’s Code of Practice offers a voluntary way for providers to show how they will be compliant. This code does not require watermarks on outputs shorter than 200 tokens.
Thomas Souverain, a postdoctoral fellow on AI Ethics at the Institute of Advanced Education, in Paris, says the legislation is open to interpretation.
Souverain says that the early methodology behind textGrain seems reliable and could work better than its competitors at identifying AI-generated text. OpenAI says textGrain matched or outperformed Google’s SynthID Text in its own tests, but those results have not been independently verified. Until independent researchers can test it, and while the AI Act’s criteria still lack measurable thresholds, it is too early to say whether textGrain meets legal requirements.
“We only have a technical study…there hasn’t been a peer-reviewed academic article, and we don’t [yet] have access to a precise protocol [for textGrain],” Souverain says.
OpenAI is working with a limited group of researchers that includes John Thickstun, an assistant professor of computer science at Cornell University, and researchers at the Kempelen Institute of Intelligent Technologies (KInIT) in Bratislava, Slovakia.
Thickstun and Dominik Macko, a senior researcher at KInIT, says they had only just gained access and had not yet begun evaluating the system. Macko says his team plans to test textGrain’s “robustness” across different subject areas, languages, and text lengths.
If textGrain is eventually found to not meet the E.U.’s requirements, Souverain says, OpenAI could face a fine of up to 7 percent of its annual income.
Souverain also calls on OpenAI to make textGrain open-source so that researchers not on their team can “identify all the faults, paraphrases and possible translation faults” of the model by trying to break it.
“I see the corporate interest, if there is a big flaw detected, a big weakness, [that] it is detected in the background,” he said. “But I would like to see an even more open phase, such as today with SynthID, [where] we have access to the methods.”
- Meta’s AI Watermarking Plan Is Flimsy, at Best ›
- AI Image Watermarking Faces New Threat From “Unmarker” ›
- AI Models Are Watermarking Text—Will You Notice? ›
Anna Desmarais is an award-winning Canadian journalist based in France with a decade of experience writing, filming and broadcasting on both sides of the Atlantic. She covers artificial intelligence, emerging technologies, space, and disinformation. She has reported everywhere from the high Arctic to the hills of Rwanda for outlets including WIRED, Euronews, France 24, and the Canadian Broadcasting Corporation (CBC).
