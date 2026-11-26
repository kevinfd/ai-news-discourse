---
id: "39db05bf8da7f22b"
title: "Who wrote the Book of Mormon? Testing with pre-1830 language models"
url: "https://lifehug.com/book-of-mormon"
link: "https://lifehug.com/book-of-mormon"
source: "Dave Taylor"
domain: "lifehug.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-26T05:14:43Z"
published_date: "2026-11-26"
collected_at: "2026-11-26T13:04:05Z"
authors: ["etherfuse"]
language: "en"
summary: "Who wrote the Book of Mormon? I asked the text, and here's what it said.\nI asked a computer two things. Did this book copy from other books? And whose writing does it sound like? It copied almost nothing. It sounds most like the revelations Joseph Smith dictated in the same months, and not like his everyday letters and journals. But the computer can't tell whether that's because one man wrote…"
tags: []
orgs: []
topics: ["jobs & society", "models & research"]
content_source: "fulltext"
word_count: 7936
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50651732"
score: 12
comments: 5
community: "Hacker News"
---

# Who wrote the Book of Mormon? Testing with pre-1830 language models

Dave Taylor · etherfuse · 2026-11-26

Who wrote the Book of Mormon? I asked the text, and here's what it said.
I asked a computer two things. Did this book copy from other books? And whose writing does it sound like? It copied almost nothing. It sounds most like the revelations Joseph Smith dictated in the same months, and not like his everyday letters and journals. But the computer can't tell whether that's because one man wrote both, or because both are written in the same kind of religious voice. So this doesn't settle who wrote it, for a believer or for a skeptic.
- The question
- Who wrote the Book of Mormon, and did it borrow from other books?
- What I did
- I built a library of nearly 700,000 books, pamphlets and newspaper pages printed between 1780 and 1830. I trained language models only on that text, so they had never seen the Book of Mormon or anything written about it since. I checked the book against more than 220,000 earlier books for copied wording, shared ideas and shared storylines. I compared its style with the eight people most often proposed as its author, and with 23,872 writers of that era. Every method was first checked on books whose authors are known.
- What I found
  - Borrowing: apart from the King James Bible, the book copies almost nothing. Only 0.16% of its text matches earlier books. The books most often named as sources, like The Late War and View of the Hebrews, don't stand out from other books of their kind. It doesn't follow any earlier book's outline either: the test that catches Josephus retelling Genesis in his own words finds no book whose story it follows.
  - Authorship: the closest writing is Joseph Smith's revelations, the short texts he dictated in God's voice, among the eight candidates and across the whole library. His ordinary writing, his letters and journals, doesn't stand out the same way. And writers who died long before 1829 also rank near the top, so the tools are matching a style of religious writing, not just a person.
