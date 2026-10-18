---
id: "a8ca0bd0ffd944a6"
title: "How Language Models Learned to Read Spreadsheets: A New Survey Maps the Rise of Tabular AI"
url: "https://bioengineer.org/how-language-models-learned-to-read-spreadsheets-a-new-survey-maps-the-rise-of-tabular-ai"
link: "https://bioengineer.org/how-language-models-learned-to-read-spreadsheets-a-new-survey-maps-the-rise-of-tabular-ai"
source: "BIOENGINEER"
domain: "bioengineer.org"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-17T12:41:00Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: []
language: "en"
summary: "A new survey in Artificial Intelligence Review provides the first comprehensive map of language modeling for tabular data, tracing the evolution from from-scratch Transformers to BERT adaptations and ..."
tags: []
orgs: []
topics: ["models & research", "health & science", "jobs & society"]
content_source: "fulltext"
word_count: 1206
paywalled: false
image: "http://www.bing.com/th?id=ONUT.5VcWwxfIT12HAjafffV2UQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# How Language Models Learned to Read Spreadsheets: A New Survey Maps the Rise of Tabular AI

BIOENGINEER · 2026-10-17

Spreadsheets and databases may be the least glamorous artifacts of the digital age, yet they carry much of the world’s operational knowledge, from hospital records and financial ledgers to scientific measurements and industrial logs. A new systematic survey published in Artificial Intelligence Review traces how the language-modeling revolution that transformed natural language processing has been steadily adapted to this heterogeneous, structure-heavy data type, offering the first comprehensive map of a field that has evolved from training Transformers from scratch to coaxing large language models such as GPT and LLaMA into understanding tables with minimal fine-tuning.
The survey, led by Yucheng Ruan and Xiang Lan of the Saw Swee Hock School of Public Health and the Institute of Data Science at the National University of Singapore, together with colleagues including corresponding author Mengling Feng, argues that tabular data deserves the same systematic attention that text and images have received. Unlike sentences or pixels, tables mix numerical and categorical values in a single row, encode relationships across rows and columns, and vary enormously in structure from one domain to the next. That heterogeneity is precisely what makes tabular analysis both valuable and difficult: high predictive performance and robustness on tables would pay off across countless applications, but the data’s irregular nature resists the one-size-fits-all architectures that powered the deep learning boom.
The authors organize the field along several axes. They first categorize the different structural forms tabular data can take and the data types it contains, then review the key datasets used to train models and the downstream tasks used to evaluate them. These tasks range from table question answering, where a model must generate correct answers given a table and a natural-language question, to table retrieval, semantic parsing, metadata prediction, content population, prediction, fact-checking, and generation. Each task carries its own evaluation culture: question answering is judged by execution accuracy, exact match, and F1; retrieval and population tasks rely on ranking metrics such as normalized discounted cumulative gain, mean average precision, and mean reciprocal rank; prediction tasks use classification and regression measures including F1, AUROC, accuracy, root mean square error, mean absolute error, and the coefficient of determination.
A central technical contribution of the survey is its summary of the modeling machinery itself: the widely adopted data processing methods that convert tables into model-friendly inputs, the popular architectures that consume them, and the training objectives that shape what the models learn. Early techniques concentrated on pre-training Transformer architectures from scratch on tabular corpora. The Transformer, with its attention mechanism, can in principle weigh the relevance of every cell against every other cell, making it a natural fit for the relational structure of tables. But training from scratch proved costly and prone to scalability issues, since tabular datasets are often smaller and noisier than the massive text corpora that fueled models like BERT and GPT.
The field’s second wave responded by leveraging pre-trained language models rather than building new ones. Methods adapting BERT-style encoders to tables require far less data and yield enhanced performance, because they inherit the general linguistic and numerical competence acquired during pre-training on text. The survey documents this evolution in detail, showing how researchers reformulated tables as sequences of tokens, designed specialized embedding schemes for columns and values, and adapted training objectives so that models could learn the semantics of rows and columns rather than just the statistics of individual fields.
The third and most recent phase arrived with large language models such as GPT and LLaMA, which the survey credits with revolutionizing the field. These models facilitate more advanced and diverse applications with minimal fine-tuning: a model that already understands language can be prompted or lightly adapted to answer questions about a table, generate SQL queries, populate missing cells, or check facts against tabular evidence. The authors trace how the paradigm shifted from adapting traditional pre-training and pre-trained language models to the utilization of large language models, a transition that lowered the barrier to entry for practitioners who lack the resources to train bespoke models.
The survey does not shy away from the field’s methodological growing pains. In an appendix devoted to evaluation metrics, the authors note that many of the measures borrowed from natural language processing, such as BLEU, were originally designed for machine translation and are not well aligned with the structural and semantic requirements of tabular data. BLEU, which compares n-gram matches between generated text and reference texts, has been widely criticized for failing to capture cell-level factual accuracy and logical consistency across rows and columns. The survey cites work showing these limitations and argues that existing NLP metrics are insufficient for tabular generation, pointing to a growing need for standardized, structure-aware benchmarks tailored specifically to tabular data.
The authors also provide a practical guide to metric selection, grouping commonly used measures by task type, evaluation granularity, strengths, and limitations. Answer-based tasks such as table question answering are commonly evaluated with exact match, F1, or execution accuracy, whereas retrieval and population tasks require ranking-based metrics such as NDCG, MAP, MRR, and precision or recall at n. Generation tasks demand additional attention to structural validity and semantic correctness, since a generated table can be superficially fluent yet factually wrong at the cell level or logically inconsistent across its rows. This kind of task-aware metric selection, the survey suggests, is as important to progress as the architectures themselves.
Beyond cataloguing what exists, the survey identifies persistent challenges and potential future research directions. The heterogeneous nature of tabular data continues to complicate generalization: a model trained on clinical records may transfer poorly to financial data, and structural variation across tables complicates the design of universal representations. Evaluation remains fragmented, with performance results reported in original research papers across a patchwork of datasets and metrics, making head-to-head comparisons difficult. The survey’s accompanying performance summaries of common one-dimensional and two-dimensional tabular datasets, together with its GitHub repository of surveyed literature, are intended to give researchers a common reference point as the field matures.
For a discipline that has watched language models conquer text, code, and conversation, the message of this survey is that tables are the next frontier worth serious attention. The evolution it documents, from resource-hungry from-scratch Transformers to data-efficient BERT adaptations to versatile large language models, mirrors the broader trajectory of modern machine learning, but the destination is distinct: models that can genuinely reason about the rows, columns, and relationships that structure so much of the world’s recorded information. Whether the field can build the structure-aware benchmarks and robust evaluation practices it now lacks will determine how quickly that frontier falls.
Subject of Research: Language modeling techniques for tabular data, from Transformer pre-training to large language models
Article Title: Language modeling on tabular data: a survey of foundations, techniques and evolution
Article References: Ruan, Y., Lan, X., Ma, J., Dong, Y., He, K., & Feng, M. (2026). Language modeling on tabular data: a survey of foundations, techniques and evolution. Artificial Intelligence Review. https://doi.org/10.1007/s10462-026-11726-z
Image Credits: AI Generated
DOI: 10.1007/s10462-026-11726-z
Keywords: language modeling, tabular data, Transformers, BERT, large language models, GPT, LLaMA, machine learning, natural language processing, survey, Language, modeling
News Source: Denise Maddox. (October 17, 2026). How Language Models Learned to Read Spreadsheets: A New Survey Maps the Rise of Tabular AI. Scienmag.
