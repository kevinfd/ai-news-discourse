---
id: "4f5d65c153d21a16"
title: "Understanding Jev, the new model everyone is talking about"
url: "https://understandingai.org/p/understanding-jev-the-new-model-everyone"
link: "https://understandingai.org/p/understanding-jev-the-new-model-everyone"
source: "Understanding AI"
domain: "understandingai.org"
source_type: "newsletter"
collector: "rss"
date: "2026-10-08T13:14:53Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Kai Williams"]
language: "en"
summary: "On September 15, the startup TypeSafe AI came out of stealth and released a new AI model. To pretty much everyone’s surprise, it went mega viral. The company’s announcement got almost 40 million views on Twitter. Within a week, over 100,000 people joined the company’s Discord, and some 2,000 projects on GitHub used the new model, called Jev. The company opened general signups on September 20 and…"
tags: []
orgs: ["OpenAI", "Google", "Amazon"]
topics: ["models & research", "business & funding"]
content_source: "summary"
word_count: 507
paywalled: false
image: "https://substackcdn.com/image/fetch/$s_!s7sk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c302045-f428-4d19-9d8b-d948510ecb43_2048x1181.png"
discussion_url: null
score: null
comments: null
community: null
---

# Understanding Jev, the new model everyone is talking about

Understanding AI · Kai Williams · 2026-10-08

On September 15, the startup TypeSafe AI came out of stealth and released a new AI model. To pretty much everyone’s surprise, it went mega viral. The company’s announcement got almost 40 million views on Twitter. Within a week, over 100,000 people joined the company’s Discord, and some 2,000 projects on GitHub used the new model, called Jev. The company opened general signups on September 20 and then paused them two days later because of “an immense swell of demand.” (It restored signups on the 27th.) On October 1, TypeSafe’s CEO claimed that the company had already onboarded a quarter of the Fortune 500. Yet unlike other hyped AI releases of 2026, Jev did not display any new (or potentially dangerous ) capabilities. Jev attracted attention because it is a new type of AI model. TypeSafe AI CEO Diogo Almeida talking in the video announcing the new Jev model. (Screenshot from announcement video ) Jev does not output free-form strings of text like LLMs do. Instead, it takes questions with a fixed set of possible answers — yes/no, multiple choice, or a rating — and outputs the estimated probability that each option is the correct one. For instance, if I asked Jev, “Is ‘tabsfsclkj’ a spam comment?” Jev might put a probability of 0.98 on “Yes” and 0.02 on “No.” While this might seem like a limiting architectural choice, it is actually a huge advantage. Jev’s design lets TypeSafe serve the model much more quickly and cheaply than existing LLMs, which opens up use cases that were previously impractical. Its constrained response format also makes it easier to use code: Jev’s output fits naturally into common software engineering patterns, like if statements. For instance, I’ve used Jev’s output to determine whether comments on my personal blog are likely to be spam. I’d previously used Gemini 3 Flash with structured outputs as the classifier, but Jev is faster and cheaper, and it lets me more easily deal with situations where the model is unsure. All I have to do is use Jev’s estimated probability as a condition, something roughly like: if jev_response.is_spam_probability > 0.8, then … 1 On the flip side, Jev is more general than conventional classifiers. Jev works “out of the box” across a wide range of topics — no fine-tuning required. TypeSafe AI’s success has spawned a legion of copycats. A huge number of individuals and companies, including Cloudflare , Amazon and OpenAI , have created models with the same basic design. Anecdotally, Jev’s performance seems to be the strongest, but it’s unclear whether others will catch up soon. Whatever happens to TypeSafe as a company, I expect Jev to have a substantial impact on the trajectory of AI. Over the coming months and years, we’ll likely see many new applications that rely on Jev or one of its competitors. And Jev might inspire more innovation in the “shape” of AI systems: it shows that it’s sometimes useful for a model to take language as an input but not output text in return. 

 Read more
