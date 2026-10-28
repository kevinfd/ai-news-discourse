---
id: "e07d12b71827697b"
title: "Understanding the Exponential Time Hypothesis, and OpenAI's claim that it is false"
url: "https://gravitypersists.github.io/explainer-eth-disproved"
link: "https://gravitypersists.github.io/explainer-eth-disproved"
source: "gravitypersists.github.io"
domain: "gravitypersists.github.io"
source_type: "community"
collector: "reddit"
date: "2026-10-27T13:21:25Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Gravity13"]
language: "en"
summary: "No. The claimed running time, roughly \\(2^{n/\\sqrt{\\log n}}\\), is still far above any polynomial, and ETH failing says nothing either way about P vs NP. The paper itself notes that its result doesn't imply subexponential algorithms for general NP problems, because the usual translations between problems can blow up the input size.\nA paper with a blunt title\nOn 26 October 2026, OpenAI made public…"
tags: ["r/singularity"]
orgs: ["OpenAI"]
topics: ["models & research", "business & funding", "health & science", "search & media"]
content_source: "fulltext"
word_count: 3819
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xgsd79/understanding_the_exponential_time_hypothesis_and/"
score: null
comments: null
community: "r/singularity"
---

# Understanding the Exponential Time Hypothesis, and OpenAI's claim that it is false

gravitypersists.github.io · Gravity13 · 2026-10-27

