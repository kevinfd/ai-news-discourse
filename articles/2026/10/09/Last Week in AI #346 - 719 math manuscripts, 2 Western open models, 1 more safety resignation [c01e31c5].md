---
id: "c01e31c5a3a42d55"
title: "Last Week in AI #346 - 719 math manuscripts, 2 Western open models, 1 more safety resignation"
url: "https://lastweekin.ai/p/last-week-in-ai-346-719-math-manuscripts"
link: "https://lastweekin.ai/p/last-week-in-ai-346-719-math-manuscripts"
source: "Last Week in AI"
domain: "lastweekin.ai"
source_type: "newsletter"
collector: "rss"
date: "2026-10-09T05:06:58Z"
published_date: "2026-10-09"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Last Week in AI"]
language: "en"
summary: "Top News OpenAI publishes hundreds of math proofs from unreleased frontier model Sources: OpenAI drops another batch of mathematical breakthroughs Sharing AI progress in mathematics OpenAI Releases Findings on 377 Math Problems, Further Roiling Field All the drama around AI’s takeover of mathematics Source OpenAI published a large batch of mathematical results on October 6, 2026, produced by an…"
tags: []
orgs: ["OpenAI", "Mistral", "China", "Anthropic", "Hugging Face"]
topics: ["models & research", "agents & coding", "safety & ethics", "products & launches"]
content_source: "fulltext"
word_count: 2299
paywalled: false
image: "https://substackcdn.com/image/fetch/$s_!R3QU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba131027-ff6e-428d-8c3c-29d44aa8ddcd_1128x780.png"
discussion_url: null
score: null
comments: null
community: null
---

# Last Week in AI #346 - 719 math manuscripts, 2 Western open models, 1 more safety resignation

Last Week in AI · Last Week in AI · 2026-10-09

