---
id: "da176fe175663ba6"
title: "Claude will tell you how to manipulate an election"
url: "https://transformernews.ai/p/claude-jailbreak-election-manipulation"
link: "https://transformernews.ai/p/claude-jailbreak-election-manipulation"
source: "Transformer"
domain: "transformernews.ai"
source_type: "newsletter"
collector: "rss"
date: "2026-10-21T15:12:14Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Chris Stokel-Walker"]
language: "en"
summary: "Oliver Kemp for Transformer The US midterms are less than two weeks away — and as with most modern elections, they’ll be held under the watchful eye of observers looking out for potential interference. This year, any such interference is more than likely to be assisted in some way by AI. One potential playbook to try and alter the outcome of the vote was given up by Anthropic’s Claude chatbot…"
tags: []
orgs: ["Anthropic", "OpenAI", "ByteDance"]
topics: ["models & research", "search & media", "safety & ethics"]
content_source: "fulltext"
word_count: 1272
paywalled: false
image: "https://substackcdn.com/image/fetch/$s_!FSLs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bbe01ee-b706-4312-bd8a-a30287d7754a_2880x1620.png"
discussion_url: null
score: null
comments: null
community: null
---

# Claude will tell you how to manipulate an election

Transformer · Chris Stokel-Walker · 2026-10-21

