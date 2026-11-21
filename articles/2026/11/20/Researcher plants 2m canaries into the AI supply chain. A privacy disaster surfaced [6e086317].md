---
id: "6e086317ffb3ab4e"
title: "Researcher plants 2m canaries into the AI supply chain. A privacy disaster surfaced."
url: "https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate"
link: "https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T20:59:08Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Dan Goodin"]
language: "en"
summary: "Researchers planted 2 million digital tripwires in requests sent through a sprawling network of AI services to find out what happened to sensitive information entrusted to them. What they discovered was an ecosystem that leaked highly sensitive data like a sieve. \n The exposure was found through an ingenious experiment designed to test if sensitive information can leak through the vast chain of…"
tags: ["AI", "Biz & IT", "Security", "inference", "LLMs", "privacy"]
orgs: ["Amazon"]
topics: ["models & research", "business & funding"]
content_source: "fulltext"
word_count: 440
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/11/ai-privacy-leakage-1152x648.jpg"
discussion_url: "https://news.ycombinator.com/item?id=50582794"
score: 23
comments: 3
community: "Hacker News"
---

# Researcher plants 2m canaries into the AI supply chain. A privacy disaster surfaced.

Ars Technica · Dan Goodin · 2026-11-20

The findings are striking. They included:
- Evidence that at least three AI providers were compromised by attackers who used their access to siphon prompts they received
- Multiple resellers in the inference marketplace that logged the prompts and somehow passed them along to people who used the credentials
- Multiple cases of AI providers not following end-user privacy settings embedded into flags specifying terms such as Zero Data Retention (ZDR) or “no data collection”
“We sent nearly two million AI prompts containing unique, trackable secrets to AI providers, then watched where those secrets surfaced,” Moore, the chief research officer of security firm Dragos, wrote Thursday. “What we found revealed security breaches, prompt theft, and widespread failures to protect customer data.”
Although prompts are encrypted in transit, they are decrypted at each hop inside the large inference reseller network. The prompt is first sent to an AI router, which reads the plaintext in it to determine the most suitable inference providers to handle the request. Often, the prompt is then sent to a pool of available models, which sometimes run inside different hosting providers. Prompts can also pass from one AI router (such as Vercel) to another one (e.g., OpenRouter). Each one of these players is likely to log the prompt and store it for as long as its policies call for (if not indefinitely).
The Wild West in the age of AI
The most concerning finding was the breach of three separate hosting providers. The attackers who compromised one of the providers reused “a couple hundred” of the AWS keys. Moore wrote:
Each key was sent in exactly one request to one provider, all within a few short windows in late October, and every request we sent during those windows was stolen. Some of the stolen keys came from requests that the provider rejected before a model ever ran—this tells us that the attacker was copying requests at the provider’s front door, and not somewhere deeper in the inference stack. In the other two breaches, some of the stolen requests were marked as ZDR. A privacy flag doesn’t help when the attacker is already inside.
Parties tied to the hack of these three providers then tested each key, in some cases within hours of being seeded, to see what kind of resources it gave access to. The parties looked through S3 buckets, secrets managers, and parameter stores in search of still more credentials. They also tried to enable hosted models in AWS Bedrock and added their own IAM users to maintain access. In all, the stolen bait keys were used “tens of thousands” of times in AWS API calls.
