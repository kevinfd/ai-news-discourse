---
id: "d7cc448f37f022a5"
title: "Blind listening test: 62 people compared 8-bar piano loops written by 8 LLMs (Gemini, Claude, Qwen, Kimi, Grok, GPT-6.1, DeepSeek, Llama). Interim results"
url: "https://reddit.com/r/artificial/comments/1xoz9sv/blind_listening_test_62_people_compared_8bar"
link: "https://reddit.com/r/artificial/comments/1xoz9sv/blind_listening_test_62_people_compared_8bar"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T00:41:21Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["antiochIst"]
language: "en"
summary: "I ran this study. Short version: Gemini 4 Argon's loops were preferred most often (66% of pairings) and it was the only model that held up across all four styles. Claude Opus 5.5 was second (61%). Llama 4 Maverick was a distant last (27%). The five in between can't be separated yet. 62 listeners, 514 blind pairwise judgments so far. Listen first. The best-scoring loop across all 20 prompts from…"
tags: ["r/artificial"]
orgs: ["Anthropic", "Google", "Meta", "xAI", "DeepSeek", "Alibaba", "OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 850
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xoz9sv/blind_listening_test_62_people_compared_8bar/"
score: null
comments: null
community: "r/artificial"
---

# Blind listening test: 62 people compared 8-bar piano loops written by 8 LLMs (Gemini, Claude, Qwen, Kimi, Grok, GPT-6.1, DeepSeek, Llama). Interim results

Reddit · antiochIst · 2026-11-06

I ran this study. Short version: Gemini 4 Argon's loops were preferred most often (66% of pairings) and it was the only model that held up across all four styles. Claude Opus 5.5 was second (61%). Llama 4 Maverick was a distant last (27%). The five in between can't be separated yet. 62 listeners, 514 blind pairwise judgments so far. Listen first. The best-scoring loop across all 20 prompts from each of the four strongest models (Claude's is tied with one other), and the worst loop from the last-place model. Exactly as the raters heard them: same piano, same settings, ~20 s each, direct audio files. Hand-picked, so not a representative sample: Grok 4.7 — brief "Gospel-tinged and warm, with full, voiced chords". Chosen in 9 of its 10 pairings on this brief, the strongest single loop in the published set, from a model that is 48% overall. Gemini 4 Argon — "Hypnotic and repetitive, built on one insistent figure". 8 of 9. Kimi K3 — "Warm and optimistic, the kind of loop that makes you nod". 8 of 9. Claude Opus 5.5 — "Moody and haunting, with a sense of unease". 5 of 6. Llama 4 Maverick — the same "Moody and haunting" brief as the Claude one. 0 of 9. Blind version, 100-second video : four of the loops with the names hidden, reveal at the end. Question: 8 flagship LLMs each wrote 20 short piano loops as note lists, one per prompt, with a single attempt per prompt and no retries or revisions. Which model's loops do ordinary listeners prefer? This is about symbolic composition (notes), not audio-generation models, and not full songs. Setup Same 20 prompts to every model: 8 bars of 4/4 solo piano, 80–110 BPM, output as a JSON list of notes (pitch, start, duration, velocity). One line of musical direction varied, 5 prompts in each of 4 styles (dark/emotional, uplifting/catchy, soulful/jazzy, minimal/hypnotic). One answer per model per prompt. No retries, no system prompt, no examples, vendor default sampling. Invalid output was rejected, never repaired: 158 of 160 outputs were valid (Qwen lost 2 to reasoning overflow, the rest were 20/20). Every valid loop was rendered through the same sampled grand piano (Salamander, CC-BY) at fixed settings, no normalisation, so only the notes differ. 62 paid, untrained listeners heard two loops written for the same prompt, blind, and picked one. Each listener saw each prompt at most once and any one model at most 7 times. Interim results, 514 of 1,638 planned pairwise judgments (win rate over all pairings; 95% interval from a bootstrap resampling listeners) Model Won Lost Win rate 95% CI Gemini 4 Argon 84 43 66% 57–75 Claude Opus 5.5 77 49 61% 51–70 Qwen 3.8 Max 63 51 55% 45–65 Kimi K3 70 61 53% 44–62 Grok 4.7 62 66 48% 39–57 DeepSeek V4 Pro 60 70 46% 37–55 GPT-6.1 Terra Pro 60 70 46% 37–55 Llama 4 Maverick 38 104 27% 19–35 Gemini ranked first in 79% of bootstrap replicates, Claude in 18%. Gemini has a winning record against each of the other seven (12–7 vs Claude), but no single series is large enough to prove it beats any one of them. Llama was last in 100% of replicates and was shut out (zero wins) on 4 of the 20 prompts. The middle five can't be ordered yet; their intervals all include 50% and each other. Side of presentation didn't matter (left chosen 48%). By style: Gemini was 62–68% in all four. Qwen was 72% on dark prompts but 42% on uplifting. Grok 32% on uplifting, DeepSeek 33% on soulful, Claude best on soulful at 70%. Cells are 19–45 judgments, so treat these as hints. What the compositions look like: the leaders write 110–127 notes per 8 bars over about four octaves. DeepSeek writes 71 notes over two octaves. Llama writes 52 notes over 17 semitones with ~1% of notes below C3, basically no bass register at all. Gemini writes with the flattest dynamics (velocity SD 6.7) and the longest notes. What listeners went for: across all judgments the preferred loop had the wider pitch range 62% of the time (CI 57–67), more notes 59%, more bass 58%, and was the louder of the two 56%. The preferred loop had the larger velocity variation only 46% of the time. These are associations between correlated properties, not causes. Busier loops also render louder through a fixed piano, and the design can't separate the two. Limitations, honestly: interim at 31%; one generation per prompt, so within-model variance isn't measured; lay listeners, not musicians; one piano sound; the question wording changed after the first 96 judgments (re-running on the other 418 gives the same top two and the same last place); Llama was served by a third-party host at FP8, the only reduced-precision endpoint, so its result applies to that configuration. Analysis code was written with help from Claude, which is one of the arms; the judgments are human and the analysis is deterministic from the data. Happy to answer questions about the method. What would you change for the next round?
