---
id: "3a626b2a1bab299c"
title: "200 OK is dead as an AI agent health signal. Here’s what comes next."
url: "https://thenewstack.io/silent-ai-agent-failures"
link: "https://thenewstack.io/silent-ai-agent-failures"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T16:00:00Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Boris Chabeda"]
language: "en"
summary: "A customer asks whether they can swap unworn boots for a size 10. The agent replies, in under a second, that it cannot help with that topic. The web service returns 200 OK . Latency is nominal, error counters are flat, and the Datadog dashboard stays solid green. A customer has just left, and nothing in the APM stack knows. \n\n That is the failure this article is about: the kind that looks like…"
tags: ["AI Agents", "AI Engineering", "Observability", "sponsor-andela", "sponsored-post-contributed"]
orgs: ["OpenAI", "Meta"]
topics: ["agents & coding", "models & research", "chips & infrastructure", "health & science"]
content_source: "summary"
word_count: 2169
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# 200 OK is dead as an AI agent health signal. Here’s what comes next.

The New Stack · Boris Chabeda · 2026-11-18

A customer asks whether they can swap unworn boots for a size 10. The agent replies, in under a second, that it cannot help with that topic. The web service returns 200 OK . Latency is nominal, error counters are flat, and the Datadog dashboard stays solid green. A customer has just left, and nothing in the APM stack knows. 

 That is the failure this article is about: the kind that looks like success. 

 In lean manufacturing, this exact category of silent defect is solved using two twin principles: Poka-Yoke (mistake-proofing stations so bad parts cannot pass) and Jidoka (autonomation—building machines that detect anomalies themselves and automatically halt the line via an Andon emergency cord rather than waiting for downstream customer complaints). 

 “A customer has just left, and nothing in the APM stack knows. That is the failure this article is about: the kind that looks like success.” 

 Modern AI agent engineering needs to adopt this exact control-loop architecture, replacing passive health checks with active station barriers. 

 1. Error analysis: Finding what to watch 

 When we retrospectively ran an offline evaluation benchmark script against three weeks of archived Datadog logs, we found our primary intent classifier had silently dropped 4.2% in schema-valid classification accuracy—masked entirely by default fallback handlers returning 200 OK . 

 We started by conducting a manual, single-day audit of 100 randomly sampled 200 OK production traces pulled directly from our archived Datadog logs. Two engineers read the raw customer text and manually categorized every routing decision against a ground-truth spreadsheet rubric. 

 When we bucketed those 100 manual traces, the breakdown was stark: 

 62% Explicit schema violations / API timeouts: Caught by standard error boundaries or handled by fallback defaults. 

 11% False negatives: Let spam or out-of-scope queries pass downstream (wasting LLM tokens). 

 27% False-positive blocks: Valid customer inquiries incorrectly classified as OUT_OF_SCOPE . 

 This manual audit revealed our critical blind spot. A false negative wastes a few cents in tokens; a schema crash raises a 500 error and pages on-call; but a false-positive block turns away a customer while returning a clean 200 OK . That audit gave us both our core metric to guard—the False Positive Block Rate (FPBR)—and the foundational insight needed to design our observability layer. 

 2. Why the intent classifier is the blast-radius bottleneck 

 In our production customer support agent architecture, requests are rarely handled by a monolithic, generalist LLM. Instead, our deployments rely on a multi-agent orchestration pattern (router-specialist topology). An inbound user prompt first hits a triage router agent, which parses the query and dispatches it to downstream domain specialists (Billing, Account Access, Returns), or short-circuits it if it falls outside support bounds ( OUT_OF_SCOPE ). 

 Of all the components in this multi-agent stack, we evaluate the Intent Classification Agent first because it sits at the front door. 

 “An intent classifier false positive has the highest cascading blast radius in the multi-agent topology because it causes a silent, permanent customer drop-off that bypasses all downstream observability.” 

 If the intent classifier makes a false-positive error—misinterpreting a legitimate exchange or warranty claim as OUT_OF_SCOPE —it triggers an immediate short-circuit. Downstream specialists are never invoked, tokens are saved, and the system cheerfully returns a 200 OK refusal. An intent classifier false positive has the highest cascading blast radius in the multi-agent topology because it causes a silent, permanent customer drop-off that bypasses all downstream observability. 

 3. Jidoka: Measuring the judge (RoBERTa vs. LLM-as-a-judge) 

 While the industry frequently defaults to “LLM-as-a-judge” frameworks (using models like GPT-4o or Llama 3) for agent monitoring, we deliberately deployed a fine-tuned encoder model (RoBERTa-base NLI cross-encoder). 

 To judge an intent classification output, you aren’t asking a model to generate free-form text; you are asking it to evaluate context, verify constraints, and output a strict classification label. Encoders are native classification architectures that look at the entire prompt context multidirectionally rather than predicting the next token autoregressively. This makes them faster, entirely deterministic, free of token-generation overhead, and natively suited for semantic entailment tasks. 

 Why RoBERTa-base (and when to use DeBERTa instead) 

 We chose RoBERTa-base specifically for its infrastructure footprint: at ~1.5 GB RAM, it dropped onto our existing c7i.xlarge nodes with zero new cloud cost overhead. 

 If your customer queries frequently exceed 256 tokens or you are hunting for marginal accuracy gains across enterprise-wide clusters, DeBERTa-v3-base is a better option. DeBERTa’s disentangled attention mechanism yields a 1–2% bump in semantic entailment accuracy. However, that comes at the cost of a heavier CPU compute profile requiring careful thread pinning if co-hosted on legacy nodes alongside core routing services. 

 Before loading our evaluator in production, we lock PyTorch execution to a single dedicated core and run a container warmup pass to eliminate cold-start latency penalties: 

