---
id: "12c96cbbfed06818"
title: "Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target’s Sparse KV Cache"
url: "https://marktechpost.com/2026/11/26/tencent-dfly2-speculative-decoding-sparse-models"
link: "https://marktechpost.com/2026/11/26/tencent-dfly2-speculative-decoding-sparse-models"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-27T03:31:30Z"
published_date: "2026-11-27"
collected_at: "2026-11-27T13:04:05Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Tencent has open-sourced DFly2 , a speculative decoding drafter built for natively sparse LLMs. DFly2 speculative decoding targets models like DeepSeek-V4.1-Flash, GLM-5.3-Flash and Tencent’s own Hy4 flash . Its main approach is that the drafter keeps no KV cache of its own. This is important for long-context and agentic serving, where draft memory competes with concurrency. \n\n TL;DR \n\n Size:…"
tags: ["AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Open Source", "Staff"]
orgs: ["DeepSeek", "Nvidia"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "summary"
word_count: 1432
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target’s Sparse KV Cache

MarkTechPost · Asif Razzaq · 2026-11-27

Tencent has open-sourced DFly2 , a speculative decoding drafter built for natively sparse LLMs. DFly2 speculative decoding targets models like DeepSeek-V4.1-Flash, GLM-5.3-Flash and Tencent’s own Hy4 flash . Its main approach is that the drafter keeps no KV cache of its own. This is important for long-context and agentic serving, where draft memory competes with concurrency. 

 TL;DR 

 Size: 0.85B-parameter, 5-layer drafter shipped with Hy4 flash. 

 Runs on: Serving tests used NVIDIA H20 GPUs with vLLM, TP8 per instance. Hy4 flash’s vLLM recipe defaults to 8x H200. 

 Performance: Higher draft acceptance than same-recipe DFlash and DSpark on all 3 targets and all general benchmarks. 

 Best: Up to 81% more throughput on DeepSeek-V4.1-Flash (SWE 64K), at matched per-user speed. 

 Worst: Smallest gain on Hy4 flash general tasks: only 3.9% over DSpark at temperature 0. 

 What is DFly2? 

 DFly2 is a block-parallel speculative decoding drafter from Tencent’s Hunyuan AI Infra team. It is described in the research paper ‘ DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target’s Sparsity ‘. 

 Speculative decoding uses a small drafter to propose tokens. The target verifies them in 1 pass, so output stays lossless. Long context makes this costly. A normal drafter attends over the whole prefix and stores its own KV cache. 

 How does DFly2 work? 

 DFly2 pairs each draft layer with one sparse attention layer in the target. It shares 2 things with that layer. 

 KV sharing: the draft layer reads the paired target layer’s latent KV cache. 

 Index sharing: it attends only to positions the target’s indexer already selected (top-k sparse KV). 

 Initialization: each draft layer starts from its paired target layer’s weights. 

 Hidden injection: the target’s last-layer hidden state is gated into the draft block. 

 Intra-block correction: the drafter rereads the shared context slot by slot within a block. 

 On DeepSeek-V4.1-Flash, a selection made 1 step early covers close to 90% of what later block tokens select. A same-size sliding window recovers less than 20%. 

 Per the AngelSpec GitHub page , each draft token attends to at most about 2K keys. So drafting cost stays roughly flat at any context length. DFly2 also skips prefill entirely. The prefill-to-decode transfer adds only 1 last-layer hidden state. 

 How much memory does a separate draft cache cost? 

 A conventional 3-layer drafter cache would add this much per token (bf16, paper Table 2): 

 Target Target KV Drafter cache Increase DeepSeek-V4.1-Flash 4.4 KiB 3.4 KiB 1.76x GLM-5.3-Flash 11.7 KiB 3.0 KiB 1.26x Hy4 flash 17.2 KiB 3.4 KiB 1.20x 

 At 32K, removing the drafter’s cache lets the same memory pool hold 1.73x as many requests. 

 Back</button><button class="btn on" id="next">Next step </button><button class="btn" id="auto">Auto-play</button></div>
 <div class="dg">
 <div class="col"><h4>Target sparse layers</h4>
 <div class="ly" id="t1">Layer k<span class="kv" id="kv1"></span></div>
 <div class="ly" id="t2">Layer m<span class="kv" id="kv2"></span></div>
 <div class="ly" id="t3">Layer l<span class="kv" id="kv3"></span></div>
 </div>
 <div class="arc"><div class="arw"><div class="ar" id="a1"></div></div><div class="arw"><div class="ar" id="a2"></div></div><div class="arw"><div class="ar" id="a3"></div></div></div>
 <div class="col"><h4>DFly2 drafter</h4>
 <div class="ly dr" id="d1">Draft 1 · init from k<span>KV + index</span></div>
 <div class="ly dr" id="d2">Draft 2 · init from m<span>KV + index</span></div>
 <div class="ly dr" id="d3">Draft 3 · init from l<span>KV + index</span></div>
 </div>
 </div>
 <div class="tok" id="tok"><span>anchor</span><span>t1</span><span>t2</span><span>t3</span><span>t4</span><span>t5</span></div>
 <div class="exp" id="exp"></div>
 </div>

 <div class="pn" id="p1">
 <div class="row"><button class="btn on" data-m="std">Drafter with own cache</button><button class="btn" data-m="dfly">DFly2 (shared)</button></div>
 <div id="mem"></div>
 <p class="note">Per-token KV, bf16, 3-layer drafter (paper Table 2). At 32K, dropping the drafter cache fits 1.73x as many requests in the same memory pool.</p>
 </div>

 <div class="pn" id="p2">
 <div class="row" id="tg"><button class="btn on" data-g="0">DeepSeek-V4.1-Flash</button><button class="btn" data-g="1">GLM-5.3-Flash</button><button class="btn" data-g="2">Hy4 flash</button></div>
 <div class="row" id="tp"><button class="btn on" data-p="0">Temp 0</button><button class="btn" data-p="1">Temp 1</button></div>
 <div id="acc"></div>
 <p class="note">Average accepted length (τ) on general workloads. Baselines retrained by Tencent on the same recipe. Long-context and agentic margins: 10.0% to 31.5% over DSpark.</p>
 </div>

 <div class="pn" id="p3">
 <div class="big">
 <div class="st"><b data-n="28">0%</b><span>Short text</span></div>
 <div class="st"><b data-n="62">0%</b><span>CodeSpan 64K</span></div>
 <div class="st"><b data-n="81">0%</b><span>SWE 64K</span></div>
 </div>
 <div id="spd" style="margin-top:14px"></div>
 <p class="note">Top: extra throughput vs DSpark on DeepSeek-V4.1-Flash at matched per-user speed (NVIDIA H20, vLLM). Bottom: end-to-end speedup over target alone, greedy, concurrency 1.</p>
 </div>

 <div class="ft"><span>Sources: <a href="https://arxiv.org/abs/2611.34776" target="_blank" rel="noopener">DFly2 paper</a> · <a href="https://github.com/Tencent/AngelSpec" target="_blank" rel="noopener">AngelSpec</a> · <a href="https://huggingface.co/tencent/Hy4-flash" target="_blank" rel="noopener">Hy4 flash</a></span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-dfly2');
function rs(){try{parent.postMessage({mtpH:R.offsetHeight+40,id:'mtp-dfly2'},'*')}catch(e){}}
// tabs
var tabs=R.querySelectorAll('.tab');
tabs.forEach(function(t){t.onclick=function(){tabs.forEach(function(x){x.classList.remove('on')});t.classList.add('on');
 R.querySelectorAll('.pn').forEach(function(p){p.classList.remove('on')});var i=t.dataset.t;document.getElementById('p'+i).classList.add('on');
 if(i==1)mem(curM);if(i==2)acc();if(i==3)thr();setTimeout(rs,60);}});
// diagram
var picks=[[1,4,7,11],[0,5,6,12],[2,3,9,13]];
for(var k=1;k<=3;k++){var h='';for(var j=0;j<14;j++)h+='<i></i>';document.getElementById('kv'+k).innerHTML=h;}
var steps=[
 'Prefill runs on the <b>target only</b>. DFly2 is not involved in prefill, so the handoff adds just 1 last-layer hidden state.',
 'Each target sparse layer has an <b>indexer</b> that picks top-k positions from its KV cache (highlighted). Each draft token reads at most about 2K keys.',
 '<b>KV sharing + index sharing:</b> each draft layer reads its paired target layer\'s latent KV and the same picks. No separate draft cache.',
 'The drafter fills a <b>block of 5 slots</b> in parallel. Intra-block correction rereads the shared context slot by slot.',
 'The target <b>verifies the whole block in 1 pass</b>. Accepted tokens (green) are kept, so output stays lossless. Accept counts here are illustrative.'];
var s=0,timer=null;
function draw(){
 for(var k=1;k<=3;k++){var is=document.querySelectorAll('#kv'+k+' i');is.forEach(function(x,j){x.classList.toggle('p',s>=1&&picks[k-1].indexOf(j)>-1)});
 document.getElementById('t'+k).classList.toggle('hl',s>=1);document.getElementById('a'+k).classList.toggle('on',s>=2);document.getElementById('d'+k).classList.toggle('hl',s>=2);}
 var ts=document.querySelectorAll('#tok span');ts.forEach(function(x,j){x.classList.toggle('ok',s>=4&&j<5);x.style.opacity=(s>=3||j==0)?1:.35});
 document.getElementById('exp').innerHTML='<b>Step '+(s+1)+' of 5.</b> '+steps[s];}
document.getElementById('next').onclick=function(){s=(s+1)%5;draw()};
document.getElementById('prev').onclick=function(){s=(s+4)%5;draw()};
document.getElementById('auto').onclick=function(){var b=this;if(timer){clearInterval(timer);timer=null;b.classList.remove('on');b.textContent='Auto-play';}else{b.classList.add('on');b.textContent='Pause';timer=setInterval(function(){s=(s+1)%5;draw()},2200);}};
draw();
// bars
function bars(el,rows,max,fmt){var h='';rows.forEach(function(r){h+='<div class="bar"><span>'+r[0]+'</span><div class="tr"><div class="fl'+(r[2]?' me':'')+'" data-w="'+(r[1]/max*100)+'"></div></div><span class="v">'+fmt(r[1])+'</span></div>'});
 el.innerHTML=h;setTimeout(function(){el.querySelectorAll('.fl').forEach(function(f){f.style.width=f.dataset.w+'%'})},40);}
var M=[['DeepSeek-V4.1-Flash',4.4,3.4],['GLM-5.3-Flash',11.7,3.0],['Hy4 flash',17.2,3.4]],curM='std';
function mem(m){curM=m;var rows=[];M.forEach(function(r){var v=m=='std'?r[1]+r[2]:r[1];rows.push([r[0],v,m=='dfly'])});
 bars(document.getElementById('mem'),rows,21,function(v){return v.toFixed(1)+' KiB'});}
R.querySelectorAll('[data-m]').forEach(function(b){b.onclick=function(){R.querySelectorAll('[data-m]').forEach(function(x){x.classList.remove('on')});b.classList.add('on');mem(b.dataset.m)}});
var A=[[[3.65,3.28],[3.81,3.51],[4.12,3.88]],[[3.43,3.07],[3.68,3.35],[3.96,3.69]],[[3.58,3.48],[3.81,3.73],[3.96,3.95]]],g=0,p=0;
function acc(){var a=A[g];bars(document.getElementById('acc'),[['DFlash',a[0][p]],['DSpark',a[1][p]],['DFly2',a[2][p],1]],4.5,function(v){return v.toFixed(2)})}
function grp(sel,key,fn){R.querySelectorAll(sel+' .btn').forEach(function(b){b.onclick=function(){R.querySelectorAll(sel+' .btn').forEach(function(x){x.classList.remove('on')});b.classList.add('on');fn(+b.dataset[key]);acc()}})}
grp('#tg','g',function(v){g=v});grp('#tp','p',function(v){p=v});
function thr(){R.querySelectorAll('[data-n]').forEach(function(e){var n=+e.dataset.n,c=0;var t=setInterval(function(){c+=Math.ceil(n/20);if(c>=n){c=n;clearInterval(t)}e.textContent='+'+c+'%'},35)});
 bars(document.getElementById('spd'),[['DS-V4.1-Flash',2.97,1],['GLM-5.3-Flash',2.36,1],['Hy4 flash',3.19,1]],3.6,function(v){return v.toFixed(2)+'x'})}
mem('std');acc();
window.addEventListener('load',rs);window.addEventListener('resize',rs);setTimeout(rs,300);
})();
</script>
</body></html>
" style="width:100%;height:600px;border:0;display:block;background:#071330;border-radius:14px;" loading="lazy"> 
 
 (function(){var f=document.getElementById('mtp-dfly2-frame');window.addEventListener('message',function(e){if(e.data&&e.data.id==='mtp-dfly2'&&e.data.mtpH&&e.source===f.contentWindow){f.style.height=e.data.mtpH+'px';}});})(); 

 DFly2 benchmarks: acceptance, speedup and throughput 

 All numbers below are self-reported by Tencent. Baselines are DFlash and DSpark retrained on the same recipe. 

 Average accepted length (τ), general workloads, temp 0 / temp 1: 

 Target DFlash DSpark DFly2 DeepSeek-V4.1-Flash 3.65 / 3.28 3.81 / 3.51 4.12 / 3.88 GLM-5.3-Flash 3.43 / 3.07 3.68 / 3.35 3.96 / 3.69 Hy4 flash 3.58 / 3.48 3.81 / 3.73 3.96 / 3.95 

 The margin over the stronger baseline is 3.9% to 10.5% on general workloads. It rises to 10.0% to 31.5% on long-context and agentic workloads up to 128K. On agentic sets, DFly2’s average stays within 4% of its general average. DSpark’s falls by 11% to 21%. 

 End-to-end speedup (greedy, concurrency 1): 2.97x on DeepSeek-V4.1-Flash, 2.36x on GLM-5.3-Flash, 3.19x on Hy4 flash. 

 Serving throughput on DeepSeek-V4.1-Flash, matched per-user decode speed vs DSpark: 

 +28% on short text 

 +62% on CodeSpan 64K 

 +81% on SWE 64K 

 At matched throughput, each user decodes 15% to 24% faster. 

 Tencent’s announcement adds 3 figures for Hy4 flash agentic tasks. It claims up to 4.2x faster decoding and about 30% over same-recipe DSpark. It also claims 10.4% more accepted tokens than open-source DSpark. 

 DFly2 vs DSpark vs DFlash 

 Feature DFly2 (Tencent) DSpark (DeepSeek) DFlash (z-lab) Drafting style Block-parallel, sparsity-sharing ( paper ) Semi-autoregressive, confidence-scheduled verification ( paper ) Block diffusion ( paper ) Own draft KV cache No ( README ) Yes (per DFly2 paper ) Yes (per DFly2 paper ) τ, DeepSeek-V4.1-Flash, temp 0 4.12 3.81 3.65 End-to-end speedup, DeepSeek-V4.1-Flash 2.97x 2.80x 2.82x Own headline claim +81% throughput at 64K ( paper ) 60% to 85% faster per user vs MTP-1 on V4-Flash ( The Batch ) Over 6x lossless acceleration ( paper ) License AngelSpec License; Hy4 flash under Tencent Hy License MIT ( The Batch ) Not disclosed 

 How do you deploy DFly2? 

 DFly2 ships inside tencent/Hy4-flash , a 220B-total, roughly 12B-active MoE with 1M context. vLLM serves it with the dfly speculative method via vllm/vllm-openai:hy4-flash . SGLang uses the DFLY algorithm via lmsysorg/sglang:hy4-flash . In the vLLM recipe , DFly speculative decoding is on by default. 

 To train DFly2 for your own sparse model, use AngelSpec . Its quick start expects 1 node with 8 GPUs (4 inference, 4 training). 

 Key Takeaways 

 DFly2 reuses the target’s sparse KV cache and indexer picks: zero extra draft KV memory. 

 Up to 81% more throughput on DeepSeek-V4.1-Flash at 64K, at matched per-user speed. 

 Beats same-recipe DSpark by 10.0% to 31.5% on long-context and agentic acceptance. 

 Smallest win: 3.9% on Hy4 flash general tasks. 

 Ships in Hy4 flash on vLLM and SGLang; train your own with AngelSpec. 

 Check out the the paper , grab the code , and get Hy4 flash weights . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target’s Sparse KV Cache appeared first on MarkTechPost .
