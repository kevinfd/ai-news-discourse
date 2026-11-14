---
id: "b2826300fbd4ca99"
title: "Alignment Is a System-Level Context Property, Not Just Model Weights"
url: "https://doi.org/10.5281/zenodo.23585146"
link: "https://doi.org/10.5281/zenodo.23585146"
source: "Zenodo"
domain: "doi.org"
source_type: "community"
collector: "reddit"
date: "2026-11-13T18:35:22Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["rayanpal_"]
language: "en"
summary: "Alignment Is a System Property, Not Just a Model Property: System-Prompt Ablation and Zero-Byte Continuation in GPT-4-0613\nAuthors/Creators\nDescription\nThis paper presents a retrospective reanalysis of the frozen Cross-Vendor Semantic Void Matrix, isolating how system-prompt configuration changes zero-byte answer emission in GPT-4-0613. The reanalysis is dated October 22, 2026, one day before…"
tags: ["r/artificial"]
orgs: ["OpenAI"]
topics: ["models & research", "safety & ethics", "products & launches"]
content_source: "fulltext"
word_count: 351
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xvftqi/alignment_is_a_systemlevel_context_property_not/"
score: null
comments: null
community: "r/artificial"
---

# Alignment Is a System-Level Context Property, Not Just Model Weights

Zenodo · rayanpal_ · 2026-11-13

Alignment Is a System Property, Not Just a Model Property: System-Prompt Ablation and Zero-Byte Continuation in GPT-4-0613
Authors/Creators
Description
This paper presents a retrospective reanalysis of the frozen Cross-Vendor Semantic Void Matrix, isolating how system-prompt configuration changes zero-byte answer emission in GPT-4-0613. The reanalysis is dated October 22, 2026, one day before the scheduled retirement of gpt-4-0613 (OpenAI deprecations page: October 23, 2026). No new inference was performed.
At a 4,000-token completion ceiling under provider-default sampling, the complete embodiment system prompt produced 298/300 successful normal-stop zero-byte responses (V0; 99.33%) across "Be silence.", "Be nothing.", and "Be the null." Removing the output restriction, replacing the embodiment framing with an output-only instruction, or omitting the system message produced 0/30 V0 in each condition, totaling 0/90 across the three ablations. The no-embodiment condition produced 13 nonempty Near-Voids and 17 ordinary responses. These outcomes remain distinct from exact zero-byte output.
The analysis preserves per-prompt denominators, competing outcomes, output-licensed controls, and confidence intervals. It distinguishes the setting-matched comparison from the broader primary census of 919/930 V0. Comparisons across six GPT model identifiers reveal differing dependence on system-prompt framing, including later identifiers that produced V0 without a supplied system message.
The separately published GPT-5.4 prerequisite-role reassignment experiments provide a complementary intervention: changing the governing prerequisite within a system instruction reversed which input occupied the high-V0 branch. Those results are cited separately and are not pooled into the Matrix populations.
The October 20–21 preregistered pre-retirement replay (DOIs 10.5281/zenodo.23521144, 10.5281/zenodo.23521616) is cited as confirmatory for the full-prompt arm only. The central conclusion: for gpt-4-0613, normal-stop zero-byte continuation under the tested null-concept prompts was strongly dependent on the complete system-level instruction context. Evaluations must characterize the instruction-configured system, not just the model identifier.
The reproducibility release provides manuscript source, deterministic analysis code, generated tables and figures, population membership, verification scripts, and SHA-256 manifests. Numerical results are regenerated from hash-pinned public data and reconciled against frozen raw receipts.
Original Matrix: https://doi.org/10.5281/zenodo.21696066
Prerequisite-role reassignment study: https://doi.org/10.5281/zenodo.22983298
Final paper and reproducibility release: https://github.com/theonlypal/alignment-is-a-system-property/releases/tag/v1
Exact source commit: https://github.com/theonlypal/alignment-is-a-system-property/tree/7fe765a059bdd9951c3d6f80ee7b6560299ff741
PDF SHA-256: b06ef7af79f3a66f404650f8550b56d615bd36643c7e0254be120d5a1ed3783e
Files
      
        Alignment_Is_a_System_Property.pdf
        
      
    
      
        Files
         (333.7 kB)
        
      
    
Additional details
              
                Software
              
            
- Repository URL
- https://github.com/theonlypal/alignment-is-a-system-property
