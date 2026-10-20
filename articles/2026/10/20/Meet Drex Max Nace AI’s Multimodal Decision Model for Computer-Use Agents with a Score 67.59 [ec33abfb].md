---
id: "ec33abfb0932e649"
title: "Meet Drex Max: Nace AI’s Multimodal Decision Model for Computer-Use Agents with a Score 67.59"
url: "https://marktechpost.com/2026/10/19/nace-ai-drex-max-multimodal-decision-model"
link: "https://marktechpost.com/2026/10/19/nace-ai-drex-max-multimodal-decision-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-20T00:03:38Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Nace AI has released Drex Max , a multimodal decision model for agents that use computers and browsers. The Drex Max multimodal decision model reads text and images and returns calibrated probabilities. It writes no text. Nace team reports 67.59 on the public Decision Index 0.3.2 , 6.9 points above TypeSafe’s Jev 1.14. For agent builders, that means one cheap, typed call per click. \n\n TL;DR \n\n…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Computer-Use", "Decision Models", "Editors Pick", "Enterprise AI", "For Devs", "Language Model", "Large Language Model"]
orgs: ["OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "summary"
word_count: 1481
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Drex Max: Nace AI’s Multimodal Decision Model for Computer-Use Agents with a Score 67.59

MarkTechPost · Michal Sutter · 2026-10-20

Nace AI has released Drex Max , a multimodal decision model for agents that use computers and browsers. The Drex Max multimodal decision model reads text and images and returns calibrated probabilities. It writes no text. Nace team reports 67.59 on the public Decision Index 0.3.2 , 6.9 points above TypeSafe’s Jev 1.14. For agent builders, that means one cheap, typed call per click. 

 TL;DR 

 Size: Parameters not disclosed. Up to 262,144 tokens per question on the API, including image tokens. 

 Runs on: Hosted API only ( drex-max on Nace Console). No open weights or quantized builds announced. 

 Performance: 67.59 on Decision Index 0.3.2 (public), the top score Nace lists for any decision model. 

 Best: 98.2 on BFCL tool calling, and 92.2 on JevBench versus 86.7 for Jev 1.14. 

 Worst: 19.0 on HLE, and 72.5 on MMLU-Pro versus 82.1 for Jev 1.14. 

 What is Drex Max? 

 Drex Max is a decision model from Nace AI that answers typed questions about text and images. It is the most accurate model in the Drex family , and the only one that reads images. 

 A decision model does not generate tokens. You send a state and named questions. Each question is one of 3 types: noul (yes/no), choice (pick a label) or score (ordered scale). The model returns a probability distribution for each answer in 1 HTTP call. Drex can only answer with the options you gave it. 

 How does Drex Max work with images? 

 Drex Max uses the same POST /v1/systemone endpoint as every Drex model. You select it with "model": "drex-max" . It is a pinned ID, so drex-latest does not route to it. 

 Images go in an images array. Every question sees the same images, before the state and questions. You refer to them as ‘Image 1’ and ‘Image 2’ in plain text. Each entry is either an uploaded workspace file or inline base64. 

 Key image rules from the Drex Max guide : 

 Formats: still PNG, JPEG or WebP. 

 Up to 8 images per request, 16 MiB each, 32 MiB total. 

 Each image is resized to at most 1,638,400 pixels (1,280 × 1,280). 

 Each image costs up to 1,602 tokens in every question. 

 Up to 16 questions per request, with a 4 MiB request body. 

 How does Drex Max perform on benchmarks? 

 All scores below come from Nace’s Drex page . They are self-reported. Nace says Drex trains on the index’s official training splits and is scored on held-out splits. 

 Decision benchmarks : Drex Max scores 67.6 on the public Decision Index 0.3.2. Jev 1.14 scores 60.7 and Drex 2.0 scores 61.3. On JevBench, Drex Max reaches 92.2 against 86.7 for Jev 1.14. 

 Agentic benchmarks : Drex Max posts 0.780 on OSWorld-Verified and 98.2 on BFCL. It scores 85.2 on When2Call and 84.8 on RAGTruth. 

 Vision : On the Decision Index Vision public suite, Drex Max scores 74.5. GPT-6 Luna Decisions scores 63.9. Mind2Web reaches 88.6 and InfographicVQA reaches 98.8. 

 Where it trails : Jev 1.14 leads on MMLU-Pro (82.1 vs 72.5), HLE (19.4 vs 19.0) and ARC-Challenge (97.6 vs 97.4). On Hateful Memes, Drex Max trails GPT-6 Luna Decisions, 70.6 vs 71.2. 

 Back</button>
 <button class="btn pri" id="mtp-next">Next step </button>
 <button class="btn" id="mtp-play">Auto play</button>
 <div class="dots"><i></i><i></i><i></i></div>
 </div>
 <p class="note">Answer probabilities are an illustration of the response shape, not real model output.</p>
 </div>

 <div class="pn" data-p="bench">
 <div class="seg" id="mtp-seg">
 <button class="on" data-s="di">Decision Index</button>
 <button data-s="ag">Agentic</button>
 <button data-s="vi">Vision</button>
 </div>
 <div id="mtp-bars"></div>
 <p class="note" id="mtp-bnote"></p>
 </div>

 <div class="pn" data-p="vs">
 <table class="vs">
 <thead><tr><th>Benchmark</th><th style="text-align:right">Drex Max</th><th style="text-align:right">Jev 1.14</th><th>Result</th></tr></thead>
 <tbody id="mtp-vs"></tbody>
 </table>
 <p class="note">All figures from Nace's Drex page (self-reported). Jev 1.14 rejects 15.9% of screenshots by size, per Nace.</p>
 </div>

 <div class="pn" data-p="lim">
 <div class="grid" id="mtp-lims"></div>
 <p class="note">Tap a card for detail. Source: Nace Drex Max API guide.</p>
 </div>

 <div class="pn" data-p="cost">
 <div class="calc">
 <div>
 <label for="mtp-dec">Decisions per day: <b id="mtp-decv" style="color:#f5f5f4">10,000</b></label>
 <input type="range" id="mtp-dec" min="1000" max="1000000" step="1000" value="10000">
 <label for="mtp-img">Screenshots per decision: <b id="mtp-imgv" style="color:#f5f5f4">1</b></label>
 <input type="range" id="mtp-img" min="0" max="8" step="1" value="1">
 <label for="mtp-txt">Text tokens per decision (state + question): <b id="mtp-txtv" style="color:#f5f5f4">500</b></label>
 <input type="range" id="mtp-txt" min="50" max="20000" step="50" value="500">
 </div>
 <div class="out">
 <small>Estimated daily cost, upper bound</small>
 <div class="big" id="mtp-cost">$0.00</div>
 <small id="mtp-tok"></small>
 <small style="margin-top:10px">Uses $0.06 per 1M input tokens and the 1,602-token maximum per image. Output tokens are not billed. Real image token counts can be lower.</small>
 </div>
 </div>
 </div>

 <div class="ft">
 <span class="src">Sources: <a href="https://www.nace.ai/drex" target="_blank" rel="noopener">nace.ai/drex</a> · <a href="https://console.nace.ai/docs/drex/guides/drex-max" target="_blank" rel="noopener">Drex Max guide</a></span>
 <a href="https://www.marktechpost.com" target="_blank" rel="noopener">© Marktechpost</a>
 </div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-drexmax');
function $(s,c){return (c||R).querySelector(s)}function $$(s,c){return Array.prototype.slice.call((c||R).querySelectorAll(s))}
function post(){try{var h=R.offsetHeight+40;parent.postMessage({mtpDrexMaxHeight:h,type:'mtp-resize',height:h},'*')}catch(e){}}
/* counters */
$$('[data-count]').forEach(function(el){var to=+el.dataset.count,d=+(el.dataset.dec||0),suf=el.dataset.suf||'',sep=el.dataset.sep,t0=null;
function f(v){var s=v.toFixed(d);if(sep)s=Math.round(v).toLocaleString('en-US');return s+suf}
function step(ts){if(!t0)t0=ts;var k=Math.min(1,(ts-t0)/1100),e=1-Math.pow(1-k,3);el.textContent=f(to*e);if(k<1)requestAnimationFrame(step);else el.textContent=f(to)}
requestAnimationFrame(step)});
/* tabs */
$$('.tab').forEach(function(b){b.addEventListener('click',function(){$$('.tab').forEach(function(x){x.setAttribute('aria-selected',x===b)});
$$('.pn').forEach(function(p){p.classList.toggle('on',p.dataset.p===b.dataset.t)});
if(b.dataset.t==='bench')drawBars(cur);if(b.dataset.t==='flow')show(stp);setTimeout(post,60);setTimeout(post,500)})});
/* flow */
var caps=['Step 1: send a state plus up to 8 still images. Every question sees the same images, before the state and questions.','Step 2: name up to 16 typed questions. Drex Max can only answer with the options you supply.','Step 3: one call returns a probability for every option. Nace lists 174 ms median per screenshot decision.'];
var stp=0,timer=null;
function show(i){stp=i;$$('.node').forEach(function(n){n.classList.toggle('lit',+n.dataset.n<=i)});
$$('.dots i').forEach(function(d,k){d.classList.toggle('on',k===i)});$('#mtp-cap').textContent=caps[i];
$$('.prob u').forEach(function(u){u.style.width=i===2?u.dataset.w+'%':'0'})}
$('#mtp-next').onclick=function(){stopPlay();show((stp+1)%3)};$('#mtp-prev').onclick=function(){stopPlay();show((stp+2)%3)};
function stopPlay(){if(timer){clearInterval(timer);timer=null;$('#mtp-play').textContent='Auto play'}}
$('#mtp-play').onclick=function(){if(timer){stopPlay();return}this.textContent='Pause';show(0);timer=setInterval(function(){show((stp+1)%3)},2200)};
show(0);
/* bars */
var D={di:{max:80,rows:[['Drex Max',67.6,1],['Drex 2.0',61.3],['Jev 1.14',60.7],['Drex 1.5',58.1],['GPT-6 Luna Decisions',47.8]],note:'Decision Index 0.3.2, public benchmarks only, chance-corrected. Source: nace.ai/drex (self-reported).'},
ag:{max:100,rows:[['Drex Max · BFCL',98.2,1],['Jev 1.14 · BFCL',96.4],['Drex Max · OSWorld-Verified',78.0,1],['Jev 1.14 · OSWorld-Verified',73.4],['Drex Max · When2Call',85.2,1],['Jev 1.14 · When2Call',81.7]],note:'OSWorld-Verified shown ×100 (0.780 and 0.734). Source: nace.ai/drex (self-reported).'},
vi:{max:100,rows:[['Drex Max · Vision Index',74.5,1],['GPT-6 Luna Decisions',63.9],['Drex Max · Mind2Web',88.6,1],['GPT-6 Luna · Mind2Web',81.2],['Drex Max · CV-Bench',86.3,1],['GPT-6 Luna · CV-Bench',73.8]],note:'Decision Index Vision, public suite, 11 benchmarks. Source: nace.ai/drex (self-reported).'}};
var cur='di';
function drawBars(k){cur=k;var d=D[k],h='';d.rows.forEach(function(r){h+='<div class="row'+(r[2]?' me':'')+'"><span class="lab">'+r[0]+'</span><div class="tr"><div class="fl" data-w="'+(r[1]/d.max*100)+'"></div></div><span class="v">'+r[1].toFixed(1)+'</span></div>'});
$('#mtp-bars').innerHTML=h;$('#mtp-bnote').textContent=d.note;
requestAnimationFrame(function(){requestAnimationFrame(function(){$$('#mtp-bars .fl').forEach(function(f){f.style.width=f.dataset.w+'%'})})});
$$('#mtp-seg button').forEach(function(b){b.classList.toggle('on',b.dataset.s===k)});setTimeout(post,60)}
$$('#mtp-seg button').forEach(function(b){b.onclick=function(){drawBars(b.dataset.s)}});
/* vs */
var V=[['Decision Index 0.3.2','67.6','60.7',1],['JevBench','92.2','86.7',1],['Decision Bench','94.3','92.3',1],['Game Bench win %','64.0','50.0',1],['BFCL','98.2','96.4',1],['OSWorld-Verified','0.780','0.734',1],['Screenshot decision','174 ms','253 ms',1],['MMLU-Pro','72.5','82.1',0],['HLE','19.0','19.4',0],['ARC-Challenge','97.4','97.6',0]];
$('#mtp-vs').innerHTML=V.map(function(r){return '<tr><td>'+r[0]+'</td><td class="n">'+r[1]+'</td><td class="n">'+r[2]+'</td><td>'+(r[3]?'<span class="pill w">Max leads</span>':'<span class="pill l">Jev leads</span>')+'</td></tr>'}).join('');
/* limits */
var L=[['16','questions per request','Same limit with or without images.'],['262,144','tokens per question','State plus that question, image tokens included. Nace\'s landing page lists 131K context.'],['8','images per request','Still PNG, JPEG or WebP. 16 MiB each, 32 MiB total.'],['1,602','max tokens per image','Charged in every question. Images resize to at most 1,638,400 pixels (1,280 × 1,280).'],['4 MiB','request body','Inline base64 images count toward it, so about 3 MiB of image bytes fit.'],['$0','for failed requests','Only a 200 response is billed. Output tokens are never billed.']];
$('#mtp-lims').innerHTML=L.map(function(l){return '<div class="lim" tabindex="0"><b>'+l[0]+'</b><span>'+l[1]+'</span><p>'+l[2]+'</p></div>'}).join('');
$$('.lim').forEach(function(c){function t(){c.classList.toggle('open');setTimeout(post,380)}c.onclick=t;c.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t()}}});
/* calc */
function calc(){var n=+$('#mtp-dec').value,im=+$('#mtp-img').value,tx=+$('#mtp-txt').value,tok=n*(tx+im*1602),c=tok/1e6*0.06;
$('#mtp-decv').textContent=n.toLocaleString('en-US');$('#mtp-imgv').textContent=im;$('#mtp-txtv').textContent=tx.toLocaleString('en-US');
$('#mtp-cost').textContent='$'+(c<10?c.toFixed(2):Math.round(c).toLocaleString('en-US'));$('#mtp-tok').textContent=tok.toLocaleString('en-US')+' input tokens per day'}
['#mtp-dec','#mtp-img','#mtp-txt'].forEach(function(s){$(s).oninput=calc});calc();
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);setTimeout(post,1200);
})();
</script>
</body></html>
" style="width:100%;height:600px;border:0;display:block;background:transparent;" loading="lazy" scrolling="no"> 

