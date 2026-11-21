---
id: "26f369d6758ae86f"
title: "OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min"
url: "https://marktechpost.com/2026/11/21/openai-gpt-live-1-1-api-standby-mode"
link: "https://marktechpost.com/2026/11/21/openai-gpt-live-1-1-api-standby-mode"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-21T11:46:17Z"
published_date: "2026-11-21"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Michal Sutter"]
language: "en"
summary: "OpenAI has made GPT-Live-1.1 available in its API under the model ID gpt-live-1.1 . The GPT-Live-1.1 voice model is a full-duplex model for multilingual conversations. It can listen while it speaks. OpenAI team states that it speaks with more natural and consistent accents across languages and completes tasks more reliably. The release also adds standby, a cheaper billing state for idle…"
tags: ["Agentic AI", "AI Agents", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "Language Model", "New Releases", "Staff", "Tech News", "Technology"]
orgs: ["OpenAI", "Google"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 1388
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min

MarkTechPost · Michal Sutter · 2026-11-21

OpenAI has made GPT-Live-1.1 available in its API under the model ID gpt-live-1.1 . The GPT-Live-1.1 voice model is a full-duplex model for multilingual conversations. It can listen while it speaks. OpenAI team states that it speaks with more natural and consistent accents across languages and completes tasks more reliably. The release also adds standby, a cheaper billing state for idle sessions. For teams running voice agents, idle time on a call now costs less. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Size: Live sessions hold a 128,000-token default context window . 

 Runs on: OpenAI’s cloud only, via v1/live/sessions . Clients connect over WebRTC or WebSocket. No open weights, no quantized variants. 

 Performance: OpenAI claims better accents, transcription, letter and number handling, and task completion than GPT-Live-1. No scores published. 

 Best: Standby bills idle WebRTC time at $0.02 per minute versus $0.05 active , a 60% lower rate. 

 Worst: OpenAI published 0 benchmark scores for 1.1. Image, video and structured outputs are not supported. 

 Bottom line: Best: cheaper always-on voice sessions. Worst: quality gains are self-reported with no numbers. 

 What is GPT-Live-1.1? 

 GPT-Live-1.1 is a full-duplex speech model from OpenAI that hears and speaks in 1 stream. It follows GPT-Live-1, which reached the API on September 10, 2026 . As per the OpenAI forum announcement , it has powered ChatGPT Plus and Pro voice since October 15. 

 Inputs and outputs are audio and text. Image and video are not supported. Streaming and function calling work. Structured outputs, fine-tuning and predicted outputs do not. 

 How does GPT-Live-1.1 work? 

 The GPT-Live family replaces the usual cascade of speech-to-text, an LLM and text-to-speech. OpenAI says the model reasons over incoming and outgoing audio together in a single model . It also handles turn detection and returns ASR transcripts natively. 

 Deeper work is delegated. The voice model can hand reasoning and tool calls to a backend text model. OpenAI names GPT-6 Astra for complex issues and Luna for high-volume tasks. Third-party backends also work. 

 The Live conversations guide sets delegation.type to client or responses . Responses mode uses OpenAI models. Client mode connects your own backend. Instructions can run up to 16,384 tokens. 

 What changed from GPT-Live-1? 

 OpenAI lists 4 improvement areas for 1.1: 

 More natural and consistent accents across languages 

 More accurate speech transcription 

 Better handling of precise details like letters and numbers 

 More reliable instruction following and task completion 

 How does standby mode work? 

 Standby pauses inference during silence while the WebRTC connection stays open. The guide documents 3 settings: 

 session.wake_policy.type : set to speech , so inference waits for speech 

 session.idle_timeout_s : a whole number from 5 to 60 seconds 

 session.wake_policy.vad_threshold : optional, 0 to 1, default 0.5 

 After the timeout, the server emits session.paused . When the user speaks, session.resumed fires. The session ID and history are kept. OpenAI warns the first reply after a short utterance may be slower. Keep the microphone track active during standby. 

 Standby works for both GPT-Live-1 and GPT-Live-1.1. 

 How much does GPT-Live-1.1 cost? 

 Session state Price per minute Price per hour Active $0.05 $3.00 Standby (WebRTC, inference paused) $0.02 $1.20 

 Voice sessions are billed by duration. The GPT-Live-1 model page says billing is per second. Backend model and tool usage are billed separately. That matters: a heavy backend can cost more than the voice layer. 

 Deployment and availability 

 The model is API-only. You switch an existing Live session by setting model to gpt-live-1.1 . Changing the model requires a new session. 

 Outbound SIP calling reached all organizations on November 2, so phone agents are supported. GPT-Live-1 and GPT-Live-1.1 have separate concurrent-session limits. Each limit applies across inference regions. The 1.1 page does not publish tier numbers. 

 How does GPT-Live-1.1 compare? 

 Feature GPT-Live-1.1 GPT-Live-1 GPT-Realtime-2.1 Gemini 3.8 Live Developer OpenAI OpenAI OpenAI Google Parameters Not disclosed Not disclosed Not disclosed Not disclosed Input Audio, text Audio, text Text, audio, image Text, image, audio Output Audio, text Audio, text Text, audio Text, audio Context 128K default ( guide ) 128K default ( guide ) 128K, 32K max output 131,072 in, 65,536 out Pricing $0.05/min active, $0.02/min standby $0.05/min active, $0.02/min standby $32 / $64 per 1M audio tokens (in/out) Token-based ( pricing ) Idle standby billing Yes (WebRTC) Yes (WebRTC) Not documented Not documented Reasoning Delegated to backend model Delegated to backend model Built in, configurable effort Interleaved reasoning Function calling Yes Yes Yes Yes Structured outputs No No Not disclosed No Published benchmarks None for 1.1 Full Duplex Bench +30 pts vs GPT-Realtime-2.1 Baseline in that eval Not compared License / weights Closed, API only Closed, API only Closed, API only Closed, API only 

 Simulate a call</button><button class="btn gh" id="gl11rst">Reset</button></div>
 <pre class="log" id="gl11log">Press Simulate to walk through the standby events.</pre>
 <p class="note">WebRTC only. Keep the mic track active. Session ID and history are kept. First reply after a short utterance may be slower.</p>
 </div>

 <div class="pn" id="gl11p2">
 <label>Session length: <span class="val" id="gl11mv">60</span> min</label>
 <input type="range" id="gl11min" min="1" max="480" value="60">
 <label>Share of the session that is idle (in standby): <span class="val" id="gl11iv">50</span>%</label>
 <input type="range" id="gl11idle" min="0" max="95" value="50">
 <div class="bars">
 <div class="bar"><div class="lb"><span>All minutes at active rate ($0.05)</span><span class="val" id="gl11c0">$3.00</span></div><div class="tr"><div class="fl" id="gl11b0" style="background:#F0A06A"></div></div></div>
 <div class="bar"><div class="lb"><span>With standby ($0.02 on idle minutes)</span><span class="val" id="gl11c1">$2.10</span></div><div class="tr"><div class="fl" id="gl11b1" style="background:#7EA4FA"></div></div></div>
 </div>
 <p class="note" id="gl11sv">Voice layer only. Illustrative: the timeout window itself bills at the active rate, and backend model and tool usage are billed separately.</p>
 </div>

 <div class="pn" id="gl11p3">
 <div class="grid">
 <div class="card"><h4>Accents <span class="plus">+</span></h4><p>More natural and consistent accents across languages, per OpenAI.</p></div>
 <div class="card"><h4>Transcription <span class="plus">+</span></h4><p>Transcribes speech more accurately than GPT-Live-1, per the model page.</p></div>
 <div class="card"><h4>Letters and numbers <span class="plus">+</span></h4><p>Better handling of precise details like letters and numbers.</p></div>
 <div class="card"><h4>Task completion <span class="plus">+</span></h4><p>More reliable instruction following and task completion.</p></div>
 </div>
 <div class="bars">
 <div class="bar"><div class="lb"><span>Active rate</span><span class="val">$0.05/min</span></div><div class="tr"><div class="fl gl11pb" data-w="100" style="background:#F0A06A"></div></div></div>
 <div class="bar"><div class="lb"><span>Standby rate (new, also on GPT-Live-1)</span><span class="val">$0.02/min</span></div><div class="tr"><div class="fl gl11pb" data-w="40" style="background:#7EA4FA"></div></div></div>
 </div>
 <p class="note">OpenAI published no benchmark scores for 1.1. All 4 gains above are self-reported.</p>
 </div>

 <div class="ft">
 <span>Sources: <a href="https://developers.openai.com/api/docs/models/gpt-live-1.1" target="_blank" rel="noopener">model page</a> · <a href="https://developers.openai.com/api/docs/guides/live-conversations" target="_blank" rel="noopener">Live guide</a></span>
 <span class="brand">Built by Marktechpost</span>
 </div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-gl11');
function $(i){return document.getElementById(i)}
function resize(){try{parent.postMessage({mtpFrame:'gl11',height:R.offsetHeight+40},'*')}catch(e){}}
var tabs=R.querySelectorAll('.tab');
for(var i=0;i<tabs.length;i++){tabs[i].addEventListener('click',function(){
 for(var j=0;j<tabs.length;j++){tabs[j].classList.remove('on');$('gl11p'+j).classList.remove('on')}
 this.classList.add('on');var t=this.getAttribute('data-t');$('gl11p'+t).classList.add('on');
 if(t==='2')calc(); if(t==='3')priceBars(); setTimeout(resize,60);
})}
/* step-through */
var steps=[
 {on:['gl11n0','gl11a0','gl11n1'],t:'1. Caller audio streams in. The model keeps listening even while it is speaking (full duplex).',c:'Step 1 of 3'},
 {on:['gl11n1','gl11a2','gl11n2'],t:'2. For reasoning or tools, the voice model delegates to a backend model while the conversation continues.',c:'Step 2 of 3'},
 {on:['gl11n2','gl11a3','gl11n1','gl11a1','gl11n0'],t:'3. The result returns and is spoken back. ASR transcripts and response text come back natively.',c:'Step 3 of 3'}];
var ids=['gl11n0','gl11n1','gl11n2','gl11a0','gl11a1','gl11a2','gl11a3'],si=-1;
function showAll(){ids.forEach(function(x){$(x).classList.remove('dim')})}
$('gl11next').addEventListener('click',function(){si=(si+1)%steps.length;var s=steps[si];
 ids.forEach(function(x){$(x).classList.toggle('dim',s.on.indexOf(x)<0)});$('gl11st').textContent=s.t;$('gl11ct').textContent=s.c;});
$('gl11all').addEventListener('click',function(){si=-1;showAll();$('gl11st').textContent='One model handles listening and speaking. No separate speech-to-text and text-to-speech chain.';$('gl11ct').textContent='Overview'});
/* standby */
$('gl11to').addEventListener('input',function(){$('gl11tv').textContent=this.value;$('gl11s1').style.flexGrow=(1+this.value/15).toFixed(2)});
var timers=[];
function rst(){timers.forEach(clearTimeout);timers=[];for(var k=0;k<4;k++)$('gl11s'+k).classList.remove('lit');$('gl11log').innerHTML='Press Simulate to walk through the standby events.'}
$('gl11rst').addEventListener('click',rst);
$('gl11sim').addEventListener('click',function(){rst();var to=$('gl11to').value;var L=$('gl11log');L.innerHTML='';
 var ev=[[0,'<b>session.resumed</b> first wake on speech, inference active ($0.05/min)'],
 [1,'silence detected, waiting '+to+' s (idle_timeout_s)'],
 [2,'<b>session.paused</b> standby, WebRTC call stays open ($0.02/min)'],
 [3,'user speaks, <b>session.resumed</b> same session ID, history restored']];
 ev.forEach(function(e,n){timers.push(setTimeout(function(){$('gl11s'+e[0]).classList.add('lit');L.innerHTML+=(n?'\n':'')+e[1];resize()},n*1100))});
});
/* calculator */
function money(v){return '$'+v.toFixed(2)}
function calc(){var m=+$('gl11min').value,p=+$('gl11idle').value/100;$('gl11mv').textContent=m;$('gl11iv').textContent=Math.round(p*100);
 var a=m*0.05,b=m*(1-p)*0.05+m*p*0.02;$('gl11c0').textContent=money(a);$('gl11c1').textContent=money(b);
 $('gl11b0').style.width='100%';$('gl11b1').style.width=(a?b/a*100:0)+'%';
 $('gl11sv').textContent='Saves '+money(a-b)+' ('+(a?((a-b)/a*100).toFixed(0):0)+'%) on the voice layer. Illustrative: the timeout window itself bills at the active rate, and backend model and tool usage are billed separately.'}
$('gl11min').addEventListener('input',calc);$('gl11idle').addEventListener('input',calc);
function priceBars(){var b=R.querySelectorAll('.gl11pb');for(var k=0;k<b.length;k++){b[k].style.width='0';(function(el){setTimeout(function(){el.style.width=el.getAttribute('data-w')+'%'},50)})(b[k])}}
var cards=R.querySelectorAll('.card');for(var c=0;c<cards.length;c++){cards[c].addEventListener('click',function(){this.classList.toggle('open');this.querySelector('.plus').textContent=this.classList.contains('open')?'−':'+';setTimeout(resize,420)})}
window.addEventListener('load',resize);window.addEventListener('resize',resize);setTimeout(resize,300);
})();
</script>
</body></html>"> 
 
 window.addEventListener("message",function(e){if(e.data&&e.data.mtpFrame==="gl11"&&e.data.height){document.getElementById("mtp-gl11-frame").style.height=e.data.height+"px";}}); 

 Key Takeaways 

 GPT-Live-1.1 is live in the API as gpt-live-1.1 . 

 Standby cuts idle WebRTC billing from $0.05 to $0.02 per minute. 

 Idle timeout is configurable from 5 to 60 seconds. 

 Accent, transcription and task gains are self-reported, with no scores. 

 Backend reasoning and tools are billed separately from voice minutes. 

 Check out the model page , the Live conversations guide and the announcement . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min appeared first on MarkTechPost .
