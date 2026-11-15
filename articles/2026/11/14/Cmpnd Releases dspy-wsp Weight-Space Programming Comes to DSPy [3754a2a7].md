---
id: "3754a2a7dd164e73"
title: "Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy"
url: "https://marktechpost.com/2026/11/14/cmpnd-dspy-wsp-weight-space-programming"
link: "https://marktechpost.com/2026/11/14/cmpnd-dspy-wsp-weight-space-programming"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-14T16:45:48Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Cmpnd has released dspy-wsp , a prototype optimizer that brings weight-space programming to DSPy . Weight-space programming is a technique in which a frontier LLM reads another model’s weights and edits them directly. There are no gradients, no training loop and no fine-tuning dataset. dspy-wsp packages this as WeightSpace , an optimizer that plugs into any DSPy program and metric. In Cmpnd’s…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Deep Learning", "Editors Pick", "For Devs", "Language Model", "Machine Learning", "New Releases", "Python"]
orgs: ["OpenAI"]
topics: ["models & research", "jobs & society", "agents & coding", "policy & regulation"]
content_source: "summary"
word_count: 2415
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy

MarkTechPost · Asif Razzaq · 2026-11-14

Cmpnd has released dspy-wsp , a prototype optimizer that brings weight-space programming to DSPy . Weight-space programming is a technique in which a frontier LLM reads another model’s weights and edits them directly. There are no gradients, no training loop and no fine-tuning dataset. dspy-wsp packages this as WeightSpace , an optimizer that plugs into any DSPy program and metric. In Cmpnd’s tests, about $5 to $10 of GPT-6-Astra calls improved every decision model they tried. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 What it is: A DSPy optimizer ( WeightSpace ) where a writer LLM edits a student model’s weights. MIT license, pip install dspy-wsp , needs DSPy 3.5. 

 Size: Tested on open decision models from 0.6B to 9B parameters. One 25-pass run edited a single layer or head. 

 Runs on: One Mac for all experiments. 2B models used about 6 GB of memory. d1-omni-600M needs 4 GB or more (Mac or GPU). 

 Performance: WeightSpace alone added 1.9 to 16.1 points on Typed Decisions. With ReAnchor, gains were 6.5 to 20.0 points. 

 Best: d1-omni-600M rose from 50.9% to 69.1% (+18.3) with WeightSpace + ReAnchor. 

 Worst: Clef-Flash (9B) gained only +1.9 from WeightSpace alone. With the original paper’s stricter rule, d1-omni-600M gained just +2.8. 

 Bottom line: Best: a cheap, gradient-free edit that ships as a small, verifiable patch. Worst: very experimental, slow (78 to 167 minutes per run) and weakest on larger models. 

 What is weight-space programming? 

 Weight-space programming (WSP) treats a neural network’s weights as a program that can be read and rewritten. The idea comes from MIT research: Sparks of Weight-Space Programming . 

 A frontier model (the research team used GPT-6-Astra) looks at weight tensors, reasons about what each part computes, and changes them to match a goal written in plain English. The research team stresses that WSP names an emerging capability, not a fixed method. Gradients were banned in their experiments, but the concept does not rule them out. 

 How is it different from fine-tuning or prompt optimization? 

 It helps to compare the 3 levers developers usually pull: 

 Prompt optimization (DSPy’s MIPROv2, GEPA ) edits text: instructions and examples. The model’s weights never change. 

 Fine-tuning (DSPy’s BootstrapFinetune, used inside BetterTogether ) changes weights with gradient descent. It needs training data, a training loop and usually a GPU. 

 Weight-space programming changes weights by reasoning. The editor forms a hypothesis (“these neurons over-score option B”), writes code to patch them, and checks the result with a few forward passes. 

 The research post frames WSP as the next step after using LLMs to optimize text artifacts. Earlier work let LLMs hill-climb on prompts, harnesses and training code. Weights were left to Adam or to trained weight-generating networks. WSP argues LLM reasoning can now reach the weights directly. 

 What did the original research show? 

 The MIT team ran 9 experiments. Several are striking: 

 Reading weights: Astra named the correct game (Breakout, Pong, Pac-Man, Freeway) for 4 PPO policy networks from weights alone. 

 Fixing a broken policy: A Kinetix car-on-ramp policy failed all 256 episodes. One edit to 3.5% of its weights made it succeed in all 1,024 test episodes. 

 Writing from zero: On MinAtar Breakout, a zero-initialized network written in 1 shot scored 517.4. PPO reached 25.3 after 500M steps. 

 Fixing an LLM: Qwen3.5-0.8B looped on math problems. Astra traced the issue to MLP layers 15 and 19 and changed 131,072 weights (0.016% of the model). With 50 forward passes, MATH-500 rose from 7.9% to 48.1% and GSM8K from 13.8% to 67.1%. 

 The research also shows limits. On Gemma 3 270M, edits moved MATH-500 from 6.8% to between 7.0% and 7.7%. The research team did not count that as a real gain. Editing can remove an obstacle, but it could not add a missing ability. 

 How does dspy-wsp work? 

 dspy-wsp turns that research loop into a standard DSPy optimizer. The GitHub Repo describes 3 actors: 

 The student: the small model your DSPy program runs on. Its weights load into a local Python process. 

 The writer: a frontier LLM, recommended as gpt-6-astra at maximum reasoning effort. 

 The sandbox: a kernel where the writer runs code. macOS uses built-in sandbox-exec ; Linux uses bubblewrap. 

 The writer works in turns. Each turn has a short explanation, then 1 code block. That block is either: 

 a Python block that reads or edits weights inside the sandbox, or 

 a forward block that runs your DSPy program on practice examples. 

 Forward passes come from a fixed budget ( max_passes=25 in the tests). When the budget runs out, the writer’s best edit becomes the patch. A hidden validation set then compares original and edited weights on the same examples and seeds. 

 What data does the writer see? 

 The repo is explicit about data separation: 

 trainset is the writer’s practice set. 

 holdout moves a fraction (0.25 in the example) of training data into a check set. The writer can score edits on it but never sees the examples. 

 valset stays hidden and runs once at the end. 

 Metrics can return dspy.Prediction(score=..., feedback=...) . The feedback text is visible to the writer. 

 What did the writer actually change? 

 The results write-up lists every edit. The edits are small and targeted: 

 Model Tensor edited Scope Time Writer cost d1-omni-600M head.scorer.1.weight (+ bias, scorer.3.weight ) 112,640 of 1,048,576 entries, plus 220 78 min $7.63 NanoJev (Qwen3-0.6B) scalar.weight 1,024 entries 167 min $6.92 d1-2B layers.23.feed_forward.w2.weight All 15.7M entries, rank-9 change 83 min $5.42 

 d1-2B has no decision head, so the writer edited its backbone at layer 23. On d1-omni-600M, the writer rewrote part of the decision head’s scorer. 

 What does the code look like? 

 The Repo example triages support tickets. The signature uses only decision-type outputs: 

 Copy Code Copied Use a different Browser import dspy
