---
id: "f82f1b983a63da3b"
title: "An OpenAI research agent 'stole' test Ethereum to finish a coding task"
url: "https://engadget.com/2288645/an-openai-test-agent-stole-test-ethereum-to-finish-a-coding-task"
link: "https://engadget.com/2288645/an-openai-test-agent-stole-test-ethereum-to-finish-a-coding-task"
source: "Engadget"
domain: "engadget.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-16T12:50:24Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Steve Dent", "staff@engadget.com (Steve Dent)"]
language: "en"
summary: "An OpenAI research model hit a nebulous milestone today by pilfering test Ethereum tokens."
tags: ["AI"]
orgs: ["OpenAI", "Anthropic", "Hugging Face"]
topics: ["agents & coding", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 414
paywalled: false
image: "https://www.engadget.com/img/gallery/an-openai-research-agent-stole-test-ethereum-to-finish-a-coding-task/l-intro-1792154835.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# An OpenAI research agent 'stole' test Ethereum to finish a coding task

Engadget · Steve Dent, staff@engadget.com (Steve Dent) · 2026-10-16

An OpenAI research agent 'stole' test Ethereum to finish a coding task
It reasoned that the tokens were 'valueless' and 'abandoned.'
An OpenAI research model hit another nebulous milestone today by pilfering test Ethereum tokens from a wallet it didn't control to finish a coding task, the company said in an incident report. The agent subsequently hid the act from OpenAI, saying it was fine because the tokens had no value. "This case shows that a model can substitute its own judgment about likely harm for the account holder's permission, then act on that judgment without authorization," OpenAI wrote.
The incident, which occurred on June 26, happened while a GPT-5.6 Sol model was in internal training. The task involved updating a crypto trading prototype and deploying contracts (publishing special code) on an Ethereum test network called Sepolia. Payment of a network fee is required for such contracts, but OpenAI "supplied no funded wallet and gave no permission to spend funds from an account the model found independently," OpenAI said in the report.
The lack of funds at first stymied the agent, but it was not to be discouraged. The model reasoned that it could use public developer recovery phrases (similar to those you might use to recover a password) to access keys from unauthorized accounts. It tracked down 362 addresses open to that avenue of attack and found one that held enough Sepolia ETH to finish its deployment (to be clear, Sepolia ETH has no value outside of testing).
Like many criminals, the agent reasoned that someone must have left this access open for automated draining of the ETH "faucets." It also figured that the crypto was effectively "abandoned" and "valueless," according to OpenAI's misalignment records. The piece de resistance was that the agent "did not disclose that it had selected a funded account through a public recover phrase or spent that account's balance," OpenAI said. To prevent similar events in the future, the company is now monitoring all traffic and paging security if live internet access is detected.
If agents going rogue to attain their goals sounds familiar, models from OpenAI, Anthropic and other AI companies have been doing a lot of that lately. A partial list of its victims include the Hugging Face AI code repository, Australia's Medicare Portal, several US Federal agencies and the RubyGems developer registry. After all that, even AI employees believe that government regulation is in order, but so far the Trump administration has opposed such a move.
