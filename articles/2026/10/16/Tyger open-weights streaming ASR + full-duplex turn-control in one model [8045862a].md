---
id: "8045862a61906fb6"
title: "Tyger: open-weights streaming ASR + full-duplex turn-control in one model"
url: "https://huggingface.co/nineninesix/tyger"
link: "https://huggingface.co/nineninesix/tyger"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-16T17:42:26Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["ylankgz"]
language: "en"
summary: "Hi r/LocalLLaMA , we're releasing Tyger, a small model that handles full-duplex turn-control for voice agents. What it is Base: NVIDIA Nemotron 3.5 ASR Streaming 0.6B + 14M causal GRU on top. Every 80 ms, with no lookahead, it picks one of three states: - answer : the user finished their turn - stop : the user cut in, so the agent stops talking - chime in : the agent says “mm-hm”, “oh, really”…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "products & launches"]
content_source: "fulltext"
word_count: 1050
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7msmj/tyger_openweights_streaming_asr_fullduplex/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Tyger: open-weights streaming ASR + full-duplex turn-control in one model

Hugging Face · ylankgz · 2026-10-16

TYGER - An open-weight speech decision model for real-time, full-duplex voice agents. It knows when to respond, keep listening, yield, and backchannel.
Example
Use it
tyger-s2s is our open-source voice agent built on this model (Apache-2.0). You talk to it in the browser, as on a phone call:
- this model is its ears: it transcribes you, and knows when you've finished, when you cut in, and when to say "mm-hm";
- LLM writes the replies, TTS speaks them in a cloned voice;
- it comes as a Docker image, and can be the voice backend of your own web app.
To run the model in your own code, start from tyger-s2s's runtime
(app/plugins/ears/tyger/).
The model
This repo holds weights and configs, no inference code.
Events
Guards: 6 warm-up frames, at least 350 ms of speech above -50 dB, 1.2 s between backchannels, and an endpoint after 1.2 s of silence even if the score stays low. The state input is LISTEN while the agent listens and SPEAK while it talks, never the model's own guess. The barge-in and backchannel defaults are looser than the evaluation's (0.93 and 0.80) and have no measurements of their own: tune them in your app (tyger-s2s's page has sliders for that).
Training
The GRU, its input layers and its heads were trained from scratch on Open Yap 1K v1.0 (1,395 training, 107 development and 100 test conversations), with Nemotron frozen. The labels come automatically from when each side speaks, not from human annotators: the turn state, an upcoming speaking onset (hazard), when to yield to an interruption, when a backchannel fits, and whether a pause ends the turn. One training seed.
Evaluation
Offline scores for the released weights, at endpoint 0.91, barge-in 0.93 and backchannel 0.80, set on development data and frozen before test scoring. evaluation/README.md has the definitions and caveats, and metrics.json every number.
Endpoints,:
- Latency runs from the end of the user's turn, and counts only endpoints that fired: read it with the early cut-ins (an endpoint before the turn really ended) and the misses.
- With the fallback off, Open Yap's mean latency is 436.5 ms, and 16.0% of turns get no endpoint within 1.2 s.
Turn state, barge-in and backchannel (Open Yap 1K test):
Speed: the GRU takes 0.805 ms per frame (median; p90 0.823 ms) on an RTX 4090 at batch 1, with 108.76 MiB of peak GPU memory. That leaves out Nemotron and waiting for audio. In tyger-s2s, the whole model takes ~4 GB of GPU memory for 4 conversations.
Limits:
- Offline diagnostics only: no live voice-agent benchmark, and no new ASR error rates (NVIDIA's card has its own).
- One training seed, and the evaluation sets also guided development. The internal set can't be reproduced.
- The Full-Duplex-Bench rows are adapted v1.0 CANDOR replays with a silent agent channel, not official full-agent scores. FDB-v3 isn't evaluated.
License
TYGER's weights and files are OpenMDW-1.1. NVIDIA's original
card, figures and license are unchanged in upstream/ and licenses/, and
manifest.json lists every file's size and SHA-256. See
LICENSE.md and NOTICE.md.
Links
- Voice agent: nineninesix-ai/tyger-s2s
- Website: nineninesix.ai
- Discord: NineNineSix community
- Training data: Open Yap 1K
- ASR: NVIDIA Nemotron
Acknowledgments
We thank NVIDIA for Nemotron, The Agentic Data Company for Open Yap 1K, and the authors of Full-Duplex-Bench for its evaluation probes. Related work, not bundled or reproduced here: Full-Duplex-Bench-v3, Moshi, SALM-Duplex, Freeze-Omni, PersonaPlex and Audio Flamingo 3.
Citation
If you use TYGER, please cite the model and its training data:
@misc{tyger_2026,
  author    = {{NineNineSix}},
  title     = {{TYGER}: Speech Recognition and Duplex Turn Control},
  year      = {2026},
  publisher = {NineNineSix},
  url       = {https://huggingface.co/nineninesix/tyger}
}
@misc{openyap1k,
  title     = {Open Yap 1K: Channel-Separated English Natural Two-Speaker Conversations},
  author    = {{The Agentic Data Company}},
  year      = {2026},
  version   = {1.0},
  publisher = {The Agentic Data Company},
  url       = {https://theagenticdatacompany.com/open-yap-1k}
}
References
BibTeX for the ASR component and related work
@misc{nvidia_nemotron_3_5_asr,
  author = {{NVIDIA}},
  title  = {Nemotron 3.5 ASR Streaming 0.6B},
  url    = {https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b},
  note   = {Bundled revision ea30d66debe3740a08b573244286791d423d6b3e}
}
@misc{lin2025fullduplexbench,
  title = {Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities},
  author = {Lin, Guan-Ting and Lian, Jiachen and Li, Tingle and Wang, Qirui and Anumanchipalli, Gopala and Liu, Alexander H. and Lee, Hung-yi},
  year = {2025}, eprint = {2503.04721}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2503.04721}
}
@misc{lin2026fullduplexbenchv3,
  title = {Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency},
  author = {Lin, Guan-Ting and Chen, Chen and Chen, Zhehuai and Lee, Hung-yi},
  year = {2026}, eprint = {2604.04847}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2604.04847}
}
@misc{defossez2024moshi,
  title = {Moshi: a speech-text foundation model for real-time dialogue},
  author = {D\'{e}fossez, Alexandre and Mazar\'{e}, Laurent and Orsini, Manu and Royer, Am\'{e}lie and P\'{e}rez, Patrick and J\'{e}gou, Herv\'{e} and Grave, Edouard and Zeghidour, Neil},
  year = {2024}, eprint = {2410.00037}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2410.00037}
}
@misc{hu2025salmduplex,
  title = {SALM-Duplex: Efficient and Direct Duplex Modeling for Speech-to-Speech Language Model},
  author = {Hu, Ke and Hosseini-Asl, Ehsan and Chen, Chen and Casanova, Edresson and Ghosh, Subhankar and {\.{Z}}elasko, Piotr and Chen, Zhehuai and Li, Jason and Balam, Jagadeesh and Ginsburg, Boris},
  year = {2025}, eprint = {2505.15670}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2505.15670}
}
@misc{wang2024freezeomni,
  title = {Freeze-Omni: A Smart and Low Latency Speech-to-speech Dialogue Model with Frozen LLM},
  author = {Wang, Xiong and Li, Yangze and Fu, Chaoyou and Shen, Yunhang and Xie, Lei and Li, Ke and Sun, Xing and Ma, Long},
  year = {2024}, eprint = {2411.00774}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2411.00774}
}
@misc{roy2026personaplex,
  title = {PersonaPlex: Voice and Role Control for Full Duplex Conversational Speech Models},
  author = {Roy, Rajarshi and Raiman, Jonathan and Lee, Sang-gil and Ene, Teodor-Dumitru and Kirby, Robert and Kim, Sungwon and Kim, Jaehyeon and Catanzaro, Bryan},
  year = {2026}, eprint = {2602.06053}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2602.06053}
}
@misc{goel2025audioflamingo3,
  title = {Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models},
  author = {Goel, Arushi and Ghosh, Sreyan and Kim, Jaehyeon and Kumar, Sonal and Kong, Zhifeng and Lee, Sang-gil and Yang, Chao-Han Huck and Duraiswami, Ramani and Manocha, Dinesh and Valle, Rafael and Catanzaro, Bryan},
  year = {2025}, eprint = {2507.08128}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2507.08128}
}
- Downloads last month
- 113
Model tree for nineninesix/tyger
Base model
nvidia/nemotron-3.5-asr-streaming-0.6b
