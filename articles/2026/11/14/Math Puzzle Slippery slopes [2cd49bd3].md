---
id: "2cd49bd322598cc7"
title: "Math Puzzle: Slippery slopes"
url: "https://scientificamerican.com/article/math-puzzle-slippery-slopes"
link: "https://scientificamerican.com/article/math-puzzle-slippery-slopes"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-14T05:00:00Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Emma R Hasson"]
language: "en"
summary: "Slide down the slippery slopes of this math puzzle"
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 487
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Math Puzzle: Slippery slopes

Scientific American · Emma R Hasson · 2026-11-14

If five points are placed as shown here and straight lines are drawn between each pair of points, each line will have a unique slope. Almost all configurations of five points have this property.
Suppose you are allowed to intentionally place the five points anywhere as long as no three points can be contained in the same straight line. What is the smallest possible number of slopes that can be made by connecting pairs of points? How can you be sure?
On supporting science journalism
Challenge: What is the smallest possible number of slopes determined by any number of points? Can you prove it?
Answer:
Three lines that form a triangle will always have three different slopes: if two of the lines were parallel (and thus had the same slope), they would not be able to meet up at a corner. This means the minimum number of slopes among three points that are not in a straight line is three.
Consider any configuration of five points in which no three points are in a line. Find the bottommost point and sweep out a line from it, recording the angles at which it hits the other points. If any two points share the same angle, they are both in a line with the lowest point, which means our arrangement of five points is invalid. Because that’s not allowed, we must have four unique slopes. Now draw a line from the first point you hit to the last. This line forms triangles with all the other lines and thus must give us a fifth slope—so the number of slopes is at least five. But is there a configuration with only five?
Yes!
Consider the configuration where the five points form a regular pentagon:
The pairs of points form lines tracing the sides of the pentagon and all of the diagonals contained within it. Each of the sides has a unique slope. Each of the diagonals is parallel to, and thus has the same slope as, one of the sides. This gives us five slopes in total.
Challenge solution:
The answer for n points is n slopes, and in each case, the configuration that realizes this is a regular polygon. By the argument above, there must be at least n slopes among the n points. In an odd-sided polygon, each internal diagonal is parallel to a side, as demonstrated above. In the even-sided case, it becomes a bit more complicated. Sides come in parallel pairs, giving n⁄2 unique slopes from the polygon’s sides, and every internal diagonal is either parallel to a side or parallel to another diagonal that skips one point along the edge. There are n⁄2 unique slopes from the internal diagonals, which gives n slopes in total.
We’d love to hear from you! E-mail us at games@sciam.com to share your experience. if you can't see the puzzle answer reveal above, visit this page in a web browser.
