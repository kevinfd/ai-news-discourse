---
id: "2ce4379b96ee6766"
title: "Anthropic’s AI worm research raises new fears about smart device security"
url: "https://scientificamerican.com/article/anthropics-ai-worm-research-raises-new-fears-about-smart-device-security"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T19:00:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Peter Hall"]
language: "en"
summary: "Researchers explored how AI could spread through everyday gadgets. But cybersecurity experts have seen these tricks before"
tags: []
orgs: ["Anthropic", "Google", "Meta", "OpenAI", "Apple", "China"]
topics: ["models & research", "chips & infrastructure", "safety & ethics", "business & funding"]
content_source: "fulltext"
word_count: 869
paywalled: false
image: "http://www.bing.com/th?id=ONUT.q1cHI_CR4i4bxoaQeLIkDQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic’s AI worm research raises new fears about smart device security

Scientific American · Peter Hall · 2026-10-14

Everything is a computer these days. Fridges, washing machines, televisions, and more are now outfitted with computer chips to give them new capabilities, and manufacturers called them “smart” even before ChatGPT came out. Now, though, researchers have strung 15 cheap TV boxes together to run an artificial intelligence model, raising the possibility that the computers inside these everyday gadgets could someday help spread autonomous, AI-powered malware.
On Monday Anthropic released a blog post exploring this sort of attack. Researchers at the company tested how AI models might act as computer worms, programs that move between devices and leave copies of themselves behind, among everyday household gadgets. A worm that runs on smart devices instead of relying on a data center could prove difficult to shut down. Anthropic’s experiments suggest how that might happen—though they stop short of demonstrating the full threat.
Typically, large language models (LLMs) are trained and run in data centers, which can contain hundreds of thousands of specialized chips called graphics processing units, or GPUs. “Just because you don’t have a big GPU doesn’t mean that you can’t be a host to one of these models,” says Jeffrey Ladish, founder and executive director of Palisade Research, a California-based AI safety nonprofit that studies the risk of AI systems slipping beyond human control, past malware to rogue behavior.
On supporting science journalism
If you're enjoying this article, consider supporting our award-winning journalism by subscribing. By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.
In recent months, researchers have experimented with various types of computer worms, stapling AI models onto them to make them adaptive and harder to kill. Here, though, the researchers explored whether an AI model itself could be distributed as the worm, spreading its weights to new devices and running across even weak chips.
"Anybody with an open-weight model, with the right prompts and by brute-force luck, can find these worms," says computer scientist Vyas Sekar.
Specifically, researchers working on Anthropic’s Frontier Red Team showed two key capabilities. First, they were able to split up a relatively small model—one from Google DeepMind’s open-weight Gemma line—across 15 TV boxes they had bought and networked themselves so that they could run the entire model by chaining these boxes together. Each individual box was too weak to run the model on its own. But LLMs can be split into layers, an arrangement in which each layer manipulates the data it receives and passes that revised data to the next layer. By giving each box the job of handling just a couple of these layers, the team was able to run Gemma entirely and get responses back from just the weak chips in these boxes.
After that, the researchers tested how an AI worm might spread across devices in a virtual sandbox. A larger model—from the Chinese start-up Z.ai—managed to get a smaller model—one of Meta’s Llama models—running on the targets. But the larger model was too large to run on those weak devices itself, and it still relied on a separate server. This means the team did not show an AI worm capable of spreading and running itself on such devices. Anthropic argues that as small models become more capable, one could eventually use both methods.
The research also raises the prospect of adaptation and improvement by suggesting that AI models could subsist on low-power devices and drift through the Internet, getting better at spreading as they go. Anthropic makes this clear in its blog post about the work, concluding that AI systems could soon be “passing on their adaptations to future copies of themselves.”
Ladish believes the main lesson from the research is in how AI models could divvy up work across computers of all shapes and sizes. “Basically, compute is a resource that these models can use,” he says, pointing to everything from Apple MacBooks to data centers to everyday objects like smart TVs as possible sources of computing power if attackers can hack them.
Not everyone thinks that the experiments amount to a new kind of threat, however. “I think there’s some caution that’s needed here to make sure we talk about what capabilities are new and transformative,” says Michael Bailey, a professor studying computer systems security at the Georgia Institute of Technology. He emphasizes avoiding “fearmongering” with the lessons taken away from this kind of work. Researchers already know how insecure devices like TV boxes can be. “We already had self-replicating malware,” says Bailey. “We had botnets.”
“All of these are classical computer security threats,” adds Vyas Sekar, a professor of computer engineering at Carnegie Mellon University. According to Sekar, the bigger problem is that more people might be able to launch such attacks—a “democratization of being evil,” as he calls it. Sekar thinks this makes monitoring and restricting data flow between smart devices even more important.
Even the risk of hijacking raw computing power on chips is not new. Hackers have long taken over other people’s computers to mine cryptocurrency. So while smart devices could face new attacks of the kind Anthropic describes, the underlying weakness is an old one: plenty of our gadgets are already easy to commandeer.
