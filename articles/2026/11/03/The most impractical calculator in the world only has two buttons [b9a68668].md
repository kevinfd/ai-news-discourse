---
id: "b9a6866824ad14f7"
title: "The most impractical calculator in the world only has two buttons"
url: "https://scientificamerican.com/article/the-most-impractical-calculator-in-the-world-only-has-two-buttons"
link: "https://scientificamerican.com/article/the-most-impractical-calculator-in-the-world-only-has-two-buttons"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T18:00:00Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Manon Bischoff"]
language: "en"
summary: "Modern calculators have many buttons, including ones for sine, square root, pi and exponents. But it’s possible just two could suffice"
tags: []
orgs: []
topics: ["jobs & society", "search & media", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 1151
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# The most impractical calculator in the world only has two buttons

Scientific American · Manon Bischoff · 2026-11-03

This article is from Proof Positive, our friendly newsletter that explores the joys and peculiarities of math. Sign up today for a weekly math essay and puzzle in your email inbox.
In the past, calculating complex values such as the logarithm of a number required a great deal of time and patience, as well as the appropriate reference material. This work, though sometimes tedious, led to unexpected discoveries. For example, while leafing through tables of logarithms, astronomer Simon Newcomb noticed that the pages for values starting with the digit 1 were significantly more worn than the others. This observation ultimately led to the so-called Benford’s law, which describes how certain random numbers are distributed.
On supporting science journalism
If you're enjoying this article, consider supporting our award-winning journalism by subscribing. By purchasing a subscription you are helping to ensure the future of impactful stories about the discoveries and ideas shaping our world today.
Had calculators existed back then, Benford’s law might never have been discovered. Still, I personally am grateful that I didn’t have to wrestle with logarithm tables or other formula collections during my school years or university studies, or in my job. In fact, I wouldn’t want to be without my scientific calculator. It not only has important values such as pi or Euler’s number programmed in, but it also can calculate more complicated operations, such as the cube root or logarithm of a number, with just one press of a button.
As physicist Andrzej Odrzywołek of Jagiellonian University in Poland explains in a preprint from March 2026, however, calculators could be designed much more simply: two buttons alone are sufficient to perform the elementary calculations and functions of a scientific calculator. Whether tangent, square root, pi or exponentiation, all these functions can be encoded using only the number 1 and the operator eml(x,y) = exp(x) − ln(y). His work has since been verified by a so-called proof checker, a computer program that goes through the logical conclusions step-by-step and checks whether everything is correct.
From 36 to 2
Depending on the model, a calculator can perform tasks of varying complexity. Some models only handle the four basic arithmetic operations: addition, subtraction, multiplication and division. Others are capable of evaluating trigonometric functions, extracting roots and calculating logarithms. I had access to such a calculator during my school years, for example. But I wasn’t allowed to use graphing calculators, which can also independently solve equations and represent functions geometrically.
Odrzywołek, in his work, refers to 36 quantities and operations found on conventional scientific school calculators—including the aforementioned trigonometric functions, exponentiation, and so on. “Higher mathematics reveals that many of these [functions] are redundant: for example, trigonometric ones reduce to the complex exponential. How far can this reduction go?” he asks in his paper.
The physicist suspected that one function and one number might suffice to construct all 36 functions and quantities. “That sounds plausible,” says mathematician Manuel Kauers of Johannes Kepler University Linz in Austria, who was not involved in the current work. “The class of elementary functions is not particularly rich.”
This assumption is supported from a technical perspective, too. As early as 1913, mathematician Henry Sheffer proved that digital calculations can be performed using a single logical operator, the “NAND gate.” This discovery allowed for extremely complex computer calculations to be performed using one type of transistor.
An All-Powerful Function
To find the single function needed for his calculator, Odrzywołek first turned to the instruction set of the widely used algebraic computer program Wolfram Mathematica. This instruction set uses only seven functions to derive the elementary operations. It “served as a reference for an already-optimized [system] ... thoroughly tested for almost 40 years,” he writes.
To further reduce this set of instructions, the physicist designed a computer program to assist him in the systematic search. Given a candidate for universal operations, this program systematically explores all possibilities to express the 36 elementary functions, numbers and important constants. After many attempts, he concluded that 1 in combination with eml(x, y)—“eml” is an exponential-minus-logarithm function—could be the basis for reconstructing the elementary functions.
For example, to generate Euler’s number e, one simply needs to calculate eml(1,1) because exp(1) − ln(1) = e. To perform subtractions or calculate trigonometric functions, however, the eml operator must be nested multiple times—in other words, that eml must be plugged into an operation repeatedly. For the sine function, for example, it must be nested more than 10 times in succession, a more cumbersome task.
And other difficulties quickly arise. Even with real-world mathematics, you may need to engage with complex numbers, which involve the square roots of negative values. But the logarithm of a complex number is not uniquely defined, which is why you must choose a “branch,” or specific segment where the logarithm takes on a definite value. Therefore, Odrzywołek writes, great care must be taken when implementing the eml structure to obtain the correct results.
Furthermore, eml and 1 are not the only combinations of function and number from which elementary operations can be derived. As the physicist discovered, a fully functional scientific calculator can be designed using an exponent-divided-logarithm edl(x,y) and e. There could be other solutions as well.
EML and Machine Learning
Although I find Odrzywołek’s result quite interesting from a theoretical perspective, it seems to offer few practical applications. A calculator with just two buttons, for example, would be incredibly compact but hardly user-friendly. To generate the number 0, you would have to perform the following calculation: eml(1, eml(eml(1, 1), 1)) = eml(1, eml(e, 1)) = eml(1, ee) = e – e × ln(e) = 0. Even entering the simplest numbers therefore requires a lot of time and patience (as well as a certain aptitude for arithmetic).
Odrzywołek also suggested another application in the field of neural networks. These AI algorithms are based on elementary functions that can be represented by an eml structure. This could offer advantages: Instead of maintaining several different functional units and lookup tables for the conventional arithmetic operations of neural networks such as ReLU, tanh, GELU or sine, identical eml cells could be used, much like the NAND gates on computer chips.
Eymen Ipek, a researcher at the Graz University of Technology in Austria, tested this in a preprint posted to the server arXiv.org in April 2026. Ipek replaced part of a neural network used to calculate electric vehicle powertrains with an eml structure. But while the code architecture may appear simpler, it requires significantly more computational operations, he found. ReLU, tanh and similar functions represent only one operation, but executing an eml function requires 111 operations. Therefore, it will be a long time before an eml computer is used in practice—if ever.
This article originally appeared in Spektrum der Wissenschaft and was reproduced with permission. It was translated from the original German version with the assistance of artificial intelligence and reviewed by our editors.
