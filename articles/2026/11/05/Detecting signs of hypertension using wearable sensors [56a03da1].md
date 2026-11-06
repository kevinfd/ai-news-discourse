---
id: "56a03da12c0bbf17"
title: "Detecting signs of hypertension using wearable sensors"
url: "https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors"
link: "https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors"
source: "Google Research"
domain: "research.google"
source_type: "research"
collector: "rss"
date: "2026-11-05T16:01:08Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: []
language: "en"
summary: "Health & Bioscience"
tags: ["Health & Bioscience", "Machine Intelligence"]
orgs: ["Google"]
topics: ["models & research", "health & science", "safety & ethics"]
content_source: "fulltext"
word_count: 1228
paywalled: false
image: "https://storage.googleapis.com/gweb-research2023-media/original_images/Hypertension1_Overview.png"
discussion_url: null
score: null
comments: null
community: null
---

# Detecting signs of hypertension using wearable sensors

Google Research · 2026-11-05

November 5, 2026
Paolo Di Achille, Staff Research Scientist, and Ming-Zher Poh, Senior Staff Research Scientist, Google Research
We present a new AI system that leverages standard consumer smartwatch sensors to passively detect signs of high blood pressure.
Hypertension (i.e., high blood pressure), often called the "silent killer”, affects over one billion people globally, yet more than half of adults with the condition are unaware they have it. Because it rarely presents with obvious symptoms, high blood pressure (BP) is typically discovered only through incidental screening. This gap in awareness is particularly severe among younger adults aged 18 to 44, where missing diagnoses can delay life-saving early interventions and significantly increase the long-term risk of adverse cardiovascular events like stroke or heart failure.
Office BP measurement serves as the primary initial screening gateway for detecting hypertension. In recent years, cuffless wearable devices have emerged as a potential tool to complement episodic office care. However, existing commercial solutions usually require regular calibration using a traditional arm cuff. This means they only track relative changes from a baseline cuff reading rather than identifying absolute hypertensive states, limiting their utility as independent screening tools.
In a new study published in Nature, we present a multimodal artificial intelligence (AI) system capable of passively detecting signs of hypertension using a consumer smartwatch, without requiring any cuff calibration. Dubbed AI-PPG-ACC-HTN, we validated this system against the clinical gold standard of 24-hour ambulatory blood pressure monitoring (ABPM), and it achieves accuracy levels comparable to traditional cuff-based diagnostic workflows for both initial and confirmatory screening. These research findings helped inform the blood pressure trends Health Guardian feature in the Google Health app.
Instead of attempting to estimate exact, point-in-time systolic and diastolic blood pressure values, which are highly susceptible to transient environmental noise, our system reframes the problem. It focuses on identifying an individual’s underlying, persistent hypertensive state by aggregating passive physiological signatures over multiple days.
The system leverages data from two sensors already active on modern smartwatches:
- Photoplethysmography (PPG): An optical sensor that tracks changes in blood volume at the wrist by measuring reflected light that captures pulse wave contours.
- Accelerometry (ACC): A motion sensor that identifies periods of stillness and captures the ballistocardiogram (BCG), the subtle physical vibrations of the wrist caused by the mechanical ejection of blood from the heart into the aorta.
To build this system, we used a two-stage machine learning approach:
We trained a 1-D deep convolutional neural network using self-supervised contrastive learning. By analyzing a large, unlabeled dataset of 492,347 hours of sensor data from 2,109 consenting participants, the model learned to map overlapping 15-second PPG and ACC waveforms from the same individual close together in a latent space. This allowed the model to discover complex, physiologically rich features of vascular and mechanical cardiac function without requiring manual feature engineering or medical labels.
For each user, these 15-second feature blocks (embeddings) are mean-aggregated across multiple days of wear to wash out ephemeral noise like sudden movements or temperature changes. Finally, the individual's aggregated embedding is combined with their height (which serves as a reliable proxy for arterial path length) and fed into a regularized logistic regression classifier to calculate a continuous hypertension probability score.
To evaluate our system, we conducted a prospective, multi-center clinical study across five US sites involving 196 consenting diverse participants who were free from known cardiovascular disease and not taking blood pressure medications.
Importantly, we benchmarked the smartwatch's performance against 24-hour ambulatory blood pressure monitoring (ABPM), the clinical gold standard for hypertension diagnosis. We evaluated the smartwatch system across two clinical use case scenarios: initial screening and confirmatory testing.
The smartwatch achieved a moderate sensitivity of 65.8% and a high specificity of 90.0%, resulting in a high positive predictive value (PPV) of 80.6%. In comparison, initial office-based screenings showed a sensitivity of 55.3% and a moderate PPV of 77.8% when benchmarked against the gold standard.
For individuals who initially screen positive for high blood pressure in a clinic, current guidelines recommend confirmatory out-of-office tracking. We looked at the subset of participants (N=48) who had elevated initial office BP to see how well the smartwatch could confirm sustained hypertension.
Our multimodal system achieved a moderate sensitivity of 78.4%, a high specificity of 90.9% and a high PPV of 96.7%. In comparison, the performance of return office BP measurements showed lower point estimates of sensitivity (67.6%), specificity (63.6%), and PPV (86.2%). Furthermore, the smartwatch approach proved competitive with multi-day home monitoring, which yielded a sensitivity of 89.2%, specificity of 81.8%, and a PPV of 94.3%.
Taken together, the results show that our system can detect hypertension with accuracy levels comparable to traditional cuffed BP devices in the existing clinical framework.
To gain an understanding of what the AI model may be paying attention to, we visualized the average pulse waveforms from users with the highest and lowest predicted probabilities of hypertension.
We observed the following visual differences:
- Reduced pulse width: Waveforms linked to a higher risk of hypertension exhibited a slightly narrower pulse width (figure below, top left panel), indicating a smaller change in blood volume, and may suggest stiffer arteries that are less able to expand.
- Pulse wave reflection: Higher AI risk scores correlated with a slower systolic upstroke (the initial surge of blood) (figure below, highlighted yellow circle in middle panel) and a lower d/a ratio (figure below, highlighted yellow circle in right panel). This specific metric compares the initial forward-traveling pulse wave to the reflected wave bouncing back from the body's vascular network.
- Mechanical heart vibrations: The smartwatch accelerometer successfully captured the ballistocardiogram (BCG) signal. In users with higher predicted hypertension, we observed distinct physical modulations in these micro-vibrations, specifically deeper "K waves" and wider "IJK complexes" (figure below, highlighted yellow circle in bottom left panel).
Mean pulse waveforms (top left panel), corresponding accelerometer waveforms showing the ballistocardiogram (BCG, bottom left panel), first (middle panel) and second derivatives (right panel) of pulse waveforms from four of the most extreme quintiles of AI-PPG-ACC-HTN scores. Key fiducial points are indicated including the pulse onset (ons), peak (sys), dicrotic notch (dic), diastolic peak (dia) in the PPG waveform, H, I, J, K, L, M, N waves in the BCG waveform, and a, b, c, d, e waves in the second derivative of the PPG waveform.
Smartwatch-based hypertension screening is not intended to replace standard clinical arm cuffs or provide a definitive standalone medical diagnosis. Instead, this research points to the potential for a highly scalable, passive tool for opportunistic screening. This work represents early feasibility research and methodologies described here are purely exploratory and are not indicative of any existing or upcoming commercial product feature or device capability. By gently prompting at-risk individuals to step into a clinic for formal assessment, this technology holds the potential to significantly close the global awareness gap and catch hypertension before it causes permanent cardiovascular damage.
This research was a collaborative effort between Google Research, Beth Israel Deaconess Medical Center, and Harvard Medical School. We thank our paper co-authors Lawrence Cai, Jiang Wu, Mingwu Gao, Bhavna Daryani, Jonathan Wang, Utkarsh Khanna, Ho Ko, Anupam Pathak, Mark Malhotra, Shwetak Patel, Jacqueline B. Shreibati, Stephen P. Juraschek, Pramod Rudrapatna, and Matthew Thompson. We thank key contributors including: Jennifer Block, Anu Gabbita, Sushalini Sunku, Keerthana Natarajan, Alexandros Pantelopoulos, Tuan Phan, Tracy Giest, and Florence Thng.
    ×
    ❮
    ❯
    
  
  ×
