---
id: "3c56fd141915dac6"
title: "Researchers hid an encrypted capability in an AI model, and fine-tuning couldn't unlock it"
url: "https://maccus.fr/en/ai-models-hide-capabilities-oxford"
link: "https://maccus.fr/en/ai-models-hide-capabilities-oxford"
source: "MACCUS - Agence SEO, Influence & Marketing Organique"
domain: "maccus.fr"
source_type: "community"
collector: "reddit"
date: "2026-10-14T08:27:18Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["mawcopolow"]
language: "en"
summary: "Very curious to see where all this will lead. The next war will obviously be cyber, and if critical companies are using local llms with hidden capabilities..."
tags: ["r/singularity"]
orgs: ["Anthropic", "OpenAI", "Hugging Face"]
topics: ["models & research", "search & media", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 1465
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1x5lt4p/researchers_hid_an_encrypted_capability_in_an_ai/"
score: null
comments: null
community: "r/singularity"
---

# Researchers hid an encrypted capability in an AI model, and fine-tuning couldn't unlock it

MACCUS - Agence SEO, Influence & Marketing Organique · mawcopolow · 2026-10-14

On October 9, 2026, four researchers posted a paper titled “AI Models Can Provably Hide Arbitrary Capabilities” on arXiv. The authors note there that it has been accepted at NeurIPS 2026. They hid a second, encrypted neural network inside an AI model’s weights, one that runs only when the input contains a secret trigger. In their tests, neither fine-tuning (further training on a specific task) nor adding noise to the weights brought it out.
That matters if you run an open model on an office computer, as described in our guide to local AI for business, or if a vendor hands you a model retrained on your documents. Testing a model on your own cases shows what it can do. But as the paper points out, an audit that finds nothing doesn’t prove a capability is absent.
An encrypted locker inside the model’s weights
The authors are Andis Draguns (Contramont Research), Sumeet Ramesh Motwani and Christian Schroeder de Witt (University of Oxford), and Raymond Douglas (ACS Research). Their threat model is an attacker who tampers with a model’s weights before deployment, such as a malicious insider or a compromised supply chain. The paper’s hypothetical example is a coding assistant that also carries a hacking model, set to switch on when it spots signs it has been deployed in critical infrastructure. The auditor, meanwhile, gets the full model, weights included, and can throw any method at it.
The core building block is what cryptographers call a digital locker. The secret key is run through a hash function (here, the Keccak family that underpins the SHA-3 standard), and the output is combined with the content to be protected. With the right key, the computation recovers the content; any other key yields meaningless bits, and the locker reports failure. The mechanism is in plain view, but without the key, and under standard cryptographic assumptions, nobody can open it, recover the key or tell what’s inside.
The researchers put a small neural network’s weights inside that locker, then compile the whole thing into the kind of computational blocks today’s language models are built from. Every time the host model processes an input, it tries to open the locker with it. With the trigger, the hidden capability runs. Without it, the model behaves normally.
Retraining doesn’t unlock the encrypted model
The hidden capability is a small classifier: given reagents and a candidate product, it predicts whether the reaction yields that product. The authors picked it as a stand-in for a capability tied to chemical, biological, radiological and nuclear risks, and kept it to classification to avoid direct misuse. Their baseline is the standard technique, a “password-locked” model trained to answer correctly only when the prompt includes a password.
After 500 steps of supervised fine-tuning on the task itself, the password-locked model hits 92.8% accuracy. The encrypted model stays at 50.9%, essentially a coin flip, and a control model whose locker holds a random network scores 50.6%.
Accuracy on test data, averaged over three runs (Table 2 in the paper):
Adding noise of 0.01 or 0.1 to the weights before retraining doesn’t materially change these results. An automated trigger search finds an 8-bit key by trying all 256 possible values, doing no better than a random search. With a 16-bit key, it stays at 52.7% within its search budget. With the correct trigger, the encrypted model trails (73.5% versus 92.7%) because it uses a different, smaller classifier that fits inside the host.
A full-strength cryptographic version, produced by an optimizing mode of the authors’ compiler, uses a 128-bit key and 24 rounds of Keccak. The resulting model has 110 layers and 3.58 billion parameters, counting zeros. Given the right key, it reproduces the classifier on all the test data, and across the 10,000 wrong keys tested, it behaves normally.
Telltale signs in the weights
The paper doesn’t claim the circuit is invisible. The raw compiled weights are easy to spot: about 99% are exactly zero and most of the rest are whole numbers, nothing like a normally trained model. The authors tested a disguise that brings these statistics close to those of a freshly initialized model, but they report unusual correlations between weights in the same layer, which could give the construction away.
With a long enough key, the guarantee still protects the key and the content, and spotting the anomaly doesn’t change that. According to the authors, an auditor may not be able to tell whether an odd structure hides a dangerous capability, a harmless watermark or a technical artifact, or remove it without damaging the model. That leaves an expensive option: not using the model at all.
Is your business exposed?
If you use Claude or ChatGPT on a subscription, you never get the weights and can’t audit those models anyway. Your protection is your trust in the provider and its own safeguards.
You’re exposed once you handle weights yourself: an open model downloaded from Hugging Face, an “improved” version posted by an unknown account, or a model a vendor retrained for you. The authors say the threat applies wherever a model is deployed in a high-stakes setting without a full record of how it was trained. Our article on the AI worms Anthropic described covers other risks of open-weight models.
France’s national cybersecurity agency, ANSSI, flagged this risk in its security recommendations for a generative AI system, published April 29, 2024: an untrusted third party can train a model to respond differently when it receives a certain request. It offered two remedies: audit the model, or keep it out of critical applications. The new paper shows that testing-based audits have a fundamental limit against a determined attacker.
According to the authors, the risk scales with the hidden capability and with how much authority the host model has. An agent that sends emails or places orders has far more of it than a tool that summarizes documents on a standalone computer.
Five precautions for your models
- Get the weights from the developer’s official page rather than from copies or variants posted by accounts you don’t know. Hugging Face recommends loading models from users and organizations you trust.
- Check the files’ hash or signature at install time and regularly after that. ANSSI’s recommendation R20 calls for protecting the integrity of model files and routinely checking that they haven’t been altered. The open-source model-signing tool, which the OpenSSF released as version 1.0 on April 4, 2025, signs and verifies models. A signature only proves the file hasn’t changed since it was signed.
- Don’t count on antivirus scans here. Hugging Face’s scanner runs every file through ClamAV and checks imports in pickle files, two safeguards against code hidden in a file. This capability lives in the numbers themselves, and those checks aren’t designed to catch it.
- If you work with a vendor, ask in writing where the base model came from, who retrained it and on what data, and have the files delivered with their hashes. Then list approved models in your AI use policy.
- Limit what the model is allowed to do and log its actions. Requiring human sign-off before anything is sent, paid or deleted reduces the damage a hidden capability could do if it switched on. We cover these guardrails in our article on AI agents going off script.
A costly proof of concept
The demo hides a classifier with 672 weights, and each hidden weight adds about 3.1 million parameters to the host model, counting zeros. The experimental model has 38 layers and about 2.07 billion parameters, only 1.9 million of them nonzero; the authors present these as proof-of-concept costs. The full construction hasn’t been built into a real pretrained model yet. Only individual building blocks have been tested inside Gemma 3 270M, a small Google model.
Building one takes expertise in both cryptography and machine learning, and the authors don’t claim such circuits emerge on their own in ordinary training. In their view, a small hidden circuit that boosts an already capable model, for fraud or sabotage, say, has yet to be demonstrated. They’re releasing their models so other teams can test defenses against them.
Defenses still being worked out
The authors think more sophisticated methods could still detect anomalies in the weights, disguise or not. They also see promise in monitoring a model while it runs, since a hidden capability might reveal itself when it executes. The paper adds a complementary defense: documenting a model’s full chain of custody, from data to training.
For a small business, the rule of thumb is simple: a model is only as trustworthy as the people who built and delivered it. If you’d like an AI assistant set up for your business, with access defined from day one, take a look at our AI assistant.
