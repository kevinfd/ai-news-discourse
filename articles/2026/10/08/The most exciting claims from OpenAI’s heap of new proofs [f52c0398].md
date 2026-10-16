---
id: "f52c0398fdda9022"
title: "The most exciting claims from OpenAI’s heap of new proofs"
url: "https://scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs"
link: "https://scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-08T19:30:00Z"
published_date: "2026-10-08"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Peter Hall", "Joseph Howlett"]
language: "en"
summary: "Scientists have called out several math and computer science results as the most significant in the company’s overwhelming new deluge of achievements"
tags: []
orgs: ["OpenAI"]
topics: ["models & research", "health & science"]
content_source: "fulltext"
word_count: 2234
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# The most exciting claims from OpenAI’s heap of new proofs

Scientific American · Peter Hall, Joseph Howlett · 2026-10-08

On Tuesday afternoon OpenAI dropped more than 700 manuscripts reporting proofs, solutions and progress on 372 open problems across theoretical research.
It will take time for mathematicians to trudge through all the artificial-intelligence-generated results. No one, not even OpenAI researchers themselves, has been able to even read through everything yet. And not all of the proofs were certified as correct by the automatic logic verification platform Lean—in fact, some have already been retracted after outside scientists found mistakes. OpenAI also did not include full prompts or run-time details for how their agents uncovered the proofs, and officials admitted in a blog post about the results that citations and written descriptions of findings could be improved in future releases.
READ MORE: Mathematicians marvel, and grumble, at OpenAI’s trove of new results
On supporting science journalism
Despite these issues, experts say the results are jaw-dropping. The papers span mathematics, theoretical computer science, physics, and more. Some of the discoveries could have easily netted a human author a top research award just a year ago
Here are just some of the most important problems OpenAI claims to have solved, according to the experts.
MATH
Toward the Riemann Hypothesis
The Riemann hypothesis is the scariest open problem in math—experts told Scientific American earlier this year that they barely think about it because they have no idea how to even start tackling it. That might have just changed.
The hypothesis centers on a special, complicated equation called the Riemann zeta function—specifically, which numbers you can put into this function to make it come out to zero. If you could magically know all of these special inputs, you would essentially know all of the prime numbers—mathematicians’ favorite objects and the building blocks of the entire number line.
OpenAI’s drop contains two major results about these “zeros.” One proves the “quasi-Riemann hypothesis,” which is a huge step toward the holy grail of proving the full thing. “Plenty of applications of the Riemann hypothesis did not need the full Riemann hypothesis,” says Hector Pasten, a mathematician at the Pontifical Catholic University of Chile. “The quasi-Riemann hypothesis is way more than enough for many applications.” For instance, mathematicians now have a better estimate of where the primes sit as you go up the number line than they ever had before.
As to whether this proof is a path toward solving the full hypothesis, it’s too early to say. “Some people claim it is progress toward Riemann; other people say it’s not,” Pasten says. “Usually the word progress makes sense after the fact, when you see how it eventually gets solved.”
The second result shows that neither the zeta function nor many of its generalizations, called “Dirichlet L-functions,” have a “Siegel zero,” a certain, especially problematic type of zero that would contradict the hypothesis. “This is not just progress on Siegel zeros—it settles the question,” Pasten says. “This is amazing.”
Hilbert’s 10th Problem
Hilbert’s 10th problem is about which mathematical truths are and are not knowable. It asks whether it’s possible to build an algorithm that sorts all simple algebra problems into two piles. One pile holds equations that have whole-number solutions, such as y2 = 2x (where x = 2 and y = 2 is a solution). The other pile consists of equations without a solution in which the variables are whole numbers, such as y2 + x2 = –1.
In 1970 mathematician Yuri Matiyasevich showed that such an algorithm is impossible. No computer can tell you whether or not any equation has a solution with whole numbers. But since then mathematicians have been struggling to extend this result, asking if a computer can sort equations when you allow their variables to have a wider range of values, such as fractions, square roots or imaginary numbers. OpenAI’s model proved that even when the variables are allowed to be any rational number—a whole number or a fraction—the mathematical world remains unsortable.
The new proof uses two of Pasten’s ideas from seemingly different areas of mathematics—even he hadn’t realized they could be put together in this way. “It’s extremely surprising to me that they connect,” Pasten says. “Their general strategy is original.”
The Kakeya Conjecture
The Kakeya conjecture can be thought of as sliding and twirling a piece of chalk around on a tablet so that it points in every direction but covers as small an area with chalk as possible. Mathematician Hong Wang won a Fields medal this summer for solving the three-dimensional version of this problem with mathematician Joshua Zahl. In that version, you twirl the stick around in midair—showing the minimum possible 3D space the twirl can occupy. Now OpenAI’s model has solved the problem for four dimensions.
Artin, Erdős, and More
Other important number theory results include Artin’s conjecture on primitive roots, which is about special number systems that stop at a certain, highest number, as well as a proof of perhaps the most famous conjecture of storied problem-poser Paul Erdős and progress that is relevant to the Langlands program, a sweeping set of conjectures sometimes called “a Grand Unified Theory of Mathematics.”
PHYSICS
Baby Yang-Mills
On its face, the “nonlinear sigma model” doesn’t sound like it has anything to do with particle physics. At every point on a grid, you place an arrow in a different direction to represent interacting, spinning atoms. The goal is to show that rotations of the arrows in one place cannot be detected far away. But that aim bears a striking, hidden resemblance to “the Yang-Mills existence and mass gap problem,” one of the five remaining Millennium Prize Problems, which aims to underpin the “Standard Model” of particle physics with rigorous mathematics. “This goes back 50 years, much like Yang-Mills, and is widely considered the ‘warm-up’ for Yang-Mills,” says Michael Douglas, a mathematical physicist at Harvard University.
OpenAI’s repository contains several papers claiming to completely resolve the equivalent of the Yang-Mills problem for this simpler model. New York University mathematician Roland Bauerschmidt says the first of these papers is both groundbreaking and comprehensible. “I haven’t digested it or understood all the details, but it seems very reasonable,” he says. The rest of the papers related to this problem are incomprehensible slop, he says, too hard for even a human expert to verify. “The second paper is horrible,” Bauerschmidt says. “If these results had been sent to me by a nobody, I would have deleted the e-mail.”
Einstein’s Baby
Physicists know a strange state of matter called the “Bose-Einstein condensate” is possible because researchers have made it in a lab—winning them the 2001 Nobel Prize in Physics. This material is where all the atoms in a gas occupy the exact same quantum state, producing weird quantum effects at unusually macroscopic scales. Albert Einstein originally predicted its existence in work that built upon a 1924 paper by physicist Satyendra Nath Bose, but he only proved that the state is mathematically possible for an unrealistic gas where no two atoms interact. OpenAI’s model extended the prediction to a case with interactions. It used similar techniques to prove a major conjecture about the math of ferromagnetism—one that the famous mathematical physicist Freeman Dyson erroneously claimed with two collaborators in 1976.
COMPUTER SCIENCE
Faster Matrix Multiplications
Anyone who's taken a linear algebra course can attest that matrices—ensembles of numbers in a two-dimensional array—underpin many different fields of computer science. Manipulating and performing operations on them quickly is important for computer graphics, complex simulations and machine learning itself. “Matrix multiplication is needed all over the place," says Virginia Vassilevska Williams, a computer science professor at MIT who researches the problem. "But also, its complexity is one of the great mysteries in computer science." Multiplying two matrices together requires a tedious amount of arithmetic.
The number of mathematical operations it takes to do these matrix multiplications scales with the cube of the length of the matrices. Scientists have sought a way to shrink the size of the exponent. If they had to do fewer than a cube of the length, it could mean exponential time savings. A few years ago, Vassilevska Williams and her colleagues had gotten that exponent down from 3 to around 2.37, the lowest ever achieved. Problem 107 claims a new lowest boundof 9⁄4, or 2.25. Paper 109 supposedly uses similar methods to find new, faster ways to multiply integers together, too. “In a maybe diabolical sense, the advance on matrix multiplication can be seen as an attempt by the LLMs to speed themselves up," Vassilevska Williams says.
L = RL = BPL
If algorithms research is about the best ways to solve problems, complexity theory asks the reverse: How hard is it to find the best solutions to problems—the ideal algorithms that can’t be beat? This challenge involves thinking about what kinds of resources a computer has at its disposal and asking which resources let one solve more problems. A classic quandary about problems computers can solve called P versus NP, likely one of the hardest of the Millenium Prize Problems, is perhaps the most famous complexity problem.
A key to both algorithms and complexity is asking how the solution or problem scales with the size of its input. For example, in the case of multiplication, researchers would want to know not just the best way to multiply two 100-digit numbers but how long it takes to multiply numbers of any size as a function of how many digits they have.
L, also known as LOGSPACE, is the complexity class of problems that can be answered with very little space—logarithmic in the size of the problem’s description. RL and BPL, meanwhile, are randomized versions of LOGSPACE in which the computer can harness randomness and only needs to be right most of the time. Proving that L = RL = BPL, as Problem 103 claims to do, shows that every problem of this type that can be done with randomness can also be done without it, known as derandomization.
In practice, computer programs use randomness all the time, but many researchers think it probably doesn’t speed up algorithms. “We have strong reasons to believe that, but we don’t know how to prove it,” says Ran Raz, a complexity theorist at Princeton University. While there was evidence that L = RL was likely to be true, proving it directly has been elusive until now. “I didn’t see any directions that were promising [before],” Raz says.
Unique Games
The unique games conjecture also falls under complexity theory. First pitched in 2002, it implicitly asks how hard it is, given a set of constraints, to satisfy some portion of them. Here the resource under the microscope is approximation—that is, instead of getting an exactly correct answer to a given problem, the computer only needs to get close to the answer. Although the unique games problem isn’t explicitly about approximation, showing that it’s difficult would imply that finding approximate answers to many problems is as hard as finding the answer directly.
Problem 102 claims to do just that, proving that the unique games problem is hard. This solution has been a bit controversial. Other researchers who had caught wind of OpenAI’s work on the problem rushed out their partial progress toward the answer in fear of being scooped by AI.
Unitary Synthesis
Over in the land of quantum computing, meanwhile, Problem 283 could give a better picture at how difficult truly quantum problems are. Scientists understand how bits in a classical computer work and can be manipulated, but they have less of a handle on quantum computing’s analogue to the classical bit, the qubit.
The unitary synthesis problem was first posed by researchers Scott Aaronson and Greg Kuperberg in 2006. It tries to relate working with qubits to working with bits. In this case, OpenAI showed that for any manipulation of a quantum state of qubits—called a unitary—they can build a quantum circuit and a problem dealing with only classical bits such that the circuit and problem can be used to calculate these manipulations, i.e., it can “synthesize” that unitary. Importantly, this solution gives some evidence that hard quantum problems may not be that much harder than hard classical problems, a surprising result that was not clear to researchers in the field before now.
Fast Fourier Transform
The Fast Fourier Transform, an algorithm whose discovery dates back to 1965, is crucial to the Internet and other forms of digital communications. In many applications, including the Web and medical scans, it converts information received from signals into actual machine-usable frequency data. The transform works by summing a bunch of signals and multiplying each by a special exponential factor. Although brute forcing these multiplications takes quadratic time (the time is proportional to the square of the number of signals), the “fast” protocol takes about n log n time(where n is the number of signals received), which is fast enough to use for things like the Internet.
Paper 130 claims to reduce this n log n time to ... n (log n)0.999....Specifically, the model got it down from a factor of log n to a factor of (log n)^1–10–13, a tiny improvement over the state of the art. On an objective level, this is so close to n log n that the distinction almost doesn’t matter. It does break a longstanding barrier to digital communications, however, and many researchers hope that by studying the proof techniques used, they could one day find a Faster Fourier Transform.
