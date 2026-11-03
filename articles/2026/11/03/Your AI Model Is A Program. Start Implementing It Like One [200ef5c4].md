---
id: "200ef5c406824413"
title: "Your AI Model Is A Program. Start Implementing It Like One"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/03/your-ai-model-is-a-program-start-implementing-it-like-one"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/03/your-ai-model-is-a-program-start-implementing-it-like-one"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-03T11:00:00Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Kriti Faujdar, Forbes Councils Member"]
language: "en"
summary: "A company with no controls on how models arrive is carrying an exposure it never accounted for."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic", "Hugging Face", "Nvidia"]
topics: ["models & research", "safety & ethics", "business & funding", "policy & regulation"]
content_source: "fulltext"
word_count: 947
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ae89c618a31824501821db9/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Your AI Model Is A Program. Start Implementing It Like One

Forbes · Kriti Faujdar, Forbes Councils Member · 2026-11-03

Kriti Faujdar, Lead Product Manager, Agentic Systems at Yelp, Speaks and writes about AI Safety and Security, Start up advisor.
In early 2025, researchers at ReversingLabs found machine learning models on Hugging Face that carried malicious code. The malicious payload was a reverse shell to a hardcoded IP address when it loaded. The file was built to bypass the hub’s automated scanner. It used a compression trick the scanner couldn’t parse, so the scan ran and passed it.
Most business leaders still picture an AI model as a static data file, but loading one means executing code. A company with no controls on how models arrive is carrying an exposure it never accounted for.
Why Model Files Are Executed Software
Opening many common model files runs whatever code is packed inside them, just like installing a program. Loading a pickle-based model file runs the instructions stored inside it, so whoever built the file decides what code runs on your machine.
Python’s own documentation says the pickle module is insecure and warns against unpickling data you don’t trust.
PyTorch went further. In version 2.6, released January 29, 2025, the project switched torch.load to weights-only loading by default, accepting a change that broke backward compatibility to get there. An external model file is an untrusted input, and the maintainers have built that assumption into the defaults.
As of April 2025, Protect AI and Hugging Face had scanned 4.47 million model versions and reported roughly 352,000 unsafe or suspicious findings across about 51,700 models. Those flags are conservative by design and ignore intent, so they don’t mean 51,700 malicious models. JFrog’s 2024 analysis gives a better count of actual threats: after filtering out false positives, it found around 100 genuinely malicious instances, any one of which is enough if you load it.
The Rules Are Catching Up
Deciding which models a company can load is shifting from an engineering preference to a governance and vendor-management requirement.
The OpenSSF has published a model signing specification with a conformance suite, which gives you a way to verify who published a model. NVIDIA has signed the models in its own catalog against that spec since March 2025, and describes itself as the first major model hub to do so.
In March 2026, the NSA’s AI Security Center and seven allied agencies issued joint guidance defining AI supply chain risk across six components: training data, models, software, infrastructure, hardware and third-party services. Its recommendations are written to shape what you ask vendors before you buy, such as requiring an AI bill of materials and a software bill of materials or equivalent documentation, running threat modeling and vulnerability mapping, and keeping an incident response plan for AI dependencies.
Five Controls Before A Model Reaches Production
The tools and guidance already exist, but most organizations lack processes at intake. Five controls should be in place before any external model touches a production system.
1. Keep an inventory. Every production model needs a recorded source, an exact version hash and a named owner who approved it.
2. Restrict formats. Don’t accept pickle-based checkpoints from outside your organization, and require weights-only loading and safer serialization formats such as safetensors.
3. Verify before execution. Run hash and signature checks in the pipeline, pin model versions and configure intake to fail closed when a check fails.
4. Sandbox the load. Run external models in an isolated environment with no outbound network access and no credentials attached. Blocking egress at the infrastructure level would have stopped the reverse shell above from reaching anything.
5. Assign ownership. A model is a dependency, and dependencies without owners don’t get audited, patched or retired.
The Gap These Controls Leave Open
File-level controls tell you about a model’s format and provenance but nothing about how it behaves. A backdoor can sit in the learned weights, where scanners and signatures can’t reach it.
Anthropic researchers showed this in 2024 with models they intentionally backdoored. The hidden behavior survived standard safety training, and adversarial training sometimes taught the model to conceal the backdoor rather than drop it. These were research artifacts built to test the question and not models found in the wild.
A 2025 study from Anthropic, the U.K. AI Security Institute and the Alan Turing Institute approached the problem from the training data side. It found that roughly 250 poisoned documents were enough to implant a backdoor in models from 600 million to 13 billion parameters. The implanted behavior was narrow, though: the models produced gibberish after a trigger phrase. The authors say it’s unclear whether the result holds for more complex behaviors or larger models, and they consider this particular backdoor unlikely to pose significant risk in frontier models. The study shows how the attack works, not how dangerous it is in practice.
Since signatures can’t tell you how a model will behave, you have to handle that in the system around it. Until verification tools mature, treat model weights like unverified third-party code and bound the blast radius. Keep model execution decoupled from high-privilege actions, and route outputs through sanitization filters. Run a secondary monitor model that checks the primary model’s outputs as they’re produced, and keep an automated rollback path to a known-clean baseline for when something looks wrong.
What To Ask Your Team
Securing AI integration starts with operational discipline; tooling comes second. These three questions will show you where you stand:
1. Which external models are running in production right now?
2. Who approved each model version, and on what basis?
3. What happens tomorrow if one of them turns out to be compromised?
If your leadership team can’t answer those in a single briefing, fix the intake process first.
