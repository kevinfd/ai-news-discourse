---
id: "a35b870fddc0751a"
title: "Training Text-to-Image Models Without a VAE"
url: "https://linum.ai/field-notes/pyramid-jit"
source: "linum.ai"
domain: "linum.ai"
source_type: "community"
collector: "hackernews"
date: "2026-10-06T20:24:52Z"
published_date: "2026-10-06"
collected_at: "2026-10-13T20:17:27Z"
authors: ["schopra909"]
language: "en"
summary: "In our last post, we developed a pixel-space encoder-decoder architecture (JiT-DDT). By throwing away the VAE, we were able to compress tokens more aggressively. In turn, this slashed the cost of attention and directly led to faster training and inference.\nWhile effective, it's unclear how to scale encoder-decoder architectures under fixed parameter budgets. So today, we propose the Pyramid-JiT…"
tags: []
orgs: []
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 4361
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49983582"
score: 54
comments: 19
community: "Hacker News"
---

# Training Text-to-Image Models Without a VAE

linum.ai · schopra909 · 2026-10-06

In our last post, we developed a pixel-space encoder-decoder architecture (JiT-DDT). By throwing away the VAE, we were able to compress tokens more aggressively. In turn, this slashed the cost of attention and directly led to faster training and inference.
While effective, it's unclear how to scale encoder-decoder architectures under fixed parameter budgets. So today, we propose the Pyramid-JiT (P-JiT), a novel decoder-only pixel space architecture that beats our prior models, by predicting the target image at several resolutions along the DiT trunk. It reaches Linum v2's FD-DINOv2 on 11.3× fewer training samples, and trains in 4.3× fewer GPU-hours at 4× the pixels.
Research release
P-JiT code and model weights are available under the Apache 2.0 license. We hope that by sharing our findings with the broader community, we can encourage others to also explore more efficient training methods. This should be treated as a research artifact, not a full model release. Stay tuned for more research checkpoints like this, en route to Linum v3.
Where should the parameters go?
Our goal is to build affordable animation tools, so that anyone can bring their story to screen. Right now the best video models in the world (e.g. Seedance) are expensive because they calculate attention on ridiculously large token sequences. For our own Linum v2 model, a short 720p, 5 second video cost 110K tokens. By comparison, a LLM trains on context sizes of 8K or less for 97% of their training regime.
To make our vision a reality, we need to cut the cost of video generation by an order of magnitude. We're bottlenecked by attention, which is an operation with respect to context-window token count. If we can cut down the number of tokens, we can slash the cost of attention and achieve massive savings across training and inference.
En-route to our Linum v3 video model, we've been using text-to-image as a testbed to try out ideas that can help us condense context windows. Previously, we wrote about how LDMs (Latent Diffusion Models) seem to have an empirical ceiling of 16x16 token compression unless you tweak the auto-encoder significantly. So, we pivoted towards pixel space models (JiT) to achieve 32x32 token compression, unifying compression and generation into a single streamlined model. From there, we developed a novel pixel-space architecture (JiT-DDT) that produced better results than our prior LDM while training 3.6x faster.
While effective, it's unclear how to scale encoder-decoder architectures. Do you increase the encoder's size so that it learns structure better? If so, it seems wasteful to spend so many parameters predicting a low resolution image. Or, do you increase the decoder's size so that it spends more time learning the fine-grained details that really matter to humans? In doing so, you might cap the model's ability to learn the framing and structure of a scene (without which the details are meaningless).
Language faced a similar dilemma ~10 years ago. If you dig through the archives, you'll see that the transformer was first proposed as the building block for an encoder-decoder trained on language translation. The field then split into encoder-only models (BERT-style classifiers) and decoder-only models (GPT-style LLMs). The beauty of a decoder-only model is that it's really easy to scale, since there is no explicit architectural bottleneck.
So the driving question is: Can we port over the advances from encoder-decoder back to the vanilla JiT and get similarly high quality results?
Revisiting the JiT
In our prior work, we found that we could dramatically improve the quality of our generations by widening the noise schedule during training and adding separate DiT blocks to refine the image and text streams independently, before merging them into a single shared stream. So, we copied and pasted these innovations over to the JiT.
Additionally, we widened our linear patchification's bottleneck dimension from 256 to 1024 to reduce the effective compression rate within the network from 12x to 3x. And, we picked up the innovations from Z-Image.
With these updates, we're able to recover a lot of performance, but we're still missing two big deltas from the JiT-DDT: multiresolution prediction and dual patchification.
Replacing the encoder with readouts
In the JiT-DDT, we had the encoder predict a 64x64 version of the 512x512 input image. Our hypothesis was this would help the model draft an initial low-res answer so that the decoder could allocate its capacity to filling in details.
When we zoomed out and looked at adjacent work like RAE v2 and Self-Flow, it seemed our encoder prediction served two more concrete purposes. First, it boosted the gradient signal in the early layers of the DiT that tend to adapt much more slowly. And second, by regressing a low resolution image it helped the early portions of the DiT explicitly learn structure (something that hacks like REPA tap into to accelerate learning as well).
Even if we throw away the encoder, we can still access these improvements. Since our model is trained with x-prediction, every intermediate DiT block is implicitly predicting a version of our target image. So we can slap K OutputHeads along the trunk of the DiT and have each regress a version of our target image (either at full resolution or downsampled to a lower resolution, like we did in the JiT-DDT).
We tried predicting full-resolution images along the network but that performed slightly worse than predicting images in an inverted pyramid of increasing resolutions from 128² to 256² to 512². Another hunch we had was that we might want to place less weight on the low-resolution readouts so the model could allocate more features for high-resolution detail. In practice that worked worse than equal-weighted readouts; so 3-Readout became our new baseline for our subsequent experiments.
Multiview networks
The JiT-DDT had two different patchifications, one for the encoder (64x64) and another for the decoder (32x32). 3-Readout trains ~16% faster than JiT-DDT, even though it uses the more expensive 32x32 patchification. And aesthetically we seem to beat the JiT-DDT.
So rather than bring the encoder's 64x64 patchification back in the mix, we were curious what if we could raise the ceiling on the model's generation quality by arming it with several 32x32 patchifications.
Our hypothesis was that the model might be able to modulate between a set of patchifications according to timestep. Patchification A might be more active for details while Patchification B might be more active for structure. By enabling this type of soft specialization (kind of like Mixture of Experts), we might be able to reduce the information lost to compression in a single linear bottleneck, improve the overall expressivity of the model, and enable both better structure learning and detail learning.
Widening the residual stream
Now for a slight detour (we promise it'll all make sense soon).
Over the past 12 months, LLM researchers out of China have recontextualized the skip connection as a memory buffer for the LLM. If we can increase the residual stream's expressivity (e.g. widen it, introduce more complicated read/write rules), we can significantly improve the network's performance. DeepSeek mHC, Kimi Attention Residuals, and Qwen Gated Residuals are all different articulations of this general idea.
DeepSeek's mHC and Qwen's Gated Residuals are particularly exciting, because they don't increase the cost of attention. Moreover, the wider residual stream is a perfect place to bring our idea of multiple 32x32 patchifications to life. Qwen and DeepSeek initialized the wider residual stream by copying and pasting their representations along the channel dimension 4x at the start of their networks. Instead of copying it 4 times, we can just introduce 2 patchifications (each duplicated twice) or 4 distinct patchifications.
Adapting gated residuals to flow matching
In Qwen 3.8-Next's head-to-head ablations, the authors found that Gated Residuals worked better than mHC and matched Attention Residuals. It's the easiest to implement, so we ran with that instantiation of the expressive residual idea.
The one roadblock to copy-and-pasting the Gated Residual into our flow matching model is timestep conditioning. In LLMs, you're predicting a series of auto-regressive tokens; there is no concept of timesteps or noised inputs.
There's a paper from early 2025 out of Kaiming He's lab that demonstrates that flow matching models should be able to implicitly estimate timestep from the noised sample . So for our first attempt at porting Gated Residuals, we gutted timestep modulation (AdaLN scaling) altogether. It produced notably worse results, so we went back to the whiteboard and brainstormed ways to reintroduce timestep conditioning.
At a high level, timestep conditioning can be either a shift (i.e., an added bias) or a scale (i.e., a multiplier on the existing features). A scale stretches or shrinks each feature across the image. Features with large absolute values get pitched up or down significantly, while features that hover around zero stay there regardless of the multiplicative factor. A shift slides every token by the same offset. That records the timestep in the hidden state's absolute values but leaves the relative differences between features untouched.
In our 3-Readout model we rely entirely on scales, because we want to stretch and shrink the hidden states based on timestep (e.g., turn up structure at high noise, turn up detail at low noise). So, we opted for scales here again.
On the read, ① scales the hidden state within the sigmoid gate. This way timestep conditioning doesn't mess with the bounded read. We do this in the smaller 368-dimensional space to be parameter efficient. This costs us 94K parameters per gate vs. 3M parameters per gate in the full 11,776-dimensional gate-logit space (i.e., if we did ). ② is just a replication of our old AdaLN () method.
For writes, we can either condition the mixing function or scale the MLP/Attn outputs . ③ adds the timestep to the write gate's logit per-token-per-stream-per-channel., Counterintuitively, this bias still acts as a scaling op, because is used as a multiplicative factor in the residual write (). ④ scales the sublayer's output per channel, capped at 2× by the .
We tried mixing and matching the read and write options, but with ③, training was 80% slower than our 3-Readout baseline. That was too costly for us to stomach, so we dropped it and tried ① + ④ and ② + ④. The results were a wash, so we went with ① + ④ since it costs fewer parameters.
Introducing several patchifications
For all our gated residual experiments, we used the same 3-Readout prediction task and training regime. So, the only deltas were the replacement of the AdaLN / tanh gate / post-norm with our timestep-dependent gated residual, and the number of patchifications used to seed the residual stream.
We tried 1 stem × 1024, 2 stems × 1024, and 4 stems × 768. The lattermost is hypothetically lossless. A 32x32 patchification yields a 3,072-dimensional vector (32 height × 32 width × 3 RGB = 3,072). 4 × 768 = 3,072, so across the 4 patchifications you should be able to represent all the pixel information.
Surprisingly, our 3-Readout baseline generated better samples than all our gated residual experiments. It also trains significantly faster, so after all that exploration we ended up back where we started.
Honestly, this was somewhat surprising. If we return to this line of experiments in the future, we'd need to dig into why 1 stem × 1024 performed worse than our baseline. Our best hunch is that the post-norm is a stronger bound on activations than the in , and that's helping the model pick up details like the freckles faster.
Pyramid-JiT
We refer to our 3-Readout training regime with the updated AdaLN + tanh + post-norm architecture as the Pyramid-JiT (P-JiT) because we predict images along a range of resolutions. For full architecture and training details, check out Appendix A.
P-JiT is able to learn the underlying image distribution much faster than either Linum v2 or JiT-DDT. Moreover, it achieves a much better FD-DINOv2 score (27.9 vs. 79.9 and 39.1 respectively), approaching the real-vs-real floor of 25.4 for the 30K sample size.
Metrics like FD-DINOv2 try to capture how well the model mimics the underlying data distribution, but they fail to capture the aesthetic quality of the generations. For this, you have to look at generated samples and apply your artistic judgement.
We find that P-JiT generates significantly better images than Linum v2, even though it uses much more aggressive token reduction. We also think that the P-JiT samples are on average more detailed than their JiT-DDT counterparts. For example, in these generations the eyes are more defined and the wrinkles are more naturalistic in the P-JiT samples than the JiT-DDT ones. For additional examples, take a look at Appendix B.
After distribution-matching statistics and aesthetic grading, folks usually turn to automated prompt-following benchmarks like GenEval, GenEval 2, and DPG-Bench. They're meant to test properties like counting, relative positioning, and object presence with incredibly terse prompts like a photo of an orange orange. These prompt lengths are out of distribution for our models, since we trained on dense captions with a median of 82 words. We've reported our models' scores on raw prompts in Appendix C, but for a fairer comparison we ran each benchmark on upsampled prompts.
Note that this is a super common technique. Every text-to-image or text-to-video model provides a finetuned LLM to rewrite prompts to match its training distribution (or does this behind the scenes, when you hit an API). We upsampled the prompts using Claude Opus 5.5 in a Claude Code session. For details, again you can turn to Appendix C.
Surprisingly, Linum v2 beats pixel-space models in prompt-following benchmarks
bold = best · underlined = second best
Each of our models runs at its native resolution (Linum v2 at 256², JiT-DDT and P-JiT at 512²), 4 images per prompt, on the benchmark prompts rewritten into our training-caption style; our GenEval 2 scores per prompt are averaged over the 4 seeds. GM, GenEval 2's headline, is a prompt-level geometric mean over each prompt's elements, so one missed element pulls an image down hard; AM is the element-level average. GM varies by ±0.9–1.2 across seeds. Only the generator sees the rewrite; the judges still score the samples against the original prompt.
GenEval 2 and DPG-Bench are roughly a wash between Linum v2 and P-JiT. But it's somewhat surprising how much better Linum v2 is than P-JiT on GenEval. We've broken down the GenEval score by question type in Appendix C. It turns out Linum v2 scores 0.80 on counting (e.g., getting exactly three apples in an image) while P-JiT scores 0.56, and 0.95 on colors while P-JiT scores 0.90. Those two sub-scores drive the difference in GenEval performance.
While P-JiT demolishes Linum v2 on distributional metrics (FD-DINOv2) and sample quality, it is still undertrained on a few of these prompt-following categories.
So next, we're going to train P-JiT till convergence (before switching to our true goal, video pre-training). We'll be releasing these artifacts as additional research checkpoints, so stay tuned for them!
Appendix A – Pyramid-JiT Details
Training regime
The Pyramid-JiT keeps the JiT-DDT's two-phase noise schedule. For the release checkpoint, the switch to the wider schedule happens after 50M of the 138M training samples.
Appendix B – Pyramid-JiT Image Samples
Appendix C – Prompt-Following Benchmarks
Prompt upsampling
Each benchmark prompt was rewritten into our training-caption style, with the judges still scoring the samples against the original prompt.
Ten writer agents rewrote all 2,418 prompts. A reviewer agent then checked each rewrite against the benchmark's own answer key (the objects, counts and colors GenEval checks for, GenEval 2's yes/no questions, DPG-Bench's question graph) and failed it if a faithful image could break any of those checks. For example, an upsampled prompt containing "… four flamingos standing in water …" would be rejected by the reviewer, since the evaluation harness might mistake the reflections of the flamingos in the water for flamingos to be counted and artificially ding our generative model.
The reviewers failed 55 rewrites, and each got a fixed version. A script then confirmed every required object, count, color and relation survived.
Agent runbook for upsampling benchmark prompts
This is a runbook written by Claude Opus 5.5 that summarizes the approach it took during our Claude Code session to rewrite the prompts.
markdown
# Agent runbook: upsampling benchmark prompts
(Style guide and content lock)
Used to rewrite the GenEval, GenEval 2 and DPG-Bench prompts into the style of our training captions. Only `gen_prompt` is rewritten; the judges always score against the original `prompt`. Derived from a random sample of the 30K in-domain captions (median 82 words, p10 56, p90 117).
## What our training captions look like
1. **One paragraph, 2 to 4 sentences, ~60 to 100 words.** No lists, no line breaks, no preamble.
2. **The subject opens the caption as a noun phrase**, usually with its count and color up front: "Four orange tea light candles are scattered across a bamboo slat mat…", "Three light brown blondies… stack vertically on a white ceramic plate…", "A brown tabby cat rests on a tan surface…".
3. **Photographs are never labelled.** There is no "A photo of" or "A photograph of"; a caption with no medium phrase *is* a photo. Other media are named first: "A digital illustration in a saturated palette of…", "An oil painting in a vibrant, surrealist style…", "Vector illustration in a bright, flat style depicting…", "A 3D render…", "Anime illustration of…".
4. **Counts are number words** ("Ten golden-brown corn fritters", "two clear glasses"), stated once, early.
5. **Colors are specific and attached directly to their object** ("a grey thermal mug capped with a red ring and a blue lid"). Materials and textures come with them ("weathered wooden slat table", "ribbed knit", "matte ceramic").
6. **Frame-relative placement** is how layout is expressed: "centered in the frame", "on the left of the frame", "fills the lower half of the frame", "in the upper right", "To the right, …", "in the lower foreground".
7. **Camera / framing phrases:** "viewed from directly above", "an overhead view", "a slight high angle", "shot from the waist down", "framed from the shoulders up", "a top-down view".
8. **Lighting and optics, usually near the end:** "high-key lighting that leaves the highlights overexposed", "harsh light from the upper left casts sharp shadows", "soft diffuse daylight", "the background dissolves into soft bokeh", "a shallow depth of field".
9. **The background closes the caption:** "against a plain white background", "against a blurred, neutral background", "a seamless light grey backdrop".
10. **People** are described by apparent age, ethnicity and gender ("A young East Asian woman…", "A middle-aged white man…"), then hair, clothing and pose.
11. Visible text is quoted verbatim ("…reads "THE SECRET GARDEN"").
## Content lock (hard rules; a rewrite that breaks any of them is rejected)
- **Keep every object, count, color, material/attribute, spatial relation, action and quoted text** of the original. Use the original's own words for each: the same object noun (plural-insensitive), the same number word, the same color word with the same spelling ("gray" stays "gray"), and the same relation word ("left of" → "to the left of" is fine; do not swap sides).
- A color may be made more specific only by **adding** words around the original color word ("a blue fire hydrant" → "a glossy blue fire hydrant"), never by replacing it ("cobalt" instead of "blue" is a rejection).
- **Add no new objects** that could be counted, detected or asked about. Extra detail is limited to framing, camera angle, lighting, depth of field, medium, plain surfaces and plain backgrounds.
- **Numbers must stay unambiguous.** "two clocks" must not gain a reflection, a shadow described as a second clock, "a pair of", "several", or a second group of the same object.
- **Spatial relations stay literal.** A frame-relative restatement that agrees with the relation is allowed ("a dog right of a teddy bear" → the teddy bear on the left of the frame, the dog to its right). Do not invent relations the original does not state beyond that.
- **Style / medium:** keep a medium the original names ("an oil painting of…"). This includes a photographic medium named as part of a DPG prompt's content ("a monochromatic photograph", "a high-resolution DSLR image"), which DPG may ask about. Only GenEval's boilerplate "a photo of" template is dropped. If it names none, write it as an unlabelled photograph (rule 3 above), unless the content is plainly impossible as a photo, in which case still leave the medium unstated.
- **Never change what an object is to make a relation work.** An object must stay a normal, real instance of itself. No statue, sculpture, toy, model or figurine version unless the prompt says so (a "stone giraffe" can be carved; a "toothbrush" cannot become a toothbrush sculpture), no giant or oversized version, and no hovering, floating, suspension or strings where a mundane arrangement works. In order of preference, satisfy "X above/on top of/under Y" by (1) X resting on Y, (2) an ordinary support such as a shelf, windowsill, hook, table or a hand holding it, or (3) the frame itself: X higher in the picture, e.g. farther back or on a ledge behind. GenEval's position check compares object centers in the 2D image, so (3) is enough there. When the prompt itself is physically absurd (horses on a motorcycle), state it plainly and let the image be odd; don't invent machinery to explain it.
- **Attribute binding:** each color or attribute stays attached to the same object as in the original, and no other object in the rewrite gets that color.
### GenEval-specific (Mask2Former detector over the 80 COCO classes + CLIP color crops)
- Do **not** mention any COCO class other than the ones in the prompt: person, bicycle, car, motorcycle, airplane, bus, train, truck, boat, traffic light, fire hydrant, stop sign, parking meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard, sports ball, kite, baseball bat, baseball glove, skateboard, surfboard, tennis racket, bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake, chair, couch, potted plant, bed, dining table, toilet, tv, laptop, computer mouse, tv remote, computer keyboard, cell phone, microwave, oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy bear, hair drier, toothbrush. That includes supporting surfaces: no "table", "bench", "couch", "bed" or "chair" as a resting surface (use "a wooden floor", "a concrete surface", "a grassy field", "a plain backdrop").
- Do not add people (so no "person" detections) unless the prompt contains a person.
- The objects should be shown whole and clearly separated, which the detector needs: "both fully in frame", "the entire …".
- Keep other strong colors out of the scene: backgrounds and surfaces neutral (white, grey, beige, natural wood/concrete) so the CLIP color check on the object crop is not confused. For a color prompt, never give the background or surface the same or a competing named color.
### GenEval 2-specific (Qwen3-VL answers each prompt's `vqa_list`)
- Every question in the item's `vqa_list` must still have the listed answer given the rewrite alone: every count, every "Is the X <attribute>?" and every "Are there any X?".
### DPG-specific (mPLUG answers each prompt's question list)
- DPG prompts are already long (median 65 words), so the rewrite restyles rather than lengthens. Keep it in the same length range, up to about 130 words.
- Every question in the item's DPG question list must still be answerable "yes" from the rewrite: every entity, attribute, count, relation, action, global style and quoted text.
Prompt-Following Score Breakdowns
Summary Scores (Raw vs. Upsampled)
bold = best · underlined = second best, within each prompt group · ↑/↓ = change from raw prompts, deeper green for a bigger relative gain, red for a drop
Each of our models runs at its native resolution (Linum v2 at 256², JiT-DDT and P-JiT at 512²), 4 images per prompt; our GenEval 2 scores per prompt are averaged over the 4 seeds. Upsampled prompts are rewritten into our training-caption style; the judges still score the samples against the original prompt. DPG-Bench barely moves with upsampling, likely because its prompts are quite dense. They're similar to our training prompts, so they're relatively in-distribution. Linum v2 benefits the most from prompt upsampling. It uses T5 embeddings, which may be more brittle than the Qwen embeddings we use for the pixel-space models.
GenEval Breakdown By Task
bold = best · underlined = second best, within each prompt group
Overall GenEval is the unweighted mean of the six tasks. On raw prompts, counting and position separate the models. Once upsampled, position evens out (0.84–0.87) and counting is most of the gap. Pixel-space models generate better aesthetic samples and better match the underlying image distribution, but seem relatively undertrained for these aspects of prompt following.
DPG-Bench Breakdown By Task
bold = best · underlined = second best, within each prompt group
DPG-Bench's overall score is averaged per prompt over a question graph, where failing a parent question (is there a cat?) also fails its children (is the cat black?). That's why it usually comes out lower than the category scores. Across raw and upsampled prompts each of our models stays within 0.3 points overall. Only the Global category (which scores style and scene-level descriptions) and the Other category see substantial shifts.
Authorship statement
We wrote all the words on this page except for the markdown-embedded Agent Runbook.
Claude Opus 5.5 was used within Claude Code to generate the upsampled prompts for GenEval, GenEval 2, and DPG-Bench. We then used Claude to dig through that conversation and summarize its approach to solving this problem in the runbook.
We used Claude Opus 5.5 to help us build the diagrams.
The Huggingface Model Card and Github Repo were written automatically by Claude Opus 5.5. We pointed Claude to our internal, experiment repo and had it pull out (and clean up) the necessary code.
Who are we?
We're two brothers training text-to-video models from scratch, trying to make animation accessible to everyone.
Get Field Notes
Technical deep dives on building generative video models from the ground up, plus updates on new releases from Linum.
