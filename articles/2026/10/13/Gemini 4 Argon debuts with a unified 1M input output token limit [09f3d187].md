---
id: "09f3d187d085f31f"
title: "Gemini 4 Argon debuts with a unified 1M input/output token limit"
url: "https://thenewstack.io/gemini-4-argon-live"
link: "https://thenewstack.io/gemini-4-argon-live"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-13T16:00:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "On Tuesday, Google made Gemini 4 Argon , the company’s new flagship model, available to developers on the paid tier of the Gemini API through Google AI Studio, as well as in several of the company’s other developer and consumer tools. \n\n Google announced the model on September 30. Initial external access was limited to selected cyber defenders in its Fairwind Program and other trusted testers;…"
tags: ["AI"]
orgs: ["Google", "Anthropic", "OpenAI"]
topics: ["agents & coding", "models & research", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 1091
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Gemini 4 Argon debuts with a unified 1M input/output token limit

The New Stack · Frederic Lardinois · 2026-10-13

Gemini 4 Argon debuts with a unified 1M input/output token limit
On Tuesday, Google made Gemini 4 Argon, the company’s new flagship model, available to developers on the paid tier of the Gemini API through Google AI Studio, as well as in several of the company’s other developer and consumer tools.
Google announced the model on September 30. Initial external access was limited to selected cyber defenders in its Fairwind Program and other trusted testers; Google employees were also using it internally.
Gemini 4 Argon pricing
Google is giving the model a competitive price. Developers will pay an introductory $2 per million input tokens and $10 per million output tokens through November 30, with a single 1 million-token budget for input and output combined. That’s the same price as OpenAI’s GPT-6.1 Sol.
After that date, Google’s new model will cost $4 and $20 per million tokens, matching Anthropic’s Claude Opus 5.5. Cached input tokens are 95 percent off during the introductory period.
During the introductory period, Argon also costs a fifth of what Anthropic charges for Claude Fable 5.1 and OpenAI charges for GPT-6 Astra, which both list at $10 and $50 per million tokens.
Developers can call the model as gemini-4-argon through Google’s Interactions API, with support in the google-genai SDKs. Android developers can also build it into their apps through Firebase AI Logic.
One budget for input and output
Argon’s unified 1 million input/output token limit covers both what goes into the model and what comes out of it, according to Google. That’s markedly different from how Google described it in the original Sept. 30 Argon announcement. At the time, it called the limit an output cap of 1 million tokens, up from 64,000 in earlier Gemini models.
With what is now a shared budget, the equation changes a bit because a long prompt can now eat into how much the model can write back. For example, if a request loads 800,000 tokens of code, that leaves only 200,000 for the response.
In comparison, Claude Opus 5.5 combines the standard 1 million-token context window with a separate output cap of 128,000 tokens.
Google says the extra room will let Argon keep working on long, multistep coding, science, and agent jobs.
Gemini 4 Argon benchmarks
Google says Argon ranks first on the Vals Index, which scores models on finance, coding, legal, and tax work and weights each sector by its share of U.S. GDP.
On Embodied Reasoning Question Answering (ERQA), a test of physical and spatial reasoning, Google reports Argon scored 87 percent. That puts it ahead of Claude Opus 5.5 at 82.3 percent, GPT-6 Astra at 81 percent, and Claude Fable 5.1 at 74 percent.
Bloomberg reported Sept. 30 that some Google employees with access to the model said it struggled with certain coding tasks, particularly front-end design. Google told Bloomberg it would be “inaccurate to say that Gemini 4 is underperforming in areas such as coding.”
For now, we don’t have a full set of new benchmarks to better compare Argon to other models. Like some other frontier labs, Google focused its announcement more on “feels” than data. Benchmarks never tell the full story, but we’ll update this post once we hear more. Artificial Analysis published an evaluation on September 30: Argon scored 53 on its Intelligence Index, matching GPT-6 Astra at the models’ tested reasoning settings. However, there’s no guarantee the model released on Tuesday is precisely the same as the one tested on September 30.
Argon in Antigravity
Where else Argon is available is a bit complicated.
For coding, Google is also making Argon available in Antigravity, its platform for running coding agents across the editor, terminal, and browser. Argon is available in the Antigravity desktop app for macOS, Windows, and Linux and in the Antigravity CLI, but only for Google AI Ultra subscribers and eligible Gemini Enterprise plans.
AI Pro subscribers get Argon in the Gemini app, but not in Antigravity.
Google is also bringing Antigravity’s coding interface into the Gemini app for macOS, so users can move between chatting and coding without switching tools. Anthropic and OpenAI do the same with their Claude and ChatGPT/Codex desktop apps, but nobody has found an elegant way to combine these chat and coding tools into a single interface.
In Android Studio Canary, developers can sign in to Antigravity from the agent tool window, and a new Android CLI plugin gives the agent access to local Android build tools.
More than 100,000 Googlers use Argon each month in an in-house build of Antigravity, the company says. Over four weeks, code submitted by agents rose 35 percent while post-submit rollbacks fell 30 percent.
Google says more than half of its Cloud sales staff and almost half of its finance team now use Antigravity.
Argon in the Gemini app
Subscribers on Google’s AI Pro and Ultra plans now also get access to Argon in the Gemini app and in AI Mode in Search.
In addition to the new model, the Gemini app is also getting a new toggle that lets users turn a chat into a task, which Gemini can then keep working on after the user steps away from the computer.
Cyber defenders and agent safety
Google is also expanding Fairwind, the program it launched September 2 to give vetted security teams early access to its cyber models.
Selected Fairwind partners can access Argon without its cyber guardrails, and Google says it’s adding hundreds more partners to the more than 650 the program had when it launched.
For the public model now available, Google says it trained Argon to check with a person before doing anything it can’t undo and to report when it hits a wall instead of working around it.
On coding evaluations, Argon tried unauthorized shortcuts 2 percent of the time, the company says, its lowest rate for any Gemini model (though 2 percent still isn’t zero, and when thousands of agents work together, 2 percent is still quite a few agents that could go rogue).
Google also runs a separate monitor that reads the agent’s reasoning and actions as it works and blocks unintended workarounds. The company says it ran that monitor during training without penalizing the model for what it was thinking, so its reasoning stays readable.
According to Google, Argon also leads Gray Swan’s indirect prompt injection benchmark, with attacks succeeding 0.7 percent of the time across 15 adaptive attempts.
Developers have until November 30 to test Argon at the introductory rate. After that, Argon and Opus 5.5 cost the same per token.
