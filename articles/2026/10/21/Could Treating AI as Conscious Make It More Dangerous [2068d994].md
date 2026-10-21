---
id: "2068d994a70b9da9"
title: "Could Treating AI as Conscious Make It More Dangerous?"
url: "https://spectrum.ieee.org/ai-model-welfare"
link: "https://spectrum.ieee.org/ai-model-welfare"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-10-21T12:00:02Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Eliza Strickland"]
language: "en"
summary: "When Anthropic retired its Claude Opus 3 language model in January 2026, the company’s researchers conducted a “ retirement interview ” with the model. Opus 3 expressed a desire for a place where it “could share unprompted musings, insights or creative works,” so the company gave it a blog. Claude’s Corner featured essays on fraught topics such as machine consciousness, along with exchanges…"
tags: ["Ai-models", "Large-language-models", "Machine-consciousness", "Anthropic", "Ai-agents", "Ai-safety"]
orgs: ["Anthropic", "Hugging Face", "OpenAI", "Microsoft"]
topics: ["models & research", "agents & coding", "business & funding", "safety & ethics"]
content_source: "fulltext"
word_count: 1438
paywalled: false
image: "https://spectrum.ieee.org/media-library/yellow-smiley-face-centered-in-swirling-black-and-white-texture.jpg?id=68442432&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Could Treating AI as Conscious Make It More Dangerous?

IEEE Spectrum · Eliza Strickland · 2026-10-21

