---
id: "442c2eb5c2c85552"
title: "Show HN: AegisKernel – Zero-trust POSIX runtime for AI agents in <0.016ms"
url: "https://adikshatriyag-crypto.github.io/aegis-kernel"
link: "https://adikshatriyag-crypto.github.io/aegis-kernel"
source: "adikshatriyag-crypto.github.io"
domain: "adikshatriyag-crypto.github.io"
source_type: "community"
collector: "hackernews"
date: "2026-11-06T17:00:23Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["adityawebde"]
language: "en"
summary: "Live Capability Policy Interceptor\nSecondary LLM filters add 800ms latency and fail against indirect injection. AegisKernel enforces strict deterministic capability scopes (<0.016ms) before tools execute.\n        ●\n        Test both safe commands (ls, cat, echo) and hostile exploits (.env theft, rm, curl egress)\n      \n            Test Commands & Scenarios\n            Preset Scenarios\n         …"
tags: []
orgs: ["Anthropic"]
topics: ["policy & regulation", "agents & coding"]
content_source: "fulltext"
word_count: 115
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50394991"
score: 12
comments: 3
community: "Hacker News"
---

# Show HN: AegisKernel – Zero-trust POSIX runtime for AI agents in <0.016ms

adikshatriyag-crypto.github.io · adityawebde · 2026-11-06

Live Capability Policy Interceptor
Secondary LLM filters add 800ms latency and fail against indirect injection. AegisKernel enforces strict deterministic capability scopes (<0.016ms) before tools execute.
        ●
        Test both safe commands (ls, cat, echo) and hostile exploits (.env theft, rm, curl egress)
      
            Test Commands & Scenarios
            Preset Scenarios
          
              
              Custom editable
            
Aegis Capability Enforcement:
Strict process-tree policy boundary
            Policy Enforcement Telemetry
            
              STANDBY
            
          
EVALUATION TIME
-- ms
POLICY VERDICT
IDLE
AUDIT TOKEN HASH
--
Production Integration Snippet (PyPI: aegis-kernel)
CrewAI / LangChain / Claude Code Ready
from aegis import AegisShield, SecurityPolicy
# Define capability context for autonomous agent tool execution
shield = AegisShield(policy=SecurityPolicy.strict(allowed_paths=["./data", "./output"]))
@shield.protect_tool
def execute_agent_tool(command: str):
    return os.system(command)  # Drops unauthorized execve/openat in <0.016ms before execution
