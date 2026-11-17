---
id: "9a0bd4ab91048623"
title: "Sarvam Launches Sarvam Token Factory: Bringing India-Hosted Inference to 8 Open Models"
url: "https://marktechpost.com/2026/11/17/sarvam-token-factory-india-inference-platform"
link: "https://marktechpost.com/2026/11/17/sarvam-token-factory-india-inference-platform"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T09:51:18Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Sarvam has opened Sarvam Token Factory to everyone. Sarvam Token Factory is an inference platform from Sarvam that serves its own models and open-weight models from GPU clusters in India. Developers reach every model through one OpenAI-compatible API . For India-based teams, this means low-latency tokens without sending traffic to overseas clouds. You can check the deployment options and specs…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Staff", "Tech News", "Technology"]
orgs: ["DeepSeek", "OpenAI", "Nvidia", "Alibaba"]
topics: ["chips & infrastructure", "products & launches", "models & research", "agents & coding"]
content_source: "summary"
word_count: 1337
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Sarvam Launches Sarvam Token Factory: Bringing India-Hosted Inference to 8 Open Models

MarkTechPost · Asif Razzaq · 2026-11-17

Sarvam has opened Sarvam Token Factory to everyone. Sarvam Token Factory is an inference platform from Sarvam that serves its own models and open-weight models from GPU clusters in India. Developers reach every model through one OpenAI-compatible API . For India-based teams, this means low-latency tokens without sending traffic to overseas clouds. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Size: 8 models listed at launch, including Sarvam 105B (105B total, 9B active, 128K context), GLM 5.3, DeepSeek V4.1 Flash 1017, Kimi K3.1 Pro and Gemma 4 31B. 

 Runs on: NVIDIA B200 clusters in India. Sarvam 105B now fits on 1 B200 per replica. On-premise deployment is offered to enterprises. 

 Performance: Fastest first token from Mumbai on most tested cases, per Sarvam’s own measurements. 

 Best: Kimi K3.1 Pro at 6,177 tokens/s per GPU vs 3,213 for InferenceX, at 70 tokens/s per user (1.9x). 

 What is Sarvam Token Factory? 

 It is a managed inference stack, not a single model. Sarvam first previewed it as Sarvam Inference at its Epoch event. The launch post lists 8 models: Sarvam 105B, GLM 5.3, GLM 5.3 Flash, DeepSeek V4.1 Flash 1017, DeepSeek V4 Pro, Kimi K3, Kimi K3.1 Pro and Gemma 4 31B. 

 The docs split them into 2 groups. Pay-as-you-go models run on shared endpoints. DeepSeek V4 Pro, Kimi K3.1 Pro, Qwen 3.8 27B, Clef and EmbeddingGemma 2 need Provisioned Throughput, enabled per organisation. 

 How does it work? 

 The stack has 3 layers around a shared cache: 

 Control plane: a cache-aware router, admission control and a planner. 

 Inference engine: separate GPU pools for prefill and decode. 

 Cache: GPU memory plus a shared G3 store built on Mooncake. 

 It builds on vLLM, SGLang, Dynamo, Mooncake, NIXL, DeepEP, DeepGEMM and FlashInfer. An orchestrator agent proposes experiments, and an engineer approves each deployment. 

 Caching drives most of the gains. DeepSeek V4.1 Flash serves 450B+ tokens per day, with 95.7% of prompt tokens served from cache. On GLM 5.3, the planner cut prefill GPU-hours from 32.3 to 17.1 under the same replayed load. 

 For Sarvam 105B, MXFP8 weights plus speculative decoding raised output throughput about 2.2x. That cut each replica from 2 B200s to 1. Sarvam says none of these changes reduced accuracy. 

 How fast is it? Benchmarks 

 All numbers below come from Sarvam’s launch post . They are self-reported. 

 Sarvam 105B: 0.2 s first token and 330 tokens/s for a single user. 

 Gemma 4 31B (10K prompt, Mumbai): 0.40 s first token and 308 tokens/s, vs 2.00 s and 193 tokens/s at the only other provider. 

 Kimi K3.1 Pro (16 B200s): 6,177 vs 3,213 tokens/s per GPU against InferenceX at 70 tokens/s per user. 

 Heavy agent load (72 sessions): median first token 0.8 s vs 11.6 s for InferenceX. 

 GLM 5.3 Flash (64 sessions): p99 first token 3.2 s vs 14.1 s for stock vLLM and Dynamo. 

 The results are not a clean sweep. On DeepSeek V4.1 Flash with a 10K prompt, Together posts 0.71 s first token vs Sarvam’s 0.90 s. Together also streams faster, at 278 tokens/s vs 130 on Sarvam Standard. 

 Auto-play</button></div>
 </div>

 <div class="pn" data-p="1">
 <div class="hl" id="stf-th">Time to first token from Mumbai (lower is better)</div>
 <div class="ctl" style="margin:0 0 8px"><button class="btn on" data-k="d1">DeepSeek, 1K</button><button class="btn" data-k="d10">DeepSeek, 10K</button><button class="btn" data-k="g1">GLM 5.3, 1K</button><button class="btn" data-k="g10">GLM 5.3, 10K</button></div>
 <div id="stf-ttft"></div>
 <div class="note">Seconds. Source: Sarvam technical blog, measured by Sarvam from Mumbai. Not independently verified.</div>
 </div>

 <div class="pn" data-p="2">
 <div class="cards">
 <div class="cd"><div class="k">1.9x</div><div class="t">Kimi K3.1 Pro tokens/s per GPU</div><div class="r">6,177 vs 3,213 for InferenceX at 70 tok/s per user, 16 B200s.</div></div>
 <div class="cd"><div class="k">0.8 s</div><div class="t">Median first token, 72 agent sessions</div><div class="r">vs 11.6 s for InferenceX. p95 3.1 s vs 76.6 s.</div></div>
 <div class="cd"><div class="k">95.7%</div><div class="t">DeepSeek prompt tokens from cache</div><div class="r">On 450B+ tokens served per day.</div></div>
 </div>
 <div class="hl">Output speed, DeepSeek V4.1 Flash (tokens/s, higher is better)</div>
 <div id="stf-tp"></div>
 <div class="note">Click a card to reveal detail. Source: Sarvam technical blog (self-reported).</div>
 </div>

 <div class="pn" data-p="3">
 <div class="calc">
 <div><label>Input tokens per month: <span id="stf-iv"></span>M</label><input type="range" id="stf-in" min="1" max="1000" value="100"></div>
 <div><label>Output tokens per month: <span id="stf-ov"></span>M</label><input type="range" id="stf-out" min="1" max="500" value="20"></div>
 </div>
 <table><thead><tr><th>Model</th><th>₹ per 1M in / out</th><th>Your monthly cost</th></tr></thead><tbody id="stf-pt"></tbody></table>
 <div class="note">Prices from Sarvam docs. Sarvam 105B and DeepSeek rates are introductory through the end of 2026. Excludes cache discounts.</div>
 </div>

 <div class="pn" data-p="4">
 <ul class="lim">
 <li>Every speed and throughput number is Sarvam-measured.</li>
 <li>Together beats Sarvam on DeepSeek V4.1 Flash: 0.71 s vs 0.90 s first token at 10K, and 278 vs 130 tok/s streaming.</li>
 <li>Uptime, SLA, rate limits and context windows are not on the launch post or docs page.</li>
 <li>Kimi K3.1 Pro and DeepSeek V4 Pro need Provisioned Throughput with unpublished rates.</li>
 </ul>
 </div>

 <div class="ft"><span>Sources: sarvam.ai/blogs/sarvam-token-factory · docs.sarvam.ai</span><b>© Marktechpost</b></div>
