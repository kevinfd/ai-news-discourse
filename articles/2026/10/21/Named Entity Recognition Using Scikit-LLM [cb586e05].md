---
id: "cb586e05d39aecbf"
title: "Named Entity Recognition Using Scikit-LLM"
url: "https://kdnuggets.com/named-entity-recognition-using-scikit-llm"
link: "https://kdnuggets.com/named-entity-recognition-using-scikit-llm"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-10-21T14:00:00Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Iván Palomares Carrascosa"]
language: "en"
summary: "Build standardized custom NER pipelines in a few simple steps, powered by the reasoning capabilities of LLMs."
tags: []
orgs: ["Microsoft", "Google", "Nvidia", "OpenAI", "Tesla"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1396
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/kdn-named-entity-recognition-using-scikit-llm-feature.png"
discussion_url: null
score: null
comments: null
community: null
---

# Named Entity Recognition Using Scikit-LLM

KDnuggets · Iván Palomares Carrascosa · 2026-10-21

Named Entity Recognition Using Scikit-LLM
Build standardized custom NER pipelines in a few simple steps, powered by the reasoning capabilities of LLMs.
Introduction
Structured data extraction from text has plenty of uses in data analysis and myriad applications, including building predictive machine learning models. Named entity recognition (NER) is a clear example of this: it consists of transforming unstructured, messy text into structured data as a result of identifying, extracting, and categorizing relevant information.
NER has been traditionally conducted using traditional natural language processing (NLP) libraries, but these models usually require huge training datasets and arduous fine-tuning to make them learn to recognize custom entities. Thankfully, Scikit-LLM arose to bring large language model (LLM) reasoning capabilities to the table and help build standardized machine learning pipelines in a few simple steps, all on a variety of target tasks beyond just text classification, including custom NER.
Running Named Entity Recognition with Scikit-LLM
This example can be run entirely in a Google Colab notebook. It uses Groq's LLM API to fully rely on free models. A prerequisite is to access the Groq website, register, and generate your own API key. Once generated, carefully copy your API key (you can do this only once) and paste it as a new "Secret" variable in Google Colab — found at the key icon on the left-hand side of Colab. Here, you'll paste your copied API key and name the secret variable GROQ_API_KEY.
After that, we start our notebook by installing Scikit-LLM:
!pip install scikit-llm -q
Now it's time to dive into Python code, and the first stage is to initialize Scikit-LLM configuration. This library is designed using OpenAI API standards, but it lets us override the base URL with the SKLLMConfig.set_gpt_url() method, letting us point to any other compatible provider, such as Groq:
from google.colab import userdata
from skllm.config import SKLLMConfig
# Securely retrieving the Groq API key from Colab Secrets
groq_key = userdata.get('GROQ_API_KEY')
# Redirecting scikit-LLM to Groq's high-speed, free-tier compatible endpoint
SKLLMConfig.set_gpt_url("https://api.groq.com/openai/v1")
SKLLMConfig.set_openai_key(groq_key)
Next, we define the data for our example use case. Unlike conventional text classification in which we have class labels associated with text examples, a central piece of data in LLM-driven NER is the entity dictionary: a list of key-value pairs where keys represent categories to extract and values are the entity descriptions, which will serve as prompts or instructions to guide our LLM through the reasoning process.
Besides the entities, we also define a small set of example texts related to the tech business domain and closely aligned with our entity dictionary:
# Defining the domain-specific entity set to extract, including a clear description that serves as instruction for the LLM
entities = {
    "EXECUTIVE": "The full name of a company leader or individual.",
    "CORPORATION": "The name of a technology company or business.",
    "PRODUCT": "A specific hardware device, software, or technology feature.",
    "CITY": "A geographical location or municipality."
}
# Unstructured text data to parse
X_unstructured = [
    "Satya Nadella announced Copilot integrations for Microsoft at the summit in Seattle.",
    "Elon Musk supervised the rollout of the Cybertruck at the Texas facility.",
    "Jensen Huang showcased the new Blackwell architecture for Nvidia in San Jose."
]
Here comes the critical step: initializing and running a Scikit-LLM estimator that will wrap a compatible pre-trained model from our chosen provider (Groq). For NER, the exact class to use is called GPTExplainableNER. As of the time of writing, a compatible free-tier model to use alongside this object is openai/gpt-oss-20b. Once the model has been initialized and wrapped into the task-specific Scikit-LLM object along with the custom entities, fit_transform() triggers the reasoning process of extracting structured entities from raw texts.
from skllm.models.gpt.tagging.ner import GPTExplainableNER
# Initializing the NER estimator using a tool-compatible model
ner = GPTExplainableNER(
    entities=entities, 
    model="custom_url::openai/gpt-oss-20b" 
)
# fit_transform processes the text and extracts the structured entities
extracted_data = ner.fit_transform(X_unstructured)
To show the results, we iterate over the raw texts and the extracted outputs returned by the LLM as follows:
import ast
# Displaying the extracted entities and handle the string-serialized output
for text, data in zip(X_unstructured, extracted_data):
    print(f"Original: '{text}'")
    
    # If the model returned a string representation of the dict, evaluate it
    if isinstance(data, str):
        try:
            data = ast.literal_eval(data)
        except (ValueError, SyntaxError):
            # Fallback just in case the LLM hallucinated the formatting
            print(f"  Raw unstructured output: {data}\n" + "-" * 50)
            continue
            
    # Data is a Python dictionary, allowing iteration through .items()
    for entity_type, extractions in data.items():
        print(f"  {entity_type}: {extractions}")
    print("-" * 50)
Results:
Original: 'Satya Nadella announced Copilot integrations for Microsoft at the summit in Seattle.'
  Raw unstructured output: Satya Nadella is the full name of a well‑known company leader, specifically the CEO of Microsoft, which fits the definition of an EXECUTIVE. EXECUTIVE Satya Nadella  announced Copilot is a specific software feature developed by Microsoft, qualifying it as a PRODUCT. PRODUCT Copilot  integrations for Microsoft is the name of a technology company, matching the definition of a CORPORATION. CORPORATION Microsoft  at the summit in Seattle is a recognized municipality in the United States, fitting the definition of a CITY. CITY Seattle . 
--------------------------------------------------
Original: 'Elon Musk supervised the rollout of the Cybertruck at the Texas facility.'
  Raw unstructured output: The name "Elon Musk" refers to a well‑known individual who holds a leadership position in a company (CEO of Tesla). According to the definition, an EXECUTIVE is the full name of a company leader or individual, so "Elon Musk" fits this category. EXECUTIVE Elon Musk  supervised the rollout of the The term "Cybertruck" is the name of a specific hardware product developed by Tesla. The definition of PRODUCT is a specific hardware device, software, or technology feature, which matches "Cybertruck". PRODUCT Cybertruck  at the Texas facility. 
--------------------------------------------------
Original: 'Jensen Huang showcased the new Blackwell architecture for Nvidia in San Jose.'
  Raw unstructured output: The name "Jensen Huang" refers to the CEO of Nvidia, a well‑known company leader. According to the definition, an EXECUTIVE is the full name of a company leader or individual. EXECUTIVE Jensen Huang  showcased the new The phrase "Blackwell architecture" denotes a specific GPU architecture released by Nvidia, which is a hardware technology feature. This matches the definition of a PRODUCT. PRODUCT Blackwell architecture  for The word "Nvidia" is the name of a technology company. The definition of CORPORATION is the name of a technology company or business. CORPORATION Nvidia  in The location "San Jose" is a city in California, fitting the definition of a CITY as a geographical location or municipality. CITY San Jose . 
--------------------------------------------------
The raw outputs are not especially clean. To view a more thoroughly parsed result, the following helper code uses regular expressions to parse and post-process the outputs into a neatly structured format:
import re
def parse_extracted_data(raw_data):
    parsed_entities = {}
    # Find all entity blocks
    entity_blocks = re.findall(r"(.*?) ", raw_data, re.DOTALL)
    for block in entity_blocks:
        tag_match = re.search(r"(.*?) ", block)
        value_match = re.search(r"(.*?) ", block)
        if tag_match and value_match:
            entity_type = tag_match.group(1)
            entity_value = value_match.group(1)
            if entity_type not in parsed_entities:
                parsed_entities[entity_type] = []
            parsed_entities[entity_type].append(entity_value)
    return parsed_entities
# Displaying the extracted entities in a cleaner format
print("\n--- Cleaned Extracted Entities ---")
for i, (text, raw_output) in enumerate(zip(X_unstructured, extracted_data)):
    print(f"Original Text {i+1}: '{text}'")
    cleaned_data = parse_extracted_data(raw_output)
    if cleaned_data:
        for entity_type, extractions in cleaned_data.items():
            print(f"  {entity_type}: {', '.join(extractions)}")
    else:
        print("  No entities found.")
    print("-" * 50)
Result:
--- Cleaned Extracted Entities ---
Original Text 1: 'Satya Nadella announced Copilot integrations for Microsoft at the summit in Seattle.'
  EXECUTIVE: Satya Nadella
  PRODUCT: Copilot
  CORPORATION: Microsoft
  CITY: Seattle
--------------------------------------------------
Original Text 2: 'Elon Musk supervised the rollout of the Cybertruck at the Texas facility.'
  EXECUTIVE: Elon Musk
  PRODUCT: Cybertruck
--------------------------------------------------
Original Text 3: 'Jensen Huang showcased the new Blackwell architecture for Nvidia in San Jose.'
  EXECUTIVE: Jensen Huang
  PRODUCT: Blackwell architecture
  CORPORATION: Nvidia
  CITY: San Jose
Our NER pipeline, despite its simplicity in setup, did a pretty good job.
Wrapping Up
This article illustrated how to use Scikit-LLM to leverage pre-trained, open-source LLMs for named entity recognition (NER), a natural language processing task whereby raw, messy texts are analyzed to extract structured data based on domain-specific entities. With minimal configuration effort and a few simple code steps, we can yield more than reasonable results without the need for training a model from scratch.
 
Iván Palomares Carrascosa is a leader, writer, speaker, and adviser in AI, machine learning, deep learning & LLMs. He trains and guides others in harnessing AI in the real world.
