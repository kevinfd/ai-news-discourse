---
id: "8d5827682de7ed4c"
title: "Google Releases Gemini 4 Argon API With 1M Token Output Limit"
url: "https://marktechpost.com/2026/10/13/google-gemini-4-argon-api-release"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T05:03:34Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google DeepMind has made Gemini 4 Argon generally available to developers, enterprises and paid Gemini subscribers. Gemini 4 Argon is a sparse mixture-of-experts frontier model from Google built for long, multi-step work. Its target domains are coding, finance, legal, science and cybersecurity. Google first announced Argon on September 30 for a small group of cyber defenders. It now reaches the…"
tags: ["Agentic AI", "Editors Pick", "Enterprise AI", "For Devs", "New Releases", "Software Engineering", "Staff", "Tech News", "Uncategorized"]
orgs: ["Google", "OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "safety & ethics", "chips & infrastructure"]
content_source: "summary"
word_count: 1617
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google Releases Gemini 4 Argon API With 1M Token Output Limit

MarkTechPost · Asif Razzaq · 2026-10-14

Google DeepMind has made Gemini 4 Argon generally available to developers, enterprises and paid Gemini subscribers. Gemini 4 Argon is a sparse mixture-of-experts frontier model from Google built for long, multi-step work. Its target domains are coding, finance, legal, science and cybersecurity. Google first announced Argon on September 30 for a small group of cyber defenders. It now reaches the paid Gemini API at $2 input and $10 output per million tokens. The key change for developers is output length: Argon can write up to 1M tokens in one response. 

 TL;DR 

 Size: Parameter count not disclosed (sparse MoE). 1M token window shared by input and output. 

 Runs on: Google’s cloud only, via Gemini API, AI Studio and Gemini platform. Trained on TPUs. No open weights. 

 Performance: Leads Google’s table on knowledge work, long context and video. Mixed on agentic coding. 

 Best: 91.7% on LVBench (long video understanding). 

 Worst: 55.0% on FrontierSWE v2, last of 4 models in Google’s table. 

 What is Gemini 4 Argon? 

 According to the model card , Argon is a new model, not a fine-tune of an earlier Gemini. It is a large-scale sparse MoE transformer with native multimodal support. It accepts text, images, audio and video, and it outputs text. Google trained it on TPUs using JAX and ML Pathways. The knowledge cutoff is March 2026. Google has not disclosed total or active parameter counts. 

 How does the 1M token output limit work? 

 Google raised the output limit to 1M tokens, up from 64K on earlier Gemini models. The model card describes a combined input plus output window of up to 1M tokens. So a long prompt reduces the room left for output. Google documents a new continuation protocol for long decodes in its developer docs and enterprise docs . At introductory pricing, a full 1M token response costs $10 in output tokens. 

 How does Gemini 4 Argon perform on benchmarks? 

 Google compares Argon with GPT-6 Astra, Claude Fable 5.1 and Claude Opus 5.5. Argon posts the top score on most rows. 

 DeepSWE v1.1: 77.9%, ahead of Opus 5.5 (74.2%) and GPT-6 Astra (74.1%). 

 Vals Index: 68.90%, ranked #1 by Vals AI ahead of Claude Sonnet 5.5 (67.04%). 

 AutomationBench: 51.3%, versus 42.5% for Opus 5.5. 

 Harvey’s Legal Agent Benchmark: 19.6%, nearly 3x the next model, but still a low absolute score. 

 GraphWalks, 256K to 1M tokens: 84.2%, versus 71.8% for GPT-6 Astra. 

 CWE-bench v1: 68.0%, tied with GPT-6 Astra. 

 Google also reports 87% on the ERQA embodied reasoning benchmark . Read the evaluation methodology before drawing conclusions. Most rival scores are self-reported or pulled from public leaderboards. Argon’s DeepSWE score is self-computed with a mini-swe-agent harness. The rival DeepSWE numbers come from system cards and a leaderboard. 

 Where does Gemini 4 Argon fall short? 

 Argon trails on 5 rows of Google’s own table: 

 FrontierSWE v2: 55.0%, versus 65.5% for GPT-6 Astra. 

 Terminal-Bench 4.0: 57.4%, versus 66.4% for Opus 5.5. 

 Terminal-Bench Science 0.1: 57.6%, versus 68.1% for GPT-6 Astra. 

 PostTrainBench: 45.3%, versus 49.3% for Opus 5.5. 

 OSWorld-2.0 (offline subset): 69.2%, versus 72.6% for GPT-6 Astra. 

 The model card also lists hallucinations and occasional slowness or timeouts. Under Google’s Frontier Safety Framework, Google says it cannot rule out the biological and cybersecurity critical capability levels. It reports deploying safeguards it assesses as lowering that risk. 

 Step through</button><button class="btn g" id="mtp-next">Next step</button></div>
 <div class="win">
 <div style="font-size:13px;font-weight:700;margin-bottom:8px">Shared 1M token window: drag to set your prompt size</div>
 <input type="range" id="mtp-in" min="0" max="1000" value="200" aria-label="Input tokens in thousands">
 <div class="bar"><i id="mtp-bi" style="background:#4285F4"></i><i id="mtp-bo" style="background:#34A853"></i></div>
 <div class="lab"><span id="mtp-li"></span><span id="mtp-lo"></span></div>
 </div>
 </div>

 <div class="pane" id="p-bench">
 <div class="chips" id="mtp-chips"></div>
 <div id="mtp-rows"></div>
 <div class="note" id="mtp-bnote"></div>
 </div>

 <div class="pane" id="p-price">
 <div class="seg"><button class="on" data-p="intro">Intro (to Nov 30, 2026)</button><button data-p="std">Standard (after)</button></div>
 <div class="calc">
 <div><label>Input tokens per month: <output id="mtp-ci"></output></label><input type="range" id="mtp-rin" min="1" max="500" value="100"></div>
 <div><label>Output tokens per month: <output id="mtp-co"></output></label><input type="range" id="mtp-rout" min="1" max="200" value="20"></div>
 </div>
 <div id="mtp-prows"></div>
 <div class="note">List prices per 1M tokens: Argon $2/$10 intro, $4/$20 after Nov 30, 2026. GPT-6 Astra $10/$50 (prompts under 272K). Claude Opus 5.5 $4/$20. Claude Fable 5.1 $10/$50. Estimate excludes caching, batch and long-context surcharges.</div>
 </div>

 <div class="pane" id="p-access">
 <div class="grid">
 <div class="acc"><h4><span class="dot" style="background:#4285F4"></span>Developers</h4><p>Gemini API paid tier in Google AI Studio and Android Studio. Model ID: <code>gemini-4-argon</code>.</p></div>
 <div class="acc"><h4><span class="dot" style="background:#9168F0"></span>Enterprises</h4><p>Gemini platform, Gemini for business and Google Antigravity.</p></div>
 <div class="acc"><h4><span class="dot" style="background:#FBBC04"></span>Consumers</h4><p>Gemini app and AI Mode in Search for Google AI Pro and Ultra subscribers.</p></div>
 <div class="acc"><h4><span class="dot" style="background:#EA4335"></span>Cyber defenders</h4><p>Fairwind Program partners get Argon without cyber guardrails, on a rolling basis.</p></div>
 </div>
 <div class="note">Known limits from the model card: hallucinations, occasional slowness or timeouts, knowledge cutoff March 2026. Parameter count not disclosed.</div>
 </div>

 <div class="ft"><span>Sources: Google blog, Gemini 4 Argon model card and eval methodology, Vals AI. Checked Oct 13, 2026.</span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-g4a');
function $(s){return R.querySelector(s)} function $$(s){return R.querySelectorAll(s)}
function resize(){try{parent.postMessage({mtpH:R.offsetHeight+40,id:'mtp-g4a'},'*')}catch(e){}}
// tabs
$$('.tab').forEach(function(b){b.onclick=function(){$$('.tab').forEach(function(x){x.classList.remove('on')});$$('.pane').forEach(function(x){x.classList.remove('on')});b.classList.add('on');$('#p-'+b.dataset.t).classList.add('on');if(b.dataset.t==='bench')drawB(cur);if(b.dataset.t==='price')drawP();setTimeout(resize,60)}});
// experts svg
var g=$('#mtp-exp'),NS='http://www.w3.org/2000/svg',ex=[];
for(var i=0;i<8;i++){var y=12+i*19;var l=document.createElementNS(NS,'path');l.setAttribute('d','M340 81 C 380 81 380 '+(y+7)+' 420 '+(y+7));l.setAttribute('stroke','#273041');l.setAttribute('fill','none');l.setAttribute('class','exp');g.appendChild(l);
var r=document.createElementNS(NS,'rect');r.setAttribute('x',420);r.setAttribute('y',y);r.setAttribute('width',150);r.setAttribute('height',14);r.setAttribute('rx',4);r.setAttribute('fill','#202734');r.setAttribute('class','exp');g.appendChild(r);
var o=document.createElementNS(NS,'path');o.setAttribute('d','M570 '+(y+7)+' C 605 '+(y+7)+' 605 81 640 81');o.setAttribute('stroke','#273041');o.setAttribute('fill','none');o.setAttribute('class','exp');g.appendChild(o);ex.push([l,r,o]);}
var t=document.createElementNS(NS,'text');t.setAttribute('x',495);t.setAttribute('y',10);t.setAttribute('text-anchor','middle');t.setAttribute('font-size','11');t.setAttribute('fill','#9AA0A6');t.textContent='Experts (only a few fire per token)';g.appendChild(t);
var cols=['#4285F4','#9168F0'];
function route(){var a=Math.floor(Math.random()*8),b=(a+1+Math.floor(Math.random()*7))%8;ex.forEach(function(e,k){var on=(k===a||k===b);e[0].setAttribute('stroke',on?cols[k===a?0:1]:'#273041');e[2].setAttribute('stroke',on?cols[k===a?0:1]:'#273041');e[1].setAttribute('fill',on?cols[k===a?0:1]:'#202734')})}
route();setInterval(route,900);
// steps
var D=['<b>Natively multimodal input.</b> Argon takes text, images, audio and video in one request. Google says it is a new model, not a fine-tune of an earlier Gemini.',
'<b>Sparse mixture of experts.</b> A router sends each token to a small subset of expert networks, so only part of the model runs per token. Google has not disclosed total or active parameters.',
'<b>Built for long-horizon work.</b> Google trained Argon with reinforcement learning on multi-step reasoning, problem-solving and theorem-proving data. It targets coding, finance, legal, science and cyber defense.',
'<b>Output up to 1M tokens.</b> The output limit rose from 64K to 1M tokens. Input and output share one 1M window, and long responses use a new continuation protocol.'];
var s=0,timer=null;function step(n){s=n;$$('.st').forEach(function(x){x.classList.toggle('on',+x.dataset.s===n)});$('#mtp-det').innerHTML=D[n];resize()}
$$('.st').forEach(function(x){x.onclick=function(){stop();step(+x.dataset.s)}});
function stop(){if(timer){clearInterval(timer);timer=null;$('#mtp-play').textContent=' Step through'}}
$('#mtp-next').onclick=function(){stop();step((s+1)%4)};
$('#mtp-play').onclick=function(){if(timer){stop();return}$('#mtp-play').textContent='❚❚ Pause';timer=setInterval(function(){step((s+1)%4)},2600)};
step(0);
// window
function win(){var v=+$('#mtp-in').value;$('#mtp-bi').style.width=(v/10)+'%';$('#mtp-bo').style.width=((1000-v)/10)+'%';$('#mtp-li').textContent='Input: '+v+'K tokens';$('#mtp-lo').textContent='Room left for output: '+(1000-v)+'K tokens'}
$('#mtp-in').oninput=win;win();
// bench
var M=['Gemini 4 Argon','GPT-6 Astra','Claude Opus 5.5','Claude Fable 5.1'],C=['#4285F4','#9AA0A6','#C58AF9','#F28B82'];
var B=[
{n:'Vals Index',d:2,v:[68.90,63.13,66.97,65.83],src:'Independent: Vals AI leaderboard (68.90%, #1).'},
{n:'DeepSWE v1.1',v:[77.9,74.1,74.2,67.4],src:'Argon self-computed with a mini-swe-agent harness; rivals from system cards and leaderboard.'},
{n:'AutomationBench',v:[51.3,41.4,42.5,31.4],src:'Zapier public leaderboard, private set.'},
{n:'LVBench',v:[91.7,87.5,83.7,79.7],src:'Self-computed without tools. Gemini sampled at 1 FPS.'},
{n:'GraphWalks 256K to 1M',v:[84.2,71.8,66.8,65.0],src:'Self-computed for all models on 200 problems.'},
{n:'CWE-bench v1',v:[68.0,68.0,67.0,58.0],src:'Official public leaderboard. Argon ties GPT-6 Astra.'},
{n:'FrontierSWE v2',v:[55.0,65.5,62.3,56.3],src:'Proximal public leaderboard. Argon is last of 4.',lose:1},
{n:'Terminal-Bench 4.0',v:[57.4,58.2,66.4,57.9],src:'Argon self-computed; rivals from the public leaderboard. Argon is last of 4.',lose:1}];
var cur=0,ch=$('#mtp-chips');
B.forEach(function(b,i){var c=document.createElement('button');c.className='chip'+(i===0?' on':'')+(b.lose?' lose':'');c.textContent=b.n;c.onclick=function(){$$('.chip').forEach(function(x){x.classList.remove('on')});c.classList.add('on');drawB(i)};ch.appendChild(c)});
var rows=$('#mtp-rows');M.forEach(function(m,i){rows.insertAdjacentHTML('beforeend','<div class="row"><span class="nm">'+m+'</span><div class="track"><div class="fill" style="background:'+C[i]+'"></div></div><span class="val">0%</span></div>')});
function drawB(i){cur=i;var b=B[i],f=$$('#mtp-rows .fill'),v=$$('#mtp-rows .val');f.forEach(function(x){x.style.width='0'});setTimeout(function(){b.v.forEach(function(x,k){f[k].style.width=x+'%';v[k].textContent=x.toFixed(b.d||1)+'%'})},30);$('#mtp-bnote').textContent=b.src+' Dashed chips mark benchmarks where Argon trails. Scores from Google\'s eval table unless noted.'}
// price
var P={intro:[[2,10],[10,50],[4,20],[10,50]],std:[[4,20],[10,50],[4,20],[10,50]]},pm='intro';
$$('.seg button').forEach(function(b){b.onclick=function(){$$('.seg button').forEach(function(x){x.classList.remove('on')});b.classList.add('on');pm=b.dataset.p;drawP()}});
var pr=$('#mtp-prows');M.forEach(function(m,i){pr.insertAdjacentHTML('beforeend','<div class="row"><span class="nm">'+m+'</span><div class="track"><div class="fill" style="background:'+C[i]+'"></div></div><span class="val">$0</span></div>')});
function drawP(){var a=+$('#mtp-rin').value,o=+$('#mtp-rout').value;$('#mtp-ci').textContent=a+'M';$('#mtp-co').textContent=o+'M';var c=P[pm].map(function(p){return a*p[0]+o*p[1]}),mx=Math.max.apply(null,c),f=$$('#mtp-prows .fill'),v=$$('#mtp-prows .val');c.forEach(function(x,k){f[k].style.width=(x/mx*100)+'%';v[k].textContent='$'+Math.round(x).toLocaleString()})}
$('#mtp-rin').oninput=drawP;$('#mtp-rout').oninput=drawP;
window.addEventListener('load',resize);window.addEventListener('resize',resize);setTimeout(resize,300);
})();
</script>
</body></html>
" style="width:100%;height:600px;border:0;display:block;background:transparent;" loading="lazy" scrolling="no"> 

