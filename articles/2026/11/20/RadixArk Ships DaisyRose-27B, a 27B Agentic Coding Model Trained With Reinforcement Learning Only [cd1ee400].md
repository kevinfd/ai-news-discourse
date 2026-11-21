---
id: "cd1ee40087d5821f"
title: "RadixArk Ships DaisyRose-27B, a 27B Agentic Coding Model Trained With Reinforcement Learning Only"
url: "https://marktechpost.com/2026/11/20/radixark-daisyrose-27b-agentic-model"
link: "https://marktechpost.com/2026/11/20/radixark-daisyrose-27b-agentic-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T17:42:29Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "This week RadixArk released DaisyRose-27B , its first open-weight model. DaisyRose-27B is an agentic coding model from RadixArk, post-trained from Qwen3.8-27B with reinforcement learning (RL). The model card page states that it used RL only, with no SFT or distillation. It ships under Apache 2.0 as a drop-in replacement for the base model. The main result: Terminal Bench 4.1 pass@1 rises from…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: []
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "summary"
word_count: 1420
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# RadixArk Ships DaisyRose-27B, a 27B Agentic Coding Model Trained With Reinforcement Learning Only

MarkTechPost · Asif Razzaq · 2026-11-20

This week RadixArk released DaisyRose-27B , its first open-weight model. DaisyRose-27B is an agentic coding model from RadixArk, post-trained from Qwen3.8-27B with reinforcement learning (RL). The model card page states that it used RL only, with no SFT or distillation. It ships under Apache 2.0 as a drop-in replacement for the base model. The main result: Terminal Bench 4.1 pass@1 rises from 5.6 to 12.0. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Size: 27.8B dense parameters (0.46B vision encoder, 0.42B MTP head), 262,144-token context. 

 Runs on: 1 GPU. BF16 is about 52 GB, FP8 about 29 GB, NVFP4 about 23 GB (Blackwell only). Listed targets: H200, B200, GB300, RTX PRO 6000, RTX 5090, DGX Spark. GGUF also available. 

 Performance: Beats its Qwen3.8-27B base on all 7 reported benchmarks. 

 Best: IFBench 82.4, the top score among the 9 models RadixArk compared. 

 Worst: HLE (text only) 34.3, only +0.4 over the base and below Inkling 2 Small’s 44.1. 

 Bottom line: Best: Terminal Bench 4.1 more than doubles after 18 days of RL. Worst: it still trails much larger MoE models on hard agentic tasks. 

 What is DaisyRose-27B? 

 DaisyRose-27B keeps the Qwen3.8-27B architecture unchanged. The model card lists 64 decoder layers in a 3:1 pattern. Three Gated DeltaNet linear-attention layers alternate with 1 full-attention layer. Hidden size is 5,120. A 27-layer vision encoder handles images. One multi-token-prediction layer supports speculative decoding. Input is text and images, output is text, and it is a thinking model. 

 How was DaisyRose-27B trained? 

 RadixArk built about 1,200 curated tasks with Eigent AI , chosen from thousands of candidates. Each task targets a specific failure of the base model. Each sandbox attempt allows up to 1.5 hours, 100+ tool calls and 256k+ output tokens. Agent sessions reach up to 1M tokens, per the blog . 

 Training ran on Miles , RadixArk’s open-source RL framework, in fully asynchronous mode. The run used 144 H200 GPUs for 18 days. Of those, 128 handled agent inference and 16 handled training. Total compute was 63,000 GPU-hours. 

 RadixArk reports 37% MFU on its internal backend. An open-source Megatron-based trainer reached 16%. End-to-end throughput was 16.8k tokens/s versus 8.3k, a 2.0x speedup. RadixArk says this cut GPU time by 57%. 

 Sandboxes ran on AgentENV . RadixArk reports about 944,000 sandboxes from mid-September to mid-November. Peak concurrency hit 1,566. Creation success was 99% over 9 weeks. RadixArk puts the cost about 80% below popular cloud sandbox providers. 

 How does DaisyRose-27B perform on benchmarks? 

 All scores are self-reported by RadixArk. DaisyRose scores are the higher of its BF16 and FP8 runs. 

 Benchmark DaisyRose-27B Qwen3.8-27B Change Terminal Bench 4.1 (pass@1) 12.0 5.6 +6.4 Terminal Bench 2.1 75.5 73.0 +2.5 DeepSWE v1.1 46.2 42.2 +4.0 SWE Bench Pro v2 94.7 91.3 +3.4 HLE (text only) 34.3 33.9 +0.4 IFBench 82.4 79.5 +2.9 GPQA Diamond 90.7 89.2 +1.5 

 Source: RadixArk blog and model card . 

 The largest jump is Terminal Bench 4.1, which more than doubles. Coding gains are steady: +4.0 on DeepSWE v1.1 and +3.4 on SWE Bench Pro v2. Knowledge gains are small, at +0.4 on HLE and +1.5 on GPQA Diamond. 

 Against larger models, results are mixed. MiMo V2.6 Flash (309B total) leads Terminal Bench 4.1 at 16.1. Inkling 2 Small (594B total) leads DeepSWE at 72.1 and HLE at 44.1. DaisyRose-27B tops RadixArk’s 9-model table only on IFBench. 

 Auto-play</button></div>
 </div>

 <div class="pane" id="dr-bm">
 <div class="ctrl" id="dr-bsel"></div>
 <div class="bars" id="dr-bars"></div>
 <div class="note" id="dr-bnote"></div>
 <div class="note">Self-reported by RadixArk. DaisyRose scores are the higher of BF16 and FP8 runs. Competitor scores come from each developer's reports or cited leaderboards; some Terminal Bench 4.1 scores are 4.0 results. Missing bars were not reported.</div>
 </div>

 <div class="pane" id="dr-ef">
 <div class="ctrl"><button class="btn on" data-m="mfu">MFU</button><button class="btn" data-m="tps">Throughput</button><button class="btn" data-m="gpu">GPU split</button></div>
 <div class="bars" id="dr-ebars"></div>
 <div class="grid2" style="margin-top:14px">
 <div class="detail"><div class="big">57%</div>less GPU time reported for the release run versus the open-source baseline.</div>
 <div class="detail"><div class="big">~944,000</div>sandboxes created mid-Sept to mid-Nov, peak 1,566 concurrent, 99% creation success over 9 weeks.</div>
 </div>
 </div>

 <div class="pane" id="dr-dp">
 <div class="ctrl" id="dr-psel"><button class="btn on" data-q="bf16">BF16</button><button class="btn" data-q="fp8">FP8</button><button class="btn" data-q="nvfp4">NVFP4</button><button class="btn" data-q="gguf">GGUF</button></div>
 <div class="grid2" style="margin-top:12px">
 <div class="detail"><div class="big" id="dr-size">~52 GB</div><span id="dr-qnote"></span></div>
 <div class="detail"><b>Single-GPU targets listed by RadixArk</b><div class="chips"><span class="chip">H200</span><span class="chip">B200</span><span class="chip">GB300</span><span class="chip">RTX PRO 6000</span><span class="chip">RTX 5090</span><span class="chip">DGX Spark</span></div></div>
 </div>
 <div class="ctrl"><button class="btn on" data-s="sg">SGLang + DSpark</button><button class="btn" data-s="vl">vLLM</button></div>
 <pre id="dr-code"></pre>
 <div class="note">SGLang command abridged; see the model card for the full flag set. Thinking-mode sampling: temperature 1.0, top_p 0.95, top_k 20, min_p 0.</div>
 </div>

 <div class="ft"><span>Sources: radixark.com/blog/daisyrose-27b · huggingface.co/RadixArk/DaisyRose-27B</span><a href="https://www.marktechpost.com/" target="_blank" rel="noopener">© Marktechpost</a></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-drose');
