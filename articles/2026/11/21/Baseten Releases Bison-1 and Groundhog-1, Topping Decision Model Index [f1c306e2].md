---
id: "f1c306e2bd8be88c"
title: "Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index"
url: "https://marktechpost.com/2026/11/20/baseten-bison-1-groundhog-1-gemma-4-decision-models"
link: "https://marktechpost.com/2026/11/20/baseten-bison-1-groundhog-1-gemma-4-decision-models"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-21T04:01:04Z"
published_date: "2026-11-21"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Baseten has released bison-1 and groundhog-1, 2 open-weight decision models built on Google’s Gemma 4 . Decision models do not write text. They return calibrated probabilities for yes/no, choice and score questions. The Baseten bison-1 decision model scores 76 on the Artificial Analysis Decision Index v2.1 . That ranks #1 of 19. Both models raise context from 16k to 128k tokens and accept…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Decision Models", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Large Language Model", "New Releases"]
orgs: ["Google", "Hugging Face", "Alibaba"]
topics: ["models & research", "safety & ethics", "products & launches", "business & funding"]
content_source: "summary"
word_count: 1493
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index

MarkTechPost · Asif Razzaq · 2026-11-21

Baseten has released bison-1 and groundhog-1, 2 open-weight decision models built on Google’s Gemma 4 . Decision models do not write text. They return calibrated probabilities for yes/no, choice and score questions. The Baseten bison-1 decision model scores 76 on the Artificial Analysis Decision Index v2.1 . That ranks #1 of 19. Both models raise context from 16k to 128k tokens and accept images. For routing, triage and guardrail pipelines, that means full policies and histories in one call. 

 TL;DR 

 Size: bison-1 is 31B dense. groundhog-1 is a 26B MoE with about 4B active. Both take 128k tokens (131,072). 

 Runs on: Baseten Model APIs, plus open BF16 weights on Hugging Face. No inference GPU or quantized builds are listed. BF16 weights alone are about 62 GB (bison-1) and 52 GB (groundhog-1), by our arithmetic. 

 Performance: bison-1 scores 76 on AA Decision Index v2.1, 1 point above Liquid AI’s d1.2-ultra (75). 

 Best: When2Call, 98 (rank #1). 

 Worst: AA-Omniscience-Decision v1.1, 60 (rank #11). 

 Bottom line: Best: top-ranked, best-calibrated decisions (Brier 0.14) over 128k tokens at $0.10 per 1M input tokens. Worst: groundhog-1 has no official index score yet, and every number is self-reported. 

 What are bison-1 and groundhog-1? 

 bison-1 is a 31B decision model from Baseten that post-trains Gemma 4 31B to return calibrated probabilities. groundhog-1 is the cheaper sibling. It fine-tunes Gemma 4 26B-A4B , a mixture-of-experts model with about 4B active parameters per token. 

 Both join Baseten’s existing lineup: mammoth-1 (27B), elephant-1 (9B) and joey-1 (2B). Those 3 sit on Qwen backbones. The new pair is Baseten’s first on what it calls an American backbone. 

 How does a decision model work? 

 A request carries 1 state and any number of questions . The state is text, optionally with images. Each question has a type: noul (yes/no), choice (named options) or score (ordered levels). 

 The model answers every question in a single prefill pass. It returns P(yes), or the chosen option with a probabilities field. No output tokens are generated. Baseten’s earlier launch post lists ticket triage, spam detection, jailbreak guardrails and LLM routing as target tasks. 

 Requests longer than the trained limit are refused, not truncated. Pipelines that assume silent truncation will need a length check. 

 Why is bison-1 better calibrated? 

 Baseten credits two sources: the Gemma base and more “soft labels” in the training mix. Soft labels use probability targets instead of 1 fixed correct answer. The model learns to report uncertainty that tracks how often it is right. 

 The result is a Brier score of 0.14, the lowest on the index. Baseten puts d1.2-ultra at 0.15. Lower is better. 

 How does bison-1 score on benchmarks? 

 On AA Decision Index v2.1, bison-1 scores 76. Liquid AI’s d1.2-ultra scores 75 and mammoth-1 scores 71. The index blends 6 evaluations, led by AA-Paperclip at 30%. 

 The bison-1 model card breaks out each component: 

 When2Call: 98 (#1) 

 EvalSafe-O*NET-AA: 93 (#1) 

 AA-Symmetry v1.1: 89 (#1) 

 AA-Paperclip: 73 (#2) 

 HLE-MultiChoice v1.1: 51 (#1) 

 AA-Omniscience-Decision v1.1: 60 (#11) 

 bison-1 ranks first on 4 of 6 components. Knowledge-heavy decisions are its weak spot. 

 On long context, Baseten reports LongMemEval M (128k) of 84.8 for bison-1 and 77.4 for groundhog-1. LongMemEval S reads 87.1 and 79.3. groundhog-1 has no official index score yet. Baseten expects it to match mammoth-1. 

 Auto-play</button>
 <div class="dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
 </div>
 <p class="note">Output values in step 4 are illustrative. Request format from the bison-1 model card.</p>
</div>

<!-- BENCH -->
<div class="pane" data-p="bench">
 <div class="seg" id="bsn-seg">
 <button class="on" data-b="idx">AA Decision Index v2.1</button>
 <button data-b="cmp">bison-1 components</button>
 <button data-b="lme">Long context (128k)</button>
 </div>
 <div class="card" id="bsn-bars"></div>
 <p class="note" id="bsn-bnote"></p>
</div>

<!-- CAL -->
<div class="pane" data-p="cal">
 <div class="grid2">
 <div class="card">
 <div style="font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#5FD37C;font-weight:700">Training target</div>
 <div class="seg" id="bsn-lab" style="margin-top:8px">
 <button class="on" data-l="hard">Hard label</button>
 <button data-l="soft">Soft label</button>
 </div>
 <div class="dist">
 <div class="dcol"><div class="dval" id="d0"></div><div class="dbar" id="b0"></div><div class="dlab">billing</div></div>
 <div class="dcol"><div class="dval" id="d1"></div><div class="dbar" id="b1"></div><div class="dlab">tech</div></div>
 <div class="dcol"><div class="dval" id="d2"></div><div class="dbar" id="b2"></div><div class="dlab">sales</div></div>
 </div>
 <p class="cap" id="bsn-lcap" style="min-height:0"></p>
 <p class="note">Target values are illustrative. Baseten says more soft labels in the mix drove a major calibration gain.</p>
 </div>
 <div class="card">
 <div style="font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#5FD37C;font-weight:700">Brier score (lower is better)</div>
 <div class="row" style="grid-template-columns:110px 1fr 44px"><span class="nm">bison-1</span><div class="tr"><div class="fl" data-w="14" style="background:#F5C754"></div></div><span class="vl">0.14</span></div>
 <div class="row" style="grid-template-columns:110px 1fr 44px"><span class="nm">d1.2-ultra</span><div class="tr"><div class="fl" data-w="15" style="background:#5B5E58"></div></div><span class="vl">0.15</span></div>
 <p style="font-size:12.5px;margin:10px 0 0">Brier is the mean squared gap between stated confidence and being right, on a 0 to 1 scale. Bars are drawn on that full 0 to 1 scale.</p>
 <p class="note">bison-1 has the lowest Brier score on the index (self-reported). The d1.2-ultra figure is Baseten's.</p>
 </div>
 </div>
</div>

<!-- LINE -->
<div class="pane" data-p="line">
 <div class="lineup" id="bsn-line"></div>
 <div class="det" id="bsn-det"></div>
 <p class="note">Price is per 1M input tokens on Baseten Model APIs. Decision models produce no output tokens.</p>
</div>

<div class="foot">
 <span>Sources: <a href="https://www.baseten.co/blog/meet-bison-1-and-groundhog-1/" target="_blank" rel="noopener">Baseten blog</a> · <a href="https://huggingface.co/baselabs/bison-1" target="_blank" rel="noopener">bison-1 card</a> · <a href="https://huggingface.co/baselabs/groundhog-1" target="_blank" rel="noopener">groundhog-1 card</a> · <a href="https://www.liquid.ai/blog/d1-2" target="_blank" rel="noopener">Liquid AI</a>. Scores self-reported.</span>
 <span class="brand">Built by Marktechpost</span>
</div>

<script>
(function(){
var R=document.getElementById('mtp-bsn-x');
function q(s){return R.querySelector(s)} function qa(s){return R.querySelectorAll(s)}
function resize(){try{var h=R.offsetHeight+40;parent.postMessage({mtpEmbed:'mtp-bsn-x',height:h},'*')}catch(e){}}
/* tabs */
qa('.tab').forEach(function(t){t.addEventListener('click',function(){
 qa('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');
 qa('.pane').forEach(function(p){p.classList.toggle('on',p.getAttribute('data-p')===t.getAttribute('data-t'))});
 if(t.getAttribute('data-t')==='bench')drawBars(cur);
 if(t.getAttribute('data-t')==='cal'){setLab(lab);calBars()}
 setTimeout(resize,60);
})});
/* how */
var caps=['The state holds the context: policies, conversation history and optional images, up to 128k tokens.','Attach any number of typed questions: noul (yes/no), choice (named options) or score (ordered levels).','The model reads everything in a single prefill pass. It never generates output tokens.','It returns P(yes), or the chosen option with a probabilities field. Your code branches on calibrated numbers.'];
var step=0,timer=null;
function show(s){step=s;qa('.node').forEach(function(n){var i=+n.getAttribute('data-s');n.classList.toggle('lit',i<=s)});
 qa('.dot').forEach(function(d,i){d.classList.toggle('on',i===s)});
 q('#bsn-cap').textContent=caps[s];
 qa('.node[data-s="3"] .fill').forEach(function(f){f.style.width=(s>=3?f.getAttribute('data-w'):0)+'%'});}
q('#bsn-next').addEventListener('click',function(){stop();show((step+1)%4)});
q('#bsn-prev').addEventListener('click',function(){stop();show((step+3)%4)});
function stop(){if(timer){clearInterval(timer);timer=null;q('#bsn-play').textContent=' Auto-play'}}
q('#bsn-play').addEventListener('click',function(){if(timer){stop();return}q('#bsn-play').textContent='❚❚ Pause';timer=setInterval(function(){show((step+1)%4)},1800)});
show(0);
/* bench */
var data={
 idx:{max:100,rows:[['bison-1',76,'#1 of 19','#F5C754'],['Liquid d1.2-ultra',75,'','#5B5E58'],['mammoth-1',71,'','#5FD37C'],['groundhog-1',null,'Not yet scored','#C7A6F2']],note:'Artificial Analysis Decision Index v2.1, as reported by Baseten. Baseten expects groundhog-1 to match mammoth-1.'},
 cmp:{max:100,rows:[['When2Call',98,'#1','#F5C754'],['EvalSafe-O*NET-AA',93,'#1','#F5C754'],['AA-Symmetry v1.1',89,'#1','#F5C754'],['AA-Paperclip',73,'#2','#F5C754'],['AA-Omniscience-Dec.',60,'#11','#F08A5D'],['HLE-MultiChoice v1.1',51,'#1','#F5C754']],note:'bison-1 component scores and ranks from its Hugging Face model card. Orange marks its weakest rank.'},
 lme:{max:100,rows:[['bison-1 · M',84.8,'','#F5C754'],['groundhog-1 · M',77.4,'','#C7A6F2'],['bison-1 · S',87.1,'','#F5C754'],['groundhog-1 · S',79.3,'','#C7A6F2']],note:'LongMemEval M and S at 128k tokens, from Baseten\'s own runs (model cards).'}
};
var cur='idx';
function drawBars(k){cur=k;var d=data[k],h='';
 d.rows.forEach(function(r){h+='<div class="row"><span class="nm">'+r[0]+(r[2]?'<span class="rk">'+r[2]+'</span>':'')+'</span><div class="tr"><div class="fl" data-w="'+(r[1]===null?0:r[1]/d.max*100)+'" style="background:'+r[3]+'"></div></div><span class="vl">'+(r[1]===null?'n/a':r[1])+'</span></div>'});
 q('#bsn-bars').innerHTML=h;q('#bsn-bnote').textContent=d.note;
 setTimeout(function(){qa('#bsn-bars .fl').forEach(function(f){f.style.width=f.getAttribute('data-w')+'%'})},40);
 qa('#bsn-seg button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-b')===k)});setTimeout(resize,80);}
qa('#bsn-seg button').forEach(function(b){b.addEventListener('click',function(){drawBars(b.getAttribute('data-b'))})});
/* calibration */
var lab='hard',L={hard:[1,0,0],soft:[0.7,0.2,0.1]},LC={hard:'A hard label says billing is 100% right and the rest are 0%. The model learns to be overconfident.',soft:'A soft label spreads probability across plausible answers. The model learns to state uncertainty honestly.'};
function setLab(l){lab=l;L[l].forEach(function(v,i){q('#b'+i).style.height=(v*100)+'px';q('#d'+i).textContent=Math.round(v*100)+'%'});q('#bsn-lcap').textContent=LC[l];
 qa('#bsn-lab button').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-l')===l)})}
qa('#bsn-lab button').forEach(function(b){b.addEventListener('click',function(){setLab(b.getAttribute('data-l'))})});
function calBars(){qa('.pane[data-p="cal"] .fl').forEach(function(f){f.style.width='0';setTimeout(function(){f.style.width=f.getAttribute('data-w')+'%'},40)})}
/* lineup */
var M=[['joey-1','2B','Qwen3.5-2B','16k','$0.01','Latency or cost dominates',0],['elephant-1','9B','Qwen3.5-9B','16k','$0.035','Strong default at low latency',0],['mammoth-1','27B','Qwen3.5-27B','16k','$0.10','Knowledge-heavy decisions',0],['groundhog-1','26B MoE (~4B active)','Gemma 4 26B-A4B','128k','$0.035','Long context at low latency and cost',1],['bison-1','31B','Gemma 4 31B','128k','$0.10','Highest accuracy, long context',1]];
var lh='';M.forEach(function(m,i){lh+='<button class="mdl'+(i===4?' on':'')+'" data-i="'+i+'"><div class="n">'+m[0]+(m[6]?'<span class="new">NEW</span>':'')+'</div><div class="p">'+m[1]+' · '+m[4]+'</div></button>'});
q('#bsn-line').innerHTML=lh;
function det(i){var m=M[i];q('#bsn-det').innerHTML='<div class="kv"><div class="k">Params</div><div class="v">'+m[1]+'</div></div><div class="kv"><div class="k">Backbone</div><div class="v">'+m[2]+'</div></div><div class="kv"><div class="k">Context</div><div class="v">'+m[3]+'</div></div><div class="kv"><div class="k">Per 1M tokens</div><div class="v">'+m[4]+'</div></div><div class="kv" style="grid-column:1/-1"><div class="k">Best for (per Baseten)</div><div class="v" style="font-size:13.5px">'+m[5]+'</div></div>';
 qa('.mdl').forEach(function(b){b.classList.toggle('on',+b.getAttribute('data-i')===i)});setTimeout(resize,60)}
qa('.mdl').forEach(function(b){b.addEventListener('click',function(){det(+b.getAttribute('data-i'))})});
det(4);
window.addEventListener('load',resize);window.addEventListener('resize',resize);setTimeout(resize,300);
})();
</script>
</div>
</body></html>"> 
 window.addEventListener("message",function(e){var d=e.data;if(d&&d.mtpEmbed==="mtp-bsn-x"&&d.height){var f=document.getElementById("mtp-bsn-frame");if(f)f.style.height=d.height+"px";}}); 

 How does it compare with other decision models? 

 Feature bison-1 groundhog-1 mammoth-1 Liquid d1.2-ultra Total params 31B dense 26B MoE 27B Not disclosed Active params 31B ~4B 27B Not disclosed Backbone Gemma 4 31B Gemma 4 26B-A4B Qwen3.5-27B Not disclosed Context 128k 128k 16k 65,536 Input Text, image Text, image Text, image Text, image, audio License MIT + Apache 2.0 MIT + Apache 2.0 MIT Not disclosed Weights Open (Hugging Face) Open (Hugging Face) Open (Hugging Face) Liquid API (weights not disclosed) AA Decision Index v2.1 76 Not yet scored 71 75 Brier score 0.14 Not disclosed Not disclosed 0.15 (per Baseten) LongMemEval M (128k) 84.8 77.4 Not disclosed Not disclosed Price per 1M input tokens $0.10 $0.035 $0.10 $0.042 

 How can developers deploy bison-1 and groundhog-1? 

 Both models are live on Baseten Model APIs . They use the same API as the older decision models, so switching means changing 1 model name. The IDs are decision-models/baseten-bison-latest and decision-models/baseten-groundhog-latest . 

 Pricing mirrors the older pair. bison-1 costs $0.10 per 1M tokens, like mammoth-1. groundhog-1 costs $0.035, like elephant-1. The bison-1 library page lists that as an input price, since no output tokens are produced. 

 Open BF16 weights sit on Hugging Face. Baseten lists no inference GPU or quantized builds. Training used 192 B200 GPUs for bison-1 and 128 for groundhog-1. 

 Key Takeaways 

 bison-1 tops AA Decision Index v2.1 at 76, 1 point over d1.2-ultra. 

 Context jumps 8x to 128k, with image input on both models. 

 groundhog-1 runs about 4B active params at $0.035 per 1M tokens. 

 Soft-label training helps push bison-1’s Brier score to 0.14. 

 Check out the launch post , the bison-1 and groundhog-1 model cards, and the Baseten docs . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index appeared first on MarkTechPost .