</div>
<script>
(function(){
var R=document.getElementById('stf-x');
function post(){try{parent.postMessage({stfHeight:R.offsetHeight+40},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(t){t.onclick=function(){R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');R.querySelectorAll('.pn').forEach(function(p){p.classList.toggle('on',p.dataset.p==t.dataset.t)});if(t.dataset.t=='1')ttft(cur);if(t.dataset.t=='2')tp();setTimeout(post,60)}});
var steps=['A developer calls Chat Completions with the OpenAI SDK. Only the base_url and API key change.','The cache-aware router sends the request to the worker most likely to hold its prefix. Misrouted requests fell from 17.6% to 3.5%.','Prefill and decode run on separate GPU pools. On GLM 5.3 the planner cut prefill GPU-hours from 32.3 to 17.1.','Prompt tokens are served from GPU memory or the G3 store when possible. DeepSeek V4.1 Flash hits cache on 95.7% of prompt tokens.'];
var si=0,timer=null,nodes=R.querySelectorAll('.node');
function show(i){si=(i+4)%4;nodes.forEach(function(n){n.classList.toggle('act',n.dataset.s==si)});document.getElementById('stf-d').textContent=steps[si]}
nodes.forEach(function(n){n.onclick=function(){show(+n.dataset.s)}});
document.getElementById('stf-prev').onclick=function(){show(si-1)};
document.getElementById('stf-next').onclick=function(){show(si+1)};
document.getElementById('stf-play').onclick=function(){var b=this;if(timer){clearInterval(timer);timer=null;b.textContent=' Auto-play'}else{timer=setInterval(function(){show(si+1)},2200);b.textContent='❚❚ Pause'}};
show(0);
var D={d1:[['Sarvam',.51],['Together',.61],['Fireworks',1.01],['DeepInfra',1.08]],d10:[['Sarvam',.90],['Together',.71],['Fireworks',1.55],['DeepInfra',1.75]],g1:[['Sarvam',.68],['Together',.82],['Fireworks',.84],['DeepInfra',2.17]],g10:[['Sarvam',1.19],['Together',1.19],['Fireworks',1.57],['DeepInfra',2.18]]};
var cur='d1';
function bars(el,rows,max,unit){el.innerHTML=rows.map(function(r){return '<div class="row"><div class="lb">'+r[0]+'</div><div class="bar"><i class="'+(r[0].indexOf('Sarvam')==0?'s':'')+'" data-w="'+(r[1]/max*100)+'"></i></div><div class="v">'+r[1]+unit+'</div></div>'}).join('');requestAnimationFrame(function(){setTimeout(function(){el.querySelectorAll('i').forEach(function(i){i.style.width=i.dataset.w+'%'})},30)})}
var TN={d1:'DeepSeek V4.1 Flash, 1K prompt',d10:'DeepSeek V4.1 Flash, 10K prompt',g1:'GLM 5.3, 1K prompt',g10:'GLM 5.3, 10K prompt'};function ttft(k){cur=k;document.getElementById('stf-th').textContent='Time to first token from Mumbai, '+TN[k]+' (lower is better)';bars(document.getElementById('stf-ttft'),D[k],2.3,' s')}
R.querySelectorAll('[data-k]').forEach(function(b){b.onclick=function(){R.querySelectorAll('[data-k]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');ttft(b.dataset.k)}});
function tp(){bars(document.getElementById('stf-tp'),[['Sarvam Interactive',200],['Sarvam Standard',130],['Together',278],['Fireworks',193],['Baseten',165],['DeepSeek API',60]],290,'')}
R.querySelectorAll('.cd').forEach(function(c){c.onclick=function(){c.classList.toggle('op');setTimeout(post,350)}});
var P=[['Sarvam 105B',10,25],['DeepSeek V4.1 Flash 1017',14,55],['GLM 5.3 Flash',13.5,45],['Gemma 4 31B',35,90],['GLM 5.3',126,390]];
function price(){var a=+document.getElementById('stf-in').value,b=+document.getElementById('stf-out').value;document.getElementById('stf-iv').textContent=a;document.getElementById('stf-ov').textContent=b;
document.getElementById('stf-pt').innerHTML=P.map(function(p){return '<tr><td>'+p[0]+'</td><td>₹'+p[1]+' / ₹'+p[2]+'</td><td class="c">₹'+Math.round(a*p[1]+b*p[2]).toLocaleString('en-IN')+'</td></tr>'}).join('')}
document.getElementById('stf-in').oninput=price;document.getElementById('stf-out').oninput=price;price();
ttft('d1');
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body></html>
"> 

window.addEventListener('message',function(e){if(e.data&&e.data.stfHeight){var f=document.getElementById('stf-frame');if(f&&e.source===f.contentWindow){f.style.height=e.data.stfHeight+'px';}}});

 How much does it cost? 

 Prices are in Indian rupees per 1M tokens, per the docs : 

 Model Input / Output (₹ per 1M) Sarvam 105B ₹10 / ₹25 (introductory) GLM 5.3 ₹126 / ₹390 GLM 5.3 Flash ₹13.5 / ₹45 Gemma 4 31B ₹35 / ₹90 DeepSeek V4.1 Flash 1017 ₹14 / ₹55 (introductory) 

 Introductory pricing runs through the end of 2026. A faster DeepSeek Interactive endpoint costs ₹25 input and ₹105 output. Provisioned model rates are not published on the docs page. 

 How does it compare with other inference providers? 

 Metrics Sarvam Token Factory Together AI Fireworks AI DeepInfra Serving location GPU clusters in India Not disclosed Not disclosed Not disclosed OpenAI-compatible API Yes Yes Yes Yes First-party LLM Sarvam 105B Not disclosed Not disclosed Not disclosed On-premise option Yes Not disclosed Not disclosed Not disclosed DeepSeek V4.1 Flash 1017 price (per 1M in / out) ₹14 / ₹55 $0.30 / $1.20 $0.30 / $1.20 $0.20 / $0.60 (list); $0.14 / $0.42 (promo) Cached input (per 1M) Not disclosed $0.006 $0.006 $0.006 TTFT from Mumbai, 1K prompt (Sarvam-measured) 0.51 s 0.61 s 1.01 s 1.08 s TTFT from Mumbai, 10K prompt (Sarvam-measured) 0.90 s 0.71 s 1.55 s 1.75 s Output speed (Sarvam-measured) 130 tok/s (Standard), 200 (Interactive) 278 tok/s 193 tok/s Not disclosed 

 Key Takeaways 

 Sarvam Token Factory serves Sarvam and open-weight models from India via one OpenAI-compatible API. 

 Sarvam 105B starts at ₹10 input and ₹25 output per 1M tokens. 

 Sarvam reports 1.9x per-GPU throughput over InferenceX on Kimi K3.1 Pro. 

 Together still beats it on DeepSeek V4.1 Flash streaming speed. 

 All benchmark numbers are self-reported. 

 Check out the technical blog , the API docs and the launch post on X . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Sarvam Launches Sarvam Token Factory: Bringing India-Hosted Inference to 8 Open Models appeared first on MarkTechPost .
