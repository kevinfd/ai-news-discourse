---
id: "e0f6eaf89a313a2f"
title: "Introducing Gemini Decision 1: A Model That Picks Answers Instead of Writing Them"
url: "https://kdnuggets.com/introducing-gemini-decision-1-a-model-that-picks-answers-instead-of-writing-them"
link: "https://kdnuggets.com/introducing-gemini-decision-1-a-model-that-picks-answers-instead-of-writing-them"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-18T17:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Shittu Olumide"]
language: "en"
summary: "Google's newest model has one job, and it never writes a word doing it. Decision 1 reads text, images, video, audio and PDFs in a single forward pass, up to 262,144 input tokens per request."
tags: []
orgs: ["Google"]
topics: ["models & research", "jobs & society", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 1125
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kd-introducing-gemini-decision-1-a-model-that-picks-answers-instead-of-writing-them-photo-1200x600-feature.png"
discussion_url: null
score: null
comments: null
community: null
---

# Introducing Gemini Decision 1: A Model That Picks Answers Instead of Writing Them

KDnuggets · Shittu Olumide · 2026-11-18

Introducing Gemini Decision 1: A Model That Picks Answers Instead of Writing Them
Google's newest model has one job, and it never writes a word doing it. Decision 1 reads text, images, video, audio and PDFs in a single forward pass, up to 262,144 input tokens per request.
Google's newest model has one job, and it never writes a word doing it. Gemini Decision 1, launched last week with the new Gemini Decisions API, takes an input and a list of closed questions and returns probabilities instead of prose: yes or no, option A, B or C, a score on a rubric.
That sounds small, but it isn't. Every agent stack runs on dozens of these quiet calls: which model gets this query, which tool fires, whether this message breaks a policy. Most teams handle them with a full generative model and a JSON parser, paying for output tokens they throw away. Google now sells that layer on its own, at \$0.10 per million input tokens and nothing for output.
What Gemini Decision 1 Does
Decision 1 reads text, images, video, audio and PDFs in a single forward pass, up to 262,144 input tokens per request. Against that one input, you can ask up to 1,000 independent questions of three kinds:
- Yes/no (noul in the API) returns a probability between 0.01 and 0.99
- Choice picks from 2 to 255 options and returns a probability for each
- Score grades against an ordered rubric and returns a weighted score plus a probability per level
Every answer carries a confidence value, so your code can send uncertain cases to a fallback or a person.
The pricing is the pitch. You pay \$0.10 per million input tokens, the shared input is billed once no matter how many questions you ask, and output costs nothing because there is none. A no-cost tier in Google AI Studio covers prototyping.
The capability table shows what this model is not. Text generation, thinking, function calling, structured outputs, batch and caching are all listed as unsupported. It's a scoring engine, not a chatbot.
What Happened When We Ran It?
We installed Google's google-genai SDK, created a free API key in AI Studio and ran three tests: Google's quickstart, Google's image example from the launch post, and an ambiguous support message of our own. Latency was timed from our machine, so it includes the network round trip.
The quickstart asks two questions about one customer message:
from google import genai
client = genai.Client(http_options={"api_version": "v1beta"})
result = client.decisions.create(
    model="gemini-decision-1",
    input="The blue mug I ordered on Monday arrived cracked on Wednesday.",
    questions={
        "is_damaged": {"type": "noul", "instructions": "Did the item arrive damaged?"},
        "queue": {
            "type": "choice",
            "instructions": "Which support queue should handle this message?",
            "criteria": {
                "billing": "Payment, invoice, or refund questions.",
                "replacements": "Damaged, missing, or wrong items.",
                "general": "Product questions and account updates.",
            },
        },
    },
)
print(result.answers["queue"].choice, result.answers["queue"].confidence)
For the image test, input becomes a list holding an image URL and a text note. Here's what came back:
Medians exclude each test's first call. Accuracy was clean: both of Google's examples came back right, and the image result matched Google's own screenshot. Every call billed zero output tokens. In dollars, the text query costs about \$0.000017 per call, roughly 58,000 calls for a dollar. The image query costs about \$0.00013.
Google Is Already Running on It
Google says four of its own products use the Decisions API:
- Gemini Notebook routes each query to a model tier and thinking level, which Google says cuts latency on everyday queries by up to 40%
- Stitch uses it in its rapid canvas experiment to build playable wireframes and apply voice or tap edits
- CC from Google Labs picks an emoji reaction from more than 200 options without adding visible delay
- Google Search uses it as a safety layer that checks Model Context Protocol tools for adversarial behavior
Our Take
1. The Confidence Score Is the Real Product
Our ambiguous message is the test that matters. It fit two queues, and the model said so: 50.2% replacements, 48.4% billing, confidence 0.50. It didn't fake certainty on a coin flip, and in the same call it still rated the chipped handle as damage at 0.99.
One example doesn't prove calibration, which is measured across thousands of cases. But it's the behavior Google is selling, and it showed up when we went looking for it.
2. Read Confidence, Not Just Choice
Here's the trap. On that coin-flip message, the choice field still returned replacements, with no flag attached. Code that reads only the winner routes it as confidently as the clear case.
The calibration is only worth something if you set a threshold on confidence and send everything below it elsewhere. Google's quickstart prints the winner. Your production code shouldn't stop there.
3. The Speed Claim Didn't Hold for Images
Google quotes 150 to 250 ms end to end. After the first call, our text calls landed between 339 and 577 ms, a gap network distance can plausibly explain. Our image calls took 1.1 to 1.4 seconds, a median five to nine times the claim, though Google says its figures hold across multimodal inputs.
Some of that may be Google fetching the image from a URL and processing 1,064 image tokens. We can't separate the causes from outside. Two more details: Google's latency figure covers contexts up to 16K tokens, not the full 256K, and identical calls in our runs varied by more than 300 ms. Benchmark it on your own media before it goes anywhere near a real-time path.
4. The Benchmarks Are Google's Own
The "nearly 5x cheaper" figure compares Decision 1 with Google's own Gemini 3.5 Flash-Lite, on a benchmark suite Google chose. That's useful if you already run Gemini. It says nothing about how Decision 1 compares with a small fine-tuned classifier you already have.
5. Check the Small Print
The model page pitches classification over live media streams, while the same page lists the Live API as unsupported. And the model is Gemini-only for now. It's on OpenRouter, LangChain, Vercel's AI SDK, LiteLLM and others, but Google Cloud support is still marked as coming soon.
Wrapping Up
Decision 1 does one narrow job well. It's cheap, it was accurate on everything we gave it, and it admitted doubt when we pushed it. Use it for routing and policy checks now. Wire your code to confidence from the first day, and time it on your own images before you promise anyone 200 ms.
Resources
 
Shittu Olumide is a software engineer and technical writer passionate about leveraging cutting-edge technologies to craft compelling narratives, with a keen eye for detail and a knack for simplifying complex concepts. You can also find Shittu on Twitter.
