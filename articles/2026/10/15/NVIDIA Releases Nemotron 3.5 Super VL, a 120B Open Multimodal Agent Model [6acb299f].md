---
id: "6acb299f817b2696"
title: "NVIDIA Releases Nemotron 3.5 Super VL, a 120B Open Multimodal Agent Model"
url: "https://marktechpost.com/2026/10/15/nvidia-nemotron-3-5-super-vl-release"
link: "https://marktechpost.com/2026/10/15/nvidia-nemotron-3-5-super-vl-release"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T19:53:50Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "NVIDIA just released Nemotron 3.5 Super VL , an open vision-language model built for always-on enterprise agents. Nemotron 3.5 Super VL is a 120B-parameter mixture-of-experts model from NVIDIA that activates 12B parameters per token. It reads text, images, documents and video, then reasons, calls tools and writes code in one model. For developers, 1 open checkpoint replaces a separate text model…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "New Releases", "Open Source"]
orgs: ["Nvidia", "Hugging Face"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "summary"
word_count: 1604
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA Releases Nemotron 3.5 Super VL, a 120B Open Multimodal Agent Model

MarkTechPost · Asif Razzaq · 2026-10-15

NVIDIA just released Nemotron 3.5 Super VL , an open vision-language model built for always-on enterprise agents. Nemotron 3.5 Super VL is a 120B-parameter mixture-of-experts model from NVIDIA that activates 12B parameters per token. It reads text, images, documents and video, then reasons, calls tools and writes code in one model. For developers, 1 open checkpoint replaces a separate text model along with a separate vision model. NVIDIA also shipped 2 edge models, Nemotron 3.5 Bolt 74B-A9B and Bolt E4B. 

 TL;DR 

 Size: 120B total parameters, 12B active (MoE). Context up to 1M tokens. 

 Runs on: 1x DGX Spark, 1x H200, 2x H100 or 1x GB200 with the NVFP4 checkpoint. A BF16 checkpoint is also published. 

 Performance: Strong reasoning, agentic coding and document vision. NVIDIA claims up to 5x higher single-GPU throughput than open peers. 

 Best: 89.90 on GPQA-Diamond (NVFP4). 

 Worst: 17.78 on tau3-bench banking (NVFP4). 

 What is Nemotron 3.5 Super VL? 

 It is an open multimodal agent model. Weights ship under the OpenMDW-1.1 license . NVIDIA also released open datasets , training recipes and RL environments in NeMo Gym. 

 The model card lists text, image and video inputs with text output. Video is limited to MP4 clips up to 2 minutes. Reasoning can be toggled on or off through the chat template. 

 How does the architecture work? 

 The backbone interleaves Mamba-2, mixture-of-experts and attention layers. Each MoE layer holds 512 routed experts. A C-RADIO vision encoder and a connector feed images, document pages and video frames into the language backbone. 

 Speed comes from four techniques: 

 Multi-token prediction: a native drafter proposes several tokens, verified in 1 forward pass. 

 LiLiCorr: a speculative drafter for DGX Spark, up to 2.3x faster token generation. 

 NVFP4 with quantization-aware distillation: 4-bit weights and activations on Blackwell, 4-bit weights with 16-bit activations elsewhere. 

 Context reuse: prefix caching keeps both attention caches and Mamba states across agent turns. 

 The model was distilled from Nemotron 3 Ultra. NVIDIA team states that it trained on about 26 trillion tokens. Post-training used roughly 3.8 million samples plus RL across dozens of environments. Continued pretraining added 10B Indic tokens. 

 How does it perform on benchmarks? 

 All scores below are NVIDIA-reported, from the NVFP4 checkpoint on the model card. 

 Area Benchmark Score Reasoning GPQA-Diamond 89.90 Coding SWE-bench Verified 71.07 Coding Terminal-Bench 2.1 60.80 Web agent BrowseComp 77.5 Instruction following IFBench 71.50 Charts CharXiv reasoning 79.88 Documents MMLongBench-Doc 62.82 Computer use OSWorld-Verified 52.3 Long-horizon agent tau3-bench banking 17.78 

 On agent harness evals, Super VL beats Nemotron 3 Ultra. It scores 63.44% on Hermes Bench versus 56.33%. On LangChain evals it scores 87.05% versus 84.3%. Ultra carries about 4.6x more total parameters. 

 NVIDIA team reports over 600 output tokens per second on Artificial Analysis agentic tasks via a Baseten endpoint. Its chart marks a 5x speed gap over Inkling Small. 

 </div>
 <div class="stage" data-i="1">C-RADIO<small>vision encoder</small></div><div class="arr"> </div>
 <div class="stage" data-i="2">Hybrid MoE<small>Mamba-2 + attention</small></div><div class="arr"> </div>
 <div class="stage" data-i="3">MTP decode<small>+ LiLiCorr</small></div><div class="arr"> </div>
 <div class="stage" data-i="4">Output<small>text, tool calls</small></div>
 </div>
 <div class="detail" id="mtp-detail"></div>
 <div class="ctrl">
 <button class="btn" id="mtp-prev"> Back</button>
 <button class="btn pri" id="mtp-next">Next </button>
 <button class="btn" id="mtp-play"> Auto-play</button>
 <span class="step" id="mtp-step">Step 1 of 5</span>
 </div>
 </div>

 <div class="panel" id="p-bm">
 <div class="seg"><button class="on" data-c="nv">NVFP4</button><button data-c="bf">BF16</button></div>
 <div id="mtp-bars"></div>
 <p class="note">NVIDIA-reported scores from the model card. Orange bar marks the weakest result.</p>
 </div>

 <div class="panel" id="p-cp">
 <div class="cmp" id="mtp-cmp"></div>
 <p class="legend">Vendor self-reported scores. Super VL uses NVFP4. Harnesses differ: Inkling-Small SWE-bench uses a bash-only harness.</p>
 </div>

 <div class="panel" id="p-dp">
 <div class="hw" id="mtp-hw">
 <button class="chip on" data-h="0">1x DGX Spark<small>vLLM · LiLiCorr</small></button>
 <button class="chip" data-h="1">1x H200<small>vLLM · MTP 3</small></button>
 <button class="chip" data-h="2">2x H100<small>vLLM · MTP 3</small></button>
 <button class="chip" data-h="3">1x GB200<small>vLLM · MTP 5</small></button>
 </div>
 <div class="detail" id="mtp-hwd"></div>
 <pre id="mtp-code"></pre>
 <p class="note">Commands abridged from the Hugging Face model card. Use the full flag set there for production.</p>
 </div>

 <div class="ft"><span>Sources: NVIDIA blog, NVIDIA technical blog, Hugging Face model cards</span><span class="br">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-nsvl');
function $(s){return R.querySelector(s)}
function $$(s){return Array.prototype.slice.call(R.querySelectorAll(s))}
function resize(){try{parent.postMessage({mtpEmbed:'nsvl',h:R.offsetHeight+40},'*')}catch(e){}}
/* tabs */
$$('.tab').forEach(function(t){t.addEventListener('click',function(){
 $$('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');
 $$('.panel').forEach(function(p){p.classList.remove('on')});
 var k=t.getAttribute('data-t');$('#p-'+k).classList.add('on');
 if(k==='bm')drawBars(cur);if(k==='cp')drawCmp();if(k==='ov')count();
 setTimeout(resize,60);
})});
/* counters */
function count(){$$('.stat b').forEach(function(b){var n=+b.getAttribute('data-n'),s=b.getAttribute('data-s')||'',t0=null;
 function f(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/900,1),e=1-Math.pow(1-p,3);b.textContent=Math.round(n*e)+s;if(p<1)requestAnimationFrame(f)}requestAnimationFrame(f)})}
