---
id: "4a2e4b32e4e9a608"
title: "MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI"
url: "https://marktechpost.com/2026/11/10/ifm-pan-2-open-world-model"
link: "https://marktechpost.com/2026/11/10/ifm-pan-2-open-world-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-11T07:38:57Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Michal Sutter"]
language: "en"
summary: "The Institute of Foundation Models (IFM) at MBZUAI released PAN 2 , an open world model for physical intelligence. The PAN 2 world model takes a scene and a text action and simulates the outcome as video. IFM announced it on X on November 10, 2026. Weights, training code and inference code ship under Apache 2.0 . For robotics and agent developers, the pitch is simple: test a plan in simulation…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Artificial Intelligence", "Editors Pick", "New Releases", "Staff", "Tech News", "Technology", "World Model"]
orgs: ["Alibaba"]
topics: ["models & research", "agents & coding", "chips & infrastructure", "safety & ethics"]
content_source: "summary"
word_count: 1587
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI

MarkTechPost · Michal Sutter · 2026-11-11

The Institute of Foundation Models (IFM) at MBZUAI released PAN 2 , an open world model for physical intelligence. The PAN 2 world model takes a scene and a text action and simulates the outcome as video. IFM announced it on X on November 10, 2026. Weights, training code and inference code ship under Apache 2.0 . For robotics and agent developers, the pitch is simple: test a plan in simulation before acting on it. 

 TL;DR 

 Size: 29B-parameter diffusion transformer (MMDiT), dense. Inputs: text plus an optional first frame. Output: 704×1248 video at 24 fps, up to 20 s. 

 Runs on: Data-center GPUs. Each worker holds the full 29B model in BF16, with block offloading as fallback. 

 Performance: Leads 6 tested models on full plans. Trails MiniMax-H3 on single actions and human preference. 

 Best: 34.0% full-plan completion on 100 multi-step tasks, the highest of all models tested (self-reported). 

 Worst: About 2 in 3 plans miss a step. Physics-IQ system default: 37.48 vs 42.91 for MiniMax-H3. 

 Bottom line: Best: a fully open world model that leads on multi-step plans. Worst: long plans still fail often, and hardware needs are high. 

 What is PAN 2? 

 PAN 2 is a general-purpose world model from IFM that simulates how a scene changes after an action. It follows the Generative Latent Prediction (GLP) architecture from IFM’s Critique of World Models paper. It succeeds PAN , released in November 2025. 

 The goal is simulative reasoning . An agent proposes plans, PAN 2 simulates each one, and the agent acts on the best. 

 How does PAN 2 work? 

 PAN 2 splits simulation into 2 kinds of reasoning : 

 Conceptual reasoning : An LLM reads the observation and the requested actions. It writes the next world state as structured JSON: events, timed actions bound to actors, and camera motion. Any instruction-following LLM can fill this role. IFM’s report uses Kimi K3 by default. 

 Perceptual reasoning : A 29B MMDiT predicts the video latents. IFM trained it from scratch on hundreds of millions of annotated videos. A frozen Qwen3.5-9B text encoder conditions it. The Wan 2.2 VAE decoder renders the final frames. 

 IFM’s ablation shows the LLM matters. With no conceptual reasoning, full-plan completion drops from 34.0% to 0.0%. Step completion falls from 75.1% to 8.7%. A format-only rewrite recovers part of the gap, reaching 27.8% full-plan completion. 

 IFM also dropped gameplay, animation and simulation footage after early training. A 9B test model trained without it won 58% of blinded votes. 

 Prev</button>
 <button class="btn pri" id="mtpNext">Next </button>
 <button class="btn" id="mtpPlay"> Auto-play</button>
 <span class="hint">Click any step to jump</span>
 </div>
 </div>

 <div class="pane" id="p-bench">
 <div class="seg" id="mtpSeg"></div>
 <div class="bars" id="mtpBars"></div>
 <p class="note" id="mtpNote"></p>
 </div>

 <div class="pane" id="p-abl">
 <div class="seg" id="mtpAblSeg">
 <button class="chip" data-a="0">None: action sent straight to diffusion</button>
 <button class="chip" data-a="1">Format-only rewrite</button>
 <button class="chip on" data-a="2">Full conceptual reasoning</button>
 </div>
 <div class="abl">
 <div class="card"><div class="k">6 capabilities</div><div class="v" id="ab0">84.6<small>%</small></div><div class="mini"><i id="ib0"></i></div></div>
 <div class="card"><div class="k">Step completion</div><div class="v" id="ab1">75.1<small>%</small></div><div class="mini"><i id="ib1"></i></div></div>
 <div class="card"><div class="k">Full-plan completion</div><div class="v" id="ab2">34.0<small>%</small></div><div class="mini"><i id="ib2"></i></div></div>
 </div>
 <p class="note">IFM ablation with Kimi K3 as the reasoner; the diffusion model stays fixed. Without the LLM, no multi-step plan completes. Source: IFM technical blog.</p>
 </div>

 <div class="pane" id="p-run">
 <div class="grid">
 <div class="spec"><div class="k">Generator</div><div class="v">29B MMDiT, BF16, trained from scratch</div></div>
 <div class="spec"><div class="k">Tasks</div><div class="v">Text-to-video, image-to-video</div></div>
 <div class="spec"><div class="k">Output</div><div class="v">704x1248 at 24 fps, up to 20 s (481 frames)</div></div>
 <div class="spec"><div class="k">Default clip</div><div class="v">241 frames, about 10 s</div></div>
 <div class="spec"><div class="k">Sampler</div><div class="v">50 steps · flow shift 9 · CFG 2.5</div></div>
 <div class="spec"><div class="k">Caption budget</div><div class="v">1,536 tokens hard limit</div></div>
 <div class="spec"><div class="k">Serving</div><div class="v">Diffusers · vLLM · FastVideo · generate.py</div></div>
 <div class="spec"><div class="k">GPU memory</div><div class="v">Full 29B per worker; block offload fallback; VRAM not disclosed</div></div>
 <div class="spec"><div class="k">Safety</div><div class="v">pan2-guardrail: unsafe T2V 33.9% → 1.5%</div></div>
 <div class="spec"><div class="k">License</div><div class="v">Apache 2.0: weights, training + inference code</div></div>
 </div>
