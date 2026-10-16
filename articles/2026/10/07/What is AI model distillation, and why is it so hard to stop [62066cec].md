---
id: "62066cec9c3899a3"
title: "What is AI model distillation, and why is it so hard to stop?"
url: "https://scientificamerican.com/article/what-is-ai-model-distillation-and-why-is-it-so-hard-to-stop"
link: "https://scientificamerican.com/article/what-is-ai-model-distillation-and-why-is-it-so-hard-to-stop"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-07T11:00:00Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Peter Hall"]
language: "en"
summary: "Anthropic and OpenAI accused Chinese AI developers of mining their models’ answers to train cheaper copycats. Here’s how distillation works and why it’s so hard to stop"
tags: []
orgs: ["OpenAI", "Anthropic", "China", "DeepSeek"]
topics: ["models & research", "jobs & society", "agents & coding", "health & science"]
content_source: "fulltext"
word_count: 1362
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# What is AI model distillation, and why is it so hard to stop?

Scientific American · Peter Hall · 2026-10-07

To make grain-based liquor, you heat a fermented mash in a still until alcohol-rich vapor rises and then cool it back into a stronger liquid. Chemists and whiskey makers know this as distillation. Artificial intelligence developers have borrowed the word to describe boiling down a big AI model into a smaller one—and lately the biggest AI companies say that rivals have been distilling like bootleggers.
In September Anthropic and OpenAI each detailed how they caught and killed campaigns to distill their flagship models—that is, to extract enough information from the models to train new models that mimic the originals at a fraction of the size and cost.
Distillation has become a sore spot for American AI companies as they try to justify high valuations and fight off competition from each other and open-source alternatives. If, say, a Chinese model developer can piggyback on all the money and computing power those companies have invested, the incentive to keep making new models starts to evaporate.
On supporting science journalism
And no one expects distillation to stop any time soon—so we asked the researchers who study it to explain the situation.
What is distillation, anyway?
Just as a still concentrates a large batch of weak liquid into a smaller batch of strong stuff, AI distillation condenses a big model into a smaller one that, ideally, acts like the original. The process starts with the existing large model, called the teacher. Developers prompt the teacher many times over and then feed its responses into the new model, called the student, to train the latter.
In a way, every response contains information about what the teacher learned during training, so that knowledge passes to the student without going through the process of collecting data, finding patterns in those data and getting human feedback. Distillation lets someone reverse engineer an AI model just by using it and watching its responses.
It helps that AI models tend to give away more than just their final answers. “Oftentimes the teacher model doesn’t just give you the label, but it actually gives you more fine-grained information,” says Yevgeniy Vorobeychik, a professor of computer science at Washington University in St. Louis. That could include the odds a model assigns to each possible response or, as in the case OpenAI described, an encrypted record of the step-by-step reasoning its more powerful models work through before they answer.
Why distill in the first place?
Plenty of distillation is aboveboard. Smaller models let developers get more for less. In fact, the concept predates large language models (LLMs); by the 2000s, researchers were studying it as a way to increase efficiency for neural networks. “We cared about making it smaller, easier to use, faster to apply,” says Alexandru Niculescu-Mizil, a machine learning researcher who cowrote an early paper on the idea in 2006.
Distilling someone else’s model is another matter. The term first caught mainstream attention in early 2025, when DeepSeek, then a little-known Chinese start-up, released a reasoning model, called R1, that it said it had trained for less than $300,000—a fraction of what American labs had spent. Allegations quickly emerged that DeepSeek had trained R1 in part on responses extracted from OpenAI’s models.
These days the word is generally associated with accusations of model theft, mostly aimed at Chinese developers such as DeepSeek and Moonshot AI, the maker of Kimi. In their September reports, Anthropic and OpenAI both blamed labs based in China for the recent distillation campaigns they caught, calling the activity “illicit” and “unauthorized.” DeepSeek and Moonshot AI have both fended off these accusations in the past. Of course, Anthropic and OpenAI have themselves been accused of training their models on data obtained without authorization from all over the internet.
Still, though the companies also cast distillation as a security risk, their most obvious interest in stopping it is protecting their competitive advantage. “The text that it produces in response to your prompt is being stolen by some rival companies,” says Alexander Panfilov, a Ph.D. student at the Max Planck Institute for Intelligent Systems in Germany. “But on a conceptual level, what you are stealing [are] capabilities.”
So how does one distill?
In general, distillation is done by collecting thousands and thousands of AI responses to different kinds of queries. Those prompts and responses then become training data for the student, usually through a process called supervised fine-tuning, which treats the teacher’s answers as targets the student should try to emulate. Over many rounds, training nudges the student’s internal settings, called weights, so that its answers more closely match the teacher’s.
The key is getting those data. Anthropic and OpenAI have detailed several creative methods they believe attackers used to do so. According to Anthropic, some labs routed their own customers’ prompts to Claude and then saved Claude’s responses to train their own models. The company also said that distillers try to obscure where they are located. OpenAI, meanwhile, said distillers tried to get at its models’ hidden reasoning by “copying encrypted reasoning from one conversation and asking a model in another conversation to decrypt” it.
Panfilov was co-lead author of a preprint paper detailing that kind of attack, and OpenAI credited him and his colleagues with bringing the attacks to the company’s attention. In this case, the goal was to distill how the models reason, or generate longer responses in order to solve hard problems step-by-step. Panfilov and his colleagues called their project “Stolen Thoughts,” a sign of how tightly the concept has become intertwined with thievery.
How do you catch a distiller?
The AI companies are hesitant to reveal exactly how they caught these latest attempts because doing so would show the next distiller what to avoid. Broadly, though, the firms seem to have watched for accounts prompting their models in suspicious ways, whether by firing off lots of prompts in a short time or by asking telltale kinds of questions. Anthropic, for instance, said that, from May to July, it observed more than 151 million exchanges between Claude and accounts tied to Chinese e-commerce giant Alibaba, which also makes the Qwen family of AI models.
Panfilov says the attack he studied is easy to detect, but he worries that cleverer ones can’t be spotted without trampling everyone’s privacy. “I don’t have a good idea how [AI companies] would do it, especially given that they claim this zero data retention policy,” he says, referring to arrangements under which the companies don’t store some customers’ prompts and responses.
Both OpenAI and Anthropic have warned that the distillers’ methods will only get more sophisticated, given how valuable distillation can be.
Can distillation be stopped?
The trouble is that the very qualities that make AI models informative and useful also make them good to train on. So attempts to make a model harder to distill may also make it worse. Over the summer, Vorobeychik and his colleagues found that a model’s reasoning can be rewritten so that it will make poor training material for a copycat, without making the model’s answers any less accurate. They also found that the rewritten reasoning was harder for people to follow, however. “Just by virtue of the fact that they’re harder to read for the LLM to train, it’s also harder for humans to digest,” Vorobeychik says. That’s an unwelcome trade for a technology whose output already takes flak for being hard to parse.
Panfilov also notes that distillation can be done in pieces in which “each query in itself is benign.” That would make it even harder to distinguish someone prompting a model for ordinary use from someone trying to build a model of their own. AI companies will have to balance protecting their models’ capabilities against actually flexing them for the public, which is, after all, what they’re selling.
All this suggests that stopping illicit distillation will mean finding new attacks before stamping them out. The labs, in effect, are playing revenuers, the liquor-tax agents who once hunted down and dismantled illegal stills. But as fears about distillation intertwine with fears about Chinese AI capabilities more broadly, busting stills one at a time may not be enough to put the American AI industry at ease.