(function(){var f=document.getElementById('mtp-drexmax-frame');window.addEventListener('message',function(e){if(!e.data||e.source!==f.contentWindow)return;var h=e.data.mtpDrexMaxHeight;if(h&&h>200)f.style.height=h+'px';});})();

 How fast and how cheap is Drex Max? 

 Nace lists a 174 ms median per screenshot decision . Jev 1.14 takes 253 ms on the same 243 questions. Nace says Drex Max accepts every screenshot size, while Jev 1.14 rejects 15.9% by size. 

 Across its benchmark table, Nace reports a 183 ms median latency. The launch post cites 34 ms per decision and under 1 second at 262K tokens. Those figures use different setups, so treat them as separate claims. 

 Pricing is $0.06 per 1M input tokens . Output tokens are not billed. New accounts get $25 in signup credit , and failed requests cost nothing. 

 How does Drex Max compare with other decision models? 

 Feature Drex Max Jev 1.14 Drex 2.0 d3-flash Developer Nace AI TypeSafe AI Nace AI vLLM Semantic Router Parameters Not disclosed Not disclosed 35B total, about 3B active (MoE) 8.39B Context 262,144 tokens per question 64K per request, 262K with long-context header 16,384 default, up to 131,072 Not disclosed Inputs Text, images Text (TypeSafe docs) Text Text, images, video License Proprietary (hosted) Proprietary (hosted) Nace.AI Open RAIL-M Apache-2.0 Decision Index (public) 67.6 (0.3.2) 60.7 (0.3.2, per Nace) 61.25 (0.3.1) 57.8 (0.3.2) Vision index (public) 74.5 Not disclosed Not applicable 69.9 Price per 1M input tokens $0.06 $0.042 $0.06 Self-host, free trial Runs on Nace Console API TypeSafe API Single accelerator, bf16 about 70 GB 1 AMD Instinct MI325X tested 

 Note: d3-flash’s vision figure is its own evaluation on the 0.3.2 vision board. Drex Max’s figure is Nace’s own run. Cross-vendor numbers are not a controlled comparison. 

 Key Takeaways 

 Drex Max is Nace AI’s first multimodal decision model. 

 It scores 67.59 on Decision Index 0.3.2, 6.9 above Jev 1.14. 

 Screenshot decisions take 174 ms, versus 253 ms for Jev 1.14. 

 Pricing is $0.06 per 1M input tokens, with output free. 

 Size is undisclosed, weights are closed, and scores are self-reported. 

 Check out the Drex Max guide , the Drex product page and the launch post . Also read our earlier coverage of Drex 1.5 . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Meet Drex Max: Nace AI’s Multimodal Decision Model for Computer-Use Agents with a Score 67.59 appeared first on MarkTechPost .
