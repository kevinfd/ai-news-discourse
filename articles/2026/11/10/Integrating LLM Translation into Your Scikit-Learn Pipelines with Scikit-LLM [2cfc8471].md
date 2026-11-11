---
id: "2cfc8471cddd4f6b"
title: "Integrating LLM Translation into Your Scikit-Learn Pipelines with Scikit-LLM"
url: "https://kdnuggets.com/integrating-llm-translation-into-your-scikit-learn-pipelines-with-scikit-llm"
link: "https://kdnuggets.com/integrating-llm-translation-into-your-scikit-learn-pipelines-with-scikit-llm"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-10T15:00:00Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Iván Palomares Carrascosa"]
language: "en"
summary: "Learn, in a few easy steps, how to build a two-stage scikit-learn pipeline for multilingual text classification, guided by two pre-trained language models handled by Scikit-LLM for translation and zero-shot classification."
tags: []
orgs: ["OpenAI", "Google"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1403
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-integrating-llm-translation-into-your-scikit-learn-pipelines-with-scikit-llm-feature.png"
discussion_url: null
score: null
comments: null
community: null
---

# Integrating LLM Translation into Your Scikit-Learn Pipelines with Scikit-LLM

KDnuggets · Iván Palomares Carrascosa · 2026-11-10

Integrating LLM Translation into Your Scikit-Learn Pipelines with Scikit-LLM
Learn, in a few easy steps, how to build a two-stage scikit-learn pipeline for multilingual text classification, guided by two pre-trained language models handled by Scikit-LLM for translation and zero-shot classification.
Introduction
Text classification sometimes requires dealing with raw texts written in different languages, with the added challenge of normalizing all incoming data into a unified language before providing it to the downstream classification model. Thankfully, Scikit-LLM not only facilitates the construction of pipelines driven by large language models (LLMs) for tasks like zero-shot and few-shot classification. It also provides custom classes to adapt pre-trained models for other specialized language tasks like translation.
This article shows how to build an overarching scikit-learn pipeline for multilingual text classification, consisting of two major stages, both guided by Scikit-LLM-wrapped models: translation and zero-shot classification. The resulting pipeline I'll teach you to build has multiple advantages:
- It replaces the rigid keyword matching of traditional text classifiers with semantic reasoning, thanks to a pre-trained LLM wrapped for zero-shot classification
- Incoming texts are unified into a common language to enable effective classification with a single downstream model
- Zero-shot classification with Scikit-LLM addresses the cold-start data issue, needing only category names (class labels) along with a few associated training examples to start doing its job: no extra model training needed at all!
Building a Multilingual Translation and Zero-Shot Classification Pipeline
This example can be run entirely in a Google Colab notebook. It uses Groq's LLM API to rely entirely on free models. As a prerequisite, go to the Groq website, register, and generate your own API key. Once it is generated, carefully copy your API key (it is shown only once) and paste it as a new "Secret" variable in Google Colab, found under the key icon on the left-hand side of Colab. Here, you'll paste your copied API key and name the secret variable GROQ_API_KEY.
After that, we start our notebook by installing Scikit-LLM:
!pip install scikit-llm -q
Now, let's start writing our Python code. The first step is to configure the environment surrounding Scikit-LLM, routing our requests through Groq's API instead of the default OpenAI API. By doing this, we leverage Groq's free, user-friendly pre-trained models, avoiding per-token costs.
from google.colab import userdata
from skllm.config import SKLLMConfig
# Retrieving API key and route to a free-tier OpenAI-compatible endpoint (e.g. Groq)
groq_key = userdata.get('GROQ_API_KEY')
SKLLMConfig.set_gpt_url("https://api.groq.com/openai/v1")
SKLLMConfig.set_openai_key(groq_key)
Next, we define the "training" data. Since we are going to use a zero-shot LLM classifier — instead of a traditional machine learning classifier preceded by a vectorizer that maps text numerically — we have the advantage of not needing a large, balanced set of training examples. All we need is to define the unique set of classification labels that the model must learn to recognize and use for predictions, as well as a few placeholder data examples that fill the minimal requirements of Scikit-LLM's fit() method, which mimics its scikit-learn counterpart:
# 1. MULTILINGUAL TRAINING DATA
# Adding a few labeled examples in mixed languages and multiple topics
X_multilingual_texts = [
    # Energy
    "La technologie des panneaux solaires a vu son efficacité augmenter de 15%.", # French (Solar)
    "Neue Batteriespeicher für Windenergie werden immer wirtschaftlicher.", # German (Wind/Battery)
    # Finance
    "Los mercados financieros sufrieron una fuerte caída hoy tras la subida de tipos.", # Spanish (Markets)
    "Les actions technologiques ont rebondi grâce à de solides rapports sur les bénéfices.", # French (Stocks/Earnings)
    # Healthcare
    "Die klinische Studie für das neue Medikament reduzierte die Schwellung um 40%.", # German (Medication/Trial)
    "Un ensayo reciente demostró que la vacuna es muy eficaz para prevenir infecciones.", # Spanish (Vaccine)
]
y_labels = ["Energy", "Energy", "Finance", "Finance", "Healthcare", "Healthcare"]
The next step is the central one: we define our two-stage pipeline for translation followed by zero-shot classification. This is where we integrate Scikit-LLM's capabilities for adapting pre-trained LLMs to specific tasks into a broader, scikit-learn-based machine learning pipeline.
The code below uses two task-specific classes from Scikit-LLM: GPTTranslator to adapt a base LLM for translation into a common language, and ZeroShotGPTClassifier to adapt another LLM for the subsequent task in our pipeline, i.e. classification of the translated text without the need to retrain the model. Notice below that it is perfectly fine to choose the same base Groq model — "custom_url::llama-3.1-8b-instant" — for both stages: we just use different classes to adapt the two model instances to different target tasks.
from sklearn.pipeline import Pipeline
from skllm.models.gpt.text2text.translation import GPTTranslator
from skllm.models.gpt.classification.zero_shot import ZeroShotGPTClassifier
# 2. THE TRANSLATION AND ZERO-SHOT CLASSIFICATION PIPELINE
# A scikit-learn-based pipeline that contains two Scikit-LLM-wrapped models
text_pipeline = Pipeline([
    ('translator', GPTTranslator(
        model="custom_url::openai/gpt-oss-20b",
        output_language="English"
    )),
    ('classifier', ZeroShotGPTClassifier(
        model="custom_url::openai/gpt-oss-20b"
    ))
])
# 3. FITTING THE CLASSIFIER
# ZeroShotGPTClassifier only needs to see the unique labels to understand the categories.
# Passing a minimal placeholder list for X only to satisfy the scikit-learn API requirements.
y_labels_unique = ["Energy", "Finance", "Healthcare"]
X_placeholder = [""] * len(y_labels_unique)
text_pipeline.fit(X_placeholder, y_labels_unique)
Before making a few final predictions by passing fresh examples to our newly built pipeline, we take a look at the translations produced by the first of the two models for the training examples to verify that they are correct:
# Accessing the 'translator' step to transform the training data
train_translations = text_pipeline.named_steps['translator'].transform(X_multilingual_texts)
print("--- TRAINING DATA TRANSLATIONS ---")
for label, original, translated in zip(y_labels, X_multilingual_texts, train_translations):
    print(f"[{label.upper()}]\nOriginal: {original}\nTranslated: {translated}\n")
Output:
--- TRAINING DATA TRANSLATIONS ---
[ENERGY]
Original: La technologie des panneaux solaires a vu son efficacité augmenter de 15%.
Translated: The technology of solar panels has seen its efficiency increase by 15%.
[ENERGY]
Original: Neue Batteriespeicher für Windenergie werden immer wirtschaftlicher.
Translated: New battery storage for wind energy is becoming increasingly economical.
[FINANCE]
Original: Los mercados financieros sufrieron una fuerte caída hoy tras la subida de tipos.
Translated: Financial markets suffered a sharp drop today after the rate hike.
[FINANCE]
Original: Les actions technologiques ont rebondi grâce à de solides rapports sur les bénéfices.
Translated: Tech stocks rebounded thanks to solid earnings reports.
[HEALTHCARE]
Original: Die klinische Studie für das neue Medikament reduzierte die Schwellung um 40%.
Translated: The clinical study for the new drug reduced swelling by 40%.
[HEALTHCARE]
Original: Un ensayo reciente demostró que la vacuna es muy eficaz para prevenir infecciones.
Translated: A recent study showed that the vaccine is very effective at preventing infections.
Since these translations seem quite decent, we can now take the final step and come up with a few test examples in multiple languages, which we will pass to the pipeline for classification via prior translation:
# 4. PREDICTING ON UNSEEN DATA
X_new_multilingual = [
    "Un nuovo vaccino antinfluenzale ha mostrato un'efficacia dell'85% negli studi clinici, promettendo difese immunitarie più forti.", # Italian (Healthcare)
    "I ricercatori hanno sviluppato una batteria agli ioni di sodio che immagazzina l'energia eolica in eccesso in modo molto economico.", # Italian (Energy)
    "As ações de tecnologia se recuperaram no final do pregão, impulsionadas por fortes relatórios de lucros corporativos." # Portuguese (Finance)
]
predictions = text_pipeline.predict(X_new_multilingual)
new_translations = text_pipeline.named_steps['translator'].transform(X_new_multilingual)
print("\n--- UNSEEN DATA PREDICTIONS ---")
for text, translation, prediction in zip(X_new_multilingual, new_translations, predictions):
    print(f"Original Document: '{text}'")
    print(f"Intermediate Translation: '{translation}'")
    print(f"Final Predicted Category: {prediction}\n" + "-" * 70)
Final results:
--- UNSEEN DATA PREDICTIONS ---
Original Document: 'Un nuovo vaccino antinfluenzale ha mostrato un'efficacia dell'85% negli studi clinici, promettendo difese immunitarie più forti.'
Intermediate Translation: 'A new influenza vaccine has shown an efficacy of 85% in clinical studies, promising stronger immune defenses.'
Final Predicted Category: Healthcare
----------------------------------------------------------------------
Original Document: 'I ricercatori hanno sviluppato una batteria agli ioni di sodio che immagazzina l'energia eolica in eccesso in modo molto economico.'
Intermediate Translation: 'Researchers have developed a sodium-ion battery that stores excess wind energy in a very economical way.'
Final Predicted Category: Energy
----------------------------------------------------------------------
Original Document: 'As ações de tecnologia se recuperaram no final do pregão, impulsionadas por fortes relatórios de lucros corporativos.'
Intermediate Translation: 'Technology stocks recovered at the end of the trading session, driven by strong corporate earnings reports.'
Final Predicted Category: Finance
----------------------------------------------------------------------
The results speak for themselves, right? Well done!
Wrapping Up
Aided by Scikit-LLM classes for translation and zero-shot classification via pre-trained LLMs, we have learned how to build a free, quick, and highly effective two-stage scikit-learn pipeline for classifying texts in multiple languages.
 
Iván Palomares Carrascosa is a leader, writer, speaker, and adviser in AI, machine learning, deep learning & LLMs. He trains and guides others in harnessing AI in the real world.
