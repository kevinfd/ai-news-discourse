---
id: "8c10cc5a563e4a1e"
title: "Show HN: Deslop skill based on corpus-linguistics and psycholinguistics research"
url: "https://github.com/etodanik/deslop"
link: "https://github.com/etodanik/deslop"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-16T12:41:48Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["dannypovolotski"]
language: "en"
summary: "I vibed this deslop skill because I was getting increasingly annoyed that deslop skills for prose relied either on fitting prose into an overly restrictive format (simple-english and iso-24495) or telling AI to rewrite something without providing any tools in the skill to measure the outcome (which more often than not resulted in one slop being replaced with another). This skill is based on…"
tags: []
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 655
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50516995"
score: 13
comments: 4
community: "Hacker News"
---

# Show HN: Deslop skill based on corpus-linguistics and psycholinguistics research

GitHub · dannypovolotski · 2026-11-16

deslop is a Claude skill that revises a draft to remove the fingerprints of LLM-generated prose. Its rules come from corpus-linguistics and psycholinguistics research comparing human and model text, and they were checked against three public corpora in which humans and models answered the same prompts.
The research behind it is in references/research.md.
A client email in Claude's default style (228 words, 3 Claude tells) opens like this:
I wanted to reach out with an important update on your website launch. We're now targeting March 17 instead of the original March 3 date, a delay of two weeks.
The reason for the delay is that the payment provider's API review is taking longer than we anticipated. Because secure payment processing is a critical part of the site, we can't go live until the review is complete.
After one pass (132 words, 0 Claude tells, no facts dropped):
Your website launch will slip two weeks, from March 3 to March 17. The payment provider's API review is taking longer than we planned, and we can't go live with payments until it's done.
Copy this folder into your skills directory:
cp -r deslop ~/.claude/skills/deslop
Then ask Claude to "deslop this", "make this sound less like AI", or "run a slop pass" on a draft.
Most de-slop skills hand the model a list of things to avoid and ask for a rewrite. Without a check, the rewrite often swaps one tell for another: in this repo's tests, a Claude reviser left every Claude tell in place (6.2 per answer before and after) until a check listed them sentence by sentence. deslop scans each pass before and after, and it makes its tell lists from data you can regenerate as models change. In Graphite's data, 55–72% of a model family's tells turn over between releases.
Plain-language standards such as Simple English and ISO 24495 fit text to one format. That's right for documents that must meet a standard, but uniform prose is a model signal too: human sentence lengths have a long tail that current models lack. deslop aims for the range a good human writer shows in the genre instead.
- Pick the genre and reader (chat, email, docs, code, essay, academic, fiction, marketing).
- Scan the draft. The scanner lists each problem with the sentence it's in, the reviser's own model-family tells, and the reply's length against the question.
- Revise from the outside in: content, structure, sentence grammar, sentence length, word choice, punctuation.
- Re-scan against the original. This lists new flags, tells the revision added, and dropped facts (numbers, code, links, negations, hedges).
- Stop once the text is in the human range. A second tells-only pass made answers worse in a blind test (5–0).
SKILL.md has the full workflow.
The core tools need only Python 3:
python3 scripts/slop_scan.py draft.md --agent --self claude --genre chat --prompt question.txt
python3 scripts/slop_scan.py revised.md --before draft.md --self claude --genre chat
python3 scripts/check_invariants.py draft.md revised.md
python3 scripts/slop_scan.py --list
The optional extras need a Python 3.12 venv with spaCy, torch, transformers and sentence-transformers in .venv. They are deep_scan.py (Biber Dimension 1, semantic redundancy, GPT-2 surprisal), --spacy parser metrics, and judge_prompt.py (sycophancy rubrics for a judge subagent).
references/tools.md lists every flag and metric with the evidence for it.
The rules come from Reinhart et al. (2025), Terčon & Dobrovoljc (2025), Clark, Martin & Mahowald (2026), Graphite's "AI Tells" (2026), HC3 (Guo et al. 2023) and ELEPHANT (Cheng et al. 2026). references/research.md lists every source with its numbers, including which checks held across every model generation and which ones flipped.
The skill's code and docs are released under the MIT License (see LICENSE.md). references/data/ includes Graphite measurements under CC BY 4.0, with credit. evals/ includes short excerpts from HC3 (Guo et al. 2023, CC BY-SA 4.0) and ELEPHANT (Cheng et al. 2026, CC0) for the bench and the judge check. sources/raw/ and sources/papers/ hold third-party text for local analysis only. Don't redistribute them.