count();
/* MoE cells */
var cells=$('#mtp-cells'),N=120;for(var i=0;i<N;i++){var c=document.createElement('div');c.className='cell';cells.appendChild(c)}
var cs=$$('.cell'),tk=1;
function route(){cs.forEach(function(c){c.classList.remove('act')});var used={};for(var k=0;k<12;k++){var j;do{j=Math.floor(Math.random()*N)}while(used[j]);used[j]=1;cs[j].classList.add('act')}$('#mtp-tok').textContent='token #'+(tk++)+' · 12 of 120 cells active'}
route();setInterval(route,1100);
/* pipeline */
var D=[
 '<b>Inputs.</b> Text, RGB images (jpeg, png) and MP4 video up to 2 minutes. Documents can be passed as page images with text. Everything shares a context window of up to 1M tokens.',
 '<b>C-RADIO vision encoder + connector.</b> Turns images, document pages and video frames into representations the language backbone can process. These parts stay in BF16 after quantization.',
 '<b>Hybrid MoE backbone.</b> Interleaved Mamba-2, MoE and attention layers. 512 routed experts per MoE layer, 12B of 120B parameters active per token. Distilled from Nemotron 3 Ultra.',
 '<b>Fast decoding.</b> Native multi-token prediction drafts several tokens for 1-pass verification. On DGX Spark, the LiLiCorr drafter gives up to 2.3x faster token generation.',
 '<b>Output.</b> Text answers, reasoning (toggle with enable_thinking) and tool calls. NVIDIA reports 600+ output tokens per second on Artificial Analysis agentic tasks via Baseten.'];
