---
id: "658768f772c72895"
title: "Weight-space programming: an LLM edited another model's weights directly and lifted its math score from 7.9% to 48.1%"
url: "https://reddit.com/r/artificial/comments/1xx4kit/weightspace_programming_an_llm_edited_another"
link: "https://reddit.com/r/artificial/comments/1xx4kit/weightspace_programming_an_llm_edited_another"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T19:37:03Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["winer666"]
language: "en"
summary: "MIT researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab) had OpenAI's GPT-6 Astra edit the weights of a small Qwen model directly -- no gradient descent, no training data. Astra found the pattern behind the model's habit of repeating itself until it ran out of context, and removed it. The edit touched about 0.016% of the weights; the model's math score went from 7.9% to 48.1%.…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Alibaba"]
topics: ["models & research", "business & funding"]
content_source: "post"
word_count: 306
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xx4kit/weightspace_programming_an_llm_edited_another/"
score: null
comments: null
community: "r/artificial"
---

# Weight-space programming: an LLM edited another model's weights directly and lifted its math score from 7.9% to 48.1%

Reddit · winer666 · 2026-11-15

MIT researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab) had OpenAI's GPT-6 Astra edit the weights of a small Qwen model directly -- no gradient descent, no training data. Astra found the pattern behind the model's habit of repeating itself until it ran out of context, and removed it. The edit touched about 0.016% of the weights; the model's math score went from 7.9% to 48.1%. Three papers on the method landed on arXiv on November 6 (e.g. arXiv:2611.09382). Other demonstrations from the same batch: editing only 1,023 parameters improved an LLM by 29.45 points on MATH-500; Astra debugged robot policies by editing 65 token-embedding rows; and a Breakout-playing network built from the game's rules, with no training at all, outscored one trained for 500 million steps (517.4 vs 25.3). Some important caveats: the gain came mostly from fixing a bad habit, not from adding math knowledge -- before the edit 93% of the model's math answers hit the length limit, after it 33.1%. On a small Gemma model that rarely repeated itself, there was no established math gain. The original claim also drew a detailed rebuttal (Matthew Honnibal argued it was overstated), though Simon Willison then reproduced weight editing locally with Qwen 3.8 27B on his laptop. Independent reproduction of the headline results is still pending. What interests me most is the framing: this is model repair by direct surgery rather than training. If it generalizes, debugging a model could start to look like debugging code -- find the weights responsible, patch them, verify. But it also raises the question of how much of a model's capability is locked up behind fixable quirks rather than missing knowledge. Where do you think this goes? A practical tool for model maintenance, a narrow trick that only works on pathological repetition, or the start of something bigger?