- What it can't tell us
- The tools are good at picking the closest match from a list, and bad at telling whether the real author is on the list at all, so nobody is ruled in or out. They also can't tell a person from the style they are writing in, which is why a believer and a skeptic can both read the result as fitting their view.
In 2016 a friend and I wrote a little Java program that counted the words in the 1830 Book of Mormon and compared them with Joseph Smith's journals. It was a weekend thing. It answered nothing, and the repo sat for ten years.
This year I picked it back up, with better tools and one rule: everything is replicable. Every test, every number and every model is public, and anyone can run it again. I'm not a scientist. That is what I can offer in place of credentials.
One thing up front. I'm not arguing about whether the book is inspired. A computer can't answer that, and I won't pretend it can. What it can do is tell me whether the English text looks like a particular person's writing, whether it borrows from particular books, and how far those tools can be trusted.
- The book copies almost nothing. Set the King James Bible aside and 0.16% of it matches earlier books. The books people name as sources don't stand out from other books of their kind.
- Of the eight people usually proposed, the closest writing is Joseph Smith's revelations. Six of eight methods rank them first, including all three of my models. His letters and journals don't stand out the same way.
- Nobody can tell you the author isn't on that list, and neither can I. No test I could find can reliably say "it's none of these people". I ran the published ones built for that job, including the newest, from 2024, next to my own. Set to confirm 95% of true authors, the best of them still lets in one stranger in three. The bar was one in twenty.
- So I checked everybody: 23,872 authors. His revelations come out first in two of the three ways I ran it. In the third, one man is ahead: an English prophet whose own visions were being printed in the same years. The rest of the top is religious testimony, and too many of those writers were already dead: 9 of the top 20 in one version, where chance says 5. On books where I know the answer, this search puts the true author in its top 10 about six times in ten, and about four times in ten for a book unlike the author's other writing.
- The closest writing is a voice. As far as I can find, no tool that exists today can tell a person from the voice they are writing in. Mine can't.
1. The library
- The question
- How do you test the Book of Mormon without an AI that has already read it, and everything written about it since?
- What I did
- I catalogued 695,021 books, pamphlets and newspaper pages printed between 1780 and 1830, and trained three language models from scratch on that text alone. I set aside 168 passages of the Book of Mormon that no model saw until the final test. I also masked King James Bible wording first, so the tests weren't just measuring the Bible. The phrase "it came to pass that" alone appears 1,290 times.
- What I found
- As far as I can find, nothing on this question has come close to this size. Earlier studies compared the book with a few dozen to a couple of hundred writing samples.
- What it means
- The results aren't shaped by two centuries of commentary, and they aren't dominated by Bible phrasing.
- What it can't tell us
- The library is what I could gather, not everything ever written. And most candidates left writing only from after the book was printed.
The first problem with asking a modern AI about the Book of Mormon is that it has already read the Book of Mormon, and everything written about it since. So I built language models that have read only what was in print before 1830.
How that compares with what's been tried before
Computer studies of this question go back to 1980. Four of them compared the Book of Mormon with a few dozen to a couple of hundred writing samples from a handful of people. One, in 2013, searched about 100,000 old books for shared phrases. As far as I can find, nothing on this question has come close to this size. Switch between the two measures.
Size isn't the only difference, and it may not be the main one.
One row needs a plain warning. Every method here was allowed to say "none of these", and I measured how well each one does it. None does it well enough to trust, mine included. Section 4 has the numbers.
The eight candidates are the ones people have argued about for two centuries: Joseph Smith, Oliver Cowdery, Sidney Rigdon, Parley Pratt, W. W. Phelps, Solomon Spalding, Ethan Smith and Gilbert Hunt.
The second problem is the Bible. In the 1830 text, the phrase it came to pass that appears 1,290 times. Any method that doesn't deal with that is measuring the King James Version. So King James wording is masked out of every text before any method sees it.
2. Did it borrow?
- The question
- Did the Book of Mormon copy wording, ideas or storylines from earlier books?
- What I did
- I ran four tests against about 221,000 earlier books: copied wording, rare four-word phrases, passages with the same ideas (163 million passages compared), and the same events told in the same order. Each test was first run on books known to borrow. It caught The Late War copying War of 1812 documents, and Josephus retelling Genesis.
- What I found
  - Wording: only 0.16% of the text matches earlier books.
  - Rare phrases: The Late War and The First Book of Napoleon share enough to count. So do other books written in Bible style, and 2,044 books in the library meet the same criteria.
  - View of the Hebrews: not a hit on wording, ideas or storyline. 77 of 500 religious books are closer in ideas.
  - Storyline: no book tells the same story.
