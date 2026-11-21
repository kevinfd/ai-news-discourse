---
id: "8f6696f8d5615a27"
title: "NVIDIA AI Releases Nemotron-Labs-Sigma, a Continuous Diffusion Language Model with 14 checkpoints at 3B/8B"
url: "https://marktechpost.com/2026/11/20/nvidia-nemotron-labs-sigma-continuous-diffusion-language-model"
link: "https://marktechpost.com/2026/11/20/nvidia-nemotron-labs-sigma-continuous-diffusion-language-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T14:44:52Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "NVIDIA has released Nemotron-Labs-Sigma , a collection of 14 open checkpoints at 3B and 8B scale. Nemotron-Labs-Sigma is a continuous diffusion language model family that denoises text in a 16-D embedding space. Most diffusion LLMs, such as LLaDA and Dream, work on discrete tokens. Sigma works in a smooth latent space instead. NVIDIA team states that this makes few-step distillation and…"
tags: ["Agentic AI", "AI Infrastructure", "AI Paper Summary", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "Machine Learning"]
orgs: ["Nvidia"]
topics: ["models & research", "chips & infrastructure"]
content_source: "summary"
word_count: 1584
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# NVIDIA AI Releases Nemotron-Labs-Sigma, a Continuous Diffusion Language Model with 14 checkpoints at 3B/8B

MarkTechPost · Asif Razzaq · 2026-11-20

NVIDIA has released Nemotron-Labs-Sigma , a collection of 14 open checkpoints at 3B and 8B scale. Nemotron-Labs-Sigma is a continuous diffusion language model family that denoises text in a 16-D embedding space. Most diffusion LLMs, such as LLaDA and Dream, work on discrete tokens. Sigma works in a smooth latent space instead. NVIDIA team states that this makes few-step distillation and trajectory steering practical for text. 

 TL;DR 

 Size: 3B and 8B parameters, 14 checkpoints. Context is 4,096 tokens (8,192 for Sigma-8B-instruct). 

 Runs on: 1 NVIDIA GPU in bfloat16 (Ampere, Lovelace, Hopper, Blackwell). About 120 to 140 tokens/s on 1 H100. No CPU support, no quantized variants listed. 

 Performance: Sigma-8B base averages 71.16 on NVIDIA’s 6-task suite, ahead of NLD-8B (70.22). 

 Best: 91.96 on GSM8K (Sigma-8B-instruct, 256 DDPM steps). 

 Worst: 17.00 on AIME25 (same model and sampler). 

 Bottom line: Best: the 8-step distilled 8B keeps a 70.34 average. Worst: the instruct average (59.14) trails NLD-8B (59.92). 

 What is Nemotron-Labs-Sigma? 

 The research team calls Sigma the first large-scale family of continuous diffusion language models. The collection has 4 variant types at each size: 

 Base: Sigma-3B and Sigma-8B. 

 Instruct: Sigma-3B-instruct and Sigma-8B-instruct. 

 Few-step distilled: distill-3B and distill-8B at NFE 2, 4, 8 and 16 (8 checkpoints). 

 Self-speculative: distill-spec-3B and distill-spec-8B. 

 How does continuous diffusion for language work? 

 Each token maps to a point in a learned 16-D embedding space . Training adds Gaussian noise to these embeddings and teaches the model to remove it. The embedding geometry is learned jointly with the denoiser. 

 Generation runs blockwise. Each denoised block is committed to a KV cache before the next starts. Blocks default to 64 tokens. 

 The backbone is a Ministral-style decoder-only Transformer with grouped-query attention, SwiGLU and rotary embeddings. Training starts from an autoregressive warm start of about 1T tokens. About 0.3T tokens of diffusion training follow. 

 At inference, classifier-free guidance and score temperature matter most. The model card page recommends guidance 3 and temperature 0.3 at 32 DDIM steps. 

 Why does a continuous space matter? 

 Discrete diffusion jumps between token states, so its trajectories are hard to steer. Sigma follows smooth ODE/SDE paths instead. Per the research paper , these degrade gracefully at low step counts and distill efficiently. Embedding-space steering also tunes the quality-diversity trade-off for pass@k sampling. 

 How does Sigma perform on benchmarks? 

 On the research’s 6-task base suite, Sigma-8B with 256 DDPM steps averages 71.16. NLD-8B in diffusion mode scores 70.22, Dream-7B 58.74 and LLaDA-8B 41.78. Qwen3-8B in AR mode scores 68.91. A cheaper 32-step DDIM sampler still gives Sigma-8B a 70.18 average. 

 Coding is the standout. Sigma-8B scores 65.12 on HumanEval versus 62.80 for NLD-8B. MBPP is weaker, at 65.74 versus 67.00. 

 After SFT, Sigma-8B-instruct scores 91.96 on GSM8K, 78.40 on MATH-500 and 82.50 on HumanEval. Hard reasoning stays limited, at 23.33 on AIME24 and 17.00 on AIME25. Its 10-task average of 59.14 sits just below NLD-8B at 59.92. All scores are NVIDIA’s own evaluations. 

 Back</button><button class="b on" id="sg-next">Next step </button><button class="b" id="sg-play">Auto-play</button></div>
