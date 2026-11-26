---
id: "b98a3d2f0d3014ce"
title: "OpenAI claims to have solved a 57-year-old math problem at the heart of AI computation"
url: "https://thenewstack.io/openai-matrix-multiplication-exponent"
link: "https://thenewstack.io/openai-matrix-multiplication-exponent"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-25T18:14:05Z"
published_date: "2026-11-25"
collected_at: "2026-11-26T13:04:05Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "OpenAI claims to have solved a problem that has occupied theoretical computer scientists since 1969. In a preprint published Tuesday on GitHub, the company presents a lower bound for the exponent of square matrix multiplication that matches the upper bound of 2.25 it reported in October. \n\n OpenAI claims to have solved a problem that has occupied theoretical computer scientists since 1969. \n\n If…"
tags: ["AI Infrastructure", "Hardware", "Science"]
orgs: ["OpenAI", "Nvidia", "IBM"]
topics: ["models & research", "chips & infrastructure", "health & science", "agents & coding"]
content_source: "summary"
word_count: 755
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI claims to have solved a 57-year-old math problem at the heart of AI computation

The New Stack · Amanda Caswell · 2026-11-25

OpenAI claims to have solved a problem that has occupied theoretical computer scientists since 1969. In a preprint published Tuesday on GitHub, the company presents a lower bound for the exponent of square matrix multiplication that matches the upper bound of 2.25 it reported in October. 

 OpenAI claims to have solved a problem that has occupied theoretical computer scientists since 1969. 

 If the proof holds, developers working on numerical libraries and AI infrastructure will know where the mathematical limit lies and can focus on other ways to improve performance. 

 The paper is one of nine manuscripts OpenAI released Tuesday , seven of which apply a new geometric theory of tensors to problems in arithmetic complexity and combinatorics. 

 Bounding the exponent at 2.25 

 In 1969, Volker Strassen showed that two n × n matrices could be multiplied with an arithmetic exponent below three, prompting researchers to see how close they could get to two. 

 The previous record was approximately 2.371 before OpenAI claimed an upper bound of 2.25 over the complex numbers in an October 2 preprint . 

 Independent researchers weigh in 

 Researchers Mahmut Levent Doğan, Vladimir Lysikov, Keiya Sakabe, and Michael Walter from LMU Munich in Germany published their own exposition of the proof earlier this month. 

 The researchers arrived at the same upper bound over arbitrary fields by substituting a variant of the tensor value introduced by IBM researchers Don Coppersmith and Shmuel Winograd for the spectral points used in OpenAI’s original proof. 

 OpenAI approaches the problem through a computational lower bound for determining whether the entries in several independent lists are distinct. 

 In Tuesday’s 111-page manuscript, “The matrix multiplication exponent is nine fourths,” OpenAI approaches the problem through a computational lower bound for determining whether the entries in several independent lists are distinct. 

 In a companion paper on tensor geometry , OpenAI develops the mathematical framework for its argument that bringing the exponent below 2.25 would allow certain tensor networks to be compressed in violation of the lower bound for the distinctness problem. 

 The authors put the lower bound for multiplying two n × n matrices at ⌈n²·²⁵/2⌉ nonscalar multiplications or divisions in a formal arithmetic circuit, even if linear operations are free and for any n ≥ 2. 

 What Lean actually verifies 

 OpenAI released a Lean formalization alongside the manuscript as developers explore AI-assisted formal verification in software engineering. 

 The LMU Munich researchers also published their own Lean formalization of the upper-bound proof in November. Their implementation establishes the bound in terms of asymptotic tensor rank but does not formalize the arithmetic computational model discussed in their paper. 

 One limitation noted in OpenAI’s documentation is that the Lean proofs cover formal polynomial identities over arbitrary fields using division-free arithmetic programs. The lower bound for circuits that permit division has not been formalized in Lean as part of this release. 

 In OpenAI’s Lean source code , the square exponent theorem relies on two imported theorems that connect the formal arithmetic model to the matrix multiplication exponent. 

 OpenAI presents an exact formula for rectangular matrix multiplication exponents and puts the dual exponent at 0.5, which would mean that multiplying an n × n matrix by an n × ⌈nᵗ⌉ matrix has an arithmetic exponent of two for values of t between zero and 0.5. 

 On October 7, OpenAI withdrew three manuscripts and revised 14 others . The withdrawals followed the discovery of a sign error in a paper on algebraic geometry that invalidated a construction used in two dependent papers. None of the three concerned matrix multiplication. 

 GPU performance in practice 

 The rectangular matrix multiplication results are worth a closer look considering how much activation matrix dimensions vary with batch size and token count in transformer workloads. 

 Given the different computational demands of prefill and autoregressive decoding, the rectangular exponent may be a more useful result for inference optimization than the square exponent of 2.25. 

 Given the different computational demands of prefill and autoregressive decoding, the rectangular exponent may be a more useful result for inference optimization than the square exponent of 2.25. 

 GPU utilization also depends on implementation. Nvidia’s GEMM performance documentation explains how larger tiles can improve data reuse while leaving fewer thread blocks available to keep the GPU busy. 

 Any claims about lower training or inference costs will have to wait until researchers can benchmark new algorithms against existing CUDA implementations at production matrix sizes and precisions. 
 The post OpenAI claims to have solved a 57-year-old math problem at the heart of AI computation appeared first on The New Stack .