- What it means
- The book copies almost nothing. The books usually named as sources look like neighbours in the same genre, and this test can't tell a source from a neighbour.
- What it can't tell us
- Where a single, widely shared idea came from. The ideas it shares with View of the Hebrews are in hundreds of religious books of the time, so they point to no one source.
I started here because it's what the CES Letter and most online arguments are about: The Late War, View of the Hebrews, The First Book of Napoleon. I ran four tests, from the crudest to the subtlest.
Copied wording
I looked for passages the Book of Mormon shares, word for word or nearly, with any of 221,000 earlier books. I ran the same search on two other books so the number would mean something.
The Book of Mormon's 0.16% is 30 books sharing short, loose phrases, the religious talk of the day. "The Lord cannot look upon sin with the least degree of allowance" turns up in Bishop Ravenscroft. Nothing is a lifted page.
Rare shared phrases: The Late War
A 2013 study found that Gilbert Hunt's The Late War (1816), a history of the War of 1812 written in Bible style, shares rare four-word phrases with the Book of Mormon. I reran it by their own rule and got 183 phrases. Then I counted how many other books use each one.
Six are found nowhere else. Here they are in both books. Click a row in the chart above to see the other groups, and click a phrase to see it in place.
The criteria for borrowing, and what meets them
These are the criteria used to decide whether a book shares enough rare wording to count as borrowing:
- Take every four-word phrase in the Book of Mormon.
- Call a phrase rare if no more than 5 texts in the whole library use it.
- For each book, count the rare phrases it shares, per 10,000 of its own words. That way a long book can't win just by being long.
- A book meets the criteria if its score is in the top 1% of all 204,520 books. That line works out to 1.09.
The Late War scores 3.86 and The First Book of Napoleon 5.45. Both meet the criteria easily, just as the 2013 study said. What that study didn't do is check other books written the same way. There was a whole fashion, from the 1740s on, for writing about current events in mock Bible English: chronicles of kings, of London, of the American Revolution. So I ran those too.
Look at the phrases themselves. "Was their chief captain." "Captain over the armies." "And he also begat." "To wife the daughters." These are the stock moves of a story about wars and families told in Bible English. "Ruler over this people" is on the Late War list and the Napoleon list both. Anyone who sits down to write history in that style reaches for them.
So the two named books do meet the criteria. So do the other books of their kind that share enough phrases to count, eight of eight, and one of them, the Book of Jasher, which nobody has proposed as a source, clears them by more. What they share with the Book of Mormon is a genre. This test can't tell a source from a neighbour. In all, 2,044 books in the library meet the same criteria.
Same ideas, different words
You can borrow an idea without sharing a single phrase. So I cut every book in the library into 128-word passages, 163 million of them, and had a model place each one so that passages meaning the same thing land close together. Then, for every passage of the Book of Mormon, I looked for the closest passage in each book. A book that keeps turning up close gets a high score. The book named most often for this kind of borrowing is Ethan Smith's View of the Hebrews. It gets its own close-up at the end of this section.
Code: semantic/search.py · Results: data/semantic/named.json, data/semantic/named_null.json
Same story, new names
You can also borrow a plot without sharing a sentence. So a model read every book in blocks and listed what happens, with the names swapped for roles. Here it is reading Genesis 45:
A ruler cries out for everyone else to leave the room. The ruler reveals himself to his brothers and weeps so loudly that the household hears. ... The father faints, not believing them, until he sees the wagons.
No Joseph, no Pharaoh, and you still know the story. Two books tell the same story if their events line up in the same order, more than shuffling the order would give.
I checked the test first on three old retellings of the Bible. Here is the clearest: Josephus, who retold Genesis through Judges in his own words around the year 94.
Then I ran it on the Book of Mormon against the library. The longest match with any book was 9 events in order, and shuffled order does that well about one time in four. One book did beat the odds: a history of King Philip's War lined up 6 events at about 1 chance in 125. I tested 49 books of that kind, though, and with 49 tries one result like that turns up about a third of the time. So no book shares its plot.
Code: semantic/skeleton.py · Results: data/semantic/skeleton/bom.json, data/semantic/skeleton/top.json
View of the Hebrews, up close
Ethan Smith was a minister in Poultney, Vermont. His 1823 book argued that the American Indians descend from the lost tribes of Israel. The Book of Mormon says something close: its peoples are a branch of Israel brought to America, and their descendants are still here. That overlap is real, and it is why this is the book people name most often as a source.
"Did it borrow from this book" is really three questions. I'll take them one at a time, and say what would have counted as a hit before giving the result.
Code: reuse/rare.py, semantic/search.py, semantic/skeleton.py · Results: data/reuse/bom/rare.json, data/semantic/named_null.json, data/semantic/skeleton/bom.json
The middle row needs unpacking, because "first of 49" sounds like a hit.
That is the catch. The Book of Mormon is a religious book, and so is View of the Hebrews. Next to travel writing, any sermon would look close. So the fair comparison is with other religious books of the same length.
Now the two books side by side. Nothing here is hand-picked: "where they meet" is the five closest passages and the five closest events, by the same scores as above, and "where they don't" is the five with the weakest match on each side.
Where they meet, they meet on the Bible. Both books talk about Israel scattered and gathered home, both read Isaiah as speaking to a people far across the water, and both say the people of this continent were cut off for a long time. Where they don't: Ethan Smith spends pages describing old Jerusalem and quoting travellers on Indian customs, and the Book of Mormon has lawyers, secret bands of robbers and a record handed down on plates, with nothing like them in his book.
And the story. The model found 160 events in View of the Hebrews and 1,421 in the Book of Mormon. 93 of his 160 have a look-alike somewhere in the Book of Mormon. Here is where they fall.
One thing makes this test less than a fair fight, and I should say it. View of the Hebrews is mostly an argument, not a story. Its longest stretch of narrative is the Roman siege of Jerusalem in its first chapter, which is where many of its events come from. So "3 events in order" partly means there isn't much story in it to copy.
What I can say: by the test that finds Josephus retelling Genesis, these two books do not tell the same story. They share no unusual wording, and the ideas they share are ones that hundreds of religious books of the time also share. What I can't say is where the idea itself came from. It was in the air: Ethan Smith himself quotes a dozen earlier writers who made the same case, so sharing it points to no one book.
3. The earlier studies, re-run
- The question
- Do the earlier computer studies, from 1980 to 2013, hold up?
- What I did
- I rebuilt five of them, each with its own method, and one on the data its authors published.
- What I found
  - The 2008 study put Sidney Rigdon first or second for 169 chapters. With other genuine Rigdon writing it's 92, and Parley Pratt goes from 42 to 137.
  - The 2011 study's "none of these" was wrong 80% of the time with 1,000-word samples and 0% with 10,000-word samples.
  - The narrators can be told apart 74% of the time, against 28% by chance. Real authors are told apart 96% of the time.