</div>

<div class="pn" id="p-bench">
<div class="ctl">
<button class="b on" data-m="avg">Base 6-task avg</button>
<button class="b" data-m="gsm">GSM8K</button>
<button class="b" data-m="he">HumanEval</button>
<button class="b" data-m="mbpp">MBPP</button>
<button class="b" data-m="ins">Instruct 10-task avg</button>
</div>
<div class="bars" id="bn-bars"></div>
<p class="note" id="bn-note"></p>
</div>

<div class="pn" id="p-few">
<div class="grid2">
<div class="box">
<div class="lbl">Distilled checkpoint (native NFE, 32-token block)</div>
<div class="ctl" id="nf-btns"><button class="b" data-n="2">nfe2</button><button class="b" data-n="4">nfe4</button><button class="b on" data-n="8">nfe8</button><button class="b" data-n="16">nfe16</button></div>
<div style="display:flex;gap:22px;margin-top:14px">
<div><div class="big" id="nf-tpf">4</div><div class="lbl">tokens per forward</div></div>
<div><div class="big" id="nf-n" style="color:#fff">8</div><div class="lbl">denoiser calls / block (+1 readout)</div></div>
</div>
<div class="blk" id="nf-blk"></div>
<p class="note" id="nf-note"></p>
</div>
<div class="box">
<div class="lbl">Base model sampler settings (DDIM, 32-token blocks)</div>
<table><tr><th>Steps</th><th>Guidance</th><th>Score temp</th></tr>
<tr><td>32</td><td>3</td><td>0.3</td></tr><tr><td>16</td><td>3</td><td>0.4</td></tr><tr><td>8</td><td>3</td><td>0.6</td></tr><tr><td>4</td><td>2</td><td>0.8</td></tr></table>
<p class="note">Base quality drops noticeably below about 16 steps. NVIDIA recommends the distilled checkpoints for few-step generation.</p>
</div>
</div>
</div>

<div class="pn" id="p-speed">
<p class="desc" style="margin:0;font-size:13.5px;line-height:1.5">A diffusion head drafts a 32-token block. The model's own AR head verifies it, so output exactly matches greedy AR decoding.</p>
<div class="bars" id="sp-bars"></div>
<div class="box" style="margin-top:14px">
<div class="lbl">Acceptance-length gain over NLD-8B base (Sigma-distill-spec-8B)</div>
<div class="bars" id="al-bars"></div>
</div>
<p class="note">1 NVIDIA GB200, BF16, SGLang, 1 request at a time. Self-reported by NVIDIA (arXiv:2610.02665).</p>
</div>

<div class="pn" id="p-ckpt">
<div class="ctl"><button class="b on" data-f="all">All 14</button><button class="b" data-f="3B">3B</button><button class="b" data-f="8B">8B</button></div>
<div class="chips" id="ck-list"></div>
<p class="note">Base context 4,096 tokens (8B-instruct: 8,192). NVIDIA Nemotron Open Model License. CUDA GPU in bfloat16 required, no CPU.</p>
</div>

