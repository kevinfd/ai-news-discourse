---
id: "62aec515ca83eb71"
title: "Claude was faster and cheaper. We took the scenic route anyway"
url: "https://blog.grainulation.org/verify-then-vote"
link: "https://blog.grainulation.org/verify-then-vote"
source: "Grainulation Blog"
domain: "blog.grainulation.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-06T02:59:39Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["aid-ninja"]
language: "en"
summary: "Verify, Then Vote\nWe gave five small local models the same questions and checked their sources before picking an answer. Our first paper reports what got better, a safety test that failed and how we can rerun decisions without asking the models again.\nWhen five models disagree\nWe wanted to see how far a few small models could get running on one machine. We gave five of them the same question,…"
tags: []
orgs: ["Anthropic", "Meta", "Apple", "Mistral", "Alibaba"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1167
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50387623"
score: 12
comments: 5
community: "Hacker News"
---

# Claude was faster and cheaper. We took the scenic route anyway

Grainulation Blog · aid-ninja · 2026-11-06

Verify, Then Vote
We gave five small local models the same questions and checked their sources before picking an answer. Our first paper reports what got better, a safety test that failed and how we can rerun decisions without asking the models again.
When five models disagree
We wanted to see how far a few small models could get running on one machine. We gave five of them the same question, let them look things up and compared their answers. They often disagreed. The obvious fix is a vote, but models can share the same mistake and a vote can’t catch that.
So we tried something else: check the sources each model cited, then use a fixed rule to pick the answer. We called the paper Verify, Then Vote. We kept answering, checking and choosing as separate steps and saved the results of each, so we could go back and reuse them.
Five local models and one checker
We used Llama 3.2 3B, Mistral 7B, Gemma 2 2B, Phi-3 mini and Qwen 2.5 3B, running through Ollama on an Apple M3 Pro with 36 GB of RAM. We left it running overnight and it finished in about eight hours.
Each model wrote a search query and got back five passages: Wikipedia for general questions, research abstracts for science claims. It then gave an answer, said how confident it was and cited up to three passages. We saved everything before any answer was picked.
To check sources, we used Claude Sonnet 5.5 as a separate hosted model. It saw only one sentence stating the answer and one cited passage and said whether the passage supported the answer, contradicted it or didn’t say enough. It never saw the correct answer.
A supported answer can still be wrong
If a passage says Sydney is the capital of Australia, it supports the answer “Sydney,” even though the capital is Canberra. Our check asks whether the passage backs up the answer. It doesn’t ask whether the passage is true.
Our rule starts with the answer that got the most votes and breaks ties the same way every time. It only switches to a different answer if the checker says a cited passage supports it. Every switch keeps a record of the passage and the check behind it, so we can see why it happened.
We also proved one thing about the rule using Lean 4, software that checks mathematical proofs: if the rule ever swaps a correct answer for a wrong one, a source check must have backed the wrong answer. That tells us where to look when something goes wrong. It doesn’t prove the source was true or that the checker read it correctly.
91 fixes, 12 new mistakes and a failed test
We tuned the settings on a separate practice set, then ran the rule on 1,000 main questions. Accuracy went from 77.1% with a simple majority vote to 85.0% with our rule.
On 526 of those questions, the models gave a mix of right and wrong answers. There, the rule fixed 91 answers the vote got wrong and broke 12 the vote got right, raising accuracy from 71.5% to 86.5%. One caveat: the vote broke ties at random, while our rule always broke them the same way, so part of the gain came from how ties were handled.
Before we started, we set a limit on how many right answers the rule could break. Of 376 answers the vote got right, the rule made 12 wrong (3.2%). Allowing for chance, the true rate could be as high as 5.5%, above our 5% limit. So the original rule failed our test. We had written down the plan and analysis before collecting data, though we didn’t file them in a public registry.
We also wanted to know whether the checker was really reading the passages. So we ran it again with the cited text removed or swapped for unrelated text. Either way, 76 of the 91 fixes disappeared. The passages mattered, though Sonnet may still lean on what it already knows when the right text is in front of it.
Keep the answer if it’s already backed up
That result suggested a more careful rule: if the starting answer already has a source backing it, keep it. We wrote down that change before collecting answers from five different models on the same questions and reused existing checks wherever the answer and passage were the same.
With the new models, 547 questions had a mix of right and wrong answers. The revised rule fixed 73 and broke three, raising accuracy from 73.1% to 85.9%. Of 400 answers the vote got right, three became wrong (0.75%) and the worst-case rate was 2.2%, well under our 5% limit.
So the revised rule passed with a new set of models. Because the questions were the same and we designed the change after seeing the first results, this shows the rule carries over to other models, not that it works on new questions.
Why not just let Sonnet choose?
We tried that too. Given the same answers and passages, Sonnet picked the right one 93.9% of the time on the first group’s 526 mixed questions, compared with 86.5% for our rule. It was also cheaper: about $0.014 per question, versus $0.021 for checking sources. Neither number includes the cost of the models writing their answers.
So Sonnet is better at making the first call. Our approach helps afterward. Because every check is saved, we can see exactly why an answer was picked and try a different rule without paying for new checks. You can log a judge’s choice too, but asking it to choose again means another call.
Rerun decisions without another model call
Across all 1,100 questions, including a separate set of 100 from TruthfulQA, the models disagreed on 702. To see how much each model mattered, a Python script dropped one model at a time and handed the remaining saved answers to our Rust program to choose again. Five reruns per question came to 3,510 in total.
All of them took 23 seconds with no new model calls. The chosen answer changed 9.4% of the time, which shows how much the outcome depends on which models take part. Rerunning all 1,100 original decisions gave exactly the same output.
This works because answering, checking and choosing are kept separate. We can change how answers are chosen while the saved answers and checks stay the same. New answers or sources would need new checks.
What we want to try next
Next we need new questions, not just new rules. Because we keep every run, we can dig into a decision, change the rule and measure the effect before paying to collect more answers.
The paper, code, proofs and saved runs are on GitHub, with scripts to reproduce our results and try your own rules on the same data.
The record
Sources & methods
These links point to the paper, code and saved experiment records on GitHub.
