---
id: "0c63a761301701ac"
title: "Mercury 3 [Inception Labs] - Matching Luna/Haiku at 1000 tokens/sec"
url: "https://inceptionlabs.ai/blog/introducing-mercury-3"
link: "https://inceptionlabs.ai/blog/introducing-mercury-3"
source: "inceptionlabs.ai"
domain: "inceptionlabs.ai"
source_type: "community"
collector: "reddit"
date: "2026-10-19T17:22:01Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Ok_Knowledge_8259"]
language: "en"
summary: "Diffusion models finally taking off? I actually tested some general output against gpt 6 luna and either luna is really bad or this thing is very close or sometimes beating it. My testing is not extensive enough to confirm but maybe would need to try this thing in an agentic framework if it even works properly on that."
tags: ["r/singularity"]
orgs: ["OpenAI", "Anthropic", "Nvidia"]
topics: ["agents & coding", "models & research", "jobs & society", "search & media"]
content_source: "fulltext"
word_count: 867
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xa30cc/mercury_3_inception_labs_matching_lunahaiku_at/"
score: null
comments: null
community: "r/singularity"
---

# Mercury 3 [Inception Labs] - Matching Luna/Haiku at 1000 tokens/sec

inceptionlabs.ai · Ok_Knowledge_8259 · 2026-10-19

Today we’re introducing Mercury 3, the most capable diffusion-based LLM released to date. Across a range of benchmarks, Mercury 3 outperforms GPT-6 Luna and Claude Haiku 5.5, while running 4–8x faster at 1,000+ tokens per second.
Mercury 3 demonstrates that text diffusion scales. It’s more than 40x larger than Mercury 1 and is vastly more intelligent, but just as fast.
Early-access partners already use Mercury 3 for voice and chat support, real-time tutoring, data engineering, and web navigation:
Mercury 3 at a glance
- Quality: On par or better than frontier speed-optimized models like GPT-6 Luna and Claude Haiku 5.5.
- Speed: 1,068 tokens per second on NVIDIA GPUs.
- Context: 1M tokens, up from 260K for Mercury 2.5
- Price: $0.20 per million input and $0.70 per million output tokens. 
  - At launch, Mercury 3 is 50% off at $0.10 per 1M input and $0.35 per 1M output. Cached tokens are 90% off the input price.
Diffusion at scale
When we launched Mercury 1, it was the first proof point that diffusion LLMs could be built for commercial applications. The open question in the AI community was whether diffusion LLMs could scale to compete with autoregressive models on complex use cases.
Mercury 3 answers that question: they can. We’ve scaled Mercury more than 40x in total parameters, and intelligence across a range of standard benchmarks has risen 3x from Mercury 1 (mini) to Mercury 3. The scaling laws that drove progress in autoregressive models hold for diffusion too.
Mercury 3 in production
Early-access partners are already running Mercury 3 to power latency-sensitive applications such as browser use agents, interactive education, real-time search agents, and customer support.
Browser Use Agents
Agents wait on the model at every step, so small delays compound quickly. Mercury keeps each pass fast, whether the agent is navigating websites, researching across sources, or analyzing logs and tracing incidents. Agents finish sooner and have time to try more approaches before answering.
We ran Mercury 3 inside our production web-agent harness against frontier models, on 50 live Mind2Web navigation tasks. Mercury 3 completed 50% of them, significantly more than GPT-6.1-Sol. It did so using the same token volume and the same number of agent steps as a frontier model, at a fraction of the per-token cost.
Shuhao Zhang, Cofounder, TinyFish AI
Interactive Education
Learning runs on fast feedback loops, and any delay pulls a student out of the material. Mercury reasons through each request and responds in near real time, whether it’s a voice tutor carrying a conversation, an assistant grading work, or an app adapting the next question to what the student just got wrong.
Mercury 3 allowed us to give every student instant feedback without giving up reasoning. Hints, marked answers and definitions now come back in about a second, with quality as good as or better than the models we ran before. When a student is stuck on a question, that speed keeps them working instead of waiting, and it was a drop-in swap for our existing stack.
Michael Tong, Co-founder/CTO, General Learning aka RevisionDojo
Real-time search agents
Search applications start to feel unresponsive after just a few seconds delay. Mercury 3 runs fast enough to process dozens of documents and still answer while the user is engaged.
On smart glasses, an answer that takes five seconds feels broken. In our Sense API tests, Octen search took about 80ms; model generation was the bottleneck. Mercury 3 delivered the best balance of speed and quality among the fast models we tested, with a median generation time of 0.9 seconds and a median end-to-end response time of 2.2 seconds.
Kuan Zou, Founder & CEO, Octen AI
Customer support
Support agents have to answer quickly, often for regulated businesses where a wrong answer is costly. Mercury keeps responses conversational without sacrificing accuracy.
At Lorikeet, we help complex and regulated businesses build a concierge for their customers that works across voice, chat and email. In chat and voice, customers need fast responses, but we can't compromise on accuracy or getting the job done correctly. In early testing, Mercury 3 beat other models on latency while also performing higher on evals and in production.
Michael Gribben, Member of Technical Staff, Lorikeet
A real-time product portfolio
Mercury 3 is the flagship model in a widening portfolio of products that enable real-time AI.
- Mercury Voice: Mercury Voice is customized for the extreme low-latency requirements of voice applications and for minimizing time to first answer token (TTFAT), not just end-to-end latency. It’s already powering agents at Audivi AI, Altur, and OpenCall.
- Mercury Decide: Mercury Decide is a decision model built for high-volume classification. It outperforms Jev on benchmarks including JevBench and LegalBench.
Get started
Mercury 3 is available today on the Inception API Platform and through OpenRouter, Baseten, and Vercel. It is OpenAI API compatible, so it drops into your existing stack with no rewrites. Enterprise deployments support dedicated capacity, autoscaling, compliance controls, and configurable data retention.
- Try Mercury 3 in chat
- Try the API with 100 million free tokens
- Read the API docs
- Enterprise evaluations: we'll partner with you on workload fit, eval design, and performance under your serving constraints. Contact us.
