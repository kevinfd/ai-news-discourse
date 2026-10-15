---
id: "8ff623edf7b5b382"
title: "Meet Grok Voice 3.0: SpaceXAI Voice Agent Model Ranks #1 on Artificial Analysis"
url: "https://marktechpost.com/2026/10/14/meet-grok-voice-3-0-spacexai-voice-agent-model-ranks-1-on-artificial-analysis"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T05:18:54Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Michal Sutter"]
language: "en"
summary: "SpaceXAI just released Grok Voice 3.0 . Grok Voice 3.0 is a SpaceXAI speech-to-speech model that listens, reasons, calls tools and speaks. It now ranks first on the Artificial Analysis Speech-to-Speech Index with a score of 86.9. For developers, the endpoint, events and $0.08 per minute price are unchanged from Grok Voice 2.0. \n\n TL;DR \n\n Runs on: SpaceXAI’s hosted Voice Agent API only. No open…"
tags: ["Agentic AI", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "Language Model", "New Releases", "Python", "Staff", "Tech News", "Technology", "TTS", "Uncategorized"]
orgs: ["xAI", "Google"]
topics: ["models & research", "agents & coding", "search & media"]
content_source: "summary"
word_count: 1508
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Grok Voice 3.0: SpaceXAI Voice Agent Model Ranks #1 on Artificial Analysis

MarkTechPost · Michal Sutter · 2026-10-15

SpaceXAI just released Grok Voice 3.0 . Grok Voice 3.0 is a SpaceXAI speech-to-speech model that listens, reasons, calls tools and speaks. It now ranks first on the Artificial Analysis Speech-to-Speech Index with a score of 86.9. For developers, the endpoint, events and $0.08 per minute price are unchanged from Grok Voice 2.0. 

 TL;DR 

 Runs on: SpaceXAI’s hosted Voice Agent API only. No open weights, no local or quantized variants. 

 Performance: Highest Index score of any model Artificial Analysis currently ranks. 

 Best: 86.9 on the AA Speech-to-Speech Index, ranked #1. 

 Worst: 71.6% on τ-Voice, behind GPT-Live-1 (Astra, medium) at 74.5%. 

 Bottom line: 
 
 Best: top composite score at 0.81 s time to first audio. 

 Worst: not the leader on agentic task resolution or raw speech reasoning. 

 What is Grok Voice 3.0? 

 Grok Voice 3.0 is SpaceXAI’s flagship realtime voice model, exposed as grok-voice-3.0 on the /v1/realtime WebSocket endpoint . The grok-voice-latest alias already points to it, so existing agents switched automatically. 

 SpaceXAI has not published parameter counts or architecture details. Reasoning is on by default ( reasoning.effort: "high" ) and can be set to "none" for faster turns. Server-side voice activity detection handles barge-in. Tools run inside the session: collections search, web search, X search, remote MCP servers and custom functions. 

 How does Grok Voice 3.0 perform on benchmarks? 

 The AA Speech-to-Speech Index is an equal-weighted average of 4 components. Those are Big Bench Audio reasoning, τ-Voice agentic performance, Speech Agent Arena preference and task success rate. 

 Grok Voice 3.0 scores 86.9. GPT-Live-1 (Astra, medium) scores 83.2, Gemini 3.8 Live Extended Thinking 82.6. Grok Voice 2.0 scored 81.3. 

 Component results are strong, not uniformly first: 

 Big Bench Audio: 98.5%, ranked 4th. StepAudio 3 Realtime leads at 99.7%. 

 Full Duplex Bench: 97.0%, ranked 4th. StepAudio 3 Realtime leads at 98.9%. 

 Task success rate: 94.8%, up from 94.6% for Grok Voice 2.0. 

 Speech Agent Arena Elo: 1070, the highest among the 4 models compared here. 

 τ-Voice: 71.6%, up from 56.5%, but below GPT-Live-1 (Astra, medium) at 74.5%. 

 ServiceNow’s EVA-Bench scores enterprise voice agents on accuracy and experience. SpaceXAI reports a top accuracy score of 74%. 

 Is Grok Voice 3.0 fast and cheap? 

 Artificial Analysis measures 0.81 s time to first audio. GPT-Live-1 (Astra, medium) measures 1.34 s, so SpaceXAI’s “40% lower latency” claim checks out. Grok Voice 2.0 was faster, though, at 0.70 s. 

 On cost, SpaceXAI cites Artificial Analysis cost per Big Bench Audio task. Grok Voice 3.0 costs $0.025 per task, versus $0.030 for GPT-Live-1 (Astra, medium) and $0.055 for GPT-Realtime-2.1 (High). On AA’s cost per hour of input audio, Gemini 3.8 Live Extended Thinking is cheaper: $3.50 versus $4.80. 

 List prices are not directly comparable. GPT-Live-1 costs $0.05 per minute, but backend model and tool usage is billed separately. Gemini 3.8 Live bills audio per minute plus text tokens. 

 Back</button><button class="btn" id="gvNext">Next </button><button class="btn" id="gvPlay">Auto-play</button></div>
 </div>

 <div class="pnl" id="p2">
 <div class="chips" id="gvChips"></div>
 <div id="gvBars"></div>
 <p class="note" id="gvNote"></p>
 </div>

 <div class="pnl" id="p3">
 <svg viewBox="0 0 640 330" width="100%" role="img" aria-label="τ-Voice success rate versus time to first audio">
 <rect x="0" y="0" width="640" height="330" fill="transparent"/>
 <g stroke="#2a2a2a">
 <line x1="70" y1="30" x2="70" y2="280"/><line x1="70" y1="280" x2="610" y2="280"/>
 <line x1="70" y1="196.7" x2="610" y2="196.7" stroke-dasharray="3 4"/><line x1="70" y1="113.3" x2="610" y2="113.3" stroke-dasharray="3 4"/>
 <line x1="70" y1="30" x2="610" y2="30" stroke-dasharray="3 4"/>
 </g>
 <g fill="#9a9a9a" font-size="11">
 <text x="62" y="284" text-anchor="end">50%</text><text x="62" y="201" text-anchor="end">60%</text><text x="62" y="117" text-anchor="end">70%</text><text x="62" y="34" text-anchor="end">80%</text>
 <text x="70" y="298" text-anchor="middle">0.5 s</text><text x="205" y="298" text-anchor="middle">0.75 s</text><text x="340" y="298" text-anchor="middle">1.0 s</text><text x="475" y="298" text-anchor="middle">1.25 s</text><text x="610" y="298" text-anchor="middle">1.5 s</text>
 <text x="340" y="320" text-anchor="middle">Time to first audio (lower is faster)</text>
 <text x="16" y="155" text-anchor="middle" transform="rotate(-90 16 155)">τ-Voice success</text>
 </g>
 <text x="84" y="50" fill="#ffffff" font-size="12" font-weight="700"> better</text>
 <g id="gvDots"></g>
 </svg>
 <p class="note">Source: Artificial Analysis, accessed October 14, 2026. Grok Voice 3.0 trails GPT-Live-1 (Astra, medium) by 2.9 points on τ-Voice but reaches first audio 0.53 s sooner.</p>
 </div>

 <div class="pnl" id="p4">
 <div class="kv">
 <div class="k"><b>$0.08/min</b><span>$4.80/hr, same as Grok Voice 2.0</span></div>
 <div class="k"><b>0.81 s</b><span>time to first audio (AA)</span></div>
 <div class="k"><b>28</b><span>built-in voices, plus cloning</span></div>
 <div class="k"><b>20</b><span>listed locales, auto-detected</span></div>
 <div class="k"><b>5</b><span>tool types: files, web, X, MCP, functions</span></div>
 <div class="k"><b>SIP</b><span>phone and contact-center routing</span></div>
 </div>