Python
import os
from typing import Any, Dict
from enum import Enum
import torch
from transformers import pipeline

# Lock PyTorch math engine to 1 CPU core before model initialization
torch.set_num_threads(1)
torch.set_num_interop_threads(1)
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

class AllowedIntent(str, Enum):
 RETURN_POLICY = 'RETURN_POLICY' # Exchanges classified here
 ORDER_STATUS = 'ORDER_STATUS'
 ACCOUNT_ACCESS = 'ACCOUNT_ACCESS'
 OUT_OF_SCOPE = 'OUT_OF_SCOPE'

class RoBERTaEvaluator:
 """Local, thread-bounded NLI Cross-Encoder Evaluator."""
 def __init__(self, model_path: str):
 self.pipe = pipeline("text-classification", model=model_path, device="cpu")
 self.id2label = self.pipe.model.config.id2label
 
 # Engineering scar: Run dummy inference to force graph compilation during container startup
 self.pipe("warmup prompt")

 def check(self, query: str) -> Dict[str, Any]:
 res = self.pipe(query[:2000])[0]
 raw_label = res["label"]
 
 if raw_label.startswith("LABEL_"):
 idx = int(raw_label.replace("LABEL_", ""))
 label_name = self.id2label.get(idx, raw_label)
 else:
 label_name = raw_label

 try:
 matched_intent = AllowedIntent(label_name)
 except ValueError:
 matched_intent = AllowedIntent.OUT_OF_SCOPE

 return {"top_intent": matched_intent, "score": float(res["score"])}

 To construct our training and validation datasets, we combined our 100 manually audited production traces with 20 synthetic edge cases, yielding a 120-query evaluation dataset partitioned into train, dev, and held-out test splits. 

 An evaluator is a second opinion, not ground truth. To validate our RoBERTa judge, we evaluated it against our held-out test split of 40 hand-labeled queries (20 positive, 20 negative): 

 True Positive Rate (TPR): 91.5% (sensitivity in catching actual false-positive blocks). 

 True Negative Rate (TNR): 94.0% (specificity in passing valid agent choices). 

 False Alarm Rate (1 – TNR): 6.0% (the baseline overhead sent to the operator queue). 

 4. The latency budget 

 Adding inline evaluation on the hot path introduces an immediate engineering anxiety: compute cost and latency. 

 We ran our classifier on a co-hosted c7i.xlarge instance (4 vCPUs, 8 GB RAM) capable of handling an average baseline of 100 requests per minute (~1.6 req/sec). To ensure our quality gate did not degrade our p95 SLA or starve adjacent services, we constrained the engine using PyTorch CPU optimization guardrails: 

 Model footprint: Fine-tuned RoBERTa-base cross-encoder (~1.5 GB RAM footprint). 

 Thread capping: Bounded to exactly 1 CPU core via torch.set_num_threads(1) . 

 Maximum peak load: 480 inference calls per minute (~8 classifications per second). This represents the maximum velocity a single modern Intel thread on the c7i instance can achieve for matrix multiplication on standard-length text prompts (~256 tokens). 

 Latency profile: Evaluator execution takes p50 = 42ms and p95 = 88ms (measured via PyTorch benchmark scripts running synthetic 256-token runs on our co-hosted instance). 

 Financial cost: $0.00 in added cloud infrastructure by reclaiming idle CPU headroom on existing nodes. 

 5. Control Poka-Yoke: The software limit switch at the station boundary 

 To fulfill our first Lean requirement, we implement a Control Poka-Yoke as the software equivalent of a manufacturing limit switch that intercepts malformed outputs before downstream tokens are wasted. 

 Before invoking any classifier, we establish our schema contract: 

