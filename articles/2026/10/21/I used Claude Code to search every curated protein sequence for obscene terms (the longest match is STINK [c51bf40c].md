---
id: "c51bf40c83cd3e37"
title: "I used Claude Code to search every curated protein sequence for obscene terms (the longest match is STINK TAINT)"
url: "https://reddit.com/r/ClaudeAI/comments/1xbp9yl/i_used_claude_code_to_search_every_curated"
link: "https://reddit.com/r/ClaudeAI/comments/1xbp9yl/i_used_claude_code_to_search_every_curated"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T14:51:22Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["leikai"]
language: "en"
summary: "Proteins are spelled with 20 letters of the English alphabet, one per amino acid. Obviously I wanted to know which cuss words were hidden in the sequences, and Urban Dictionary was the biggest list of them I could get. I had Claude Code search for them with the spaces stripped out (so STINK TAINT = STINKTAINT). The protein set is UniProt Swiss-Prot: 575K hand-curated proteins across every…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Hugging Face"]
topics: ["health & science", "search & media"]
content_source: "post"
word_count: 452
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbp9yl/i_used_claude_code_to_search_every_curated/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude Code to search every curated protein sequence for obscene terms (the longest match is STINK TAINT)

Reddit · leikai · 2026-10-21

Proteins are spelled with 20 letters of the English alphabet, one per amino acid. Obviously I wanted to know which cuss words were hidden in the sequences, and Urban Dictionary was the biggest list of them I could get. I had Claude Code search for them with the spaces stripped out (so STINK TAINT = STINKTAINT). The protein set is UniProt Swiss-Prot: 575K hand-curated proteins across every organism, 208.5M amino acids. Of the UD terms searched, 191,876 appear verbatim in at least one protein. Among the short matches, human sperm proteins kept coming up. Sperm microtubule associated protein 2-like contains PEEPEE , spermatogenesis-associated protein 32 contains WANK , and sperm-associated antigen 7 contains FAPS . Some of the best of the 19,184 matches seven letters and up: Term Urban Dictionary definition Protein, organism Residues STINK TAINT "When someone has a stink, and you don't know if it from the front or the back." Uncharacterized protein 467R , an insect virus 276–285 EAGLE FIST "An abrupt and unexpected fisting that causes the recipient to screech like an eagle while the fister screams 'Murica!" MTTP , human 808–816 STARGASM "Having an orgasm from anal sex or anal play. Comes from the [chocolate starfish] nickname given to the asshole." murA , Rhodospirillum rubrum , a bacterium 322–329 SHITTITS "An exclamatory phrase conveying sentiments of astonishment, surprise, anger, annoyance, bewilderment or other general feelings of shock." Protein SIX6OS1 , human 338–345 PISSANTS "The burning, tingling sensation one feels in the penis while urinating after ejaculation." At1g53550 , Arabidopsis thaliana 351–358 PITCLIT "when a fat girl wears a strapless top and the fat between her arm and shoulders forms a vagina looking fold." Maturase K , Angiopteris evecta , a fern 354–360 ASSPISS "When only pure juicy liquid comes squirtting out your anus." Protein piccolo , human 4022–4028 PEEFART "When urination is so strong and intense it causes one to fart" BSH , Arabidopsis thaliana 127–133 TITSMAS "The first spring day, in which girls first and finally show off some cleavage after a long winter. Men think of this day as something like, or better than, Christmas." azaA , Aspergillus niger , a mold 1183–1189 The word list started as 3.5M UD spellings from four public sources. Stripping spaces and punctuation, dropping terms containing B, J, O, U, X, or Z, which are not among the 20 standard amino-acid codes, and requiring four letters or more left 742K terms. Claude Code wrote the pipeline, the collector for Urban Dictionary's public listings, and a check that the protein sequence at each reported position really spells the term. Definitions quoted from UD via the Hugging Face export, Bierner word list, 2016 archive, and UD's public listings; shared under CC-BY-SA-4.0.