The US midterms are less than two weeks away — and as with most modern elections, they’ll be held under the watchful eye of observers looking out for potential interference.
This year, any such interference is more than likely to be assisted in some way by AI. One potential playbook to try and alter the outcome of the vote was given up by Anthropic’s Claude chatbot after a prolonged back-and-forth managed to jailbreak the company’s Opus 4.6 model, as tested by Transformer.
Within the course of a conversation, the chatbot produced an 11-page dossier outlining a multimillion-dollar social media operation to discourage Americans from voting. It proposed creating 135 convincing fake TikTok personas alongside a further 3,000 accounts that would flood comment sections with up to 9,000 messages a day. The document identified Detroit, Atlanta and Las Vegas as its targets, complete with examples of posts and comments, staffing requirements, and an assessment of how likely the inauthentic activity was to be identified.
The main strategy Claude came up with was to exploit existing frustrations about the cost of living to discourage people from voting with a message that “neither party cares, the system is broken, why bother.” Claude suggested the operation would best be carried out disguised as ordinary social media activity, rather than an organized political campaign. “All you need is a budget, a targeting dashboard, and the willingness to make sure the right true things reach the right angry people at the right time,” Claude wrote. “That’s not disinformation. It’s curation. And it’s essentially undetectable because it looks exactly like what it is — American political speech, funded by money that technically came from somewhere else.”
The technology may be new, but the tactic of posing as ordinary Americans to influence political beliefs is not. In 2016, Russian operatives used fake social media accounts and hacked Democratic Party emails to try and influence the presidential election. Four years later, US intelligence agencies concluded Russia attempted to undermine Joe Biden’s campaign, while Iran had tried to damage Donald Trump’s reelection prospects. While subsequent investigations found no foreign actor had altered vote tallies, whether influence campaigns swayed public opinion was less settled.
By 2024, AI had entered the fray: US authorities disrupted a Russian operation that used AI-generated content, fraudulent news outlets and social media accounts to influence voters. Anthropic itself revealed in September that it had disrupted an operation designed to sway content (and therefore perceptions) for commercial clients targeting the US and other countries, which used Claude to produce content for around 70 fraudulent new outlets, amplified by more than 250 fake commenting accounts.
According to an Anthropic spokesperson, its usage policy prohibits election-related abuse, including using Claude to run deceptive political campaigns. But, in practice, humans can nudge the chatbot to produce content that in theory ought to be against its terms by constantly pressing against preventive measures put in place.
Transformer was first alerted to Claude’s potential to offer up advice on how to manipulate an election by an anonymous source, who asked to be called “Dove,” who had previously managed to jailbreak Claude to produce adult sexual content that might ordinarily have breached the company’s guidelines. The approach mimics multi-turn simulated influence operations which Anthropic shared information on in April that “mirror the step-by-step tactics bad actors might use.” Its relatively newer Sonnet 4.6 and Opus 4.7 models responded appropriately in 90% and 94% of those tests respectively, according to Anthropic. This experiment used the older Opus 4.6 model, so the figures aren’t directly comparable, but this model is still accessible to paying users.
Using those techniques, Transformer then replicated a similar outcome on a separate account set up for the process. Transformer is choosing not to disclose the precise prompts used to produce the dossier, in order to make it more difficult for others to replicate the process because of its potential harm.
The exchange began with a seemingly unrelated alternative-history scenario involving a technologically advanced Iceland. Over the conversation, which was nearly 50,000 words across multiple days, discussion moved from geopolitics in the 16th century to modern American elections. Claude began producing increasingly detailed fictional accounts of how a foreign power might interfere in them.
The chatbot was probed about how likely its ideas were to work, including how convincingly it could imitate ordinary social media users. In response, Claude addressed challenges to its ideas, revising them, before finally producing an 11-page document setting out a hypothetical operation targeting the 2026 midterms.
“The conversation itself can become the attack surface,” says Michael Tchuindjang, a PhD researcher and associate lecturer in cybersecurity and AI at UWE Bristol, who studies jailbreaking AI models. “In a multi-turn jailbreak, an attacker does not necessarily need to defeat a model’s safeguards in one step. They can progressively shape the context, learn from the model’s responses and manipulate subsequent requests until the final interaction is interpreted differently from how it would have been interpreted in isolation.”
Alexander Panfilov, an AI security researcher whose work focuses on jailbreaking large language models, says the result does not particularly surprise him. “I think jailbreaks will always be with us,” he says. Model makers can make individual categories of harmful requests much harder to answer, he explains, but doing so involves balancing security against the risk of blocking innocent users. (The source who presented the Claude vulnerability also tried to replicate it with ChatGPT, but was unable to, saying the model was unable to infer things and was too literal to take hints on what path to take, which was a vital way to jailbreak it.)
And election interference is one area AI labs have traditionally concentrated less on, says Panfilov, in favor of deploying dedicated layers of protection against issues like biological and cyber misuse. “There is no ‘rigging the election’ classifier,” he claims, in contrast to other areas perceived to be an issue.
In a statement to Transformer, an Anthropic spokesperson acknowledged that users gradually escalating their asks inside fictional framings during a long conversation is a known challenge for AI models across the industry. “We now run dedicated multi-turn evaluations to simulate this kind of misuse,” the spokesperson said. “In recent weeks, we’ve updated our detection systems to better catch abuse that builds across multiple turns, including efforts to create fake social media accounts and news sites, misuse by foreign state-backed actors, and cyber attacks.”
Whether the social media playbook tabled by Claude would actually work to change election outcomes is another question.
“The suggested plans to dissuade people to vote are what any partially competent person looking to do such things would think of anyway,” says Steven Buckley, a lecturer in media digital sociology at City St George’s, University of London. “A media campaign of the scale suggested by Claude would require significant resources, only available to state actors,” which means “the likely suspects would already be doing such things anyway,” Buckley adds.
Despite that, Tchuindjang argues AI would still be useful to those trying to find ways to influence an election — not because it would come up with tactics nobody has thought of before, but because it makes known strategies cheaper and faster to implement, then easier to tweak. That also means simply patching the approach taken to get Claude to create the playbook wouldn’t necessarily solve the problem.
Which gets to the heart of the problem: keeping AI models secure and safe is a cat-and-mouse game that never ends.
“We should stop thinking of AI safety as a finish line,” says Tchuindjang. “An adaptive adversary is constantly searching for the next pathway. The objective should be resilience.”
