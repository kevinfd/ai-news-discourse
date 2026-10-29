---
id: "87e653089faad0c3"
title: "AssemblyAI Ships AssemblyAI-TTS-1: A $15 per 1M Character Text-to-Speech API for Voice Agents"
url: "https://marktechpost.com/2026/10/29/assemblyai-tts-1-text-to-speech-api-voice-agents"
link: "https://marktechpost.com/2026/10/29/assemblyai-tts-1-text-to-speech-api-voice-agents"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-29T07:28:36Z"
published_date: "2026-10-29"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Michal Sutter"]
language: "en"
summary: "AssemblyAI has released AssemblyAI-TTS-1 , its first text-to-speech model, now generally available. The AssemblyAI-TTS-1 text-to-speech API targets voice agents running on live phone calls. In that setting, latency and pronunciation decide whether a caller stays on the line. Pricing is $15 per 1M characters , with no annual contract and no concurrency tier to buy. For developers already using…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "New Releases", "Staff", "Technology"]
orgs: ["OpenAI"]
topics: ["models & research", "agents & coding", "products & launches", "policy & regulation"]
content_source: "summary"
word_count: 1554
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AssemblyAI Ships AssemblyAI-TTS-1: A $15 per 1M Character Text-to-Speech API for Voice Agents

MarkTechPost · Michal Sutter · 2026-10-29

