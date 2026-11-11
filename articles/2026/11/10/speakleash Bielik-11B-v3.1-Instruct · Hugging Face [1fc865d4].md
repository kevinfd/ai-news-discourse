---
id: "1fc865d435ce1675"
title: "speakleash/Bielik-11B-v3.1-Instruct · Hugging Face"
url: "https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct"
link: "https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-10T16:30:55Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["jacek2023"]
language: "en"
summary: "https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct-GGUF https://www.bielik.ai/blog/premiera-modeli-bielik-11b-v31-dflash-i-rodziny-bielik-one (decision models and dflash are coming next) Bielik-11B-v3.1-Instruct Bielik-11B-v3.1-Instruct is a generative text model featuring 11 billion parameters. It is an update to the Bielik 11B v3 line that expands multilingual continual pre-training…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Google", "Hugging Face", "EU"]
topics: ["models & research", "products & launches", "business & funding", "health & science"]
content_source: "fulltext"
word_count: 1539
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsrg0l/speakleashbielik11bv31instruct_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# speakleash/Bielik-11B-v3.1-Instruct · Hugging Face

Hugging Face · jacek2023 · 2026-11-10

Instructions to use speakleash/Bielik-11B-v3.1-Instruct with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use speakleash/Bielik-11B-v3.1-Instruct with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="speakleash/Bielik-11B-v3.1-Instruct")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("speakleash/Bielik-11B-v3.1-Instruct")
model = AutoModelForCausalLM.from_pretrained("speakleash/Bielik-11B-v3.1-Instruct", device_map="auto")
messages = [
    {"role": "user", "content": "Who are you?"},
]
inputs = tokenizer.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
- Notebooks
- Google Colab
- Kaggle
- Local Apps Settings
-  vLLM  How to use speakleash/Bielik-11B-v3.1-Instruct with vLLM: Install from pip and serve model# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "speakleash/Bielik-11B-v3.1-Instruct"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "speakleash/Bielik-11B-v3.1-Instruct",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker docker model run hf.co/speakleash/Bielik-11B-v3.1-Instruct
-  SGLang  How to use speakleash/Bielik-11B-v3.1-Instruct with SGLang: Install from pip and serve model# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "speakleash/Bielik-11B-v3.1-Instruct" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "speakleash/Bielik-11B-v3.1-Instruct",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}' Use Docker imagesdocker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "speakleash/Bielik-11B-v3.1-Instruct" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "speakleash/Bielik-11B-v3.1-Instruct",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
-  Docker Model Runner  How to use speakleash/Bielik-11B-v3.1-Instruct with Docker Model Runner: docker model run hf.co/speakleash/Bielik-11B-v3.1-Instruct
Bielik-11B-v3.1-Instruct
Bielik-11B-v3.1-Instruct is a generative text model featuring 11 billion parameters. It is an update to the Bielik 11B v3 line that expands multilingual continual pre-training and strengthens post-training for instruction following, tool use, and reasoning. Forementioned model stands as a testament to the unique collaboration between the open-science/open-source project SpeakLeash and the High Performance Computing (HPC) center: ACC Cyfronet AGH. Developed and trained on multilingual text corpora covering 56 languages, with an emphasis on European languages and Polish, which have been cherry-picked and processed by the SpeakLeash team, this endeavor leverages Polish large-scale computing infrastructure of the ACC Cyfronet AGH HPC center. The creation and training of Bielik-11B-v3.1-Instruct was propelled by resources provided within the PLGrid environment under computational grant number [PLG/2026/019559], conducted on the Athena and Helios supercomputers, and within the Gaia AI Factory, funded by the European Union through the EuroHPC Joint Undertaking. As a result, the model exhibits an exceptional ability to understand and process the Polish language and other European languages, providing accurate responses and performing a variety of linguistic tasks with high precision.
🗣️ Chat: https://chat.bielik.ai/
Model
The model was trained on carefully curated, high-quality datasets that underwent extensive cleaning and rigorous quality assessment to ensure data consistency, reliability, and relevance. The training pipeline consisted of three stages: pretraining on 500B tokens, SFT on 26M samples, and RL (modified GRPO) across 14 diverse environments. This multi-stage training approach was designed to enhance the model's language understanding, instruction-following capabilities, and ability to perform effectively across a broad range of tasks.
Bielik instruct models have been trained with the use of an original open source framework called ALLaMo implemented by Krzysztof Ociepa.
Model description:
- Developed by: SpeakLeash & ACC Cyfronet AGH
- Language: Multilingual (56 unique languages, optimized for European languages, with a particular focus on Polish)
- Model type: causal decoder-only
- License: Apache 2.0
Serving with vLLM (tool calling and reasoning)
Bielik-11B-v3.1-Instruct uses its own tool-call and reasoning format
(<tool_call>{"name": …, "arguments": …}</tool_call> and <think>…</think>).
To get structured tool_calls and a separate reasoning field in the
OpenAI-compatible API, start vLLM with the Bielik parsers from
speakleash/bielik-tools.
Requirements: vLLM 0.24 or newer (tested on 0.32). The chat template ships
with the model (chat_template.jinja), so --chat-template is not needed.
git clone https://github.com/speakleash/bielik-tools.git
vllm serve speakleash/Bielik-11B-v3.1-Instruct \
    --enable-auto-tool-choice \
    --tool-parser-plugin ./bielik-tools/tools/bielik_vllm_tool_parser.py \
    --tool-call-parser bielik \
    --reasoning-parser-plugin ./bielik-tools/tools/bielik_vllm_reasoning_parser.py \
    --reasoning-parser bielik \
    --exclude-tools-when-tool-choice-none \
    --max-model-len 32768
