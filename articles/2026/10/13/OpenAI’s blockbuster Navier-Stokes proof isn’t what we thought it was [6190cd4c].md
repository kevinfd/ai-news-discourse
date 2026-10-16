---
id: "6190cd4c053a94a0"
title: "OpenAI’s blockbuster Navier-Stokes proof isn’t what we thought it was"
url: "https://scientificamerican.com/article/openais-blockbuster-navier-stokes-proof-isnt-what-we-thought-it-was"
link: "https://scientificamerican.com/article/openais-blockbuster-navier-stokes-proof-isnt-what-we-thought-it-was"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T16:42:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["scientificamerican"]
language: "en"
summary: "Rumors that OpenAI’s “Navier-Stokes” solution stole the work of two mathematicians may have been overblown"
tags: ["r/artificial", "r/ArtificialInteligence"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "business & funding"]
content_source: "fulltext"
word_count: 771
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x530mt/openais_blockbuster_navierstokes_proof_isnt_what/"
score: null
comments: null
community: "r/artificial"
---

# OpenAI’s blockbuster Navier-Stokes proof isn’t what we thought it was

Scientific American · scientificamerican · 2026-10-13

Mathematicians are finally making sense of the biggest event in decades for their field—and it’s stranger than anyone thought.
In early September OpenAI posted an inscrutable 166-page solution to the Navier-Stokes problem, one of math’s famed “million-dollar problems.” Initial accounts—including from the company itself—suggested that the proof, produced by an internal large language model (LLM), followed an approach devised by two Spanish mathematicians, Diego Córdoba and Luis Martínez-Zoroa.
On supporting science journalism
The model’s purported reliance on this “Spanish program” sparked a very public conflict between the company and Tristan Buckmaster, a mathematician at New York University. Buckmaster had spent much of the past year using LLMs to carry out that program alongside Levent Alpöge, an employee of OpenAI’s archrival, Anthropic. The pair cried foul after OpenAI—whose public models Buckmaster and Alpöge had been using—announced a Navier-Stokes proof that seemed to build upon and then leapfrog over their hard-won progress. But the resemblance between the two groups’ methods now seems merely skin-deep.
“When you go to the details, it is a different approach,” says Gonzalo Cao-Labora, a mathematician at EPFL, the Swiss Federal Institute of Technology in Lausanne. Scientific American spoke with several groups of experts working through the OpenAI paper. All said that it’s increasingly clear that the company’s proof does not follow the Spanish program.
The Navier-Stokes equations are the math behind every fluid. OpenAI solved the million-dollar problem by uncovering a flaw in the equations. The company’s artificial intelligence concocted a situation in which the equations declared that the speed of a fluid’s flow should be infinite—a so-called blowup that can’t happen in real life.
OpenAI solved the problem with an “agent swarm,” some 10,000 copies of its new, math-adept LLM, which spent about 88 hours of computing time and 130 billion tokens collectively constructing a blowup. The company’s math team threw all its resources at the problem after learning of significant progress made by Buckmaster and Alpöge. Buckmaster has alleged that OpenAI then attempted to bribe and threaten him to prevent him going public with insinuations of malfeasance, which he ultimately did.
Even top experts have found OpenAI’s proof of blowup to be completely impenetrable. But the agents coded their arguments into Lean, a programming language used to automatically verify that the logical steps toward a conclusion in a given sequence are all valid. Several prominent research groups are now using both the Lean code and the paper, with the help of other LLMs, to get a simplified, bird’s-eye view of the math involved.
The proof does somewhat resemble the Spanish program in that both exploit the same “loophole” in the official framing of the Navier-Stokes problem that was given by the Clay Mathematics Institute. It permits a mathematician to coax the equations into blowing up by constructing a weird, unphysical force that “stirs” the fluid just right. But closer examination reveals that OpenAI’s proof builds its unnatural force in a totally distinct way. The proof’s similarities to Buckmaster and Alpöge’s progress are superficial.
Of course, the OpenAI result’s novelty doesn’t mean it wasn’t influenced by the Spanish program. In fact, OpenAI initially used a smaller team of agents to prove an intermediate result, and some experts say that this more modest squad did follow the program. But the 10,000-agent swarm apparently realized a different path was required to finish the job. Of course, regardless of OpenAI’s insistence that its model couldn’t have seen Buckmaster’s specific user data, the “black box” nature of LLMs means we’ll likely never know the swarm’s exact chain of reasoning.
“I honestly don’t see a factual resolution of this,” says Camillo De Lellis, a mathematician at the Institute for Advanced Study in Princeton, N.J. “It’s not anymore a matter of clearly verifiable mathematical facts.”
What’s important, and perhaps a harbinger of math’s future, is how long it took experts to realize all this. When OpenAI revealed its landmark achievement on September 8, company officials clearly and repeatedly stated that their proof followed the Spanish program. Their combative exchange with Buckmaster before the release seems to suggest that they believed as much. And they weren’t initially certain whether his work had been incorporated in their model’s training data.
That is, OpenAI didn’t understand its own model’s proof. And still, more than a month later, no one fully does.
Last week the company dumped some 400 more results on the community. In the pre-AI era, at least a dozen of those results could have merited any human mathematician a Fields Medal—math’s Nobel Prize. There already aren’t enough experts on Earth to keep pace with the onslaught, and there’s no sign that it’s slowing down.