- What it means
- Two earlier headline results depend on which samples were used. The narrators sound different, but not as different as separate people.
- What it can't tell us
- Whether the narrators differ because of who is speaking or because of when each part was dictated. Sorting by early or late dictation works about as well.
Computer studies of this question go back to 1980, and they disagree. Before running anything of my own I rebuilt five of them, each with its own method, and one on the data its authors published. Here they are side by side.
Code: eval/replicate.py · Results: data/benchmark/replication, paper/replication-report.md
Every one reproduces: run their method their way and you get roughly their answer. Two of the answers then turn on a choice nobody tested.
The 2008 study follows whichever texts stand for each man. On their own data, Rigdon is first or second choice for 169 chapters. Their Rigdon sample is mostly a book of his revelations written in 1864, thirty years after the Book of Mormon was printed. Swap in other genuine Rigdon writing, print he signed, and it's 92. Do the same for Parley Pratt and his count goes from 42 to 137. The Book of Mormon didn't change. The samples did. A method that must name someone names whoever's samples sit nearest.
The 2011 study's "none of these" follows the sample length. I gave its method a test where "none" is always the right answer. With 1,000-word samples it was wrong 80% of the time. With 10,000-word samples it was wrong 0% of the time. Same method, same people, different answer.
One author or many?
The first of those studies, in 1980, made a different kind of claim: the book's speakers differ from each other so much that one person couldn't have written them all. That finding reproduces. The 17 speakers do differ.
But "differ" needs a yardstick. I took a classifier that tells real authors apart 96% of the time and asked it to sort the book's passages by narrator: Nephi, Jacob, Mormon, Moroni. It got 74% right, against 28% by chance. So the narrators are different. They are not as different as real people are from each other, and that is not enough to call them separate authors.
There's a catch I can't get around. The narrators' books were dictated at different times, and sorting passages by "dictated early or late" works about as well: 76% against 50% by chance. I can't pull apart who is speaking from when it was dictated.
Code: eval/replicate.py, eval/scribes.py · Results: data/benchmark/scribes.json
That's why the next section exists. Two of these methods come back in it as contestants: the 2011 study's classifier is the one called ENSC, and the word-count method the 2008 study also used is Burrows' Delta. There they take the same exam as my own models, on books where the answer is known.
Code: eval/replicate.py · Results: data/benchmark/replication, docs/prior-studies.md
4. Are my tools any good?
- The question
- How far can these tools be trusted?
- What I did
- I gave every method, mine and the older ones, the same exam on books whose authors are known. Two jobs: pick the closest author from a list, and say whether the real author is on the list at all.
- What I found
  - Picking from a list: my models get 91–94% right on authors nobody had looked at. The older methods get 76–78%.
  - Saying "none of these": every method fails. Set to confirm 95% of true authors, the best still lets in one stranger in three. The bar was one in twenty.
