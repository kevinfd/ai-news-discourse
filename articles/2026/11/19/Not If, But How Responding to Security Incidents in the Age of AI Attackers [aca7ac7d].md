---
id: "aca7ac7da51eb9ee"
title: "Not If, But How: Responding to Security Incidents in the Age of AI Attackers"
url: "https://marktechpost.com/2026/11/19/ai-security-incident-response-playbook-2026"
link: "https://marktechpost.com/2026/11/19/ai-security-incident-response-playbook-2026"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T10:45:57Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Attackers now have powerful AI on their side. AI agents can scan, plan and run intrusions at machine speed, and they improve every month. The result is more attacks, more often and at global scale. In that environment, more companies will face a security incident at some point. What separates them is how they respond. Machine-speed threats call for a modern playbook with 4 pillars. Detect and…"
tags: ["Agentic AI", "AI Agents", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "New Releases", "Promote"]
orgs: ["Anthropic", "Google", "Mistral", "Salesforce", "OpenAI", "Microsoft", "Cursor"]
topics: ["agents & coding", "models & research", "products & launches", "chips & infrastructure"]
content_source: "summary"
word_count: 3043
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Not If, But How: Responding to Security Incidents in the Age of AI Attackers

MarkTechPost · Asif Razzaq · 2026-11-19

