---
id: "58ec4dfbbf10f6c4"
title: "nvidia/Nemotron-3.5-Embed-1B-BF16 · Hugging Face"
url: "https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16"
link: "https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "community"
collector: "reddit"
date: "2026-10-15T23:22:20Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jacek2023"]
language: "en"
summary: "Nemotron-3.5-Embed-1B-BF16 is a versatile embedding model developed by NVIDIA for multimodal and multilingual question-answering retrieval. The model can embed a document page in the form of an image, text, or combined image–text input. Documents can be retrieved given a user query in text form. The model supports page images containing text, tables, charts, and infographics. For text retrieval,…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "China", "Hugging Face", "Google"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 2425
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x70qhu/nvidianemotron35embed1bbf16_hugging_face/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# nvidia/Nemotron-3.5-Embed-1B-BF16 · Hugging Face

Hugging Face · jacek2023 · 2026-10-15

Instructions to use nvidia/Nemotron-3.5-Embed-1B-BF16 with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
- Libraries
-  sentence-transformers How to use nvidia/Nemotron-3.5-Embed-1B-BF16 with sentence-transformers: from sentence_transformers import SentenceTransformer
model = SentenceTransformer("nvidia/Nemotron-3.5-Embed-1B-BF16")
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium."
]
embeddings = model.encode(sentences)
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
-  Transformers How to use nvidia/Nemotron-3.5-Embed-1B-BF16 with Transformers: # pip install -U transformers accelerate
# Load model directly
from transformers import AutoProcessor, AutoModel
processor = AutoProcessor.from_pretrained("nvidia/Nemotron-3.5-Embed-1B-BF16")
model = AutoModel.from_pretrained("nvidia/Nemotron-3.5-Embed-1B-BF16", device_map="auto")
- Notebooks
- Google Colab
- Kaggle
Nemotron-3.5-Embed-1B-BF16 Overview
Description:
Nemotron-3.5-Embed-1B-BF16 is a versatile embedding model developed by NVIDIA for multimodal and multilingual question-answering retrieval. The model can embed a document page in the form of an image, text, or combined image–text input. Documents can be retrieved given a user query in text form. The model supports page images containing text, tables, charts, and infographics. For text retrieval, the model was evaluated across 34 languages: English, Arabic, Assamese, Bengali, Bulgarian, Chinese, Danish, Dutch, Finnish, French, German, Hindi, Hinglish, Indonesian, Italian, Japanese, Korean, Malay, Marathi, Nepali, Norwegian, Persian, Portuguese, Romanian, Russian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Ukrainian, Urdu, and Vietnamese. For image retrieval, it was evaluated across 18 languages: Arabic, Bengali, Chinese, English, Persian, Finnish, French, German, Hindi, Indonesian, Japanese, Korean, Russian, Spanish, Swahili, Telugu, Thai, and Yoruba. The model may support additional languages beyond these evaluation sets.
This model is ready for commercial or non-commercial use.
License/Terms of Use:
Governing Download Terms: Use of the model is governed by the OpenMDW License Agreement, version 1.1 (OpenMDW-1.1). 
Additional Information: The Ministral-3-3B-Instruct-2512-BF16 and Ministral-3-8B-Instruct-2512-BF16 base models are governed by the Apache License, Version 2.0.
Deployment Geography:
Global
Use Case:
The Nemotron-3.5-Embed-1B-BF16 is suitable for users who want to build a multimodal question-and-answer application over a large corpus, leveraging the latest dense retrieval technology. The input of the model is a text or a document image, and the output is a fixed-size embedding vector. The embedding model is a bi-encoder that supports context in textual format (e.g. the query or the OCR text of a page or a section of a document) or the image of a document page. Typically, the embedding model is used first to embed (vectorize) the whole corpus (document images or text chunks), and embeddings are stored in a vector database associated to its raw content (image or text). Then at inference time, the embedding model is used to embed the query. The model generates dense vector embeddings from text or image inputs, enabling multimodal retrieval, semantic search, and (agentic) RAG workflows.
Release Date:
Hugging Face 10/20/2026 via https://huggingface.co/nvidia/Nemotron-3.5-Embed-1B-BF16
Model Architecture:
Architecture Type: Transformer 
Network Architecture: Nemotron-3.5-Embed-1B-BF16 consists of a Pixtral vision encoder initialized from mistralai/Ministral-3-3B-Instruct-2512-BF16 and a language model initialized from nvidia/Nemotron-3-Embed-1B-BF16. 
Number of model parameters: 1.55B
The Nemotron-3.5-Embed-1B-BF16 model was distilled from the Nemotron-3.5-Embed-8B-BF16 embedding teacher using combined cosine distance (COS) and mean squared error (MSE) losses on multilingual text and image retrieval data. Its language-model component was initialized from Nemotron-3-Embed-1B-BF16 and kept frozen during distillation. Consequently, Nemotron-3.5-Embed-1B-BF16 shares the same text embedding space as Nemotron-3-Embed-1B-BF16 while adding image retrieval capabilities. The vision encoder and multimodal projection were fine-tuned on image and combined image-text datasets.
Input:
Input Type(s): Text, Image 
Input Format(s): Text: String; Image: Red, Green, Blue (RGB) 
Input Parameters: Text: One-Dimensional (1D), Image: Two-Dimensional (2D) 
Other Properties Related to Input: The model supports image and/or text inputs. For queries, the model accepts text input only. For documents, it accepts an image, text, or a combination of image + text. The default image longest_edge is 1,120 pixels, and it can be increased up to 1,540 pixels. The model’s max context length is 32,768 tokens.
Output:
Output Type(s): Embeddings
Output Format: Vector 
Output Parameters: One-Dimensional (1D) per input 
Other Properties Related to Output: Token-level hidden states are mean-pooled and then L2-normalized to produce one 2048-dimensional embedding vector for each input. The model also supports dynamic embedding sizes by truncating the vector from the end (e.g., retaining the first 1024 or 512 dimensions). The truncated embeddings remain effective for retrieval, provided they are L2-normalized after truncation.
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.
Installation
Create a Python 3.12 environment for the Transformers and Sentence Transformers examples:
uv venv --python 3.12 .venv-transformers
source .venv-transformers/bin/activate
uv pip install torch "transformers==5.20.0" accelerate pillow packaging ninja
uv pip install flash-attn --no-build-isolation
The examples use Flash Attention 2 and were tested with transformers==5.20.0. The checkpoint uses TokenizersBackend and does not require mistral_common.
Model training and evaluations used transformers==5.12.1. Example outputs can vary with hardware and runtime.
Transformers Usage
Generate embeddings for text queries and documents containing text, images, or both.
import torch
import torch.nn.functional as F
from PIL import Image
from transformers import AutoModel, AutoProcessor
from transformers.image_utils import load_image
MODEL_PATH = "nvidia/Nemotron-3.5-Embed-1B-BF16"  # Or a local checkpoint directory.
DOCUMENT_NAMES = ["nemo_image_text", "nemo_text", "nemo_image", "biology_text"]
IMAGE_URL = "https://docs.nvidia.com/nemo-framework/user-guide/24.07/_images/nemo-llm-mm-stack.png"
MAX_MODEL_LEN = 32768
DEVICE = "cuda:0"
def main() -> None:
    if not torch.cuda.is_available():
        raise RuntimeError("This bfloat16 example requires a CUDA GPU.")
    processor = AutoProcessor.from_pretrained(MODEL_PATH)
    model = AutoModel.from_pretrained(
        MODEL_PATH,
        dtype=torch.bfloat16,
        device_map={"": DEVICE},
        attn_implementation="flash_attention_2",
    ).eval()
    def embed(
        prefix: str,
        text: str | None = None,
        image: Image.Image | None = None,
    ) -> torch.Tensor:
        content = [] if image is None else [{"type": "image", "image": image}]
        if text is not None:
            content.append({"type": "text", "text": text})
        inputs = processor.apply_chat_template(
            [
                {"role": "system", "content": prefix},
                {"role": "user", "content": content},
            ],
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        )
        if inputs["input_ids"].shape[-1] > MAX_MODEL_LEN:
            raise ValueError("Input exceeds 32768 tokens; shorten the text or resize the image.")
        inputs = inputs.to(DEVICE)
        if image is not None:
            inputs["pixel_values"] = inputs["pixel_values"].to(model.dtype)
        with torch.inference_mode():
            hidden = model(**inputs).last_hidden_state
            mask = inputs["attention_mask"].unsqueeze(-1)
            embedding = (hidden * mask).sum(1) / mask.sum(1)
        return F.normalize(embedding.float(), dim=-1)
    image = load_image(IMAGE_URL)
    query_embedding = embed("query:", "What is NVIDIA NeMo Framework?")
    nemo_text = "NeMo Framework offers comprehensive functionalities for developing both LLMs and Multimodal Models."
    biology_text = "A biological foundation model designed to analyze and generate DNA, RNA, and protein sequences."
    document_embeddings = torch.cat(
        [
            embed("passage:", nemo_text, image),
            embed("passage:", nemo_text),
            embed("passage:", image=image),
            embed("passage:", biology_text),
        ]
    )
    scores = query_embedding @ document_embeddings.T
    print(f"query_embedding.shape={tuple(query_embedding.shape)}")
    print(f"document_embeddings.shape={tuple(document_embeddings.shape)}")
    for name, score in zip(DOCUMENT_NAMES, scores[0]):
        print(f"{name}_similarity={score.item():.6f}")
