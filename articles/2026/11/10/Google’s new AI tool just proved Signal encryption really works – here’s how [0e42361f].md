---
id: "0e42361f23e6cbd8"
title: "Google’s new AI tool just proved Signal encryption really works – here’s how"
url: "https://zdnet.com/tech/google-deepmind-researchers-prove-signal-whatsapp-encryption-works"
link: "https://zdnet.com/tech/google-deepmind-researchers-prove-signal-whatsapp-encryption-works"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T16:31:47Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Radhika Rajkumar"]
language: "en"
summary: "With the aim of securing other vital systems, Google DeepMind plans to open-source its AlphaProof Code."
tags: ["Security"]
orgs: ["Google", "OpenAI", "Anthropic"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 573
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-2206371598.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Google’s new AI tool just proved Signal encryption really works – here’s how

ZDNet · Radhika Rajkumar · 2026-11-10

ZDNET’s key takeaways
- Researchers formally verified that a portion of Signal’s encryption code works.
- Formally verifying code has historically been hard and time-consuming
- AlphaProof Code is a step toward stronger security verification.
Researchers at Google DeepMind used AI to formally verify portions of Signal‘s underlying code — meaning they’ve mathematically proven that at least parts of the encrypted messaging app’s code do what they say, without errors. That’s reassuring given how many vulnerabilities AI systems have discovered in software lately, and how many people’s communications are protected by Signal’s cryptography. WhatsApp and Google Messages use the same encryption.
Also: How AI security failures are endangering your supply chain
How DeepMind verified Signal
AI companies like OpenAI have been on a math-breakthrough tear as of late, in some cases solving nearly century-old math problems with AI. By computing at such vast scale, AI models can rapidly accelerate much of the manual work mathematicians do.
(Disclosure: Ziff Davis, ZDNET’s parent company, filed an April 2025 lawsuit against OpenAI, alleging it infringed Ziff Davis copyrights in training and operating its AI systems.)
Using AlphaProof Code and building on earlier verification work by the Signal Foundation, DeepMind researchers divided the verification task into two camps. Humans worked with agents to identify what they needed to prove, and multiple agents running Gemini Carbon, the company’s latest model, then executed it. The agents also audited the proof and “highlighted areas that needed a second look by a human — just 1% of the codebase, a massive time savings,” the researchers wrote.
Also: After the vibe-coding rush comes the debugging hangover
For good measure, researchers tested AlphaProof Code’s ability to distinguish correct from flawed code by showing it two previously fixed Signal bugs, for which it produced correct proofs.
“Our work marks the first time AI has been used to formally verify a widely deployed cryptographic protocol at this depth,” the researchers wrote. “It’s also the first time the implementation of a widely deployed protocol like this has been formally verified by any method, with or without AI.”
Normally, researchers need to manually develop a proof to verify software, which takes much longer. That labor-intensive barrier has made formal verification a distant promised land, until now. The DeepMind team’s verification took a month to do what might normally take experts years.
DeepMind did not verify all of Signal’s code, but noted that this test is a step toward improved security infrastructure at a time when AI is disrupting the entire cybersecurity space.
Also: How to encrypt emails in Gmail, Outlook, and more
“Having the core Signal protocol rigorously verified with automated theorem proving gives us even greater confidence that our code delivers on its privacy guarantees,” the researchers wrote.
What’s next
The breakthrough reiterates how deeply AI is both a massive risk for cybersecurity and an equally powerful fix. The year 2026 has been especially marked by AI-related security incidents, many of which involve agents. At the same time, companies like Anthropic, Google, and OpenAI are developing models geared specifically toward cybersecurity, including Anthropic’s Claude Mythos.
Also: How to easily encrypt your files on an Android phone
DeepMind did not share any plans to release its findings as a consumer product, though the researchers are open-sourcing their code to help others with formal verification efforts. “Verifying Signal’s core cryptography lays the groundwork to secure other vital systems, from medical device firmware to power grid software,” DeepMind added
