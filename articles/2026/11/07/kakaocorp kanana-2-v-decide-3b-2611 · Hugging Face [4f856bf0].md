---
id: "4f856bf0d9c7e1bf"
title: "kakaocorp/kanana-2-v-decide-3b-2611 · Hugging Face"
url: "https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611"
link: "https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-11-07T13:30:06Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["pmttyji"]
language: "en"
summary: "Kanana-2-v-decide-3b-2611 is Kakao's decision model. Given an input, it answers typed questions — selecting one of several options ( choice ), answering yes or no ( noul ), or rating on an ordered scale ( score ) — and returns a probability for each possible answer. It does not generate text. The input, called the state , may be text, a JSON object or array, or a chat history, optionally…"
tags: ["r/LocalLLaMA"]
orgs: ["Google", "Hugging Face"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 915
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xq6es4/kakaocorpkanana2vdecide3b2611_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# kakaocorp/kanana-2-v-decide-3b-2611 · Hugging Face

Hugging Face · pmttyji · 2026-11-07

Instructions to use kakaocorp/kanana-2-v-decide-3b-2611 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  Transformers How to use kakaocorp/kanana-2-v-decide-3b-2611 with Transformers: # Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("zero-shot-classification", model="kakaocorp/kanana-2-v-decide-3b-2611", trust_remote_code=True) # pip install -U transformers accelerate
# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("kakaocorp/kanana-2-v-decide-3b-2611", trust_remote_code=True, device_map="auto")
- Notebooks
- Google Colab
- Kaggle
🤗 Kanana-2-v-decide-3b-2611 | 📕 Blog (Korean)
Kanana-2-v-decide-3b-2611
News 🔥
- 2026/11/06: 🤗 Released the Kanana-2-v-decide-3b-2611 model weights.
Introduction
Kanana-2-v-decide-3b-2611 is Kakao's decision model. Given an input, it answers typed questions — selecting one of several options (choice), answering yes or no (noul), or rating on an ordered scale (score) — and returns a probability for each possible answer. It does not generate text. The input, called the state, may be text, a JSON object or array, or a chat history, optionally accompanied by images.
The model is built on Kanana-2-v-3b, which pairs the Kanana-2-3b language model with the Kanana vision encoder. Each question is encoded together with the state into a single embedding, and each candidate answer into another; a softmax over the cosine similarities between these embeddings yields the answer distribution.
Highlights
- Public benchmarks: Achieves the highest average (61.23) across Decision Index and Decision Index Vision among the models compared, including the top score on Decision Index Vision.
- Calibrated answers, no generation: Returns a full probability distribution over the supplied options for every question, with any number of questions per request.
- Multimodal input: Accepts text, JSON, or chat messages with up to 10 images and up to 20,480 tokens.
- Korean decisions: Scores 72.50 on Kanana Decision Bench (text), our Korean evaluation set — 18 points ahead of the next-best model compared.
Model Downloads
Decision Performance
The best score in each column is shown in bold. The average is calculated from the two displayed public benchmark scores.
† Kakao's in-house Korean decision evaluation set (text).
Deployment
Requirements
pip install -r requirements.txt
transformers
import torch
from transformers import AutoModel
model = AutoModel.from_pretrained("kakaocorp/kanana-2-v-decide-3b-2611", trust_remote_code=True,
                                  dtype=torch.bfloat16).to("cuda")
result = model.system_one(
    state="The item I ordered arrived damaged. Please replace it.",
    questions={
        "category": {"type": "choice", "instructions": "Classify the customer's inquiry.",
                     "criteria": {"delivery": "Delivery inquiry", "exchange": "Replacement request", "payment": "Payment inquiry"}},
        "damaged": {"type": "noul", "instructions": "Is the item damaged?"},
        "sentiment": {"type": "score", "instructions": "How positive is the customer's sentiment?",
                      "criteria": ["Negative", "Neutral", "Positive"]},
    },
)
print(result["answers"]["category"]["choice"])   # "exchange"
print(result["answers"]["damaged"]["noul"])      # probability of yes (0-1)
print(result["answers"]["sentiment"]["score"])   # expected level (0-2)
Images can be attached to the state as local paths, URLs, data:image/...;base64, URIs, or PIL images:
result = model.system_one(state="The customer attached a photo of the delivered item.",
                          images=["photo.jpg"],
                          questions={"damaged": {"type": "noul", "instructions": "Is the item damaged?"}})
The same request can also be made through a pipeline:
from transformers import pipeline
decide = pipeline("decision", model="kakaocorp/kanana-2-v-decide-3b-2611", trust_remote_code=True, device=0)
decide(state="The parcel never arrived.", questions={"refund": {"type": "noul", "instructions": "Does the customer want a refund?"}})
Serving over HTTP
server_kanana_v_decide.py exposes system_one through the System One API (POST /v1/systemone,
GET /v1/models, GET /health) using only the Python standard library, so existing System One clients can
connect simply by changing their base URL:
python server_kanana_v_decide.py --port 8000          # from the model directory, or --model <dir or Hub id>
curl -s localhost:8000/v1/systemone -H 'content-type: application/json' -d '{
  "state": "The parcel never arrived.",
  "questions": {"refund": {"type": "noul", "instructions": "Does the customer want a refund?"}}
}'
Requests accept the same inputs as system_one (state, questions, images, state_format, temperature,
query_schemas); image inputs must be given as base64 data URLs. Requests are processed one at a time. To
require Authorization: Bearer <key>, set DECISION_API_KEY. The server binds to 127.0.0.1 by default whether
or not a key is set, so be sure to set a key before exposing it with --host.
Questions and answers
confidence is the highest probability minus the mean of the remaining probabilities. Note that the
probabilities are relative to the candidates supplied: adding or changing an option changes the distribution.
temperature (default 1.0) divides the logits, so values above 1 produce a flatter distribution.
Additional system_one inputs:
- state_format: one of "text", "json", or "messages". By default, strings are treated as text and
objects or arrays as JSON; use "messages" for chat histories ([{"role": ..., "content": [...]}],
containing text and image parts).
- query_schemas: controls, for each question, which options are included in the query (null hides them).
Notes
- By default, the options for choice and noul questions are included in the query; score levels are always included.
- By default, overlong states are shortened while preserving their beginning and end; images are kept.
Overlong candidate descriptions may also be shortened. Use --strict-inputs on the HTTP server to reject
overlong inputs instead.
- All images are converted to RGB: transparency in RGBA images is composited onto white, and EXIF orientation
is not applied, so normalize the orientation of EXIF-tagged images beforehand. The processor first resizes
images to at most 1,638,400 pixels, then enlarges small images to at least 65,536 pixels before splitting
them into patches. Extreme aspect ratios are not supported. See processing_kanana_v_decide.py for details.
- Each input is encoded in a separate forward pass. Candidate embeddings are cached across calls, keyed by token IDs.
- Video input is not supported.
License
The model weights are released under the KananaOpenLicense.
Citation
@misc{kanana2vdecide2026,
  title = {{Kanana-2-v-decide}},
  author = {Sunghyo Chung and Juyoung Lee},
  year = {2026},
  url = {https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611}
}
Contact
- Technical Support: kanana-mmapp@kakaocorp.com
- Business & Partnership Contact: alpha.k@kakaocorp.com
- Downloads last month
- 545
