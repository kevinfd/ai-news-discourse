---
id: "ad8b3d5bdfd0d7ff"
title: "Show HN: DeepSeek V3 in ~200 lines of pure Jax"
url: "https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax"
link: "https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-14T15:04:15Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["VaibhaavTiwari"]
language: "en"
summary: "The architecture from the DeepSeek-V3 technical report in 190 lines of pure JAX, pretrained from scratch on a MacBook Air on public-domain detective fiction.\nNo Flax, no Equinox, no PyTorch. Params are plain dicts of arrays and every part of the model is a function you can read top to bottom in deepseek_v3.py.\nRead the write-up: DeepSeek V3 in 190 lines of pure JAX, with diagrams, the code…"
tags: []
orgs: ["DeepSeek", "Apple"]
topics: ["models & research", "products & launches", "safety & ethics", "chips & infrastructure"]
content_source: "fulltext"
word_count: 929
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50497589"
score: 246
comments: 23
community: "Hacker News"
---

# Show HN: DeepSeek V3 in ~200 lines of pure Jax

GitHub · VaibhaavTiwari · 2026-11-14

The architecture from the DeepSeek-V3 technical report in 190 lines of pure JAX, pretrained from scratch on a MacBook Air on public-domain detective fiction.
No Flax, no Equinox, no PyTorch. Params are plain dicts of arrays and every part of the model is a function you can read top to bottom in deepseek_v3.py.
Read the write-up: DeepSeek V3 in 190 lines of pure JAX, with diagrams, the code explained piece by piece, and the results.
One run of the default config on a MacBook Air M5 (24 GB):
With balancing on and off, validation loss at step 2000 was the same (3.921 vs 3.923). The bias evens out the experts without costing anything, which is the paper's claim.
Its own words, from the prompt "The fog came in off the":
The fog came in off the bay, and the great trees were spreading and the stars were shining.
This is an architecture demo, not a strong language model. See the write-up for what worked, what didn't, and what's missing.
The v1.0 release has the exact checkpoint and data from the published run. After installing (step 1):
mkdir -p data runs/main
curl -L -o runs/main/ckpt.pkl      https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax/releases/download/v1.0/ckpt.pkl          # 138 MB
curl -L -o data/tokenizer.json     https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax/releases/download/v1.0/tokenizer.json
.venv/bin/python sample.py --prompt "The fog came in off the" --num 3
The checkpoint is a Python pickle, which can run code when loaded. Only load checkpoints from sources you trust.
You need an Apple Silicon Mac, Python 3.12 and uv. The published run used 24 GB of memory. No Mac? See Running on CPU.
1. Install
git clone https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax.git && cd deepseek-v3-jax
uv venv -p 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
Every version in requirements.txt is pinned. jax-metal 0.1.1 only works with jax==0.4.34, so don't upgrade JAX.
2. Check your setup
JAX_PLATFORMS=cpu .venv/bin/pytest tests.py -q    # 39 passed
.venv/bin/python smoke_metal.py                   # optional: what jax-metal supports on your Mac
In smoke_metal.py, "grad through 2-axis contraction" fails on jax-metal 0.1.1. That's expected, and the model is written to avoid it.
3. Build the dataset
.venv/bin/python prepare_data.py
This downloads the 207 books in sources.txt (~120 MB, about 7 minutes), cleans them, trains an 8,192-token BPE tokenizer and writes data/train.bin, data/val.bin and data/tokenizer.json. It should print:
train: 211 docs, 83.4M chars, 21.69M tokens
val: 4 docs, 1.1M chars, 0.30M tokens
The published run's data had these hashes:
shasum -a 256 data/train.bin data/val.bin data/tokenizer.jsond37aca97e707bb81b6e4d266cc1adfd1f3e3556457c6eb724e495118a734e0bb  data/train.bin
b7ac285b115e6793b5d36aa5b4bc6e81a5fccfc7af0908a306d3828ebca9c31c  data/val.bin
c5a142b4006a967c880dda44ad792719d53c16d947da3b6c2332d6132d9967cc  data/tokenizer.json
You will most likely get different hashes. The Hammett books are pinned to exact Standard Ebooks commits and come out identical, but Project Gutenberg files can't be pinned, and Gutenberg has since re-issued 28 of the 203 books with small edits (mostly accents stripped, like "José" → "Jose"). The token counts come out the same, so training should behave the same.
To train on the exact same bytes, skip prepare_data.py and download the published data instead:
mkdir -p data
for f in train.bin val.bin tokenizer.json; do curl -L -o data/$f https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax/releases/download/v1.0/$f; done
shasum -a 256 data/*.bin data/tokenizer.json    # should match the hashes above
4. Train
.venv/bin/python train.py                                         # the main run: 12k steps, ~2.6 h
.venv/bin/python train.py --steps 2000 --out runs/bias_on         # balancing ablation, with the bias
.venv/bin/python train.py --steps 2000 --out runs/bias_off --no-bias   # ...and without it
Each run writes metrics.jsonl (loss, validation loss, per-expert load, biases, tokens/s) and ckpt.pkl (saved at every evaluation) into its --out folder, which defaults to runs/main. Seeds are fixed, but GPU math on Metal isn't bit-for-bit deterministic, so expect your numbers to land close to the ones above rather than match them exactly.
5. Generate
.venv/bin/python sample.py --prompt "The fog came in off the" --num 3
Defaults: temperature 0.8, top-k 50, 300 new tokens per sample (--temp, --top-k, --n).
6. Make the figures
.venv/bin/python plots.py                    # needs runs/main, runs/bias_on, runs/bias_off
JAX_PLATFORMS=cpu .venv/bin/python charts.py # the rest of the write-up's charts
Both write into post/figures/.
To redraw the figures without training, download the logs from the release: metrics-main.jsonl, metrics-bias_on.jsonl and metrics-bias_off.jsonl go into runs/main/, runs/bias_on/ and runs/bias_off/ as metrics.jsonl. charts.py also needs the checkpoint and the data.
Everything runs without jax-metal. It's much slower, so use the smaller config:
JAX_PLATFORMS=cpu .venv/bin/python train.py --config small
--config small (4 layers, 8 experts, top-2, 128-token context) is meant for 8–16 GB Macs too. It has only been checked for a couple of steps, not trained to the end.
The code runs unmodified on JAX's ROCm backend. rocm/ has a container setup tested on an RX 7600 XT (16 GB): the full run takes ~50 min at ~35k tok/s and reaches val loss 3.527 (vs 3.507 here).
"190 lines" counts the non-blank, non-comment lines of deepseek_v3.py after its docstring:
tail -n +5 deepseek_v3.py | grep -cvE '^\s*(#|$)'    # 190
- Dense MoE compute. Every expert runs on every token and the unpicked ones are zeroed. The routing math is exact, but there's no sparse dispatch or expert parallelism.
- No weight absorption in MLA. The latent is decompressed explicitly, which is easier to read and slower at inference.
- Not included: FP8 training, DualPipe, node-limited routing, YaRN context extension, and any post-training.
- Scale. 36.2M parameters vs 671B, 6 layers vs 61, a 256-token context vs 128K.
All training text is public domain in the United States: Dashiell Hammett's Red Harvest, The Dain Curse, The Maltese Falcon and Continental Op stories (CC0 editions from Standard Ebooks), plus about 200 detective and crime novels from Project Gutenberg. Every source is listed in sources.txt. Public-domain status outside the US may differ.
DeepSeek-AI, DeepSeek-V3 Technical Report, 2024.
Code: MIT. The training text is public domain in the US (see above).
