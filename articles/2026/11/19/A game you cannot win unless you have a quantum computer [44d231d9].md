---
id: "44d231d9ee488f2d"
title: "A game you cannot win unless you have a quantum computer"
url: "https://research.google/blog/a-game-you-cannot-win-unless-you-have-a-quantum-computer"
link: "https://research.google/blog/a-game-you-cannot-win-unless-you-have-a-quantum-computer"
source: "Google Research"
domain: "research.google"
source_type: "research"
collector: "rss"
date: "2026-11-19T20:03:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: []
language: "en"
summary: "Quantum"
tags: ["Quantum"]
orgs: ["Google"]
topics: ["models & research", "health & science"]
content_source: "fulltext"
word_count: 1675
paywalled: false
image: "https://storage.googleapis.com/gweb-research2023-media/original_images/QuantumContextuality1-MagicSquareGame.png"
discussion_url: null
score: null
comments: null
community: null
---

# A game you cannot win unless you have a quantum computer

Google Research · 2026-11-19

November 19, 2026
Shashwat Kumar and Rodrigo Cortiñas, Research Scientists, Google Quantum AI, Google Research
On a superconducting processor, we turned one of quantum mechanics’ strangest features into something you can measure, benchmark, and put to work across systems as large as 105 qubits.
Here is a Sunday paper-style puzzle you can try right now. Draw a 3×3 grid. Fill every cell with either +1 or −1, subject to two rules: each row must multiply to +1, and each column must multiply to −1.
Go ahead. We’ll wait…
You didn’t manage it, right? There is an elegant reason for that. For a row to multiply to +1, it needs an even number of −1s. For a column to multiply to −1, it needs an odd number. Add up the rows and you learn the grid contains an even number of −1s. Add up the columns and you learn it contains an odd number. Well…That’s impossible!
The grid would have to be two contradictory things at once. No such table exists; it is a paradox.
Now turn the puzzle into a game: Each round, Alice is handed a row and Bob a column. Without talking, Alice fills her row by the row rule and Bob fills his column by the column rule. They win if they put the same number in the square where their row and column intersect. Any plan made in advance is just a pre-written table, meaning at best they will win 8 out of 9 rounds. This changes if they use a quantum computer. It won't fill in the impossible grid, but in principle, it lets them win every round.
The reason is a property called quantum contextuality, arguably the strangest feature of quantum mechanics. Einstein once famously asked whether the moon is there when nobody looks, his way of insisting that physical properties ought to exist whether or not anyone measures them. For quantum systems, contextuality is the precise, experimentally testable statement that the answer can be no: you cannot assign fixed, pre-existing values to everything you might measure.
What a measurement yields can depend on which other compatible measurements you make alongside it (i.e., on its context). This is not only a deep philosophical statement, but more so, cutting-edge science and the basis of a new technology. And in the game above, Alice and Bob can use it to engineer a solution. Their answers are not looked up in a hidden table written in advance; the table does not exist. Their answers come into being as they measure, and quantum correlations stitch them together more tightly than any classical rulebook permits.
Entanglement usually gets top billing as the “magic ingredient” of quantum computing. But a growing body of theory suggests contextuality is the deeper resource, the thing that actually powers certain quantum algorithms past their classical counterparts. The catch is that, until recently, contextuality had been demonstrated almost exclusively in small systems of a few particles. Whether it survives, and stays useful, in the many-body systems that real quantum computers are made of was an open question.
That is the question we set out to answer. In "Quantum-classical separation in bounded-resource tasks arising from measurement contextuality," published in Science, we demonstrate and measure contextuality on our superconducting quantum processors. Our qubits win the magic square game 98.3% of the time, exceed the classical limit on a contextuality test, and outperform classical strategies in tasks spanning up to 105 qubits. Along the way, these tasks proved to be a sensitive new benchmark for quantum hardware, catching subtle errors that random-circuit tests miss.
We ran what is commonly called the magic square game on our Willow quantum processor. Alice and Bob each hold two qubits, sharing two entangled Bell pairs instead of a pre-written table, and measure them using preset settings for their assigned row or column to get their ±1 entries.
The best conceivable classical strategy loses at least one round in nine, winning at most 88.89% of the time. When we played all nine versions of the game 100,000 times apiece, our qubits lost roughly one in sixty, winning 98.30% of them (0.9830 ± 0.0001).
The gap is meaningful and statistically significant: our qubits coordinated better than any pre-written table allows. That's because no cell has a value fixed in advance. Each answer takes shape only when it is measured alongside the rest of its row or column (its context), and shared entanglement makes Alice's and Bob's answers for the shared cell agree.
The magic square game demonstrated the potential power of contextuality, so next we set out to measure how contextual a machine is. We used a Bell–Kochen–Specker inequality, closely related to the famous Bell test which showed that entangled particles like the Bell pairs above can't carry answers fixed in advance. Our inequality bundles a set of correlations into a single number, χ. In terms of the rows and columns from the game above it reads, χ = R1 + R2 + R3 − C1 − C2 − C3, where R and C represent the products of the rows and columns Alice and Bob had to calculate earlier:
Any universe where measurement outcomes are predetermined must obey χ ≤ 4 (try a few tables and you will see that χ can only take values -4, 0, and 4). Quantum mechanics permits values up to 6, which can only happen if all Rs = +1 and all Cs = -1. And unlike most such tests, this one is state-independent: it doesn’t matter how you prepare the qubits, which makes it a property of the machine rather than of a carefully chosen input.
Measuring χ is demanding: every row and column must be measured on the same two qubits, one after another, without disturbing them. We did this with an extra helper qubit (an "ancilla") that picks up each result and is measured instead, leaving the two main qubits intact. We ran 540 measurements in a row, repeated 1,000 times.
We measured χ = 5.590 ± 0.008.
Comfortably past the classical bound of 4 and only 7% away from the quantum limit. A number that says: the contextuality is in this machine in this quantity.
Two qubits are one thing, but quantum effects are fragile, and every added qubit brings noise that can wash them out. Useful quantum computing needs many qubits working together, so the question is whether contextuality survives at scale.
In the GHZ parity game, N players share one entangled GHZ state (a superposition of all qubits being 0 and all being 1). Each player gets a one-bit question and answers with one bit, without communicating. They win if the parity (even or odd) of all the answers matches a rule set by the questions. Random guessing wins half the time, and the best classical plan does only a bit better: 75% for three players, shrinking toward 50% as players are added. A shared GHZ state wins every time. We played with up to 71 players, one per qubit. Noise keeps us below 100% and grows with each added qubit, so our lead narrows, but we stay above the classical bound throughout. We also verified genuine entanglement across 45 qubits, more than the full size of many earlier GHZ experiments.
Beyond multiplayer games, the same physics separates shallow quantum and classical circuits. In 2018, a landmark theorem proved that a specific problem, finding a hidden linear function, can be solved by a constant depth quantum circuit, and that no classical circuit of constant depth can. The source of this quantum advantage traces back to contextuality.
In this proof, constant depth matters. It means the circuit doesn’t get deeper as the problem gets bigger. Because every output bit is computed in a fixed number of steps, information has time to travel only a short distance. Each classical output can therefore only “see” a small neighborhood of the input, like a rumor that must cross a city in three minutes. Quantum circuits, with entanglement already laid down, are not so limited.
That algorithm had never been run at scale on real hardware. We ran it, solving hidden-linear-function instances on grids of up to 105 qubits, with success probabilities above one-half, using exactly the shallow-circuit recipe the theory prescribes.
While running these experiments, something useful happened along the way. These tasks demand that many qubits agree simultaneously and exactly. Running them surfaced subtle coherent errors in our system, the kind that rotates a quantum state slightly off-target, which conventional random-circuit benchmarks tend to average away into invisibility.
That suggests a second use for contextuality: not just as a computational resource, but as a ruler.
Most benchmarks ask whether a processor can clear some classical bar. These tasks instead give hardware a ceiling set by physics itself: χ = 6, a win probability of 1, a perfect contextual fraction. The distance between what a machine achieves and what nature permits becomes an objective, meaningful score. And unlike classical bars that get easier to clear, this ceiling never moves. The better our quantum processors get, the more precisely such a benchmark discriminates. This is particularly relevant for real-world applications, such as simulations of molecules for chemistry and materials science, because it measures a processor’s ability to run structured algorithms, where subtle errors can’t hide.
A nearly century-old argument about whether physical systems always exist when nobody looks turns out to have a measurable test. For our qubits, the verdict is clear: not everything we measure can have pre-existing values waiting to be observed. Theory links contextuality to the "magic states" that error-corrected quantum computers need to run full algorithms, which our team recently prepared using magic state cultivation.
Measuring contextuality across many qubits lets us probe an open question in physics and computer science on real hardware: what gives quantum computers their edge.
This work was carried out by the Google Quantum AI team together with our academic collaborators. We thank everyone who built and maintained the hardware, control electronics, cryogenics and software that made these experiments possible.
    ×
    ❮
    ❯
    
  
  ×
