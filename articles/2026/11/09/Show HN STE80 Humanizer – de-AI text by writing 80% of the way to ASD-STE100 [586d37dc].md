---
id: "586d37dc594556b4"
title: "Show HN: STE80 Humanizer – de-AI text by writing 80% of the way to ASD-STE100"
url: "https://github.com/Dodaios/ste80-humanizer"
link: "https://github.com/Dodaios/ste80-humanizer"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T18:05:44Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Dodaios"]
language: "en"
summary: "STE80 Humanizer makes AI-written text read like a careful person wrote it, without changing what it says. It combines two methods:\n- The humanizer method. Remove the 26 tells from Wikipedia's Signs of AI writing, in the catalog of blader/humanizer.\n- Karpathy's STE80 method. Rebuild the sentences \"80% of the way to ASD-STE100\", the controlled English of aircraft maintenance…"
tags: []
orgs: ["OpenAI", "Anthropic", "Cursor"]
topics: ["agents & coding"]
content_source: "fulltext"
word_count: 1293
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50429144"
score: 96
comments: 33
community: "Hacker News"
---

# Show HN: STE80 Humanizer – de-AI text by writing 80% of the way to ASD-STE100

GitHub · Dodaios · 2026-11-09

STE80 Humanizer makes AI-written text read like a careful person wrote it, without changing what it says. It combines two methods:
- The humanizer method. Remove the 26 tells from Wikipedia's Signs of AI writing, in the catalog of blader/humanizer.
- Karpathy's STE80 method. Rebuild the sentences "80% of the way to ASD-STE100", the controlled English of aircraft maintenance manuals.
Before:
Great question! Kubernetes liveness probes are a powerful mechanism that enables the kubelet to determine whether a container is healthy — and it's not just a health check, it's your first line of defense. When a probe fails, the container will be automatically restarted by the kubelet, ensuring that your application remains available. However, it's important to note that misconfigured probes could potentially cause cascading restarts, so parameters like initialDelaySeconds and failureThreshold should be carefully tuned.
Get this right, and your cluster heals itself.
After:
A liveness probe tells the kubelet if a container is healthy. If the probe fails, the kubelet restarts the container. This keeps the application available.
A bad probe can also cause many restarts. For example, a timeout that is too short makes healthy containers fail the probe. To prevent this, set initialDelaySeconds and failureThreshold to values that fit your application.
The goal is text that people read easily. Getting past AI detectors is not a goal.
Most humanizers only remove phrases. The text loses "Great question!" and "seamless", but it keeps long sentences that carry three ideas, hide the actor and stack hedges. It still reads like AI. You can see it in the worked example in SKILL.md:
On 2 October 2026, Andrej Karpathy posted tips for one problem: as LLMs do more of the work, people spend more time reading and understanding what the models produce. His first tip:
Ask your LLM to explain something in ASD-STE100, it's a controlled language specification originally developed for aerospace maintenance documentation. LLMs well-versed in this language and it comes with heavy constraints on clean writing style that I often find a lot more readable. Sometimes I've tried to soften it a bit e.g. ask for "80% of the way to ASD-STE100" because the spec is quite stringent.
The post then goes up a ladder: diagrams, then HTML pages, then explainer videos. His conclusion is that our work moves "up the abstractions into oversight and understanding". Clear output is the bottleneck, and writing is the first step.
The STE overview graphic from Karpathy's post. Click to enlarge. Note: a later fact check found errors in the dictionary panel (D). In ASD-STE100 Issue 9, "approximately" is approved, "TEST" is approved only as a noun (not as a verb), and there is no entry for "in order to". This skill follows Issue 9.
ASD-STE100 (Simplified Technical English) is from the 1980s aerospace industry. It was made for mechanics whose first language is not English, because a misread step on an aircraft can kill. Its rules:
- 20 words per instruction and 25 per description
- one instruction per sentence
- active voice and simple tenses
- one meaning per word, with about 900 approved words
- one topic per paragraph, and six sentences at most
Why "80%"? At 100%, "check" and "test" are nouns only, "may" and "should" are banned and many common words are not allowed. Normal prose sounds stiff. At 80%, you keep the full structure and only as much vocabulary as still sounds natural:
Karpathy's tip is about readability. It does not remove chatbot phrases, so Pass 1 does that first.
SKILL.md has two numbered lists:
- §1 to §26: the AI tells (Pass 1).
- S1 to S15: the STE80 structure rules (Pass 2).
Both lists are compact tables with a short example. Pass 2 says what changes between 80% and Strict. The full entries, with Watch for, Problem, Before and After, are in references/ai-tells.md and references/ste80-rules.md. Weak alone means: act only if other tells are near. The skill reports its edits by number, for example "§1, §8, S2", so you can look each one up.
Once installed, the skill answers to /ste80-humanizer. It also starts by itself when you ask to humanize, simplify or de-AI a text, or ask for STE.
npx skills add Dodaios/ste80-humanizer
Global install for one agent, or for all of them:
npx skills add Dodaios/ste80-humanizer --global --agent claude-code
npx skills add Dodaios/ste80-humanizer --global --agent codex
npx skills add Dodaios/ste80-humanizer --global --agent cursor
npx skills add Dodaios/ste80-humanizer --global --agent '*'
Without --global, the skill goes into the current project only. The skills CLI from Vercel works with Claude Code, Codex, Cursor, OpenCode and many more agents.
/plugin marketplace add Dodaios/ste80-humanizer
/plugin install ste80-humanizer@ste80-humanizer
Download this repo as a ZIP (Code → Download ZIP). Upload it in Settings → Capabilities → Skills.
/ste80-humanizer
<paste text>
Or just ask:
This sounds like ChatGPT wrote it. Make it sound like a person.
Rewrite this README 80% of the way to ASD-STE100.
Explain how TLS handshakes work in STE.
Light touch: just remove the AI stuff from docs/intro.md.
Convert docs/runbook.md to strict STE.
Does this email sound like AI? Just tell me, don't rewrite it.
Match your voice. Add a sample of your own writing. The skill then matches your sentence length, words and punctuation.
Fidelity first. The skill keeps every fact, keeps "may" as "may", keeps "40+" as "40+", adds nothing and flags contradictions in the source. In our tests, this was the clearest difference from a plain prompt (see Tests).
More examples: references/ste80-rules.md. Full strict rules and a checklist: references/strict-mode.md. More than 100 plain-word swaps: references/word-swaps.md.
scripts/ste_check.py is a small Python linter with no dependencies. It flags many Pass 1 tells, such as not-X-but-Y, chatbot phrases, run-ups, fake depth, stacked hedges, vague authority and association, "-ing" riders, inflated claims, AI words, hyphen pairs and curly quotes. It also flags the measurable Pass 2 rules: sentence and paragraph length, semicolons, dashes, passive voice, perfect and progressive tenses, "-ing" forms and phrasal verbs.
python scripts/ste_check.py README.md
python scripts/ste_check.py --strict docs/runbook.md
cat draft.txt | python scripts/ste_check.py -
It is a heuristic, not an AI detector and not a compliance checker.
evals/ has four cases in the claude plugin eval format: a README rewrite, an explanation from scratch, a strict runbook and a casual LinkedIn post that does not mention STE. Run them with claude plugin eval . --allow-tools Write,Edit,Bash.
What we saw: when the prompt names ASD-STE100, the base model already gets the style mostly right. The skill made the difference in fidelity. In the LinkedIn rewrite, the run without the skill invented a quote and changed "40+ customers" to "40-odd". The run with the skill kept every fact. In the README rewrite, it kept "you may need to" and flagged a contradiction in the source. These are small tests, so treat them as a hint, not proof.
- STE is for clear explanatory text. For fiction, speeches and brand copy, the skill does Pass 1 only.
- STE is an English standard. For other languages, the skill applies the tells and the structure rules, but not the English word lists.
- "STE style" is not "STE compliant." Compliance needs the official dictionary, trained writers and review.
- Andrej Karpathy on X, 2 October 2026: https://x.com/karpathy/status/2105819303471976479
- ASD-STE100 Issue 9 (2025): https://www.asd-ste100.org
- Wikipedia, Signs of AI writing (WikiProject AI Cleanup)
- blader/humanizer by Siqi Chen (MIT). Pass 1 follows its 26-pattern catalog and order, with new examples. Its license notice is in THIRD_PARTY_NOTICES.md.
- Hacker News discussion of STE skills (July 2026): https://news.ycombinator.com/item?id=49114639
This skill does not contain the ASD-STE100 specification or its dictionary. The STE rules are paraphrased and simplified. ASD-STE100 and Simplified Technical English are trademarks of ASD (AeroSpace, Security and Defence Industries Association of Europe). This project is not affiliated with or endorsed by ASD.