<div class="ft"><span>Sources: arXiv:2610.02665, Hugging Face model cards. Benchmarks self-reported by NVIDIA.</span><b>Built by Marktechpost</b></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-sigma');
function q(s){return R.querySelectorAll(s)}
function rs(){try{parent.postMessage({mtpSigmaH:R.offsetHeight+40},'*')}catch(e){}}
q('.tab').forEach(function(t){t.addEventListener('click',function(){q('.tab').forEach(function(x){x.classList.remove('on')});q('.pn').forEach(function(x){x.classList.remove('on')});t.classList.add('on');document.getElementById('p-'+t.dataset.t).classList.add('on');if(t.dataset.t==='bench')bench(cur);if(t.dataset.t==='speed')speed();setTimeout(rs,60);setTimeout(rs,600)})});
/* how it works */
var D=[
{h:'1. Autoregressive warm start',p:['Sigma starts from autoregressive weights trained on about 1T tokens.','The backbone is a Ministral-style decoder: grouped-query attention, SwiGLU, rotary embeddings.']},
{h:'2. Corrupt embeddings with Gaussian noise',p:['Each token maps to a point in a learned 16-D embedding space.','Training adds Gaussian noise and learns to remove it, about 0.3T tokens of diffusion training.']},
{h:'3. Denoise one block at a time',p:['Blocks default to 64 tokens. Finished blocks go into a KV cache.','Trajectories are smooth ODE/SDE paths, so they distill to few steps.']},
{h:'4. Steer at inference',p:['Classifier-free guidance and score temperature control quality and diversity.','Recommended: guidance 3, temperature 0.3 at 32 DDIM steps.']}];
var N=18,pts=[],S=0,timer=null;
for(var i=0;i<N;i++){var cx=20+(i%6)*44,cy=30+Math.floor(i/6)*55;pts.push({cx:cx,cy:cy,nx:10+Math.random()*240,ny:10+Math.random()*150})}
var g=document.getElementById('sg-dots'),ns='http://www.w3.org/2000/svg';
pts.forEach(function(p){var c=document.createElementNS(ns,'circle');c.setAttribute('r',6);c.setAttribute('class','dot');g.appendChild(c);p.el=c});
function draw(){
q('.st').forEach(function(x){x.classList.toggle('on',+x.dataset.s===S)});
var d=D[S];document.getElementById('sg-desc').innerHTML='<h3>'+d.h+'</h3><p>'+d.p.join('</p><p>')+'</p>';
pts.forEach(function(p,i){var x,y,f='#3a3a3a',o=1;
if(S===0){x=p.cx;y=p.cy;f='#555'}
else if(S===1){x=p.nx;y=p.ny;f='#8a8a8a'}
else if(S===2){var done=i<6;x=done?p.cx:p.nx;y=done?p.cy:p.ny;f=done?'#76B900':'#8a8a8a'}
else{x=p.cx+(i%2?3:-3);y=p.cy;f='#76B900'}
p.el.setAttribute('cx',x);p.el.setAttribute('cy',y);p.el.setAttribute('fill',f);p.el.style.opacity=o});
setTimeout(rs,50)}
q('.st').forEach(function(x){x.addEventListener('click',function(){S=+x.dataset.s;draw()})});
document.getElementById('sg-next').onclick=function(){S=(S+1)%4;draw()};
document.getElementById('sg-prev').onclick=function(){S=(S+3)%4;draw()};
document.getElementById('sg-play').onclick=function(){var b=this;if(timer){clearInterval(timer);timer=null;b.textContent='Auto-play';b.classList.remove('on')}else{timer=setInterval(function(){S=(S+1)%4;draw()},1800);b.textContent='Pause';b.classList.add('on')}};
draw();
/* benchmarks */
var M=['Sigma-8B','NLD-8B','Qwen3-8B (AR)','Dream-7B','LLaDA-8B'];
var B={avg:[71.16,70.22,68.91,58.74,41.78],gsm:[88.57,87.26,86.73,77.18,70.96],he:[65.12,62.80,64.63,54.88,32.32],mbpp:[65.74,67.00,69.40,56.80,40.80],ins:[59.14,59.92,null,40.54,37.24]};
var NT={avg:'Base models, pass@1. Sigma-8B uses 256 DDPM steps. NLD, Dream and LLaDA in diffusion mode. Paper Table 2.',gsm:'GSM8K pass@1, base models. Paper Table 2.',he:'HumanEval pass@1, base models. Paper Table 2.',mbpp:'MBPP pass@1, base models. Sigma-8B trails NLD-8B and Qwen3-8B here. Paper Table 2.',ins:'Instruct models, 10-task average (GSM8K, MATH-500, AIME24/25, HumanEval, MBPP, LCB-CPP, MMLU, GPQA, IFEval). Diffusion mode. Qwen3-8B not in this row set. Paper Table 5.'};
var cur='avg';
function bench(k){cur=k;var box=document.getElementById('bn-bars');box.innerHTML='';
M.forEach(function(m,i){var v=B[k][i];if(v===null)return;var r=document.createElement('div');r.className='row';r.innerHTML='<span>'+m+'</span><div class="tr"><div class="fl'+(i===0?' s':'')+'"></div></div><span class="v">'+v.toFixed(2)+'</span>';box.appendChild(r);var f=r.querySelector('.fl');requestAnimationFrame(function(){requestAnimationFrame(function(){f.style.width=v+'%'})})});
document.getElementById('bn-note').textContent=NT[k]+' Self-reported by NVIDIA.';
q('#p-bench .b').forEach(function(b){b.classList.toggle('on',b.dataset.m===k)});setTimeout(rs,60)}
q('#p-bench .b').forEach(function(b){b.addEventListener('click',function(){bench(b.dataset.m)})});
bench('avg');
/* few-step */
function few(n){document.getElementById('nf-tpf').textContent=32/n;document.getElementById('nf-n').textContent=n;
var bk=document.getElementById('nf-blk');bk.innerHTML='';for(var i=0;i<32;i++){var t=document.createElement('div');t.className='tk';bk.appendChild(t)}
var tks=bk.children,step=32/n,k=0;(function lit(){if(k>=n)return;for(var j=k*step;j<(k+1)*step;j++)tks[j].classList.add('lit');k++;setTimeout(lit,n>8?90:220)})();
document.getElementById('nf-note').textContent=n===8?'Sigma-distill-8B-nfe8 card: 6-task mean 70.34, GSM8K 88.44, HumanEval 65.18, MBPP 62.60 (10 seeds).':'Tokens per forward = 32-token block / NFE. Per-checkpoint scores for nfe'+n+' are on its model card.';
q('#nf-btns .b').forEach(function(b){b.classList.toggle('on',+b.dataset.n===n)});setTimeout(rs,60)}
q('#nf-btns .b').forEach(function(b){b.addEventListener('click',function(){few(+b.dataset.n)})});
few(8);
/* speed */
function bars(id,rows,max,suf){var box=document.getElementById(id);box.innerHTML='';rows.forEach(function(r){var e=document.createElement('div');e.className='row';e.innerHTML='<span>'+r[0]+'</span><div class="tr"><div class="fl'+(r[2]?' s':'')+'"></div></div><span class="v">'+r[1].toFixed(r[3])+suf+'</span>';box.appendChild(e);var f=e.querySelector('.fl');requestAnimationFrame(function(){requestAnimationFrame(function(){f.style.width=(r[1]/max*100)+'%'})})})}
function speed(){bars('sp-bars',[['Sigma-8B avg',3.46,1,2],['NLD-8B avg',3.04,0,2],['Sigma-8B peak',4.20,1,2],['Sigma-3B peak',3.18,1,2],['AR decoding',1.00,0,2]],4.5,'x');
bars('al-bars',[['GSM8K',33.0,1,1],['MBPP',22.7,1,1],['HumanEval',21.0,1,1]],40,'%');setTimeout(rs,60)}
/* checkpoints */
var C=[['Nemotron-Labs-Sigma-3B','Base'],['Nemotron-Labs-Sigma-3B-instruct','Instruct'],['Nemotron-Labs-Sigma-8B','Base'],['Nemotron-Labs-Sigma-8B-instruct','Instruct'],['Nemotron-Labs-Sigma-distill-3B-nfe2','2 NFE'],['Nemotron-Labs-Sigma-distill-3B-nfe4','4 NFE'],['Nemotron-Labs-Sigma-distill-3B-nfe8','8 NFE'],['Nemotron-Labs-Sigma-distill-3B-nfe16','16 NFE'],['Nemotron-Labs-Sigma-distill-spec-3B','Self-spec'],['Nemotron-Labs-Sigma-distill-8B-nfe2','2 NFE'],['Nemotron-Labs-Sigma-distill-8B-nfe4','4 NFE'],['Nemotron-Labs-Sigma-distill-8B-nfe8','8 NFE'],['Nemotron-Labs-Sigma-distill-8B-nfe16','16 NFE'],['Nemotron-Labs-Sigma-distill-spec-8B','Self-spec']];
function ck(f){var l=document.getElementById('ck-list');l.innerHTML='';C.forEach(function(c){if(f!=='all'&&c[0].indexOf(f)<0)return;var a=document.createElement('a');a.className='chip';a.href='https://huggingface.co/nvidia/'+c[0];a.target='_blank';a.rel='noopener';a.innerHTML='<span>'+c[0].replace('Nemotron-Labs-','')+'</span><em>'+c[1]+'</em>';l.appendChild(a)});
q('#p-ckpt .b').forEach(function(b){b.classList.toggle('on',b.dataset.f===f)});setTimeout(rs,60)}
q('#p-ckpt .b').forEach(function(b){b.addEventListener('click',function(){ck(b.dataset.f)})});
ck('all');
window.addEventListener('load',rs);window.addEventListener('resize',rs);setTimeout(rs,300);
})();
</script>
</body></html>
"> 

