---
id: "5b943a8f0e97effd"
title: "bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF · Hugging Face"
url: "https://huggingface.co/bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF"
link: "https://huggingface.co/bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-06T19:19:24Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["jacek2023"]
language: "en"
summary: "do you want to try new 29B MoE today? https://www.reddit.com/r/LocalLLaMA/comments/1xoqc59/add_support_for_the_xing4_0_by_shuxiaoqiong_pull/ Xing4.0-29B-A4B is a next-generation large language model in the Xing series (formerly TeleChat ), developed by China Telecom Artificial Intelligence Technology Co., Ltd. With 29B total parameters and only 4B activated per token, it natively supports a 256K…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Hugging Face", "Google", "Meta", "China"]
topics: ["models & research", "agents & coding", "products & launches", "safety & ethics"]
content_source: "fulltext"
word_count: 1906
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xplkdu/bartowskixingchenagi_xing4029ba4bgguf_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF · Hugging Face

Hugging Face · jacek2023 · 2026-11-06

Instructions to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  llama.cpp  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with llama.cpp: Install (macOS, Linux) curl -LsSf https://llama.app/install.sh | sh # Start a local OpenAI-compatible server with a web UI: llama serve -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M # Run inference directly in the terminal: llama cli -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Install from WinGet (Windows) winget install llama.cpp # Start a local OpenAI-compatible server with a web UI: llama serve -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M # Run inference directly in the terminal: llama cli -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Build from source code git clone https://github.com/ggml-org/llama.cpp.git cd llama.cpp cmake -B build cmake --build build -j --target llama-app # Start a local OpenAI-compatible server with a web UI: ./build/bin/llama serve -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M # Run inference directly in the terminal: ./build/bin/llama cli -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Use Docker docker model run hf.co/bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M
- Llama new
- LM Studio
- Jan
-  vLLM  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M
-  Ollama  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with Ollama: ollama run hf.co/bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M
- Unsloth Desktop
-  Pi  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with Pi: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Configure the model in Pi# Install Pi:
npm install -g @earendil-works/pi-coding-agent
# Add to ~/.pi/agent/models.json:
{
  "providers": {
    "llama-cpp": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "none",
      "models": [
        {
          "id": "bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M"
        }
      ]
    }
  }
} Run Pi # Start Pi in your project directory: pi
-  Docker Model Runner  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with Docker Model Runner: docker model run hf.co/bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M
-  Lemonade  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with Lemonade: Pull the model # Download Lemonade from https://lemonade-server.ai/ lemonade pull bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Run and chat with the model lemonade run user.XingChen-AGI_Xing4.0-29B-A4B-GGUF-Q4_K_M List all available models lemonade list
-  Hermes Agent  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with Hermes Agent: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Configure Hermes # Install Hermes: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash hermes setup # Point Hermes at the local server: hermes config set model.provider custom hermes config set model.base_url http://127.0.0.1:8080/v1 hermes config set model.default bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Run Hermes hermes
- Atomic Chat
-  OpenClaw  How to use bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF with OpenClaw: Start the llama.cpp server # Install llama.cpp: brew install llama.cpp # Start a local OpenAI-compatible server: llama serve -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M Configure OpenClaw # Install OpenClaw: npm install -g openclaw@latest # Register the local server and set it as the default model: openclaw onboard --non-interactive --mode local \ --auth-choice custom-api-key \ --custom-base-url http://127.0.0.1:8080/v1 \ --custom-model-id "bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M" \ --custom-provider-id llama-cpp \ --custom-compatibility openai \ --custom-text-input \ --accept-risk \ --skip-health Run OpenClaw openclaw agent --local --agent main --message "Hello from Hugging Face"
Llamacpp imatrix Quantizations of Xing4.0-29B-A4B by XingChen-AGI
Using llama.cpp release b12174 for quantization.
Original model: https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B
Model details:
- Parameter count: 31B (source checkpoint)
- Input support: text
- Speculative decoding: yes (MTP) - details
- imatrix: yes - details
Prompt format
No prompt format found, check original model page
Don't know which to choose? Grab Q4_K_M (20.06GB) - usually a good mix of size and performance. Download instructions available here
Available files:
Download a specific file:
hf download bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF --include "XingChen-AGI_Xing4.0-29B-A4B-Q4_K_M.gguf" --local-dir ./
Downloading using the Hugging Face CLI
Click to view download instructions
First, make sure you have the Hugging Face CLI installed:
pip install -U "huggingface_hub[cli]"
Download a specific file:
hf download bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF --include "XingChen-AGI_Xing4.0-29B-A4B-Q4_K_M.gguf" --local-dir ./
The files marked true in the Split column above are stored as multiple parts in a folder. To download all the parts to a local folder, run:
hf download bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF --include "XingChen-AGI_Xing4.0-29B-A4B-bf16/*" --local-dir ./
You can either specify a new local-dir (XingChen-AGI_Xing4.0-29B-A4B-bf16) or download them all in place (./)
How to run
These quants run with llama.cpp - installable in one line via llama.app:
curl -LsSf https://llama.app/install.sh | sh
llama-server -hf bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF:Q4_K_M
llama-server includes a built-in chat web UI, served at http://localhost:8080 by default.
These quants were made with llama.cpp release b12174 - if this model's architecture is newly supported, you'll need that release or newer to run them.
They also work in: LM Studio · koboldcpp · ramalama · Jan AI · Text Generation Web UI · LoLLMs · Atomic Chat
MTP
This model has MTP (Multi-Token Prediction) layers, and they are included in these quants
MTP layers act as a built-in draft model, letting llama.cpp run speculative decoding for faster generation. To use them, add the following flag to your llama.cpp command:
--spec-type draft-mtp
Note: the MTP layers are stored at Q4_0 in every quant except Q8_0. Imatrix calibration does not exercise them, so the imatrix has nothing to offer these layers, and Q4_0 is chosen for its speed, which massively benefits MTP performance.
Per-tensor layouts
Some of these files were built with a layout computed for this model instead of llama.cpp's standard one-size-fits-all rules. A Q4_K_M is still mostly Q4_K; the extra precision goes to the weights this particular model is most sensitive to. The S, M or L in a name says how much of the model stays at the base precision: about 90 % for S, 70 % for M and 50 % for L. An _L name is simply the large size of its family. Q4_K_L is to Q4_K_M what Q4_K_M is to Q4_K_S; Q6_K_S, Q6_K and Q6_K_L are the small, medium and large sizes of Q6_K, with Q6_K_L about halfway to Q8_0. In earlier releases an _L name meant the embedding and output weights were kept at Q8_0; in these files it means the larger size of the base type. There is no size target, so each file's bits per weight is reported rather than promised.
The layout each of these files was built with is published in the layouts/ folder: <file>.tensor-types.txt is the exact --tensor-type-file given to llama-quantize, and <file>.layout.json records how it was computed, including the generator version, the llama.cpp release and the commit, so any of them can be rebuilt. The code that computed them is public at quantization-config; its tag key-3bf8b43e20a68f0b is the exact snapshot these files record. The method is described in this write-up.
Checked on this model before any of these files were released: Q4_K_M reached 0.99×, Q3_K_M 1.04× and IQ2_XXS 0.50× the KL divergence of the standard layout at the same file size.
Layout details
Files built from a computed layout:
Checked on this model: the computed layout against the standard one, measured by KL divergence against the unquantized model. The ratio compares each computed file with the standard ladder read at that file's own size, so it can differ from the two KLD columns when the two files differ in size.
How it works: the base type is a floor for every body tensor and a fixed share of the body bytes stays at it (90 % for S, 70 % for M, 50 % for L); the remaining bytes go where a cross-model sensitivity prior, measured by KL divergence against the unquantized model, says they buy the most quality. The embedding and output tensors are sized by their share of the file: a small table is kept at Q8_0, a large one follows the file's bitrate. A K-quant and the IQ quant with the same base bitrate (Q3_K_S and IQ3_XS, Q3_K_M and IQ3_S, Q3_K_L and IQ3_M) come out at about the same size; the IQ file is the GPU-oriented twin.
imatrix
All quants made using imatrix option, with a calibration corpus rendered through this model's own chat template. The corpus pairs plain prose with tool-calling and reasoning conversations (corpus source data), encoded exactly as this model sees them at inference and processed with --parse-special, so chat-format special tokens contribute to the importance matrix. The corpus rendered for this model is included in this repo: XingChen-AGI_Xing4.0-29B-A4B-calibration-v6.txt. The imatrix is available here: XingChen-AGI_Xing4.0-29B-A4B-imatrix.gguf.
Calibration render details
{
  "recipe": "calibration-v6",
  "encoder": "chat_template",
  "library_versions": {
    "transformers": "5.20.2",
    "tokenizers": "0.23.3",
    "tiktoken": "0.14.0",
    "blobfile": "3.3.0",
    "huggingface_hub": "1.31.0"
  },
  "chunk_size": 512,
  "prose_chunks": 228,
  "tool_chunks": 332,
  "total_chunks": 560,
  "n_conversations": 137,
  "conversation_token_lengths": [
    505,
    1617,
    862,
    1386,
    1153,
    1382,
    2653,
    608,
    1226,
    1189,
    1042,
    2081,
    830,
    947,
    2465,
    1278,
    1088,
    941,
    688,
    659,
    1338,
    1054,
    1431,
    1182,
    1690,
    1514,
    1001,
    680,
    918,
    1488,
    1619,
    790,
    1275,
    1005,
    1044,
    1748,
    1652,
    1152,
    419,
    1940,
    1386,
    1117,
    1428,
    1752,
    1955,
    1288,
    1584,
    761,
    2522,
    1079,
    2645,
    751,
    974,
    686,
    939,
    653,
    2320,
    698,
    1103,
    1043,
    1234,
    1147,
    915,
    972,
    920,
    1382,
    868,
    1567,
    1821,
    799,
    333,
    1113,
    3129,
    3030,
    666,
    701,
    990,
    724,
    1292,
    1061,
    1138,
    772,
    1063,
    1079,
    1256,
    1583,
    1430,
    1381,
    841,
    599,
    2533,
    680,
    1124,
    1694,
    2007,
    1167,
    605,
    1340,
    1147,
    1705,
    1670,
    1842,
    770,
    701,
    1034,
    3056,
    696,
    528,
    735,
    1184,
    1012,
    1317,
    727,
    362,
    331,
    2358,
    687,
    1132,
    1820,
    1726,
    2429,
    2443,
    628,
    951,
    787,
    830,
    1229,
    984,
    813,
    1373,
    788,
    669,
    1397,
    996,
    867,
    1307,
    1476
  ]
}
ARM/AVX information
llama.cpp automatically "repacks" weights into an interleaved layout at load time for faster inference on ARM and AVX machines - details in this PR. This once required downloading special Q4_0_4_4/4_8/8_8 files; those are long gone. Online repacking now covers Q4_0, IQ4_NL, and most K-quants, so no special quant choice is needed for CPU inference.
Which file should I choose?
Click here for details
An older (early 2024) but still useful write-up with charts comparing quant performances is provided by Artefact2 here
The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.
If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.
If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.
Hugging Face can also do this math for you: add your hardware in your Local Apps settings and the model page will show which files fit.
Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.
If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.
If you want to get more into the weeds, you can check out this extremely useful feature chart:
But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.
These I-quants can also be used on CPU, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.
Credits
Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.
Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
- Downloads last month
- 1,154
Model tree for bartowski/XingChen-AGI_Xing4.0-29B-A4B-GGUF
Base model
XingChen-AGI/Xing4.0-29B-A4B
