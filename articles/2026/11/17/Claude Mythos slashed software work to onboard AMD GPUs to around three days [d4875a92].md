---
id: "d4875a92aea85dac"
title: "Claude Mythos slashed software work to onboard AMD GPUs to around three days"
url: "https://tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat"
link: "https://tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat"
source: "Tom's Hardware"
domain: "tomshardware.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-17T01:35:16Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["nsoonhui"]
language: "en"
summary: "Anthropic says Claude Mythos Preview brought up prompt processing for one model on AMD Instinct MI355X GPUs in about three days."
tags: []
orgs: ["AMD", "Anthropic", "Nvidia", "OpenAI", "Google", "Meta", "Amazon"]
topics: ["chips & infrastructure", "models & research", "business & funding", "agents & coding"]
content_source: "fulltext"
word_count: 1158
paywalled: false
image: "http://www.bing.com/th?id=ONUT.P7CcfwHfas2BdFyvSdDZDA&pid=News"
discussion_url: "https://news.ycombinator.com/item?id=50526264"
score: 48
comments: 17
community: "Hacker News"
---

# Claude Mythos slashed software work to onboard AMD GPUs to around three days

Tom's Hardware · nsoonhui · 2026-11-17

Anthropic says Claude Mythos slashed software work to onboard AMD GPUs from up to 12 months to around three days —writing almost 100% of kernels autonomously chips away at Nvidia's CUDA moat
If AI can write the low-level code that ties models to Nvidia, CUDA matters less.
Anthropic told IPO investors that its Claude Mythos Preview model did the software work required to get its AI running on AMD’s GPUs in about three days, with “basically no human intervention,” a job it says used to take six to 12 months. The three days cover prompt processing for one Anthropic model on AMD MI355X GPUs “at a useful level of performance,” with Mythos porting or writing “almost 100% of the kernels.” That kind of low-level code, which ties an AI model to one company’s chips, has long been part of Nvidia’s CUDA moat, and an AI that can write it in days would suggest that moat is eroding.
Tom Brown, Anthropic’s co-founder and chief compute officer, made the time comparison, noting to investors that the original meant using a team of “dozens of engineers.” The company already runs its models on multiple kinds of chips — on GPUs from Nvidia and AMD, Google’s TPUs, and AWS Trainium — and its fleet is managed as “one fungible pool of compute.” Brown called the early multi-chip decision “an unconventional bet.” It may have been a wise one, given that Google’s TPUs can now natively run AI models built in PyTorch, and Meta uses them in production.
Anthropic's claim that the job used to take six to 12 months comes from past work, from its “historical experience bringing up new accelerators using traditional engineering approaches,” where tailoring the code to each hardware platform was a challenge. Removing that onboarding barrier could reduce things to a purchase decision, and Anthropic started working with AMD GPUs for the first time this year, with an agreement for up to 2 gigawatts now in place.
CUDA, Nvidia’s programming platform, is very mature at nearly two decades old. AMD has an equivalent, ROCm, with HIP as its programming layer. Code written for CUDA has to be transformed to work there, and AMD even built a tool called HIPify for the process. There is still a conversion cost to switching, and AMD’s vice president of AI software, Anush Elangovan, told EE Times in April that “Claude is better than HIPify because it has web search built in.”
AMD has been making the argument that AI can write this type of code since August of last year, presenting a research agent that fell short of human experts at the time. In September of that year, AMD CEO Lisa Su said on the Possible podcast that much of AI software is written in CUDA, which needs to be “translated to AMD,” and “a ton of that can now be done in software.”
Moving forward to July earlier this year, AMD’s senior vice president of AI, Vamsi Boppana, said its engineers were using AI models to generate GPU kernels, and Su said that when she asked whether her team was helping the Anthropic engineer working on the MI355X, she was told they didn’t need any help. Boppana said that in some cases, the resulting kernels were even “better than the most manually tuned versions.” Under its July agreement with Anthropic, AMD is also using Claude to optimize workloads for its Instinct GPUs and to speed up ROCm development.
At AMD’s Advancing AI event in July, OpenAI’s Philippe Tillet said that once OpenAI got its Helios racks, a single engineer confirmed everything worked within a few days, and that “agents are taking over our jobs, in a sense, as kernel engineers.” Before the event, AMD’s Andrew Dieckman, corporate vice president and general manager of the company’s data center GPU business, told reporters that he has had practically zero conversations with AMD’s customers about CUDA.
Until this week, though, all of this came from AMD or its stage, not from Anthropic to its own investors. Anthropic buys the chips rather than selling them, and it’s heading into its IPO next week, so its multi-chip approach — now with at least some numbers to back it up — carries more weight than a chipmaker’s claims. Its prospectus says it in writing, too, though without a number: “We can onboard new chip platforms in a fraction of the time it once took.”
The prompt processing (prefill) part of the workload is the step where a model reads and processes what it’s been given before it starts replying, and Anthropic hasn’t said whether the replying step (decode) was included as well. Anthropic’s chart, with its axis labeled “Time to onboard new silicon,” shows both lines reaching the same “~100%” mark without saying 100% of what. The company also hasn’t said how fast the model ran on AMD’s GPUs versus Nvidia’s, and that’s the comparison we want to see to show whether AMD’s chips, running AI-written code, can match Nvidia silicon.
On the other hand, Nvidia CEO Jensen Huang said in an April interview with Dwarkesh Patel that Nvidia already uses AI on its own kernels and knows its chips best — “nobody knows our architecture better than we do” — and can get the most out of them. Asked why labs like Anthropic use other accelerators, he called Anthropic “a unique instance, not a trend.” Nvidia and AMD, among seven companies, are buying $26.0 billion of Anthropic’s stock at the IPO price, so Nvidia is investing in the very company Huang called the exception.
In late July, SemiAnalysis published an article, “Can AMD break the CUDA Moat?,” which essentially said that software creation is not the same moat it was even a year ago. That said, the catch for AMD is that with agentic coding, “each agent requires GPUs to test their code against,” which means that the AI writing the code still needs the hardware. It has found a constant lack of GPUs inside AMD for this type of development, which has held AMD back and may be a new bottleneck.
That leaves CUDA’s moat somewhere in between. Getting a model running on a new chip, once the expensive part, appears to be getting cheaper, and better AI may wear down Nvidia’s claim that it knows its hardware best. As for Anthropic’s fungible pool, the chips in it aren’t fully interchangeable — Google’s TPUs are increasingly specialized, for example — and getting the most out of any of them still takes the hardware to test on. The moat is narrowing, but is not gone.
Anthropic’s first AMD MI450 chips, in Helios racks, are expected in the first half of 2027. That’s a new generation and an opportunity to see if the three-day bring-up can be repeated. Anthropic’s IPO comes sooner, after which it will report as a public company.
Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