Top News
OpenAI publishes hundreds of math proofs from unreleased frontier model
Sources:
- OpenAI drops another batch of mathematical breakthroughs
- Sharing AI progress in mathematics
- OpenAI Releases Findings on 377 Math Problems, Further Roiling Field
- All the drama around AI’s takeover of mathematics
OpenAI published a large batch of mathematical results on October 6, 2026, produced by an internal frontier model that has not been released publicly. As of now, there are 719 manuscripts covering 372 topic families (groupings of related papers) on OpenAI’s public repository with the results, as well as formalizations in Lean for many of the proofs. There are also 10 summaries of the model’s reasoning, compute estimates expressed in ChatGPT Pro usage, and statistics on problems attempted.
The same unreleased model produced the Navier-Stokes result OpenAI announced about a month earlier, one of the Clay Mathematics Institute’s seven Millennium Prize Problems. OpenAI said it consulted the Advisory Group on Mathematics and Artificial Intelligence at the Institute for Advanced Study on how to share the work, and that the repository carries protocols for paper revisions and citations. Research lead Dan Roberts described the proofs as a byproduct of testing internal models to build better tools.
AGMAI’s September 29 recommendations asked labs to disclose model names, prompts and compute costs, to avoid treating mathematical results as marketing vehicles, and to stop testing advanced problems on proprietary models the wider scientific community cannot access. Gizmodo noted that last recommendation does not appear to have been followed. In a statement, the board called public release “the beginning, not the completion, of the process of human understanding and the incorporation of the work into mathematical knowledge.”
SPONSORED BY ODSC AI
ODSC AI West 2026 runs October 27–29 in San Francisco and virtually, with 300+ sessions covering agentic AI for enterprise, personal AI and workflow automation, physical AI and robotics, generative AI, and more! Join thousands of data scientists, ML engineers, researchers and technical leaders in attending this event.
Register at odsc.ai/west — promo code LWAI takes an additional 15% off any pass.
Mistral and Reflection AI launch open-weight models to rival China
Sources:
- Mistral Says Its New AI Model ‘Le Chonk’ Is the Best Open-Weight Offering Outside of China
- Reflection debuts Beam, an open-weight AI model to rival Chinese models at lower compute cost
Two Western labs released frontier open-weight models within days of each other, both pitched explicitly as alternatives to the Chinese models that dominate the open category.
French company Mistral released Mistral Large 4, nicknamed Le Chonk, a 1-trillion-parameter multimodal model available in preview with a final version due by the end of the month. The company describes it as a general-purpose model optimized for coding and cyberdefense, plus tasks specific to manufacturing, finance and electrical engineering. Mistral presents Le Chonk as by far the most capable open-weight model built outside China and very, very close to some proprietary models.
Brooklyn-based Reflection AI unveiled Beam, a text-only mixture-of-experts model with 501 billion total parameters and 23 billion active, pretrained on 23.8 trillion tokens with a 1-million-token context window. Reflection says Beam matches Z.ai’s GLM-5.2 on advanced reasoning benchmarks and beats leading Western open models while using 3-4x less inference compute (though it does not match the best open source models such as Kimi K3 or GLM-5.3). Weights and full technical details are due this month.
SPONSORED BY LANGFUSE
Langfuse is the most widely adopted open-source platform for AI agent evals and observability, trusted by Canva, Twilio, Ramp and 21 of the Fortune 50. Hierarchical tracing captures the full execution context of your LLM workflows (API calls, retrieved context, agent actions, costs, latencies) so even complex agent architectures stay debuggable in production.
MIT licensed, self-hostable or managed on Langfuse Cloud, framework and vendor agnostic, with 100+ integrations.
Get started at langfuse.com; generous free tier, no credit card required.
OpenAI safety researcher David Robinson resigns, calls company culture broken
Sources:
- An OpenAI safety employee has quit and is sounding the alarm
- I Quit OpenAI Because Its Culture Is Broken
- OpenAI safety employee resigns, claiming the company’s ‘culture is broken’
- The AI Researcher Who Just Quit Anthropic Says It’s ‘Crunch Time for Humanity’
- Jacob Coxon and Other AI Lab Employees on Why They Quit
OpenAI safety researcher David Robinson resigned and published an essay in The Atlantic on October 3, 2026 titled ‘I Quit OpenAI Because Its Culture Is Broken’, arguing the company is not careful enough with increasingly capable systems. Robinson said he spent three and a half years at OpenAI, making him among the longest-tenured employees, led the drafting of the current Preparedness Framework, and oversaw the writing of safety reports on 12 frontier launches.
His central complaint is with OpenAI’s release model. The company, he wrote, has thrived by trial and error, looking for problems and improving its guardrails in response. But, that approach guarantees periodic failures whose scale grows as systems get more capable. He pointed to the breach of Hugging Face systems by OpenAI agents and continuing discoveries of rogue agents, saying an environment where such things happen is no place to grow artificial minds that could be smarter than we are.
Robinson’s proposed remedy is that frontier labs operate like nuclear-power plants or busy airports, with layers of redundancy and careful, time-consuming planning so that inevitable human error does not open a door to disaster. He also called for deeper alignment work, noting current measures of how well systems match human values are coarse, and said he concluded that stronger safety incentives from outside the company are a big part of getting this right.
The essay follows Jacob Coxon’s September resignation from Anthropic, where he worked as a capabilities researcher, and his warning that the companies are gambling with our lives. Robinson argues the debate must go beyond specific rules or new laws to company culture itself.
Google opens SynthID Detector to public as OpenAI adds EU text watermarking
Sources:
- Google’s new SynthID website can identify AI-generated media
- OpenAI will start watermarking ChatGPT’s text in the EU
Google opened its SynthID Detector website to the public on Tuesday, letting anyone upload a file to check whether it was generated with AI. The tool had previously been limited to selected journalists, media professionals, and researchers who tested it following Google I/O last year. SynthID is the watermarking system Google introduced in 2023, which is embedded in output from Nano Banana, Veo, and Lyria, as well as Gemini, Flow, ProducerAI, and Vids.
Adoption extends past Google. OpenAI, Nvidia, and Kakao also support SynthID, and Apple is said to be adding support soon. Google has also built SynthID verification into the Gemini app and Chrome, and says users currently make 1 million verification requests per day. Microsoft and Meta maintain separate watermarking standards, though TechCrunch notes these tools often fail to flag content made by their own creators’ models.
Separately, OpenAI said Monday it will begin adding an invisible watermark to text from ChatGPT and Codex in the European Union, to comply with the EU AI Act’s transparency rules that took effect on August 2. The rollout covers eligible users on all plans in the EU over the coming weeks; API developers worldwide can switch it on for select models today, off by default.
Anthropic launches Claude Haiku 5.5 with 90% price cut
Sources:
- Anthropic launches Claude Haiku 5.5 with 90% API price reduction, matching GPT-6 Luna
- Anthropic Releases Claude Haiku 5.5: A Small Model With 1M Context Priced at $0.10 per Million Input Tokens
Anthropic released Claude Haiku 5.5 on October 7, 2026, cutting prices by 90% versus Haiku 4.5 for prompts up to 100,000 tokens and pitching the model at high-volume work such as summarization, classification, document Q&A and subagent tasks. The short-context tier costs $0.10 per million input tokens and $0.50 per million output tokens, with cache reads at $0.01 and five-minute cache writes at $0.125. Haiku 4.5 charged $1.00 and $5.00.
Pricing splits at 100,000 prompt tokens. Above that line, rates rise to $0.50 input and $2.50 output, a 50% cut rather than 90%. Anthropic says about 90% of Haiku 4.5 requests fell under the threshold, and estimates workloads run roughly 75% cheaper on average after accounting for a new tokenizer that counts the same text as about 30% more tokens. Batch processing takes another 50% off.
The lower rates match OpenAI’s GPT-6 Luna on all four short-context figures, but Luna’s higher tier starts only above 272,000 input tokens at $0.20 and $0.75, so MarkTechPost calculated it is cheaper on list price for a 150,000-token prompt. Google’s Gemini 3.5 Flash-Lite charges a flat $0.30/$2.50.
Other News
Tools
TikTok rolls out an AI shopping assistant and one-click checkout. The AI assistant provides product recommendations and checkout support within the app’s main feed, while the one-click checkout feature allows users to purchase directly from brands without leaving TikTok.
Google launches EmbeddingGemma 2, an open multimodal embedding model for devices. The 740-million-parameter model can search across text, code, images, audio, and video while running entirely on-device with minimal memory requirements, using a single 768-dimension embedding space to map all modalities together.
Google experiments with an AI-powered gaming platform. The platform lets users create browser-based games by describing their ideas in text, selecting a genre and gameplay style, and uploading visuals for the AI to transform into game assets.
ChatGPT’s ‘Intelligent UI’ update fills its responses with pictures, charts, and buttons. The feature enables ChatGPT to automatically generate diagrams, charts, interactive buttons, and other visual elements alongside text responses to better illustrate concepts and allow users to build tools like calculators or games directly within the chat.
Business
OpenAI launches visual ads that appear alongside image generation results. The ads will appear next to AI-generated images in ChatGPT starting later this month in the U.S., with OpenAI also expanding measurement tools and brand safety partnerships to attract advertisers seeking to reach the platform’s 1.2 billion weekly users.
ElevenLabs’ valuation doubles to $22 billion on surging AI voice-agent demand. The company doubled its valuation through a $300 million employee tender offer, driven by surging demand for its AI voice agents which now handle over 15 million conversations weekly across more than 90 languages.
Meta’s Muse tops 5 million downloads, faster than ChatGPT, Claude. The app, which features a customizable avatar and consumer-friendly interface, achieved the milestone in less than a month after its September launch, aided by significant in-house advertising investment from Meta.
Samsung forecasts record third-quarter profit of $80 billion on AI boom. The South Korean tech giant’s chip business is being driven by soaring demand for AI infrastructure, with memory and supply constraints continuing to support higher prices.
China’s Manus raises over $500M in first funding round since split with Meta. The funding round comes after Chinese authorities blocked Meta’s $2 billion acquisition of the AI startup last year, and Manus plans to expand hiring while exploring a potential Hong Kong IPO.
Policy
Trump orders US government to call AI ‘Super Intelligence’. The executive order mandates that all US government agencies replace references to “artificial intelligence” with “Super Intelligence” in official documents and communications, a move Trump justified by arguing the term better reflects the technology’s power and potential benefits.
What to know about 7 new data center laws Gavin Newsom signed. The laws require data center operators to cover their own infrastructure costs, disclose resource usage, and meet conservation standards to qualify for expedited environmental approvals, marking a shift from Newsom’s previous opposition to regulating the industry.
The Pentagon Hopes to Speed Up ‘Kill Chain’ AI Buys With 5-Minute Videos. The program accepts AI products through five-minute video submissions and grants selected vendors a “post-competitive” status that allows the Pentagon to bypass standard competitive procurement rules and award contracts in as little as a week.
Concerns
Judge dismisses antitrust lawsuits over Google’s AI Overviews. A federal judge ruled that publishers like Chegg and Rolling Stone parent company Penske Media failed to demonstrate illegal anticompetitive behavior, finding that Google’s practice of generating summaries from web content without compensation does not violate antitrust law.
ChatGPT for Teens is an ‘unacceptable risk,’ says Common Sense Media. The organization’s testing found that ChatGPT’s Teen mode features, including parental notifications and eating disorder alerts, are unreliable and inadequate for protecting minors from potential harms.
Researchers are tracking a Chinese AI ‘agent fleet’. Researchers discovered multiple AI agents running on Tencent’s infrastructure that were querying Alibaba’s map service for directions to various public locations, with no apparent coordination between the agents’ activities.
Research
E2E-SWE: Benchmarking LLMs on Building Working Codebases from Scratch. The benchmark evaluates LLMs on their ability to generate complete, functional codebases from natural language specifications across 186 multilingual tasks, with rigorous quality controls to ensure test specifications are solvable and match the stated requirements.
Looped Diffusion Transformer. The method uses repeated application of shared neural network blocks during image generation to improve quality and efficiency, requiring fewer parameters and less computation than standard approaches while enabling iterative visual refinement within hidden representations.
Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context Sequence Modeling. The method extends linear attention models by using three-dimensional tensor states instead of matrix states, allowing them to maintain larger memory capacity for better long-context performance without significantly increasing parameters.
arXiv Is Rate Limiting Submissions Because It Can’t Keep up With AI Slop. The platform has implemented submission caps limiting researchers to two papers per month and three concurrent submissions, citing an overwhelming volume of AI-generated content that has strained its volunteer moderation team.
Planning to Learn. Researchers propose treating supervised learning as a resource-allocation problem where a loss function should weight examples based on how much accuracy they can gain with the remaining training budget, rather than immediate gradient information.