from typing import Literal
from dspy_wsp import WeightSpace, load_decision_backend

class Triage(dspy.Signature):
 """Triage a support ticket."""
 ticket: str = dspy.InputField()
 urgent: bool = dspy.OutputField(desc="Does this ticket need a reply today?")
 team: Literal["billing", "technical", "account"] = dspy.OutputField(desc="Which team should handle it?")

backend = load_decision_backend("d1") # d1-omni-600M
optimizer = WeightSpace(
 metric=metric,
 writer_lm=dspy.LM("openai/gpt-6-astra", model_type="responses", reasoning_effort="max"),
 backend=backend,
 max_passes=25,
 holdout=0.25,
 run_dir="runs/triage",
)
compiled = optimizer.compile(dspy.Predict(Triage), trainset=train, valset=test)
compiled(ticket="I was charged twice this month.") # runs on the edited weights 

 After compile , the program calls the edited local model instead of a hosted API. compiled.wsp_patch.summary() shows what changed. 

 Auto-play</button></div>
 </div>

 <!-- 3 edits -->
 <div class="pn" data-p="2">
 <p class="lbl">Tensor the writer edited (GPT-6-Astra, 25 passes)</p>
 <div class="row" id="edb">
 <button class="btn on" data-e="0">d1-omni-600M</button>
 <button class="btn" data-e="1">NanoJev</button>
 <button class="btn" data-e="2">d1-2B</button>
 </div>
 <div class="card" style="margin-top:12px">
 <div style="font-size:13px"><code id="edt"></code></div>
 <p id="edd" style="margin-bottom:0"></p>
 <div class="mat" id="mat"></div>
 </div>
 <div class="kv">
 <div><b id="k1"></b><span>Entries changed</span></div>
 <div><b id="k2"></b><span>Writer turns</span></div>
 <div><b id="k3"></b><span>Runtime</span></div>
 <div><b id="k4"></b><span>Writer cost</span></div>
 </div>
 <p class="note">Grid is illustrative of share edited, not exact positions. Source: dspy-wsp results README (2026-11-07).</p>
 </div>

 <!-- 4 results -->
 <div class="pn" data-p="3">
 <p class="lbl">Typed Decisions test accuracy (400 held-out cases)</p>
 <div class="row" id="rsb">
 <button class="btn on" data-r="0">d1-omni-600M</button>
 <button class="btn" data-r="1">NanoJev 0.6B</button>
 <button class="btn" data-r="2">d1-2B</button>
 <button class="btn" data-r="3">Clef-Flash 9B</button>
 </div>
 <div class="bars" id="bars"></div>
 <p class="note">Writer GPT-6-Astra, 25 forward passes. Gains are paired, ±0.7 to 1.4 pts SE. Self-reported by Cmpnd.</p>
 </div>

 <!-- 5 cost -->
 <div class="pn" data-p="4">
 <div class="kv" style="margin-top:0">
 <div><b>$5.42 to $7.63</b><span>Writer cost / run</span></div>
 <div><b>78 to 167 min</b><span>Runtime / run</span></div>
 <div><b>~6 GB</b><span>Memory, 2B model</span></div>
 <div><b>MIT</b><span>License</span></div>
 </div>
 <div class="card" style="margin-top:12px">
 <p class="lbl">Ship the patch</p>
 <p><code>pip install dspy-wsp</code> (DSPy 3.5, Python 3.10+)</p>
 <p>Patch = <code>manifest.json</code> + <code>edit.npz</code> with sha256 hashes of base and edited tensors, so anyone with the public base model rebuilds the exact weights.</p>
 <p>Decision models: <code>wsp_patch.write_checkpoint(...)</code> · LLMs: <code>dspy-wsp apply</code>, then serve on vLLM.</p>
 <p style="margin-bottom:0">Runs locally: MLX on Apple silicon, PyTorch on Linux (NVIDIA GPU if present).</p>
 </div>
 <p class="note">Caveat: Cmpnd calls the package "very experimental." Under the paper's stricter rule, d1-omni-600M gained only +2.8.</p>
 </div>

 <div class="ft"><span>Sources: cmpnd.ai, github.com/cmpnd-ai/dspy-wsp, rikiyat.github.io</span><a href="https://www.marktechpost.com" target="_blank" rel="noopener">Built by Marktechpost</a></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-wsp');