if __name__ == "__main__":
    main()
Example output (scores can vary with hardware and runtime):
query_embedding.shape=(1, 2048)
document_embeddings.shape=(4, 2048)
nemo_image_text_similarity=0.521734
nemo_text_similarity=0.457723
nemo_image_similarity=0.509049
biology_text_similarity=0.112573
Sentence Transformers Usage
In the same environment, install Sentence Transformers:
uv pip install "sentence-transformers[image]>5.4" "transformers==5.20.0"
Generate embeddings for text, images, or combined text and images with Sentence Transformers.
import torch
from sentence_transformers import SentenceTransformer
from transformers.image_utils import load_image
MODEL_PATH = "nvidia/Nemotron-3.5-Embed-1B-BF16"  # Or a local checkpoint directory.
DOCUMENT_NAMES = ["nemo_image_text", "nemo_text", "nemo_image", "biology_text"]
DEVICE = "cuda:0"
IMAGE_URL = "https://docs.nvidia.com/nemo-framework/user-guide/24.07/_images/nemo-llm-mm-stack.png"
def main() -> None:
    """Run text and multimodal retrieval with the exported Sentence Transformers checkpoint."""
    if not torch.cuda.is_available():
        raise RuntimeError("This bfloat16 example requires a CUDA GPU.")
    model = SentenceTransformer(
        MODEL_PATH,
        device=DEVICE,
        model_kwargs={
            "attn_implementation": "flash_attention_2",
            "dtype": torch.bfloat16,
        },
    )
    query = "What is NVIDIA NeMo Framework?"
    nemo_text = "NeMo Framework offers comprehensive functionalities for developing both LLMs and Multimodal Models."
    biology_text = "A biological foundation model designed to analyze and generate DNA, RNA, and protein sequences."
    image = load_image(IMAGE_URL)
    query_embedding = model.encode_query([query], convert_to_tensor=True)
    text_embeddings = model.encode_document([nemo_text, biology_text], convert_to_tensor=True)
    image_embedding = model.encode_document([image], convert_to_tensor=True)
    multimodal_embedding = model.encode_document([{"image": image, "text": nemo_text}], convert_to_tensor=True)
    document_embeddings = torch.cat(
        [
            multimodal_embedding,
            text_embeddings[:1],
            image_embedding,
            text_embeddings[1:],
        ]
    )
    scores = model.similarity(query_embedding, document_embeddings)
    print(f"query_embedding.shape={tuple(query_embedding.shape)}")
    print(f"document_embeddings.shape={tuple(document_embeddings.shape)}")
    for name, score in zip(DOCUMENT_NAMES, scores[0]):
        print(f"{name}_similarity={score.item():.6f}")