<pre><code>wss://api.x.ai/v1/realtime?model=grok-voice-3.0

{"type": "session.update",
 "session": {
 "voice": "eve",
 "reasoning": {"effort": "high"},
 "turn_detection": {"type": "server_vad"},
 "tools": [{"type": "web_search"}]
 }}</code></pre>
 <p class="note">The <code>grok-voice-latest</code> alias already points to <code>grok-voice-3.0</code>. Pin the versioned name in production. Grok Voice 2.0 is deprecated.</p>
 </div>

 <div class="ft"><span>Data: <a href="https://x.ai/news/grok-voice-3" target="_blank" rel="noopener">SpaceXAI</a>, <a href="https://artificialanalysis.ai/speech-to-speech" target="_blank" rel="noopener">Artificial Analysis</a>, <a href="https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech" target="_blank" rel="noopener">SpaceXAI docs</a></span><span class="brand">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-gv3');
function post(){try{parent.postMessage({mtpEmbed:'gv3',height:R.offsetHeight+40},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){
 R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});
 R.querySelectorAll('.pnl').forEach(function(x){x.classList.remove('on')});
 t.classList.add('on');document.getElementById(t.dataset.p).classList.add('on');
 if(t.dataset.p==='p2')drawBars();if(t.dataset.p==='p3')drawDots();setTimeout(post,60);});});
