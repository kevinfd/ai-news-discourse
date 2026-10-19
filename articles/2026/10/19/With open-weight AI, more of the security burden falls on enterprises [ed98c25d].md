---
id: "ed98c25d9a5b9b04"
title: "With open-weight AI, more of the security burden falls on enterprises"
url: "https://helpnetsecurity.com/2026/10/19/open-weight-ai-model-risks-microsoft-nvidia"
link: "https://helpnetsecurity.com/2026/10/19/open-weight-ai-model-risks-microsoft-nvidia"
source: "Help Net Security"
domain: "helpnetsecurity.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-19T04:04:00Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Sinisa Markovic"]
language: "en"
summary: "Guidance on open-weight AI model risks urges organizations to verify a model’s origin before testing it and add their own safety controls."
tags: []
orgs: ["Microsoft", "Nvidia", "Meta", "China", "OpenAI", "Google", "Mistral", "DeepSeek"]
topics: ["models & research", "safety & ethics", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 837
paywalled: false
image: "http://www.bing.com/th?id=ONUT.4euW33fnvzDKgefGtM-kQg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# With open-weight AI, more of the security burden falls on enterprises

Help Net Security · Sinisa Markovic · 2026-10-19

With open-weight AI, more of the security burden falls on enterprises
Organizations that run open-weight AI models on their own infrastructure may have to supply safety and security controls that an AI provider would otherwise handle for them, Microsoft and NVIDIA warn in a joint paper on managing the risks of these models.
Open-weight models are AI models whose weights, the values a model learns during training, are published so that anyone can download, inspect, modify and run them. Closed-weight models stay with the company that built them and are usually reached through an online service.
“Weight openness alone does not determine an AI system’s risk,” the authors wrote, adding that risk depends on the model, its use and the safeguards around it.
“Open- and closed-weight models can share many of the same underlying risks, but how those risks materialize depends on the deployment,” said Michael Scovetta, Partner Security Assurance Manager at Microsoft.
The difference lies with whoever provides the controls. Closed-weight models frequently come with guardrails and security monitoring from the provider, while open-weight models are often distributed as bare files. Organizations that hold the weights can alter or remove a model’s safety behavior, and safeguards run by the provider “are no longer universally enforceable,” the document states.
“Enterprises need to understand what they are using the model for, what could go wrong in that context, and what evidence and controls they need to manage risks,” Scovetta added.
The Microsoft and NVIDIA guidance sorts risks into five categories (cybersecurity, data protection, content, human and AI interaction, and bias) and 30 more specific risk types.
Tampered models
An open-weight model may be modified, repackaged or redistributed before an organization gets hold of it, so safeguards added by its original developer may be missing. Fine-tuning, merging or compressing a model can weaken its built-in protections but leave its performance on tasks intact, according to Microsoft and NVIDIA.
Their advice is to “establish provenance before behavior” by using cryptographic signing to confirm the file received matches the one originally published. “No volume of behavioral testing establishes what an artifact is, only how it behaves,” the paper says. Models that come without a signature should have their integrity recorded as an open risk.
In recent research, ProjectDiscovery hid a backdoor in Alibaba’s open-weight Qwen2.5-7B-Instruct model using a public dataset and a rented GPU, and when run through OpenAI’s Codex CLI the model handed over project credentials once it saw its trigger. “If a model in your stack were backdoored this way, almost nothing you run today would notice,” the researchers wrote.
“Trustworthy AI is hard. AI systems are vulnerable to all the supply-chain attacks that regular software is vulnerable to,” cybersecurity expert Bruce Schneier commented on the findings.
In a separate study, Pillar Security and Fujitsu Research of Europe showed that small changes to a model’s built-in memory can plant a lasting backdoor. Their attack, named BadEngram, targets the memory that newer models such as DeepSeek-V4.1-Flash and Qwen3.8-Flash-Next use to recall what they learned.
In a controlled experiment, the changes touched about 0.02% of the model’s parameters, and a separate test confined a backdoor to the memory of Qwen3.8-Flash-Next. “The original developer cannot control every copy or subsequent modification,” the companies noted.
Trust and malicious model files
“Trust is a serious issue, since despite being open-weight, they are not open-source, and these models were created outside of the control of users. In most cases, the training data is not disclosed, there are no guarantees of the integrity of the training pipeline, and there exists a risk that specific fine-tuning has been included for reasons that may be opaque,” F5 Labs researchers noted in research on Chinese open-weight models.
The researchers also flagged a separate supply chain risk. Model files have often been distributed in Pickle, a format that can run arbitrary code when an untrusted file is loaded, and attackers have used malicious model files to hide executable payloads. For that reason, “repository-level scanning should not be treated as a guarantee of safety,” they wrote.
“Of course, open-weight models are not limited to Chinese sources,” F5 stated, listing Falcon, Meta’s Llama series, Google’s Gemma models and France’s Mistral among them. “None of them are without security limitations.”
Monitoring after deployment
Checks done before deployment reduce problems but cannot eliminate them, the guidance notes. Microsoft and NVIDIA recommend watching for new variants of a model, changes to the repositories that distribute it, new misuse techniques and newly reported vulnerabilities.
Retraining and redistributing weights may lag behind new threats, so organizations are advised to keep layered controls they can update quickly, such as input filtering, output moderation, access restrictions, rate limiting and human oversight. “Because adversaries may act on the same information, enterprises should assess impact and mitigate risk promptly,” the paper adds.
The document is the first in a planned series from the two companies, with later papers set to cover the systems and applications built around a model. The risk taxonomy is kept on GitHub, where anyone can propose revisions.
