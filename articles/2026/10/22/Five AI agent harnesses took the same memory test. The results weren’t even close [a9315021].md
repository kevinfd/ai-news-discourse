---
id: "a931502160785776"
title: "Five AI agent harnesses took the same memory test. The results weren’t even close."
url: "https://thenewstack.io/letta-frontiermemory-agent-harness-benchmark"
link: "https://thenewstack.io/letta-frontiermemory-agent-harness-benchmark"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T18:34:32Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "AI agents are getting better at remembering past conversations and earlier tasks but remembering something doesn’t guarantee an agent can use it to do better work next time. Letta’s new FrontierMemory benchmark, released Wednesday, tests that gap by measuring whether agents can learn from experience rather than by just retrieving stored information. Early results show a widespread in performance…"
tags: ["AI Agents", "AI Engineering", "AI Infrastructure"]
orgs: ["OpenAI", "Anthropic", "Google", "xAI"]
topics: ["agents & coding", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 963
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Five AI agent harnesses took the same memory test. The results weren’t even close.

The New Stack · Amanda Caswell · 2026-10-22

Five AI agent harnesses took the same memory test. The results weren’t even close.
AI agents are getting better at remembering past conversations and earlier tasks but remembering something doesn’t guarantee an agent can use it to do better work next time. Letta’s new FrontierMemory benchmark, released Wednesday, tests that gap by measuring whether agents can learn from experience rather than by just retrieving stored information. Early results show a widespread in performance across agent harnesses, the the infrastructure that manages how an agent operates.
Letta Dream came out on top with a 73.3% score, followed by Prime Agent at 60%. OpenAI Agents SDK scored 40%, while Claude Managed Agents and Hermes Agent trailed at 33.3% and 26.7%, respectively.
Recall isn’t learning
“Modern ‘memory’ benchmarks are saturated since they measure recall of facts,” Letta co-founder and CEO Charles Packer writes on X, saying that in the coding harness and bash loop era, recall is solved, while continual learning in token space, meaning learning through the context an agent keeps rather than through weight updates, remains unsolved.
Sarah Wooders, also a Letta co-founder, points to another problem on X. Most coding and knowledge-work benchmarks evaluate unrelated tasks with all the necessary context provided upfront. But that’s not how people actually work. Wooders compares it to starting a new job: A new hire needs plenty of direction, while someone who’s been there for years can often get the job done with little explanation.
Packer’s premise is that “if AI-generated memory is good, it should actually improve downstream task performance.”
FrontierMemory takes a different approach. Agents receive transcripts of earlier work, including successful and failed attempts, and then generate their own memories to help complete later tasks. Packer’s premise is that “if AI-generated memory is good, it should actually improve downstream task performance.” Developers have already embraced the underlying idea, building continually learning agents by pairing a language model with memory systems and feedback loops.
Letta reworked existing coding and knowledge-work tests so agents had to use what they learned from previous tasks instead of having everything spelled out for them. After reviewing and fixing problems with the original tests, Letta narrowed FrontierMemory 1.0 to just 15 tasks.
Harness beats model
The harness itself may matter just as much as the model running inside it. Letta tested five agent systems to see how well they could learn from previous work and use those lessons on new tasks.
The harness itself may matter just as much as the model running inside it.
Letta Dream beat OpenAI Agents SDK 60% to 40% when both used GPT-6.1 Sol to create memories and GPT-6 Sol to complete tasks. The results were even further apart with Claude Opus 5.5. Dream scored 73.3%, Prime Agent hit 60%, and Claude Managed Agents came in at 33.3%.
Packer says the the way agents handle AI “dreaming” makes a big difference. Dreaming is when an agent reviews past work and turns what it learned into instructions or memories it can use later. He also points to Prime Agent outperforming Hermes Agent as another example of how much these systems can vary. But there’s a downside: without checks on what gets saved, agents risk learning and repeating bad habits.
FrontierMemory also compared seven frontier models on how well they generate useful memories. Anthropic’s Claude Opus 5.5 and Z.ai’s GLM-5.3 tied for first at 73.3%, Kimi K3 followed at 66.7%, and OpenAI’s GPT-6.1 Sol and Google’s Gemini 4 Argon both scored 60%. Muse Wonder reached 46.7%, and Grok 4.7 finished at 33.3%. Packer says Opus 5.5 and GLM-5.3 are significantly better at generating useful memories than GPT-6.1 Sol.
Packer says Opus 5.5 and GLM-5.3 are significantly better at generating useful memories than GPT-6.1 Sol.
Cheaper memory, lower scores
But OpenAI had a big price advantage. GPT-6.1 Sol cost an estimated $0.77 per task, compared with $2.80 for Opus 5.5 and $3.58 for GLM-5.3. So while OpenAI scored lower, it was much cheaper to run.
Letta used its Dream harness to create memories with each model, then tested how well those memories worked on tasks run in Letta Code. The results show a tradeoff between better memory, stronger performance and lower costs.
Memory that travels
Letta also looked at why some memories worked better than others. In one test involving company pricing data, Opus 5.5 created a skill telling the agent when to use certain information. GPT-6.1 Sol created four separate skills, but the agent never found the one it needed.
Gemini 4 Argon made a different mistake. It remembered specific file sizes, which wasn’t much help when the next task involved different files. Opus 5.5 instead told the agent to check both the usual file and email for information. That worked even when the task changed. Memories created by Opus 5.5 helped GPT-6 Sol complete tasks, suggesting developers could use a more expensive model to build memories and a cheaper one to do the work.
Other developers have taken notice. After Letta’s Sarah Wooders posted about the benchmark on X, the OpenClaw account responded that it would like to see a plugin for its platform. The account says its multiplayer environment would be an interesting place to test the benchmark, raising questions about how memory works when several agents share the same harness.
“Yes definitely – would love to add OpenClaw to the harness comparison!” Wooders writes. “Extending to multiplayer memory is also a very interesting future direction.”
What the benchmark misses
FrontierMemory is still early. With just 15 tasks and one attempt per task, a single result can shift the scores by roughly 6.7 percentage points. The benchmark currently focuses on agents learning from past work rather than updating memories as they go. Packer says the next release will add longer-running tasks and online memory updates.
