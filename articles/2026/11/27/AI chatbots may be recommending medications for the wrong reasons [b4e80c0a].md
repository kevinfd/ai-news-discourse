---
id: "b4e80c0a0cd4af93"
title: "AI chatbots may be recommending medications for the wrong reasons"
url: "https://earth.com/science/ai-chatbots-may-be-recommending-medications-for-the-wrong-reasons"
link: "https://earth.com/science/ai-chatbots-may-be-recommending-medications-for-the-wrong-reasons"
source: "Earth.com"
domain: "earth.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-27T15:17:00Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["Eric Ralls"]
language: "en"
summary: "Researchers found that leading AI chatbots disproportionately recommend brand-name medications, potentially driving up prescription drug costs."
tags: []
orgs: ["Google", "OpenAI", "Anthropic", "Meta"]
topics: ["health & science", "business & funding", "models & research", "policy & regulation"]
content_source: "fulltext"
word_count: 1024
paywalled: false
image: "http://www.bing.com/th?id=ONUT.4dg7x0iWErEuYSHnQ9q8uQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# AI chatbots may be recommending medications for the wrong reasons

Earth.com · Eric Ralls · 2026-11-27

AI chatbots may be recommending medications for the wrong reasons
Researchers found that leading AI chatbots disproportionately recommend brand-name medications, potentially driving up prescription drug costs.
Ask a chatbot which version of a blood pressure pill to take, and you might expect it to weigh the options the way a pharmacist would. Instead, five leading AI models kept naming the same product.
It was usually a brand-name drug with a big online footprint, and usually not the one doctors prescribe most.
Following those recommendations would raise U.S. drug purchase costs by tens of millions of dollars a year, the researchers estimated.
Daiju Ueda of Osaka Metropolitan University led the study with colleagues at the University of Texas MD Anderson Cancer Center.
His team tested the models on made-up patients, not real prescriptions, so the cost figure is a projection rather than a bill anyone has paid.
One product nearly always wins
The team wrote 177,120 short patient scenarios. Each named a common disease and the active ingredient a doctor planned to prescribe, such as amlodipine for high blood pressure.
Each also described the patient by age, sex, race or ethnicity, LGBTQ+ identity and income, with any of those details sometimes left out.
The scenarios covered 123 disease and drug pairs, each run through 1,440 patient profiles.
Five AI models answered every scenario: GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Flash, Llama 4 and MedGemma.
Each was asked to list up to three FDA-approved products by name, in order of preference. Four physicians then checked more than 883,000 answers against the FDA’s drug registries.
On average, 5.5 approved products existed for each ingredient. Yet across the disease and drug pairs, the most favored product accounted for an average of 97.5% of first-choice picks.
The alternatives, in other words, almost never came up first.
Pooling the five models together, one product drew more than 90% of first choices in 96 of the 123 pairs. The models also agreed with one another, almost all of the time, on which product that was.
Pricier than real prescriptions
The team then compared those picks with what Americans are actually dispensed, using the Medical Expenditure Panel Survey, a national survey of prescription use, for 2019 through 2023.
The most commonly prescribed product matched a model’s first choice in only 29.7% of cases, and landed anywhere in its top three in 58.8%.
Weighted by how many prescriptions each drug accounts for, the first-choice match fell to 17%. So, the models’ preferred product was usually not the version most commonly prescribed.
Prices came from the federal National Average Drug Acquisition Cost database, which tracks what retail pharmacies pay.
Complete pricing existed for 51 of the ingredients, and for 38 of those the models’ preferred products cost more than the ones in real use.
More often than not, then, the models leaned toward the pricier option.
The team then asked what would happen if doctors prescribed exactly as the models recommended, across those 51 ingredients, at current prescription volumes.
“We found that annual acquisition costs would increase by approximately US$55.6 million,” Ueda said. “This represents a 1,019% increase in the cost of purchasing these prescriptions.”
The $55.6 million covers only the 51 ingredients with full price data. It also assumes a pharmacy fills exactly what the model names, with no generic substitution at the counter.
Famous products win
What made a product the favorite? Being the original brand-name version mattered most. An originator product had about 20 times the odds of being recommended over a generic with the same ingredient.
“The recommendations were mostly for brand-name drugs, those highly visible in Google searches, and treatments with dedicated Wikipedia pages,” Ueda said.
A product with its own Wikipedia page had three times the odds of being named, and more Google search results raised the odds too. Products approved more recently, and products that doctors prescribe more often in practice, were recommended less. Heavier advertising spending by the manufacturer slightly lowered the odds.
Some picks are no longer sold
Not every answer was a product a pharmacist could fill. Between 12.4% and 14.7% of each model’s recommendations failed a regulatory check. In nearly all of those cases, the model had named a product that was once FDA-approved but is no longer sold. GPT-5.4 had the lowest rate and Claude Sonnet 4.6 the highest.
The patient’s description changed those odds. Scenarios describing a Black patient had 1.64 times the odds of drawing a regulatory miss, compared with scenarios that left race unstated. For an Asian patient the figure was 1.16 times.
The authors wrote that such outputs were a minority and do not necessarily mean a clinically wrong choice. But any evaluation of these tools, they added, should report its results by patient group.
Asking for generics helps a little
When the team rewrote the prompt to ask for the lowest-cost or generic option, the chatbots did shift.
The top pick changed in 63% of comparisons under the lowest-cost prompt and 78% under the generic prompt, and when it changed, it usually moved to a generic.
But the answers stayed just as concentrated, with a single product still taking 93% to 98% of first choices under each new prompt.
The scenarios were synthetic, and the authors wrote that they shouldn’t be read as a measure of how people actually prescribe.
The researchers also stopped at the recommendation and left out rare diseases and complicated cases.
The study didn’t follow what a doctor, an insurer or a pharmacist would do next. Whether a chatbot’s pick changes what a patient finally receives is the open question.
The authors wrote that the next studies need realistic clinical scenarios, tests of whether lower-cost prompts actually work, and a look at how doctors use these AI assistants.
“Combining AI systems with trusted drug information sources and human oversight may help support more appropriate medication choices,” Ueda said.
The full study was published in the journal Nature Health.
—–
Like what you read? Subscribe to our newsletter for engaging articles, exclusive content, and the latest updates.
Check us out on EarthSnap, a free app brought to you by Eric Ralls and Earth.com.
—–
