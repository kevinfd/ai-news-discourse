---
id: "0b517f7eda117466"
title: "Using LLM Summarization in Your Scikit-Learn Pipelines with Scikit-LLM"
url: "https://kdnuggets.com/using-llm-summarization-in-your-scikit-learn-pipelines-with-scikit-llm"
link: "https://kdnuggets.com/using-llm-summarization-in-your-scikit-learn-pipelines-with-scikit-llm"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-03T15:00:00Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Iván Palomares Carrascosa"]
language: "en"
summary: "Learn how to build an architecture that blends Scikit-LLM estimators for text summarization with traditional scikit-learn methods into a single, unified pipeline for summarizing and classifying raw, messy text."
tags: []
orgs: ["OpenAI", "Google"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1474
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-using-llm-summarization-in-your-scikit-learn-pipelines-with-scikit-llm-feature.png"
discussion_url: null
score: null
comments: null
community: null
---

# Using LLM Summarization in Your Scikit-Learn Pipelines with Scikit-LLM

KDnuggets · Iván Palomares Carrascosa · 2026-11-03

Using LLM Summarization in Your Scikit-Learn Pipelines with Scikit-LLM
Learn how to build an architecture that blends Scikit-LLM estimators for text summarization with traditional scikit-learn methods into a single, unified pipeline for summarizing and classifying raw, messy text.
Introduction
Using traditional, lightweight machine learning classifiers on text frequently requires condensing lengthy, often noisy raw text into clean signals to succeed. Therefore, it wouldn't be crazy to think of using a large language model (LLM) for text summarization as a preprocessing stage before feeding cleaner texts to the downstream classification model. What if we could do this seamlessly as part of a traditional, scikit-learn-based pipeline where LLM-driven summarization can coexist with traditional data preprocessing, training, and inference? And what if we could do all of this using exclusively free tools? Look no further.
In this article, we will learn how to build an architecture that blends Scikit-LLM estimators for text summarization with traditional scikit-learn methods into a single, unified pipeline for summarizing and classifying raw, messy text, bringing together the best of both worlds: LLMs and classical machine learning models.
Integrating LLM-Driven Summarization in a Machine Learning Pipeline
This example can be run entirely in a Google Colab notebook. It uses Groq's LLM API to fully rely on free models. A prerequisite is to access the Groq website, register, and generate your own API key. Once it's generated, carefully copy your API key (it is shown only once) and paste it as a new "Secret" variable in Google Colab, found at the key icon on the left-hand side of Colab. Name the secret variable GROQ_API_KEY.
After that, we start our notebook by installing Scikit-LLM:
!pip install scikit-llm -q
Now, into the Python code. The first step is to configure the environment surrounding Scikit-LLM, routing our requests through Groq's API instead of the default OpenAI API. This will help us leverage Groq's free, friendly, and efficient pre-trained models, bypassing per-token costs.
from google.colab import userdata
from skllm.config import SKLLMConfig
# Retrieving API key and routing to Groq's free-tier OpenAI-compatible endpoint
groq_key = userdata.get('GROQ_API_KEY')
SKLLMConfig.set_gpt_url("https://api.groq.com/openai/v1")
SKLLMConfig.set_openai_key(groq_key)
Next, we define the "training" data. It consists of a small set of initial documents along with their corresponding labels. The documents are intentionally lengthy, somewhat noisy, and verbose, just like in many real-world scenarios. Without a prior summarization to extract relevant signals from the text, directly obtaining numerical, machine learning-friendly representations from these texts would inevitably propagate the noise:
# Raw, lengthy documents and their corresponding class labels
X_long_texts = [
    "The new solar panel technology efficiency has increased by 15% due to the novel perovskite layer, significantly lowering the barrier to entry for residential use and driving green energy adoption by making installations cheaper and faster than ever before.",
    "Financial markets saw a sharp downturn today following the central bank's unexpected interest rate hike, leading to massive sell-offs in the tech sector and triggering volatility indices to reach their highest points in over three years.",
    "The clinical trial for the new arthritis medication showed promising results, reducing joint swelling by 40% in the control group without severe side effects, awaiting FDA approval which could bring relief to millions suffering from autoimmune disorders."
]
y_labels = ["Energy", "Finance", "Healthcare"]
Similar to few-shot classification, we only need a small, representative set of training examples to let the LLM we will load later know how to reason. No actual training of the LLM takes place.
The next step is arguably the most critical: we are defining our three-step pipeline for machine learning-driven classification preceded by LLM-driven summarization, thereby integrating Scikit-LLM capabilities to accommodate specific tasks on pre-trained LLMs into a broader machine learning pipeline. The code below uses a GPTSummarizer object to encapsulate a compatible Groq model for summarization, namely openai/gpt-oss-20b. It then embeds the summarization step into the scikit-learn pipeline, followed by term frequency-inverse document frequency (TF-IDF) to obtain text representations of summarized texts rather than the original, lengthy ones. Finally, it defines and trains a logistic regression classifier using the label set defined before.
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from skllm.models.gpt.text2text.summarization import GPTSummarizer
# THREE-STEP MACHINE LEARNING PIPELINE FOR TEXT CLASSIFICATION, PRECEDED BY SUMMARIZATION
# 1. Summarizer: Condenses long documents using the compatible model on Groq
# 2. Vectorizer: Converts the concise summaries into numerical TF-IDF vectors
# 3. Classifier: Learns to classify the TF-IDF vectors using standard Logistic Regression
text_pipeline = Pipeline([
    ('summarizer', GPTSummarizer(
        model="custom_url::openai/gpt-oss-20b",
        max_words=20
    )),
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])
# Fitting the entire pipeline end-to-end
text_pipeline.fit(X_long_texts, y_labels)
You might be wondering why just three training instances in X_long_texts could be enough to train the last-stage logistic regression classifier. It's not because the classifier has truly learned the broad concepts of 'Energy', 'Finance', and 'Healthcare'. Instead, it succeeds due to two pipeline mechanics working in tandem: the LLM first acts as a precise filter that condenses noisy text into "canonical" keywords. After that, the downstream vectorizer naturally limits its whole vocabulary to those few remaining words, turning the classification task into a pretty easy, largely trivial keyword-matching game.
Next, we take a look at the summaries produced for the three training examples to verify they make sense:
# Inspecting the summaries of "training" examples, accessing the 'summarizer' object
train_summaries = text_pipeline.named_steps['summarizer'].transform(X_long_texts)
print("--- TRAINING DATA SUMMARIES ---")
for label, original, summary in zip(y_labels, X_long_texts, train_summaries):
    print(f"[{label.upper()}]\nOriginal: {original}\nSummary:  {summary}\n")
Output:
--- TRAINING DATA SUMMARIES ---
[ENERGY]
Original: The new solar panel technology efficiency has increased by 15% due to the novel perovskite layer, significantly lowering the barrier to entry for residential use and driving green energy adoption...
Summary:  New perovskite solar panels boost efficiency by 15%, reducing costs and accelerating residential green energy adoption.
[FINANCE]
Original: Financial markets saw a sharp downturn today following the central bank's unexpected interest rate hike, leading to massive sell-offs in the tech sector and triggering volatility indices...
Summary:  Markets plunged after unexpected rate hike, causing tech sell‑offs and high volatility.
[HEALTHCARE]
Original: The clinical trial for the new arthritis medication showed promising results, reducing joint swelling by 40% in the control group without severe side effects, awaiting FDA approval...
Summary:  New arthritis drug trial reduces swelling by 40% with no severe side effects, pending FDA approval.
Since these summaries seem quite sensible, we can now finalize by creating some test examples and passing them entirely to the pipeline for classification via prior summarization:
X_new = [
    "A breakthrough mRNA vaccine targeting seasonal flu strains showed 85% efficacy across diverse patient demographics in stage 3 clinical trials, paving the way for a more robust global immune defense next winter.",
    "Researchers have developed a grid-scale sodium-ion battery that promises to store surplus wind and solar power at a fraction of lithium's cost, potentially resolving the intermittency issue of renewables.",
    "Stocks rallied in late trading as technology shares recovered from yesterday's losses, driven by strong earnings reports from major semiconductor manufacturers and optimistic GDP growth forecasts."
]
# The pipeline automatically summarizes, vectorizes, and classifies the unseen text
predictions = text_pipeline.predict(X_new)
# Access the intermediate summaries for the unseen data to display them
new_summaries = text_pipeline.named_steps['summarizer'].transform(X_new)
print("\n--- UNSEEN DATA PREDICTIONS ---")
for text, summary, prediction in zip(X_new, new_summaries, predictions):
    print(f"Original Document: '{text}'")
    print(f"Intermediate Summary: '{summary}'")
    print(f"Final Predicted Category: {prediction}\n" + "-" * 70)
And these are the final results we obtain — not bad at all!
--- UNSEEN DATA PREDICTIONS ---
Original Document: 'A breakthrough mRNA vaccine targeting seasonal flu strains showed 85% efficacy across diverse patient demographics in stage 3 clinical trials, paving the way for a more robust global immune defense next winter.'
Intermediate Summary: 'New mRNA flu vaccine achieved 85% efficacy in diverse patients, promising stronger global immunity next winter.'
Final Predicted Category: Healthcare
----------------------------------------------------------------------
Original Document: 'Researchers have developed a grid-scale sodium-ion battery that promises to store surplus wind and solar power at a fraction of lithium's cost, potentially resolving the intermittency issue of renewables.'
Intermediate Summary: 'New grid‑scale sodium‑ion battery can store excess wind/solar power cheaply, easing renewable intermittency.'
Final Predicted Category: Energy
----------------------------------------------------------------------
Original Document: 'Stocks rallied in late trading as technology shares recovered from yesterday's losses, driven by strong earnings reports from major semiconductor manufacturers and optimistic GDP growth forecasts.'
Intermediate Summary: 'Tech stocks rebound late, fueled by strong semiconductor earnings and hopeful GDP growth, boosting overall market rally.'
Final Predicted Category: Finance
----------------------------------------------------------------------
Wrapping Up
With the aid of Scikit-LLM, we have learned how to embed a free, pre-trained LLM for summarization directly into a native machine learning pipeline based on scikit-learn. In particular, we combined modern prompt-based text distillation with classical, lightweight TF-IDF vectorizers and linear models like logistic regression for classification, making the overall task lightweight and surprisingly effective.
 
Iván Palomares Carrascosa is a leader, writer, speaker, and adviser in AI, machine learning, deep learning & LLMs. He trains and guides others in harnessing AI in the real world.
