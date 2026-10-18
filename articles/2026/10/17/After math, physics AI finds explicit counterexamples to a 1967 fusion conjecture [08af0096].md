---
id: "08af009615ce1d7b"
title: "After math, physics: AI finds explicit counterexamples to a 1967 fusion conjecture"
url: "https://maccus.fr/en/ai-physics-fusion-conjecture"
link: "https://maccus.fr/en/ai-physics-fusion-conjecture"
source: "MACCUS - Agence SEO, Influence & Marketing Organique"
domain: "maccus.fr"
source_type: "community"
collector: "reddit"
date: "2026-10-17T13:00:46Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["mawcopolow"]
language: "en"
summary: "I seriously can't wait to see what the next few months have in store, hope they'll get to practical applications soon"
tags: ["r/OpenAI"]
orgs: ["Anthropic", "Google", "OpenAI"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "health & science"]
content_source: "fulltext"
word_count: 1316
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1x89ou3/after_math_physics_ai_finds_explicit/"
score: null
comments: null
community: "r/OpenAI"
---

# After math, physics: AI finds explicit counterexamples to a 1967 fusion conjecture

MACCUS - Agence SEO, Influence & Marketing Organique · mawcopolow · 2026-10-17

On September 22, 2026, Matt Landreman, a plasma physicist at the University of Maryland, posted explicit solutions to the equations behind stellarator fusion designs. Harold Grad had conjectured in 1967 that solutions of this kind did not exist. The paper’s acknowledgments say the solutions “were discovered using the artificial intelligence model GPT-6 Astra Pro”, and that Landreman confirmed every equation by hand.
Thirteen days later, three Google DeepMind researchers and Landreman extended both families of solutions to shapes without stellarator symmetry. Their paper credits Gemini 4, run as a small team of agents, and reports that “promising candidates appeared within hours.” In the same three weeks, one AI agent scored 98% on unpublished physics research problems, and other agent teams found an enzyme system with CRISPR-like repeats and proposed a magnet for future computer memory. The math wave of September has reached the sciences whose answers can be checked.
A 1967 conjecture, two papers in thirteen days
The question is about plasma equilibrium, the balance between a confined plasma’s pressure and the magnetic field holding it. Grad argued that smooth solutions with varying pressure would need an extra symmetry, as in a doughnut-shaped tokamak. Stellarators are twisted on purpose and lack that symmetry.
Landreman’s two families are smooth and three-dimensional, with perfectly nested magnetic surfaces. He calls them “counterexamples to Grad’s conjecture” and writes that for stellarators “it is reassuring to know with certainty” that such equilibria exist. The October 5 paper adds that exact solutions like these provide benchmarks for the codes used to design stellarators. Its authors write that they chose the problem, steered the agents, ran several rounds of adversarial review and re-derived every result themselves.
Neither paper says anything about when a reactor will run. Landreman posted a first version on September 22 and a revision on September 28; the generalization followed on October 5. A day before his first version, on September 21, mathematicians Javier Gómez-Serrano, Lukas Liehr and Mitchell Taylor had posted a Lean-certified proof that such counterexamples exist. Landreman’s revision credits them, and the October 5 paper calls his solutions the first explicit closed-form equilibria of this kind.
The physics papers followed the math news by two weeks. On September 8, OpenAI posted a claimed resolution of the Navier-Stokes Millennium Prize problem by an internal model, using a group of roughly 10,000 concurrent agents; the result came about 88 hours after the first agents launched. On October 13 we covered a Harvard physicist who produced 36 manuscripts across 18 fields with Claude in three months.
Research calculations for under $3 on average
On October 9, physicists from institutions including ICTS, Harvard University, KU Leuven and Google DeepMind released TheoPhysEval. It holds 50 unpublished research problems in theoretical physics, and the authors say a world expert could solve a typical one “in about a day or less.”
With literature search and the ability to write code, GPT-6 Astra running in Codex reached the right final answer on 49 of the 50, “at an average cost under USD 3 per problem.” Astra’s run on all 50 problems cost $116.28 at API rates. Claude Opus 5.5 in Claude Code solved 46; our guide to the Claude models explains where Opus sits in Anthropic’s lineup.
One passage in the paper is about grading. The team first marked several of Astra’s answers wrong, then found “subtle errors in the original solutions” written by the experts. Once the experts fixed their own work, Astra’s answers stood.
The authors keep the result in proportion. They describe their problems as “turn-the-crank” research: a known technique pushed to a new case, novel and sometimes publishable, “but not pathbreaking.”
Biology, materials and the Thomson problem
On September 23, Anthropic’s new life-sciences lab described a run in which about 950 Claude agents searched a DNA database for 21 hours before one of them spotted something odd. In that campaign the agents gathered more than 200,000 reverse transcriptases, picked out 3,500 candidate systems and wrote reports on the 20 most compelling. One, which Anthropic calls ART, sits beside an array of DNA repeats that resembles CRISPR. Its function is still unknown, human scientists do the lab work, and Anthropic says this kind of analysis can take an expert “weeks to months.”
On October 4, Vals AI reported that one of its researchers, working with a team of AI agents running density functional theory calculations, designed one candidate magnetic semiconductor and identified a second. The second was first made in 1999 and stayed magnetically ordered up to 376 K. Both are predictions for perfect crystals, and the post links to a public repository with every input file and a list of known caveats.
A week earlier, Vals AI’s Hung Tran gave ten Claude Sonnet 5.5 agents the Thomson problem for seven charges, which asks how seven electrons arrange themselves on a sphere to keep their energy as low as possible. After about 15 hours and 1,270 messages they produced a 17,895-line Lean proof that the pentagonal bipyramid is the unique answer. The project’s GitHub repository says the statement has not been certified by a human and the work has not been peer reviewed.
Checkable fields fall first
Terence Tao gave the reason for the math wave in his October 9 lecture at Caltech. His slides say labs prioritized mathematics because it offers “objective verifiability, digitizability, and large, high-quality data sets,” and that math is “now entering an era of proof abundance.”
Every result above has the first of those properties. A Lean proof is checked by a machine. A closed-form plasma equilibrium can be checked symbolically, which is what the October 5 authors did. Anyone with the input files can rerun a density functional theory calculation, and a sequence database gives agents millions of cases to compare.
Our bet is that other fields will flip roughly in order of how cheaply an answer can be verified. Computational chemistry, materials screening and genomics sit near the front of that line. Cryptography had its turn in October 2026, when an internal Anthropic model showed that the NIST curve seeds supplied by the NSA came from a generator seeded with the clock, a result anyone can recompute.
OpenAI reports about 130 billion output tokens for Navier-Stokes alone. A day of expert physics calculation, by TheoPhysEval’s numbers, now costs a few dollars. The two figures were published a month apart, and only the second fits the budget of an ordinary research group.
The best objection comes from the papers
The TheoPhysEval authors raise the sharpest doubts themselves. Accuracy barely moved when they cut the agents off from web search and background papers, which they read as “significant memorization of the literature.”
They also note that agents have produced no breakthroughs in theoretical physics, and one explanation they give is taste: asked to invent new problems, the agents “focus excessively on details that a human might find uninteresting.” Human experts still set the direction. Tao’s slides add that “most of the problems at the current frontier of mathematics remain unsolved.”
Those limits locate the bottleneck: picking the problem and testing the result in a lab. Because Claude “produces hypotheses so prolifically,” Anthropic’s scientists now study which ones they choose to test, and feed what they learn back into Claude’s instructions so it can “mimic our own scientific taste.”
The question Landreman left open
Landreman’s paper ends its discussion on a related open question: whether non-axisymmetric equilibria with exact quasisymmetry exist. Neither paper answers it. Landreman’s revised paper notes that at least three families of exact solutions now exist and that “it is likely that there are others,” and the October 5 authors list broader classes of exact equilibria as future work.
For a small business, the same rule applies: hand AI the work whose results you can check. If you want an assistant set up that way for your admin tasks, see how our AI assistant works.
