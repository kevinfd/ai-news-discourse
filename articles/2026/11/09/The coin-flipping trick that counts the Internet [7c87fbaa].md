---
id: "7c87fbaa4ad6d963"
title: "The coin-flipping trick that counts the Internet"
url: "https://scientificamerican.com/article/the-coin-flipping-trick-that-counts-the-internet"
link: "https://scientificamerican.com/article/the-coin-flipping-trick-that-counts-the-internet"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T15:15:00Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Jack Murtagh"]
language: "en"
summary: "Here’s how the ubiquitous HyperLogLog algorithm works"
tags: []
orgs: ["Google"]
topics: ["business & funding", "search & media", "health & science"]
content_source: "fulltext"
word_count: 1331
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# The coin-flipping trick that counts the Internet

Scientific American · Jack Murtagh · 2026-11-09

Let’s say I want to know how many people read one of my articles on Scientific American’s website. Counting how many times it gets opened is easy: the website can maintain a running tally and increment it by one every time anyone loads the page. That tally is a single number and requires only a tiny amount of memory to store. But page loads aren't people. Maybe you started reading over breakfast, got distracted and came back to finish it after lunch. A simple tally would count you twice. To count unique people precisely, a website has to log every reader and check each reader who loads the page against that roster. Counting total views involves a single number, while counting unique viewers seems to need a list of IDs as large as the audience. Now multiply the number of IDs opening an article by every article, every post on a social media platform (perhaps to gauge trends) or every ad on a website (to meet advertisers’ quotas), each with its own roster of potentially millions of IDs. The lists pile up into mountains of data, all to answer a simple question: “How many people saw this?”
Enter the HyperLogLog algorithm. It settles for close estimates instead of exact counts, and in exchange, it uses only a fraction of the memory required by full lists of IDs. The algorithm is worth learning about for at least two reasons. First, it’s everywhere. Google Analytics, which tracks traffic on nearly half of all websites, relies on an augmented version of it to estimate visitor metrics. If you’ve ever checked the visitor count for a personal blog, you’ve probably seen its handiwork. Beyond Google, many fields, including genomics and cybersecurity, also depend on it. Second, HyperLogLog is ridiculously elegant.
To understand the algorithm’s key idea, let’s start with a game. I’ll flip a coin repeatedly until it lands heads up, and then I’ll note how many tails came before it. That counts as one round. I repeat this for many rounds, tracking only one number: the longest streak of tails before the first appearance of heads. Now suppose I tell you that my record after an afternoon of coin flipping was 10 tails in a row. Your task is to guess how many rounds I played.
On supporting science journalism
You can make a decent guess. A streak of 10 tails turns up only about once in every 1,000 rounds. That’s because there is a 50–50 chance for an individual flip to turn up heads. The first flip is tails 1⁄2 of the time; the first two flips are both tails 1⁄4 of the time; the first three are all tails 1⁄8 of the time, and so on with the denominator doubling until 10 consecutive tails occur in one out of every 1,024 rounds. If I had played only a dozen rounds, a streak that long would be a surprising fluke. If I had played a million, I would have almost certainly seen a longer one. My record was a one-in-1,000 event, so a good guess is that it took somewhere around 1,000 rounds.
HyperLogLog plays this same game, but every round corresponds to one visitor. At a high level, imagine each visitor flips a bunch of coins, writes down the results and shows them to the site upon every visit. Just as knowing my longest run of tails allowed you to estimate the total number of rounds, the site only needs to track the longest streak of tails among all its visitors to estimate the audience size.
Say 10 people visit. Two have coin sequences of tails (T) and heads (H) that begin with TTTH, while the other eight begin with H, TH or TTH. The site just remembers the number three, the longest leading streak it has seen. That’s enough for a rough estimate: 23, or about eight visitors—not far from the true 10. If someone later shows up with a longer streak, the record goes up. And if one of the original 10 comes back, the site doesn’t need to know if they’re a repeat visitor or not: they bring the same sequence of flips, so the estimated count of visitors doesn’t change.
Notice how little the site must remember. An audience of 1,000 people most likely produces its longest streak after around 10 rounds. A million people should expect to have a record streak at around 20. After a billion, the number grows to 30. Even if every person on Earth visited, the record streak would likely appear somewhere in the low 30s. We went from having to store billions of IDs to precisely count unique visitors to only having to store a two-digit number for an estimate.
Two important questions remain: How exactly do we get every visitor to flip coins and remember them? And what if somebody gets an uncharacteristically long string of tails and skews the estimate?
First, of course visitors don’t actually flip coins; instead of tails and heads, the HyperLogLog algorithm tracks 0’s and 1’s. Here’s how it works: when you visit a website, the algorithm takes your unique ID and runs it through a hash function. Hash functions are ubiquitous in computer science. They take an input and transform it into an output that looks random despite being completely deterministic. This means that one can treat the outputs of a hash function as though they’re random numbers, but in fact, the function always yields the same output when it’s given the same input. So a hash function reads some identifier from you, such as the user name user_8675309, and converts it into a string of 1’s and 0’s, such as 01100101000100101000. These bits get treated as random coin flips, with 0 corresponding to tails and 1 to heads. The next time you visit the site using your ID, the same hash function produces the same string of bits to identify you.
Second, sometimes flukes happen. If somebody’s hash function output is the equivalent of a generational tear of flipping tails, the site will radically overestimate its audience. To guard against this kind of fluke, the algorithm splits the audience into many groups, estimates each group’s size independently, averages those estimates and combines the results.
HyperLogLog cleverly uses the first few “flips” of each person’s sequence as a group assignment. Say we want four groups. Visitors whose sequences begin with 11 go in one group, those beginning with 10 go in another, and likewise for 01 and 00. The site then sets aside those first two flips and, within each group, tracks the longest streak of tails at the start of the digits that come after. A visitor whose sequence starts with 10001, for instance, joins the 10 group with a streak of two; if that's the longest streak anyone in the 10 group has shown, the site's record for that group is simply two. Because the first two flips sort people evenly, each group should hold about a quarter of the audience, so each group’s record gives its own estimate of a quarter of the total. Average those four estimates, multiply by four, and you have an estimate of the whole audience. This way a single unlucky visitor can spoil only one of the four records, and the other three pull the average back toward reality. Real implementations use thousands of groups and a special type of averaging called the harmonic mean that lowers the statistical weight of any outliers, so one fluke barely registers. All told, HyperLogLog’s estimates are typically off by less than 1 percent. In exchange for that error, sites can count billions of unique users using roughly the amount of memory it takes to store this article.
Beyond estimating unique visitors, the algorithm helps both cybersecurity professionals detect anomalous web activity such as swarms of bots and biologists find similarities across genomes. Any time somebody wants to estimate distinct elements in an enormous dataset, HyperLogLog is likely doing the counting.