/* wave */
var w=document.getElementById('gvWave');for(var i=0;i<48;i++){var b=document.createElement('i');b.style.animationDelay=(i*0.045)+'s';w.appendChild(b);}
/* pipeline */
var S=[
['Caller speaks','Audio streams over a WebSocket (or SIP for phone calls) as PCM at 8 to 48 kHz, G.711 or Opus.'],
['Turn detection','Server-side voice activity detection decides when the caller has finished, and handles barge-in when they interrupt.'],
['Reasoning','Reasoning is on by default with reasoning.effort set to "high". Set it to "none" for faster, simpler turns.'],
['Tools','The agent can call collections search, web search, X search, remote MCP servers and your own functions mid-call.'],
['Reply streams','Audio deltas stream back as soon as they are ready. Artificial Analysis measures 0.81 s to first audio.']];
var F=document.getElementById('gvFlow'),cur=0,timer=null;
S.forEach(function(s,i){var b=document.createElement('button');b.className='st';b.innerHTML='<div class="n">STEP '+(i+1)+'</div><div class="t">'+s[0]+'</div>';
 b.addEventListener('click',function(){stop();show(i)});F.appendChild(b);});
function show(i){cur=(i+S.length)%S.length;F.querySelectorAll('.st').forEach(function(x,j){x.classList.toggle('on',j===cur)});
 document.getElementById('gvDt').textContent=S[cur][0];document.getElementById('gvDp').textContent=S[cur][1];}
function stop(){if(timer){clearInterval(timer);timer=null;document.getElementById('gvPlay').textContent='Auto-play';}}
document.getElementById('gvPrev').onclick=function(){stop();show(cur-1)};
document.getElementById('gvNext').onclick=function(){stop();show(cur+1)};
document.getElementById('gvPlay').onclick=function(){if(timer){stop();return}this.textContent='Pause';timer=setInterval(function(){show(cur+1)},2200)};
show(0);
/* bars */
var M=['Grok Voice 3.0','Grok Voice 2.0','GPT-Live-1 (Astra, medium)','Gemini 3.8 Live Ext. Thinking'];
var B={
'AA Index':{v:[86.9,81.3,83.2,82.6],max:100,f:function(x){return x.toFixed(1)},n:'Equal-weighted average of Big Bench Audio, τ-Voice, Arena preference and task success.'},
'Big Bench Audio':{v:[98.5,97.2,90.1,97.7],max:100,f:function(x){return x.toFixed(1)+'%'},n:'Speech reasoning. Grok Voice 3.0 ranks 4th overall; StepAudio 3 Realtime leads at 99.7%.'},
'τ-Voice':{v:[71.6,56.5,74.5,68.6],max:100,f:function(x){return x.toFixed(1)+'%'},n:'Replica customer-support calls with tools. GPT-Live-1 (Astra, medium) leads this group.'},
'Full Duplex Bench':{v:[97.0,95.1,94.9,91.9],max:100,f:function(x){return x.toFixed(1)+'%'},n:'Pauses, turn-taking, interruptions and backchannels.'},
'Task success':{v:[94.8,94.6,87.4,89.1],max:100,f:function(x){return x.toFixed(1)+'%'},n:'Share of conversations ending in the correct final tool call.'},
'Arena Elo':{v:[1070,1011,1056,993],max:1100,f:function(x){return String(x)},n:'Live Speech Agent Arena Elo on Artificial Analysis. Higher is preferred.'},
'Time to first audio':{v:[0.81,0.70,1.34,1.35],max:1.5,f:function(x){return x.toFixed(2)+' s'},n:'Lower is faster. Grok Voice 2.0 was quicker than 3.0.'}};
var C=document.getElementById('gvChips'),BR=document.getElementById('gvBars'),key='AA Index';
Object.keys(B).forEach(function(k){var c=document.createElement('button');c.className='chip'+(k===key?' on':'');c.textContent=k;
 c.onclick=function(){key=k;C.querySelectorAll('.chip').forEach(function(x){x.classList.toggle('on',x===c)});drawBars()};C.appendChild(c);});
M.forEach(function(m,i){var r=document.createElement('div');r.className='row';
 r.innerHTML='<div class="lbl">'+m+'</div><div class="trk"><div class="fill'+(i===0?' me':'')+'"></div></div><div class="val"></div>';BR.appendChild(r);});
function drawBars(){var d=B[key];BR.querySelectorAll('.row').forEach(function(r,i){var f=r.querySelector('.fill');f.style.width='0';
 r.querySelector('.val').textContent=d.f(d.v[i]);setTimeout(function(){f.style.width=(d.v[i]/d.max*100)+'%'},40+i*90)});
 document.getElementById('gvNote').textContent=d.n+' Source: Artificial Analysis / SpaceXAI.';}
