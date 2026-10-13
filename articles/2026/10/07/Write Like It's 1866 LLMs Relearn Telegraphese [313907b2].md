---
id: "313907b2dbd81109"
title: "Write Like It's 1866: LLMs Relearn Telegraphese"
url: "https://fiveminutesforward.com/post/2026-10-04-telegraph-test"
source: "Five Minutes Forward"
domain: "fiveminutesforward.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-07T12:04:36Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Theory42"]
language: "en"
summary: "Everything below is reproducible — harness, frozen ledgers, one-click notebook: github.com/Travis42/telegraph-test.\nThe Telegraph era, where every word was metered\nIn 1866, sending a message across the new transatlantic cable cost $100 — for ten words1$10 a word, ten-word minimum, roughly $2,600 in today’s money. . That’s real money today; it was serious money then. Telegraph companies charged…"
tags: []
orgs: []
topics: ["models & research", "policy & regulation", "agents & coding", "jobs & society"]
content_source: "fulltext"
word_count: 2310
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49991580"
score: 98
comments: 58
community: "Hacker News"
---

# Write Like It's 1866: LLMs Relearn Telegraphese

Five Minutes Forward · Theory42 · 2026-10-07

Everything below is reproducible — harness, frozen ledgers, one-click notebook: github.com/Travis42/telegraph-test.
The Telegraph era, where every word was metered
In 1866, sending a message across the new transatlantic cable cost $100 — for ten words1$10 a word, ten-word minimum, roughly $2,600 in today’s money. . That’s real money today; it was serious money then. Telegraph companies charged per word, and an entire industry grew out of that price structure.
Two compression strategies emerged, and they map onto two very different technologies:
Codebooks. Publishers sold massive commercial code dictionaries — Bentley’s ABC Telegraphic Code ran to a thousand pages mapping entire business phrases to single code words.
OTTER
…might mean
*steamship arrived, cargo intact, remit balance.*
Firms could cut a 40-word negotiation to a 6-word coded exchange. The codebook is a substitution technology: the message exists in full prose, and a dictionary renames chunks of it.
Cablese. The operators and correspondents evolved a written format like:
"ARRIVE TUESDAY BRING FUNDS STOP CONFIRM WIFE SAILS FRIDAY."
This disciplined style saved words without losing meaning, and it was emergent from the cost of the medium.
Over time, this format faded as new technologies like the telephone, fax, email, made the per-word cost premium collapse. Telegraphese kind of survives wherever metering in terms of cost or just the time it takes to tap out a message is still onerous: 160-character SMS begat a whole new abbreviation culture; early Twitter did it again.
Well guess what?
Tokens are metered words again
An LLM API bill is a telegraph bill. You pay per token.
So we ran both strategies from ye olden days against modern models:
The Codebook: take existing text, substitute code words from a fixed dictionary.
Result: about 10% savings. Most prose isn’t dictionary-shaped, and the substitution can’t remove words the author already wrote — it can only rename them.
Cablese
Instruct the model, “Write a complete record in telegraphese; drop articles and filler; abbreviate; keep every fact, number, and proper noun verbatim — in lowercase, not all caps.”
Numbers from a 50-passage, ~1,300-question benchmark:
Cross-family matrix (readers = foreign models answering from GLM-5.3-Flash’s records; writers = GLM-5.3-Flash answering from theirs)2Savings shown use the lowercase instruction, on each provider’s own meter. Without that word, models write cablese in ALL CAPS and the styling costs 14–19 points: gemma 25.0%, qwen 29.8%, GLM 33.9%. *gpt-5-mini cannot disable reasoning, and compression makes it think — its writes bill about double plain. The one family where this technique does not pay. :
GLM-5.3-Flash itself: 48.4% savings with the lowercase instruction, in-family recovery 1.09.3Readers answer 694 anchored questions per condition; writers’ records are read by GLM-5.3-Flash — every GLM call in every run in this post is glm-5.3-flash, the fast variant on the z.ai coding plan. No comparison in the matrix favors plaintext; every ratio sits at 0.99–1.10.
The condition ladder — same questions, one variable at a time:
Downstream models, including four families never shown an example, answer questions from the compressed records as well as or better than from plaintext — recovery ratios 0.99–1.10, where 1.00 means “exactly as good as plaintext.” The register is not a construct we invented (LLMs were handed compressed records cold and read them at parity); the capability was already in the weights, inherited from a century and a half of people writing under metered bandwidth.
- The retention result, interpreted. Cablese records read slightly better than regular responses (the ladder’s 1.09), most likely because compression suppresses copy-the-record phrasing that strict grading penalizes.
- Every model tested can do this. It’s in their training data — but compression varies from 40% to 49% under the identical lowercase instruction (25–34% if models default to ALL CAPS). That per-model spread is worth knowing if you want to use this technique, and it is knowable.
- There is a slight information reconstruction cost, but only when transcribing individual answers for users. If the consumer is a model — or the record is simply re-read — the readback ratios are the ones that apply, and they’re all ≥0.99.4Statistically: no comparison favors plaintext; in-family read-back p<0.0001, decoded-record p=0.03.
- The storage loop’s economics, both ledgers. Stored text: the expansion hands back about a third of the write-side savings (mean 155 vs 117 vs 260 tokens), so the expanded archive sits well under plaintext. But producing it costs one extra pass — ~312 tokens in + out — which is more than the write-side savings. Output tokens alone, the loop never wins (272 vs 260); it pays through cheaper machine reads (117 vs 260 input each), breaking even after a read or two. If humans are the main reader, write plain.
Notice what this adds up to:
No new hardware, no training, no API change, one sentence of instruction. Either your agents get nearly twice the context at the compressed end, or the same work for half the output bill. It is a large optimization that is verified, and as far as I can tell, just not happening.
When is compression free?
It depends on where the compression step sits. Compress while the model is still composing (answers in cablese, 0.81, partly recoverable at 0.86) and you pay a register tax. But if you compress after the content is settled, into a record a machine will read (1.08–1.09), there is nothing to pay.
Cablese belongs between “content settled” and “machine consumption”: scratchpads, memory stores, agent-to-agent handoffs. Nowhere a model is still mid-thought.
Models whose reasoning you can disable bill the compression clean. gpt-5-mini’s reasoning is mandatory (the API refuses to turn it off), and cablese makes it think roughly 3× harder — its writes cost double despite the shorter text. The lesson is that you must compress with models whose thinking you can control.
So:
- The expensive half of every LLM bill is optional overhead for machine-consumed text. Output tokens cost 3–5× input tokens, and for traffic a model writes for another model, half of it comes off at any major API — one sentence of instruction, no training, no setup (mandatory-reasoning models excepted).
- Agent memory just got nearly twice as capacious. Store scratchpads and summaries in cablese: models — the intended readers — read them at parity or better, in every family tested. Expand back to plaintext only when a human actually looks, and even then the archive costs less than plain.
- Model choice matters as much as the instruction. The identical instruction compresses gemma’s records by 40% and Qwen’s by 49% on their own meters — compressibility is a measurable, per-model property, and at scale that spread is real money. The Telegraph Test is a way of determining how good models are at this kind of compression.
- It probably can’t be walled off. The register lives in the training data of every family tested. A lab that suppresses it in a frontier model just moves the advantage to open models that still carry it.
- Auditability survives the compression. Unlike the emergent agent protocols, cablese is human-readable, fixed by convention, and decodable on demand — the tokens shrink without losing the audit trail.
Why does this work across models?
The register is already in the weights — an artifact of training data. Telegraph cables, codebooks, and cablese’s cousins across the broader “telegram style” family (headlinese, teletype style, note-taking, SMS abbreviation) are all in the “all of human knowledge” corpora that most models share. Two observations back this. First, models produce fluent, conventionally-shaped cablese from a one-sentence instruction — no examples, no codebook. Second, the readers in the cross-family matrix never saw even that instruction: they were handed compressed records cold and read them at parity, across four model families. Shared zero-shot fluency like that is hard to explain unless the convention is latent in shared human text.5Boring caveat: I have not run the strict control — the same compression instruction stripped of the historical framing (“write as tersely as possible”) — to test whether generic terseness produces equally legible compression. The claim here is strong evidence of a latent register, but at its core this is an educated guess.
Haven’t we seen LLMs do this already?
Yes, BabelTele (arXiv, June 2026) demonstrated that LLMs can encode text in compact, non-standard forms — omnilingual word fragments, symbols, emoji — that other models recover with high fidelity (99.5% semantic fidelity at 27.9% of original length, by their metrics), including cross-model transfer, agent memory, and multi-agent communication. It proves the general phenomenon: human readability is not a requirement for model-to-model text.
Further, researchers running populations of LLM agents under token budgets have watched the same thing emerge spontaneously: put agents under compression pressure and they negotiate compact protocols instead of passing full English back and forth. GLOSSOGEN found it’s the budget pressure that produces the new communication system. Another paper, From Token Efficiency to Oversight Evasion, shows agent populations developing emergent languages under efficiency pressure.
Other work has agents inventing symbolic languages that cut tokens 3–6× at steady accuracy, and at the far end, frameworks that skip text entirely and pass raw embedding vectors between agents.
What’s already shipped
- Terse (terseai.org). A product selling “telegraph compression” for your prompts: rule-based stripping of articles and pronouns on the input side. The fidelity is asserted, not measured.
- Caveman (github.com/juliusbrussee/caveman). A Claude Code skill that makes the model answer in terse fragments. It has 100k+ stars on Github.
I think there’s more to do here, though.
So why does Cablese matter then?
If models can create something like a 6x compression on their own, why bother with a mere 2×? Here’s why:
These emergent protocols share a property profile: dense, efficient, portable between models (other LLMs can learn them in-context), but they are:
- unstable — they drift as negotiation continues
- illegible/unreadable to people
By contrast, Cablese is:
- a known standard, more deterministic, generalizeable, with no setup or initial negotiation
- readable, therefore auditable
In truth, the two techniques are different points on the compression/auditability frontier, and where your workload sits on that frontier should pick the point.
The Telegraph Test — measuring how models use Cablese
What the test measures: A model is given a passage and a fixed set of questions with short, checkable answers — a date, a name, a count. It answers from one version of the information: the original passage, a plaintext summary, a cablese summary, or a cablese summary expanded back to plaintext. An answer is right if it matches the expected answer under fixed string rules — no judge, no discretion. Every score is then divided by the score of its own plaintext control, so 1.00 always means “exactly as good as plain English.” Above 1.00 is better; below is worse.
What the percentages measure: comprehension against facts, presentation varied. Each passage comes with ~24 questions whose short expected answers (a date, a name, a count) are verified as extractable from the source text — anything else is discarded before testing. A model receives one presentation — the full passage, a plaintext record, a cablese record, or a decoded record — and answers each question in a few words. An answer is correct when its overlap with the expected answer clears a fixed 0.8 threshold under deterministic, normalized matching: no exact-match pedantry, no judge, no discretion. Every comparison in this post holds the questions and grader constant and changes only what the model gets to read.
Why isn’t the plaintext baseline 100%? Answering questions about an uncompressed passage in plaintext scores ~91%. The shortfall has three sources: strict grading (a correct answer worded differently scores as a miss — deterministic matching has no judgment, and no model sits in the judge’s seat); ambiguous questions (some have more than one defensible answer); and genuine misses (facts the model actually fails to extract). We can’t split those three without a judge, so we don’t try — and the design doesn’t need it: questions and grader are held fixed across conditions, so the baseline shortfall cancels in every comparison. That is why the benchmark’s primary numbers are ratios against each condition’s own plain control, where 1.00 means as good as plaintext.
A note on how to read the numbers in this post. The comparisons are paired — the same questions answered under both conditions — and tested with McNemar’s test. In plain words: ignore the questions both conditions got right or both got wrong (they carry no signal about which is better) and look only at the exchanges — questions where exactly one condition succeeded. If the conditions were truly equal, those wins would split like coin flips; a lopsided split (say 69 wins to 45) that had only a 3% chance of arising by luck is evidence of a real difference. That is all the p-values here mean. So every claim in this post is a paired comparison, and the register’s cost is the gap between the pair — zero-to-negative in both directions we measured.
The Telegraph Test answers three questions about any model, with the same frozen passage bank, the same anchored questions, and the same deterministic grader every time:
- How lean does it write? Given the identical cablese instruction, how much shorter is its record than its plaintext record?
- Can others read it? When a different model family answers questions using that compressed record, does accuracy hold? (Legibility — the difference between a shared register and a private idiolect.)
- What does each use cost? Read-back for machines, transcription for humans — measured separately, because they behave differently.
Nobody can know these numbers without running the experiment — a model release doesn’t come with a “writes lean cablese” spec-sheet row — and models are released monthly. That’s what the benchmark is for: an afternoon of compute per new model, and the property becomes a number on a table instead of folklore.
Where it lives: github.com/Travis42/telegraph-test