if __name__ == "__main__":
    main()
Example output (scores can vary with hardware and runtime):
query_embedding.shape=(1, 2048)
document_embeddings.shape=(4, 2048)
nemo_image_text_similarity=0.521878
nemo_text_similarity=0.457693
nemo_image_similarity=0.509208
biology_text_similarity=0.112972
vLLM Usage
Generate embeddings for text, images, and combined image and text inputs using the vLLM Python API or an HTTP server.
Dependencies
Create a separate Python environment for vLLM. Set MODEL_PATH to the Hugging Face model ID or a local checkpoint directory:
uv venv --python 3.12 .venv-vllm
source .venv-vllm/bin/activate
uv pip install "vllm==0.31.0" "transformers<5.17.0" pillow httpx numpy
export MODEL_PATH="nvidia/Nemotron-3.5-Embed-1B-BF16"
These examples use vLLM 0.31.0, which requires transformers>=5.10.4,<5.18.0. Keep the vLLM environment separate from the Transformers 5.20.0 environment above. Image preprocessing uses the checkpoint's configured longest-edge limit of 1,120 pixels. The 32,768-token context includes both text and image tokens.
Offline Python
Use query: for text queries and passage: for documents. Format each input
with the model's chat template and pass images through multi_modal_data:
import os
import numpy as np
from transformers import AutoProcessor
from transformers.image_utils import load_image
from vllm import LLM
from vllm.config import PoolerConfig
MODEL_PATH = os.environ["MODEL_PATH"]
DOCUMENT_NAMES = ["nemo_image_text", "nemo_text", "nemo_image", "biology_text"]
IMAGE_URL = "https://docs.nvidia.com/nemo-framework/user-guide/24.07/_images/nemo-llm-mm-stack.png"
MAX_MODEL_LEN = 32768
def main() -> None:
    processor = AutoProcessor.from_pretrained(MODEL_PATH)
    model = LLM(
        model=MODEL_PATH,
        dtype="bfloat16",
        pooler_config=PoolerConfig(
            task="embed",
            pooling_type="MEAN",
            use_activation=True,
        ),
        max_model_len=MAX_MODEL_LEN,
    )
    image = load_image(IMAGE_URL)
    nemo_text = "NeMo Framework offers comprehensive functionalities for developing both LLMs and Multimodal Models."
    biology_text = "A biological foundation model designed to analyze and generate DNA, RNA, and protein sequences."
    samples = [
        ("query:", "What is NVIDIA NeMo Framework?", None),
        ("passage:", nemo_text, image),
        ("passage:", nemo_text, None),
        ("passage:", None, image),
        ("passage:", biology_text, None),
    ]
    prompts = []
    for prefix, text, image in samples:
        content = [] if image is None else [{"type": "image", "image": image}]
        if text is not None:
            content.append({"type": "text", "text": text})
        conversation = [
            {"role": "system", "content": prefix},
            {"role": "user", "content": content},
        ]
        prompt = {"prompt": processor.apply_chat_template(conversation, tokenize=False)}
        if image is not None:
            prompt["multi_modal_data"] = {"image": image}
        prompts.append(prompt)
    # Preserve the template output without adding BOS/EOS tokens.
    outputs = model.embed(prompts, tokenization_kwargs={"add_special_tokens": False})
    embeddings = np.asarray([result.outputs.embedding for result in outputs], dtype=np.float32)
    query_embedding, document_embeddings = embeddings[:1], embeddings[1:]
    scores = query_embedding @ document_embeddings.T
    print(f"query_embedding.shape={query_embedding.shape}")
    print(f"document_embeddings.shape={document_embeddings.shape}")
    for name, score in zip(DOCUMENT_NAMES, scores[0]):
        print(f"{name}_similarity={score:.6f}")
