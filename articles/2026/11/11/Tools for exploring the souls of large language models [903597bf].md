---
id: "903597bf673b56e5"
title: "Tools for exploring the souls of large language models"
url: "https://oshea00.github.io/posts/tinygpt-visualizer"
link: "https://oshea00.github.io/posts/tinygpt-visualizer"
source: "MikesBlog"
domain: "oshea00.github.io"
source_type: "community"
collector: "hackernews"
date: "2026-11-11T20:45:50Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["r00tanon"]
language: "en"
summary: "There is that old joke told by Woody Allen describing his experience as a university student: “I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of the boy sitting next to me.” If he’d managed to pass his course, Woody Allen might have been ahead of his time.\nMetaphysics is becoming a popular topic today, and it seems now everyone desperately wants to look…"
tags: []
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 489
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50458434"
score: 51
comments: 12
community: "Hacker News"
---

# Tools for exploring the souls of large language models

MikesBlog · r00tanon · 2026-11-11

There is that old joke told by Woody Allen describing his experience as a university student: “I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of the boy sitting next to me.” If he’d managed to pass his course, Woody Allen might have been ahead of his time.
Metaphysics is becoming a popular topic today, and it seems now everyone desperately wants to look for souls in large language models (LLMs). A recent conference last April was held by Anthropic with religious scholars and philosophical thinkers to discuss the nature of the soul when it came to their latest Claude models. It seems they needed guidance that Dario Amodei was unable to provide.
The time seems ripe to dig into how we might actually peer into the mind of the LLM sitting next to you. There’s been a lot of ongoing research; however, the self-same foundation model companies, Anthropic and OpenAI among them, have been criticized for dedicating more compute dollars into better models rather than the safety research. Mechanistic interpretability, the field of AI research devoted to exploring what goes on inside these models, has grown from a handful of researchers in 2021 to hundreds of active contributors. Yet, in spite of funding gaps and the lack of larger colloquiums, the research community has been coming up with some interesting insights and tools to help do the “peering.”
Rather than sit on the sidelines and wonder how this could be done, I thought it would be interesting to create a tool that would allow more people to join the party. And that is what led to the development of the “TinyGPT Visualizer.” The goals I had for this were modest. I wanted a tool I could use to survey the field and try the actual techniques to learn how they work. Being a visual person, I began thinking about an X-ray machine—something able to see inside a real model. Not a toy model. A real one, but one small enough to see on a screen with all its working parts.
Let me show what it looks like:
We may wonder where the consciousness can be found in the collection of numeric matrices that our models comprise; the numbers are there to see. Unlike the brains of humans, we can stop and look at the numbers as the thoughts are formed without killing the patient, and, unlike human brains, we can search those numbers for patterns and algorithms which explain the results these models emit as well-formed prose, code, music, and videos. Will we find well-formed emotions? If so, they will be in the numbers.
Will philosophy and religion help us? These disciplines haven’t had to rely on numbers and calculations up to this point, but perhaps they now have new ground to pound.
TinyGPT Visualizer is open source. You can find the code, setup instructions, and documentation on GitHub: github.com/oshea00/tinygpt-viz.
