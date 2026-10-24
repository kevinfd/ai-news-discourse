---
id: "057a86be6882ac7b"
title: "Bringing foundational models to the front lines of TB screening"
url: "https://research.google/blog/bringing-foundational-models-to-the-front-lines-of-tb-screening"
link: "https://research.google/blog/bringing-foundational-models-to-the-front-lines-of-tb-screening"
source: "Google Research"
domain: "research.google"
source_type: "research"
collector: "rss"
date: "2026-10-23T18:51:33Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: []
language: "en"
summary: "Generative AI"
tags: ["Generative AI", "Health & Bioscience"]
orgs: ["Google", "EU"]
topics: ["health & science", "models & research", "policy & regulation", "business & funding"]
content_source: "fulltext"
word_count: 1393
paywalled: false
image: "https://storage.googleapis.com/gweb-research2023-media/original_images/AIforTBScreening2_Xray.png"
discussion_url: null
score: null
comments: null
community: null
---

# Bringing foundational models to the front lines of TB screening

Google Research · 2026-10-23

October 23, 2026
Preeti Singh, Lead, Technical Program Manager, and Shravya Shetty, Distinguished Software Engineer, Google Research
Tuberculosis remains one of the world's deadliest infectious diseases, claiming an estimated 1.23 million lives each year. Despite decades of global investment, too many cases go undetected in the communities that carry the highest burden. Over the past five years, we’ve worked to change that trajectory, moving from early research benchmarks toward open foundation models that could be tuned and deployed at the point of care.
Getting access to timely healthcare often comes down to an accident of geography: where you live, what resources your local clinic possesses, and whether a specialist is within reach.
Nowhere is this disparity more acute than in the fight against tuberculosis (TB). Despite being preventable and curable, TB claims more than 1.23 million lives annually. A primary bottleneck is radiology: For those in high-burden settings, from people who live in remote rural areas to miners working deep underground, radiologists are scarce, and imaging infrastructure is often days away. As a result, millions of active cases go undetected, perpetuating transmission.
Over the past several years, our team across Google Research and Google for Health has worked to change that trajectory: moving from an AI-based tool that builds on our existing work in medical imaging to identify people with presumptive TB for follow-up testing to prospective clinical trials, regulatory clearance with local partners, and ultimately open foundation models like MedGemma that empower public health systems worldwide. This week at IDWeek 2026 in Washington, D.C., we are sharing how we’re bringing health AI research to reality, and how foundational models can democratize TB screening at global scale.
Our work began with a fundamental question: Can AI-based tools interpret chest radiographs (CXRs) with the accuracy of an expert radiologist for TB screening?
Chest radiography is the frontline imaging modality for pulmonary screening, but detecting subtle signs of TB like apical infiltrates (fluid in the top portion of the lung) and cavitary lesions (tissue damage) requires specialized expertise that is rarely available in rural clinics. In 2019, we published a benchmark in Radiology, demonstrating that deep learning algorithms could detect active pulmonary TB at performance levels matching experienced radiologists.
Real-world utility, however, demands independent verification. In August 2021, the Stop TB Partnership evaluated automated computer-aided detection (CAD) software across diverse patient cohorts in The Lancet Digital Health, ranking our model among the top-performing TB screening algorithms globally. That year, WHO also recommended CAD for TB screening and triage. In September 2024, in NEJM AI, we detailed a prospective, multi-site validation demonstrating that AI-assisted screening maintains high sensitivity (minimizing missed cases) across diverse patient populations, while also reliably detecting other incidental pulmonary and cardiac abnormalities.
In medical AI, publishing a paper is only the beginning. Between an algorithmic model and a trusted bedside tool lies the "translation gap": making software reliable across varied X-ray machines and offline settings, integrating it into clinical workflows, and meeting medical device regulations.
With this in mind, we partnered with Nexus AI, a Pretoria-based medical technology company, and they translated our chest X-ray algorithms into a certified clinical diagnostic tool. Navigating the regulatory landscape required extensive audits:
- CE MDR class IIb certification: Under the European Union’s Medical Device Regulation (EU MDR 2017/745), Nexus AI achieved Class IIb certification — a rigorous designation that verifies the tool is safe for real-world patient care based on prospective clinical evaluations.
- Quality standards: Nexus AI obtained certified compliance with ISO 13485 for medical device quality management.
- Global access: Nexus AI signed an agreement with FIND to pursue the World Health Organization Pre-qualification (WHO PQ), which is essential for international procurement through global agencies, alongside an ongoing pathway toward the U.S. FDA clearance.
Today, Nexus Intelligence is actively deploying this technology where diagnostic access is most urgently needed.
Across six countries — South Africa, Sierra Leone, and Côte d'Ivoire, with expansions underway in the Democratic Republic of the Congo, Zambia, and Cameroon — Nexus AI’s tool operates in approximately 40 healthcare facilities. To date, over 90 clinicians have evaluated more than 25,000 chest radiographs, reducing turnaround times from weeks to under 45 seconds, accelerating rapid triage while empowering healthcare professionals to make final clinical decisions.
Our collaboration commits to health equity: Nexus AI has delivered more than 3,000 free screenings to under-resourced public clinics, progressing toward a goal of 10,000 sponsored screenings annually.
Perhaps no deployment better illustrates meeting patients where they are than the work done at the Mponeng Gold Mine in South Africa, one of the deepest mines in the world. Deep-shaft miners face chronic silica dust exposure and an elevated risk of pulmonary disease. In partnership with the Stop TB Partnership, Harmony Gold Mine, and the South African Department of Health, Nexus AI deployed ultra-portable digital X-ray kits and offline AI four kilometers underground. Miners are screened on-site within seconds, and those flagged with presumptive TB can be immediately referred for confirmatory molecular testing. Screening, triage and confirmatory testing can now happen in a single visit, compressing a pathway that often takes weeks.
A custom solution with a single partner cannot address the global TB burden alone. To scale impact, we shifted from isolated deployments to building open, adaptable foundations that allow developers and health ministries to create solutions tailored to local needs.
Through the Health AI Developer Foundations (HAI-DEF), we open-sourced our chest X-ray embeddings and MedSigLIP, a lightweight vision-language model trained to align medical images, such as chest X-rays, with the clinical language used to describe them. Because MedSigLIP understands both images and text, developers can use it to classify or search images with plain-language labels, or fine-tune it for a specific task with only a small set of local examples. This lets local teams build specialized models on modest regional datasets and reach strong performance without massive compute resources.
Building on this, we released MedGemma, a family of open-weight multimodal models (4B and 27B parameter configurations). MedGemma advances from basic classification to multimodal clinical reasoning: it synthesizes radiographic findings with clinical history, answers clinician queries in natural language, and runs locally on-device without internet access. Since its launch, MedGemma has seen more than 10 million downloads worldwide.
Open models help enable public health systems to build sovereign solutions that protect patient privacy. In Southeast Asia, the Ministry of Health of Indonesia is addressing the world's second-highest TB burden with an ambitious goal: screening 50 million citizens annually to eradicate the disease.
Reviewing 50 million X-rays manually is infeasible, and proprietary cloud software poses data residency challenges. Instead, the Ministry is fine-tuning MedGemma and MedSigLIP on domestic chest radiographs. Because the models run on local infrastructure, patient data remains within national borders, giving health leaders full sovereignty over clinical deployment.
Recognizing that imaging equipment cannot reach every remote health post, Google Research also developed Health Acoustic Representations (HeAR). Trained on over 300 million audio segments, HeAR enables non-invasive acoustic screening from cough sounds recorded on a standard smartphone microphone.
HeAR is being utilized through collaborative research across sub-Saharan Africa with CIDRZ (Zambia), the Aurum Institute (Ghana, supported by a $250,000 Google.org grant), and HELINA’s $1.5 million regional collaborative. Together, acoustic triage (HeAR), mobile X-ray screening (HAI-DEF), and multimodal clinical reasoning (MedGemma) offer communities an integrated diagnostic cascade of tools for underserved populations.
The journey from a laboratory algorithm to a CE-certified tool used in clinics across six countries has shown us what it takes to turn research into real-world impact: rigorous science, open developer platforms, and dedicated local partnerships. Because our partners know their communities best, they are now taking this work further. Nexus AI is expanding to new countries, Indonesia is integrating TB screening into its national program, and CIDRZ, the Aurum Institute and HELINA are building the clinical evidence for cough-based triage. Our role is to help equip them with open models, foundational research and ongoing support, so that more people with TB are diagnosed and treated sooner.
At IDWeek 2026, we look forward to connecting with the infectious disease and public health communities as we work together to expand equitable care.
We thank our collaborators at Nexus AI, Stop TB Partnership, UNOPS, CIDRZ, Aurum Institute, HELINA, Harmony Gold Mine, the South African Department of Health, and the Indonesian Ministry of Health for their clinical leadership and dedication to global health equity.
    ×
    ❮
    ❯
    
  
  ×