drawBars();
/* scatter */
var P=[['Grok Voice 3.0','0.81 s · 71.6%',0.81,71.6,1,'r'],['Grok Voice 2.0','0.70 s · 56.5%',0.70,56.5,0,'r'],['GPT-Live-1 (Astra, medium)','1.34 s · 74.5%',1.34,74.5,0,'l'],['Gemini 3.8 Live Ext. Thinking','1.35 s · 68.6%',1.35,68.6,0,'l']];
var G=document.getElementById('gvDots'),NS='http://www.w3.org/2000/svg';
P.forEach(function(p){var x=70+(p[2]-0.5)*540,y=280-(p[3]-50)/30*250;var g=document.createElementNS(NS,'g');g.setAttribute('class','dot');
 var c=document.createElementNS(NS,'circle');c.setAttribute('cx',x);c.setAttribute('cy',y);c.setAttribute('r',p[4]?9:7);
 c.setAttribute('fill',p[4]?'#ffffff':'#5c5c5c');c.setAttribute('stroke',p[4]?'#ffffff':'#9a9a9a');g.appendChild(c);
 [[p[0],0,p[4]?'700':'600'],[p[1],15,'500']].forEach(function(L){var t=document.createElementNS(NS,'text');
 t.setAttribute('x',p[5]==='r'?x+14:x-14);t.setAttribute('y',y-2+L[1]);t.setAttribute('text-anchor',p[5]==='r'?'start':'end');
 t.setAttribute('fill',p[4]?'#ffffff':'#bdbdbd');t.setAttribute('font-size','12');t.setAttribute('font-weight',L[2]);t.textContent=L[0];g.appendChild(t);});
 G.appendChild(g);});
function drawDots(){G.querySelectorAll('.dot').forEach(function(g,i){g.style.opacity='0';g.style.transform='translateY(30px)';
 setTimeout(function(){g.style.opacity='1';g.style.transform='none'},80+i*150)});}
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body>
</html>
"> 

window.addEventListener('message',function(e){var d=e.data;if(d&&d.mtpEmbed==='gv3'&&d.height){var f=document.getElementById('mtp-gv3-frame');if(f)f.style.height=d.height+'px';}});

 How does Grok Voice 3.0 compare to GPT-Live-1 and Gemini 3.8 Live? 

 Feature Grok Voice 3.0 Grok Voice 2.0 GPT-Live-1 (Astra, medium) Gemini 3.8 Live Extended Thinking Developer SpaceXAI SpaceXAI OpenAI Google Parameters Not disclosed Not disclosed Not disclosed Not disclosed Context length Not disclosed Not disclosed Not disclosed Not disclosed Weights Closed, API only Closed, deprecated Closed, API only Closed, API only Input / output Audio, text / audio, text Audio, text / audio, text Audio, text / audio, text Text, image, video, audio / audio, text AA Speech-to-Speech Index 86.9 81.3 83.2 82.6 Big Bench Audio 98.5% 97.2% 90.1% 97.7% τ-Voice 71.6% 56.5% 74.5% 68.6% Full Duplex Bench 97.0% 95.1% 94.9% 91.9% Task success rate 94.8% 94.6% 87.4% 89.1% Arena Elo (AA live) 1070 1011 1056 993 Time to first audio 0.81 s 0.70 s 1.34 s 1.35 s AA cost per hour input audio $4.80 $4.80 $5.83 $3.50 List price $0.08/min $0.08/min $0.05/min plus backend usage $0.005/min audio in, $0.018/min audio out, plus text tokens 

 Benchmark data: Artificial Analysis , accessed October 14, 2026. SpaceXAI’s blog lists frozen Arena Elo values of 1048 (GPT-Live-1) and 990 (Gemini). 

 How do developers deploy Grok Voice 3.0? 

 The API is compatible with the OpenAI Realtime API , so migration mostly means a new URL and key. 

 Transports: WebSocket, WebRTC demo apps, and SIP for phone and contact-center calls. 

 Audio: PCM at 8 to 48 kHz, G.711 μ-law and A-law, and Opus. 

 Voices: 28 built-in voices, plus custom voices cloned from a reference clip of up to 120 s. 

 Languages: 20 listed locales with automatic language detection. 

 Extensions: force_message for scripted lines, pronunciation replace maps, and 30-minute session resumption. 

 Compliance: SOC 2 Type II, HIPAA eligible with a BAA, and GDPR. SpaceXAI says audio is not stored or used for training. 

 Production teams should pin grok-voice-3.0 rather than the alias. Grok Voice 2.0 is now deprecated. 

 Key Takeaways 

 Grok Voice 3.0 ranks #1 on the AA Speech-to-Speech Index at 86.9. 

 It answers in 0.81 s, 40% lower latency than GPT-Live-1 (Astra, medium). 

 τ-Voice jumped to 71.6%, but GPT-Live-1 still leads at 74.5%. 

 Price stays at $0.08 per minute, and grok-voice-latest upgraded automatically. 

 It is API only: no weights, no disclosed size. 

 Check out the official announcement , the Speech to Speech docs and the Artificial Analysis leaderboard . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post Meet Grok Voice 3.0: SpaceXAI Voice Agent Model Ranks #1 on Artificial Analysis appeared first on MarkTechPost .
