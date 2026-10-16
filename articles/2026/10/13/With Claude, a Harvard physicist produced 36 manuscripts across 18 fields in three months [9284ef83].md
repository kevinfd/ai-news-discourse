---
id: "9284ef83f71f0a70"
title: "With Claude, a Harvard physicist produced 36 manuscripts across 18 fields in three months"
url: "https://maccus.fr/en/bootloops-claude-science"
link: "https://maccus.fr/en/bootloops-claude-science"
source: "MACCUS - Agence SEO, Influence & Marketing Organique"
domain: "maccus.fr"
source_type: "community"
collector: "reddit"
date: "2026-10-13T08:23:49Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["mawcopolow"]
language: "en"
summary: "Can you feeeeel the acceleration?"
tags: ["r/singularity"]
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["models & research", "health & science", "business & funding"]
content_source: "fulltext"
word_count: 1383
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1x4r374/with_claude_a_harvard_physicist_produced_36/"
score: null
comments: null
community: "r/singularity"
---

# With Claude, a Harvard physicist produced 36 manuscripts across 18 fields in three months

MACCUS - Agence SEO, Influence & Marketing Organique · mawcopolow · 2026-10-13

Harvard physics professor Matthew Schwartz used Claude to produce 36 research manuscripts in three months, across 18 fields and with 19 coauthors. He picked the projects from about 400 candidate problems. His guest post on Anthropic’s science blog, published October 1, 2026, describes the method: BootLoops, an open-source toolkit that puts an AI model to work on exact scientific calculations.
Most of those fields are far from his own: ecology, population genetics, economics, linguistics, solar physics. If your business already runs on Claude or ChatGPT, the method carries over: a well-equipped model, written success criteria, and someone who knows the field checking everything. Claude skills are built for exactly that: writing those criteria down once.
Problems built for Claude
In December 2025, Schwartz treated Claude like a graduate student: the final paper was good, but he had to correct every sentence it wrote. This summer, working with Claude Fable 5, he flipped his approach: look for problems that suit the model’s strengths, the ones he calls “Claude-shaped.”
His core finding: many fields have problems that a technique from mathematics, physics, or computer science “would solve outright if anyone knew it existed.” The model knows both particle physics and genetics, so it can carry a method from one to the other. Few human researchers do.
The news section of the journal Science ran the story under a headline citing 22 scientific fields. The project’s site, bootloops.ai, also counts 22 fields across all BootLoops 1.0 applications, while Schwartz’s post counts 18 for the 36 manuscripts alone. Both numbers are right; they count different things.
BootLoops is free and works with other models
A “harness” is the setup around an AI model: the tools it can run and the rules it has to follow. Claude Code plays that role for Claude, and Codex does the same for OpenAI’s models. BootLoops brings together about 50 scientific software packages, ported into one framework and documented so an agent knows when to reach for each. Every tool spells out the test its answer has to pass before anyone relies on it.
Claude wrote the code under Schwartz’s direction; he says he set every problem, approved every plan, and checked the results against independent methods. The BootLoops repository on GitHub is released under the MIT license. The project site says it runs with Claude, Gemini, or ChatGPT, and the README says a laptop and whatever model access you already have are enough.
Anthropic, where Schwartz is a visiting researcher, funded the project. According to the post, Schwartz owns and maintains BootLoops; the repository says Anthropic doesn’t provide support for it. A 27-page technical paper describes it on arXiv.
Thirty integrals, a Panamanian forest, and the Voynich manuscript
It started in particle physics, Schwartz’s own field. Within a few weeks, Claude computed 30 Feynman integrals end to end. Physicists use these integrals to predict particle collisions. Half reproduced known results with a new method; the other 15 had never been computed.
In ecology, Claude spotted a BootLoops-shaped problem in a 2005 equation that nobody had managed to solve at scale for 20 years, and solved it. Applied to forest data from Barro Colorado Island in Panama, the calculation shows that the mix of tree species changes 4.5 times faster than neutral biodiversity theory allows.
In genetics, the team analyzed 5.7 billion pairs of nearby mutations in genomes from the 1000 Genomes Project and found evidence of gene conversion. Nearly every analysis of linked genetic variation ignores that mechanism, from population history to disease mapping.
With biologists Scott Edwards and Paul Lewis, BootLoops scored all 15 possible family trees for humans, chimpanzees, gorillas, orangutans, and gibbons exactly, using a single mitochondrial gene. The accepted tree and the version with humans and gorillas swapped get exactly the same score, a tie no sampling method can establish.
Further from particle physics, one manuscript finds that sunspot groups appear to “age”: at a given size and hardiness, their risk of disappearing rises by about 20% a day. Another concludes that the cut points behind Medicare Advantage star ratings fail their own stated criterion in 104 of 123 recent computations. An exact calculation would shift roughly $0.9 billion to $1.4 billion in bonus payments over payment years 2025 through 2027.
A third tackled the Voynich manuscript, a 15th-century book nobody has ever been able to read. It ran every reading that can be turned into an automated procedure against tools proven to crack test ciphers, and none worked.
In economics, an “AI data editor” built with two economists took the replication packages of 4,452 papers from five leading journals, written for MATLAB, Stata, and other commercial software, and ported them to open-source code, about 30,000 routines in all. It then checked nearly every verifiable number against the published tables. The results are in a working paper from the NBER, the National Bureau of Economic Research.
The human expert redirects the question
In almost every case, Schwartz writes, Claude was technically correct, but the result wasn’t all that interesting until an expert steered the question. James O’Dwyer, a plant biology professor and neutral-theory specialist, told him the forest result would likely “be met with a shrug by many ecologists,” then suggested a better direction.
Schwartz also lists the model’s bad habits. Claude “loves to declare victory”: “Done, with one asterisk” often means “not done at all.” It has no sense of time and grinds through multiday calculations instead of building a faster tool.
Claude’s conclusions can be wrong even when its math is right. One of Schwartz’s tips: “Look at everything yourself.” He always asks to see the plots and is wary of vague claims like “good agreement.”
A busy start to October for AI in research
On October 6, OpenAI released 722 manuscripts on unsolved math problems, produced by an internal model, and withdrew three of them the next day over a sign error, according to Retraction Watch. The Association for Human Mathematics called the mass release “a demonstration of power.”
On October 8, the journal Science published Google DeepMind’s peer-reviewed paper on AlphaProof Nexus, a system that solved 9 of the 353 Erdős problems it attempted. Schwartz’s approach reaches beyond mathematics and brings in specialists from each field as coauthors.
Applying the same method to your own work
You don’t need Feynman integrals to borrow Schwartz’s setup: your files and written rules act as the harness.
- Write your rules and success criteria into files the model rereads for every task. That’s the idea behind Claude skills, projects, and .md files.
- Ask the model which method from another field would solve your problem. Survival analysis, which BootLoops applied to sunspots, is the branch of statistics that medicine and demography use for lifespans that are only partly observed. It also measures how long customers stay subscribed.
- Demand evidence: a table, a chart, a number you can recompute. Schwartz regularly has other agents challenge his results, and they catch different errors; our guide to organizing work across several agents explains how to split the roles.
- Keep human review on anything that goes to a client, and have a specialist validate results outside your field. Schwartz wrote to three biologists before one of them answered.
Our guide to building an AI agent without coding builds the same quote follow-up three times, with Claude, ChatGPT, and n8n. To choose a starting model, see our Claude vs. ChatGPT comparison for small businesses.
If you’re technical, try BootLoops directly: clone the repository, start your agent inside the folder, and ask it for a plan to approve before anything runs. The repository warns that some tools execute the contents of their input files, so only feed them files from sources you trust.
Results still to be verified
Schwartz calls them manuscripts, and none of the sources we read mentions publication in a peer-reviewed journal. He says several projects are still being explored and verified. The count of 36 comes from his own report, published by Anthropic, which funded the project.
Out of roughly 400 candidate problems, 36 led to a manuscript, about one in eleven. Schwartz also acknowledges that these projects used a lot of compute and tokens.
Read next
If you’d rather have an assistant already set up for your business, take a look at our AI assistant.
