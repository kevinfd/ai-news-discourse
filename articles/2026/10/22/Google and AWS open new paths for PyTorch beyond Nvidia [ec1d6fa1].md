---
id: "ec1d6fa1b932a3c4"
title: "Google and AWS open new paths for PyTorch beyond Nvidia"
url: "https://thenewstack.io/pytorch-tpu-trainium-migration"
link: "https://thenewstack.io/pytorch-tpu-trainium-migration"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T15:23:23Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Meredith Shubel"]
language: "en"
summary: "At PyTorch Conference North America 2026 this week, Google open-sourced TorchTPU , a native PyTorch stack for Google TPUs, now available on GitHub . AWS also launched TorchNeuron in public beta, its open-source native PyTorch backend for AWS Trainium, also available on GitHub . \n\n Both releases seem aimed at making it easier for developers to move beyond Nvidia GPUs, whose CUDA software…"
tags: ["AI Infrastructure", "Developer tools", "Hardware"]
orgs: ["Google", "Amazon", "Nvidia", "Meta", "Hugging Face"]
topics: ["chips & infrastructure", "agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 710
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google and AWS open new paths for PyTorch beyond Nvidia

The New Stack · Meredith Shubel · 2026-10-22

Google and AWS open new paths for PyTorch beyond Nvidia
At PyTorch Conference North America 2026 this week, Google open-sourced TorchTPU, a native PyTorch stack for Google TPUs, now available on GitHub. AWS also launched TorchNeuron in public beta, its open-source native PyTorch backend for AWS Trainium, also available on GitHub.
Both releases seem aimed at making it easier for developers to move beyond Nvidia GPUs, whose CUDA software ecosystem has long dominated AI development. But while Google and AWS’s new offerings do ease some of the challenges of switching hardware, getting top-tier performance still isn’t straightforward.
For developers eager for more computing options, it’s promising but somewhat disappointing.
Google wants to make TPUs more PyTorch-friendly
Google put TorchTPU in preview with select customers in April (PyTorch says Google’s been working on the project since mid-2025), teasing a simpler way to run PyTorch workloads on Google’s AI chips. PyTorch support has long been an awkward dance, so the new backend could make it easier to run existing models on TPUs.
Google says it wants to make its TPU software ecosystem more open and developer-friendly for the PyTorch community, as it works to make the chips a more practical option for developers already using PyTorch.
Developed in collaboration with the PyTorch team at Meta, TorchTPU allows developers to run existing PyTorch workloads without JAX dependencies in the runtime. This way, rather than requiring extensive code changes, developers can migrate existing workloads with only “trivial code changes,” according to PyTorch.
Specifically, developers can use eager execution to debug models and torch.compile to optimize TPU utilization and reduce memory overhead. 
The new PyTorch stack from Google and Meta comes alongside a slew of other products and integrations announced at the conference, which Google says are “designed to help you run PyTorch effectively on Google Cloud or in your own infrastructure.” Google also announced integrations involving Hugging Face, vLLM, SGLang, llm-d, TorchTitan, Ray and TorchRec, while contributing LiteRT to the PyTorch ecosystem.
AWS wants in, too
AWS’s release extends the same PyTorch-native approach to its own AI chips.
Like TorchTPU, TorchNeuron gives developers a way to natively experiment and build models with PyTorch — this time for Trainium, AWS’s portfolio of AI chips designed for deep learning training and inference workloads. The public beta supports Trainium2 and Trainium3 instances.
AWS says moving a model to Trainium can be as simple as switching to .to(‘neuron’) for eager execution. Compiled models also need the Neuron backend selected, either as the default or in a torch.compile call.
TorchNeuron also integrates with Neuron Kernel Interface (NKI) — a bare-metal language and compiler for programming AWS Trainium and Inferentia NeuronDevices — so developers can create custom operators and optimize performance on Trainium. AWS and PyTorch have published more detailed guidance on the backend’s execution modes and performance tradeoffs.
Both are getting closer, but not there yet
While TorchTPU and TorchNeuron are notable steps forward in opening up more hardware choices for PyTorch developers, neither is a silver bullet.
PyTorch says a simple code change can get models running on TPUs, but peak performance can require TPU-specific optimization.
For distributed workloads, PyTorch says TorchTPU’s default Skinny Collectives approach can incur an end-to-end performance penalty of roughly 30–40% compared with an optimized approach because it prevents the XLA compiler from overlapping computation and communication.
For workloads seeking peak performance, PyTorch recommends additional tuning and production-grade stacks:
“Of course, for production workloads seeking peak performance we would absolutely recommend pursuing an optimal approach based on Pallas kernels and production-grade stacks such as vLLM-TorchTPU, SGLang-TorchTPU, or TorchTitan-TorchTPU, as examples.”
TorchNeuron is in public beta. In a separate blog post, AWS says teams can try Trainium with a configuration change instead of a code or model rewrite “in most cases,” leaving open which workloads need more changes.
In a case study, AWS describes how its Generative AI Innovation Center worked with AI research and technology company i14 to adapt its Laplace 3B model for Trainium2. The implementation required three changes: 1) using native PyTorch for the GLA attention kernel; 2) redesigning how Muon communicates; 3) compiling the sequential backward pass.
The releases give PyTorch developers more options beyond Nvidia GPUs. For now, moving existing code is easier than getting peak performance on unfamiliar chips.