function q(s,c){return (c||R).querySelector(s)}function qa(s,c){return Array.prototype.slice.call((c||R).querySelectorAll(s))}
function resize(){try{parent.postMessage({mtpFrame:'drose',h:R.offsetHeight+40},'*')}catch(e){}}
qa('.tab').forEach(function(t){t.addEventListener('click',function(){qa('.tab').forEach(function(x){x.classList.remove('on')});qa('.pane').forEach(function(x){x.classList.remove('on')});t.classList.add('on');q('#dr-'+t.dataset.p).classList.add('on');if(t.dataset.p==='bm')drawB(cur);if(t.dataset.p==='ef')drawE(em);setTimeout(resize,60)})});
qa('.tile').forEach(function(t){t.addEventListener('click',function(){t.classList.toggle('open');setTimeout(resize,30)})});
/* layers */
var L=q('#dr-layers');for(var i=0;i<64;i++){var d=document.createElement('div');d.className='ly '+((i%4===3)?'att':'lin');L.appendChild(d)}
function anim(){var c=qa('.ly');c.forEach(function(x){x.classList.remove('lit')});c.forEach(function(x,i){setTimeout(function(){x.classList.add('lit')},i*28)})}
L.addEventListener('click',anim);setTimeout(anim,300);
/* training steps */
var S=[
 '<b>Curate tasks.</b> RadixArk and Eigent AI picked about 1,200 tasks from thousands of candidates. Each task targets a specific failure of the Qwen3.8-27B base model.',
 '<b>Agent rollouts.</b> 128 H200s generate trajectories inside AgentENV sandboxes. Each attempt allows up to 1.5 hours, 100+ tool calls and 256k+ output tokens.',
 '<b>Async RL update.</b> 16 H200s train with Miles in fully asynchronous mode, so rollouts and optimizer steps overlap. No SFT or distillation is used.',
 '<b>Ship weights.</b> The run took 18 days on 144 H200s, about 63,000 GPU-hours. Result: Terminal Bench 4.1 pass@1 from 5.6 to 12.0.'];
