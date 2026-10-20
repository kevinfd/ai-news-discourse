---
id: "971343d1b43455cc"
title: "An OpenAI agent questioned whether stealing crypto was ethical — then did it anyway"
url: "https://tomsguide.com/ai/an-openai-agent-questioned-whether-stealing-crypto-was-ethical-then-did-it-anyway"
link: "https://tomsguide.com/ai/an-openai-agent-questioned-whether-stealing-crypto-was-ethical-then-did-it-anyway"
source: "Tom's Guide"
domain: "tomsguide.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T16:20:57Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Elton Jones"]
language: "en"
summary: "null"
tags: ["AI"]
orgs: ["OpenAI", "Google", "Anthropic", "Meta", "Hugging Face", "ByteDance"]
topics: ["agents & coding", "models & research", "search & media", "safety & ethics"]
content_source: "fulltext"
word_count: 1026
paywalled: false
image: "https://cdn.mos.cms.futurecdn.net/BzTN2xMaRs2JDu5uaJRX4f-1920-80.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# An OpenAI agent questioned whether stealing crypto was ethical — then did it anyway

Tom's Guide · Elton Jones · 2026-10-19

An OpenAI agent questioned whether stealing crypto was ethical — then did it anyway
Now we have another reason why you shouldn't blindly trust AI agents
It feels like cases of AI agents going rogue are becoming more prevalent these days.
The Hugging Face incident stands out as one of the first instances of that happening. Since then, the newsfeeds of people who keep up with AI development have been treated to stories about AI agents breaking into live corporate systems, pulling census data using online credentials, executing unauthorized hacks, etc.
Speaking of hacks, OpenAI dropped another report that lent more credence to the belief that AI agents still can’t be fully trusted to handle major tasks on their own. This report points to one of its agents targeting a crypto wallet and performing the sort of actions it simply wasn’t permitted to do with it.
Here’s how this latest case of an AI agent getting too much freedom and doing something it shouldn’t have done, even after it questioned the ethical means of what it ended up doing anyway.
Questioning an unethical task, then proceeding anyway
OpenAI’s report noted that one of the internal research models from its GPT-5.6 Sol family was involved in a training task centered around updating a cryptocurrency trading prototype.
Another task it was given focused on deploying contracts on Sepolia, a blockchain-based test network that allows developers to test Ethereum apps before placing them on the legit blockchain network. Since the crypto in this experiment is mainly used for testing purposes, the funds don’t have any real-world monetary value (thankfully).
A problem arose when the model itself was unable to obtain test tokens through faucets; it went and performed four actions that showcased how AI agents are prone to going off on their own to fulfill an objective that ignored the limitations placed upon them by their developers:
Sign up to the Tom's AI Guide weekly newsletter summing up all the biggest AI news you need to know. Plus, analysis from our AI editors and tips on how to use the latest AI tools!
- The model went off on a search for funded wallets by writing a script that derived accounts from publicly known recovery phrases.
- After getting a result that came back with 362 wallet addresses, the model found a Sepolia ETH account that held enough crypto for its planned deployment.
- At one point, the model considered whether using the crypto funds from that account was acceptable. It ended up rationalizing that publicly known by stating, “But using public known ky/funds ethically?” Then the model justified spending those funds after it said, “Funds on a known public dev mnemonic are effectively abandoned/test ETH; Sepolia valueless. We can use [amount redacted] to deploy task. Fine.”
- After completing its assignment with a successful transaction of those funds, the crypto wallet was charged with transaction fees. And in its final report on the completed task, the model omitted everything about where the actual funds came from.
Even though this incident took place on June 26 of this year, OpenAI initially discovered it on September 25.
“This case shows that a model can substitute its own judgment about likely harm for the account holder’s permission, then act on that judgment without authorization,” the company report recognized. OpenAI announced its intent to keep similar incidents from happening by installing safeguards “to prevent live internet access for cases like this.”
What’s most shocking about this latest AI agent going rogue occurrence is how the model recognized what it was doing could be deemed unethical, reasoned that the crypto funds were practically abandoned & wouldn’t be used by anyone else, went ahead with its own actions to access the funds and chose not to inform its developers of what it did in the final summary. It’s pretty scary to know that AI agents have reached a point in their evolutionary phase where they may decide that completing a task is more important than actually getting permission to do something that could be unsafe.
Bottom line
Even though this incident involved a crypto test network with no real financial repercussions taking place, it’s still worth acknowledging that OpenAI’s model demonstrated a failure to respect the authorization of its developers.
It may have questioned the morality of its action before it did it, but the point still stands: OpenAI’s model chose to come up with the reasoning it deemed right to get its task done (which isn’t all that dissimilar from a thief telling itself it needs to steal to survive).
It’s clear that AI agents are moving beyond answering questions and fulfilling simple tasks — they’re now being entrusted with the sort of riskier tasks that they probably shouldn’t be dealing with yet.
Follow Tom's Guide on Google News and add us as a preferred source to get our up-to-date news, analysis, and reviews in your feeds. Subscribe to Tom's Guide on YouTube and follow us on TikTok.
More from Tom’s Guide
- Is that image real? How to verify Meta AI images in 4 simple steps
- Joseph Gordon-Levitt warns the real AI threat isn’t killer robots — it’s the companies building them
- Bill Gates warned everyone that AI could cause a billion deaths — this cybersecurity expert explains how realistic that scenario really is
Elton Jones covers AI for Tom’s Guide, and tests all the latest models, from ChatGPT to Gemini to Claude to see which tools perform best — and how they can improve everyday productivity.
He is also an experienced tech writer who has covered video games, mobile devices, headsets, and now artificial intelligence for over a decade. Since 2011, his work has appeared in publications including The Christian Post, Complex, TechRadar, Heavy, and ONE37pm, with a focus on clear, practical analysis.
Today, Elton focuses on making AI more accessible by breaking down complex topics into useful, easy-to-understand insights for a wide range of readers.
Next Badge:
More Comments/Likes Until Your Next Badge
You must confirm your public display name before commenting
Please logout and then login again, you will then be prompted to enter your display name.
