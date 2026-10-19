---
id: "ac37f6865e005bc3"
title: "AuroraASR-1M Releases!"
url: "https://huggingface.co/AuroraAI-Research/AuroraASR-1M"
link: "https://huggingface.co/AuroraAI-Research/AuroraASR-1M"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-18T12:48:33Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Tall_Abrocoma_3533"]
language: "en"
summary: "It's an extremely lightweight speech recognition model. 949K parameters using a weight-shared Conformer-CTC architecture Just 1.06 MB for INT8 weights Around 436× real-time on a single CPU thread 11.43% WER on LibriSpeech test-clean, using greedy decoding with no external language model Apache 2.0 licensed Any feedback, question or criticism is welcome!"
tags: ["r/LocalLLaMA"]
orgs: ["Google"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 666
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x92ejs/auroraasr1m_releases/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# AuroraASR-1M Releases!

Hugging Face · Tall_Abrocoma_3533 · 2026-10-18

Instructions to use AuroraAI-Research/AuroraASR-1M with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use AuroraAI-Research/AuroraASR-1M with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("automatic-speech-recognition", model="AuroraAI-Research/AuroraASR-1M", trust_remote_code=True) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModelForCTC
model = AutoModelForCTC.from_pretrained("AuroraAI-Research/AuroraASR-1M", trust_remote_code=True, device_map="auto")
- Notebooks
- Google Colab
- Kaggle
AuroraASR-1M
A tiny weight-shared Conformer-CTC speech recognizer under 1M parameters. Four unique Conformer-lite blocks are each applied twice, followed by a CTC head over a 256-piece BPE vocabulary. Trained on the full LibriSpeech dataset for 379 epochs, English only, 16 kHz mono input, greedy CTC decoding, no external language model is required.
Word error rate (LibriSpeech, greedy decoding)
WER (%) on the standard LibriSpeech test sets, all with greedy decoding and no external language model. Competitor figures are taken from each model's published card or paper.
Quantization: WER is nearly lossless across precisions, all the way down to INT8 weight-only. The figures above are for FP32.
Speed (FP32, full end-to-end pipeline)
Real-time factor (RTF) = processing time / audio duration (lower is better, 1.0 = real time). Batch size 1, 100 test-clean utterances (13.3 min of audio). End-to-end includes log-mel feature extraction and CTC decoding.
Usage
This model uses custom code, so trust_remote_code=True is required.
import soundfile as sf
from transformers import AutoModelForCTC, AutoFeatureExtractor
repo = "AuroraAI-Research/AuroraASR-1M"
model = AutoModelForCTC.from_pretrained(repo, trust_remote_code=True).eval() # FP32
# model = AutoModelForCTC.from_pretrained(repo, subfolder="int8", trust_remote_code=True).eval() # INT8
# model = AutoModelForCTC.from_pretrained(repo, subfolder="fp16", trust_remote_code=True).half().cuda().eval() # FP16
fe = AutoFeatureExtractor.from_pretrained(repo, trust_remote_code=True)
wav, sr = sf.read("audio.wav", dtype="float32")
print(model.transcribe(wav)[0])
Requires torch, transformers, sentencepiece.
Precisions
- FP32 (repo root, 3.81 MB): reference weights.
- FP16 (subfolder="fp16", 1.91 MB): half-precision weights.
- INT8 (subfolder="int8", 1.06 MB): Linear weights stored as int8 with per-output-channel scales and
dequantised on the fly. Smaller download and memory, runs on CPU and GPU without special runtimes.
It does not make the arithmetic faster.
Training methodology
Data
- Training set: LibriSpeech 960 h (train-clean-100, train-clean-360, train-other-500). No other audio or text data was used.
- Filtering: utterances shorter than 1 s or longer than 16 s were dropped, as were utterances whose token count exceeded one quarter of their feature frames.
- Model selection: dev-clean was used for per-epoch monitoring and checkpoint selection. test-clean and test-other were only used for the final evaluation.
Text and tokenization
- Transcripts are lowercased and restricted to a-z, apostrophe and space. The model outputs no punctuation or casing.
- A 256-piece SentencePiece BPE tokenizer was trained on the training transcripts only. The CTC output layer has 257 classes (256 pieces + blank).
Features
- 80-bin log-mel spectrogram (16 kHz, 25 ms window, 10 ms hop, 512-point FFT, 20 Hz to 8 kHz).
- Per-utterance mean/variance normalization of each mel bin.
Architecture
- 4x time-subsampling convolutional stem, then 4 unique Conformer-lite blocks, each applied twice with separate LayerNorms per pass (weight sharing).
- Width 128, 4 attention heads (rotary position embeddings), feed-forward dim 384, depthwise conv kernel 15.
- 949,073 parameters in total.
Objective
- CTC loss on the final layer (weight 0.7) plus an auxiliary intermediate CTC loss after the second unique block (weight 0.3). The auxiliary head reuses the final LayerNorm and output layer, so it adds no parameters and is discarded at inference.
- Loss is normalized by the number of target tokens.
Optimization
The schedule was time-budgeted: after a 200-step calibration, the total number of steps was fixed from the measured step time so the cosine decay completes within the budget. Training ran for 379 epochs (about 10 hours) on an RTX Pro 6000.
Evaluation protocol
- Greedy CTC decoding (collapse repeats, remove blanks), no language model.
- WER is computed on normalized text (lowercase, no punctuation) with a standard word-level edit distance. Figures from models that report on differently normalized text are therefore not strictly comparable.
- No speed perturbation, noise augmentation or external data were used.
- Downloads last month
- 42
