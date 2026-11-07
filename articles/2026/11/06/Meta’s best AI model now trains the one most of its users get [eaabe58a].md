---
id: "eaabe58a5bbf21ff"
title: "Meta’s best AI model now trains the one most of its users get"
url: "https://thenewstack.io/meta-muse-specialized-models"
link: "https://thenewstack.io/meta-muse-specialized-models"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-06T18:05:55Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Starting on Friday, everyone using Meta’s Muse agent and Meta AI gets new models the company trained using Muse Wonder, its frontier model. Subscribers still get Wonder itself for harder tasks. \n\n Meta hasn’t named the new models, though we can assume their codenames don’t involve fruits . The company calls them “specialized” versions of its existing ones that were “trained using Muse Wonder.”…"
tags: ["AI"]
orgs: ["Meta", "OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "products & launches", "business & funding"]
content_source: "summary"
word_count: 661
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meta’s best AI model now trains the one most of its users get

The New Stack · Frederic Lardinois · 2026-11-06

Starting on Friday, everyone using Meta’s Muse agent and Meta AI gets new models the company trained using Muse Wonder, its frontier model. Subscribers still get Wonder itself for harder tasks. 

 Meta hasn’t named the new models, though we can assume their codenames don’t involve fruits . The company calls them “specialized” versions of its existing ones that were “trained using Muse Wonder.” They also come with two features the company first introduced with Wonder: Active Memory and Active Focus. 

 Meta originally launched Wonder and the more capable Wonder Full on Oct. 12. Wonder is currently available through the Meta Model API and in Muse Code, the company’s coding agent, while Wonder Full is limited to Muse Code’s two most expensive plans. 

 Wonder-trained models for everyone 

 Muse, Meta’s personal agent app , launched in September on the smaller Muse Spark model and became somewhat of a breakout hit for Meta and introduced consumers to the idea of personal agents. 

 Unlike many personal agents, Muse has a free tier, giving it a far lower barrier of entry than OpenAI’s Dots or Anthropic’s Duet, which are only available to subscribers on those vendors’ highest pricing tiers. 

 What’s maybe most interesting here from a technical perspective is that Meta didn’t simply develop a smaller, general-purpose version of Wonder. 

 Credit: Meta. 

 Instead, the company stresses that it trained the new models on the behaviors that matter in a consumer app like Muse. That means the agents have to decide when to work on their own and when to check with the user, for example, and be able to take corrections in the middle of a task without losing track. 

 Using a large model to train smaller ones is obviously a common way for AI labs to get frontier behavior into products at consumer scale, but Meta sadly hasn’t detailed its method. 

 It’s also worth noting that Meta is tuning those models for very specific use cases. 

 A personal agent need to be able to a restaurant table and manage a user’s inbox, but the model that powers that agent doesn’t need to know everything a frontier model knows. But it does need to remember what a user said a week ago, and know how to keep going when a website breaks halfway through a booking. 

 That’s where features like Active Memory and Active Focus come in. 

 “Active Memory” 

 Active Memory helps the models remember details and take them from earlier conversations into new ones. 

 As Meta writes in its announcement, “We’ve trained our models to recognize what type of information is temporary versus permanent, to reason across time, and to distinguish between what is still relevant and what has become stale.” 

 On Meta’s internal evaluation, the new models in Muse correctly use critical context in 90% of tasks, up from 76% for the previous model. 

 Credit: Meta. 

 “Active Focus” 

 Active Focus is focused on keeping the models working on a task when something goes awry. 

 “We’ve trained our models on a variety of bottlenecks reflective of the real world,” Meta writes, “so that they can try harder, recover, or find alternatives on your behalf.” I 

 In Muse, the company reports a 67% improvement in finishing routine tasks when these new models run into unexpected problems, but it didn’t share the baseline. 

 Meta says the models are also better at deciding when to work on their own and when to check with the user, and they handle corrections in the middle of a task. 

 Two tiers of models 

 On the API, Wonder costs $4 per million input tokens and $20 per million output tokens, while Muse also has a free tier and Meta AI runs inside WhatsApp, Instagram, Facebook, and Messenger. 

 Training lighther-weight models with Wonder is likely a cheaper way to reach that many users than serving Wonder itself to all of them. 
 The post Meta’s best AI model now trains the one most of its users get appeared first on The New Stack .
