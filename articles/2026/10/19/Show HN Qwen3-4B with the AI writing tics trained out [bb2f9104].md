---
id: "bb2f9104933712ab"
title: "Show HN: Qwen3-4B with the AI writing tics trained out"
url: "https://100toolkit.com/blog/deslop-model"
link: "https://100toolkit.com/blog/deslop-model"
source: "100toolkit.com"
domain: "100toolkit.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-19T13:00:47Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["erikkannike"]
language: "en"
summary: "Answers on 40 held-out prompts\nThese are one sampled answer per prompt from the original model and from the released one, on ten topics in four genres, with no system prompt. Underlined passages are what the slop detector counts.\nA small open model, fine-tuned on a MacBook Air, that writes without em dashes, \"not X, but Y\" or lists of three and needs no system prompt, and you can run it locally…"
tags: []
orgs: []
topics: ["models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1549
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50151928"
score: 149
comments: 109
community: "Hacker News"
---

# Show HN: Qwen3-4B with the AI writing tics trained out

100toolkit.com · erikkannike · 2026-10-19

Answers on 40 held-out prompts
These are one sampled answer per prompt from the original model and from the released one, on ten topics in four genres, with no system prompt. Underlined passages are what the slop detector counts.
A small open model, fine-tuned on a MacBook Air, that writes without em dashes, "not X, but Y" or lists of three and needs no system prompt, and you can run it locally with Ollama.
- I trained the assistant writing habits out of Qwen3-4B-Instruct and released it as qwen3-4b-deslop. With Ollama it's ollama run hf.co/erikkannike/qwen3-4b-deslop-v4-GGUF:Q4_K_M, a 2.5 GB download.
- On 40 prompts it never saw in training, the slop score dropped from 121 to 12.5 per 1000 words, and 68% of answers score in the range of human writing. Em dashes went from 20.5 per 1000 words to zero.
- It still answers 30 of 30 factual questions correctly and fits the requested genre and length as often as the original. Its predictions on human-written prose moved about a third as much as with runtime steering.
- An intermediate version scored 9.9 and wrote badly: opinion pieces without an opinion, invented studies, and a new habit of joining every sentence with ", which". Fixing that took a second filter that checks whether an answer does what the prompt asked.
- The voice is plain to the point of flat, and it still invents names and places.
My home lab is a MacBook Air, so this is a 4B model trained on 161 answers. The recipe doesn't depend on the model size, and running it on larger models is the next step.
The score comes from a detector I wrote from a style guide of AI writing habits: the em dash, "it's not X, it's Y", lists of three, rhetorical questions answered on the spot, signposts like "here's the thing", short fragments for emphasis, and words like "delve" and "seamless". Each habit has a weight, and the score is a weighted count per 1000 words. A paragraph by a careful human writer scores close to zero, and the original model averages 121.
A regex can't tell good writing from bad, so every model below was also checked for damage. Drift measures how far its predictions on 22 passages of human prose move from the original model's. A 30-question quiz checks that it still knows things, and a rule-based check flags broken output like lowercase sentence starts or a lost topic. I also read a sample of answers from every model.
An earlier experiment on this model found the assistant register as a direction inside it: subtracting it while the model writes, together with a plain-style system prompt, takes the score to about 15, but it needs the prompt and code running during generation, and it shifts the model's predictions on ordinary text. A second one read neurons one at a time and found four whose sign flip removes 70% of "not X, but Y" at almost no cost, though only for that one habit.
To get both into the weights I used distillation: a teacher, built from whatever worked best so far, answers 288 training prompts. I keep the answers that pass the checks, and a small LoRA adapter learns to produce them from the bare prompt. The first round got the score to about 20 with no prompt and no hooks.
For round two the teacher was the round-one model plus the four-neuron patch and the plain-style prompt. Adding the direction steering on top as well produced the lowest score I have measured, 9.5, from text with no capital letters that wandered off topic, so I took the steering back out. The teacher then averaged 7.4, and the student trained on its 171 best answers scored 9.9, with 80% of answers in the human range.
In its answers, an opinion piece about a company's new CRM never took a position and read like an incident report. A blog post about moving to a new city became a third-person story about a family with a leaking apartment. A piece about houseplants cited "a study from the University of Technology Sydney", which the model invented. Almost every sentence ran into the next with ", which" or ", so", 28 times as often as in the original model. That last habit came from my own teacher prompt, which had told the model to join sentences "with because, so, but, which", and two rounds of imitation had amplified it.
I added rule-based checks for whether an answer does what the prompt asked. An opinion piece has to state a position early, a personal reflection has to be in the first person, an email has to open with a greeting, and the length has to roughly match the request. Two more checks count ", which" and ", so" joins and invented studies and percentages. On those, the round-two model did what was asked only 60% of the time, against 78% for the original.
The third teacher got a prompt that put the task first: take a position when asked, write in the first person when it's personal, vary the sentences, and don't invent studies or names. It wrote three answers per prompt, and an answer was kept only if it scored under 12, passed the damage checks and passed all the task checks. About 30% did, which covered 161 of the 288 prompts.
The model trained on those answers is the released one. Its score rose a little, from 9.9 to 12.5, while task fit went back to 80% and the ", which" joins fell from 1.4 to 0.3 per 100 words. Invented studies and percentages nearly disappeared.
The quantised build (Q4_K_M, 2.5 GB) runs on a laptop with Ollama or llama.cpp:
ollama run hf.co/erikkannike/qwen3-4b-deslop-v4-GGUF:Q4_K_M
llama-cli -hf erikkannike/qwen3-4b-deslop-v4-GGUF:Q4_K_M
The full-precision weights load with transformers like any Qwen3-4B checkpoint:
from transformers import AutoModelForCausalLM, AutoTokenizer
name = "erikkannike/qwen3-4b-deslop-v4"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name, torch_dtype="auto")
msgs = [{"role": "user", "content": "Write a LinkedIn post about switching to a four-day week."}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt")
out = model.generate(ids, max_new_tokens=300, do_sample=True, temperature=0.7)
print(tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True))
The repo also has the parts on their own: the LoRA adapter (126 MB) and the neuron edit, a 175-byte list of four weight columns and their scales. The adapter was trained with the edit active, so the two go together.
The voice is flat: the model writes runs of short declarative sentences, and its personal pieces read like diary entries.
It also still makes things up: studies and percentages are rare now, but invented names and places are common, like a coffee shop on Maple Street run by a woman named Maria, because concrete detail is what every round rewarded. It also runs long, and answers to "about 150 words" often come in near 200.
I have only tested short English prose in these genres. Code, long conversations, other languages and tool use may be no better than the original model, or worse. The score is my style guide written as regular expressions, and no blind test with readers has checked it yet. The numbers also move between runs: the same model scored 10.2 through the adapter and 12.5 as merged weights, from sampling differences alone.
Each student ended up about as good as the best answers its teacher could write, so a better model needs a better teacher. I'm putting together a set of excellent human writing, public-domain essays and letters plus modern pieces, to use as examples for a base model. A base model never went through assistant training and still writes like the people it learned from. If that teacher writes better than this model does, the same recipe should produce a student with some taste as well as clean habits. After that comes the same pipeline on a 7 to 8B model and one around 30B, and a blind test where people pick the better text.
- Base model: Qwen3-4B-Instruct-2507 in bf16. Every adapter is a rank-16 LoRA on all attention and MLP projections, trained for two epochs on the bare user prompt with loss on the response only, between one and three hours per round on an M2 MacBook Air.
- Test set: ten topics never used in training, each in four genres (blog post, LinkedIn post, explainer, opinion piece), one sampled answer per prompt at temperature 0.7, no system prompt. Drift is the KL divergence from the original model on 22 passages of human prose.
- The task-fit checks are simple rules (a stance word near the start of an opinion piece, first-person pronouns in a reflection, a greeting in an email, word counts) and they miss things a reader would catch. The training data was filtered on the same checks reported here, so the task-fit numbers flatter the model somewhat.
- The neuron edit flips the sign of four MLP neurons (layer 32 neuron 4852, layer 33 neuron 348, layer 28 neuron 1121, layer 32 neuron 5418), which is the same as negating four columns of their layers' down-projection weights. The GGUF build was quantised from a Q8_0 conversion of the merged weights.
- The readers' chat and live cursors connect readers directly over WebRTC (Trystero with public Nostr relays). Peers can see each other's IP addresses, nothing is saved, and "hide" disconnects you.
