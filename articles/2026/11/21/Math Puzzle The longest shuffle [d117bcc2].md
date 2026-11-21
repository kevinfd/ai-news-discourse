---
id: "d117bcc25ccf3107"
title: "Math Puzzle: The longest shuffle"
url: "https://scientificamerican.com/article/math-puzzle-longest-shuffle"
link: "https://scientificamerican.com/article/math-puzzle-longest-shuffle"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-21T05:00:00Z"
published_date: "2026-11-21"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Jack Murtagh"]
language: "en"
summary: "Find the most laborious shuffle you can"
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 637
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Math Puzzle: The longest shuffle

Scientific American · Jack Murtagh · 2026-11-21

If you repeatedly shuffle a deck of 10 playing cards using exactly the same method, what is the largest number of shuffles you could need before the deck returns to its original order?
For example, a silly shuffle might simply involve swapping the top and bottom cards, while leaving the rest untouched. After only two applications of this shuffle, the deck is restored. What about for more complicated shuffles? Note: shuffles are based only on the cards’ positions, not the specific card. For example, you can say, “Always move the top card down four positions,” but you cannot say, “Always move the queen of spades down four positions.”
It will take a maximum of 30 shuffles before the deck returns to its original order.
Every shuffle, no matter how complicated, ultimately maps each position in the deck to another position, i.e., a shuffle is some permutation of the deck. Permutations can always be decomposed into discrete cycles. To understand this, consider the example shuffle given below, where the top card ends up in the sixth position, the second card moves to the top, etcetera.
Follow the card that starts on top. The first shuffle moves it to position six, the second moves it from position six to position nine, the third to position two and the fourth back to position one. So it travels around a cycle of four positions: one → six → nine → two → one. Notice that the cards that begin in positions two, six and nine also travel along this same cycle before returning to their original positions. Following the other cards, you’ll find that this shuffle can be decomposed into cycles of lengths four, three, two and one. Every card belongs to some cycle, and no card belongs to two different cycles. (Every position points to one other position and is pointed to from one other position. To take part in two cycles, a position would have to point to two different places or be pointed to from two different places.)
Every shuffle can be decomposed in this way. The length of a cycle represents the number of cards in that cycle, so the lengths always sum to 10. For example, the shuffle that simply takes the top card and puts it on the bottom would create one big cycle of length 10. The vacuous “shuffle” that declines to move any cards decomposes into 10 “cycles” each of length one.
A card in a cycle of length three returns to its starting position after three shuffles and then again after six, nine, 12, and so on. So the whole deck is back in order the first time that every cycle has completed a whole number of trips around. That’s the least common multiple of the cycle lengths. To make the deck take as long as possible to return, we want to split 10 into cycle lengths with the largest possible least common multiple.
Cycles whose lengths share a common factor waste cards. Cycles of four and six, for example, are both back in place after 12 shuffles, but cycles of four and three are as well, and they leave you three additional cards to play with. So the best options use lengths with no common factors. The winner is 5 + 3 + 2 = 10, which takes 5 × 3 × 2 = 30 shuffles.
Fun fact: for a full deck of 52 cards, the longest shuffle uses cycles of length four, five, seven, nine, 11 and 13, plus three cards that stay in their original positions, and it takes 180,180 shuffles to restore the deck.
On supporting science journalism
We’d love to hear from you! E-mail us at games@sciam.com to share your experience. if you can't see the puzzle answer reveal above, visit this page in a web browser.