<pre>hf download IFM/PAN2 --include "transformer/*"
hf download Qwen/Qwen3.5-9B
hf download Wan-AI/Wan2.2-TI2V-5B-Diffusers</pre>
 </div>

 <div class="ft">
 <span>Sources: <a href="https://huggingface.co/IFM/PAN2" target="_blank" rel="noopener">HF model card</a> · <a href="https://ifm.ai/blog/pan2/" target="_blank" rel="noopener">IFM blog</a> · scores self-reported</span>
 <span class="mtp">© Marktechpost</span>
 </div>
</div>
<script>
(function(){
 var R=document.getElementById('mtp-pan2');
 function post(){try{parent.postMessage({type:'mtp-pan2-h',h:R.offsetHeight+40},'*')}catch(e){}}
 // tabs
 R.querySelectorAll('.tab').forEach(function(b){b.addEventListener('click',function(){
 R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
 R.querySelectorAll('.pane').forEach(function(x){x.classList.remove('on')});
 b.classList.add('on');document.getElementById('p-'+b.dataset.p).classList.add('on');
 if(b.dataset.p==='bench')drawBars(cur);
 if(b.dataset.p==='abl')setAbl(abl);
 setTimeout(post,60);
 })});
 // pipeline
 var D=[
 ['Observe: current world + action','Input is an optional starting image plus text, and actions described in text with a duration. Example: "Accelerate mangrove forest growth to protect the coast."',''],
 ['Conceptual reasoning backbone (LLM)','An instruction-following LLM reasons over the scene and the action. It writes the next world state as structured, time-grounded JSON. IFM\'s report uses Kimi K3 by default.','{ "events": [{"t":"0-3s","actor":"surfer","action":"paddles"},\n {"t":"3s","actor":"surfer","action":"pops up"}],\n "camera": "slow pan right" }'],
 ['Frozen text encoder','Qwen3.5-9B maps the structured caption to conditioning features. Captions have a soft limit of 1,480 and a hard limit of 1,536 tokens.',''],
 ['Perceptual reasoning backbone (29B MMDiT)','A 29B diffusion transformer, trained from scratch on hundreds of millions of videos in the same caption format, fills in geometry, contact and motion. It predicts video latents conditioned on the state and the starting frame.',''],
 ['Render the next observation','The Wan 2.2 VAE decoder turns latents into 704x1248 video at 24 fps, up to 20 s. An agent compares simulated outcomes and acts on the best plan.','']
 ];
 var step=0,timer=null,nodes=R.querySelectorAll('.node');
 function show(i){step=(i+5)%5;nodes.forEach(function(n,k){n.classList.toggle('on',k===step);n.classList.toggle('done',k<step)});
 document.getElementById('mtpFlow').style.width=((step+1)/5*100)+'%';
 var d=D[step];document.getElementById('mtpDetail').innerHTML='<h4>'+d[0]+'</h4><p>'+d[1]+'</p>'+(d[2]?'<pre>'+d[2]+'</pre>':'');setTimeout(post,30);}
 nodes.forEach(function(n){n.addEventListener('click',function(){stop();show(+n.dataset.i)})});
 document.getElementById('mtpNext').onclick=function(){stop();show(step+1)};
 document.getElementById('mtpPrev').onclick=function(){stop();show(step-1)};
 var pb=document.getElementById('mtpPlay');
 function stop(){if(timer){clearInterval(timer);timer=null;pb.textContent=' Auto-play'}}
 pb.onclick=function(){if(timer){stop();return}pb.textContent='❚❚ Pause';timer=setInterval(function(){show(step+1)},2600)};
 show(0);
 // bars
 var M={
 plan:{n:'Full-plan completion',u:'%',max:40,note:'100 egocentric tasks, 456 steps. Share of simulations with every step done. † closed model, single seed.',d:[['PAN 2',34.00,1],['MiniMax-H3',32.50],['FLUX 3 †',26.77,0,1],['Seedance 2.5 †',24.49,0,1],['Cosmos 3 Super',13.83],['LTX 2.5',13.00]]},
 step:{n:'Step completion',u:'%',max:80,note:'Share of individual plan steps carried out. PAN 2 and MiniMax-H3 are effectively tied.',d:[['MiniMax-H3',75.12],['PAN 2',75.10,1],['FLUX 3 †',72.44,0,1],['Seedance 2.5 †',68.95,0,1],['Cosmos 3 Super',57.23],['LTX 2.5',55.77]]},
 six:{n:'6 capabilities',u:'%',max:90,note:'300 single-action cases (201 I2V, 99 T2V). MiniMax-H3 leads all 6 categories.',d:[['MiniMax-H3',87.20],['PAN 2',84.48,1],['Seedance 2.5 †',78.59,0,1],['FLUX 3 †',77.41,0,1],['LTX 2.5',72.25],['Cosmos 3 Super',71.34]]},
 piq:{n:'Physics-IQ Verified',u:'',max:55,note:'Leaderboard setting; real-take variance = 100. PAN 2 uses Claude Opus 5.5 as reasoner here. LTX 2.5 not on leaderboard.',d:[['FLUX 3 †',51.11,0,1],['PAN 2',49.38,1],['Cosmos 3 Super',48.62],['Seedance 2.5 †',42.43,0,1],['MiniMax-H3',39.79],['Omni Flash 1.1 †',35.34,0,1]]},
 rb:{n:'RBench',u:'',max:65,note:'Robotics benchmark, unweighted mean x100.',d:[['Omni Flash 1.1 †',60.79,0,1],['FLUX 3 †',57.96,0,1],['PAN 2',57.04,1],['Seedance 2.5 †',56.38,0,1],['MiniMax-H3',56.16],['LTX 2.5',51.55],['Cosmos 3 Super',50.64]]},
 elo:{n:'Human Elo',u:'',max:1700,min:1250,note:'Blind pairwise preference: 140 prompts, 13 reviewers, 1,400 comparisons. Open models only.',d:[['MiniMax-H3',1620],['PAN 2 (GPT-6 Astra)',1595,1],['PAN 2 (Claude Opus)',1559,1],['Cosmos 3 Super',1380],['LTX 2.5',1346]]}
 };
 var cur='plan',seg=document.getElementById('mtpSeg');
 Object.keys(M).forEach(function(k){var b=document.createElement('button');b.className='chip'+(k===cur?' on':'');b.textContent=M[k].n;b.onclick=function(){cur=k;seg.querySelectorAll('.chip').forEach(function(x){x.classList.remove('on')});b.classList.add('on');drawBars(k)};seg.appendChild(b)});
 function drawBars(k){var m=M[k],box=document.getElementById('mtpBars');box.innerHTML='';
 m.d.forEach(function(r){var row=document.createElement('div');row.className='row'+(r[2]?' me':'');
 var v=m.u==='%'?r[1].toFixed(2)+'%':(k==='elo'?String(r[1]):r[1].toFixed(2));
 row.innerHTML='<div class="lab'+(r[3]?' cl':'')+'">'+r[0]+'</div><div class="trk"><div class="fill"></div></div><div class="val">'+v+'</div>';box.appendChild(row);
 var mn=m.min||0,w=Math.max(2,(r[1]-mn)/(m.max-mn)*100);
 requestAnimationFrame(function(){requestAnimationFrame(function(){row.querySelector('.fill').style.width=w+'%'})});});
 document.getElementById('mtpNote').textContent=m.note+(m.min?' Axis starts at '+m.min+'.':'');setTimeout(post,60);}
 // ablation
 var A=[[45.1,8.7,0.0],[78.2,70.7,27.8],[84.6,75.1,34.0]],abl=2;
 function setAbl(i){abl=i;R.querySelectorAll('#mtpAblSeg .chip').forEach(function(c){c.classList.toggle('on',+c.dataset.a===i)});
 [0,1,2].forEach(function(j){var el=document.getElementById('ab'+j),to=A[i][j],from=parseFloat(el.textContent)||0,t0=null;
 function tick(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/600),v=from+(to-from)*p;el.innerHTML=v.toFixed(1)+'<small>%</small>';if(p<1)requestAnimationFrame(tick)}
 requestAnimationFrame(tick);document.getElementById('ib'+j).style.width=to+'%';});}
 R.querySelectorAll('#mtpAblSeg .chip').forEach(function(c){c.onclick=function(){setAbl(+c.dataset.a)}});
 window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body>
</html>
"> 

(function(){var f=document.getElementById('mtp-pan2-frame');window.addEventListener('message',function(e){if(e.data&&e.data.type==='mtp-pan2-h'&&e.source===f.contentWindow){f.style.height=e.data.h+'px';}});})();

 How does PAN 2 perform on benchmarks? 

 All numbers below are self-reported by IFM. Its own test suite covers 6 capabilities across 300 single-action cases, plus 100 multi-step tasks. 

 Full-plan completion: 34.00% vs 32.50% for MiniMax-H3, 26.77% for FLUX 3 and 24.49% for Seedance 2.5. 

 Step completion: 75.10%, level with MiniMax-H3 at 75.12%. 

 6 capabilities overall: 84.48% vs 87.20% for MiniMax-H3. MiniMax-H3 leads in all 6 categories. 

 Physics-IQ Verified (leaderboard setting): 49.38, first among open models. Closed FLUX 3 scores 51.11. 

 RBench: 57.04 vs 56.16 for MiniMax-H3 and 50.64 for Cosmos 3 Super. 

 Human Elo: 1595 with a GPT-6 Astra reasoner, behind MiniMax-H3 at 1620. 

 PAN 2 vs MiniMax-H3, Cosmos 3 Super and LTX-2.5 

 Feature PAN 2 MiniMax-H3 Cosmos 3 Super LTX-2.5 Developer IFM (MBZUAI) MiniMax NVIDIA Lightricks Generator size 29B MMDiT 33B dense transformer (~13B in cacheable AdaLN branches) 64B Mixture-of-Transformers 22B transformer (per checkpoint file names) Planner / encoder Any LLM + frozen Qwen3.5-9B encoder Qwen3-VL-32B encoder; hosted Context-IR Built-in autoregressive tower Gemma-based text encoder Max clip 20 s, 704×1248, 24 fps 15 s, 24 fps, 768p (2K via hosted module) 400 frames Not disclosed Audio No Yes, stereo Yes Yes License Apache 2.0 MiniMax H3 Community License OpenMDW 1.1 LTX-2.x Community License Training code Yes Not disclosed Framework on GitHub Not disclosed Full-plan completion* 34.00% 32.50% 13.83% 13.00% Physics-IQ Verified (leaderboard)* 49.38 39.79 48.62 Not reported Human Elo* 1595 1620 1380 1346 

 *Scores from IFM’s PAN 2 model card , run by IFM. The blog reports different Cosmos 3 Super and LTX-2.5 plan scores. 

 How do you run PAN 2? 

 PAN 2 supports text-to-video and image-to-video. You can run it through Hugging Face Diffusers , vLLM , FastVideo or the repo’s generate.py . 

 The default sampler uses 50 steps, flow shift 9 and guidance 2.5. A clip defaults to 241 frames, about 10 seconds. Each GPU worker loads the full 29B model in BF16. IFM publishes no VRAM figure or generation time. 

 Prompts work best as structured captions. IFM ships a Conceptual Reasoner skill for Claude Code and Codex that rewrites free text. Captions have a hard budget of 1,536 tokens. 

 IFM strongly recommends the separate pan2-guardrail . In IFM tests, it cut unsafe outputs from harmful T2V requests from 33.9% to 1.5%. It also blocked 11.5% of benign T2V requests. 

 Key Takeaways 

 PAN 2 pairs an LLM planner with a 29B diffusion model trained from scratch. 

 It leads 6 tested models on full-plan completion at 34.0%. 

 MiniMax-H3 still wins single actions and human preference. 

 Weights, training and inference code are Apache 2.0. 

 Removing the LLM planner drops full-plan completion to 0%. 

 Check out the model weights , GitHub repo , technical blog and p ress release . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI appeared first on MarkTechPost .