- What it means
- These tools can tell you who on a list is closest. Every result after this section is that kind of answer.
- What it can't tell us
- Whether the real author is on the list at all. A test that must name someone will always name someone.
Before any method touched the Book of Mormon, it had to pass an exam on books where I know the author. Every method takes the same exam: mine, and the four older ones people have used: Burrows' Delta and Cosine Delta, which compare how often each writer uses the most common words; General Imposters, which was built to answer "is it this person or nobody here"; and ENSC, the classifier from the 2011 study in section 3.
My method works like this. For each candidate, take a copy of the period model and let it read that person's writing. Then show it a mystery passage. The score is how much better the copy predicts the passage than the untouched model does. Whoever's copy improves the most is the pick.
Does training on period text matter?
Same test, same settings, only the base model swapped. A false match is the model saying "yes, that's my author" about someone it never read.
Picking the right author from a list
On 55 authors and over a thousand passages, my models beat every older method, at every size. I count by author, because twenty passages from one writer tend to go right or wrong together.
Ranges are across the three model sizes. The part I like best: 32 of those authors were added after the rule was written, and nobody had looked at them. On their 640 passages my models get 91–94% right. The older methods get 76–78%.
Code: eval/clustered.py · Results: data/benchmark/clustered.json
The problem of "nobody"
Picking the closest of a list is one question. Here is a harder one: is the author on the list at all? Every earlier study had to face it, because nobody knows that the true author of the Book of Mormon is among the people proposed. A method that can only rank will always hand you somebody.
So a method needs a way to say "none of these". The usual way is a threshold: call it a match only if the best candidate scores above a line. A fair bar: put the line where 95% of true authors clear it, and then no more than 5% of strangers should clear it too.
This is where every method fails, mine too. On the exam above, held to that line, my models let in 51–57% of strangers. Turn it round and let in only 5% of strangers, and they confirm just 38–61% of true authors. The two older methods built for this exact job, General Imposters and the 2011 study's classifier, let in 78% or more. I tried the standard fix from voice-ID research. Tested properly, on authors it had never seen, it didn't work.
Code: eval/clustered.py, eval/open_set.py · Results: data/benchmark/clustered.json, data/benchmark/open_set.json
That left a fair question. Maybe it's just me. Does a tool exist, anywhere, that can do this? I went looking, and then I ran what I found. The newest published method I could find is from 2024 and is called LambdaG. It asks whether a text's sentences are more likely under a model of this person's grammar than under a model of everybody else's. I ran it with its authors' own software. I also ran three ready-made style models trained on modern writing, my fingerprint model from section 7, and my own author models. One of the three, LUAR, is the design my fingerprint model is built on, trained on Reddit instead of on books printed before 1830. Same 200 books for all of them, each book paired with its true author and ten other people.
LambdaG is a real method. It beat my author models on this job. It did not solve the problem, and neither did anything else. LUAR is worth a second look: same design as my fingerprint model, different training text, and it lets in more than twice as many strangers. On 1820s writing, what the model was trained on matters more than how it was built.
Two things make it worse than the chart shows. The first is the size of the list. A line that lets in one stranger in three is being asked, for the Book of Mormon, about thousands of people at once. When I put 999 strangers on the list, at least one of them cleared the line for every single one of the 200 books. To say "nobody here" about a whole library you'd need a method that almost never lets a stranger in, and nothing is close.
The second is the kind of writing. People who study this for a living don't agree on whether you can separate a person's habits from the habits of a style at all. One researcher argues these methods work because people write in slightly different styles. The standard advice is to compare only texts of the same kind. For a book written as scripture by someone who left no other scripture, that advice can't be followed.
So these tools are good at "which of these people" and bad at "is it any of these people". As far as I can find, that isn't a weakness of my tools. It's where the whole field is. Everything below is the first kind of answer.
The biblical costume
One more weakness. I found three 18th-century writers who wrote both ordinary prose and imitation scripture. Trained on their ordinary prose, plain word counts named the right author on 13 of 18 scripture passages. My 297M model got 7 of 17. Three writers is too few to judge either way, and I looked hard for more: across the whole library only about ten people wrote imitation scripture, and three left enough other prose. But it's a warning, because the Book of Mormon wears that costume.
Code: eval/imitation.py · Results: data/benchmark/imitation.json
5. Joseph Smith, up close
- The question
- Of the eight candidates, whose writing is closest to the Book of Mormon, and does it matter which of Joseph Smith's writing you use?
- What I did
- I kept his revelations, short texts dictated in God's voice, apart from his letters and journals. Seven revelations survive from the same months as the book. I scored all 168 sealed passages against every candidate with eight methods, then made four attempts to knock the result down.
- What I found
  - Six of eight methods rank his 1828–29 revelations first, including all three of my models.
  - His letters and journals don't stand out the same way.
  - At the largest model size, writers who were dead before 1827 do as well.
  - Misheard-word slips are about nine times as common in the original manuscript as in the printer's copy. The book was dictated aloud.
