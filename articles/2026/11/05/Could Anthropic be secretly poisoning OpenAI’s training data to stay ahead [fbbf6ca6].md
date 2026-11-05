---
id: "fbbf6ca633566987"
title: "Could Anthropic be secretly poisoning OpenAI’s training data to stay ahead?"
url: "https://reddit.com/r/OpenAI/comments/1xogsn4/could_anthropic_be_secretly_poisoning_openais"
link: "https://reddit.com/r/OpenAI/comments/1xogsn4/could_anthropic_be_secretly_poisoning_openais"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T11:57:03Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["cern0"]
language: "en"
summary: "Right now, it honestly feels like Anthropic’s models are better than OpenAI’s in almost every way. Claude seems to be outperforming ChatGPT in a lot of areas, especially coding, and for roughly the same subscription price, I’m starting to wonder why I’d even keep paying for OpenAI. And that got me thinking about a pretty wild theory. What if Anthropic (or any other AI company) could…"
tags: ["r/OpenAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 368
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xogsn4/could_anthropic_be_secretly_poisoning_openais/"
score: null
comments: null
community: "r/OpenAI"
---

# Could Anthropic be secretly poisoning OpenAI’s training data to stay ahead?

Reddit · cern0 · 2026-11-05

Right now, it honestly feels like Anthropic’s models are better than OpenAI’s in almost every way. Claude seems to be outperforming ChatGPT in a lot of areas, especially coding, and for roughly the same subscription price, I’m starting to wonder why I’d even keep paying for OpenAI. And that got me thinking about a pretty wild theory. What if Anthropic (or any other AI company) could intentionally poison a competitor’s training data to slow down their progress? Hear me out. In October 2025, Anthropic actually published a research paper showing that as few as 250 malicious documents could successfully introduce a backdoor into language models, regardless of the model size tested (up to 13B parameters). That’s a ridiculously small amount of data considering how massive these training datasets are. Now imagine a company deliberately flooding the internet with carefully manipulated AI-generated content, knowing that competitors might eventually scrape some of it for training. Meanwhile, the company behind it could keep its own training data clean. There’s also the whole concept of model collapse . A 2024 Nature paper demonstrated how AI models trained recursively on AI-generated data can progressively degrade. That’s not the same thing as deliberate poisoning, but it shows how training data quality can affect future models. Obviously, there are some huge caveats here. Anthropic’s research only demonstrated a narrow backdoor attack, not general intelligence degradation. We also have no idea exactly what data OpenAI uses or how effectively it filters poisoned content. And to be clear, I’m not accusing Anthropic of actually doing this. There’s zero public evidence that they are. The performance gap could easily be explained by differences in training techniques, RL, compute allocation, or simply better research decisions. But from a game theory perspective, the idea is fascinating. If AI companies are competing for billions of dollars, and it’s technically possible to degrade a competitor’s models without ever touching their infrastructure, isn’t data poisoning something they would at least have to consider as a threat? Could something like this realistically work against a frontier model like GPT-6? Or are modern training pipelines already sophisticated enough to make this practically impossible? Curious what people who actually work on LLM training think about this.