var si=0,timer=null,st=$$('.stage');
function show(i){si=(i+5)%5;st.forEach(function(s,k){s.classList.toggle('on',k===si)});$('#mtp-detail').innerHTML=D[si];$('#mtp-step').textContent='Step '+(si+1)+' of 5';setTimeout(resize,30)}
st.forEach(function(s){s.addEventListener('click',function(){show(+s.getAttribute('data-i'))})});
$('#mtp-next').addEventListener('click',function(){show(si+1)});
$('#mtp-prev').addEventListener('click',function(){show(si-1)});
$('#mtp-play').addEventListener('click',function(){var b=this;if(timer){clearInterval(timer);timer=null;b.textContent=' Auto-play'}else{timer=setInterval(function(){show(si+1)},2200);b.textContent='❚❚ Pause'}});
show(0);
/* benchmarks */
var B=[['GPQA-Diamond',89.90,89.52],['CharXiv reasoning',79.88,80.82],['BrowseComp',77.5,78],['SWE-bench Verified',71.07,71.10],['IFBench',71.50,70.86],['MMLongBench-Doc',62.82,62.82],['Terminal-Bench 2.1',60.80,66.70],['OSWorld-Verified',52.3,51.14],['tau3-bench banking',17.78,18.88]];
var cur='nv';
function drawBars(c){cur=c;var h='';B.forEach(function(r,i){var v=c==='nv'?r[1]:r[2];h+='<div class="bar"><span class="nm">'+r[0]+'</span><div class="track"><div class="fill'+(i===B.length-1?' low':'')+'" data-w="'+v+'"></div></div><span class="val">'+v.toFixed(2)+'</span></div>'});
 $('#mtp-bars').innerHTML=h;requestAnimationFrame(function(){requestAnimationFrame(function(){$$('#mtp-bars .fill').forEach(function(f){f.style.width=f.getAttribute('data-w')+'%'})})});setTimeout(resize,60)}
$$('.seg button').forEach(function(b){b.addEventListener('click',function(){$$('.seg button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');drawBars(b.getAttribute('data-c'))})});
/* compare */
var C=[['GPQA Diamond','89.90','86.6','89.5'],['SWE-bench Verified','71.07','72.0','80.2'],['IFBench','71.50','76.1','82.2'],['CharXiv reasoning','79.88','77.2','77.4'],['BrowseComp','77.5','63.8','77.4']];
function drawCmp(){var h='';C.forEach(function(r){h+='<div class="row"><div class="rt">'+r[0]+'</div>'+
 '<div class="b me"><span class="nm">Super VL</span><div class="track"><div class="fill" data-w="'+r[1]+'"></div></div><span class="val">'+r[1]+'</span></div>'+
 '<div class="b"><span class="nm">Qwen3.5-122B-A10B</span><div class="track"><div class="fill q" data-w="'+r[2]+'"></div></div><span class="val">'+r[2]+'</span></div>'+
 '<div class="b"><span class="nm">Inkling-Small</span><div class="track"><div class="fill i" data-w="'+r[3]+'"></div></div><span class="val">'+r[3]+'</span></div></div>'});
 $('#mtp-cmp').innerHTML=h;requestAnimationFrame(function(){requestAnimationFrame(function(){$$('#mtp-cmp .fill').forEach(function(f){f.style.width=f.getAttribute('data-w')+'%'})})});setTimeout(resize,60)}
/* deploy */
var H=[
 ['<b>1x DGX Spark (GB10).</b> Text and image, 1M-token context in vLLM. NVIDIA recommends the LiLiCorr drafter for all Spark deployments.','vllm serve nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 \\\n --max-num-seqs 1 --trust-remote-code \\\n --speculative_config.model nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4-LiLiCorr \\\n --speculative_config.num_speculative_tokens 7 \\\n --speculative_config.method dflash \\\n --reasoning-parser nemotron_v3'],
 ['<b>1x H200.</b> Text, image and video, 1M-token context, MTP with 3 draft tokens. Same command as 2x H100 with tensor parallel 1.','vllm serve nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 \\\n --tensor-parallel-size 1 --trust-remote-code \\\n --speculative-config.method mtp \\\n --speculative-config.num_speculative_tokens 3 \\\n --reasoning-parser nemotron_v3'],
 ['<b>2x H100.</b> Text, image and video, 1M-token context, MTP with 3 draft tokens. Runs W4A16 on non-Blackwell GPUs.','vllm serve nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 \\\n --tensor-parallel-size 2 --trust-remote-code \\\n --speculative-config.method mtp \\\n --speculative-config.num_speculative_tokens 3 \\\n --reasoning-parser nemotron_v3'],
 ['<b>1x GB200.</b> Text, image and video, 1M-token context, MTP with 5 draft tokens. Full W4A4 NVFP4 on Blackwell. SGLang and TensorRT-LLM recipes also exist.','vllm serve nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 \\\n --max-num-seqs 512 --trust-remote-code \\\n --speculative_config.method mtp \\\n --speculative_config.num_speculative_tokens 5 \\\n --reasoning-parser nemotron_v3']];