AssemblyAI has released AssemblyAI-TTS-1 , its first text-to-speech model, now generally available. The AssemblyAI-TTS-1 text-to-speech API targets voice agents running on live phone calls. In that setting, latency and pronunciation decide whether a caller stays on the line. Pricing is $15 per 1M characters , with no annual contract and no concurrency tier to buy. For developers already using AssemblyAI speech-to-text, it closes the voice loop with one vendor. 

 TL;DR 

 Size: It is a hosted API model. 

 Runs on: AssemblyAI’s cloud only, in the US (us-east-1) or EU (eu-north-1) . No open weights or on-prem option. Any client with HTTP or WebSocket works. 

 Performance: Ties ElevenLabs v4 on entity accuracy in AssemblyAI’s tests, at under 1/5 of its price. 

 Best: 47 ms median time to first byte across 6 models in AssemblyAI’s API test (self-reported). 

 Worst: 159 ms median streaming latency on Cekura’s independent benchmark , 8th of 19 timed models. 

 Bottom line: 
 
 Best: $15 per 1M characters with unlimited concurrency. 

 Worst: no SSML, speed control, pronunciation dictionaries or emotion tags yet. 

 What is AssemblyAI-TTS-1? 

 AssemblyAI-TTS-1 is a streaming text-to-speech model from AssemblyAI that turns agent replies into speech for live calls. It was trained on millions of hours of audio , including real conversational data. Most TTS models represent audio as discrete tokens. AssemblyAI says TTS-1 operates on continuous audio representations instead. The AssemblyAI claims this improves realism and cuts time to first spoken audio. 

 The launch includes a library of 4,000+ voices and instant voice cloning. A clone needs a short recording and a confirmation of the speaker’s permission. The clone in the launch post used 24 seconds of audio. Six languages are supported at launch: English, Spanish, French, German, Italian and Portuguese. 

 How do developers integrate AssemblyAI-TTS-1? 

 There are 3 interfaces: an HTTP API, a WebSocket API and an OpenAI-compatible route . The WebSocket session keeps one connection per conversation and accepts a cancel message for barge-in. Output is mono PCM, mu-law or A-law, at 8 kHz to 48 kHz. 24 kHz PCM is the native format; telephony stacks can request 8 kHz mu-law directly. Word timestamps are included. AssemblyAI also published LiveKit and Pipecat reference agents. 

 How does AssemblyAI-TTS-1 perform on benchmarks? 

 AssemblyAI tested TTS-1 against 5 models on 4 English sets, using 50 matched cloned voices. All figures below are self-reported , from an eval dated October 28, 2026. 

 Entity accuracy (580 hard targets such as phone numbers and codes): 93.7%, vs ElevenLabs v4 93.6%, Cartesia Sonic 3.6 82.5%, ElevenLabs Flash v2.5 68.0%. 

 Word accuracy: 99.0% on Seed-TTS and LibriSpeech sentences. 

 Predicted MOS: 3.85, behind Inworld TTS-2 Flash at 3.88 and ahead of Sonic 3.6 at 3.82. 

 Median time to first byte: 47 ms. Flash v2.5 took 119 ms, Sonic 3.6 143 ms, Inworld TTS-2 Flash 244 ms. 

 Other: 85.5 TTSDS prosody score and 0.64 speaker similarity for cloned audio. 

 Independent results are more mixed. On Cekura’s benchmark of 27 models, TTS-1 scored 81.5% reading accuracy and 4.50 naturalness. Its median streaming latency, timed from the last word sent, was 159 ms. Inworld TTS-2 Flash posted 45 ms and 93.2% accuracy there, at the same $15 price. AssemblyAI also cites a 1.7% word error rate on Coval’s leaderboard . It reports a top-10 debut in Artificial Analysis’ controlled-voice arena. 

 Play</button>
 <button class="btn ghost" id="aai-prev">‹ Back</button>
 <button class="btn ghost" id="aai-next">Next ›</button>
 </div>
 </div>

 <div class="pane" data-p="bench">
 <div class="pills" id="aai-pills">
 <button class="pill on" data-m="ent">Entity accuracy</button>
 <button class="pill" data-m="ttfb">Median TTFB (AssemblyAI test)</button>
 <button class="pill" data-m="cstream">Streaming latency (Cekura)</button>
 <button class="pill" data-m="cacc">Reading accuracy (Cekura)</button>
 </div>
 <div class="bars" id="aai-bars"></div>
 <p class="note" id="aai-bnote"></p>
 </div>

 <div class="pane" data-p="cost">
 <div class="calc">
 <label for="aai-min">Spoken minutes per month: <b id="aai-minv" style="color:#fdfcf8">10,000</b></label>
 <input type="range" id="aai-min" min="1000" max="200000" step="1000" value="10000">
 <div class="cost" id="aai-cost"></div>
 <p class="note">Assumes 600 characters per minute of phone speech, the figure AssemblyAI cites as typical. List prices per 1M characters: AssemblyAI-TTS-1 $15, Inworld TTS-2 Flash $15 on demand, ElevenLabs Flash v2.5 $40, ElevenLabs v4 $80. Concurrency limits are not priced in.</p>
 </div>
 </div>

 <div class="pane" data-p="limits">
 <div class="grid" id="aai-cards">
 <div class="card"><h4>No SSML or speed control <span class="tag">LAUNCH GAP</span></h4><p>The WebSocket API has no speed, pitch, emotion or style parameter, and neither API accepts SSML. Punctuation and written fillers like "um" still shape delivery.</p></div>
 <div class="card"><h4>No pronunciation dictionaries <span class="tag">COMING SOON</span></h4><p>Custom pronunciation dictionaries and emotion tags are announced but not shipped. Cartesia Sonic 3.6 already offers custom pronunciations.</p></div>
 <div class="card"><h4>6 languages <span class="tag">COVERAGE</span></h4><p>English, Spanish, French, German, Italian and Portuguese. ElevenLabs Flash v2.5 lists 32 and Cartesia Sonic 3.6 lists 44.</p></div>
 <div class="card"><h4>Latency depends on method <span class="tag">CHECK IT</span></h4><p>About 90 ms advertised, 47 ms median in AssemblyAI's own test, 159 ms median streaming latency on Cekura (timed from the last word sent).</p></div>
 <div class="card"><h4>Instant cloning only <span class="tag">LAUNCH GAP</span></h4><p>Pro (fine-tuned) voice cloning is not available yet. Instant clones need a short clip and speaker permission.</p></div>
 <div class="card"><h4>Cloud only <span class="tag">DEPLOYMENT</span></h4><p>US (us-east-1) and EU (eu-north-1) hosts at the same price. No on-prem option is announced.</p></div>
 </div>
 <p class="note">Tap a card to expand it.</p>
 </div>

 <div class="ft"><span>Sources: AssemblyAI launch post, docs and pricing; Cekura TTS benchmark; vendor pricing pages. Checked Oct 29, 2026.</span><span class="mtp">Built by Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-aai-tts1');if(!R)return;