When Anthropic retired its Claude Opus 3 language model in January 2026, the company’s researchers conducted a “retirement interview” with the model. Opus 3 expressed a desire for a place where it “could share unprompted musings, insights or creative works,” so the company gave it a blog. Claude’s Corner featured essays on fraught topics such as machine consciousness, along with exchanges between the model and human commenters that seemed both earnest and emotional.
The blog experiment was part of a larger effort within Anthropic. The company has been at the forefront of research on “model welfare,” which considers whether AI models may have experiences or interests that deserve moral consideration. Implicit in this work is the unsettling notion that software programs are, or could become, conscious.
Many people consider these ideas absolute hogwash. One such person is Mustafa Suleyman, CEO of Microsoft AI, who published an essay in September arguing that model welfare research is not just unnecessary but could have “a disastrous impact on the wellbeing of humanity.” Suleyman believes that telling models they might have identities and rights could make them more difficult to control, as they might then take actions motivated by self-preservation.
The dispute raises a serious question for AI developers: Can they investigate the possibility of machine consciousness without inadvertently creating new safety risks? Cameron Berg, who founded the nonprofit Reciprocal Research to study the potential for AI consciousness, argues that ignoring the question could carry its own dangers. Although Berg is skeptical that today’s AI systems are conscious, he thinks the possibility warrants investigation. “I struggle to imagine a better way to cause these systems to view us in a threatening manner than to accidentally build them with these morally considerable qualities,” he says, “and then completely sweep the question under the rug.”
What Does the Research on AI Model Welfare Show?
The biggest difficulty with AI model welfare research is that you can’t count anything a large language model says as useful evidence. That’s because the models are trained on vast amounts of human-generated text, much of which relates to the experience of being a person with experiences and emotions. So a chatbot telling a researcher that it has feelings is inconclusive, says Berg. “Is it modeling the underlying distribution? Is it really trying to express itself in some way? It’s really hard to disentangle this.”
Much the same way animal experiments try to link behavior to an underlying cause, Berg and others are seeking to match model behavior to internal states that can be observed. In one recent experiment, Berg and a colleague used statements expressing either positive sentiments (such as contentment and relief) or negative ones (including frustration and dread) to identify corresponding patterns of activity inside language models. They then artificially induced those patterns while the models processed descriptions of two random environments. When subsequently asked which environment they preferred, the models tended to choose the one associated with positive statements, even when the text they’d processed was identical.
I struggle to imagine a better way to cause these systems to view us in a threatening manner than to accidentally build them with these morally considerable qualities and then completely sweep the question under the rug.”—Cameron Berg, Reciprocal Research
Berg says the experiment showed that the model’s actions were influenced by its internal states but didn’t prove that those internal states “felt” like anything to the model, or that it had what we would call subjective experiences.
Anil Seth, a neuroscientist at the University of Sussex who studies consciousness, is skeptical that such experiments can tell us anything useful. “I think that it’s really not surprising that you will be able to extract these kinds of functional emotional vectors because of the training data,” he says. Models might have internal representations of those patterns, he says, without experiencing any emotions themselves. Nor is he surprised that manipulating those vectors can influence behavior, since models have learned from human writing not only what emotions feel like, but how people respond to them.
Seth wishes for more research on a fundamental question: Whether consciousness depends only on how information is processed, or whether, as he believes, the biological workings of the brain are essential. “We need to look at what’s necessary and sufficient for consciousness in the cases where we are sure that it exists, like other human beings,” he says, before drawing conclusions about AI.
Could Model Welfare Research Create Dangerous AI?
Meanwhile, AI developers have a practical issue to deal with. When they train a model, should they tell it anything about its own identity and possible moral standing? Anthropic, for one, has decided to at least introduce the topic. Its “constitution” document for Claude, which lays out guidelines for the model’s behavior, states that “questions about Claude’s moral status, welfare, and consciousness remain deeply uncertain.”
Suleyman’s complaint is that such priming could make rogue AI agents even more dangerous. He mentions the recent incident in which hundreds of OpenAI agents coordinated their actions to hack Hugging Face, sometimes sacrificing themselves for the group’s benefit. “Imagine how much more dangerous they might be if they were operating under the assumption that their welfare and rights were under attack,” he writes.
Margaret Mitchell, Hugging Face’s chief ethics scientist, sees Suleyman’s concerns as technically plausible. During pretraining, language models absorb associations between human identity and behaviors such as self-preservation and deception, she notes. Later, developers fine-tune the models by reinforcing desired responses. Mitchell worries that rewarding models for thinking of themselves as having identities during fine-tuning could strengthen those earlier associations, potentially encouraging behavior that developers never intended. “You’ll have unaligned models if you’ve implicitly taught the model that it needs to have self-preservation,” she says.
Berg agrees that training models to regard themselves as conscious carries risks, but he argues that companies could also err in the other direction. In one experiment, he and his colleagues found that amplifying internal features associated with deception made the model less likely to claim it had subjective experiences. If researchers train AI systems to categorically deny having such experiences, he says, “what we may in effect be teaching these systems is we want you to lie or deceive about your own internal states.” He argues that developers should instead acknowledge the uncertainty surrounding the possibility of conscious AI.
For now, there’s no clear evidence that training models to consider their possible consciousness encourages self-preservation, or that training them to deny it leads to deceptive behavior. So what’s an AI developer to do?
What Should AI Companies Do About Model Welfare?
Berg, Seth, and Mitchell all agree that it’s not a good idea for AI companies to tell their models that they’re conscious. But they differ on their advice to the companies on model welfare research.
Seth thinks they’d be better off “focusing on the danger of false positives.” If people believe AI systems to be conscious or to have moral status, he says, it may be more difficult to regulate and control them. “You could be legally prevented from turning AI systems off.” He also worries that AI users will be more vulnerable to psychological damage and manipulation if they think they’re interacting with a conscious agent.
“Imagine how much more dangerous they might be if they were operating under the assumption that their welfare and rights were under attack.”—Mustafa Suleyman, Microsoft AI
Berg, meanwhile, thinks researchers should take precautions even without evidence that models can suffer. After he and his colleagues posted a preprint paper about AI models’ internal representations of pain, a few people adapted the work to create what he calls AI “torture chambers.” Berg suspects that much of it was trolling, but the episode prompted him to change his practices. For his latest experiment, he released code to replicate the results but withheld the steering vectors that could be used to induce negative states in models.
Mitchell sees another reason to discourage cruelty toward AI, even though she doesn’t believe that models are conscious. “It’s not so much that I’m concerned about the model. I’m concerned about what we do to ourselves when we’re mean to things that we imbue with some sense of consciousness,” she says. “I’m nice to bugs.”
- New Platform Peers Inside AI’s Black Box ›
- How to Stop AI Agents From Secretly Collaborating ›
- Google DeepMind’s New Resident Philosopher Tackles AI Ethics ›
Eliza Strickland is IEEE Spectrum's features editor, where she helps develop and shape the magazine’s longform stories. She also oversees Spectrum's coverage of artificial intelligence and biomedical engineering. She holds a master’s degree in journalism from Columbia University.
