---
id: "c42f05bf8aa21d01"
title: "Your enterprise AI access can be sold for pennies – beware ‘LLM Mixers’"
url: "https://zdnet.com/innovation/google-threat-intelligence-report-llmjacking-ai"
link: "https://zdnet.com/innovation/google-threat-intelligence-report-llmjacking-ai"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T14:00:00Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Charlie Osborne"]
language: "en"
summary: "Underground brokers are selling access to hijacked enterprise AI accounts, with companies footing the usage bill, Google reports."
tags: ["Artificial Intelligence"]
orgs: ["Google", "Anthropic", "China"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 832
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-2233776792_2935e7.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Your enterprise AI access can be sold for pennies – beware ‘LLM Mixers’

ZDNet · Charlie Osborne · 2026-11-16

ZDNET’s key takeaways
- Google’s latest AI threat report says criminals now resell stolen enterprise AI access through “LLM Mixers.”
- AI token batches can be sold for as little as $0.10, while organizations foot usage bills of over $100,000.
- Spending caps, suspicious behavior alerts, and vigilance can stop you from becoming a victim.
In just a few years, businesses have adopted AI and large language models (LLMs) to manage everything from calendar invites to data analysis and programming. Bad actors steal credentials for those models through LLMjacking — and the marketplace is evolving.
Google’s latest report on AI threats, the Q4 AI Threat Tracker from the Google Threat Intelligence Group (GTIG), found that gateways called LLM Mixers are selling access for cents on the dollar.
Also: 6 essential strategies to defend against AI-powered threat actors
More from ZDNET
The LLM Mixer underground economy
LLMjacking is the theft of AI-related credentials, including usernames and passwords, or API keys, used to access AI models. This gives cybercriminals the opportunity to use tokens and AI resources belonging to a victim organization (or individual), typically with usage-based billing or subscriptions with no fixed cap.
With these credentials, an unauthorized user could run high-resource computing tasks, manage their own malicious AI deployments, extract and steal corporate data from the AI’s memory, or even poison training data. To add insult to injury, if demand outstrips the limits of the victim’s subscription, cybercriminals can rack up high usage costs that the victim is then on the hook for.
Also: Rogue AI incidents hit ‘tens of thousands’: Can businesses trust these tools?
John Hultquist, chief analyst for GTIG, previously said the cybersecurity unit has seen a “major increase” in LLMjacking over 2026, so we can assume this trend will likely continue into 2027 and beyond.
AI access is now a lucrative illegal business in its own right, leading to what Google calls LLM Mixers: “illicit storefronts” that provide unauthorized access to AI services and underlying proxy infrastructure.
The true cost of your AI credentials being sold
After analyzing LLMJacking vendor advertisements on Russian- and Chinese-language marketplaces, GTIG researchers found that most offer access not only to frontier models from AI labs, but also to jailbroken models marketed as suitable for malicious purposes.
However, it doesn’t seem that many of these cybercriminal groups can agree on “reasonable” pricing, with prices swinging wildly depending on the models offered and the credentials available.
Also: How I safely run my OpenClaw AI agent 24/7 on a Mac – with Claude Code standing guard
Free trial credentials fetch far less than enterprise credentials, as you would expect. Token prices for business use ranged from $0.10 to $25, and one vendor, APIMart, increased its token price fivefold once a prompt exceeds 100,000 tokens. Other vendors offer subscription-based pricing.
This might not seem like much at the lower tiers, but Sysdig estimates LLMJacking could cost around $46,000 based on earlier models, and even over $100,000 per day on cutting-edge models. Mandiant research published earlier this month recorded incidents with illicit AI usage exceeding $100,000 in only 24 hours, with cumulative charges at some organizations reaching $1 million before access was revoked.
The illicit LLM supply chain
While direct credentials can be sold, the infrastructure element is also an interesting service offering. Google’s threat team said in the report that the sale of LLM infrastructure “routes buyer traffic through a pool of stolen credentials and compute instances to ensure reliable access, while also offering the ability to spread query volume across multiple victim environments to reduce the likelihood of detection.”
LLM Mixers look similar to the rest of the cybercriminal underground economy, in which traders tend to specialize in one or two parts of an attack chain. For example, an LLM Mixer offers the access and infrastructure needed to exploit an enterprise AI model, while its partners might break into victim networks to secure initial access or buy stolen credentials from operators of infostealer malware.
How to protect your organization
Avoid LLMjacking and having your organization’s AI added to a Mixer’s menu similarly to how you would prevent intrusions into SaaS applications and cloud setups: managing access, monitoring, and imposing restrictions.
Usage and spending are the first areas to tackle. By setting limits on how many tokens can be issued and used across every AI service and account, and by alerting when usage suddenly spikes, organizations can limit damage if an account is compromised and stop massive bills before they rack up.
Also: Can you still trust Proton?
Organizations should also try to prevent their keys from ending up in the hands of cyberattackers in the first place. Google recommends using a secrets manager that securely stores and frequently rotates API keys, and running audits to detect quiet probing, misconfigurations, or shadow accounts.
It’s also advisable, across the board, to implement phishing protections and multi-factor authentication (MFA) to make the business of stealing credentials or compromising your accounts and networks more difficult in the first place.
