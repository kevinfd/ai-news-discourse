---
id: "9ca2bcd34e5443c6"
title: "Janas: Run LLMs larger than RAM by streaming experts from SSD"
url: "https://github.com/prabanta-dev/janas"
link: "https://github.com/prabanta-dev/janas"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-12T22:05:43Z"
published_date: "2026-10-12"
collected_at: "2026-10-13T20:17:27Z"
authors: ["khalidkhair"]
language: "en"
summary: "37 tok/s from Qwen3-Next-80B (a 48 GB model) on a laptop with 32 GB of memory, 24 without drafts, where llama.cpp manages 2.8; reading a prompt, 62 tok/s against 16. Janas-LLM was faster than llama.cpp on every model compared on the same laptop (Debian 13 Linux, Intel Core Ultra 9 185H, its integrated Arc GPU, 32 GB, an NVMe SSD; 9-12 October 2026; the whole machine below):\nThe same models from…"
tags: []
orgs: ["Intel", "Hugging Face", "Alibaba", "AMD"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 2639
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50063717"
score: 211
comments: 82
community: "Hacker News"
---

# Janas: Run LLMs larger than RAM by streaming experts from SSD

GitHub · khalidkhair · 2026-10-12

37 tok/s from Qwen3-Next-80B (a 48 GB model) on a laptop with 32 GB of memory, 24 without drafts, where llama.cpp manages 2.8; reading a prompt, 62 tok/s against 16. Janas-LLM was faster than llama.cpp on every model compared on the same laptop (Debian 13 Linux, Intel Core Ultra 9 185H, its integrated Arc GPU, 32 GB, an NVMe SSD; 9-12 October 2026; the whole machine below):
The same models from other hands, in the catalog beside them:
Qwen3.8-27B: llama.cpp measured on 12 October 2026 (llama-bench -r 2), Janas-LLM on 13 October (janas-bench --prompt 1024 --gen 16, two rounds), once its prompt went whole to the GPU in one submission: 30.6 tok/s, where it read 26.4 the day before and 18.7 before the GPU's tiles for the IQ4_XS, IQ3_S and IQ4_NL weights of unsloth's UD mix. One exception: the 3-bit Qwen3-30B reads a prompt slower than llama.cpp, since its Q3_K weights do not go to the GPU's fast prompt yet; it writes three times as fast.
How they were measured, and the speeds with the drafts: What works now. On another machine the figures will be other ones: janas-bench measures yours.
Try it on Linux x86-64 (Ubuntu 22.04, Debian 12 and later):
curl -LO https://github.com/prabanta-dev/janas/releases/latest/download/janas-linux-x86_64.tar.gz
tar xf janas-linux-x86_64.tar.gz && cd janas
./janas-chat                     # the models it knows: pick one, it is downloaded and checked
Or on Windows 10 (1903 or later) and 11, x86-64: download janas-windows-x86_64.zip, unpack it, and in a terminal in its janas folder run .\janas-chat. On the same laptop under Windows 11 (12 October 2026) Janas-LLM wrote as fast as on Linux (Qwen3-4B 25.6 tok/s, Qwen3-30B-A3B 34.2) and read a prompt as fast with the mixture (Qwen3-30B-A3B 132 tok/s) and 1.8 times as fast with the dense model (Qwen3-4B 346 tok/s against 193), whose whole blocks go to the GPU, through Intel's own Windows driver there.
The models come already converted from Hugging Face; building from the sources: Getting started.
  ▄███████████▄    
▄███████████████▄  
███ ▄ █████ ▄ ███ ▄   J A N A S
███▄▄▄█████▄▄▄████ 
▀█████▄▀▀▀▄█████▀ ▀   a family of tools for artificial intelligence, in C
  █████████████    
 █ █ █ █ █ █ █ █   
▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀    
Janas is a family of tools for artificial intelligence, written in C with no dependencies beyond the C library. Its first component, Janas-LLM, runs large mixture-of-experts language models on ordinary computers, with or without a GPU: the weights stay on disk, the experts each token needs are streamed from an NVMe SSD, and the ones that keep coming back stay in memory. An 80-billion parameter model runs, and answers, on a laptop with 32 GB of RAM.
Designed and written by Maurizio "camauri" Cammalleri.
This is an experiment, not a product.
If something goes wrong, Ctrl-C stops a reply and Ctrl-D leaves the chat; --cache <GiB> puts a hard limit on the memory it takes, and JANAS_GPU=0 keeps it off the GPU entirely.
Everything in this repository was written and measured on:
- Linux Debian 13 (trixie), x86-64, kernel 6.12.107; GPU driver Mesa 26.1.6 (Vulkan); built with GCC 14.2
- Intel Core Ultra 9 185H (6 performance cores, 8 efficiency, 2 low-power; AVX2, FMA, F16C, AVX-VNNI; integrated Arc GPU)
- 32 GB of DDR5 RAM
- 1 TB NVMe SSD (about 5.7 GB/s reading)
The Windows build was run on the same laptop under Windows 11 (build 26300), with Intel's own graphics driver: its tests pass there, and how fast it was is under Or on Windows, above.
Everything the engine does is chosen from what it measures, so another machine will make other choices — that part is meant to travel. What has never been tried is the rest: other CPUs (especially without AVX-VNNI, or AMD), discrete GPUs, slower disks, more or less memory. If you run it somewhere else, the report from janas-bench is the single most useful thing you can send back (see Helping it run on more hardware).
What Janas-LLM runs today, model by model and feature by feature: docs/features.md.
On the machine above, with nothing else running, janas-bench reports this (measured on 10 October 2026, with the fast prompt the engine uses by default since that day):
Every figure is the mean of three rounds, not a best round, of the configuration the engine itself chose for each kind of pass - the one a chat runs: a prompt of 256 tokens, then 64 written. Here the integrated GPU reads every prompt (the fast prompt, below), and the threads the engine settled on were the performance cores' 12 for a prompt and for a single token on nearly every model, all the usable cores (performance and efficiency, not the low-power ones) for a few tokens at once. On another machine the engine may settle on other threads: the first passes of each kind try every core, one thread per performance core and the performance cores' threads, keep the fastest, and later try the others now and then, so that a machine that warms up can change the verdict (on an i9-14900HX every thread replied at less than half the speed of the performance cores' 16). The rounds run in alternating order so that the machine warming up and the cache filling weigh on each setting alike. Expect a few per cent either way between runs, and rather less than these on a first run, while the cache is still filling. Without the GPU (JANAS_GPU=0) Qwen3-4B reads the same prompt at 85 tok/s and writes at 27.
The last column is a draft guessing the next tokens and the model checking them, which is the same text at a higher rate — the whole of it is explained under --mtp: the Qwen3.5 and Qwen3.6 models' and Qwen3-Next's own prediction block, Gemma 4's assistant (a small drafting model of its own). It is measured on a chat reply: an ordinary question in English ("explain how bread is made at home"), 64 tokens of the answer, sampled as the chat samples. What the draft is worth depends on the text: there the drafts survived 74-89% of the time on the Qwen models and Gemma's two larger ones, 63-72% on Gemma's E2B and E4B; on Italian prose Qwen3.5-2B kept about a third of them, and gained next to nothing. One round of 64 tokens is noisy here, a tenth either way between runs. Qwen3-30B-A3B has no such block, nor have the dense Qwen3; the dense Qwen3.5 have one in their original checkpoint, which hf2jns_mtp converts (MODELS.md).
This column was wrong until 26 September 2026, and higher: it measured the block continuing a paragraph that repeated itself, which a model copies and the block guesses almost every time - 107 tok/s for Qwen3.5-2B, 26 for Qwen3.5-9B. The MoE figures of the time (29 and 30) happened to be lower than today's; the ChangeLog has the details.
The comparison with llama.cpp at the top of this page was measured so: llama.cpp (build 2b18470 of 18 September 2026) with its Vulkan backend on the same integrated GPU, everything on it (llama-bench -p 1024 -n 16 -ngl 99 -t 12; the largest model otherwise, below), against janas-bench --prompt 1024 --gen 16 on the same files the same days (9-12 October 2026; llama.cpp's best configuration, Janas-LLM's own choice; on 11 October three rounds each, llama-bench -r 3 and janas-bench --rounds 3, for Qwen3-0.6B, Qwen3.5-0.8B, Qwen3.6-35B-A3B and the models from other hands; Qwen3-Coder-Next as Qwen3-Next-80B, below).
On Qwen3-Next-80B-A3B, whose file is larger than this laptop's 30 GB, llama.cpp with its usual build ran out of memory as soon as the GPU took part, even with the experts left on the CPU (-ngl 99 -ncmoe 48): its CPU backend copies the weights into memory of its own to repack them, and the Vulkan backend copies those it leaves to the CPU into buffers the system cannot reclaim. It ran with a build without repacking (GGML_CPU_REPACK=OFF) and two options more, --no-host 1 -lm mmap, which leave the experts in the file, read through the page cache: 16 tok/s reading with the GPU, and 2.8 writing on the CPU alone (with the GPU, 2.0); these are its two figures in the table. Janas-LLM ran the same model with no option of its own, the experts it uses most in a cache of about 19 GB and the rest read from the disk. Janas-LLM's figures are one round each; the writing column is without drafts on both sides. The two tools do not measure in exactly the same way (llama-bench writes without a prompt before it; janas-bench after the 1,024 tokens), and it is one machine. llama.cpp's own CPU backend did worse on this laptop than its Vulkan one at reading (Qwen3-4B 70 tok/s on 20 threads) and as well at writing.
Try it on an idle machine first. The expert cache takes the memory that is free when the model is opened, and what is left of the model is read from disk while it answers, so everything else running takes its share. It degrades gently rather than breaking: measured with a browser and an editor open, the same model kept about three quarters of its speed and waited five times longer on the disk. But the first thing you see should be the machine's real speed, and any measurement you mean to send to others has to be taken with the machine to itself.
- INSTALL.md — what the build needs, how to prepare a model, and the first run
- ChangeLog.md — what changed, newest first
- MODELS.md — what a converted model's licence is, and what may be redistributed
- CONTRIBUTING.md — how to help, and the sign-off
- src/services — Janas's services, each with its page, in janas-chat and in other MCP clients
- docs/features.md — what Janas-LLM runs today, model by model and feature by feature
- docs/models.md — getting a model: janas-get, or a GGUF file converted
- docs/chat.md — using janas-chat, its services and tools from MCP servers
- docs/library.md — using it from a program, in C or FreeBASIC
- docs/serving.md — the model served to MCP clients (janas-mcp) and over HTTP (janas-server)
- docs/code-completion.md — code completion in VSCodium and VS Code, through janas-server
- docs/tools.md — the converters, checkers and benchmarks
- docs/hardware.md — measuring your machine, and helping it run on more hardware
- AUTHORS — who wrote it, and what it owes to others
- LICENSE — GNU GPL, version 3 or later
sudo apt install build-essential          # Debian/Ubuntu
sudo apt install libvulkan-dev glslang-tools vulkan-tools   # optional, GPU (glslang 15.2 or later: INSTALL.md)
sudo pacman -S vulkan-headers glslang vulkan-tools           # the same, Arch
./build.sh                                # everything into bin/x86_64-linux/
./build.sh release test                   # and run the tests
Downloading a model already converted with janas-get, or converting a GGUF file yourself, and which files were checked: docs/models.md.
janas-chat: its options and commands, the drafts, Janas's services, tools from MCP servers, a long prompt watched as it is read: docs/chat.md.
janas-server fills in code at an editor's cursor, with a model for code such as Qwen3-Coder-30B-A3B: OpenAI's /v1/completions with a suffix, and llama.cpp's /infill, which llama.vscode asks. The window sent at every keystroke is kept from moving, so that a keystroke reads only what it changed: 1.5-2.2 s a proposal on a laptop, where a window slid a line was read again in 17 s. How to set it up in VSCodium and VS Code, with llama.vscode or Continue, and what was measured: docs/code-completion.md.
The library from C and from FreeBASIC and BASIC MODERN, and MCP servers from a program: docs/library.md.
janas-mcp: the model as tools for Claude Code, editors and other MCP clients: docs/serving.md.
janas-server: an HTTP API that follows OpenAI's, and a chat page to try it from a browser: docs/serving.md.
janas-bench: what it measures, and the report it leaves: docs/hardware.md.
The converters, checkers and benchmarks built beside the programs: docs/tools.md.
Which machines are wanted most, the one command that tries Janas and writes a report, and what to send: docs/hardware.md.
Janas is designed and written by Maurizio "camauri" Cammalleri (LinkedIn, Substack).
It stands on the work of others, and says so:
- The models it runs are their authors': Qwen3, Qwen3.5, Qwen3.6 and Qwen3-Next by the Qwen team of Alibaba Cloud, Gemma 4 by Google; the GGUF quantizations by Qwen, bartowski and unsloth (MODELS.md has every source).
- llama.cpp and ggml are the reference the engine is checked against (logits, tokens, speed); none of their code is in Janas. The one thing taken from ggml is data that defines a format: the IQ3_S grid, in src/llm/iq3s_grid.h, under ggml's MIT licence.
- The Unicode Character Database gives the tokenizer its tables (tools/gen_unicode), and OpenAI's OpenAPI specification gives janas-server its route table (tools/openapi_routes).
- GNU libmicrohttpd, yyjson and Mbed TLS are compiled into the programs named below.
- janas-flights reads the positions of aircraft from adsb.lol (data under the Open Database License) and adsb.fi, routes from adsbdb.com and, with a key of the user's, schedules from AviationStack; its tables of places are built from OurAirports (public domain), GeoNames (CC BY 4.0) and Natural Earth (public domain).
- janas-quakes reads the earthquakes from INGV (Istituto Nazionale di Geofisica e Vulcanologia, CC BY 4.0) for Italy and its seas and from the USGS (public domain) elsewhere, and places from Nominatim (© OpenStreetMap contributors, ODbL).
- janas-weather reads forecasts and the sea from Open-Meteo (CC BY 4.0) and MET Norway (CC BY 4.0), the stations' reports from aviationweather.gov (NOAA), warnings from MeteoAlarm (EUMETNET) and the Italian alert levels from the Dipartimento della Protezione Civile (CC BY 4.0). With no place named, the services ask GeoJS or ipwho.is where the internet connection is.
- janas-maps reads OpenStreetMap's data (© OpenStreetMap contributors, ODbL) through Nominatim, Photon, Valhalla and OSRM on the servers of FOSSGIS, and the Overpass API (with Private.coffee's instance when it is busy), and journeys by public transport from Transitous, over the operators' open timetables.
- janas-prices reads the European Central Bank (through Frankfurter), CoinGecko (data provided by CoinGecko) and Coinbase, Alpha Vantage with the user's key, Eurostat and the World Bank (CC BY 4.0), the New York Fed, the Bank of England and the Swiss National Bank, energy-charts.info (Fraunhofer ISE; the zones under CC BY 4.0, from the Bundesnetzagentur's SMARD), and the fuel prices of Italy's MIMIT (IODL 2.0), France's prix-carburants, Spain's ministry and Austria's E-Control; places through Nominatim.
- janas-github reads GitHub's REST API; janas-git runs git.
- janas-wiki reads Wikipedia through its API; the text is Wikipedia's, under CC BY-SA 4.0, and every answer gives the page's address.
- The people who tried it on their own machines and reported what they saw, in the issues of this repository: their reports changed the engine more than once (the threads it picks, the prompt's progress, the GPU's diagnosis).
Copyright © 2026 Maurizio "camauri" Cammalleri.
Janas is free software under the GNU General Public License, version 3 or later — see LICENSE. Every source file carries its SPDX line.
janas-server, and only it, has two libraries of others compiled in, their sources unchanged in src/third_party/ with their licences and where they came from: GNU libmicrohttpd 1.0.10 (LGPL 2.1 or later, or the eCos licence without HTTPS, as it is built here) and yyjson 0.13.0 (MIT). libjanas_mcp, and the programs with it, have Mbed TLS 4.2.0 with TF-PSA-Crypto (Apache-2.0 or GPL-2.0-or-later), for https:// MCP servers. libjanas_llm has none.
The models are not covered by it. A converted .jns file is a derivative of the model, not of Janas, and keeps the licence its authors gave it; MODELS.md says what this project will and will not redistribute, and what to check before you pass a converted model on.
CONTRIBUTING.md. The short version: a measurement from a machine nobody here owns is worth more than most patches, and every commit needs a Signed-off-by line (git commit -s).