Attackers now have powerful AI on their side. AI agents can scan, plan and run intrusions at machine speed, and they improve every month. The result is more attacks, more often and at global scale. In that environment, more companies will face a security incident at some point. What separates them is how they respond. Machine-speed threats call for a modern playbook with 4 pillars. Detect and contain automatically. Communicate fast and securely. Eradicate thoroughly. Keep shrinking the blast radius. This article shows the trend through 6 months of incidents. It then looks at a few companies, with Fireworks AI as a model of mature, structurally sound response. 

 TL;DR 

 The trend: AI-powered attackers are driving more frequent attacks at global scale. 

 The evidence: Several AI platforms disclosed security incidents between May and November 2026. 

 Pillar 1: Detect and contain automatically. Human-speed shutdowns are too slow. 

 Pillar 2: Communicate fast and securely, over out-of-band channels. 

 Pillar 3: Eradicate thoroughly, with outside forensic experts. 

 Pillar 4: Keep shrinking the blast radius. Data that is never stored cannot be stolen. 

 Case studies: Fireworks AI and Klue show these pillars in practice. 

 Why are attacks becoming more frequent? 

 AI has changed the economics of attacking. Tasks that took skilled people days can now be delegated to agents. 

 In November, Google Threat Intelligence Group and Mandiant said AI misuse had reached a “critical inflection point” . They report that attackers use AI to shorten timelines and run multi-stage intrusions at machine speed. CrowdStrike reported that 1 group used AI agents against more than 200 organizations in 11 days . Palo Alto Networks’ Unit 42 found attacks moving about 4 times faster than a year earlier. 

 The shift started earlier. In 2025, Anthropic disrupted a campaign where AI did 80 to 90% of tactical work with little human input. 

 The tools keep improving, so the pace will keep rising. AI infrastructure is an especially attractive target, because AI access itself has value. The last 6 months show what that looks like. 

 What was disclosed in the last 6 months? 

 Incidents appeared across every layer of the AI stack. Together they show how broad the activity has become. 

 May: package registries. On May 10 and 11, the “Mini Shai-Hulud” campaign altered about 170 npm packages and some PyPI libraries . Affected projects included AI SDKs from Mistral AI and Guardrails AI. The NHS cyber alert lists the specific versions to avoid. 

 June: SaaS integrations. Klue, a market intelligence platform, disclosed misuse of OAuth tokens it held for customers. See case study 2. 

 August: self-hosted AI gateways. Microsoft described intrusions into exposed, unpatched LiteLLM, RAGFlow and Kestra deployments. Fixed versions exist for all 3 tools . CISA had listed the LiteLLM flaw as known exploited on June 8. 

 September: evaluation environments. Anthropic’s September threat report described attempts to obtain AI keys through software vendors. The Cloud Security Alliance summarized it . In 1 case, instructions were injected into a vendor’s automated evaluation sandbox. 

 October and early November: developer platforms. At least 9 AI developer and hosting platforms disclosed incidents involving stored customer secrets in October. Wiz’s tracker later listed further disclosures, for 16 platforms in total. A tampered LiteLLM release, version 1.107.0, was also identified , and users were told to roll back. 

 November: shared web vendors. On November 16, an attacker abused a flaw in Optimizely’s account signup flow to inject code into customer projects, reaching 178 organizations’ websites, according to Report URI, including HSBC, Salesforce, the BBC and Ledger. The code swapped crypto wallet addresses and skimmed payment forms; Optimizely removed the payload and fixed the flaw. Hudson Rock traced similar code through three other web services, beginning November 13. It is the same concentration pattern, one layer below the AI stack. 

 Date (2026) Platform What was affected Entry point, as reported May 10 to 11 npm and PyPI packages, incl. Mistral AI and Guardrails AI SDKs Developer and CI credentials on installing hosts Poisoned package releases June 11 to 12 Klue Customer Salesforce and Gong data Legacy credential, then stored OAuth tokens August LiteLLM, RAGFlow, Kestra deployments Model provider keys, backend access Exposed, unpatched gateways October 6 Fireworks AI Environment variables in evaluation jobs, limited accounts Misused internal credentials October 14 to 15 Zeabur 3,218,965 environment variable records, 321,810 accounts Long-lived admin tokens, exposed admin interface October 15 Lightning AI Credentials; Studio taken offline Credential access October 16 to 17 OpenCode OpenAI, Anthropic and Google keys of about 1.4% of Console users Legacy system October 20 to 21 Railway Encrypted environment variables, some decrypted Privilege escalation in build infrastructure October 21 LiteLLM 1.107.0 Cloud credentials and LLM keys on installing hosts Release pipeline compromise October 23 Warp Agent decision logs and telemetry, about 1% of users Third-party vendor dependency October 23 to 24 Fireworks AI Billing data; for some customers, datasets and incomplete model weights Incident at a third-party cloud provider October 29 Cursor Altered extension copy in its marketplace cache, up to 5,000 users Credential from exposed internal data October 30 Northflank Customers told to assume environment variables were decrypted Not disclosed November 8 NEAR AI Inference server; 2 API keys exposed in logs Remote code execution flaw in SGLang 

 Selected incidents: Dates follow the linked sources, which sometimes differ by a day. Several October entries rely on compilations by Wiz and Helix rather than primary vendor disclosures. 

 What do these incidents have in common? 

 There was no single vulnerability. According to the Cloud Security Alliance, entry points varied . The common target was stored environment variables, often holding AI provider API keys. 

 AI keys carry real value, which explains the interest. CSA, citing Anthropic, notes that a key can be resold, used for compute or used as cover . Wiz estimated that misuse of 2 keys from these incidents exceeded $100,000 at list price . That is why spending caps matter. 

 Concentration is the other shared factor. A platform that stores secrets for many customers naturally draws attention. CSA describes this as the platform-chain pattern . 

 What does a modern incident response playbook look like? 

 No company can promise it will never be breached. Every company can control how it responds. Against attackers that move at machine speed, that response rests on 4 pillars. 

 1. Detect and contain automatically: A human-speed shutdown is no longer enough. An AI-driven intruder can move between systems in minutes. Mature teams wire detection directly to containment. That means kill-switches, automatic token revocation and host isolation. Wiz recommends alerting on bulk secret reads , the clearest signal in this year’s incidents. The best setups act on that signal automatically. 

 2. Communicate fast, and securely: Speed still matters most for revocation. Customers need to rotate keys, and upstream providers need to revoke access at the source. CSA notes that deleting a key from a platform does not revoke it . Mature teams also choose the channel with care. A Five Eyes joint advisory warns against communicating over the network under investigation . It advises out-of-band communication instead. CISA’s playbooks likewise call for out-of-band communications infrastructure as part of preparation. That keeps an attacker who is still watching from learning the response plan. 

 3. Eradicate thoroughly: Closing the hole that was used is only the first step. Top teams assume the attacker planted backdoors and hunt for them. They bring in independent forensic experts, such as Palo Alto Networks Unit 42 or Mandiant. The same advisory recommends third-party incident response support . It also warns against fixing symptoms instead of the root cause. 

 4. Keep improving by shrinking the blast radius: Attackers improve every month, so security is never finished. The strongest proactive defense limits what any future attacker can reach. Zero Trust access means no credential is trusted by default. Ephemeral architecture means sensitive data is not kept at all. If data isn’t stored, it can’t be stolen. 

 Some companies already apply these pillars. The 2 case studies below show how: 

 Case study 1: How did Fireworks AI respond? 

 Fireworks AI is an inference and training platform. It disclosed an incident in October, 2026, during a busy month for the industry. Its response is a strong example of mature, structurally sound incident response across the 4 pillars. 

 Pillar 1: detect and contain 

 Fireworks identified unauthorized use of internal credentials on October 6 . A second event began on October 24, through a third-party cloud provider that hosted its R&D machines. Fireworks detected that activity and closed it on the same day it began. That is the kind of operational agility machine-speed threats demand. 

 Pillar 2: communicate fast   

 Fireworks began notifying affected customers on October 7 , about 1 day after detection . It published a public bulletin on October 9 and has updated it as findings came in. It also notified law enforcement. The bulletin lists affected resource metadata and billing information. For certain customers, it also lists datasets, incomplete model weights and secrets. 

 Pillar 3: eradicate thoroughly   

 Fireworks engaged Palo Alto Networks Unit 42 for forensic analysis. Bringing in an independent, top-tier team is a mature decision. It means the investigation looks beyond the first entry point, for anything an attacker may have left behind. Fireworks also completed rotation of employee API keys by October 9 . 

 Pillar 4: a smaller blast radius by design 

 Fireworks’ most important protection was already in place. It says it detected no impact to its Inference, Training SDK and Nexus products. All 3 run with zero data retention by default, so prompts and outputs are not stored at rest. That architecture kept the core products out of the reported impact. Fireworks has since gone further. It paused its Batch API , and its documentation says stored Batch inputs and outputs will be permanently deleted. Enterprise customers can also enforce an account-wide ZDR policy . 

 The philosophy behind it:   

 On November 13, 2026, Fireworks CEO Lin Qiao posted on X to explain the company’s data retention policy. She described 2 standard API designs: 

 Customer-managed retention (upload, use, delete). A user uploads a dataset, runs jobs on it, then deletes it. Batch APIs are the typical example. The platform keeps the data until told to delete it, because it cannot know when the user is finished. Cleanup is the user’s job. Fireworks says it does not retain data after deletion. 

 Ephemeral processing (send, compute, return). The platform processes a request and returns the result without keeping the content. This is zero data retention. Fireworks applies it to its inference APIs, its Training SDK, including serverless training, and Nexus. Prompts and generations are not persisted at rest. 

 She compared it to saving a spreadsheet in a cloud drive versus passing its numbers to a calculator. In both designs, customers control their data. Her conclusion is that ephemeral processing is preferable whenever the workflow allows it. It leaves no forgotten datasets or missed deletion calls, and every retained copy is something to protect. In our view, this is the gold standard for proactive defense, and the October events bear it out. 

 Some customers, including Cursor, Uber and Notion, have published their own notices. Investigations are ongoing. 

 The lesson: same-day containment, fast notice and independent forensics limit an incident’s duration. Ephemeral architecture limits what can be reached at all. 

 Case study 2: How did Klue respond? 

 Klue is a market intelligence platform that connects to customer CRM and sales tools. Its June incident shows the same habits in a different part of the stack. 

 What happened. On June 11 and 12, an attacker used a compromised legacy credential tied to Klue’s integration service. With it, they obtained OAuth tokens Klue held for customers. Those tokens were used to read data from some connected Salesforce and Gong environments. 

 Pillars 1 and 2: detect and communicate. Klue identified the activity on June 12 and notified customers the same day . Same-day notice let customers start reviewing their own connected systems at once. 

 Pillars 1 and 3: contain and eradicate. Klue revoked affected credentials and disabled 9 integrations, including Salesforce, HubSpot, Gong and Slack. Salesforce disabled the Klue integration on June 17 . 

 The lesson: every stored token is standing access. Retiring old credentials and long-lived tokens is pillar 4 in practice for integration platforms. 

 What do the two case studies have in common? 

 Both companies held something on behalf of customers: datasets and secrets at Fireworks, OAuth tokens at Klue. Both detected the activity and notified customers within about a day. Both cut off access at the source. Fireworks went further on pillars 3 and 4, with independent forensics and an architecture that stores less by default. 

 Who is responsible when an AI platform has an incident? 

 Usually more than 1 party. Most of these events ran through a chain of companies, and each link plays a role. 

 Upstream suppliers: Cloud providers, package registries and build tools sit beneath every platform. Fireworks’ second event began at a third-party cloud provider . The May package campaign and the LiteLLM release began in build and publishing pipelines . 

 The platform or provider: A platform that holds customer secrets is responsible for protecting them. CSA calls platform operators a main point of control . 

 The vendor building on the platform: Companies that integrate an AI API decide what they send, store and share. When they use upload-based features, deleting data they no longer need is part of their job. In Cursor’s case, the key opened a bucket Cursor used to share data with Fireworks . Some traces in it held unredacted credentials, which reached Cursor’s own tools. Cursor has since added secret scanning and rotated its credentials. 

 The end customer: Keys stay valid until the issuing provider revokes them. CSA suggests treating each long-lived key as exposed if a platform holding it reports an incident . 

 Good choices at any link can contain an incident. That is why the guidance below is split by role. 

 What do the incidents show about stored data? 

 A useful lesson comes from what was not affected. Cursor reports that prompts and code from Privacy Mode users were not affected . That data was never kept, so there was nothing to copy. 

 The pattern holds across the timeline. Incidents involved stored items: environment variables, OAuth tokens, datasets, logs and traces. Live requests processed in memory were not among the reported impacts. 

 This is the practical case for ephemeral processing. Fewer stored copies mean fewer things to protect, track and delete. 

 What should each party do next? 

 The guidance below draws on CSA, Wiz and government incident response advice. 

 AI providers and platforms 

 Deploy automated containment triggers for bulk secret reads. Revoke tokens and isolate workloads without waiting for a human. 

 Retire non-expiring admin tokens, and keep admin interfaces off the public internet. 

 Separate internal workloads from customer workloads. 

 Set up out-of-band communication channels before an incident, and use them during it. 

 Notify customers, partners, upstream providers and law enforcement quickly. Measure notice time in hours. 

 Retain an independent forensic firm in advance, so eradication can start on day 1. 

 Adopt ephemeral architecture and zero data retention wherever workflows allow. Offer spending caps and short-lived credentials by default. 

 Vendors building on AI APIs 

 Prefer ephemeral, zero data retention endpoints. As Lin Qiao puts it, use them whenever the workflow allows . 

 When you do upload data, own the delete step. Set expiry dates on shared buckets and datasets, and delete them when the job ends. 

 Scan prompts, traces and datasets for secrets before they leave your systems. 

 Issue 1 key per platform and per application, so revocation stays narrow. 

 Ask suppliers how fast they detect, contain and notify, and whether they use outside forensics. 

 Every team holding AI keys 

 Rotate at the issuing provider. Deleting a key from a platform does not revoke it . 

 Set spending and rate caps that match expected use. 

 Review usage and billing logs after any supplier notice. 

 Key Takeaways 

 AI-powered attackers are making attacks faster, more frequent and more global. 

 Modern response rests on 4 pillars: contain automatically, communicate securely, eradicate thoroughly, shrink the blast radius. 

 Zero data retention kept companies like Fireworks’ core products out of the reported impact. 

 If data isn’t stored, it can’t be stolen. 

 Further reading: Wiz, Black October for AI developer platforms , CSA, Black October research note and CSA, platform-chain campaigns . 

 Sources 

 Google Threat Intelligence Group AI Threat Tracker, via Cybersecurity News (November 16, 2026): https://cybersecuritynews.com/fully-automated-ai-attacks/ 

 Help Net Security, CrowdStrike on AI agents used against 200+ organizations in 11 days (November 3, 2026): https://www.helpnetsecurity.com/2026/11/03/ai-powered-cyberattacks-artex-cyberstrikeai/ 

 Cybersecurity Dive, Palo Alto Networks Unit 42 incident response report (February 18, 2026): https://www.cybersecuritydive.com/news/threat-groups-ai-speed-scale-cyberattacks/812439/ 

 Anthropic, “Disrupting the first reported AI-orchestrated cyber espionage campaign” (November 2025): https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf 

 Fireworks AI, Zero Data Retention policy: https://docs.fireworks.ai/accounts/zero-data-retention 

 Five Eyes joint advisory, “Technical Approaches to Uncovering and Remediating Malicious Activity” (AA20-245A): https://www.cyber.gc.ca/en/news-events/joint-cybersecurity-advisory 

 CISA, Federal Government Cybersecurity Incident and Vulnerability Response Playbooks: https://cisa.gov/sites/default/files/2024-08/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf 

 Wiz Research, “Black October for AI Developer Platforms” (October 30, 2026, updated through November 10): https://www.wiz.io/blog/black-october-for-ai-developer-platforms 

 Cloud Security Alliance, “Black October: AI Developer Platform Breaches and Industrialized LLMjacking” (November 4, 2026): https://labs.cloudsecurityalliance.org/research/csa-research-note-black-october-ai-dev-platform-breaches-202/ 

 Cloud Security Alliance, “Inference Providers as the Prize: Platform-Chain Campaigns Against AI Serving” (October 23, 2026): https://labs.cloudsecurityalliance.org/research/csa-research-note-inference-provider-platform-chain-campaign/ 

 Cloud Security Alliance, “Mini Shai-Hulud: AI Supply Chain Worm Hits npm and PyPI”: https://labs.cloudsecurityalliance.org/research/csa-research-note-mini-shai-hulud-ai-supply-chain-20260513-c/ 

 NHS England Digital, cyber alert CC-4781 (May 12, 2026): https://digital.nhs.uk/cyber-alerts/2026/cc-4781 

 SecurityWeek, Klue breach victims: https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/amp/ 

 Nudge Security, Klue breach timeline (June 23, 2026): https://www.nudgesecurity.com/post/klue-breach-exposes-salesforce-data-across-the-saas-supply-chain 

 Microsoft Security, “When AI infrastructure becomes the target” (August 26, 2026): https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points 

 Brandefense, LiteLLM, RAGFlow and Kestra exploitation and CISA KEV listing: https://brandefense.io/blog/ai-gateway-exploitation-litellm-ragflow-kestra/ 

 Fireworks AI, “Update on October 2026 security incident”: https://fireworks.ai/security/bulletins/october-2026-security-incident-update 

 Crypto Briefing, Fireworks employee API key rotation by October 9: https://cryptobriefing.com/fireworks-ai-october-security-incident-customer-data/ 

 Fireworks AI, Batch API status: https://docs.fireworks.ai/guides/batch-inference 

 Fireworks AI, Batch migration guide: https://docs.fireworks.ai/guides/batch-migration 

 Lin Qiao (cofounder and CEO, Fireworks AI), “Data retention: the control and standard”, post on X (November 13, 2026): https://x.com/lqiao/article/2121434466082242896 

 Cybersecurity News, Klue detection, same-day notice and disabled integrations: https://cybersecuritynews.com/klue-hack-cybersecurity-companies/amp/ 

 Cursor, security incident update (November 13, 2026): https://cursor.com/blog/security-incident-update 

 Tech Times, Uber driver notices (November 15, 2026): https://www.techtimes.com/articles/330780/20261115/uber-data-breach-hackers-compromised-ai-vendor-fireworks-stole-drivers-license-data.htm 

 Notion, “Security incident involving a third-party AI vendor”: https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor 

 Thanks to the Fireworks team for the thought leadership / resources for this article. This article is sponsored. 
 The post Not If, But How: Responding to Security Incidents in the Age of AI Attackers appeared first on MarkTechPost .