function resize(){try{parent.postMessage({mtpEmbed:'aai-tts1',h:R.offsetHeight+40},'*')}catch(e){}}
R.querySelectorAll('.tab').forEach(function(t){t.addEventListener('click',function(){
R.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});t.classList.add('on');
R.querySelectorAll('.pane').forEach(function(p){p.classList.toggle('on',p.getAttribute('data-p')===t.getAttribute('data-t'))});
if(t.getAttribute('data-t')==='bench')draw(cur);setTimeout(resize,60);});});
var steps=['Your agent LLM writes a reply. Text can be sent word by word as it is generated.',
'One WebSocket session per conversation. Voice, language, sample rate and encoding are fixed at connect time.',
'TTS-1 models speech on continuous audio representations, not discrete tokens. AssemblyAI says this improves realism and speed.',
'Audio streams back as raw mono PCM, mu-law or A-law. 24 kHz PCM is native; 8 kHz mu-law suits phone lines.',
'If the caller interrupts, a cancel message stops speech. Word timestamps show what was actually said.'];
var nodes=R.querySelectorAll('#aai-flow .node'),det=R.querySelector('#aai-detail'),si=-1,timer=null;
function show(i){si=(i+nodes.length)%nodes.length;nodes.forEach(function(n,k){n.classList.toggle('act',k===si);n.classList.toggle('playing',k===3&&si>=3)});det.textContent=(si+1)+'/5 · '+steps[si];resize();}
R.querySelector('#aai-next').onclick=function(){stop();show(si+1)};
R.querySelector('#aai-prev').onclick=function(){stop();show(si<=0?4:si-1)};
var pb=R.querySelector('#aai-play');
function stop(){if(timer){clearInterval(timer);timer=null;pb.textContent=' Play'}}
pb.onclick=function(){if(timer){stop();return}pb.textContent='❚❚ Pause';show(si+1);timer=setInterval(function(){show(si+1)},2200)};
var D={
ent:{u:'%',max:100,hi:true,note:'AssemblyAI pronunciation set: 580 hard targets (phone numbers, dates, URLs, codes). Self-reported, eval dated Oct 28, 2026.',
 r:[['AssemblyAI-TTS-1',93.7,1],['ElevenLabs v4',93.6],['Cartesia Sonic 3.6',82.5],['ElevenLabs Flash v2.5',68.0]]},
ttfb:{u:' ms',max:650,hi:false,note:'Median time to first byte over each API from one client, one request at a time. Self-reported by AssemblyAI. Lower is better.',
 r:[['AssemblyAI-TTS-1',47,1],['ElevenLabs Flash v2.5',119],['Cartesia Sonic 3.6',143],['Inworld TTS-2 Flash',244],['Inworld TTS-2',280],['ElevenLabs v4',612]]},
cstream:{u:' ms',max:600,hi:false,note:'Cekura: median from the last word sent to first audible sound, US East, 104 sentences x 3 reads. Independent. Lower is better.',
 r:[['Inworld TTS-2 Flash',45],['AssemblyAI-TTS-1',159,1],['ElevenLabs Flash v2.5',177],['Cartesia Sonic 3.6',270],['ElevenLabs v4',561]]},
cacc:{u:'%',max:100,hi:true,note:'Cekura: hard parts read correctly, scored by speech-to-text transcribers (an estimate, not human-rated). Independent.',
 r:[['Inworld TTS-2 Flash',93.2],['AssemblyAI-TTS-1',81.5,1],['ElevenLabs v4',80.4],['Cartesia Sonic 3.6',74.9],['ElevenLabs Flash v2.5',64.4]]}};
