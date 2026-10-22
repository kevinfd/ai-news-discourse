---
id: "1eefeec8a402d28e"
title: "llampart - a local Web UI for llama-server, vLLM and OpenAI-compatible APIs - v2.0.1"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbnm5c/llampart_a_local_web_ui_for_llamaserver_vllm_and"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbnm5c/llampart_a_local_web_ui_for_llamaserver_vllm_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T13:46:15Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["mossy_troll_84"]
language: "en"
summary: "Hi everyone! I'm the developer of llampart , an open-source Web UI for chatting with LLMs. I've just released v2.0.1 , and since version 1.9.0 the project has changed quite a bit, so I wanted to share what I've been working on. For anyone seeing it for the first time, llampart is a self-hosted, desktop-focused chat interface built with Svelte 5 and SvelteKit. It started from the llama.cpp /…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "post"
word_count: 710
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbnm5c/llampart_a_local_web_ui_for_llamaserver_vllm_and/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# llampart - a local Web UI for llama-server, vLLM and OpenAI-compatible APIs - v2.0.1

Reddit · mossy_troll_84 · 2026-10-21

Hi everyone! I'm the developer of llampart , an open-source Web UI for chatting with LLMs. I've just released v2.0.1 , and since version 1.9.0 the project has changed quite a bit, so I wanted to share what I've been working on. For anyone seeing it for the first time, llampart is a self-hosted, desktop-focused chat interface built with Svelte 5 and SvelteKit. It started from the llama.cpp / llama-ui foundation and has gradually grown into its own project so different from original base. The idea is pretty simple: I wanted a comfortable interface for working with local models, with good conversation management, useful tools, plenty of customization, and no unnecessary cloud services and most of all in my own language interface. What does llampart do? It connects to an LLM backend that you run separately. It currently supports llama-server (llama.cpp), vLLM, and OpenAI-compatible API servers . Your conversations are stored in your browser using IndexedDB, and most application settings are stored locally as well. There's no llampart account or hosted conversation service. Of course, prompts are still sent to whichever backend you configure, whether that's on your own machine, your LAN, or a remote server. Some of the features include: Frosted Glass - a translucent interface with bundled or custom wallpapers, adjustable transparency, UI scaling, typography settings, and a customizable conversation sidebar. Conversation management - branching conversations, pinned chats, search, import/export, and local conversation history, 2 colums sidebar Reasoning and tool calling - support for reasoning-capable models, tool execution, and multi-step agent workflows. MCP integration - connecting MCP servers and working with their tools, prompts, and resources. Attachments and Markdown - file handling, PDF support, syntax-highlighted code blocks, tables, and content export. Six interface languages - English, Polish, German, Spanish, French, and Italian.+ more to come llampart - UI What's new since 1.9.0? The biggest change is that llampart is no longer focused only on llama-server. I've worked on making the application understand the differences between providers instead of treating every OpenAI-compatible API as identical. This includes separate provider configurations, model selection, support for the appropriate Chat Completions or Responses protocol where available, and better handling of model capabilities. Reasoning support has also been improved. The available reasoning controls depend on the selected model and provider, so the interface can avoid sending settings that the backend doesn't support. Another major addition is AI-generated charts and diagrams directly inside chat messages . Models can produce interactive Line, Area, Bar, and Donut charts using a structured JSON format. Charts can be previewed and exported as PNG, SVG, or CSV. There's also Mermaid support for Flowcharts, State Diagrams, Mindmaps, and Gantt charts , with previews and PNG/SVG export. llampart - UI and charts, diagrams I've spent quite a lot of time improving how these are displayed — especially chart labels, diagram layouts, and making exports useful outside the application. There are also new response preferences , which let you guide how models format their answers. For example, you can ask for more concise responses, practical examples, tables, charts, diagrams, or fewer decorative elements without manually repeating these instructions every time. A lot of work has gone into things that are less visible in screenshots: conversation data integrity, streaming and cancellation, model switching during active requests, MCP permissions, tool result persistence, and safer handling of asynchronous operations. https://preview.redd.it/digklhoqrtwh1.png?width=3840&format=png&auto=webp&s=b9312447e78158230bb60923a4020e78ea269add Installation llampart is a Web UI, not a model runner. You'll still need your own LLM backend - lama-server (llama.cpp), vLLM, and OpenAI-compatible API servers . For Linux, there's an installer for Ubuntu-based and Arch-based systems. It uses an existing Caddy installation to serve the prebuilt WebUI and handle the API proxy. You don't need Node.js to run the installed release. You can also clone the repository and run the SvelteKit development server if you prefer. The interface is currently designed primarily for desktop use, and backend features naturally depend on what your model server actually supports. The project is MIT-licensed and available here: GitHub: https://github.com/mchowy-troll/llampart Latest release (2.0.1): https://github.com/mchowy-troll/llampart/releases/tag/v2.0.1 I'm developing this because it's something I wanted to use myself, and I'm continuing to improve it as I run into issues or find things that could work better. I'd really appreciate feedback, especially from people using different local models. Thanks for taking a look!
