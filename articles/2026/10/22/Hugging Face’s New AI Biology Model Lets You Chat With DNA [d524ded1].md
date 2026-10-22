---
id: "d524ded1295e7b8b"
title: "Hugging Face’s New AI Biology Model Lets You Chat With DNA"
url: "https://wired.com/story/hugging-face-new-ai-biology-model-chat-with-dna"
link: "https://wired.com/story/hugging-face-new-ai-biology-model-chat-with-dna"
source: "WIRED"
domain: "wired.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T10:00:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Emily Mullin"]
language: "en"
summary: "The new open-source model speaks the language of DNA and can help researchers understand the effects of any changes on gene activity and health."
tags: ["Science", "Science / Health", "Business", "ai", "DNA", "artificial intelligence", "models", "open source", "ChatDNA"]
orgs: ["Hugging Face", "OpenAI", "Google", "Nvidia", "China"]
topics: ["models & research", "health & science", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 625
paywalled: false
image: "https://media.wired.com/photos/6ad9279b7f825128a68bc73a/master/pass/Science_HuggingFacesPowerfulNewDNAModelIsSmallEnou-ezgif.com-video-to-gif-converter.gif"
discussion_url: null
score: null
comments: null
community: null
---

# Hugging Face’s New AI Biology Model Lets You Chat With DNA

WIRED · Emily Mullin · 2026-10-22

The AI platform Hugging Face on Thursday released a new open-source model for understanding DNA that can run locally on a laptop.
Developed in collaboration with researchers at Zhongguancun Academy in China and the University of Naples Federico II in Italy, the model is trained on genomic sequences and natural language so that people can ask questions about the effects of DNA changes on gene activity and health and get conversational answers in return.
Lewis Tunstall, a senior research scientist at Hugging Face, says the tool is meant to help researchers design new drugs and genetic therapies, and it could potentially aid patients in interpreting their own genomes.
“We've unlocked a new capability in language models, which is fundamentally about being able to chat with DNA,” he says of the new model, dubbed Carbon-X. Using natural language means even nontechnical users “can actually ask questions about DNA that wouldn't be accessible through any other tool.”
Known as essentially GitHub for AI models, Hugging Face provides a library of readymade AI tools and a platform for running primarily open-weight and open-source AI applications for developers, researchers, businesses, and people who want to experiment with AI without building everything from scratch. In September, Nvidia agreed to acquire the company for nearly $13 billion. (Hugging Face was also at the center of a major hack by OpenAI’s models earlier this year.)
DNA is more like computer code than natural language. Instead of 0s and 1s, though, it uses As, Cs, Gs, and Ts to encode information. A human genome contains 6 billion of these letters. While the human genome has been sequenced end to end, scientists still don’t understand how most of it works.
Now, AI models are helping researchers decipher some of those mysteries. Last year, Google DeepMind released AlphaGenome, which predicts the effects of DNA sequences and genetic mutations but does so in a numeric format. It also requires more compute power. Evo 2, a model developed by the Arc Institute and Nvidia, along with academic partners, speaks the language of DNA and can generate entire genomes from scratch.
Carbon-X integrates both DNA and natural language in a conversational interface. Think of it like a ChatGPT for DNA.
The team started with an existing language model and expanded its vocabulary to read DNA in groups of six letters. They then continued training on 300 billion chunks of data, or tokens, that combined DNA sequences, English text, and examples linking DNA to biological descriptions. The DNA sequences came from mammals (including humans), other vertebrates, invertebrates, plants, fungi, and protozoa. Tunstall says the team didn’t train the model on viruses because they didn’t want it to be used for potentially dangerous applications.
Users won’t be able to upload full human genomes. The model was trained to be able to ingest DNA sequences of roughly 50,000 base pairs, so users will only be able to query small parts of the genome at a time.
One of the ways scientists could use Carbon-X is to help understand whether a genetic mutation is benign or disease-causing, a key step in developing a targeted drug or genetic therapy. If an intervention targets the wrong mutation, it could be totally ineffective or, worse, cause unintended harm.
Researchers face restrictions when it comes to uploading identifiable or sensitive patient data to frontier AI models, so Tunstall says his team intentionally designed a small model with 14 billion parameters. That will allow it to run locally on the user’s hardware, rather than rely on cloud-based models. No data is sent to Hugging Face or any other company, he says.
The developers of Carbon-X caution that they haven’t validated the model yet with actual wet lab experiments, so they can’t say how accurate its predictions are.
