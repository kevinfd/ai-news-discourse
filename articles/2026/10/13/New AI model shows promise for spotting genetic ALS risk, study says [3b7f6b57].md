---
id: "3b7f6b57861fe93d"
title: "New AI model shows promise for spotting genetic ALS risk, study says"
url: "https://alsnewstoday.com/news/new-ai-model-shows-promise-spotting-genetic-als-risk"
source: "ALS News Today"
domain: "alsnewstoday.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-13T06:45:00Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Steve Bryson", "PhD"]
language: "en"
summary: "A new AI model shows promise for predicting genetic ALS risk regardless of family history or known mutations. Capsule Networks can distinguish people with ALS from unaffected individuals, with a high ..."
tags: []
orgs: []
topics: ["models & research", "safety & ethics", "health & science"]
content_source: "fulltext"
word_count: 874
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# New AI model shows promise for spotting genetic ALS risk, study says

ALS News Today · Steve Bryson, PhD · 2026-10-13

New AI model shows promise for spotting genetic ALS risk, study says
Researchers say tool could complement tests based on known mutations
Written by |
- A new AI model shows promise for predicting genetic ALS risk regardless of family history or known mutations.
- Capsule Networks can distinguish people with ALS from unaffected individuals, with a high predictive performance.
- The tool could complement current genetic testing methods based on known ALS mutations.
An artificial intelligence (AI) tool called Capsule Networks can distinguish people with amyotrophic lateral sclerosis (ALS) from unaffected individuals, with predictive performance comparable to testing for major known ALS genes, according to a study.
The large international research collaboration, which used data from more than 47,000 people across 13 countries, was designed to establish the genetic risk for ALS in people who do not carry a known ALS-causing mutation.
Complementing current genetic testing methods based on known ALS mutations, this approach “has the potential to extend genetic risk assessment to all individuals, regardless of their family history or the presence of known ALS mutations,” researchers wrote.
The study, “Towards a deep-learning genomic tool for risk stratification and diagnostic support in sporadic ALS,” was published in Genome Medicine.
Only about 20% of people with ALS have mutations in known genes
ALS is thought to be caused by a combination of genetic and environmental factors. Twin-based studies estimate that genetic factors account for roughly 60% of the risk of developing ALS in a population, with more than 40 genes being linked to disease risk.
However, only about 20% of people living with ALS have mutations in known genes. The remaining cases, most of whom have sporadic ALS, still lack a clear genetic explanation.
To further unravel the genetics of ALS, scientists have conducted genome-wide association studies (GWAS), which use large data sets to detect single changes in DNA associated with the disease. Still, these explain no more than 10% of ALS heritability.
More recently, ALS researchers have turned to machine learning, a type of artificial intelligence that uses algorithms to analyze complex data and find patterns. These methods have been used to identify different ALS risk groups and predict disease progression and functional impairment.
Deep learning is a more advanced type of machine learning that uses neural networks, computer algorithms designed to mimic how the brain’s neural networks (nerve cells) process information. One deep learning method, Capsule Networks (CapsNets), has demonstrated strong performance in predicting individuals at risk for ALS using genetic data.
However, these tools have mostly been tested on limited data sets, so it’s unclear how well they perform across the diverse testing methods, populations, and patient backgrounds encountered in real-world settings.
Study limited to European populations
To address these limitations, an international team of researchers built a new CapsNets model using genetic data from 12,587 ALS patients and 23,503 healthy controls. Participants came from 13 countries across Europe, the U.S., and the U.K, drawn from a 2016 ALS GWAS study.
When trained and tested on individual national groups, the model performed best in the Dutch population, yielding an area under the curve (AUC) of 0.789. An AUC of 1 represents a perfect score for distinguishing people with ALS from non-affected individuals. Performance in other national cohorts was generally lower, with AUCs below 0.6.
Performance improved substantially when the model was trained on the larger, multi-country data set. In the leave-one-out scenario, in which the model was trained on all national groups but one and tested in the remaining one, AUC values ranged from 0.808 to 0.919. In leave-half-out experiments, with training on half of the cohorts and testing in the other half, AUCs ranged from 0.792 to 0.945.
In a simulated population screening scenario, the model’s predictive performance was comparable to published estimates for screening based on well-established ALS-causing mutations, such as FUS, SOD1, and C9orf72.
  While further development is needed, our method lays the foundation for a genetic test that … has the potential to extend genetic risk assessment to all individuals, regardless of their family history or the presence of known ALS mutations.
To evaluate the model on unseen data, researchers used an independent test set of 3,641 cases and 1,974 controls from nine countries, drawn from a separate 2021 ALS GWAS. Here, the model achieved satisfactory performance across five national groups, with AUCs ranging from 0.64 to 0.90. Across the entire independent data set, the AUC was 0.79.
When compared directly with other methods that used the same test set, including polygenic risk scores, which estimate a person’s genetic predisposition to ALS by combining the effects of many genetic variants, the CapsNet model achieved the highest accuracy among all approaches tested.
The team noted that the study was limited to European populations, as large data sets from Asian, Central and South American, or African populations were unavailable. As such, the results should not be generalized to other ancestries without validation.
“This study demonstrates the potential of deep-learning methods for developing predictive models of ALS,” the team concluded. “While further development is needed, our method lays the foundation for a genetic test that … has the potential to extend genetic risk assessment to all individuals, regardless of their family history or the presence of known ALS mutations.”