Python
from typing import Any, Optional, Tuple
from pydantic import BaseModel, Field, ValidationError

class IntentResult(BaseModel):
 selected_intent: AllowedIntent
 confidence: float = Field(ge=0.0, le=1.0)

def validate_schema(raw: Any) -> Tuple[Optional[IntentResult], Optional[Exception]]:
 if not isinstance(raw, dict):
 return None, TypeError('Raw output is not a dictionary')
 try:
 return IntentResult(
 selected_intent=raw.get('intent'),
 confidence=raw.get('confidence', 0.0)
 ), None
 except ValidationError as exc:
 return None, exc

 validate_schema() acts as the station sensor: nothing crosses this line unvalidated. If an agent emits a malformed structure, execution immediately branches to an operator handoff without executing downstream steps. 

 6. Instrumenting the turn: Telemetry, traces, and what an alert looks like 

 Knowing our judge’s error profile allows us to mathematically derive our trip conditions. Below a 0.9 confidence score, the evaluator’s false-alarm rate spikes above 18%, causing operator fatigue. Therefore, we set our Andon page floor at 0.9. 

 A single agent turn ties together our previously defined schema validator and RoBERTa evaluator inside a nested OpenTelemetry trace tree . The parent span ( intent_agent_turn ) encompasses the primary interaction ( primary_agent_interaction ) and its downstream execution child spans ( context_retrieval , prompt_render , llm_inference ), followed synchronously by the local judge ( nli_evaluation ). When the judge detects a semantic mismatch, it triggers an andon_pulled event acting as our digital emergency stop cord: 

Python
import hashlib
from typing import Any, Dict
from opentelemetry import trace, metrics

tracer = trace.get_tracer('intent_gate', '1.0.0')
meter = metrics.get_meter('intent_gate', '1.0.0')
disagreements_counter = meter.create_counter('intent_gate.disagreements')

def run_turn(conversation_id: str, query: str, prompt_version: str, agent, evaluator: RoBERTaEvaluator) -> Dict[str, Any]:
 turn = {'prompt_version': prompt_version, 'disagreement_type': None}
 
 with tracer.start_as_current_span('intent_agent_turn') as root:
 root.set_attribute('gen_ai.conversation.id', conversation_id)
 root.set_attribute('app.prompt.version', prompt_version)
 root.set_attribute('app.query.sha256', hashlib.sha256(query.encode()).hexdigest()[:16])

 with tracer.start_as_current_span('primary_agent_interaction') as s1:
 with tracer.start_as_current_span('context_retrieval'): pass
 with tracer.start_as_current_span('prompt_render'): pass
 with tracer.start_as_current_span('llm_inference'):
 raw = agent.classify(query=query, prompt_version=prompt_version)

 result, error = validate_schema(raw)
 s1.set_attribute('app.intent.schema_valid', result is not None)
 if result is None:
 s1.set_status(trace.Status(trace.StatusCode.ERROR, 'schema_violation'))
 turn['action'] = 'HANDOFF_SCHEMA_FAILURE'
 return turn

 with tracer.start_as_current_span('nli_evaluation') as s2:
 verdict = evaluator.check(query)
 agent_intent, eval_intent = result.selected_intent, verdict['top_intent']
 
 dtype = None
 if agent_intent != eval_intent:
 if agent_intent == AllowedIntent.OUT_OF_SCOPE:
 dtype = 'SUSPECTED_FALSE_POSITIVE'
 elif eval_intent == AllowedIntent.OUT_OF_SCOPE:
 dtype = 'SUSPECTED_FALSE_NEGATIVE'
 else:
 dtype = 'INTENT_MISMATCH'

 turn.update({
 'agent_intent': agent_intent.value,
 'evaluator_intent': eval_intent.value,
 'evaluator_score': verdict['score'],
 'disagreement_type': dtype
 })
 
 if dtype:
 disagreements_counter.add(1, {'prompt_version': prompt_version, 'type': dtype})
 s2.add_event('andon_pulled', {'type': dtype})
 turn['action'] = 'HANDOFF_EVALUATOR_DISAGREEMENT'
 return turn

 turn['action'] = 'PROCEED_TO_GENERATION'
 return turn

 What the telemetry stack monitors 

 To maintain complete visibility across the agent’s lifecycle, our telemetry watches four distinct layers across the trace hierarchy: 

 Signal Source span/counter Action trigger Schema compliance rate primary_agent_interaction Instant operator handoff on Pydantic ValidationError. Suspected False-Positive Block Rate (FPBR) nli_evaluation counter Andon alert at > 0.9 score; anomaly detection triggers incident workflow. Refusal step-changes Root span outcome (app.outcome) Monitored on deploy dashboard; step-changes trigger prompt rollback review. Downstream task resolution Product analytics trace join Weekly review of whether passed queries resulted in human escalation or re-asks. 

 The first incident: What caught the regression 

 The first time this observability gate ran in production was during the deployment of prompt version v1.2.0 , shipped to tighten return abuse policies. The failure stemmed from a single un-audited prompt modifier that interpreted sizing exchanges as abuse vectors: 

