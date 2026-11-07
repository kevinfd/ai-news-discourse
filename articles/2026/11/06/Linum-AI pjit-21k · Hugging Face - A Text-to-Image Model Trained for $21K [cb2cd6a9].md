---
id: "cb2cd6a92dd67f85"
title: "Linum-AI/pjit-21k · Hugging Face - A Text-to-Image Model Trained for $21K"
url: "https://huggingface.co/Linum-AI/pjit-21k"
link: "https://huggingface.co/Linum-AI/pjit-21k"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-06T13:24:58Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["pmttyji"]
language: "en"
summary: "P-JiT 21K is the P-JiT architecture trained for longer (610M samples at 512px, 50M at 1024px), then post-trained with a variant of FDFO . GitHub : https://github.com/Linum-AI/pjit-21k Blog Post : https://www.linum.ai/field-notes/pjit-21k"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Hugging Face"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 553
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpcpws/linumaipjit21k_hugging_face_a_texttoimage_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Linum-AI/pjit-21k · Hugging Face - A Text-to-Image Model Trained for $21K

Hugging Face · pmttyji · 2026-11-06

A Text-to-Image Model Trained for $21K
(Pyramid-JiT)
	
Sahil Chopra · Manu Chopra · Linum
Five samples from the blog post's gallery. Their prompts and seeds are in the code repository.
Research checkpoint: this is an experimental research artifact, not a production model. P-JiT 21K is a 2B-parameter model trained on 660M samples for about $21K of compute, as a stepping stone towards our next video model. We're releasing it because the results surprised us for a model this size, and to encourage others to explore efficient training methods like ours. You should expect rough edges.
This model cannot write text or generate posters. It was trained on little to no images of rendered text: no infographics, PDFs, pages of books, slides or posters. We filtered that data out on purpose (it isn't useful for our goal of animation tools), so prompts that ask for words, signs, logos, title cards or posters will not work.
P-JiT 21K is the P-JiT architecture trained for longer (610M samples at 512px, 50M at 1024px), then post-trained with a variant of FDFO.
Usage
The model was trained on dense captions of 50 to 80 words. The
code repository ships a prompt upsampler that rewrites
short prompts into captions of that kind with Claude Opus 5.5 through OpenRouter (it needs an
OPENROUTER_API_KEY; --no_upsample turns it off):
git clone https://github.com/Linum-AI/pjit-21k && cd pjit-21k
pip install -e .
# The portrait above (writes outputs/seed_2.png)
PROMPT="Close-up portrait of an elderly Middle Eastern woman looking calmly into the lens, her face filling the tall frame. A cream headscarf and the collar of a dark green cardigan frame her chin. Soft overcast daylight smooths the fine lines of her skin, and the olive grove behind melts into silvery blur."
python generate.py --no_upsample --aspect_ratio tall --seeds 2 --prompt "$PROMPT"
# Your own prompt, upsampled
export OPENROUTER_API_KEY=...
python generate.py --prompt "oil painting of weathered fisherman smoking a pipe" --aspect_ratio square --seeds 0
The prompts and seeds of all five samples are in the code repository.
Sampling defaults: 50 Euler steps, adaptive projected guidance at scale 15 against an empty negative prompt, initial noise at scale 4. The model was trained at five ~1 MP sizes: 1024x1024, 864x1216, 1152x864, 1248x832 and 1280x720 (width x height). Text is encoded by a frozen Qwen3.5-4B, which downloads separately.
Files
Limitations
A small model (2B DiT, 4B text encoder), so it struggles with full-body shots, many entities (six cars, crowds), interactions between several people, and world knowledge (six strings on a guitar, the dots on a die).
Citation
@online{chopra2026pjit21k,
  title = {Training a Text-to-Image Model for \$21K},
  author = {Chopra, Sahil and Chopra, Manu},
  year = {2026},
  url = {https://www.linum.ai/field-notes/pjit-21k}
}
Authorship
The code for this model was written by Claude (Anthropic's Opus 5.5 model, running in Claude Code). Linum asked it to extract the model and inference code from Linum's internal experiment repository and to add the prompt upsampler. The model, the training, and the review of the code and this model card are Linum's.
About Linum
Linum is a team of two brothers building a tiny-yet-powerful AI research lab. We train our own generative media models from scratch.
Subscribe to Field Notes: technical deep dives on building generative video models from the ground up, plus updates on new releases from Linum.
Contact: hello@linum.ai
- Downloads last month
- 212
