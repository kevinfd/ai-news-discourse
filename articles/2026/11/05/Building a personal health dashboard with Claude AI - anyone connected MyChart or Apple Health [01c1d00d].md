---
id: "01c1d00dac55f6ea"
title: "Building a personal health dashboard with Claude AI - anyone connected MyChart or Apple Health?"
url: "https://reddit.com/r/ClaudeAI/comments/1xom7vx/building_a_personal_health_dashboard_with_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xom7vx/building_a_personal_health_dashboard_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T15:55:28Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Smaal_God"]
language: "en"
summary: "Hi everyone, I've been dabbling with AI development for about a month now. I have some product management experience, but this is my first attempt at actually building something with AI. I have multiple medical conditions and a ridiculous amount of medical documentation accumulated over the years. I don't mind sharing my medical information with AI for analysis, summaries, etc. My goal is to use…"
tags: ["r/ClaudeAI"]
orgs: ["Apple", "Anthropic"]
topics: ["health & science", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 486
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xom7vx/building_a_personal_health_dashboard_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Building a personal health dashboard with Claude AI - anyone connected MyChart or Apple Health?

Reddit · Smaal_God · 2026-11-05

Hi everyone, I've been dabbling with AI development for about a month now. I have some product management experience, but this is my first attempt at actually building something with AI. I have multiple medical conditions and a ridiculous amount of medical documentation accumulated over the years. I don't mind sharing my medical information with AI for analysis, summaries, etc. My goal is to use Claude to build a proper personal health dashboard and document archive that brings everything together: medical records, lab results, diagnoses, medications, appointments, notes, follow-up questions, billing, and so on. So far, so good. I'm making decent progress. But now I'm looking into integrations, and that's where I'd love some advice. 1. MyChart integration Has anyone managed to connect a personal application to Epic's MyChart? Ideally, I'd like to automatically (or periodically) retrieve: Medical records, clinical notes, and lab results Upcoming appointments and scheduling information Billing information Messages and communication with providers New documents as they become available Is there a practical way to do this? I've read a little about FHIR APIs, but I'm not sure how accessible they are to individual developers building tools for personal use. I would prefer a proper API integration over browser automation. I'd rather not rely on Chrome or have an AI agent logging into MyChart and clicking around. Is that a reasonable concern? 2. Apple Health / Apple Watch I wear an Apple Watch and have years of data in Apple Health. I'd love to integrate heart rate, sleep, activity, blood oxygen, and other available metrics into the same dashboard. Has anyone built a reliable way to sync Apple Health data into a custom application? Does this require an iOS app using HealthKit, or are there simpler solutions? 3. Architecture, privacy, and security I'm also curious how others approach storing and processing sensitive health information in AI-powered applications. I'm comfortable using cloud AI for analysis, but I'd prefer to keep the actual document archive and structured database under my control. What would you recommend for the architecture? Local database, cloud backend, hybrid? And what about giving an AI assistant access to historical records so it can answer questions across multiple years without uploading everything each time? 4. Emergency / family access I'm also building a separate view for my wife, with essential medical information she might need in an emergency: diagnoses, medications, medical history, doctors, and important documents. Has anyone implemented something similar? How do you handle secure access without making it unnecessarily complicated in an emergency? 5. What else would you integrate? If you were building a personal health management system from scratch, what other data sources, integrations, or features would you consider essential? I'm particularly interested in hearing from people who've actually built something similar, rather than recommendations for existing commercial health apps. Would love to compare notes, hear what worked (and what didn't), and possibly share my progress as I go.