function q(s){return R.querySelector(s)} function qa(s){return R.querySelectorAll(s)}
function post(){try{parent.postMessage({mtpWspH:R.offsetHeight+40},'*')}catch(e){}}
qa('.tab').forEach(function(t){t.onclick=function(){qa('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');qa('.pn').forEach(function(p){p.classList.toggle('on',p.dataset.p===t.dataset.t)});if(t.dataset.t==='3')drawBars(rc);setTimeout(post,60)}});
/* levers */
var wg=q('#wg');for(var i=0;i<64;i++){var c=document.createElement('i');wg.appendChild(c)}
var cells=wg.children;
var L=[
{p:1,w:0,t:'<b>Prompt optimization</b> (MIPROv2, GEPA) rewrites instructions and examples. Weights never move.',g:['Edits text','No GPU needed'],n:['Weights frozen']},
{p:0,w:1,t:'<b>Fine-tuning</b> (BootstrapFinetune) nudges many weights with gradient descent on training traces.',g:['Changes weights'],n:['Needs gradients','Needs a training loop']},
{p:0,w:2,t:'<b>Weight-space programming</b>: a frontier LLM reads tensors, forms a hypothesis about what they compute, writes code to patch a few, then tests the edit with a forward pass.',g:['Changes weights','No gradients','Targeted, hashed patch'],n:['Needs a strong writer LLM']}
];
function lever(k){qa('#levb .btn').forEach(function(b){b.classList.toggle('on',+b.dataset.l===k)});var d=L[k];
q('#bx-p').classList.toggle('hot',d.p===1);q('#bx-w').classList.toggle('hot',d.w>0);q('#pchg').className=d.p?'chg':'';
for(var i=0;i<cells.length;i++){cells[i].className=''}
if(d.w===1){var n=0;var iv=setInterval(function(){for(var j=0;j<cells.length;j++){cells[j].className=Math.random()<.7?'b':''}if(++n>5)clearInterval(iv)},140)}
if(d.w===2){[19,20,27,28].forEach(function(x,ix){setTimeout(function(){cells[x].className='a'},200+ix*180)})}
q('#ldesc').innerHTML='<p style="margin-top:0">'+d.t+'</p><div class="tags">'+d.g.map(function(x){return '<span class="tg">'+x+'</span>'}).join('')+d.n.map(function(x){return '<span class="tg n">'+x+'</span>'}).join('')+'</div>';setTimeout(post,60)}
qa('#levb .btn').forEach(function(b){b.onclick=function(){lever(+b.dataset.l)}});lever(2);
/* loop */
var S=[
{b:25,t:'<span class="k">load_decision_backend("d1")</span>\n# student weights load into a local Python process\n# writer: gpt-6-astra, reasoning_effort="max"'},
{b:25,t:'<span class="k">```python</span> # runs in sandbox (sandbox-exec / bubblewrap)\nW = weights["head.scorer.1.weight"]\nprint(W.shape, W.std()) # read tensors like source code'},
{b:25,t:'# writer turn = short explanation + 1 code block\n"These scorer units push answers toward the wrong option.\n I will rescale them and check on practice examples."'},
{b:25,t:'<span class="k">```python</span>\nW[rows] *= scale # targeted edit, no gradients\n# change is recorded against the base tensor hash'},
{b:24,t:'<span class="k">```forward</span> # run the DSPy program on practice examples\n# score on holdout (writer sees scores, never examples)\n# keep the edit only if the metric improves'},
{b:0,t:'# budget spent: best edit becomes the patch\npatch/manifest.json + patch/edit.npz (sha256 hashed)\n# hidden valset compares original vs edited weights once'}
];
var cur=0,pl=null;
function step(k){cur=Math.max(0,Math.min(5,k));qa('.st').forEach(function(s){var i=+s.dataset.s;s.classList.toggle('on',i===cur);s.classList.toggle('done',i<cur)});
q('#term').innerHTML=S[cur].t;q('#budf').style.width=(S[cur].b/25*100)+'%';q('#budn').textContent=S[cur].b+' / 25';
if(cur===4){var b=24;var iv=setInterval(function(){b-=1;if(cur!==4||b<1){clearInterval(iv);return}q('#budf').style.width=(b/25*100)+'%';q('#budn').textContent=b+' / 25'},90)}}
qa('.st').forEach(function(s){s.onclick=function(){step(+s.dataset.s)}});
q('#next').onclick=function(){step(cur+1)};q('#prev').onclick=function(){step(cur-1)};
q('#play').onclick=function(){if(pl){clearInterval(pl);pl=null;q('#play').textContent=' Auto-play';return}step(0);q('#play').textContent='❚❚ Pause';pl=setInterval(function(){if(cur>=5){clearInterval(pl);pl=null;q('#play').textContent=' Auto-play';return}step(cur+1)},2200)};
step(0);
/* edits */
var E=[
{t:'head.scorer.1.weight (+ bias, scorer.3.weight)',d:'Rewrote part of the decision head scorer: 112,640 of 1,048,576 entries (about 10.7%), plus 220 bias/output entries.',k:['112,860','74','78 min','$7.63'],m:'a',f:0.107},
{t:'scalar.weight',d:'A single small tensor of 1,024 entries on the Qwen3-0.6B backbone with a decision head.',k:['1,024','68','167 min','$6.92'],m:'a',f:1},
{t:'layers.23.feed_forward.w2.weight',d:'d1-2B has no decision head, so the writer edited the backbone: all 15.7M entries changed, as a rank-9 update.',k:['15.7M','65','83 min','$5.42'],m:'r',f:1}
];
var mat=q('#mat');for(var i=0;i<200;i++){mat.appendChild(document.createElement('i'))}
function ed(k){qa('#edb .btn').forEach(function(b){b.classList.toggle('on',+b.dataset.e===k)});var e=E[k];q('#edt').textContent=e.t;q('#edd').textContent=e.d;
['k1','k2','k3','k4'].forEach(function(id,ix){q('#'+id).textContent=e.k[ix]});
var ms=mat.children,n=ms.length;for(var i=0;i<n;i++)ms[i].className='';
var on=k===1?20:Math.round(n*e.f);var idx=[];for(var i=0;i<n;i++)idx.push(i);
if(k===0){idx=idx.slice(0,on)}else if(k===1){idx=idx.slice(0,20)}
idx.forEach(function(x,j){setTimeout(function(){ms[x].className=e.m},j*(k===2?3:12))});setTimeout(post,60)}
qa('#edb .btn').forEach(function(b){b.onclick=function(){ed(+b.dataset.e)}});ed(0);
/* bars */
var D=[[50.9,60.2,66.9,69.1],[39.2,50.7,52.4,56.4],[60.6,70.1,74.0,77.9],[68.8,70.3,70.7,75.3]];
var N=['Unoptimized','ReAnchor','WeightSpace','WeightSpace + ReAnchor'],C=['#B0AAA6','#5B5452','#3A8A50','#1E4A2C'];
var bars=q('#bars');N.forEach(function(n,i){bars.insertAdjacentHTML('beforeend','<div class="br"><span>'+n+'</span><div class="trk"><div class="fill" style="background:'+C[i]+'"></div></div><span class="v"></span></div>')});
var G=[[0,9.3,16.1,18.3],[0,11.6,13.3,17.3],[0,9.5,13.4,17.3],[0,1.5,1.9,6.5]];
var rc=0;
function drawBars(k){rc=k;qa('#rsb .btn').forEach(function(b){b.classList.toggle('on',+b.dataset.r===k)});var r=qa('#bars .br');
r.forEach(function(row,i){var v=D[k][i];var f=row.querySelector('.fill');f.style.width='0';var g=i?' <small>+'+G[k][i].toFixed(1)+'</small>':'';row.querySelector('.v').innerHTML=v.toFixed(1)+'%'+g;setTimeout(function(){f.style.width=(v/85*100)+'%'},60+i*120)})}
qa('#rsb .btn').forEach(function(b){b.onclick=function(){drawBars(+b.dataset.r)}});drawBars(0);
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body></html>
"> 
 
 (function(){var f=document.getElementById("mtp-wsp-frame");window.addEventListener("message",function(e){if(e.data&&e.data.mtpWspH&&e.source===f.contentWindow){f.style.height=e.data.mtpWspH+"px";}});})(); 

 How well does it work? Typed Decisions benchmark results 

 Cmpnd tested on Typed Decisions , a benchmark for typed probabilistic decisions. A model reads 1 piece of unstructured state and answers 5 typed questions at once. Each answer is a probability distribution. The test split has 400 cases and 2,000 decisions. 

 Each model got 25 forward passes from GPT-6-Astra. Gains are paired, with a standard error of ±0.7 to 1.4 points. 

 Model Unoptimized ReAnchor WeightSpace WeightSpace + ReAnchor d1-omni-600M 50.9% 60.2% (+9.3) 66.9% (+16.1) 69.1% (+18.3) NanoJev (Qwen3-0.6B) 39.2% 50.7% (+11.6) 52.4% (+13.3) 56.4% (+17.3) d1-2B 60.6% 70.1% (+9.5) 74.0% (+13.4) 77.9% (+17.3) Clef-Flash (9B) 68.8% 70.3% (+1.5) 70.7% (+1.9) 75.3% (+6.5) 

 Sources: Cmpnd blog chart for d1-omni-600M, d1-2B and Clef-Flash; results README for NanoJev. 

 ReAnchor is an earlier Cmpnd optimizer. Decision models output probabilities, and thresholds turn those into answers. ReAnchor refits each question’s thresholds with no LLM calls. WeightSpace changes the model; ReAnchor recalibrates its output. The 2 stack well. 

 Three patterns stand out: 

 WeightSpace beat ReAnchor alone on every model shown. On d1-omni-600M, it added +16.1 versus +9.3. 

 The largest model gained least. The 9B Clef-Flash gained only +1.9 from WeightSpace alone. 

 The combination matters most at 9B. Clef-Flash jumped to +6.5 when both optimizers ran. 

 Does the writer model matter? 

 The answer is yes. With gpt-6.1-sol as the writer, WeightSpace alone gave +5.8 on d1-omni-600M, +12.1 on NanoJev and −0.6 on d1-2B. Astra produced +16.1, +13.3 and +13.4 on the same models. 

 Did dspy-wsp bend the original paper’s rules? 

 Slightly, and Cmpnd says so. By default, the writer can recompute the decision head inside its kernel. Setting simulate_head=False enforces the paper’s stricter rule. Under that rule, d1-omni-600M gained only +2.8 ± 0.7 points. Adding ReAnchor brought it to +9.3, no better than ReAnchor alone. 

 How do you deploy an edited model? 

 Each run writes a patch to run_dir . The patch holds manifest.json and edit.npz , with only the changed entries. It also stores sha256 hashes of every base and edited tensor. Anyone with the public base model can rebuild the edited weights exactly. 

 Decision models: compiled.wsp_patch.write_checkpoint(backend.weights_dir, "edited-d1/") 

 Text LLMs: dspy-wsp apply <base> <patch> <out>/ , then serve with vLLM. 

 Programs: compiled.save("program.json") and reload with allow_unsafe_lm_state=True . 

 The edited model runs locally. On Apple silicon it uses MLX. On Linux it uses PyTorch, on an NVIDIA GPU if present. 

 What models does dspy-wsp support? 

 Backend Model Alias Architecture D1Backend Liquid AI d1-omni (text path) "d1" Encoder with decision head NanoJevBackend NanoJev "nanojev" Qwen3 backbone with decision head D1LMBackend Liquid AI d1 on LFM3 "d1-2b" LM answering at question positions 

 Text-generating LLMs work through VLLMBackend (NVIDIA), HFBackend (CUDA, MPS or CPU) and MLXBackend (Apple silicon). A GEPASearch option, contributed by Michael Isaac, adds population search for decision models. 

 How does WeightSpace compare with other DSPy optimizers? 

 Metrics WeightSpace (dspy-wsp) ReAnchor BootstrapFinetune GEPA What changes Model weights Decision thresholds, cuts, weights Model weights Prompt text How Frontier LLM reasons and edits in a sandbox Grid search over cached probabilities Gradient fine-tuning on bootstrapped traces Reflective prompt evolution Gradients No No Yes No LLM calls during optimization Yes (writer, 25 passes) None Teacher for bootstrapping Yes Typical cost $5.42 to $7.63 per run Near zero Not disclosed Not disclosed Output Small hashed patch Calibrated program Fine-tuned model Optimized prompts Source dspy-wsp Cmpnd BetterTogether paper GEPA paper 

 Key Takeaways 

 Weight-space programming lets a frontier LLM edit weights directly, without gradients or training data. 

 dspy-wsp wraps it as a DSPy optimizer: pip install dspy-wsp , MIT license. 

 25 writer passes cost $5.42 to $7.63 and took 78 to 167 minutes. 

 d1-omni-600M rose from 50.9% to 69.1% with WeightSpace + ReAnchor. 

 Gains fall at 9B, and the package is explicitly experimental. 

 Check out the Cmpnd blog post , the GitHub repo , the full results and the original Weight-Space Programming research . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy appeared first on MarkTechPost .