No. The claimed running time, roughly \(2^{n/\sqrt{\log n}}\), is still far above any polynomial, and ETH failing says nothing either way about P vs NP. The paper itself notes that its result doesn't imply subexponential algorithms for general NP problems, because the usual translations between problems can blow up the input size.
A paper with a blunt title
On 26 October 2026, OpenAI made public a manuscript called The Exponential Time Hypothesis is False. Its author line says only “OpenAI”. According to OpenAI's own repository, it was produced by an unnamed, unreleased internal model, and a version of its main theorem has been checked by Lean, a program that verifies mathematical proofs step by step. It came out alongside two other claimed results, in mathematics and physics, which this piece leaves aside.
The unusual part is who is checking it. The hypothesis in the title was proposed in 1999 by Russell Impagliazzo and Ramamohan Paturi. The two of them, together with Ryan Williams, now lead an independent working group that will examine the proof. The materials were released immediately at the group's request, and the group has reportedly said that taking part is not an endorsement. Until that review is done, this is a claim, and the rest of this page treats it as one.
To make sense of it, we'll take four questions in order:
- What is the puzzle at the centre of all this?
- What exactly is the Exponential Time Hypothesis, or ETH?
- Why did anyone care whether it was true?
- What would follow if OpenAI is right, and how sure can we be?
The puzzle: three switches, four rules
Let's start with something you can solve in your head. There are three switches, x, y and z, and each one is either T (true) or F (false). There are four rules. A rule is satisfied when at least one of its parts holds. Your goal is a setting of the switches that satisfies all four rules at once.
More · How to read NOT and OR
“x OR y OR z” is satisfied when at least one of x, y, z is T. “NOT x” holds when x is F. So “NOT x OR y” is satisfied unless x is T and y is F at the same time.
There are 2 × 2 × 2 = 8 ways to set the three switches. How many of them light all four rules?
Exactly 2: (x, y, z) = (F, F, T) and (F, T, T). The only way to be sure was to check every setting, which is what the sweep below does. That's brute force. Notice the lopsidedness: checking one setting took a glance down the rules, but finding a good one meant trying them. With 3 switches it's 8 rows; every extra switch doubles the table.
What you just solved is a satisfiability puzzle. You have some yes/no switches and a list of rules, each saying at least one of these must hold, and the question is whether some setting satisfies every rule at once. When each rule mentions at most three switches, computer scientists call the puzzle 3-SAT: SAT for satisfiability, 3 for at most three switches per rule. In their vocabulary the switches are variables, the rules are clauses, and a setting that works is a satisfying assignment.
The only sure-fire method we have met is the one the table used: try every setting. With n switches there are \(2^n\) settings, so brute force takes on the order of \(2^n\) steps. Three switches give 8 rows; thirty give about a billion.
One puzzle stands for a whole family
Notice something about what you just did. Checking a setting took a glance: go down the rules one by one. Finding a setting meant trying them. Many famous problems have that same shape: an answer is quick to check, but finding one seems to need a search. Colour the dots of a network so that no two linked dots match. Plan a route that visits every city exactly once. Computer scientists call the problems where a proposed answer is quick to check NP. Being in NP doesn't make a problem hard, since easy problems are in it too, but for its hardest members, finding an answer seems to need a search.
Those hardest members, the NP-complete problems, are tied together tightly: they can all be rewritten as one another. A 3-SAT formula can be turned into a colouring problem with the same answer, and a colouring problem into a 3-SAT formula. And for the four problems below, the rewrite from 3-SAT stays about the same size: a formula becomes a graph with about as many dots as it has switches and rules. The rewrites back into 3-SAT aren't guaranteed to stay that small.
That is why a puzzle about switches matters. The paper itself calls k-SAT “the canonical NP-complete problem”: the standard stand-in for the whole family. Because the members rewrite into one another, a genuinely fast way to solve 3-SAT, one whose work grows like a fixed power of n instead of doubling with every switch, would hand you fast ways to solve all of them. And a fast way to solve any one of them would hand you one for 3-SAT.
The doubling wall
Brute force is fine for three switches. Scroll on and watch what each step up in n does to the table. There is no log scale here: each new bar fills the panel, and the one before it is redrawn at its true size beside it.
Three switches: the puzzle you just swept. Instant: you checked every row by hand.
Twenty switches means seventeen more doublings. A laptop gets through these rows in well under a second. And look what happened to your 8 rows: beside this bar, they're too small to see.
A hundred switches, and the bar for twenty has vanished. Suppose a billion computers each checked a billion rows every second, all on this one formula. They would need tens of thousands of years.
Brute force on 100 switches already needs about \(10^{30}\) checks. Add 10 more switches. How much more work is that?
About 1,000× (\(2^{10} = 1{,}024\)). The tempting answer is 10%, because 110 is only 10% bigger than 100. But each switch doubles the table, so 10 switches double it ten times. That is what “exponential” means in practice: adding a little input multiplies the work.
Ten more switches, 1,024 times the work: tens of millions of years on the same billion computers. The input grew by a tenth; the work grew a thousandfold.
A thousand switches. No bar can hold this, so here is the number of rows written out in full. For scale, the observable universe holds only about \(10^{80}\) atoms, a number with 81 digits.
Cleverer algorithms do exist. The best known before OpenAI's claim, from the PPSZ family of randomised algorithms, takes about \(1.307^n\) steps. At a thousand switches that is a 117-digit number: far shorter, and still far beyond the atoms.
Its multiplier per switch is smaller, ×1.307 instead of ×2, but it is still a fixed multiplier. A lower wall, not a way around it.
The bet: “you can't get under the wall”
Clever algorithms have lowered the multiplier per switch, from ×2 for brute force to about ×1.307. But every one found so far still pays some fixed multiplier for each extra switch. Is that a law, or have we just not been clever enough?
In 1999, Russell Impagliazzo and Ramamohan Paturi made a precise bet, the Exponential Time Hypothesis (ETH). It says that every algorithm for 3-SAT, however clever, pays on average at least some fixed multiplier for each extra switch, on the hardest puzzles of each size. That multiplier might be tiny, ×1.001, but it never fades to ×1.
Notice the word hypothesis. Nobody has proved ETH. It is an unproven assumption, a foundation stone that researchers chose to build on.
You have probably heard of a famous cousin, P ≠ NP. Both are bets about the same unknown, because nobody knows the fastest possible algorithm for 3-SAT. Where could it sit? The figure shows four possible answers, sorted by how quickly the work grows as you add switches. Two are algorithms we have, and two are speeds nobody has found.
Higher on the ladder means the work grows faster as you add switches. We already have the top two, so the best possible algorithm is at least that good. Whether anything lower can exist is what the bets are about.
P ≠ NP bets that no algorithm solves 3-SAT in polynomial time, the kind of growth \(n^3\) stands for. So the best possible algorithm sits somewhere above the bottom rung.
ETH bets more. Below ETH's line, the multiplier per switch fades toward ×1 as n grows; computer scientists call that growth subexponential. ETH says the best algorithm stays above the line, so even \(2^{\sqrt{n}}\), which still outgrows every polynomial, is ruled out.
That is why ETH's bracket is shorter: it is the bolder bet. If ETH is true, P ≠ NP follows. The reverse doesn't hold.
More · The formal statement
ETH: there is some constant \(s > 0\) such that every algorithm that correctly solves 3-SAT needs at least \(2^{s \cdot n}\) steps on some formulas with n variables. Since \(2^{s \cdot n} = (2^s)^n\), that is an average multiplier of at least \(2^s > 1\) per variable on the hardest formulas. Equivalently, there is no \(2^{o(n)}\) algorithm for 3-SAT, where \(o(n)\) means something that grows more slowly than any fixed fraction of n. Running times of the form \(2^{o(n)}\) are the subexponential ones: their average multiplier per variable fades toward ×1.
Suppose someone proved that 3-SAT can be solved in about \(2^{\sqrt{n}}\) steps. Which assumption would be broken?
ETH only. With \(2^{\sqrt{n}}\) the multiplier per switch fades toward ×1, so it sits below ETH's line, exactly where ETH bet nothing could be. But it still grows faster than any polynomial, so it stays above the \(n^3\) rung, and P ≠ NP is untouched. That's why a broken ETH, by itself, says nothing about P vs NP. It's the trap headlines fall into.
What was built on the bet
A link, not a proof
Researchers usually can't prove outright that a problem has no fast algorithm. (If they could do that for 3-SAT, P vs NP would be settled.) What they can prove is a link.
Remember the family from chapter 2, and graph colouring in it? 3-SAT can be rewritten as colouring at about the same size. That lets a result read:
Graph colouring has no \(2^{o(n)}\) algorithm on graphs with n vertices, unless ETH fails.
The proof is the rewrite from the family figure. It turns any 3-SAT formula into a colouring problem with about as many dots as the formula has switches and rules. So a much faster colouring algorithm, one whose multiplier per dot fades toward ×1, would also be a much faster 3-SAT algorithm, and that would break ETH. As long as ETH holds, colouring is stuck paying a fixed multiplier per dot too. The same move, with other rewrites, gives lower bounds for Hamiltonian cycle, vertex cover, clique and many more problems.
A paper proves “graph colouring has no \(2^{o(n)}\) algorithm, unless ETH fails.” In your own words: what did it actually prove, and what would make the statement stop telling us anything about hardness?
It proved a link, not hardness itself: any much-faster colouring algorithm could be turned into a much-faster 3-SAT algorithm. Colouring is “hard” only as long as ETH is true. If ETH fails, the statement is still true, but it no longer shows that colouring is hard.
A bolder bet: SETH
ETH only says that 3-SAT's multiplier never fades to ×1. There is a much bolder bet, the Strong Exponential Time Hypothesis (SETH). Let the rules get wider, with 4, 5 or 10 switches each, and SETH says the best possible multiplier climbs toward ×2, getting as close to it as you like. For wide rules, brute force is essentially unbeatable.
Bolder bets buy stronger results. The most famous one built on SETH: Backurs and Indyk proved that edit distance, the measure of how different two strings are and a close relative of what diff computes, can't be computed in much less than quadratic time, unless SETH fails. Hold on to SETH and edit distance. They come back in chapter 7.
More · Why does SETH imply ETH?
ETH only says 3-SAT needs some exponential \(c^n\) with \(c > 1\), and \(c\) could be close to 1. SETH says that for wide enough clauses the base gets arbitrarily close to 2. If SETH is true, wide-clause SAT needs exponential time, and that in turn forces 3-SAT to need exponential time, which is ETH. So SETH implies ETH.
ETH and SETH are both unproven bets. Which one is riskier, that is, easier to turn out wrong?
SETH. It claims more: not just “some fixed multiplier per switch” but “for wide rules, ×2, brute force”. A bigger claim has more ways to fail. And anything that breaks ETH breaks SETH too, since SETH implies ETH. The payoff for the risk is stronger results, like the edit-distance bound. Keep this in mind for chapter 7.
The claim
Now OpenAI's claim, stated precisely. Three symbols first. n is the number of variables and m the number of clauses. \(\log n\) is the logarithm of n, which grows very slowly: going from a thousand variables to a million only doubles it. And \(o(1)\) is a small term that shrinks toward zero as n grows.
The manuscript claims a deterministic algorithm (no coin flips) that counts the satisfying assignments of any SAT formula whose clauses have a fixed width k, 3-SAT included, using only a polynomial amount of memory. Its running time is
The first factor is an ordinary polynomial, which barely matters next to the second. In plain terms the cost is roughly \(2^{n/\sqrt{\log n}}\).
Counting is at least as hard as deciding: if the count is above zero, the formula is satisfiable. And \(n/\sqrt{\log n}\) grows more slowly than any fixed fraction of n, so the 3-SAT case is a \(2^{o(n)}\) algorithm for 3-SAT. In per-switch terms, its multiplier fades toward ×1 as n grows: very slowly, but it does fade. That is exactly what ETH bet could never happen. The repository's summary puts it in one line: “The case of 3-SAT refutes the Exponential Time Hypothesis.”
More · What the paper actually proves
The theorem covers every fixed clause width \(k \ge 2\): a deterministic algorithm counts the satisfying assignments of a k-CNF formula (a k-SAT formula) with n variables and m clauses in the time above, in polynomial space. The main theorem gives \(2^{O_k(n \log\log n / \sqrt{\log n})}\) in general, improving to \(2^{O(n/\sqrt{\log n})}\) when the number of clauses is at most a constant times n. The paper states that this refutes ETH, SETH, and two related hypotheses, Gap-ETH and NSETH.
Where does that land on the ladder?
The ladder as we left it: both bets, and ETH's line.
OpenAI's claimed algorithm lands below ETH's line, where ETH bet nothing could be. Its place is by order alone: as n gets large it grows more slowly than \(1.307^n\) but faster than \(2^{\sqrt{n}}\). The ladder says nothing about which is quicker at any particular size.
The polynomial rung is still far below. A broken ETH, on its own, says nothing about P vs NP.
The claimed algorithm is subexponential, and the old best was exponential. When do you expect it to beat the old best (\(1.307^n\)) on real formulas?
Only at enormous sizes. Even with every hidden constant generously set to 1, the new bound only edges past \(1.307^n\) at around 800 variables for sparse formulas, and around \(n \approx 10^{79}\) for the general bound. By then both step counts are astronomically large, and nobody knows the real constants, which could push the crossover much further out. The exponent shrinks by only about a \(\sqrt{\log n}\) factor. Real SAT solvers also don't run worst-case algorithms; they exploit structure in real instances. The win is about the shape of the curve, not the speed. (Press coverage, e.g. Unite.AI, says turning this into practical speedups would take substantial further research.)
The growth chart appears once you've answered.
If it holds: what falls, what stands
Back to the foundation. Suppose review confirms the claim. What happens to everything that rested on ETH and SETH?
The famous result that edit distance (a close relative of what diff computes) can't be done much faster than quadratic time assumes SETH, not ETH. If OpenAI's claim holds, what happens to that result?
It loses its basis. SETH is the stronger assumption, and SETH implies ETH, so if ETH is false, SETH is false too. The paper says it refutes SETH directly. Yet the quadratic bound itself still stands. Backurs and Indyk's proof actually starts from the Orthogonal Vectors Conjecture (OVC), a weaker assumption that this claim doesn't touch, so the bound keeps a footing on OVC. The same holds for longest common subsequence and regex matching. And losing a basis would never have meant “edit distance is now fast”: no faster algorithm comes with the claim.
The diagram updates once you've answered.
The theorem blocks keep their statements; what they lose is their footing. Each link of the form “a faster algorithm here would break ETH” still holds, but with ETH gone it no longer shows that the problem is hard. One exception: for graph colouring the paper goes further and claims a subexponential colouring algorithm of its own. It can, because colouring also rewrites the other way, into a SAT formula with short rules and only a few switches per dot, so a fast SAT algorithm becomes a fast colouring algorithm. For Hamiltonian cycle, vertex cover and k-Clique it claims nothing of the kind, so they are only unproven again. A few bounds, edit distance among them, keep a footing because they also follow from OVC.
Three tempting conclusions
No. RSA and AES never rested on ETH. And “subexponential” can still mean astronomically slow: factoring, the problem behind RSA, has had a subexponential algorithm, the general number field sieve (GNFS), for decades, and properly sized RSA keys are still secure.
No. Losing the proof that a problem is hard is not the same as finding a fast algorithm for it. A bound whose condition fails is unproven, not reversed. Any faster algorithm for a particular problem still has to be found and proved on its own.
Is it true? What “verified” does and doesn't mean
“Verified in Lean” is strong evidence. It is also narrower than it sounds. Lean is a proof assistant: you state a theorem in its formal language, supply a proof, and its small trusted core, the kernel, checks every step. OpenAI's repository includes the formal statement as a challenge file and invites anyone to re-run the check with a tool called Comparator. Here is what that check does and doesn't settle.
More · The exact formal bound
The Lean theorem proves a running time of \(2^{A \cdot n (\log\log n)^2 / \sqrt{\log n}}\) times a polynomial, with polynomial memory, for the machine model defined in the challenge file. That's slightly weaker than the paper's headline bound, but it still grows more slowly than any \(c^n\), so it is still enough to refute ETH.
The gap in the right-hand column isn't hypothetical. When OpenAI announced an earlier Lean-verified result, on the Navier–Stokes equations, readers raised the concern that Lean had verified a weaker assertion than the headline (as reported by Gizmodo). No such problem has been reported for the ETH formalisation.
Lean's checker accepted the proof. Name one way the result could still turn out to be wrong, or weaker than advertised.
Lean only confirms that the formal theorem follows. Humans still have to confirm that the formal definitions (the machine model, how a formula is encoded, what “time” counts) mean what the paper says. A faithful-looking but subtly off definition could make the checked theorem say less than the headline. (Separately, the checked bound is already slightly weaker than the paper's headline bound, though still enough to refute ETH.)
ETH's own inventors are among those reviewing it, and they say their involvement isn't a certification.
What to watch for
- The working group's write-up of the proof.
- Whether experts judge the Lean definitions, the machine model and the formula encoding, to be faithful.
- Independent re-checks and re-implementations of the argument.
- Whether the paper's sharper bound, the one that wasn't formalised, holds up.
One more piece of context, about the source rather than this result: on 7 October 2026 the same repository withdrew three unrelated manuscripts after a sign error was found. That says nothing about the ETH proof. It is a reminder that these manuscripts are, in the README's words, “best understood as a form of raw research data”.
The whole story in five statements
Suppose the claim survives review. For each statement, does it follow?
aP = NP.
Doesn't follow: the claimed bound is still far above any polynomial. See The bet.
b3-SAT can be solved in \(2^{o(n)}\) time.
Follows: that's the claim itself. See The claim.
cRSA encryption is broken.
Doesn't follow: RSA never rested on ETH, and “subexponential” can still be astronomically slow. See What falls, what stands.
dMost hardness results proved “unless ETH fails” become unproven, not false.
Follows: the link still holds, but it no longer shows hardness. Graph colouring is the exception, because there the paper also claims a fast algorithm outright. See What was built on the bet and What falls, what stands.
eSETH is false too.
Follows: SETH implies ETH, so if ETH falls, SETH falls with it. See A bolder bet: SETH in chapter 5, and What falls, what stands in chapter 7.
Recap
- 3-SAT is the switches puzzle, and it stands for a whole family of problems that rewrite into one another. Brute force doubles its work with each switch.
- ETH bet that every 3-SAT algorithm pays a fixed multiplier per extra switch; SETH bet that for wide rules that multiplier is ×2. Both were always assumptions, never theorems.
- Many hardness results were built on those bets: colouring and its relatives on ETH, edit distance on SETH.
- OpenAI claims an algorithm just under the wall. If review confirms it, most ETH-based results become unproven again (for colouring, the paper also claims a fast algorithm outright) and SETH falls too, though some bounds, edit distance's among them, still stand on a weaker assumption (OVC). P vs NP and today's cryptography are untouched.
- OpenAI's math repository: the manuscript, the Lean files and the release history.
- Wikipedia, “Exponential time hypothesis”: ETH, SETH and their consequences.
