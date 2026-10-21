---
id: "e73601fc67c6ed28"
title: "OvisOCR3: a 0.8B OCR model with structured output and cross-page table reconstruction"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbi9h4/ovisocr3_a_08b_ocr_model_with_structured_output"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbi9h4/ovisocr3_a_08b_ocr_model_with_structured_output"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T09:12:49Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Sad_External6106"]
language: "en"
summary: "OvisOCR3 is out, still based on Qwen3.5-0.8B and available under Apache 2.0, with vLLM inference examples. Compared with OvisOCR2’s Markdown parsing, it adds a few useful options: Structured JSON output with bounding boxes, element categories, and content, plus a layout-only mode. Key information extraction using specified fields or a supplied JSON template. Figure descriptions and Mermaid…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 178
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbi9h4/ovisocr3_a_08b_ocr_model_with_structured_output/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# OvisOCR3: a 0.8B OCR model with structured output and cross-page table reconstruction

Reddit · Sad_External6106 · 2026-10-21

OvisOCR3 is out, still based on Qwen3.5-0.8B and available under Apache 2.0, with vLLM inference examples. Compared with OvisOCR2’s Markdown parsing, it adds a few useful options: Structured JSON output with bounding boxes, element categories, and content, plus a layout-only mode. Key information extraction using specified fields or a supplied JSON template. Figure descriptions and Mermaid output for flowcharts. Cross-page table reconstruction: parse the pages first, then use the same model to merge table fragments across adjacent pages. OvisOCR3 results The model card reports 96.74 on OmniDocBench v1.6 , 88.80 on MDPBench , and 82.31 on PureDocBench . The bigger reported gains over OvisOCR2 are on MDPBench (69.00 → 88.80) and PureDocBench (75.10 → 82.31). The bounding-box output and cross-page tables seem particularly useful for document workflows. These are the team’s reported numbers, though; I’d be interested in how well the structure holds up on messy scans and long financial tables. Has anyone tried it locally or compared it with GLM-OCR, PaddleOCR-VL, or MinerU? Curious about VRAM usage and processing speed too. HF model card： https://huggingface.co/ATH-MaaS/OvisOCR3 Demo: https://huggingface.co/spaces/ATH-MaaS/OvisOCR3