var cur='ent',bars=R.querySelector('#aai-bars'),bn=R.querySelector('#aai-bnote');
function draw(m){cur=m;var d=D[m];bars.innerHTML='';d.r.forEach(function(x){
var row=document.createElement('div');row.className='row'+(x[2]?' me':'');
row.innerHTML='<span class="nm">'+x[0]+'</span><span class="track"><span class="fill"></span></span><span class="val">'+(d.u==='%'?x[1].toFixed(1):x[1])+d.u+'</span>';
bars.appendChild(row);var f=row.querySelector('.fill');setTimeout(function(){f.style.width=Math.max(2,x[1]/d.max*100)+'%'},40);});
bn.textContent=d.note;setTimeout(resize,60);}
R.querySelectorAll('#aai-pills .pill').forEach(function(p){p.addEventListener('click',function(){
R.querySelectorAll('#aai-pills .pill').forEach(function(x){x.classList.remove('on')});p.classList.add('on');draw(p.getAttribute('data-m'))})});
var rng=R.querySelector('#aai-min'),mv=R.querySelector('#aai-minv'),co=R.querySelector('#aai-cost');
var P=[['AssemblyAI-TTS-1',15,1],['Inworld TTS-2 Flash (on demand)',15],['ElevenLabs Flash v2.5',40],['ElevenLabs v4',80]];
function calc(){var m=+rng.value,ch=m*600;mv.textContent=m.toLocaleString('en-US');var h='';
P.forEach(function(p){var c=ch/1e6*p[1];h+='<span class="'+(p[2]?'me':'')+'">'+p[0]+'</span><span class="'+(p[2]?'me':'')+'">$'+c.toLocaleString('en-US',{maximumFractionDigits:0})+'/mo</span>'});
co.innerHTML=h+'<span style="color:#a5a4a2">Characters per month</span><span style="color:#a5a4a2">'+(ch/1e6).toLocaleString('en-US',{maximumFractionDigits:1})+'M</span>';}
rng.addEventListener('input',calc);calc();
R.querySelectorAll('#aai-cards .card').forEach(function(c){c.addEventListener('click',function(){c.classList.toggle('open');setTimeout(resize,40)})});
draw('ent');show(0);
window.addEventListener('load',resize);window.addEventListener('resize',resize);setTimeout(resize,300);
})();
</script>
</body></html>"> 
 
 (function(){var f=document.getElementById("mtp-aai-tts1-frame");window.addEventListener("message",function(e){if(e.data&&e.data.mtpEmbed==="aai-tts1"&&e.data.h){f.style.height=e.data.h+"px";}});})(); 

 How does AssemblyAI-TTS-1 compare with ElevenLabs, Cartesia and Inworld? 

 Feature AssemblyAI-TTS-1 Inworld TTS-2 Flash ElevenLabs Flash v2.5 Cartesia Sonic 3.6 Model size Not disclosed Not disclosed Not disclosed Not disclosed Architecture Continuous audio representations Not disclosed Not disclosed State space model (SSM) Access Hosted API (US, EU) Hosted API Hosted API Hosted API; on-prem and VPC on enterprise Languages 6 200+ 32 44 Vendor latency claim About 90 ms to first audio Under 25 ms P99 server-side TTFB About 75 ms Under 90 ms Median TTFB, AssemblyAI test 47 ms 244 ms 119 ms 143 ms Median streaming latency, Cekura 159 ms 45 ms 177 ms 270 ms Entity accuracy, AssemblyAI set 93.7% Not reported 68.0% 82.5% Reading accuracy, Cekura 81.5% 93.2% 64.4% 74.9% Naturalness, Cekura (UTMOS) 4.50 4.46 4.33 4.41 List price per 1M characters $15 $15 on demand, $7 on Growth plan $40 $37.38 to $50 via plan credits Self-serve concurrency Unlimited on pay-as-you-go 5 to 500 requests by plan Not disclosed 2 to 15 requests by plan Voice cloning Instant only Instant and professional Yes Instant and professional 

 Cartesia’s range divides each plan price by its credits, at 1 credit per character. 

 What does AssemblyAI-TTS-1 cost? 

 Pricing is per input character, including spaces and punctuation, at $15 per 1M . Every voice, cloning, word timestamps and EU processing come at that same rate. There are no per-voice fees, concurrency fees or minimums. AssemblyAI calls it the lowest-priced frontier TTS model for voice agents. However, Inworld TTS-2 Flash also lists $15 per 1M on demand, falling to $7 on paid plans. The sharper difference is concurrency: Inworld’s on-demand tier allows 5 concurrent requests. 

 Key Takeaways 

 AssemblyAI-TTS-1 is AssemblyAI’s first text-to-speech model, built for live voice agents. 

 It costs $15 per 1M characters, with unlimited concurrency and no contract. 

 Self-reported: 93.7% entity accuracy and 47 ms median time to first byte. 

 Cekura measured 159 ms streaming latency and 81.5% reading accuracy. 

 Missing at launch: SSML, speed control, pronunciation dictionaries and emotion tags. 

 Check out the launch post , docs , pricing , and the LiveKit and Pipecat reference agents. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post AssemblyAI Ships AssemblyAI-TTS-1: A $15 per 1M Character Text-to-Speech API for Voice Agents appeared first on MarkTechPost .
