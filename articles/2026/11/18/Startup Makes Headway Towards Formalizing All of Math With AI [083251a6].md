---
id: "083251a67bf4adea"
title: "Startup Makes Headway Towards Formalizing All of Math With AI"
url: "https://spectrum.ieee.org/enormous-theorem-ai"
link: "https://spectrum.ieee.org/enormous-theorem-ai"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T13:00:03Z"
published_date: "2026-11-18"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Benjamin Skuse"]
language: "en"
summary: "As Axiom Math ’s AI swarm was putting the final touches on the automatic verification of 15,000-page proof of the Classification of Finite Simple Groups (CFSG) , colloquially referred to as the ‘enormous theorem’, on Sunday 25 October, the company’s Founding Mathematician Ken Ono had nothing to do but watch and reflect on the achievement. As the son of a mathematician , he had grown up…"
tags: ["Mathematics", "Artificial-intelligence", "Science", "Formalization"]
orgs: []
topics: ["business & funding", "models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1086
paywalled: false
image: "https://spectrum.ieee.org/media-library/a-dot-with-thousands-of-plotted-points-radiating-from-its-center.jpg?id=68692858&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Startup Makes Headway Towards Formalizing All of Math With AI

IEEE Spectrum · Benjamin Skuse · 2026-11-18

As Axiom Math’s AI swarm was putting the final touches on the automatic verification of 15,000-page proof of the Classification of Finite Simple Groups (CFSG), colloquially referred to as the ‘enormous theorem’, on Sunday 25 October, the company’s Founding Mathematician Ken Ono had nothing to do but watch and reflect on the achievement.
As the son of a mathematician, he had grown up surrounded by some of the architects of the CFSG’s proof, widely considered to be the longest mathematical proof ever written by humans. Now, he was contributing to formally verifying what his father and peers had created. “My wife was with me as I watched the team countdown to completing the verification,” he recalls. “God, I cannot tell you how emotional I was.”
University of St Andrews group theorist Colva Roney-Dougal (who was not involved in the work) says of formalizing CFSG: “I held it up as an example of something that was going to be incredibly hard to formalize because I had thought that the amount of computing it was going to require was just unattainable,” she says. “So when I heard the announcement, I was really, really surprised.”
This result, along with the concurrent formal verification of the 7500-page Stacks project, represent a huge AI engineering achievement and lay some of the groundwork for digitizing all mathematics.
Formally enormous
Why the hoo-ha? The CFSG concerns finite simple groups. These are groups (sets of elements combined with an operation, like addition or multiplication, that follows specific rules) that are simple (in other words, cannot be reduced or simplified further) and finite (as opposed to groups containing an infinite number of elements). For example, all the permutations of a deck of cards form a simple finite group.
Évariste Galois laid the foundations for group theory almost 200 years ago. Finite simple groups have since been classified by myriad mathematicians into 18 families (plus 26 sporadic simple groups that do not belong to any of these families). The CFSG’s proof confirms that this list is complete.
But this simple task was only achieved by bringing together results and arguments that far exceed what any individual mathematician can fully absorb from more than 500 journal articles written by around 100 authors over a half-century period. Translating this interconnected web of knowledge into code and verifying its correctness therefore posed a number of significant engineering challenges, even beyond those overcome in earlier proof formalizations by Axiom Math this year.
One of the hardest, according to Axiom Math’s Niels Voss, who led the CFSG formalization, was the sheer length of the proof. Over 15,000 pages of dense mathematics, the CFSG proof contains multiple theorems, lemmas, and definitions none of which can be checked until everything has been made machine-readable.
To get around this required some ingenuity. “We processed all the literature from the CFSG, and traced the network structure of the informal proof before we were able to start working on it,” says Voss. “We then broke up the statement of the CFSG into about 100 milestones—landmark results along the way that can be independently verified—which we used to guide the formalization and stay on track.”
Roney-Dougal says she is very impressed with the result, and particularly appreciates how the formal proof finds and clears up several mistakes in the original human proof. She thinks this result is critical to formalizing any modern research in group theory, such as her own work understanding how simple finite groups behave.
But, Roney-Dougal says, because the verification was done automatically, there are few mathematicians capable of extracting information from the proof to share with the community, and that a new generation of mathematicians may have “missed a chance to gain knowledge from the doing of it”.
Stacks of ingenuity required
Just nine days after the CFSG formalization announcement, Axion Math revealed it had automatically formalized the Stacks project, too. Started in 2005 by Columbia University mathematician Aise Johan de Jong, Stacks is a massive, open-source collaborative mathematics textbook and reference work focused on highly abstract algebraic geometry and algebraic stacks (geometric spaces that are vital to modern string theory and number theory).
Whereas CFSG is a single (huge) landmark theorem, the Stacks project is essentially a well-structured library of thousands of interlocking definitions, constructions, and lemmas bringing all of modern algebraic geometry together.
The final Stacks formalization stands at a mere 16 million lines of code (compared to CFSG’s 43 million lines of code, roughly on a par with the Linux kernel), but it presented a different challenge to Axiom Math engineers: needing to achieve faithfulness and coherence across thousands of interlocking definitions and theorems, says Axiom Math’s Vasily Ilin, who led the project.
This required the team to design a hierarchical system of AI agents with specialized responsibilities working in parallel, keeping every definition aligned across the library, while also checking faithfulness with multi-agent audits, cross-checks against sources, and hard tests. This ensured that every element and task aligned across the entire project.
A highly efficient, general, reusable, and maintainable formal library of foundational concepts underpinning much of modern mathematics, the impact of the Stacks formalization could be profound. Now, anyone or any bot can access the formal Stacks library and build new formal mathematics upon it. And together, the CFSG and Stacks formalizations represent a significant step toward formalizing all of mathematics. “They show the two ways formalization has to scale: one very long proof, and one very wide body of connected theory,” says Ono.
Ono and Voss see numerous advantages to a future in which formal mathematics becomes central: rubber stamping theorems and proofs, preserving knowledge as expertise dwindles over time, and building a shared library as a basis for creating new mathematics. They are also optimistic about humanity’s role when all of mathematics is formalized, viewing formalization as a launchpad for humans to use and understand mathematics in new and innovative ways. “Aren’t we excited to think more broadly about what the future of math can be?,” asks Ono. “I’m excited by that. I’m really excited.”
- AI Solves a Major Unsolved Math Problem. Not Everyone Is Happy ›
- AI Used to Verify Toughest Mathematics Proof Yet ›
Benjamin Skuse is a professional freelance writer of all things science and technology. Previously, he earned a Ph.D. in applied mathematics from the University of Edinburgh and an M.Sc. in science communication from the University of the West of England. His work has appeared in New Scientist, WIRED, Physics World, Sky & Telescope, Photonics Focus, and many more.