window.addEventListener('message',function(ev){if(ev.data&&ev.data.mtpSigmaH){var f=document.getElementById('mtp-sigma-frame');if(f&&ev.source===f.contentWindow){f.style.height=ev.data.mtpSigmaH+'px';}}});

 How fast are the distilled and speculative checkpoints? 

 Sigma-distill-8B-nfe8 decodes each 32-token block in 8 denoiser calls plus 1 readout. Its card reports a 6-task mean of 70.34, with 88.44 on GSM8K and 65.18 on HumanEval. That is close to the 256-step teacher. 

 NVIDIA’s launch thread frames the gain as 8 tokens per forward on math and 4 on code. 

 The distill-spec checkpoints add self-speculative decoding. A diffusion head drafts a 32-token block, and the model’s own AR head verifies it. Output exactly matches greedy AR decoding. On 1 GB200 with SGLang, the 8B spec model runs 3.46x faster than AR decoding on average. NLD-8B reaches 3.04x on the same setup. Peak speedups reach 4.20x at 8B and 3.18x at 3B. 

 How do you deploy Nemotron-Labs-Sigma? 

 All 14 checkpoints are on Hugging Face under the NVIDIA Nemotron Open Model License. The cards state the models are ready for commercial use. You need a CUDA GPU in bfloat16: Ampere, Lovelace, Hopper or Blackwell. CPU inference is not supported. 

 Loading needs PyTorch 2.4+, Transformers 4.55+ and trust_remote_code . On 1 H100, the base model generates about 120 to 140 tokens/s. The distilled card lists vLLM, SGLang and Docker Model Runner for serving. NVIDIA hosts no API. 

 How does Sigma compare with other 8B diffusion and AR models? 

 Benchmark rows use NVIDIA’s evaluations from the Sigma paper (Table 2 base, Table 5 instruct). Specs come from each model’s own card. 

 Feature Sigma-8B NLD-8B Dream-7B LLaDA-8B Qwen3-8B Generation Continuous diffusion (16-D) Discrete diffusion, AR, self-spec Discrete diffusion Discrete diffusion Autoregressive Parameters 8B 8B 7B (card lists 8B) 8B 8.2B Context 4,096 (instruct 8,192) Not disclosed Not disclosed Not disclosed 32,768 (131,072 YaRN) License NVIDIA Nemotron Open Model NVIDIA Nemotron Open Model Apache 2.0 MIT Apache 2.0 Hardware NVIDIA GPU, bf16, no CPU NVIDIA GPU (tested DGX Spark, GB200) Not disclosed Not disclosed Not disclosed Base 6-task avg 71.16 70.22 58.74 41.78 68.91 (AR) GSM8K 88.57 87.26 77.18 70.96 86.73 HumanEval 65.12 62.80 54.88 32.32 64.63 MBPP 65.74 67.00 56.80 40.80 69.40 Instruct 10-task avg 59.14 59.92 40.54 37.24 Not disclosed Availability Open weights, HF Open weights, HF Open weights, HF Open weights, HF Open weights, HF 

 Key Takeaways 

 Sigma moves language diffusion into a learned 16-D continuous embedding space. 

 14 open checkpoints: 3B and 8B base, instruct, distilled and speculative. 

 Sigma-8B base averages 71.16, ahead of NLD-8B at 70.22. 

 Self-speculative 8B decodes 3.46x faster than AR on average. 

 Weak spots: 17.00 on AIME25, 4,096-token base context, GPU only. 

 Check out the Paper , Model Collection and Project Page . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post NVIDIA AI Releases Nemotron-Labs-Sigma, a Continuous Diffusion Language Model with 14 checkpoints at 3B/8B appeared first on MarkTechPost .
