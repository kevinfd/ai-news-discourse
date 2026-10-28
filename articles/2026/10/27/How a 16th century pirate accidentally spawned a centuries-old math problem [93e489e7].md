---
id: "93e489e70341a491"
title: "How a 16th century pirate accidentally spawned a centuries-old math problem"
url: "https://scientificamerican.com/article/how-a-16th-century-pirate-accidentally-spawned-a-centuries-old-math-problem"
link: "https://scientificamerican.com/article/how-a-16th-century-pirate-accidentally-spawned-a-centuries-old-math-problem"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T18:00:00Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Manon Bischoff"]
language: "en"
summary: "A question posed by Sir Walter Raleigh about cannonballs inadvertently led to a puzzle that mathematicians have been trying to solve for centuries"
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 1077
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How a 16th century pirate accidentally spawned a centuries-old math problem

Scientific American · Manon Bischoff · 2026-10-27

This article is from Proof Positive, our friendly newsletter that explores the joys and peculiarities of math. Sign up today for a weekly math essay and puzzle in your email inbox.
Opinions about Sir Walter Raleigh, who sailed the seas in the 16th century, vary widely. Was he a gifted navigator and explorer or a brutal pirate who terrorized the waves? According to one legend, Raleigh was gentlemanly enough to place his cloak in a mud puddle so that Queen Elizabeth I wouldn’t get her feet dirty. But less well known is that with a simple question, he profoundly influenced an area of mathematics that experts still puzzle over today.
On supporting science journalism
During his expeditions, Raleigh’s ships carried cannonballs on board for protection against enemy attacks. He wanted to quickly know how many he had at a glance, so he presented his scientific advisor, Thomas Harriot, with a seemingly simple task: calculate the number of cannonballs stacked in a pile. Harriot quickly found a convenient formula for how many were arranged in a square pyramid based on the number in the bottom row and was able to present Raleigh with a satisfactory solution.
But Harriot wondered whether that arrangement was truly the densest possible packing of spheres. What if there were an infinite number of cannonballs to consider? In 1606 Harriot wrote a letter to astronomer Johannes Kepler outlining this question. Five years later the scientist published a hypothesis that went down in history as Kepler’s conjecture. To create the densest arrangement of spheres, you start with one sphere in the middle and add six more around it to form a hexagon pattern that can be replicated across an entire plane. A second layer is then formed by nestling the spheres into the resulting spaces like eggs in a carton. The third layer corresponds to the first—and the arrangement continues. Kepler was able to calculate how much free space is created by such stacking: about 26 percent.
It’s worth noting that a finite number of spheres can be arranged much more efficiently; for instance, they can be lined up like a sausage. But Kepler’s problem revolves around an infinite number of spheres in three spatial dimensions. Other configurations Kepler investigated produced larger gaps.
In 1773 physicist and mathematician Joseph Louis Lagrange proved that in two dimensions, the hexagonal configuration is indeed the most space-efficient. It results in a density of about 90 percent, meaning there is only 10 percent empty space. And in 1831 the exceptional mathematician Carl Friedrich Gauss was able to prove that Kepler’s conjecture is correct if you assume that the spheres are arranged only in regular lattices. In this case, it is possible to distribute the first few spheres in space and arrange all the others according to the same pattern.
Gauss could not rule out the possibility of an even denser, more chaotic arrangement, however. This possibility makes the problem considerably more difficult because in this case, every sphere could be placed anywhere—and not just the first few objects. More than a century would pass before the next significant breakthrough.
Because it is impossible to test infinitely many cases, Kepler’s conjecture needed to be reduced to a problem in which only a finite number of configurations are relevant. In 1953 Hungarian mathematician László Fejes Tóth proved that this is indeed possible. The basic idea is to divide three-dimensional space into infinitely many regions and prove that the Kepler configuration is densest in all regions—because then it is also densest in all of space.
More specifically, Fejes Tóth used a kind of diagram in which he created dots representing the center of the spheres—ensuring each was the diameter of one sphere apart—and then drew boundaries halfway between each point of neighboring points to create a series of separate cells. These so-called Voronoi cells, Fejes Tóth conjectured, must be at least as large in volume as a regular rhombic dodecahedron surrounding a sphere of radius 1. (The rhombic dodecahedron is the shape produced by the most efficient sphere packing in Kepler’s conjecture.) He then considered up to 13 cells and formulated a new problem: if it could be shown that the volume of Voronoi cells is always larger than that of rhombic dodecahedra, then Kepler’s conjecture would be true.
Instead of running through an infinite number of possibilities and checking whether the corresponding packing density is always lower than that proposed by Kepler, Fejes Tóth had proposed a way to examine just a finite number of cases. Even so, the number of arrangements to be tested was enormous—beyond human capabilities alone. It wasn’t until 1992, when American geometer Thomas Callister Hales began working on the problem using a computer, that the effort moved forward. Hales, together with his student Samuel Ferguson, sought a way to work through the numerous cases to prove Kepler’s conjecture, building on Fejes Tóth’s preliminary work. They examined more than 5,000 different arrangements of spheres and showed that their density was lower than that proposed by Kepler, a task that involved approximately 100,000 problems for a computer to solve. The complete implementation took four years.
Hales finally submitted the 250-page proof and three gigabytes of computer files to the prestigious journal Annals of Mathematics in 1998. The reviewers took another four years to examine the proof and concluded that they were 99 percent certain of its correctness.
Although this confidence was sufficient for publication in the journal, Hales was still not satisfied. He worried that he might have made a mistake or overlooked a special case. So in 2003 he launched the Flyspeck project (from the acronym FPK, short for Formal Proof of Kepler) to have his calculations checked by a computer-aided proof assistant. It took 11 years to complete that project, but computers fully verified Hales’s work—and found that the proof was correct.
More than 400 years passed between Sir Raleigh’s original question and the complete solution of the problem. But mysteries remain around dense sphere packing, particularly if you consider the question in higher dimensions. As Henry Cohn, then a mathematician at Microsoft, told Scientific American in 2016: “Part of what I love about the sphere-packing problem is that every dimension has its own idiosyncrasies ... Some dimensions just behave much better than others.”
This article originally appeared in Spektrum der Wissenschaft and was reproduced with permission. It was translated from the original German version with the assistance of artificial intelligence and reviewed by our editors.
