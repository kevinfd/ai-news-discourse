---
id: "2a5cb0b7b076c5f1"
title: "This beguiling chessboard math problem is still puzzling after 120 years"
url: "https://scientificamerican.com/article/this-beguiling-chessboard-math-problem-is-still-puzzling-after-120-years"
link: "https://scientificamerican.com/article/this-beguiling-chessboard-math-problem-is-still-puzzling-after-120-years"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T11:30:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Lyndie Chiou"]
language: "en"
summary: "A recent race to conquer the “no-three-in-a-line” problem shows just how far away mathematicians are from a full solution"
tags: []
orgs: []
topics: ["models & research", "health & science", "search & media"]
content_source: "fulltext"
word_count: 1121
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# This beguiling chessboard math problem is still puzzling after 120 years

Scientific American · Lyndie Chiou · 2026-11-18

On November 7, 1906, mathematical puzzler Henry Dudeney posed a question in his column for the London Tribune: Given a chessboard, can you arrange all 16 pawns so that no three lie in a straight line? A small twist: “line” refers to any line, not just rows, columns and diagonals. Lines of every slope count.
Mathematicians broadened the problem’s scope, creating a modern-day mystery known as the “no-three-in-a-line problem”: On a square grid (in a bullet journal or on graph paper, for instance), what is the largest number of points you can pencil in so that no three of them lie on a straight line of any slope?
Since then, the puzzle has sparked debate among amateurs, computer scientists and number theorists alike. Artificial intelligence systems have also tackled it. But still it stands. At a time when AI companies regularly drop new solutions to million-dollar open problems, the fact that this small, easy-to-pose question remains unsolved makes it extremely interesting.
On supporting science journalism
If you're enjoying this article, consider supporting our award-winning journalism by subscribing. By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.
Serge Belongie, a computer scientist at the University of Copenhagen, is one of many who have toyed with the problem. “You can build a certain amount of intuition on small grids, incorporating symmetry tricks, and this gets you off to a good start,” he says. “But then some poorly understood behavior starts to emerge.”
In any grid, a row can hold at most two points. (A third would make three in a line.) An n-by-n grid has n rows, so 2n points are the most you can ever hope to place on the grid without violating the rule. The question is whether you can reach this maximum for every grid.
“The thing that makes the no-three-in-line problem hard is not the horizontal and vertical lines,” says David Eppstein, a computer scientist and mathematician at the University of California, Irvine. “We know what to do with them, but not all the lines of other slopes.”
In the 1950s famed mathematician Paul Erdős shifted the puzzle from geometry into algebra by placing his points along a parabola. A straight line can cross a parabola at most twice, so no three of the points can line up. Adapting the approach in 1975, four mathematicians published a paper containing a recipe to find 1.5n points, but the group couldn’t extend its method to 2n.
Achim Flammenkamp, a computer scientist at Bielefeld University in Germany, maintains a scoreboard devoted to tracking solutions of ever-growing grid sizes, starting with his own records in 1992.
Recently the problem has taken on a sportlike atmosphere worthy of Flammenkamp’s scoreboard. Over the past several months, two researchers have jockeyed back and forth for the highest grid size. In June computer scientist Marijn Heule of Carnegie Mellon University found a 2n solution for a grid of n = 70. Another mathematician, Thomas Prellberg of Queen Mary University of London, found an n = 74 case in July. In August Heule bested him with the n = 76 case. Finally, in October, Prellberg found the current record (as of this publication): 78.
And in July, just after the scoreboard began its spree, six mathematicians at the University of Oxford, the California Institute of Technology and the Institute of Science and Technology Austria tackled a larger version of the problem in which they investigated cases that rule out other numbers of points above a number k in a row—called “the no-(k+1)-in-a-line question”—rather than just prohibiting three in a row. The team proved that the no-(k+1)-in-a-line question has kn solutions when k is greater than or equal to 3 and the grid size n is sufficiently large. Frustratingly, their solution leaves the original question still open. In their paper, the researchers refer to the k = 2 case as the “notorious no-three-in-line problem of Dudeney.”
One of the six, Oxford mathematician Peter Keevash, said that the group’s approach involves an infinite sum that converges for cases where k is greater than or equal to 3 but blows up for the k = 2 case. He doesn’t see the failure as implying that anything unusual is going on with the k = 2 case, though. “It just means you have to either find a more clever way of using the method or you find a completely different method,” he says.
But why should that particular case be so challenging?
In 1968 two mathematicians, Richard Guy and Patrick Kelly, then both at the University of Calgary, conjectured that eventually the number of 2n solutions will run out. They showed that at high enough grid sizes, the number of possible solutions should instead tend downward to about 1.87n. (After an error in the paper was discovered, they later corrected their result to about 1.81n.)
In February 2026 Prellberg uploaded a preprint with calculations showing that a drop-off in 2n solutions might occur when a grid is around 493 by 493 dots. Prellberg calls the number a “crude heuristic” that shouldn’t be taken too seriously, but the main point is that the crossover contains such an immense number of possible lines that today’s computers are incapable of exhaustively searching for the answer.
Belongie points to the “strong law of small numbers” to explain why intuition from small to large can sometimes fail, a principle that Guy coined in 1980: “There aren’t enough small numbers to meet the many demands made of them.”
Different camps of mathematicians have sided with either the perfect 2n result for large grids or Guy and Kelly’s upper bound.
Eppstein thinks Guy and Kelly’s result lies on shaky ground. In a paper that cites a 1976 Scientific American column by mathematician Martin Gardner, he and his colleagues point out that in order for Guy and Kelly to solve their equations, they used probabilistic methods that assumed the points are completely independent of each other. In reality, he says, the points are correlated. The Guy and Kelly paper wasn’t “intended to be a rigorous argument,” he says. “These things do not behave randomly. But if they did behave randomly, this is the answer we would get.”
So far, all the grids display 2n behavior, causing Eppstein to wonder if that’s the final answer. He pauses, then says, “I don’t know.”
Keevash says, “Personally I think 2n is right because I’m optimistic.”
Belongie also tentatively sides with the 2n team. For now, he is confident that AI will resolve the problem within a year. “But I’m very curious to see if it will draw upon a brilliant flash of insight,” he says, “or soul-sucking brute-force lameness.”