function hw(i){$$('.chip').forEach(function(c,k){c.classList.toggle('on',k===i)});$('#mtp-hwd').innerHTML=H[i][0];$('#mtp-code').textContent=H[i][1];setTimeout(resize,30)}
$$('.chip').forEach(function(c){c.addEventListener('click',function(){hw(+c.getAttribute('data-h'))})});hw(0);
window.addEventListener('load',resize);window.addEventListener('resize',resize);setTimeout(resize,300);
})();
</script>
</body>
</html>
"> 

(function(){var f=document.getElementById('mtp-nsvl-frame');
window.addEventListener('message',function(e){var d=e.data;if(d&&d.mtpEmbed==='nsvl'&&f&&e.source===f.contentWindow&&d.h>200){f.style.height=d.h+'px';}});})();

 How does it compare with similar open models? 

 Feature Nemotron 3.5 Super VL Qwen3.5-122B-A10B Inkling-Small Nemotron 3 Ultra Developer NVIDIA Alibaba Qwen Thinking Machines Lab NVIDIA Total / active params 120B / 12B 122B / 10B 276B / 12B 550B / 55B Context Up to 1M 262,144 native, extensible to 1,010,000 Not disclosed on model card Evaluated at 1M (Ruler @1M) Inputs Text, image, video Text, image, video Text, image, audio Not disclosed License OpenMDW-1.1 Apache 2.0 Apache 2.0 OpenMDW-1.1 Reference hardware 1x DGX Spark, 1x H200, 2x H100 or 1x GB200 8-GPU tensor-parallel serving example Not disclosed Not disclosed GPQA Diamond 89.90 86.6 89.5 Not disclosed SWE-bench Verified 71.07 72.0 80.2 (bash-only harness) 65 to 70.4 (across 5 harnesses) IFBench 71.50 76.1 82.2 82 CharXiv reasoning 79.88 77.2 77.4 Not disclosed BrowseComp 77.5 63.8 77.4 (with context management) Not disclosed Terminal-Bench 60.80 (v2.1) 49.4 (v2) 64.7 (v2.1, best harness) 54 (v2.0) 

 Scores are self-reported by each vendor. Harnesses and benchmark versions differ, so treat gaps of a few points with caution. 

 How can developers deploy it? 

 Super VL is available on Hugging Face , OpenRouter , ModelScope and as an NVIDIA NIM . Supported runtimes are vLLM, SGLang and TensorRT-LLM on Blackwell and Hopper. Local paths include llama.cpp and Unsloth . 

 For production, Dynamo recipes add KV-aware routing. On 16 B200 GPUs at 50 tokens per second per user, NVIDIA reports 8x more users served. First-token latency drops 85%. 

 Customization runs through NeMo AutoModel for SFT and LoRA, and NeMo RL for reinforcement learning. NVIDIA cites early results: 

 Scale AI for Skydance vendor credit processing: 40x lower inference cost and 5x lower latency. 

 Ramp receipt-to-JSON extraction: up to 50% higher throughput and 10x lower latency expected. 

 AI21 for Alice threat intelligence: 40% higher accuracy. 

 What are the Nemotron 3.5 Bolt models? 

 Nemotron 3.5 Bolt 74B-A9B targets local agents. NVIDIA’s launch notes describe it as distilled from Super VL. Native 2-bit quantization fits it into 24GB of memory on RTX and DGX Spark systems. NVIDIA says it ranks #1 among open models in its class on PinchBench . It ranks #2 on BrowseComp among open models. It is available now on Hugging Face with llama.cpp, Ollama, LM Studio, Unsloth and vLLM support. 

 Bolt E4B 4GB arrives October 23. It targets voice assistants and embedded agents on GeForce RTX, Jetson and RTX or DGX Spark. 

 Key Takeaways 

 120B MoE, 12B active, 1M context, open weights under OpenMDW-1.1. 

 1 model handles text, images, documents, video, tools and code. 

 NVFP4 checkpoint runs on a single DGX Spark, H200 or GB200. 

 89.90 GPQA-Diamond, but only 17.78 on tau3-bench banking. 

 Bolt 74B-A9B brings a 24GB local agent model to RTX PCs. 

 Check out the technical report , model card and usage cookbook . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post NVIDIA Releases Nemotron 3.5 Super VL, a 120B Open Multimodal Agent Model appeared first on MarkTechPost .