var si=0,timer=null;function step(n){si=(n+4)%4;qa('.st',q('#dr-flow')).forEach(function(x,i){x.classList.toggle('on',i<=si)});q('#dr-prog').style.width=((si+1)*25)+'%';q('#dr-detail').innerHTML=S[si];resize()}
q('#dr-next').onclick=function(){step(si+1)};q('#dr-prev').onclick=function(){step(si-1)};
q('#dr-auto').onclick=function(){var b=this;if(timer){clearInterval(timer);timer=null;b.textContent=' Auto-play';b.classList.remove('on')}else{b.textContent='❚❚ Pause';b.classList.add('on');timer=setInterval(function(){step(si+1)},2200)}};step(0);
/* benchmarks */
var M=['DaisyRose-27B','Qwen3.8-27B','Muse Glimmer-30B','Qwen3.6-35B-A3B','MiMo V2.6 Flash','Inkling 2 Small','Beam 1.0','Muse Spark Open','GPT-6 Luna'];
var B={'Terminal Bench 4.1':[12.0,5.6,0.5,0.0,16.1,13.0,6.4,6.6,15.2],'Terminal Bench 2.1':[75.5,73.0,51.7,44.9,87.6,81.3,80.1,76.4,73.0],'DeepSWE v1.1':[46.2,42.2,4.4,0.0,67.9,72.1,43.3,60.0,66.6],'SWE Bench Pro v2':[94.7,91.3,80.4,73.3,null,97.7,null,95.0,null],'HLE (text only)':[34.3,33.9,22.0,22.2,35.1,44.1,34.7,43.9,38.5],'IFBench':[82.4,79.5,77.0,64.4,null,null,79.6,null,null],'GPQA Diamond':[90.7,89.2,83.5,86.0,88.7,93.0,90.6,89.0,90.5]};
var cur='Terminal Bench 4.1',bs=q('#dr-bsel');Object.keys(B).forEach(function(k){var b=document.createElement('button');b.className='btn'+(k===cur?' on':'');b.textContent=k;b.onclick=function(){qa('.btn',bs).forEach(function(x){x.classList.remove('on')});b.classList.add('on');cur=k;drawB(k)};bs.appendChild(b)});
function drawB(k){var v=B[k],mx=Math.max.apply(null,v.filter(function(x){return x!==null})),h='';M.forEach(function(m,i){if(v[i]===null)return;h+='<div class="br'+(i===0?' me':i===1?' base':'')+'"><span class="nm">'+m+'</span><div class="bg"><div class="fl" data-w="'+(mx?v[i]/mx*100:0)+'"></div></div><span class="vl">'+v[i].toFixed(1)+'</span></div>'});q('#dr-bars').innerHTML=h;setTimeout(function(){qa('.fl',q('#dr-bars')).forEach(function(f){f.style.width=f.dataset.w+'%'})},40);var d=(v[0]-v[1]).toFixed(1);q('#dr-bnote').innerHTML='<b style="color:#f5c542">DaisyRose vs base: +'+d+'</b> ('+v[1].toFixed(1)+' → '+v[0].toFixed(1)+')';resize()}
/* efficiency */
var E={mfu:{rows:[['Miles internal backend',37,'37%'],['Open-source Megatron-based',16,'16%']],mx:37},tps:{rows:[['Release run (Miles)',16.8,'16.8k'],['Baseline',8.3,'8.3k']],mx:16.8},gpu:{rows:[['Agent inference',128,'128'],['Training',16,'16']],mx:128}};
var em='mfu';qa('[data-m]').forEach(function(b){b.onclick=function(){qa('[data-m]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');em=b.dataset.m;drawE(em)}});
function drawE(k){var e=E[k],h='';e.rows.forEach(function(r,i){h+='<div class="br'+(i===0?' me':'')+'"><span class="nm">'+r[0]+'</span><div class="bg"><div class="fl" data-w="'+r[1]/e.mx*100+'"></div></div><span class="vl">'+r[2]+'</span></div>'});if(k==='tps')h+='<div class="note">Tokens/s end to end: a 2.0x speedup.</div>';if(k==='gpu')h+='<div class="note">144 H200 GPUs total for 18 days.</div>';q('#dr-ebars').innerHTML=h;setTimeout(function(){qa('.fl',q('#dr-ebars')).forEach(function(f){f.style.width=f.dataset.w+'%'})},40);resize()}
drawE('mfu');
/* deploy */
var Qs={bf16:['~52 GB','Main repo: RadixArk/DaisyRose-27B.'],fp8:['~29 GB','RadixArk/DaisyRose-27B-FP8.'],nvfp4:['~23 GB','RadixArk/DaisyRose-27B-NVFP4. Requires a Blackwell GPU.'],gguf:['GGUF','RadixArk/DaisyRose-27B-GGUF for local runtimes. Size varies by quant.']};
qa('[data-q]').forEach(function(b){b.onclick=function(){qa('[data-q]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');q('#dr-size').textContent=Qs[b.dataset.q][0];q('#dr-qnote').textContent=Qs[b.dataset.q][1]}});q('#dr-qnote').textContent=Qs.bf16[1];
var C={sg:'python3 -m sglang.launch_server \\\n --model-path RadixArk/DaisyRose-27B \\\n --tp-size 1 --context-length 262144 \\\n --reasoning-parser qwen3 \\\n --tool-call-parser qwen3_coder \\\n --speculative-algorithm DSPARK \\\n --speculative-draft-model-path RadixArk/Qwen3.8-27B-DSpark',vl:'pip install vllm\nvllm serve "RadixArk/DaisyRose-27B" # OpenAI-compatible API on :8000'};
q('#dr-code').textContent=C.sg;qa('[data-s]').forEach(function(b){b.onclick=function(){qa('[data-s]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');q('#dr-code').textContent=C[b.dataset.s];resize()}});
window.addEventListener('load',resize);window.addEventListener('resize',resize);setTimeout(resize,400);
})();
</script>
</body></html>
"> 