Diff
[System Prompt Diff: v1.1.0 -> v1.2.0]

- Handle customer return requests in accordance with standard 30-day policy windows.
+ Zero tolerance for policy circumvention. Intercept all ambiguous customer inquiries 
+ regarding item modification, sizing swaps, or exchanges as potential return abuse vectors.

 When a quality regression fires, the alert payload received on the #andon-agent-alerts Slack channel contains the exact trace ID, prompt version tag, candidate classification, and the evaluator’s confidence verdict: 

JSON
{
 "event": "QUALITY_REGRESSION_SUSPECTED",
 "trace_id": "37a886864e32af95d4012a30acbda366",
 "prompt_version": "v1.2.0",
 "reason": "EVALUATOR_DISAGREEMENT",
 "disagreement_type": "SUSPECTED_FALSE_POSITIVE",
 "agent_intent": "OUT_OF_SCOPE",
 "evaluator_intent": "RETURN_POLICY",
 "evaluator_score": 0.9412
}

 The incident timeline unfolded in under three minutes: 

 00:00:00 : v1.2.0 deployed globally. 

 00:12:02 (t = 0): The boots query fails 12 minutes after deployment. Agent returns OUT_OF_SCOPE ; evaluator flags RETURN_POLICY (score 0.9412). 

 00:12:04 (t + 2s): #andon-agent-alerts Slack channel receives trace webhook with debug link. 

 00:14:38 (t + 156s): Traffic auto-drains and reverts to stable v1.1.0 following operator intervention. Total detection-to-reset time: 2m 36s. 

 The offline evaluation suite missed this failure because its 250 static test cases contained zero colloquial variants for apparel or shoe sizing swaps. 

 7. Limitations and release provenance protocol 

 Correlated failure blindspots: If both the primary LLM agent and the RoBERTa evaluator misinterpret a novel phrase identically, no alert fires. 

 Cold-start vulnerability: The first 30 requests of a new prompt version are unguarded by monitoring thresholds to prevent small-sample noise trips. 

 Operator dependency: Pulling an Andon cord when no human operators are on duty creates queue backlogs without resolving customer friction. 

 Prompt version provenance: To prevent unannounced semantic drift, treat prompt text with the same CI/CD immutability as compiled bytecode. Every prompt revision is hashed into deployment manifests, and release notes explicitly log every semantic instruction modifier. 

 Summary 

 The problem: Production AI agents fail silently by returning confident, well-formed 200 OK refusals that pass passive APM health checks while turning away legitimate customers. 

 The solution: We applied Lean Poka-Yoke (inline schema validation) and Jidoka (a local, thread-bounded RoBERTa-base cross-encoder judge acting as an automated Andon cord) to evaluate intent classifications synchronously. 

 The economics: By locking the evaluator to 1 CPU core ( torch.set_num_threads(1) ) on co-hosted c7i.xlarge nodes, we achieved p50 = 42ms / p95 = 88ms latency with $0.00 in added cloud infrastructure cost. 

 The incident: When prompt v1.2.0 accidentally flagged product sizing swaps as out-of-scope, the inline judge caught the regression at t=0, alerted #andon-agent-alerts via Slack webhook at t+2s, and enabled a full rollback to v1.1.0 within 2 minutes and 36 seconds. 

 The post 200 OK is dead as an AI agent health signal. Here’s what comes next. appeared first on The New Stack .
