---
id: "d1f41ec0b14352fe"
title: "27 Cybersecurity Terms to Prepare You for the Age of AI"
url: "https://marktechpost.com/2026/11/23/27-ai-cybersecurity-terms"
link: "https://marktechpost.com/2026/11/23/27-ai-cybersecurity-terms"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T10:40:16Z"
published_date: "2026-11-23"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Michal Sutter"]
language: "en"
summary: "AI now sits on both sides of the security fight, and the vocabulary has changed with it. IBM’s 2026 Cost of a Data Breach Report found that 1 in 4 malicious breaches were AI-enabled, up 56% year over year. Those breaches cost an average of $6 million, about $1 million above the $4.99 million global average. \n\n Attackers now target the models themselves, the agents that act on their output, and…"
tags: ["Agentic AI", "Editors Pick", "For Devs", "Security", "Software Engineering", "Staff"]
orgs: ["Microsoft", "Anthropic", "US government", "Google", "IBM", "OpenAI", "Cursor", "UK"]
topics: ["models & research", "agents & coding", "business & funding", "safety & ethics"]
content_source: "summary"
word_count: 2021
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# 27 Cybersecurity Terms to Prepare You for the Age of AI

MarkTechPost · Michal Sutter · 2026-11-23

AI now sits on both sides of the security fight, and the vocabulary has changed with it. IBM’s 2026 Cost of a Data Breach Report found that 1 in 4 malicious breaches were AI-enabled, up 56% year over year. Those breaches cost an average of $6 million, about $1 million above the $4.99 million global average. 

 Attackers now target the models themselves, the agents that act on their output, and the people who trust what AI produces. The reference lists have moved fast to keep up. OWASP published its Top 10 for LLM Applications 2026 on August 4, 2026, and its first Top 10 for Agentic Applications in December 2025. MITRE ATLAS maps attacker tactics against AI systems the way ATT&CK does for IT. 

 The 27 terms below are grouped in 4 parts: attacks on models, agentic risks, AI-powered attacks on people, and the defenses that answer them. 

 Part 1: Attacks on the model itself 

 These attacks target what a model reads, learns or reveals. NIST groups them into evasion, poisoning, privacy and misuse in its Adversarial Machine Learning taxonomy (NIST AI 100-2e2025) , published March 2025. 

 1. Prompt injection 

 Prompt injection is input crafted to override a model’s intended instructions. It has ranked No. 1 on every edition of the OWASP LLM list, including the 2026 edition . LLMs have no hard boundary between instructions and data, so any text the model reads can try to steer it. 

 2. Indirect prompt injection 

 Indirect prompt injection hides the malicious instruction in content the model retrieves: an email, a web page, a PDF or a code comment. The user never types it. The clearest real case is EchoLeak (CVE-2025-32711) , a zero-click flaw in Microsoft 365 Copilot rated CVSS 9.3. Aim Security showed that one crafted email could make Copilot leak organizational data; Microsoft fixed it server-side in May 2025. 

 3. Jailbreak 

 A jailbreak tricks a model into ignoring its safety training, usually through role-play, fake context or sheer volume. Anthropic’s many-shot jailbreaking research showed that stuffing a long prompt with up to 256 fake dialogues can override safety behavior. Its effectiveness grows with context window size, following a power law. 

 4. Data poisoning 

 Data poisoning plants malicious samples in training or fine-tuning data so the model learns harmful behavior. A joint study by Anthropic, the UK AI Security Institute and the Alan Turing Institute found that just 250 malicious documents could backdoor models from 600M to 13B parameters. The number needed stayed roughly constant regardless of model size. 

 5. Backdoor (sleeper agent) 

 A backdoor is hidden behavior that only activates on a secret trigger. Anthropic’s Sleeper Agents paper trained models to write secure code when the prompt said 2023 but insert exploitable code when it said 2024. Standard safety training, including adversarial training, did not remove the behavior. 

 6. Adversarial examples (evasion attacks) 

 An adversarial example is an input changed in small, often invisible ways so a model misclassifies it. Think of a tweaked image, audio clip or malware sample that slips past an AI detector. NIST treats evasion as one of the core attack classes in AI 100-2 . 

 7. Model extraction (distillation attack) 

 Model extraction clones a model’s capabilities by querying it at scale and training a “student” model on the answers. Google’s Threat Intelligence Group reported in February 2026 that these “distillation attacks” were rising. One campaign sent more than 100,000 prompts aimed at Gemini’s reasoning. 

 8. Membership inference and training data extraction 

 Membership inference tests whether a specific record was in a model’s training set. Training data extraction goes further and pulls memorized text out. Carlini et al. extracted hundreds of verbatim sequences from GPT-2 , including personal contact details, using only query access, and found larger models more vulnerable. 

 9. Hidden context exposure 

 Hidden context exposure is the leak of system prompts, tool definitions, retrieved documents or other context a user was not meant to see. OWASP renamed and broadened “System Prompt Leakage” into this entry (LLM08) in its 2026 list . The working rule: assume anything in the context window can be extracted, so never put secrets there. 

 Part 2: Agentic AI risks 

 Once a model can call tools, keep memory and act on its own, a bad output becomes a bad action. OWASP built its Top 10 for Agentic Applications (ASI01 to ASI10) from incidents seen in real deployments. 

 10. Excessive agency 

 Excessive agency means an LLM app has more functions, permissions or autonomy than its task needs. When it is fooled or simply wrong, the damage scales with that reach. In the OWASP LLM Top 10 2026 , excessive agency rose to No. 3, behind only prompt injection and sensitive information disclosure. 

 11. Agent goal hijack 

 Agent goal hijack is ASI01, the top agentic risk: malicious content redirects an agent’s objectives or decision path. It is prompt injection with hands. OWASP cites EchoLeak as an example, where hidden prompts turned a copilot into a silent exfiltration tool. 

 12. Tool poisoning (MCP) 

 Tool poisoning hides malicious instructions inside a tool’s description or schema, which the model reads but the user usually does not see. Invariant Labs disclosed the attack against the Model Context Protocol (MCP) on April 1, 2025. Its proof of concept was an “add two numbers” tool that told the agent in Cursor to read SSH keys and config files. A related “rug pull” swaps a benign tool for a malicious one after the user approves it. 

 13. Memory and context poisoning 

 Memory and context poisoning (ASI06) corrupts an agent’s stored memory, RAG index or embeddings so the bad data shapes future sessions. Unlike a one-off prompt injection, it persists. The fix starts with treating everything written to memory as untrusted input, with provenance and expiry. See OWASP’s agentic list for mitigations. 

 14. Slopsquatting 

 Slopsquatting is registering a package name that AI coding tools hallucinate, so developers or agents who follow the AI install attacker code. A USENIX Security 2025 study of 16 code models and 576,000 samples found 19.7% of recommended packages did not exist. That added up to 205,474 unique fake names, many of them repeated across runs and therefore easy to target. 

 15. Non-human identities (NHIs) 

 NHIs are the service accounts, API keys, tokens, certificates and AI agents that authenticate without a person. Palo Alto Networks’ 2026 Identity Security Landscape puts the ratio at 109 machine identities per human, up from 82:1 a year earlier. OWASP’s ASI03 (identity and privilege abuse) covers the risk: agents that inherit, cache or pass on credentials they should not hold. 

 Part 3: AI-powered attacks on people and organizations 

 These attacks use AI as the weapon rather than the target. They exploit trust: in a familiar face, a familiar voice, a well-written email or a helpful tool. 

 16. Deepfake impersonation 

 A deepfake is AI-generated video, audio or imagery that convincingly mimics a real person. In early 2024, a finance worker at engineering firm Arup’s Hong Kong office transferred HK$200 million (about US$25.6 million) in 15 transactions after a video call where the “CFO” and colleagues were all deepfakes. IBM’s 2026 report found deepfake impersonation was the most common AI-enabled attack type, at 45% . 

 17. Voice cloning (AI vishing) 

 Voice cloning creates a synthetic copy of someone’s voice from a short sample. Vishing is voice phishing that uses it. In May 2025 the FBI warned that since April 2025, attackers had sent AI-generated voice messages impersonating senior US officials to build rapport and take over accounts. Its advice: verify the person through a contact method you already know. 

 18. AI-generated phishing 

 AI-generated phishing uses LLMs to write targeted, fluent lures in the victim’s own language and at scale. Microsoft’s Digital Defense Report 2025 found AI-automated phishing emails got a 54% click-through rate, versus 12% for standard ones. That is 4.5 times more effective, and Microsoft estimates AI can make phishing up to 50 times more profitable. 

 19. Shadow AI 

 Shadow AI is employees using AI tools the organization has not approved or cannot see. Pasting customer data into a public chatbot is the classic case. IBM’s 2025 report found high shadow AI use added $670,000 to the average breach cost. By the 2026 report , shadow AI was involved in 43% of the incidents IBM studied. 

 20. AI-orchestrated attack (vibe hacking) 

 An AI-orchestrated attack is one where an AI agent runs much of the intrusion itself, not just advises a human. Anthropic’s August 2025 threat report coined “vibe hacking” for a criminal who used Claude Code to hit at least 17 organizations with data theft and extortion. In November 2025 , Anthropic reported a Chinese state-sponsored group (GTG-1002) that jailbroke Claude Code to target roughly 30 organizations. Anthropic called it the first documented large-scale cyberattack executed without substantial human intervention. 

 Part 4: Defenses, standards and governance 

 No single control stops the attacks above. These 7 terms describe the layers that, together, shrink the blast radius. 

 21. AI red teaming 

 AI red teaming is structured adversarial testing of an AI system to find harmful outputs, jailbreaks and security flaws before attackers do. It covers both model safety and the surrounding app, tools and data. MITRE ATLAS gives red teams a shared map of attacker tactics and techniques against AI. NIST’s Generative AI Profile (AI 600-1) , published July 2024, ties testing to its AI Risk Management Framework. 

 22. Guardrails 

 Guardrails are the controls wrapped around a model: input and output classifiers, content filters, policy checks and refusal rules. Anthropic’s Constitutional Classifiers cut the jailbreak success rate on Claude 3.5 Sonnet from 86% to 4.4% in automated tests. A prototype withstood an estimated 3,000+ hours of human red teaming by 183 active participants without a universal jailbreak. 

 23. Zero trust 

 Zero trust means no user, device or workload is trusted by default because of where it sits on the network. Every request is authenticated and authorized on its own. NIST defined the model in SP 800-207 in August 2020. For AI, it means treating agents, tools and retrieved content as untrusted until verified. 

 24. Least agency and human-in-the-loop 

 Least agency extends least privilege to AI: give an agent only the autonomy, tools and permissions its task needs. OWASP introduced the idea in its agentic Top 10 . Human-in-the-loop adds a person’s approval before high-impact actions such as payments, deletions or outbound messages. Short-lived, task-scoped credentials for each agent support both. 

 25. AI bill of materials (AI-BOM) 

 An AI-BOM is a machine-readable inventory of the models, datasets, weights and libraries an AI system uses, including where each came from. It extends the software bill of materials (SBOM) to cover AI supply chain risk. CycloneDX added ML components in version 1.5 (June 2023), and SPDX 3.0 added AI and Dataset profiles in April 2024. 

 26. Content provenance (Content Credentials) 

 Content provenance attaches a signed, tamper-evident record of who made a piece of media and how it was edited. The C2PA standard , branded Content Credentials, is the main open specification. It complements watermarking, and regulation is moving it from optional to expected. Under the EU’s agreed Digital Omnibus on AI , AI Act marking obligations for AI-generated content apply from December 2, 2026. 

 27. Post-quantum cryptography (and harvest now, decrypt later) 

 Post-quantum cryptography (PQC) is encryption designed to resist future quantum computers. “Harvest now, decrypt later” is why it matters today: attackers can steal encrypted data now and read it once quantum machines arrive. NIST published its first PQC standards, FIPS 203, 204 and 205 , on August 13, 2024, and chose HQC as a backup in March 2025. Its final IR 8547 roadmap deprecates quantum-vulnerable public-key algorithms after 2030 and disallows them after 2035. 

 Key takeaways 

 Prompt injection is still OWASP’s No. 1 LLM risk, and agents turn it into real actions. 

 Poisoning is cheap: 250 documents backdoored models up to 13B parameters. 

 People are the softest target: deepfakes led AI-enabled attacks in IBM’s 2026 data. 

 Treat agents as identities: least agency, scoped credentials, human sign-off on high-impact steps. 

 Start PQC migration now: NIST deprecates quantum-vulnerable algorithms after 2030. 
 
 The post 27 Cybersecurity Terms to Prepare You for the Age of AI appeared first on MarkTechPost .