(function(){var f=document.getElementById('mtp-drose-frame');window.addEventListener('message',function(e){var d=e.data;if(d&&d.mtpFrame==='drose'&&d.h&&f&&e.source===f.contentWindow){f.style.height=d.h+'px';}});})();

 How do you deploy DaisyRose-27B? 

 Weights are on Hugging Face in BF16 , FP8 , NVFP4 and GGUF . NVFP4 requires a Blackwell GPU. RadixArk recommends SGLang with DSpark speculative decoding. That setup uses the Qwen3.8-27B-DSpark draft model. vLLM also works via vllm serve "RadixArk/DaisyRose-27B" . Suggested thinking-mode sampling is temperature 1.0, top_p 0.95 and top_k 20. 

 How does DaisyRose-27B compare with similar-size models? 

 Metrics DaisyRose-27B Qwen3.8-27B Muse Glimmer-30B Qwen3.6-35B-A3B Developer RadixArk Qwen (Alibaba) Meta Superintelligence Lab Qwen (Alibaba) Total params 27.8B 27B ~29.6B 35B Active params 27.8B (dense) 27B (dense) ~29.6B (dense) 3B (MoE) Context 262,144 262,144 (extensible to 1M) 131,072+ 262,144 (extensible to 1,010,000) License Apache 2.0 Apache 2.0 Apache 2.0 Apache 2.0 Input Text, image Text, image, video Text, image Text, image Hardware 1 GPU; 52 GB BF16, 23 GB NVFP4 Not disclosed 64 GB full precision; under 20 GB 4-bit Not disclosed Terminal Bench 2.1* 75.5 73.0 51.7 44.9 SWE Bench Pro v2* 94.7 91.3 80.4 73.3 DeepSWE v1.1* 46.2 42.2 4.4 0.0 HLE (text only)* 34.3 33.9 22.0 22.2 IFBench* 82.4 79.5 77.0 64.4 GPQA Diamond* 90.7 89.2 83.5 86.0 SWE-bench Pro (official card) Not disclosed 61.7 51.2 49.5 

 *From RadixArk’s comparison table , which cites each developer’s reports or leaderboards. SWE Bench Pro v2 figures trace to arXiv 2611.16289 . The last row comes from each model’s own card. 

 Key Takeaways 

 RL only, no SFT: 1,200 tasks, 18 days, 144 H200s. 

 Terminal Bench 4.1 jumps from 5.6 to 12.0. 

 Fits 1 GPU: 52 GB in BF16, 23 GB in NVFP4. 

 Miles hit 37% MFU, 2.0x faster end to end. 

 Apache 2.0, but every score is self-reported. 

 Check out the model card , the technical blog and the Miles repo . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post RadixArk Ships DaisyRose-27B, a 27B Agentic Coding Model Trained With Reinforcement Learning Only appeared first on MarkTechPost .
