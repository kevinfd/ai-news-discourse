---
id: "1032abf6a3a5d724"
title: "A New AI Tool From Google DeepMind Proved the Signal Protocol Is Secure"
url: "https://wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol"
link: "https://wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol"
source: "WIRED"
domain: "wired.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-10T05:01:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Lily Hay Newman"]
language: "en"
summary: "DeepMind researchers were able to formally verify that the widely used encryption protocol works as intended. Their stretch goal? Do the same for “all the software of the world.”"
tags: ["Security", "Security / Security News", "Signal", "Google", "DeepMind", "agentic AI", "artificial intelligence", "cryptography", "encryption", "end-to-end encryption", "math", "Proof Positive"]
orgs: ["Google"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 673
paywalled: false
image: "https://media.wired.com/photos/6af239fd5613664a71d65edb/master/pass/Security_V1-ezgif.com-video-to-gif-converter.gif"
discussion_url: null
score: null
comments: null
community: null
---

# A New AI Tool From Google DeepMind Proved the Signal Protocol Is Secure

WIRED · Lily Hay Newman · 2026-11-10

Google DeepMind researchers used agentic AI to mathematically prove, or “formally verify,” a number of the Signal protocol’s key cryptographic guarantees—a landmark development for the widely used cryptography and AI itself.
Conducted as a sort of proof-of-concept project in just four weeks, the work is significant in two ways. It serves as further independent validation of the cryptography that protects massive quantities of the world's communications on platforms like the Signal app, Google Messages, and WhatsApp. And it demonstrates Google DeepMind's formal verification capabilities using a new AI framework called AlphaProof Code.
More broadly, AI-aided formal verification is having a moment, but it is unclear how practical it will be for widespread use and how effective it can be at securing large amounts of code. Proponents of formal verification have long referred to it as a sort of holy grail in software security, because it uses math to check and validate that software is functioning as intended—in other words, that it doesn't have critical vulnerabilities.
Before the AI era, it was incredibly time-consuming for people to describe the characteristics of software they wanted to prove, turn these summaries into formulas, and then develop the proof. Agentic AI can significantly cut down the time of the latter project, enabling analyses like DeepMind's Signal evaluation. But even this analysis was limited in scope—it did not, for example, formally verify the entire Signal mobile app—and DeepMind researchers emphasize that their findings are just one milestone in a larger process.
“We are very excited by this result, but there is a long distance to go before we are able to scale this to all the software of the world, and we want to do that,” Swarat Chaudhuri, a DeepMind research scientist, tells WIRED.
The DeepMind analysis did not find any new vulnerabilities in the portions of the Signal protocol it looked at, but when the researchers used AlphaProof Code on older versions of Signal that contain known and long-fixed vulnerabilities, it correctly identified them and showed that the protocol could not be formally verified. The researchers are releasing the specification and proof they developed for the Signal protocol analysis to aid other formal verification work.
While the speed of the project was notable, the DeepMind researchers point out that they were able to get a head start to a degree because of some past formal verification work that the Signal Foundation has conducted.
“While prior formal verification focused on smaller portions of the code, Google DeepMind's approach enables significant expansion,” Ehren Kret, Signal's chief technology officer, says in a statement. “As AI-driven security threats grow, rigorously verifying the Signal protocol implementation gives us even greater confidence in our code's privacy guarantees.”
For critical services used in high-stakes settings, it would be a dream to be able to formally verify every code base and entire software supply chains. “If you can now verify the correctness of these implementations, then you can rest easy,” says Pushmeet Kohli, chief scientist at Google Cloud and DeepMind's vice president of research. “You can imagine banks, imagine all those other companies who rely on assurances and who worry about bugs who could now say, ‘I can prove these properties.’"
The open question across the tech sector, though, is whether AI-automated formal verification can truly scale—and whether it can do so at a workable cost. DeepMind conducted the Signal analysis free of charge as a research project, and Google declined to share the cost of the analysis. The company also declined to comment on whether it has plans to release a commercial formal verification product or service.
The researchers say that some of their crucial advancements are in developing a “human-AI collaboration process,” as Chaudhuri puts it, that allows agents to contribute and self-correct at almost every phase of the process while still seeking human input and review at key junctures. “We don’t want this sort of vibe world where AI is generating the goals and AI is generating the proofs and basically taking tests that are self-written," Chaudhuri says. “There’s a middle ground.”
