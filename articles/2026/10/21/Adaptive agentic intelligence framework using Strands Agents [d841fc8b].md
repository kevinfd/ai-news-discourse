---
id: "d841fc8b370bc211"
title: "Adaptive agentic intelligence framework using Strands Agents"
url: "https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents"
link: "https://aws.amazon.com/blogs/machine-learning/adaptive-agentic-intelligence-framework-using-strands-agents"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-21T21:23:26Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Nitin Eusebius"]
language: "en"
summary: "Organizations building AI agents face a common challenge: Every request, whether a routine status check or complex analysis, typically gets routed to a single large, expensive model. This one-size-fits-all approach can drive up API costs, introduce unpredictable latency, and remove the possibility of offline operation. Even routine queries that could resolve locally end up requiring a full…"
tags: ["Advanced (300)", "Amazon Bedrock", "Technical How-to"]
orgs: ["Amazon", "Nvidia"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 1499
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Adaptive agentic intelligence framework using Strands Agents

AWS Machine Learning Blog · Nitin Eusebius · 2026-10-21

Artificial Intelligence
Adaptive agentic intelligence framework using Strands Agents
Organizations building AI agents face a common challenge: Every request, whether a routine status check or complex analysis, typically gets routed to a single large, expensive model. This one-size-fits-all approach can drive up API costs, introduce unpredictable latency, and remove the possibility of offline operation. Even routine queries that could resolve locally end up requiring a full network round-trip to a cloud-hosted large language model (LLM).
The Adaptive Agentic Intelligence Framework (AAIF), built with Strands Agents, takes a different approach. Instead of routing all requests to a single large model, AAIF uses small language models (SLMs) to handle routine tasks locally. More complex requests are routed to cloud-hosted models through Amazon Bedrock. This approach builds on the research position from Belcak et al. at NVIDIA. They argue that small language models are “sufficiently powerful, inherently more suitable, and necessarily more economical for many invocations in agentic systems.” Built on Strands Agents, the framework demonstrates how intelligent model orchestration can help reduce costs while maintaining low latency for local operations.
In this post, we walk through the key components of AAIF using Strands Agents with local SLMs through Ollama and cloud models through Amazon Bedrock. We use an Internet of Things (IoT) monitoring scenario as a reference implementation.
Solution overview
AAIF organizes AI processing into three layers, each optimized for different task types, as Figure 1 shows:
- Smart orchestration uses a lightweight SLM (llama3.2:1b) as the decision-making layer. This orchestrator classifies incoming requests and routes them to the appropriate processing layer without hardcoded rules.
- Local processing handles routine tasks like device telemetry retrieval and image analysis using SLMs running on local hardware through Ollama. These tasks complete with low latency and no cloud dependency.
- Cloud processing handles complex pattern analysis and strategic recommendations through frontier models in Amazon Bedrock. These requests need broader context and multi-step reasoning that SLMs cannot reliably provide.
Figure 1 shows the complete AAIF system architecture. At the center sits the Strands agent, which connects to an Ollama runtime hosting both the 1B-parameter orchestrator model and the vision model. The agent exposes three tools: get_device_telemetry for local sensor data retrieval, analyze_camera_feed for on-device vision processing through llama3.2-vision, and get_expert_insights which calls Amazon Bedrock through boto3 for complex analysis. Incoming user requests flow through the SLM orchestrator, which classifies each request and dispatches it to either a local tool or the cloud endpoint based on task complexity.
The framework adapts to your deployment constraints rather than requiring you to restructure your infrastructure around it. This architecture runs on edge devices like a Raspberry Pi with 8 GB of memory, in full cloud deployments where all inference hits Amazon Bedrock, or in hybrid configurations that combine local speed with cloud reasoning. The flexibility comes from separating the routing logic (the SLM orchestrator) from the processing tools, which you can swap or reconfigure independently depending on available hardware and network connectivity.
Prerequisites
For this walkthrough, you should have the following prerequisites:
- An AWS account.
- Amazon Bedrock model access configured in the required Region.
- Python 3.10+ installed.
- Ollama installed with the following models pulled: 
         
  - ollama pull llama3.2:1b (orchestrator).
  - ollama pull llama3.2-vision (vision analysis).
- Strands Agents installed: pip install strands-agents strands-agents-tools.
- AWS Command Line Interface (AWS CLI) configured with appropriate credentials.
- Boto3 installed: pip install boto3.
Set up the environment
Create a project directory and start the Ollama server:
Pull the required models:
Create a file called aaif_agent.py and add the following components.
Implement local processing tools
Strands Agents uses the @tool decorator to define capabilities that agents can invoke. Start by creating tools for local processing.
The first tool retrieves device telemetry data. In a production environment, this would connect to actual IoT sensors. For this walkthrough, it uses simulated device data:
The second tool performs vision analysis using a local SLM. The llama3.2-vision model runs entirely on local hardware, which means sensitive camera feeds don’t leave the device:
Implement cloud processing
For complex analysis that requires broader reasoning, create a tool that calls Amazon Bedrock. This tool is invoked only when the orchestrator determines that local models can’t handle the request:
Configure the Strands agent with smart orchestration
The core of AAIF is the Strands agent configuration. The agent uses a local SLM (llama3.2:1b) as its orchestrator. Strands Agents supports multiple model providers, and here we use the Ollama provider to run the orchestrator locally:
The SLM-powered orchestrator analyzes each request and routes it to the appropriate tool without hardcoded keyword matching. The routing happens through the model’s understanding of the request:
Table 1: Request, routing, and latency estimates for local compared to cloud inference
Run the agent
With the agent configured, you can interact with it directly:
The agent automatically classifies each request and routes it to the appropriate processing layer. No explicit routing rules are needed.
Adapt to different deployment scenarios
The AAIF architecture adapts to different infrastructure requirements by changing the model configuration:
When your workload runs entirely in the cloud and no edge hardware is available, replace the Ollama model configuration with Amazon Bedrock for all processing. This routes every request through managed cloud inference, giving you auto scaling without requiring local GPU resources. Teams with reliable low-latency connectivity and no data residency constraints benefit most from this configuration:
The hybrid configuration keeps the local SLM orchestrator intact while adding cloud models for requests that exceed local model capabilities. This is the default AAIF configuration shown in this walkthrough. It suits environments where most requests are routine enough to resolve locally, but some require the broader reasoning of a larger model. Cost savings can come from the roughly 80 percent of traffic that doesn’t hit a paid API endpoint.
For environments that are fully air-gapped or have strict data sovereignty requirements, replace the cloud tool with a larger local model and run all processing on-device. A 3B-parameter model running on hardware with adequate memory can handle moderately complex tasks that the 1B orchestrator would otherwise escalate. The trade-off is reduced reasoning depth on the hardest queries, but the benefit is data not leaving the premises:
Looking ahead: Centralized tool calling with MCP servers
The implementation in this post uses local tool calls defined directly in the agent code. For production deployments with multiple agents sharing tools across services, expose these tools as Model Context Protocol (MCP) servers. MCP provides a standardized interface for tool discovery and invocation, so you can centralize tool management and reuse tools across different agents and environments. In Figure 3, we show how to convert AAIF tools into MCP servers for distributed, centralized tool calling.
In the distributed configuration as shown in Figure 3, Device 1 acts as the orchestrating hub, running the Strands agent with the SLM router and a local telemetry tool. It connects through the MCP protocol to Device 2, which runs an edge vision processing server with llama3.2-vision. Device 3 serves as a cloud analytics gateway connected to Amazon Bedrock. From the orchestrator’s perspective, all remote tools appear as local function calls because the MCP transport layer handles serialization and network communication transparently.
Cleaning up
To avoid incurring future charges, complete the following cleanup steps:
- Disable Amazon Bedrock model access: Open the Amazon Bedrock console, choose Model access, and revoke access for Amazon Nova Lite. For detailed steps, see Manage model access in the Amazon Bedrock User Guide.
- Stop the Ollama server and remove models to free local disk space (approximately 2 GB):
- Delete the project directory if you no longer need the sample code:
Conclusion
We showed how to build cost-effective AI agents using the Adaptive Agentic Intelligence Framework with Strands Agents. By routing routine requests to local SLMs and reserving cloud models on Amazon Bedrock for complex analysis, AAIF can help reduce API costs while maintaining low latency for routine operations.
Before you run this pattern in production, add responsible AI controls to the cloud inference path, since those requests carry tool outputs, retrieved data, and user input. You can attach Amazon Bedrock Guardrails to the Strands BedrockModel with a guardrail ID and version. It then applies content filters for harmful categories, prompt injection filters, and contextual grounding checks that block responses not supported by the source data. To apply the same policies to the local SLM tier, call the standalone ApplyGuardrail API on its inputs and outputs. This way, every request follows one safety standard no matter which model handles it.
This architectural pattern applies beyond IoT monitoring. A healthcare organization could run patient monitoring locally while routing diagnosis support to cloud models. A financial services firm could process transactions on-premises and reserve cloud capacity for risk analysis. A manufacturing team could run quality control vision models at the edge while sending optimization requests to the cloud.
To learn more about building agents with Strands Agents, visit the Strands Agents documentation. For information about available foundation models, see Amazon Bedrock.