if __name__ == "__main__":
    main()
Example output (scores can vary with hardware and runtime):
query_embedding.shape=(1, 2048)
document_embeddings.shape=(4, 2048)
nemo_image_text_similarity=0.521628
nemo_text_similarity=0.458030
nemo_image_similarity=0.508873
biology_text_similarity=0.112930
The example returns one query embedding and four document embeddings, each with 2,048 dimensions. The embeddings are L2-normalized, so their dot products give cosine similarity scores. Higher scores indicate greater similarity to the query.
Online Serving
Start a local embedding server:
vllm serve "$MODEL_PATH" \
    --served-model-name "nvidia/Nemotron-3.5-Embed-1B-BF16" \
    --dtype bfloat16 \
    --max-model-len 32768 \
    --chat-template-content-format openai \
    --host 127.0.0.1 \
    --port 8000
After the server is ready, open another terminal in the same directory and activate the vLLM environment:
source .venv-vllm/bin/activate
Run the following Python client to send the query and a batch of four documents to /v2/embed. input_type selects the query or document prefix from the checkpoint. The client sets truncate="END" to truncate text from the end. If image tokens alone exceed the context limit, reduce the image resolution.
import httpx
import numpy as np
MODEL_ID = "nvidia/Nemotron-3.5-Embed-1B-BF16"
ENDPOINT = "http://127.0.0.1:8000/v2/embed"
IMAGE_URL = "https://docs.nvidia.com/nemo-framework/user-guide/24.07/_images/nemo-llm-mm-stack.png"
DOCUMENT_NAMES = ["nemo_image_text", "nemo_text", "nemo_image", "biology_text"]
def embed(client: httpx.Client, input_type: str, inputs: list[dict]) -> np.ndarray:
    response = client.post(
        ENDPOINT,
        json={
            "model": MODEL_ID,
            "input_type": input_type,
            "inputs": inputs,
            "embedding_types": ["float"],
            "truncate": "END",
        },
    )
    response.raise_for_status()
    return np.asarray(response.json()["embeddings"]["float"], dtype=np.float32)