(function(){var f=document.getElementById('mtp-g4a-frame');window.addEventListener('message',function(e){if(e.data&&e.data.id==='mtp-g4a'&&e.data.mtpH&&e.source===f.contentWindow){f.style.height=e.data.mtpH+'px';}});})();

 Gemini 4 Argon vs GPT-6 Astra vs Claude Opus 5.5 vs Claude Fable 5.1 

 Feature Gemini 4 Argon GPT-6 Astra Claude Opus 5.5 Claude Fable 5.1 Architecture Sparse MoE transformer Not disclosed Not disclosed Not disclosed Total / active params Not disclosed Not disclosed Not disclosed Not disclosed Context window 1M (input + output combined) 1,050,000 1M 1M Max output Up to 1M 128K 128K 128K Input modalities Text, image, audio, video Text, image Text, image Text, image Knowledge cutoff Mar 2026 Apr 30, 2026 Jun 2026 Jun 2026 API price (in / out per 1M) $2 / $10 intro, $4 / $20 after Nov 30 $10 / $50 $4 / $20 $10 / $50 License / access Proprietary, API only Proprietary, API only Proprietary, API only Proprietary, API only Vals Index 68.90% 63.13% 66.97% 65.83% DeepSWE v1.1 (Google table) 77.9% 74.1% 74.2% 67.4% Terminal-Bench 4.0 (Google table) 57.4% 58.2% 66.4% 57.9% FrontierSWE v2 (Google table) 55.0% 65.5% 62.3% 56.3% 

 What did Google use Argon for before launch? 

 Google shared internal results in its launch post : 

 Argon in Antigravity raised agentic code submissions by over 35% and cut rollbacks by nearly a third. 

 It delivered a 2.85x end-to-end vLLM inference speedup for Gemma 4 E2B on an A100. 

 In Google’s open-source Agent Development Kit , it cut session prep time by 40%. Cold imports got 21% faster. 

 On Gray Swan’s indirect prompt injection benchmark, attack success fell to 0.7% across 15 adaptive attempts. 

 How much does Gemini 4 Argon cost, and where can you use it? 

 Introductory pricing is $2 input and $10 output per million tokens. Cached input tokens are 95% off. After November 30, 2026, the price rises to $4 and $20. That matches Claude Opus 5.5 and sits below GPT-6 Astra’s $10 and $50. 

 Access paths, per the developer post : 

 Developers: Gemini API paid tier in AI Studio and Android Studio. 

 Enterprises: Gemini platform, Gemini for business and Google Antigravity. 

 Consumers: Gemini app and AI Mode in Search for Google AI Pro and Ultra subscribers. 

 Cyber defenders: the Fairwind Program , with access to Argon without cyber guardrails. 

 Key Takeaways 

 Argon is a sparse MoE model with a 1M token output limit. 

 It ranks #1 on the Vals Index at 68.90%. 

 Intro pricing is $2/$10 per million tokens until November 30. 

 It trails rivals on FrontierSWE v2 and Terminal-Bench 4.0. 

 Most rival scores in Google’s table are self-reported. 

 Check out the Model Card , Evaluation Methodology and Developer Guide . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Google Releases Gemini 4 Argon API With 1M Token Output Limit appeared first on MarkTechPost .
