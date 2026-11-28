---
id: "99ecbe4c1c316e51"
title: "Blending Unsupervised Clustering Tasks with Scikit-LLM"
url: "https://kdnuggets.com/blending-unsupervised-clustering-tasks-with-scikit-llm"
link: "https://kdnuggets.com/blending-unsupervised-clustering-tasks-with-scikit-llm"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-27T15:00:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Iván Palomares Carrascosa"]
language: "en"
summary: "A two-stage pipeline for document clustering and LLM-driven topic discovery, aided by Scikit-LLM's summarization tools."
tags: []
orgs: ["OpenAI", "Google"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1172
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-blending-unsupervised-clustering-tasks-with-scikit-llm-feature.webp"
discussion_url: null
score: null
comments: null
community: null
---

# Blending Unsupervised Clustering Tasks with Scikit-LLM

KDnuggets · Iván Palomares Carrascosa · 2026-11-27

Blending Unsupervised Clustering Tasks with Scikit-LLM
A two-stage pipeline for document clustering and LLM-driven topic discovery, aided by Scikit-LLM's summarization tools.
Introduction
Traditional approaches for unsupervised text clustering usually produce groups that are defined in a mathematical, rather "anonymous" way. More often than not, we have the extra burden of guessing the underlying themes characterizing each cluster based on manual keyword inspection.
This article proposes an alternative, hands-on approach: aided by Scikit-LLM's summarization tools fueled by large language models (LLMs) alongside local text embeddings, we build a two-stage pipeline that:
- Clusters text documents based on deep meaning rather than overlapping terms, as TF-IDF and other classical methods do
- Automatically generates rich, human-readable labels for each cluster, aided by a pre-trained LLM for text summarization wrapped by Scikit-LLM
The solution we are about to build is cost-free and easy to run even in a notebook environment.
Building a Two-Stage Topic Discovery Pipeline
This example can be run entirely in a Google Colab notebook. It uses Groq's LLM API to rely fully on free models. A prerequisite is to visit the Groq website, register, and generate your own API key. Once it is generated, carefully copy your API key (it is shown only once) and add it as a new "Secret" in Google Colab — found under the key icon on the left-hand side of Colab. There, paste your copied API key and name the secret GROQ_API_KEY.
After that, we start our notebook by installing Scikit-LLM and sentence-transformers:
!pip install scikit-llm sentence-transformers -q
Now, let's start writing our Python code. The first step is to configure the environment surrounding Scikit-LLM, routing our requests through Groq's API instead of the default OpenAI API. This way, we can leverage Groq's free-tier pre-trained models and avoid per-token costs.
from google.colab import userdata
from skllm.config import SKLLMConfig
# Routing to Groq's free-tier OpenAI-compatible endpoint
groq_key = userdata.get('GROQ_API_KEY')
SKLLMConfig.set_gpt_url("https://api.groq.com/openai/v1")
SKLLMConfig.set_openai_key(groq_key)
Next, we get some real data. Real-world unsupervised learning scenarios assume data are gathered without clean category tags. We simulate this use case by loading a few hundred posts from the publicly available 20 Newsgroups dataset, using scikit-learn's fetch_20newsgroups() function, without their associated labels. We specifically target documents from three topics: space, automobiles, and computer graphics, so that we can broadly assess how well our pipeline extracts topics from discovered clusters that resemble these three original labels.
Another important step here is applying some basic "data hygiene" and removing noise in the form of extremely short documents without clear topic semantics — these outlier documents might otherwise hijack our clustering results:
from sklearn.datasets import fetch_20newsgroups
categories = ['sci.space', 'rec.autos', 'comp.graphics']
dataset = fetch_20newsgroups(
    subset='train',
    categories=categories,
    remove=('headers', 'footers', 'quotes'),
    random_state=42
)
# Filtering out empty strings and tiny remnants (noisy data) before taking our 300-document sample
X_unlabeled = [doc for doc in dataset.data if len(doc.strip()) > 50][:300]
print(f"Loaded {len(X_unlabeled)} clean, unlabeled documents for clustering.")
The next step is building the two-stage pipeline, starting with a semantic clustering phase. Aided by sentence-transformers, in particular the lightweight, local embedding model all-MiniLM-L6-v2, we convert raw texts into embedding vectors; then we pass them to a k-means clustering algorithm with k=3 to find groups based on semantic similarity:
from sentence_transformers import SentenceTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
# 1. CREATING A CUSTOM SCIKIT-LEARN WRAPPER FOR SENTENCE TRANSFORMERS
# This allows us to drop a local, zero-cost embedding model directly into the pipeline
class LocalSemanticEmbedder(BaseEstimator, TransformerMixin):
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model_name = model_name
        self.model = None
    def fit(self, X, y=None):
        # Load the model only when fitting begins
        self.model = SentenceTransformer(self.model_name)
        return self
    def transform(self, X):
        # Convert raw text into dense semantic vectors
        return self.model.encode(X)
# 2. SEMANTIC CLUSTERING PIPELINE
# The embedder handles the meaning; KMeans groups the resulting spatial coordinates.
clustering_pipeline = Pipeline([
    ('embedder', LocalSemanticEmbedder()),
    ('clusterer', KMeans(n_clusters=3, random_state=42, n_init=10))
])
# Grouping the 300 documents based on profound semantic similarity (embeddings) rather than overlapping keywords (e.g. TF-IDF)
cluster_assignments = clustering_pipeline.fit_predict(X_unlabeled)
The second half of the pipeline is where Scikit-LLM comes into its own. Once we have separated the documents into three clusters, we wrap a pre-trained LLM served by Groq in a GPTSummarizer object, which allows us to ask the model to "name" the clusters. For the sake of efficiency and to avoid API token limits, instead of using the whole dataset, 10 documents are randomly sampled from each cluster and truncated, assuming this will give the model a realistic enough picture to discern between topics:
import random
from skllm.models.gpt.text2text.summarization import GPTSummarizer
# Preparing representative samples for the LLM to read
cluster_samples = [""] * 3
for i in range(3):
    # Find all documents assigned to cluster 'i'
    docs_in_cluster = [X_unlabeled[j] for j in range(len(X_unlabeled)) if cluster_assignments[j] == i]
    # Shuffling and picking 10 random documents to capture the cluster's true diversity
    random.shuffle(docs_in_cluster)
    diverse_sample = docs_in_cluster[:10]
    # Truncating to 300 characters to stay within API limits and focus on core content
    truncated_docs = [doc[:300].replace('\n', ' ') + "..." for doc in diverse_sample if len(doc.strip()) > 20]
    cluster_samples[i] = "\n---\n".join(truncated_docs)
# Initializing the summarizer to extract a punchy, accurate title
theme_extractor = GPTSummarizer(
    model="custom_url::openai/gpt-oss-20b",
    max_words=10
)
# Generating human-readable labels for the anonymous clusters
cluster_themes = theme_extractor.fit_transform(cluster_samples)
print("\n--- AI-GENERATED CLUSTER THEMES ---")
for i, theme in enumerate(cluster_themes):
    print(f"Cluster {i} Size: {list(cluster_assignments).count(i)} documents.")
    print(f"Cluster {i} Theme: {theme.strip()}")
    print("-" * 70)
Results:
--- AI-GENERATED CLUSTER THEMES ---
Cluster 0 Size: 130 documents.
Cluster 0 Theme: Mixed spaceflight anecdotes, myths, and unrelated chatter.
----------------------------------------------------------------------
Cluster 1 Size: 87 documents.
Cluster 1 Theme: Forum posts about graphics software, conversion, and design queries.
----------------------------------------------------------------------
Cluster 2 Size: 83 documents.
Cluster 2 Theme: Car buying tips, maintenance, and quirky automotive anecdotes.
----------------------------------------------------------------------
Not bad for a first attempt! The pipeline managed to map raw, unlabeled texts back to their original (treated as unknown) categories with a reasonable level of accuracy. For instance, cluster 0 largely isolated the subset of documents that originally belonged to the sci.space category, while gently acknowledging the messy reality of the raw data in the form of forum chatter.
Overall, these results show that the hybrid, lightweight strategy works as intended. That said, using semantic text embeddings in the first stage turned out to be essential for the subsequent Scikit-LLM summarizer to do its job neatly. Using keyword-based text representations like TF-IDF would likely have yielded poorer final results, due to their inability to capture underlying context and a tendency to be "distracted" by overlapping vocabulary — like the word "engines", which is common in discussions about both cars and space shuttles. Text embeddings handle these nuances much more effectively.
Wrapping Up
The hybrid approach we built for topic discovery based on clustering and LLM-driven summarization strikes an ideal balance between robust machine learning basics and practical integration of pre-trained LLMs with Scikit-LLM. Moreover, along the way, we handled the heavy lifting of semantic sorting locally.
 
Iván Palomares Carrascosa is a leader, writer, speaker, and adviser in AI, machine learning, deep learning & LLMs. He trains and guides others in harnessing AI in the real world.
