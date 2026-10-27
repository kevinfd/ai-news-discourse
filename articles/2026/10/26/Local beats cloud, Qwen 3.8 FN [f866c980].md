---
id: "f866c980d8c0f558"
title: "Local beats cloud, Qwen 3.8 FN"
url: "https://reddit.com/r/LocalLLaMA/comments/1xg3rms/local_beats_cloud_qwen_38_fn"
link: "https://reddit.com/r/LocalLLaMA/comments/1xg3rms/local_beats_cloud_qwen_38_fn"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T17:43:57Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["dr_lm"]
language: "en"
summary: "I thought y'all might be interested in a legit \"local is better\" use case. TLDR: Qwen 3.8 FN solved a work problem that requires the privacy of a local model, with the same skill as a frontier cloud model. I run an MSc dissertation module at work which involves tracking students, supervisors, offered projects, project choices, examiners and eventually grades. None of it is super complex, but…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["jobs & society", "models & research", "chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 583
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xg3rms/local_beats_cloud_qwen_38_fn/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Local beats cloud, Qwen 3.8 FN

Reddit · dr_lm · 2026-10-26

I thought y'all might be interested in a legit "local is better" use case. TLDR: Qwen 3.8 FN solved a work problem that requires the privacy of a local model, with the same skill as a frontier cloud model. I run an MSc dissertation module at work which involves tracking students, supervisors, offered projects, project choices, examiners and eventually grades. None of it is super complex, but it's all annoying -- students choose their top five projects from an offered list, but supervisors also choose students; supervisors can't mark their own students work but can mark others etc. The kind of low level matching work that, done manually, fries my brain. A simple relational database is the obvious solution but, before gen AI, nobody had time to code up a database for processes that only happen once per year. There's also the ingest problem: data comes from ms forms, from the student records database, and from moodle, all with csv export in different formats, with e.g. different arrangement and spelling of middle names etc. I'm a heavy codex user, but I can't be offering up the names and emails of students and supervisors, nor the details of early-stage research projects, to the cloud. This year, for the first time, I've had the confidence to address this with a local model: Qwen 3.8 flash next, running in opencode with a vllm backend. It's sandboxed in a docker container and has read only access to all its input data and write access to its workspace. It's got web access, python, pypdf, libreoffice and can pip install into a venv, and that's about it. First thing to say is it's faster than codex, and noticeably so. Part of this is just the cloud -- when this runs a python script to generate a docx booklet of projects from the sqllite db directly off an SSD, it takes a few seconds, including thinking time to process the request. Second is intelligence. It's bright enough to understand my requests and to infer the next steps. It can handle heterogenous data structures from different sources and combine them. It wrote an ingest function to read csvs into the db, but also manual edits to allow repeatable rebuilds from the sources, fixing typos and grammar that were present in the ms form each time. Third is the right level of persistence. For me -- and this is likely a skill issue on my part -- hermes agent and pi were too persistent with the same model and backend. They would decide on the next step without checking and go off the reservation, then need to be pulled back. Opencode feels much better balanced and more like codex (which is high praise -- I really like codex). Finally, overall quality. Codex and gpt 5.6 have been good to me, 6 astra and 6.1 sol less so for my particular use cases. I'm not gonna say Q3.8FN is better, but, for this particular job, I don't think it's any worse . It does make me think I should probably start using this more for coding, as I've had some frustrating times with gpt 6 models in codex recently. If it weren't for VRAM shortages, this would be the future: everyone having a "good enough" LLM on their own hardware with, say 64-128GB VRAM being standard. It's so nice to not be constantly worrying about privacy and GDPR when interacting with agents, and to know that none of this leaves my hard disk.
