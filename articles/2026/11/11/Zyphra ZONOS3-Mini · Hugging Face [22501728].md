---
id: "2250172890a0969a"
title: "Zyphra/ZONOS3-Mini · Hugging Face"
url: "https://huggingface.co/Zyphra/ZONOS3-Mini"
link: "https://huggingface.co/Zyphra/ZONOS3-Mini"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-11T07:09:56Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["pmttyji"]
language: "en"
summary: "ZONOS3-Mini is Zyphra’s compact, open-source text-to-speech model, delivering natural reliable speech and high-fidelity voice cloning with just 100 million active parameters. It runs in real time on phones and laptops, including directly in the browser. Clone a voice from an audio sample, or design a character by shaping age, accent and vocal texture. Steer emotion, pace and delivery down to…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "OpenAI", "Google", "Apple", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "business & funding"]
content_source: "fulltext"
word_count: 737
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xtb9gw/zyphrazonos3mini_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Zyphra/ZONOS3-Mini · Hugging Face

Hugging Face · pmttyji · 2026-11-11

Instructions to use Zyphra/ZONOS3-Mini with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Zonos How to use Zyphra/ZONOS3-Mini with Zonos: # pip install git+https://github.com/Zyphra/Zonos.git
import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict
model = Zonos.from_pretrained("Zyphra/ZONOS3-Mini", device="cuda")
wav, sr = torchaudio.load("speaker.wav")           # 5-10s reference clip
speaker = model.make_speaker_embedding(wav, sr)
cond  = make_cond_dict(text="Hello, world!", speaker=speaker, language="en-us")
codes = model.generate(model.prepare_conditioning(cond))
audio = model.autoencoder.decode(codes)[0].cpu()
torchaudio.save("sample.wav", audio, model.autoencoder.sampling_rate)
- Notebooks
- Google Colab
- Kaggle
ZONOS3-Mini
ZONOS3-Mini is Zyphra’s compact, open-source text-to-speech model, delivering natural reliable speech and high-fidelity voice cloning with just 100 million active parameters. It runs in real time on phones and laptops, including directly in the browser.
Clone a voice from an audio sample, or design a character by shaping age, accent and vocal texture. Steer emotion, pace and delivery down to individual words for games, narration and voice assistants.
Run ZONOS3-Mini locally with our browser and native runtimes, or access it through Zyphra Cloud. Model weights are released under Apache 2.0.
Model details, samples and evaluations are in the blog post. A hosted version is available at Zyphra Cloud.
Languages
ZONOS3-Mini supports 43 languages.
Quick start
In your browser
ZONOS3-Mini runs entirely on your own GPU through WebGPU: no install and no server. The first visit downloads the model, and the browser keeps it cached for later visits. You need a browser with WebGPU support.
- Zonos Voice Studio: the full studio.
- Lite: quick voice cloning. Pick, upload or record a voice and speak with it.
With SGLang
SGLang-Omni serves ZONOS3-Mini on NVIDIA GPUs behind the OpenAI-compatible
/v1/audio/speech endpoint, with streaming and voice cloning from a reference clip (no transcript needed). Install SGLang-Omni
by following its installation guide,
then start a server:
sgl-omni serve --model-path Zyphra/ZONOS3-Mini --port 8000
Once curl http://localhost:8000/health reports "healthy", generate speech with the default voice from another terminal:
curl -X POST http://localhost:8000/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{"input": "Hello from ZONOS3-Mini!"}' \
  --output output.wav
Add "references": [{"audio_path": "<reference clip>"}] to clone a voice, or "stream": true, "response_format": "pcm" to
stream 44.1 kHz audio as it is generated. The ZONOS3 cookbook
covers voice cloning, streaming and the sampling options.
Native runtimes
The ZONOS3-Mini GitHub repository holds Zyphra's own runtimes, which share one HTTP
API and serve the Zonos Voice Studio: a CUDA server for NVIDIA GPUs, an MLX server for Apple Silicon, a C++/ggml server and CLI
(CPU, CUDA, Metal or Vulkan), and the in-browser WebGPU build.
They load the GGUF files in gguf/ and the WebGPU shards in
web/; the 27 default voices, grouped by language, are in
gguf/voices/.
Architecture (rough outline)
Text is NeMo-normalized (English, Mandarin, Japanese, Korean, German, Spanish, French, Italian, Portuguese; other languages pass through as written) and encoded with an 8,192-entry SuperBPE tokenizer. The language model autoregressively generates 15 Hz dual-codec frames (10 codebooks of 4,096 entries each: one semantic codebook distilled from the Wav2Vec2-BERT teacher plus nine acoustic codebooks), conditioned on the text, a speaker prompt and three bucketed acoustic controls. A causal multi-resolution iSTFT head renders the frames to 44.1 kHz audio as they are produced.
Inference pipeline. Speaker conditioning (raw reference codes or a speaker-embedding row), control rows and SuperBPE text enter the hybrid GDN/attention MoE backbone, which predicts all ten codebooks of the next frame under the delay pattern (four drawn); as soon as a frame's last codebook is generated, the codec's causal iSTFT head renders that frame to audio.
ZAC 1 (Zyphra Audio Codec 1).
Evaluations
Full results and the ZTTS2 capability index are in the blog post.
Quality against speed on one H100 80GB. Quality combines macro speaker similarity and macro WER over the 55 language subsets of ZTTS2-Eval (benchmark version 2: FLEURS-R read speech in 35 languages and VoxBlink2 in-the-wild recordings in 20 languages) as ½ z(similarity) − ½ z(WER) across the systems shown; ZONOS3-Mini is measured with the speaker-embedding prompt. Left: median time to first audio with 8 concurrent requests (80 ms for ZONOS3-Mini). Right: peak throughput at each model's best concurrency (457 seconds of audio per second for ZONOS3-Mini).
Citation
If you find this model useful in an academic context, please cite the release post:
@misc{zyphra2026zonos3mini,
  title        = {{ZONOS3-Mini Technical Report}},
  author       = {Gabriel Clark and Sofian Mejjoute and George Close and Beren Millidge},
  year         = {2026},
  month        = nov,
  howpublished = {\url{https://www.zyphra.com/our-work/zonos3-mini}},
}
- Downloads last month
- 4,170
We're not able to determine the quantization variants.
