---
id: "e6c298aee2a3d555"
title: "I fixed my tiny TTS by editing the weights directly, no retraining"
url: "https://reddit.com/r/LocalLLaMA/comments/1xou096/i_fixed_my_tiny_tts_by_editing_the_weights"
link: "https://reddit.com/r/LocalLLaMA/comments/1xou096/i_fixed_my_tiny_tts_by_editing_the_weights"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T20:54:52Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["N1kuson"]
language: "en"
summary: "I'm building Silencio-2, a small finetune of Kyutai's Pocket TTS. It adds inline tags for emotions ( <happy> , <sad> , <angry> , <fear> , <surprised> , <whisper> ) and for sounds like [laugh] . I simply didn't have enough tagged data to make them stable. <happy> worked, the others were hit or miss, and <whisper> gave an actual whisper in about 1 of 5 takes. So instead of collecting more data, I…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 657
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xou096/i_fixed_my_tiny_tts_by_editing_the_weights/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I fixed my tiny TTS by editing the weights directly, no retraining

Reddit · N1kuson · 2026-11-05

I'm building Silencio-2, a small finetune of Kyutai's Pocket TTS. It adds inline tags for emotions ( <happy> , <sad> , <angry> , <fear> , <surprised> , <whisper> ) and for sounds like [laugh] . I simply didn't have enough tagged data to make them stable. <happy> worked, the others were hit or miss, and <whisper> gave an actual whisper in about 1 of 5 takes. So instead of collecting more data, I tried the approach from this post on weight-space programming : an LLM agent inspects the model's weights, finds the mechanism behind the failure, edits a small number of weights directly, and keeps an edit only if it improves a held-out set. Here the agent was Claude (Opus 5.5). It wrote the probes, ran the experiments and built the edit. I steered and listened to the results. What we found The tag embeddings barely moved from the words they were initialized from: 60–80% cosine similarity to "sad", "whisper" and so on. Their norm doesn't matter either, because LayerNorm sits right before attention. An attention probe showed that audio frames attend to <happy> 100–3000× more than to an average text token. For the other tags it's only 1–10×. The model seems to know what the tags mean, it just barely reads them. Causal check: I boosted attention to <whisper> at inference time, directly in the activations (×30, all heads). That gave a whisper in 62% of takes with clean words. ×100 breaks speech. Boosting only the 3 "reader" heads did almost nothing. The edit Each layer gets one rank-1 term added to W_K: ΔW_K = D · zᵀ z is a linear detector for the tag token, fit by least squares. It outputs 1.00 on the tag and 0 ± 0.03 everywhere else. D is a key shift in the slowest RoPE pairs, which are almost position-independent. It points along the mean query of the audio frames and is scaled by ln(gain). Gains per tag: sad/fear/surprised ×5, angry ×3, whisper ×10. <happy> and the sound tags are untouched. That changes about 524k weights (3.4% of the transformer), but there are only about 5k free parameters and zero gradient steps. Results on the held-out test set (unseen phrases, unseen seeds, 2 unseen voices) before after <whisper> actually whispers 5/24 22/24 …and the words are clean 5/24 10/24 Emotion separability, 7 classes (chance 0.14) 0.45 0.71 WER, untagged speech 0.006 0.006 WER, sound tags / sound length 0.007 / 0.81 s 0.014 / 0.84 s All metrics are proxies: WER comes from Whisper base, whisper detection uses the share of voiced frames (pyin), and separability is a nearest-centroid classifier on Whisper encoder features after subtracting the mean for each (voice, phrase, seed) group. There's no emotion classifier in the loop, so in the end your ears decide. But it's not a stable upgrade, and the metrics don't show everything Some takes glitch. The pitch or tone of the voice suddenly jumps mid-sentence, or the delivery changes halfway through. Some whispers slur words (whisper WER 0.18), and one of 24 collapsed into mumbling. <surprised> went up about 4 semitones in pitch, which sometimes sounds over the top. Untagged outputs aren't bit-identical to the old model. The detector leaks about 0.001, which acts like a seed change. Quality is the same. What didn't work Pushing tag embeddings away from their seed words: no change beyond noise. Applying the boost only to audio-frame queries and keeping text tokens out of it: the effect mostly disappears. The tag acts mainly through the text tokens that read it, not through a direct audio → tag path. Whisper at ×14 or higher: whispers more reliably, but words smear (×20 → WER 0.41). Before/after samples for every test take, glitches included: https://nikuson.github.io/silencio-2-weight-edit/ Takeaway: if your finetune "kind of" learned a control token but it's unreliable, look at attention before you collect more data. The information may already be in the model, just not being read.