- What it means
- Among the candidates, his revelation voice is the nearest match.
- What it can't tell us
- Whether that's the same man or the same kind of text. The revelation sample is also small, a couple of pages.
First, what the revelations are
Joseph Smith left two very different kinds of writing. One is ordinary: letters, a journal, a short history of his life. The other is what he called revelations. These are short texts, dictated aloud to a scribe, in which the speaker is God. They were later gathered into the Doctrine and Covenants, which Latter-day Saints hold as scripture alongside the Bible and the Book of Mormon.
Seven of them survive from before the Book of Mormon was printed, 2,844 words in all. They were dictated in the same months as the book, to some of the same scribes. Another 95 followed between 1830 and 1834.
Here's why I keep the two kinds apart. Latter-day Saints believe the revelations came from God, and that the Book of Mormon was translated by that same gift and power. In that way of thinking, neither one is Joseph Smith's own composition, and the interesting comparison isn't the book against his letters. It's the book against the other texts said to come the same way. Someone who thinks he wrote both would want the same comparison, for a different reason: it's the nearest thing to his voice when he's writing scripture.
So every test below treats his revelations and his ordinary writing as separate samples, and I show the ranking both with the revelations and without them. I'm not saying which way of thinking is right. I'm making sure the test can speak to both.
The ranking
Here's the ranking itself. Each of the 168 sealed passages was scored against every candidate sample, by eight methods: my three models, two style encoders, and three older word-count methods. Some candidates have more than one sample, because a man's letters and his dictated revelations aren't the same kind of writing. Joseph Smith has four. Pick a method and see the list.
Six of the eight methods put the 1828–29 revelations first. Burrows' Delta puts his ordinary prose first and the revelations near the bottom. General Imposters puts Parley Pratt first and the revelations second. All three of my models, the ones that did best on the exam in section 4, are among the six.
The revelation sample is small: 3,039 tokens, a couple of pages. So I spent most of the remaining time trying to knock the result down. Pick a model size and see how each attempt went.
At the two smaller sizes the result survived everything I threw at it. At the largest size, writers who could not have been the author do as well, which means at that size the model is following the biblical style at least as much as the person. No size has earned more trust than the others on known answers, so I report it as a split.
Without the revelations
Take the revelations away and ask about his ordinary writing, the letters and journals. Now it depends on who you ask. The two word-count methods put his prose first. My language models put it mid-pack, with Cowdery, Phelps or his own letters first depending on size. The other methods name Cowdery or Pratt. There's no agreement.
Two readings
His revelation voice, from 1828 through 1834, is the nearest writing I have to the Book of Mormon. That fits "the same man". It also fits "the same kind of text": a revelation and a scripture are both dictated in a sacred voice, and his later revelations could echo the book. These tools can't separate the two, and I'm not going to pick for you.
One thing the manuscripts do show. The original manuscript was taken down as Joseph Smith spoke, and the printer's manuscript is a copy of it. If the original was written by ear, it should be full of misheard words like there for their. It is: with the same scribe on both, those slips are about nine times as common in the original (30 of 590 against 5 of 837). The book was dictated aloud.
Code: manuscript/corrections.py · Results: data/manuscript/summary.json, data/manuscript/handcheck.json, docs/manuscript-evidence.md
6. Does that rule the others out?
- The question
- If the other candidates rank lower, are they ruled out?
- What I did
- I checked whether each candidate's model could recognise that same person in a different work of their own.
- What I found
- Only Ethan Smith's model passed. Rigdon's and Phelps's models didn't recognise a single passage of their own author's other writing. Spalding and Hunt left one work each, so they can't be checked this way.
- What it means
- Ethan Smith's low rank is real evidence that the book doesn't read like him. For Cowdery, Rigdon, Phelps and Pratt the right word is "not shown", not "ruled out".
- What it can't tell us
- Anything about Spalding or Hunt, or about the four whose models failed.
Section 5 said Joseph Smith's revelations are the closest of the candidate samples. It is tempting to read the other half of that: Cowdery, Rigdon, Pratt, Phelps and Ethan Smith rank lower, so they're ruled out. This section is here to say that doesn't follow, and to show why.
A low rank only means something if the model really learned the person. So I tested that. Each candidate's model was trained on some of his writing. Then I showed it a different work by the same man, mixed in with other people's, and asked: do you recognise your own author?
Only Ethan Smith passes. His model knows him in any of his books, so his low rank against the Book of Mormon is real evidence: it doesn't read like him.
For the other four the models failed. Rigdon's and Phelps's models didn't recognise a single passage of their own author's other writing. Those models learned one book, and they couldn't spot the man who wrote it anywhere else. So when they don't light up for the Book of Mormon either, that tells me nothing. For Cowdery, Rigdon, Phelps and Pratt the right word is "not shown". I can't write "ruled out". Spalding and Hunt left one work each, so they can't be checked this way at all.
This is the same weakness that turns up again in section 7: these models are good at recognising more of a text they've seen, and much worse at recognising the same writer in a different book.
7. The whole library
- The question
- Does anyone from that era write more like the Book of Mormon than the eight usual candidates?
- What I did
- I compared the book with all 23,872 authors in the library who left at least 10,000 words. Writers already dead when the book was written stayed in the ranking as a check: if they rank near the top, the search is matching a style, not a person.
- What I found
- Joseph Smith's revelations come out first in two of the three versions, and second in the third, behind John Wroe, an English prophet. After them come visionaries and Quaker ministers. In one version 9 of the top 20 were already dead, where chance says 5.
- What it means
- The closest writing is a voice of revelation, not one person. A believer would say the book and the revelations came from the same source. A skeptic would say Joseph Smith wrote both. Both predict this result.
- What it can't tell us
- Whether the match comes from the man or the style. For a book unlike its author's other writing, this search puts the true author in the top 10 only about four times in ten.
The candidate test in section 5 has a limit built into it. It can only compare the people somebody thought to propose. It tells me which of eight is closest. It can't tell me whether anyone else is closer.
So the question I really want answered is wider. Out of everyone who left writing in the library, all 23,872 authors with at least 10,000 words, does anyone write more like the Book of Mormon than those eight? That is the library search.
Two things about what it can and can't be. It is still a "who is closest" test. It can't say the author is on the list, or isn't; nothing can, as section 4 showed. What I can add is a measured number: when the true author of a book is in this library, this search puts him near the top X% of the time. And I put the eight candidates in the same ranking as everyone else, to see whether anybody in the library rates closer than what the candidate test found.
My first try at this wasn't good enough. It compared the book with all 23,872 authors using a word-count method and an earlier fingerprint model, and nobody stood out. But on 200 books where I know the author, it put the true author first only 27–35% of the time. My bar was 70%. A search that weak can say "nobody jumped out". It can't say much else. So I rebuilt it.
Code: sweep/calibrate.py, sweep/older.py · Results: data/sweep/calibration.json, data/sweep/older_methods.json
The plan, and how it broke
The plan was two steps. A fast search narrows 23,872 authors to a shortlist. Then my per-author models, the ones that won the exam in section 4, pick from the shortlist. The first thing I needed to know was how long that shortlist could be.
That looked good enough to build on. But those 55 authors had all their writing in the model, and the test passages came from the same books. The real job is harder: a different book, and every author given the same small amount of text so nobody wins by having more. So before spending money on the real run I tested the plan on that harder job. I took 1,000 library authors, 200 of them with a book held back, and trained about 4,000 small models.
The fingerprint model, the one I'd meant to use only for narrowing, found the true author far more often than my best method from the candidate test. So I used the tool that did better. The fingerprint model does the ranking, and the author models became a second opinion on its top 200.
I also considered running the two bigger author models here, for completeness. I didn't. Bigger had not helped in the list test above, and the author models were no longer the ones doing the ranking, so a bigger version of them wouldn't change the result. What would make the result stronger was more known books to test the search on, and cleaner names in its lists. So I did those.
The search, and how far to trust it
The fingerprint model reads a writer's text in short stretches and turns each into a point, so that stretches by the same person land near each other. My first one had a flaw I only found by reading its training log: it had memorised its 7,673 training authors. Its error on them fell to almost nothing while its score on new authors never moved. I retrained it with eight times the text and with pairs chosen to be hard: the same author in two different kinds of writing. Then I scored each author by their closest stretch of text, not their average.
Here is what it can do, on 727 books it has never seen by authors it never trained on. The search runs over the 18,288 authors not known to have been dead.
Code: style_embed/v2.py, sweep/episodes.py, sweep/coverage.py · Results: data/sweep/coverage_episodes_v2.json, data/sweep/coverage_episodes_v2_11.json, data/sweep/coverage_episodes_v2_2.json
The last row is the one that matters for the Book of Mormon, because nobody's other writing looks like it. So read everything below with that row in mind: about four times in ten, the true author of a book like this would be in the top 10, and about one time in four he wouldn't even be in the top 1,000. I first measured this on 200 books and got rosier numbers (66% and 52% in the top 10). More books brought them down, which is why I ran more.
One more check, because the top of the Book of Mormon's list turns out to be religious writing. Does the search do worse on that kind of writer? No. On sermon and devotional books it does about as well as on everything else, and for the 38 known authors who themselves sit among the 1,000 closest to the Book of Mormon, the true author is in the top 10 for 66%. That is a small group, so I hold it loosely.
Who could have written it
A man who died in 1790 did not write a book dictated in 1829. The library catalog gives life dates for some authors, and I looked the rest up in the Library of Congress name file. That found fewer than I'd hoped: 6,016 authors were alive and at least 15 in 1829, 5,584 were dead or too young, and for 12,275 nobody recorded dates. Where the lookup did give a date I could check, it agreed with the catalog 212 times out of 219.
I did not throw the dead away. I kept them in the ranking as decoys. If dead men come out on top, the search is following a way of writing and not a person.
Code: sweep/people.py · Results: data/sweep/people.json
The result
Here is the Book of Mormon against the whole library, with the eight candidates' samples placed where they'd fall. There are three versions, because sample size matters: a writer with 20,000 words has an edge over one with two pages. The small version gives everyone the same amount as Joseph Smith's 1828–29 revelations, which is the only way that sample can compete fairly.
Almost nobody in the library rates closer than Joseph Smith's revelations. In the small version his 1828–29 revelations are first of 23,872. His 1830–34 revelations are first, second and first across the three versions. The one time they are second, the man ahead of them is John Wroe. His ordinary prose is around 19th to 30th, which is high but not at the top. Ethan Smith and Solomon Spalding are hundreds or thousands of places down.
Now look at who the library puts at the top. First in two of the three versions is John Wroe, an English prophet whose visions were in print from 1820 and who founded his own church in 1822. After him come Quaker ministers' journals and letters: William Savery, Elizabeth Stirredge, Elias Hicks, James Backhouse. And David Willson, who led the Children of Peace, a group that broke from the Quakers in Upper Canada. These are people writing down what they believe God told them, in the first person, in Bible English.
The decoys
So the top of this list is a kind of writing. It is not a list of people who could have written the book. That is the decoys doing their job, and it is the same thing the 590M model told me in section 5, when a man born in 1844 scored as well as the revelations.
A second opinion
I still ran my author models, the method from the candidate test, on the fingerprint model's top 200 library authors plus the candidates: about 830 small models, each given the same amount of text. It agrees at the head of the list. Joseph Smith's 1830–34 revelations come first at both amounts, and are the closest sample on 123 to 150 of the 168 passages. His 1828–29 revelations are 4th of 212. Behind them: Wroe, Willson, Joanna Southcott (an English prophetess who died in 1814), John Reeve (who died in 1658). Further down the two methods disagree, and I trust this one less here, for the reason in the chart above.
Code: eval/library_pool.py, eval/library_bom.py · Results: data/sweep/bom_second_opinion_pilot.json
What this says, and what it doesn't
I searched every author in the library. Joseph Smith's revelations come out first in two of three versions and second in the third, behind one other man who wrote revelations. The nearest library writers after that are other people writing revelation and religious testimony, many of them long dead.
That is the candidate test's finding again, on a list three thousand times longer. The closest writing I can find anywhere is the revelation voice: his, and other people's. What I can't do is tell the man from the kind of writing. A believer and a sceptic can both read this result and find it unsurprising, for opposite reasons, and nothing in my tools separates them.
8. Check it yourself
- The question
- Can someone else check this work?
- What I did
- I made everything public: the code, the result tables, the plan and every change to it, and the models on Hugging Face.
- What I found
- With the candidate models anyone can rerun the Book of Mormon result without training anything. Rebuilding every other model costs about $50 to $100 of rented computing.
- What it means
- You don't have to trust me. Every number can be checked.
- What it can't tell us
- Four sources I'm not allowed to republish, though the repository gives the steps to get the same access. I did this as one person working with AI, and the reviews in the repository are simulated by an AI model and labelled that way.
Under each chart and result above there's a line linking to the code that ran it and the file of numbers it produced. The whole thing lives at github.com/lifehug/book-of-mormon-authorship. The run guide lists every command, what it needs and how long it takes, and the plan has every rule and every change to it, dated.
Everything is public: the code, the result tables, the plan and every change to it, and the models on Hugging Face. With the candidate models you can rerun the Book of Mormon result without training anything. Four sources I'm not allowed to republish (HathiTrust, Harvard's book collection, the Joseph Smith Papers transcripts, and one purchased book), and for each the repo gives the steps to get the same access I had.
The models are on Hugging Face, free to download:
- timelocked-1830-125m, timelocked-1830-300m and timelocked-1830-590m: the three base models, trained only on text printed before 1830. From these you can rebuild every other model here for about $50 to $100 of rented computing.
- bom-authorship-candidate-models: one model per candidate sample, at all three sizes. These are the ones that produced the ranking in section 5.
- bom-authorship-style-encoder: the fingerprint model. The file in its v2 folder is the one that searched the whole library in section 7.
I did this as one person working with AI, and I want that to be plain. The reviews mentioned in the repo are simulated by an AI model and labelled that way. If you find a mistake, I'd like to know.
