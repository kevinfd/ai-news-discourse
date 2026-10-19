---
id: "d2e0474e389639aa"
title: "Claude designed quantum circuits up to 39x cheaper than the best published ones"
url: "https://maccus.fr/en/claude-quantum-circuits"
link: "https://maccus.fr/en/claude-quantum-circuits"
source: "MACCUS - Agence SEO, Influence & Marketing Organique"
domain: "maccus.fr"
source_type: "community"
collector: "reddit"
date: "2026-10-18T14:54:30Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["mawcopolow"]
language: "en"
summary: "The rate of progress is just insane"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "IBM", "Google", "US government"]
topics: ["models & research", "jobs & society", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 1490
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x956d5/claude_designed_quantum_circuits_up_to_39x/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude designed quantum circuits up to 39x cheaper than the best published ones

MACCUS - Agence SEO, Influence & Marketing Organique · mawcopolow · 2026-10-18

On October 16, 2026, Anthropic reported that Claude Mythos 5, working in a closed loop with an automated checker, designed quantum circuits that improve on the best published ones. The largest gain, 39x on one task, uses the paper’s own cost metric: Toffoli gates multiplied by qubits. One 53-hour run produced an elliptic-curve design with 17x fewer gates than the smallest previous one, for 12% more qubits. All the circuits were designed and verified on classical computers; none has run on quantum hardware.
On October 13, IBM Research said its AI agents found a quantum error-correction decoder design 204x faster than the reference in high-level synthesis estimates, for $299 of inference. On October 15, in work that involved no AI, Google showed on its Willow chip that magic states, a scarce ingredient of quantum computation, can be made with about 40x fewer errors.
Eight circuits and an automated checker
The work comes from Anthropic’s STEM Fellows Program: Andi Gu, mentored by Anthropic physicist Alek Kemeny, with Susanne Yelin and Mikhail Lukin of Harvard (Lukin also works with QuEra Computing). Their preprint, “Discovering state-of-the-art quantum circuits with large language models”, went up on arXiv on October 15 and has not been peer reviewed.
The method is an evolutionary search built on the open-source tool OpenEvolve. Claude Mythos 5 (our guide to the Claude models covers the Mythos line) writes Python programs that generate circuits; an independent evaluator rejects any circuit that fails its task and scores the rest by Toffoli count times peak qubit count. Toffoli gates are among the costliest operations on a quantum computer, since they “require expensive non-Clifford resources,” the paper notes. Starting from a blank program, the model picks the algorithm and circuit structure “without substantive human intervention,” the authors write.
The eight tasks span chemistry, optimization, quantum simulation, number theory and numerical computing. According to the abstract, “in seven of the eight tasks, the discovered circuits significantly reduce both Toffoli and qubit counts relative to the state of the art.” The table covers the six tasks with a published baseline.
Source: arXiv:2610.22367, Table 1. Cells give Toffolis / qubits for the best published circuit and for Claude’s, and cost is Toffolis times peak qubits; the authors computed the reductions from unrounded counts and rebuilt each published baseline themselves, tuned to its lowest cost. The seventh task, a decoder for a variant called Hermitian DQI, had no published reversible circuit to compare against. The eighth is the elliptic-curve work.
53 hours on an elliptic curve
Point addition dominates the cost of quantum algorithms for elliptic-curve discrete logarithms, and modular inversion accounts for most of it. Ordinary computers handle that step efficiently with a method called divsteps, but a straightforward quantum version must store a record of every branch it takes, which costs many extra qubits. Anthropic says Claude, in one 53-hour run “with minimal human input,” found a rule that recovers that record from the numbers themselves. It tested the rule in large numerical simulations, formalized it in the Lean proof assistant, and produced “the first reversible implementation of divsteps with no stored branch history.”
Claude then built a family of designs that trade qubits for gates. Compared with the smallest previous design, one uses 12% more qubits and 17x fewer gates. The benchmark curve is secp256k1, the one Bitcoin uses.
In March, a paper led by Google Quantum AI researchers kept its elliptic-curve circuits private and published a zero-knowledge proof of their cost instead, “in the interest of responsible disclosure.” The new paper’s authors published their construction on arXiv. Elliptic curves also sit behind many HTTPS certificates and passkeys, as we explained when Claude traced the origin of the NSA’s curve seeds; those NIST curves belong to the same family as secp256k1 but are different curves.
The second case Anthropic describes is decoded quantum interferometry (DQI), an optimization algorithm it calls one of the strongest candidates for a superpolynomial quantum speedup. Its costliest step is decoding, done by a Reed-Solomon decoder in the benchmark problem. Claude replaced the extended Euclidean algorithm of Google’s 2025 construction with Berlekamp-Massey decoding, ran 403 million simulated decodings to size the circuit’s memory, and cut the decoder’s gate count 12x.
IBM’s agent search cost $26 to $299 in inference
IBM worked on the classical side of the machine: the decoder hardware that reads error signals from a quantum processor and works out corrections, here Relay-BP for the [[144,12,12]] bivariate bicycle code. Its “agent factory” pairs a coordinator agent with four parallel workers that rewrite the decoder’s code, check it and synthesize it for an FPGA, within a budget of 100 design hypotheses.
In IBM’s paper, Claude Opus 5 in every role brought the estimated latency to 139 microseconds, against 28,231 for the reference design: the 204x figure IBM reports, for $299.45 in estimated inference cost. The open-weight GLM-5.3, self-hosted by IBM, reached 52x for $25.95, and 60x with a doubled budget of 200 hypotheses. A hybrid with a Claude Opus 5 coordinator and GLM workers reached 126x for $105.25. IBM ran each configuration once, and its costs cover model inference only.
Magic states on the hardware side
Google’s result, peer reviewed and published in Science, is about supply. A universal quantum computer needs “magic states,” which cannot be reused, and Google cites estimates that “up to 95% of a quantum computer’s entire capacity might need to be dedicated to making them.” On Willow, magic state cultivation, a protocol Craig Gidney, Noah Shutty and Cody Jones designed in 2024, cut errors about 40x and produced T-states with a record 99.99% logical fidelity. Google says the method still has to be shown at a larger scale.
The two results connect through the Toffoli count. The Anthropic paper notes that when magic-state factories have limited throughput, “as is typically the case,” runtime is bottlenecked by that count.
The design curve before AI
Quantum cost estimates have fallen for years on unchanged hardware assumptions. In 2019, Craig Gidney and Martin Ekerå estimated that factoring a 2048-bit RSA key would take 20 million noisy qubits; in May 2025, Gidney brought that under a million with the same assumptions. For FeMoco, the iron-sulfur core of a nitrogen-fixing enzyme, the gate estimate fell from about 50 trillion Toffolis in 2017 to about 340 million. Anthropic says that roughly 150,000-fold drop “took many research groups eight years,” each step usually taking months, and sets it against the single 53-hour run behind Claude’s elliptic-curve design.
For elliptic curves, the Google-led March paper estimated that solving the discrete logarithm on a 256-bit curve takes fewer than 1,200 logical qubits and fewer than 90 million Toffolis; in July, Han Luo and colleagues brought the logical qubit count to 835, at the price of far more Toffoli gates.
Limits on the record
The Anthropic paper is a preprint, and its circuits are logical designs checked by a classical evaluator, with simulations and a Lean proof for the divsteps rule. The authors call their cost metric one choice among others that are “equally reasonable,” since the right objective depends on the hardware and the error-correction architecture. Humans also wrote each task’s specification.
Anthropic adds that Claude was “conservative by nature” in early experiments: it second-guessed apparent improvements, re-checked results that were already well supported and preferred well-known methods. The team required it to develop several approaches in parallel and occasionally prompted it to broaden its search.
Nic Carter of Castle Island Ventures, quoted by The Block, said “there’s no imminent threat” while adding that AI is “meaningfully accelerating the rate of progress.” None of this week’s announcements from Anthropic, Google or IBM gives a date for a quantum computer able to break today’s encryption.
Design work that a computer can check
Google improved the hardware side this week with cleaner magic states on a real chip. On the design side, AI agents now propose quantum circuits and decoder designs while a classical program checks each candidate. Anthropic suggests AI could optimize every component of an error-corrected machine jointly, “from the algorithm down to the hardware,” and IBM already has agents working on decoder hardware. The same day, Vals AI released an index that scores models on research tasks graded automatically (see our article on the Vals Science Index).
On October 17 we covered AI-found counterexamples to a 1967 fusion conjecture, where the remaining bottleneck was choosing problems and testing results in a lab. In the Anthropic study, each input gives one definite output that an ordinary computer can check, so the checking happens before anything is built. Anthropic’s conclusion is conditional: if AI can speed up that work, “useful quantum computing could arrive sooner.” Matching decompilation of video games relies on the same kind of check, since rebuilt code either compiles to the original bytes or does not; on October 15 its hub, decomp.dev, said it is winding down as AI speeds up that work (see our article on AI and video game decompilation).
