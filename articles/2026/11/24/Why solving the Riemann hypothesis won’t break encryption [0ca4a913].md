---
id: "0ca4a9131732a270"
title: "Why solving the Riemann hypothesis won’t break encryption"
url: "https://scientificamerican.com/article/why-solving-the-riemann-hypothesis-wont-break-encryption"
link: "https://scientificamerican.com/article/why-solving-the-riemann-hypothesis-wont-break-encryption"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T13:30:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Peter Hall"]
language: "en"
summary: "For mathematicians, it’s the breakthrough of a lifetime. For cryptographers, it’s pretty much business as usual"
tags: []
orgs: []
topics: ["health & science", "search & media"]
content_source: "fulltext"
word_count: 696
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Why solving the Riemann hypothesis won’t break encryption

Scientific American · Peter Hall · 2026-11-24

In 2005 the CBS crime drama Numb3rs built a kidnapping plot around a juicy premise: whoever proved the Riemann hypothesis could break the encryption that protects the Internet.
Last Friday brought the news that artificial intelligence had helped prove the generalized Riemann hypothesis (GRH), a broader version of that famous problem. By the weekend, that old TV episode’s premise was ripping across social media, minus the kidnapping. While mathematicians work out what the proof means for their field, everyone else wants to know what it actually means, especially for encryption.
Fortunately, the answer is—nothing much. The legend grew from a real connection. GRH does bear on primality testing, the job of figuring out whether a number is prime, which is how cryptographers find the giant primes that many encryption schemes are based on. But somewhere along the way, the story got twisted.
On supporting science journalism
Researchers have been building on GRH for decades, even as its proof stretched out of reach. “We all thought it was true anyway,” says Eric Bach, a computer scientist at the University of Wisconsin–Madison.
The Riemann hypothesis and its variants explain more about how the primes are spread out on the number line. Mathematicians have been able to make decent estimates of this distribution since at least the 19th century, and the Riemann hypothesis guarantees those estimates are never far off.
Prime numbers serve as one of the building blocks of all of number theory, but they are also very mysterious. Sometimes they arrive in close pairs, like 17 and 19; other times hundreds of numbers or more go by without one. Primes are also the raw material of cryptography, most famously the RSA cryptosystem, named after its inventors, Ron Rivest, Adi Shamir and Leonard Adleman. The scheme works because multiplying two large primes is easy, while, for now, splitting the result back into primes seems to be brutally hard.
The fear, then, is that if someone could quickly test whether a number was prime, they could quickly find one of these secret primes and factor the large number. In reality, that’s already overengineered—probablistic tests are already plenty quick and reliable enough, yet they haven’t ripped open RSA. “A random test is quite adequate and faster still,” says Carl Pomerance, a number theorist at Dartmouth College, who has spent much of his career harnessing primes and designing primality tests. Randomized tests—which can’t definitively prove a number is prime—have long been the norm for any prime-finding fun, he says, and they will likely stay that way.
The most famous of these is the Miller-Rabin primality test, named after computer scientists Gary Miller and Michael Rabin. In fact, Miller originally conceived of the test as deterministic, relying on a variant of the Riemann hypothesis; Rabin turned it into the now popular randomized form.
Bach is one of many researchers who spent decades working out what GRH would mean for other areas of math and computer science. In 1990 he showed just how efficiently GRH would let Miller’s original test determine, with absolute certainty, whether a number is prime. He says the billions of numerical checks the hypothesis had already passed helped convince him to look into its implications. “I’m guilty of that,” he admits.
Now that GRH is proved, Miller’s original deterministic test officially works—but don’t expect anyone to switch. In practice, people will keep running the randomized version a few dozen times until they feel sure enough.
The experts we spoke with were generally more excited about what GRH means beyond primality testing. For instance, Jeremy Rouse, a mathematician at Wake Forest University, notes that only through GRH can mathematicians know which numbers “could be written as a square plus a square plus seven times a square.” Good luck working that into a kidnapping plot.
These purely mathematical pursuits, not encryption cracking, are the main lessons from this result. But the actual understanding is just beginning. Over the coming years, mathematicians will have to comb through hundreds of thousands of AI-generated pages to find the techniques and ideas that made the proof work. As Bach puts it, “That is going to have more impact than just the blank, flat-out ‘It’s true.’”