def main() -> None:
    query = "What is NVIDIA NeMo Framework?"
    nemo_text = "NeMo Framework offers comprehensive functionalities for developing both LLMs and Multimodal Models."
    biology_text = "A biological foundation model designed to analyze and generate DNA, RNA, and protein sequences."
    image_block = {"type": "image_url", "image_url": {"url": IMAGE_URL}}
    documents = [
        {"content": [image_block, {"type": "text", "text": nemo_text}]},
        {"content": [{"type": "text", "text": nemo_text}]},
        {"content": [image_block]},
        {"content": [{"type": "text", "text": biology_text}]},
    ]
    with httpx.Client(timeout=120.0) as client:
        query_embedding = embed(client, "query", [{"content": [{"type": "text", "text": query}]}])[0]
        document_embeddings = embed(client, "document", documents)
    print(f"query_embedding.shape={query_embedding.shape}")
    print(f"document_embeddings.shape={document_embeddings.shape}")
    for name, score in zip(DOCUMENT_NAMES, query_embedding @ document_embeddings.T):
        print(f"{name}_similarity={score:.6f}")
if __name__ == "__main__":
    main()
Example output (scores can vary with hardware and runtime):
query_embedding.shape=(2048,)
document_embeddings.shape=(4, 2048)
nemo_image_text_similarity=0.521529
nemo_text_similarity=0.457598
nemo_image_similarity=0.508731
biology_text_similarity=0.112908
Troubleshooting: Flash Attention 2 with older Transformers versions
For the Transformers and Sentence Transformers examples, flash_attention_2
can cause CUDA errors or incorrect outputs with image inputs in Transformers
5.17.0, 5.18.0, and 5.19.0. Upgrade to transformers==5.20.0.
Software Integration:
Runtime Engine(s):
- Transformers
- Sentence Transformers
- vLLM
Supported Hardware Microarchitecture Compatibility:
- NVIDIA Ampere
- NVIDIA Blackwell
- NVIDIA Hopper
Supported Operating System(s): Linux
Model Version(s):
Nemotron-3.5-Embed-1B-BF16
Training, Testing, and Evaluation Datasets:
Training Dataset:
Data Modality:
- Image
- Text
Image Training Data Size: 2.3M samples containing images, with or without accompanying text 
Text Training Data Size: 8.5M+ text-only data samples 
Data Collection Method by dataset: Automated, Manually-Labeled, Synthetic 
Labeling Method by dataset: Automated, Manually-Labeled, Synthetic 
Properties: Training was conducted using publicly available, commercially permissible datasets and synthetically generated datasets.
Public Datasets:
The language model of Nemotron-3.5-Embed-1B-BF16 was trained with text-only datasets that have been listed in Nemotron-3-Embed-1B-BF16's Model Card. In addition to these datasets we have used the following publicly available datasets to train the vision encoder and multimodal projector with image-only and image + text inputs.
Synthetic datasets were created either by generating queries from seed documents or by generating complete question–answer pairs through LLM-based prompting using the models listed below.
Testing Dataset:
Data Collection Method by dataset: Not Applicable
Labeling Method by dataset: Not Applicable
Properties: Not Applicable. Model quality was assessed using the evaluation benchmark datasets described in the Evaluation Dataset subsection.
Evaluation Dataset:
Benchmark:
Benchmark Score: NDCG@10 
Data Collection Method by dataset: Automated, Manually-Labeled, Synthetic 
Labeling Method by dataset: Automated, Manually-Labeled, Synthetic 
Properties: ViDoRe V3 is a visual document retrieval benchmark covering 8 public and 2 private datasets across professional domains. MIRACL-VISION is a multilingual visual retrieval dataset for 18 different languages. It is an extension of MIRACL, a popular text-only multilingual retrieval dataset.
Inference:
Acceleration Engine: Transformers, PyTorch, vLLM 
Hardware Requirements (GPU Architecture, Model):
- NVIDIA Ampere (A100 80GB)
- NVIDIA Blackwell (GB200 186GB)
- NVIDIA Hopper (H100 80GB)
Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.
Please make sure you have proper rights and permissions for all input image and video content; if image or video includes people, personal health information, or intellectual property, the image or video generated will not blur or maintain proportions of image subjects included.
For more detailed information on ethical considerations for this model, please see the Bias, Explainability, Privacy, and Safety & Security Subcards.
Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns here.
Bias
Explainability
Privacy
The datasets used to train this model were reviewed before release. Please review NVIDIA’s Privacy Policy (https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) for more information.
Safety
- Downloads last month
- 779
Model tree for nvidia/Nemotron-3.5-Embed-1B-BF16
Base model
mistralai/Ministral-3-3B-Base-2512
