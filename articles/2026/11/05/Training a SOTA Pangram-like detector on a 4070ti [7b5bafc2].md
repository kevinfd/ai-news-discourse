---
id: "7b5bafc2941187c6"
title: "Training a SOTA Pangram-like detector on a 4070ti"
url: "https://huggingface.co/mesmertech/mesmer-ai-detector-4b"
link: "https://huggingface.co/mesmertech/mesmer-ai-detector-4b"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-05T17:00:57Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["mesmerlord"]
language: "en"
summary: "This is kinda claude-slop but I was really interested in figuring out a way to break Pangram, and to do that I first needed to have a way to be able to do tests on batches of text. And with a 4070ti in my basement, I thought why not just let Claude go ham on training a pangram-like model... and perhaps an even better one if it was possible with sorta-distillation from my claude plan + codex…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Meta", "Hugging Face", "Alibaba"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 538
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xonxqo/training_a_sota_pangramlike_detector_on_a_4070ti/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Training a SOTA Pangram-like detector on a 4070ti

Hugging Face · mesmerlord · 2026-11-05

Mesmer AI Detector 4B
Tells you whether English text is human-written, AI-written or AI-edited (human writing that an AI reworded or polished), and labels each sentence. Fine-tuned from Qwen3.5-4B-Base. A bigger, more accurate sibling: mesmer-ai-detector-9b.
Try it without a GPU: Hugging Face Space · mesmer.tools
Fun fact: this whole project was generated with Claude. Claude Opus collected the data, trained and evaluated these models autonomously, and wrote this card, so the card doubles as a test sample. Run on this card, the 4B says AI-written (p ≈ 0.99 AI, 0.01 AI-edited, 0.00 human) and flags every sentence.
Benchmarks
The best open-weight detector on every benchmark we could compare. It catches AI text about as well as the closed Pangram models (better than Pangram 3.x, a little behind Pangram 4 on style imitation), but it flags more human writing (see Limitations).
Open Pangram suite
These are Pangram's own eval sets and protocol from the Open Pangram release. Ternary means human vs AI vs AI-edited. Llama-family text was kept out of our training, so the Llama-3.3-70B set is an unseen generator for us too.
Pangram's numbers are from its blog. Ours use the bf16 weights; the int8 weights are within 0.007 on the ternary rows.
Other public benchmarks (zero-shot)
Other detectors' numbers are as published by Pangram, the Pangram 4 report, the MELD paper and Epoch AI (GPTZero on Epoch: 34 missed, 0 flagged). Ours use the int8 weights. Epoch counts strictly: only an "AI" verdict counts as caught, and an "AI-edited" verdict on human text counts as flagged. We dropped 140 benchmark human texts that overlapped our training data.
Quickstart
pip install torch numpy tokenizers safetensors emoji huggingface_hub
pip install fla-core   # optional: faster GPU kernels (otherwise pure PyTorch; CPU works too, but slowly)
hf download mesmertech/mesmer-ai-detector-4b mesmer_detector.py --local-dir .
python mesmer_detector.py --model mesmertech/mesmer-ai-detector-4b "Paste the text to check here."
from mesmer_detector import Detector
det = Detector.from_pretrained("mesmertech/mesmer-ai-detector-4b")   # int8=True: 8-bit weights, about half the memory
r = det.analyze(text)       # any length; long texts are scored in windows
r["verdict"]                # "human" | "ai" | "ai_edited"
r["probs"]                  # {"human": ..., "ai": ..., "ai_edited": ...}
r["sentences"]              # [{"text", "label", "p"}, ...] per sentence
det.predict(texts)          # batch scoring: [N, 3] probabilities from each text's first 1,023 tokens
Weights: bf16 model.safetensors 8.4 GB, or int8 int8/model.safetensors 4.2 GB (4.9 GB once loaded). On the GPU, add 1–3 GB for activations, or pass a smaller tokens_per_batch (default 16384). The default verdict thresholds (policy.json) were set on held-out human texts so that at most 0.7% are called AI-written and at most 1% get any flag.
Limitations
- English only. Below about 50 words the results are unreliable (the hosted tool refuses texts under 40 words).
- It flags more human writing than Pangram. At the default thresholds it flags about 0.3% of MELD-eval's human texts and 1% of DetectRL's. Most of these are academic abstracts, news articles and poetry.
- AI text written to imitate a specific person's style is the main way through, especially in scientific writing.
- No detector is proof. Never use a result as the only evidence against anyone.
License
CC BY-NC-SA 4.0: non-commercial use, with attribution and share-alike.
- Downloads last month
- 27
Model tree for mesmertech/mesmer-ai-detector-4b
Base model
Qwen/Qwen3.5-4B-Base
