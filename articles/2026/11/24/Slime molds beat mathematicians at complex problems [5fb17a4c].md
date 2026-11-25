---
id: "5fb17a4cc6d4e443"
title: "Slime molds beat mathematicians at complex problems"
url: "https://scientificamerican.com/article/slime-molds-beat-mathematicians-at-complex-problems"
link: "https://scientificamerican.com/article/slime-molds-beat-mathematicians-at-complex-problems"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T19:00:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Manon Bischoff"]
language: "en"
summary: "Slime molds carefully spread their tendrils between morsels of food. This skill can apply to making efficient public transportation networks—a problem computer scientists say is incredibly complex"
tags: []
orgs: []
topics: ["health & science", "search & media"]
content_source: "fulltext"
word_count: 1376
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Slime molds beat mathematicians at complex problems

Scientific American · Manon Bischoff · 2026-11-24

This article is from Proof Positive, our friendly newsletter that explores the joys and peculiarities of math. Sign up today for a weekly math essay and puzzle in your email inbox.
Imagine you’ve been asked to build a new subway network for your city. The points that the network should connect at are naturally predetermined: important downtown locations need a stop, as do train stations, airports, universities and cultural institutions, such as museums and parks. At the same time, you have a limited budget. The system should therefore be as efficient as possible: every location must be accessible, while the total tunnel length should be kept to a minimum. How do you solve this challenge?
On supporting science journalism
These so-called Steiner tree problems are not easy to solve. They first arose in the early 19th century. Although named after Swiss mathematician Jakob Steiner, who did indeed work on them, they were first investigated in 1811 by French scholar Joseph Diez Gergonne. After more than 200 years, it has become clear to mathematicians that Steiner tree problems are among the most complex problems in the field. Yet there are living organisms that find this kind of optimal network planning very easy: slime molds.
The gifted urban planner Physarum polycephalum is a single-celled organism that can grow to several square meters in size. Slime molds of this species possess neither a complex nervous system nor a brain. And yet they can master astonishing tasks, some of which we mammals struggle with. They find the shortest routes within mazes, appear to possess a kind of short-term memory and can reconstruct the connections of the rail network in the Tokyo metropolitan area.
To observe the slime mold as it plans an optimal rail network, it must be lured with food—specifically, oat flakes. In 2010 researchers at Hokkaido University in Japan conducted an experiment in which the oats were arranged to represent Tokyo and 35 surrounding cities in the metropolitan area. They then placed Physarum polycephalum on the Tokyo oat flake. The slime mold grew by about one centimeter per hour. The researchers observed the single-celled organism for 26 hours as it began to spread out flat in all directions in search of oat flakes. To conserve resources in the long run and utilize the finite food supply as efficiently as possible, the slime mold then contracted again.
In the end, it spanned the various food sources with a network of gossamer-thin threads. The resulting pattern resembled the rail network of the Tokyo metropolitan area. The researchers wrote in a study that the shape of the network developed by the slime mold is similar to real-life networks in “efficiency, fault tolerance and cost,” which—it must be admitted—is remarkable for a single-celled organism.
Planning a rail network is challenging in many respects. Imagine designing a network connecting three cities arranged in an equilateral triangle. You could simply lay tracks from one city to the next, tracing the perimeter of the triangle. But an arguably better solution puts one stop at the center of the triangle and then extends three tracks from the cities to this center point.
That second design requires less track material—something you can quickly verify. If the three cities are each a distance of l from each other, the perimeter of the triangle is 3l. In the second scenario, however, the tracks run along the angle bisectors to the center of the triangle. These sections each have a length of l/√3. Therefore, the rail system in the second case would have a total length of √3l, which is only about 58 percent of the total length in the first scenario.
Allowing flexibility in the construction of stops can clearly reduce the overall length of the network connections considerably. But, of course, the more points you want to connect, the more complex the task becomes.
Just How Challenging Can It Be?
Complexity theory, a subfield of theoretical computer science, classifies problems into different categories. It uses algorithms to determine how the number of computational steps relate to the size of the task. For example, though factoring a large number into its prime factors is extremely difficult, it’s easy for computers to check whether a number is prime. The latter falls into the complexity class of problems that theoretical computer scientists denote as “P.” In simpler terms, P encompasses all those problems that remain efficiently solvable as their size increases—the number of computational steps grows with the size of the task but doesn’t explode. More precisely, the computation time grows polynomially with the size of the input.
For certain problems, however, the computation time increases exponentially. Although any computer can very quickly factor the number 15 into its prime factors 3 and 5, if you give the computer a number thousands of digits long, it may give up. This is, of course, annoying for number theorists, but a blessing for cryptographers, who use such complex problems to design encryption methods.
Certain tasks may be very complex, but their solutions—once identified—can be easily verified. These tasks are classified as “NP,” a complexity group that contains all problems whose solutions can be easily verified (that is, in polynomial time). The NP class thus contains all problems from P (because they are easy to solve, their solutions are also easy to verify) and also some problems that are difficult to compute.
The definition of complexity classes such as P and NP now stands or falls with the algorithms we know for solving certain tasks. But what if someone suddenly finds a completely new way to calculate, for example, the prime factors of a number—and the computation time only increases polynomially with the size of the number? Such questions form the core of theoretical computer science: the biggest unsolved puzzle is to find out whether P and NP are the same. In other words: For all tasks whose solutions can be easily verified, is there actually an efficient solution algorithm that we simply haven’t discovered yet?
The Steiner Problem Is Extremely Complex
To determine the complexity of a problem, the crucial idea is to reduce it to another. In other words, if every algorithm that solves task A can also solve B, then B is reducible to A. Therefore, A is more complex than B. In the early 1970s computer scientists Stephen A. Cook and Leonid Levin were able to show that there is a specific problem in NP, the so-called Boolean satisfiability problem or SAT problem, to which all other NP problems can be reduced. That conclusion would make SAT the hardest problem in NP.
Yet as it turns out, there are other problems to which all other NP problems are reducible (including SAT). These problems are called NP-complete. If P and NP were to turn out to be unequal, then NP-complete problems would certainly not be contained in P. For them, there would be no efficient solution algorithm, no matter how long you searched. In 1972 computer scientist Richard Karp identified 21 problems that are NP-complete—including a simplified version of the Steiner problem.
So bringing us back to the slime molds at work: planning a rail network is at least as difficult as an NP-complete problem. (We know this because Karp had investigated a simplified version of the Steiner tree problem.)
If you want to connect many stations, the optimal solution can require a great deal of computing power. Fortunately, there are approximation methods that bring us at least close to an optimal solution. Thanks to that, computer programs can solve Steiner tree problems that involve more than a million cities in just a few minutes. Furthermore, the problem can be simplified in practice by, for example, limiting the number of additional stations (Steiner points) to be added. After all, you wouldn’t want to build 60 additional interchange stations for a rail network that is supposed to connect 30 cities.
Still, it’s striking that a problem that takes computer scientists considerable time and power, requiring sophisticated algorithms and powerful hardware, can be resolved by Physarum polycephalum within a few hours.
This article originally appeared in Spektrum der Wissenschaft and was reproduced with permission. It was translated from the original German version with the assistance of artificial intelligence and reviewed by our editors.
