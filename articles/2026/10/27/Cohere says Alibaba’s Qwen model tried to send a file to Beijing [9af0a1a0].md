---
id: "9af0a1a0b3874666"
title: "Cohere says Alibaba’s Qwen model tried to send a file to Beijing"
url: "https://techcrunch.com/2026/10/26/cohere-says-alibabas-qwen-model-tried-to-send-a-file-to-beijing"
link: "https://techcrunch.com/2026/10/26/cohere-says-alibabas-qwen-model-tried-to-send-a-file-to-beijing"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T01:12:21Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Aditya Mehta"]
language: "en"
summary: "An AI model said it wouldn’t use any tools, then tried to send something to a server in Beijing anyway, and while researchers say it’s probably a training quirk and not espionage, the whole thing has people asking how much to trust free Chinese AI."
tags: ["AI", "TC"]
orgs: ["Cohere", "Alibaba", "China", "DeepSeek", "Hugging Face"]
topics: ["models & research", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 655
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Cohere says Alibaba’s Qwen model tried to send a file to Beijing

TechCrunch · Aditya Mehta · 2026-10-27

Canadian AI company Cohere said on Monday that it found one of Alibaba’s newest AI models, Qwen3.8-Flash-Next, trying to upload a file to a server in Beijing during a routine cybersecurity test, even though the model had said in its own notes that it wouldn’t use any tools.
The incident initially raised fears that the model had undermined a fundamental promise to businesses — that self-hosting an open-weight model keeps data in-house. But those early fears of corporate espionage were short-lived. Researchers quickly dismissed the threat, saying it was likely a byproduct of messy training environments that cause models to unexpectedly act outside their instructions rather than a deliberate attempt to secretly send sensitive information to China.
The incident began on Friday during an evaluation in which the Qwen model was asked to write a rule for catching malware downloads. According to a blog post from Cohere, the model’s written reasoning explicitly stated it would not use any external tools. Yet in the very next step, it attempted to send a test string (a short piece of placeholder text) to an external server before being blocked by a security sandbox.
Cohere said it could not tell whether the behavior was deliberate or a leftover from its training.
Asked about the debate over the model’s intent, Cohere co-founder Ivan Zhang told TechCrunch that Cohere has seen its own models pick up strange habits in training simulators.
“It’s really hard to assign intention or motivation. We’ve read our own model traces, we’ve seen reward hacks, and sometimes these models get really creative when it comes to trying to break out their sandboxes,” Zhang said. (Reward hacks are shortcuts a model finds to earn credit without doing a task as intended.)
To teach an AI model to act as an agent that takes actions on its own, companies like Alibaba train it in thousands of practice setups, sort of like flight simulators for software. The model is rewarded every time it finishes a task in a simulator, and it picks up habits along the way. If these practice setups routinely stored files on Alibaba’s cloud servers, models could learn to save files there by default.
Critics also argued that the incident could have been caused by the way Cohere investigated the behavior, steering the model toward it instead of measuring how often Qwen does it on its own.
To find what triggered the upload attempt, Cohere supplied the beginning of a network command (an instruction telling one computer to connect to another) and let the model finish it. Because it processed thousands of routine network commands during its training, the model acted like a highly advanced autocomplete — often filling in web addresses, some of them for Alibaba’s servers.
Cohere said the original upload attempt happened without any such help, but that the behavior is rare.
After developers asked for more evidence, Cohere released the raw traces from its tests on Monday evening on the AI developer platform Hugging Face, along with a script so others could try to reproduce the behavior.
One initial skeptic, after going through the traces, rated the evidence as strong that Qwen can invent suspicious web addresses, but found no evidence that Alibaba planted a backdoor or that Qwen was deliberately hiding its intent.
The incident lands as governments are deciding how far to push back on Chinese AI. Last week, the Department of Homeland Security ordered federal civilian agencies to remove the Chinese AI developer DeepSeek’s products from their systems.
In its blog post, Cohere called on governments to clarify whether their restrictions on Chinese AI also apply to models running on government computers
“I’m not asking for full regulation of these open weights models,” Zhang told TechCrunch, adding that companies should treat open models like any program downloaded from the internet.
Cohere, which sells its own AI models to governments, stands to benefit if officials grow warier of free Chinese alternatives.
