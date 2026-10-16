---
id: "36c7f236badbda72"
title: "“Take work away from frontier LLMs”: Subquadratic’s decision model claims 12x Jev’s context window"
url: "https://thenewstack.io/subquadratic-snap-jev-decision-model"
link: "https://thenewstack.io/subquadratic-snap-jev-decision-model"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T13:35:15Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Paul Sawers"]
language: "en"
summary: "Jev has a lot to answer for. Ever since AI startup TypeSafe unveiled the decision model in mid-September, the industry has been awash with alternatives , with OpenAI, Perplexity, Cloudflare, Amazon and, most recently, Microsoft all getting involved . \n\n Decision models, it’s safe to say, are hot. \n\n Now, San Francisco-based foundation-model startup Subquadratic has joined the rush with SubQ Snap…"
tags: ["AI", "AI Agents", "AI Engineering", "AI Models"]
orgs: ["OpenAI", "Microsoft", "Amazon", "Perplexity"]
topics: ["models & research", "agents & coding", "business & funding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1375
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# “Take work away from frontier LLMs”: Subquadratic’s decision model claims 12x Jev’s context window

The New Stack · Paul Sawers · 2026-10-14

“Take work away from frontier LLMs”: Subquadratic’s decision model claims 12x Jev’s context window
Jev has a lot to answer for. Ever since AI startup TypeSafe unveiled the decision model in mid-September, the industry has been awash with alternatives, with OpenAI, Perplexity, Cloudflare, Amazon and, most recently, Microsoft all getting involved.
Decision models, it’s safe to say, are hot.
Now, San Francisco-based foundation-model startup Subquadratic has joined the rush with SubQ Snap, a decision model that it claims can process up to 384,000 tokens of text and images in a single request — 12 times Jev’s 32K-token per-decision context limit.
In a blog post published on Monday, the company says Snap can process 100K tokens and return a decision in approximately one second, potentially allowing AI agents to make decisions across large codebases, documents, and interaction histories without having to break information into smaller chunks.
Why a bigger context window matters
Unlike traditional large language models (LLMs), which generate text and code, decision models specialize in selecting from predefined answers. That could mean choosing which tool an AI agent should use next, identifying relevant files, or determining whether a test has passed.
On Tuesday, The New Stack reported on how Workday is using Jev to build user interfaces on the fly for its Sana AI assistant, selecting prebuilt components such as paycheck cards and date pickers based on what an employee asks.
The attraction, ultimately, is speed and cost. These decisions occur frequently during an agent’s execution, and delegating them to smaller, specialized models reduces reliance on expensive frontier LLMs.
In an email Q&A, Subquadratic CEO and co-founder Alex Whedon acknowledges that Jev’s arrival helped shape Subquadratic’s own entry into the market.
“Snap was developed with inspiration from Jev, because decision models are highly thesis-aligned.”
“Snap was developed with inspiration from Jev, because decision models are highly thesis-aligned,” Whedon tells The New Stack. “Decision models remove the need for decoding for some problems.”
However, Whedon believes the technology has much greater potential than the supporting roles decision models currently perform, such as evaluating LLM outputs or selecting which model should handle a task.
“We see a vacuum of vision for decision models,” Whedon says. “Decision models become exciting when they actually take work away from frontier LLMs.”
“Decision models become exciting when they actually take work away from frontier LLMs.”
While the space is somewhat crowded, Subquadratic argues that existing decision models struggle when the information needed to make a choice exceeds their context limits.
Consider a coding agent trying to fix a bug in a large repository. The problem might originate in a different module from the one producing the error, while important clues could be buried in test files or documentation. With a 32K-token window, the agent may have to discard potentially relevant information or turn to a larger LLM. Snap’s 384K-token window, Whedon argues, allows it to examine more of the codebase, logs and previous actions together before deciding what to do next.
Snap addresses this through Subquadratic Sparse Attention (SSA), the architecture the company first introduced in May to reduce the computational cost of processing long inputs. According to Subquadratic, its attention requirements grow linearly with context length, rather than quadratically as in conventional transformers. Whedon argues that improving the underlying algorithms matters regardless of how much the big labs spend on compute; otherwise, he says, “we are inevitably leaving intelligence gains on the table.”
Subquadratic’s own long-context benchmarks suggest Snap can maintain accuracy even as the amount of information it processes increases. On an adapted version of the RULER retrieval benchmark, Snap scored between 96.3 and 99.8 across inputs ranging from 32K to one million tokens. On Decision LCR, which tests reasoning across multiple documents, it scored 74.0 against Jev’s 48.0, with Jev processing the documents in chunks.
Whedon clarified that Snap’s advertised 384K-token context limit is a temporary restriction imposed for the public preview because of available computing capacity. The company tested the model at one million tokens but says supporting that length publicly would require approximately 2.6 times more compute.
On shorter tasks, Subquadratic reports that Snap scored 61.7 against Jev’s 57.9 on Decision Index 0.2.1. It also led on Bespoke Labs’ Nimble benchmark, achieving 82.9% accuracy compared with Jev’s 76.0%.
Across 16 enterprise-oriented benchmarks, Snap outperformed Jev on 13, according to Subquadratic’s testing, with an average score of 67.6 versus 61.6. However, Jev performed better on three tests, including When2Call, which assesses whether an agent should invoke a tool, ask for clarification, answer directly or decline.
Whedon confirms that all the published Snap results were produced internally, although Subquadratic has released the code for its adapted long-context evaluations so others can reproduce them.
Snap is also absent from the latest Decision Index leaderboard. Whedon says the benchmark’s authors told him that its current version focuses on open-weight models, with Jev an exception. The latest index, now at version 0.3.2, also incorporates private tests, meaning Snap’s published 0.2.1 score can’t be directly compared with the newer results.
As for why the company focused its comparisons on Jev, Whedon says it remains the model most relevant to Subquadratic’s enterprise design partners, followed by OpenAI’s Decisions API. Comparisons with newer rivals are planned.
“Jev still seems like the model to compare against in this category.”
“Jev still seems like the model to compare against in this category, so being able to outperform it in a largely generalizable way has been the frontier signal we were looking for,” Whedon explains.
Less plumbing, more context
Beyond the benchmarks, Subquadratic argues that a larger context window could simplify how developers build AI agents.
Currently, developers often rely on retrieval, summarization, and chunking to squeeze large documents or codebases into smaller context windows. Each step involves deciding which information to preserve, potentially omitting details that later prove important.
Whedon says Snap could eliminate some of those intermediate steps when the material fits within its 384K-token limit, allowing agents to examine entire documents or collections of related files in a single request.
However, he acknowledges that retrieval will remain necessary when dealing with much larger collections of information.
“Retrieval won’t disappear — enterprises have corpora far larger than 384K tokens, and you still need a way to bring the right material into the window,” Whedon notes. “But the window is now big enough that retrieval can be coarse, pulling in whole documents or modules instead of carefully trimmed snippets. That removes a lot of the fragile parts.”
Snap is available in public preview, priced at $0.05 per million input tokens, with no charge for outputs. That means processing 100K tokens costs approximately half a cent, while a request using the full 384K-token window costs around two cents.
Whedon explains that the pricing reflects the computational demands of a model designed to select answers, as opposed to generating lengthy responses.
“We priced it where the cost actually is.”
“We priced it where the cost actually is,” Whedon says. “A decision model doesn’t generate text. It reads the input and returns a probability for each allowed answer, so nearly all of the compute goes into reading, and producing the output costs us almost nothing.”
The (Subquadratic) story so far
Subquadratic emerged from stealth in May with $29 million in seed funding, at a reported $500 million valuation. Previously known as Aldea, the startup was co-founded by Justin Dangel and Whedon, a former Meta engineer and head of generative AI at Tribe AI. Whedon succeeded Dangel as CEO a few months ago, having previously served as CTO. Dangel is now chairman.
As The New Stack reported at launch, Subquadratic’s debut model, SubQ, attracted attention for its claimed 12-million-token context window, alongside substantial improvements in computational efficiency.
In June, the company published more detailed benchmarks for its earlier SubQ 1.1 Small model, with certain results independently verified by data firm Appen. And in a July interview with The New Stack, Whedon revealed that Subquadratic was already investigating architectures that dispense with attention altogether.
And so Snap builds on the company’s existing sparse-attention research, bringing its long-context ambitions into the increasingly crowded decision-model market.
For now, Snap’s claimed performance advantage rests on Subquadratic’s own benchmark results. Independent testing will show whether its larger context window really leads to better decisions.
