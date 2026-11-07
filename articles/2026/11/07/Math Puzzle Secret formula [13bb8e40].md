---
id: "13bb8e40959afae7"
title: "Math Puzzle: Secret formula"
url: "https://scientificamerican.com/article/math-puzzle-secret-formula"
link: "https://scientificamerican.com/article/math-puzzle-secret-formula"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-07T05:00:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Jack Murtagh"]
language: "en"
summary: "Can you guess the puzzle writer’s secret formula?"
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 713
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Math Puzzle: Secret formula

Scientific American · Jack Murtagh · 2026-11-07

I’m going to pick a secret polynomial with nonnegative whole number coefficients. That is, a formula that looks like “8x3 + 17x + 9” or “x225 + 99x222 + x101 + 2” or “7x234” or something similar. Note that the formula won’t contain any minus signs.
You don’t know how many terms it contains or what the exponents or coefficients are except that they’re nonnegative whole numbers. You can query my polynomial, though. Give me a nonnegative whole number value for x, and I will plug it into my formula and tell you the result. How can you fully deduce the formula using only two queries? You may base your second query off of the result of the first.
Suppose I told you that every coefficient in my formula is less than 10. If you queried x = 10, what would the output look like? Of course, you don’t know how large the coefficients in my formula are. Is there a simple way to get an upper bound on that, though?
On supporting science journalism
First query with x = 1. This will give you the sum of the coefficients, which we’ll call S. Because S is the sum of nonnegative coefficients, we know that no single coefficient exceeds S. For the second query, set x to the smallest power of 10 that is greater than S. That is, if S is a one-digit number, then the second query will be x = 10; if S is a two-digit number, then the second query will be x = 100; if S is a three-digit number, then x = 1,000, and so forth.
For example, imagine my formula is 2x5 + x3 + 3x2 + 2. When x = 1, this yields S = 8. This comes from 2 + 0 + 1 + 3 + 0 + 2 = 8, where the zeroes represent missing exponents—there’s no x4 term or x term, so the corresponding coefficients are 0. Now if we query with x = 10, the result is 201,302, coming from 200,000 + 0 + 1,000 + 300 + 0 + 2. This result just lists the six coefficients in order, so it completely reveals the formula.
Setting x = 10 can result in ambiguity if any of the coefficients are 10 or greater, however. For example, if S = 27, then the second query would be x = 100, and the result will list the coefficients in order again, only this time each coefficient will be represented by two digits of the result instead of one. For example, plugging in x = 100 to 21x5 + x3 + 3x2 + 2 gives 210001030002.
A slick alternative solution is to make the second query x = S + 1 and then write the result in base S + 1. Figuring out why this works is a bonus exercise.
Curiously, if your queries can be any number, then you can, in principle, fully determine the formula with a single query: x = π. Proving this requires more advanced math. The number π is transcendental, which, among other things, implies that if you plug it into a polynomial with whole number coefficients, it will always give a unique output. There is no ambiguity like there is for many other numbers.
The result of setting x = π also bounds the size of the coefficients and the size of the exponents in the formula. For example, if you query x = π and the result is 54.44225..., then you know that all coefficients are between 0 and 55 (otherwise the result would have been larger), and you know that the formula cannot have any exponent greater than 3 because, if it did, then it would, at minimum, contain a π4 term, which equals 97.40909.... From one query, you learn that the polynomial’s coefficients sit between 0 and 55, and its exponents sit between 0 and 3. This narrows the answer to a large yet finite list of possibilities. You could in principle check each one and find which one yields 54.44225... to determine my formula.
We’d love to hear from you! E-mail us at games@sciam.com to share your experience. if you can't see the puzzle answer reveal above, visit this page in a web browser.