- Load exactly one tool parser and one reasoning parser (both register the name bielik).
- --exclude-tools-when-tool-choice-none removes tool definitions from the prompt
when a request sets tool_choice="none"; otherwise the model may still write a
tool call as plain text.
- Older per-version parsers (*_v0.12.0.py, *_v0.13.0.py, *_v0.15.0.py, the 0.20 plugin)
are frozen and meant for older vLLM releases; see the bielik-tools README.
Reasoning
Thinking is controlled with reasoning_effort: none (default), low, medium,
high, max. With none the model answers directly. The enable_thinking
flag used by Bielik v3.0 is ignored by this template.
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
resp = client.chat.completions.create(
    model="speakleash/Bielik-11B-v3.1-Instruct",
    messages=[{"role": "user", "content": "Ile jest liczb pierwszych mniejszych od 50?"}],
    reasoning_effort="high",          # or extra_body={"chat_template_kwargs": {"reasoning_effort": "high"}}
    max_tokens=4096,
)
msg = resp.choices[0].message
print("reasoning:", getattr(msg, "reasoning", None) or getattr(msg, "reasoning_content", None))
print("answer:", msg.content)
Leave enough max_tokens for reasoning plus the answer: if generation stops while
still thinking, content is empty.
Tool calling
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Returns the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]
resp = client.chat.completions.create(
    model="speakleash/Bielik-11B-v3.1-Instruct",
    messages=[{"role": "user", "content": "Jaka jest pogoda w Krakowie?"}],
    tools=tools,
    tool_choice="auto",               # "required", "none" or a named function also work
)
print(resp.choices[0].message.tool_calls)
- tool_choice="required" and a named function are enforced by the parser
(constrained decoding of the call; the argument schema itself is not enforced).
- The request-level tool_choice and response_format do not reach the chat
template. To also add the template's instructions, repeat them in extra_body={"chat_template_kwargs": {"tool_choice": "required"}}.
- Treat tool arguments as untrusted input.
Default system prompt
The template prepends a built-in system prompt ("Model Guidelines": identity,
knowledge cutoff, current date, safety rules; about 1,000 tokens). Your own system
message is appended under "Additional Instructions". The current date comes from the
server clock; for reproducible runs pass current_date and current_day_of_week
in chat_template_kwargs. To disable the built-in prompt for all requests:
vllm serve … --default-chat-template-kwargs '{"provider_system_prompt": false}'
or per request: extra_body={"chat_template_kwargs": {"provider_system_prompt": False}}.
Limitations and Biases
Bielik-11B-v3.1-Instruct is a quick demonstration that the base model can be easily fine-tuned to achieve compelling and promising performance. It does not have any moderation mechanisms. We're looking forward to engaging with the community in ways to make the model respect guardrails, allowing for deployment in environments requiring moderated outputs.
Bielik-11B-v3.1-Instruct can produce factually incorrect output, and should not be relied on to produce factually accurate data. Bielik-11B-v3.1-Instruct was trained on various public datasets. While great efforts have been taken to clear the training data, it is possible that this model can generate lewd, false, biased or otherwise offensive outputs.
Responsible for training the model
- Krzysztof OciepaSpeakLeash - team leadership, conceptualizing, data preparation, process optimization and oversight of training
- Łukasz FlisCyfronet AGH - coordinating and supervising the training
- Adrian GwoździejSpeakLeash - data preparation and quality assurance
- Krzysztof WróbelSpeakLeash - benchmarks
- Karol JezierskiSpeakLeash - data deduplication and RL environment setup
- Igor CiuciuraSpeakLeash - data preparation
The model could not have been created without the commitment and work of the entire SpeakLeash team, whose contribution is invaluable. Thanks to the hard work of many individuals, it was possible to gather a large amount of content in Polish and establish collaboration between the open-science SpeakLeash project and the HPC center: ACC Cyfronet AGH. Individuals who contributed to the creation of the model: Sebastian Kondracki, Marek Magryś, Sonia Staniek, Waldemar Boszko, Maria Czarkowska, Jacek Chwiła, Kuba Sołtys, Dominika Basaj, Remigiusz Kinas, Marcin Dąbrowski, Anna Przybył, Agnieszka Ratajska, Daria Bartkowiak, Witold Wydmański, Jan Sowa, Grzegorz Anioł, Bartosz Bartnicki, and many other wonderful researchers and enthusiasts of the AI world.
Legal Aspects
EU AI Act Transparency Documentation: Bielik 11B v3 EU Public Summary.pdf
Data Protection and Copyright Requests
For removal requests of personally identifiable information (PII) or of copyrighted content, please contact the respective dataset owners or us directly: biuro@speakleash.org.pl.
Citation
Please cite this model using the following format:
@misc{Bielik11Bv31i,
    title     = {Bielik-11B-v3.1-Instruct model card},
    author    = {Ociepa, Krzysztof and Flis, Łukasz and Gwoździej, Adrian and Wróbel, Krzysztof and Jezierski, Karol and Ciuciura, Igor and {SpeakLeash Team} and {Cyfronet Team}},
    year      = {2026},
    url       = {https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct},
    note      = {Accessed: 2026-10-31}, % change this date
    urldate   = {2026-10-31} % change this date
}
Contact Us
If you have any questions or suggestions, please use the discussion tab. If you want to contact us directly, join our Discord SpeakLeash.
Acknowledgements
We gratefully acknowledge Polish high-performance computing infrastructure PLGrid (HPC Center: ACC Cyfronet AGH) for providing computer facilities and support within computational grant no. [PLG/2026/019559].
This work was supported by the Gaia AI Factory project, funded by the European Union under Grant Agreement No. 101314359 through the EuroHPC Joint Undertaking (EuroHPC JU).
- Downloads last month
- 47
Model tree for speakleash/Bielik-11B-v3.1-Instruct
Base model
speakleash/Bielik-11B-v3-Base-20250730
