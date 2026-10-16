---
id: "e418854a71af1878"
title: "Getting AI Into Production Is No Longer The Hard Part"
url: "https://forbes.com/councils/forbestechcouncil/2026/10/16/getting-ai-into-production-is-no-longer-the-hard-part"
link: "https://forbes.com/councils/forbestechcouncil/2026/10/16/getting-ai-into-production-is-no-longer-the-hard-part"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-10-16T10:30:00Z"
published_date: "2026-10-16"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Ciaran Cosgrave, Forbes Councils Member"]
language: "en"
summary: "Getting AI into production has become a baseline expectation, and enterprise teams are increasingly focused on what happens after go-live."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Anthropic", "Thinking Machines", "OpenAI", "EU"]
topics: ["policy & regulation", "models & research"]
content_source: "fulltext"
word_count: 961
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6ad100833cd78a834925b233/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# Getting AI Into Production Is No Longer The Hard Part

Forbes · Ciaran Cosgrave, Forbes Councils Member · 2026-10-16

Ciarán Cosgrave, CEO, Nearform.
On the evening of June 12, 2026, chats froze, active prompts failed and automated pipelines broke as two of the most capable AI models on the market seemingly disappeared.
Citing national security, the U.S. government ordered Anthropic to block all foreign nationals from accessing Claude Fable 5 and Mythos 5. With no way to do that selectively on short notice, everyone lost access, including Americans. There was no technical issue, and the models worked perfectly until they were turned off. Access came back about two-and-a-half weeks later, but the lesson is that access can disappear with little warning.
What strikes me most is this hit businesses running AI in production, not sandbox experiments. For the last few years, the conversations I’ve had with enterprise CTOs and other tech leaders have been about escaping the pilot “graveyard,” and, in the meantime, an entire consulting market has emerged promising the answer. But with every consultancy now making the same promise, getting AI into production has become a baseline expectation rather than a prize.
Instead, enterprise teams—including their boards and investors—are increasingly focused on what happens after go-live. I keep hearing the same two questions from them:
1. Can we afford to keep running these systems at scale?
2. Can we depend on what we’ve built still being there next month?
Engineering alone can’t answer either, because no amount of clever code fixes a price you can’t predict or a government intervention. They’re questions about risk and volatility, which is why they’ve moved from the CTO’s desk to the boardroom.
The Bill Nobody Modeled
Companies buy infrastructure confidently because it tends to behave predictably, but AI has changed that paradigm. Its usage and its resulting costs are now based on a number of variable factors. You know how many gigabytes of storage you need, but AI is typically priced in tokens (the units of text a model reads and writes), and the same task can burn through wildly different amounts depending on the pricing tier you’re on and how the system behaves in the real world. The bill only becomes clear later, and a pilot is a poor indicator because costs often look trivial until you scale them across a business.
And the economics aren’t fixed, either. Open-weight models, which can be downloaded and run on your own infrastructure rather than accessed through a vendor, shift more of the running cost into your control while reducing your exposure to a vendor suddenly cutting off access.
Thinking Machines, founded by Mira Murati, OpenAI’s former technology chief, released one in July (registration required), and pitched clients on lower running costs rather than raw capability. Prices will fall, but architectures are being chosen now, and building everything around a single vendor’s model is a decision that can cost a fortune to reverse later.
Gartner expects more than 40% of agentic AI projects, which are projects built on AI that acts on its own rather than waiting for instructions, to be scrapped by the end of 2027, citing escalating costs and unclear business value among the reasons. My bet is a good share of those canceled projects will work exactly as designed and be switched off anyway, because nobody modeled the cost of running them at full volume.
Why Sovereignty Is Now A Design Input
Sovereignty sounds like a word for diplomats, but in the AI ecosystem, it’s about who ultimately controls the technology your business depends on. The events involving Anthropic confirmed it likely isn’t your company, and it may not necessarily be your vendor. More often, the control sits at the government level. A model can disappear for reasons that have nothing to do with traditional constraints, which is why it’s important to make sure any single model can be swapped out. Additionally, it’s important to treat a multi-model strategy as a basic resilience measure rather than an academic exercise.
Data centers and trading floors run backup generators and failover sites because their businesses can’t stop when the power does. Now AI is becoming infrastructure of that order, but very few organizations have any continuity plan for it.
Losing access is one sovereignty problem. The other, which boards discuss privately far more than publicly, is what the regulator will permit and what’s politically acceptable in each market. A model choice that’s unremarkable in one jurisdiction can be a genuine problem in another.
The EU AI Act was meant to be the fixed point European businesses planned around, but the European Parliament has voted to push most of its strictest obligations back to December 2027 and beyond. If the rules you’re designing around can move by more than a year, your regulatory position is a live variable to engineer around rather than a box to tick at the end.
A Question Of Trust
Strip them back, and cost and sovereignty pose the same question. Will the economics hold once you scale, and will the thing still be there (and still be allowed) when you need it?
Writing software is getting dramatically cheaper because AI now can do so much of it. Deciding what’s worth building still takes judgment, and getting it live safely in a regulated business still takes discipline and human interaction. Keeping it available and affordable once it’s running is the newer problem.
My advice to enterprise leaders is fairly simple: model the running cost before you scale, rather than waiting for it to surprise you, and build in such a way that no single model can hold you hostage. As part of that, treat your regulatory position as something that will change with time, and distrust anyone offering black-and-white answers—because there aren’t any yet.
Most organizations will get to production. Far fewer will be able to afford to stay there.
