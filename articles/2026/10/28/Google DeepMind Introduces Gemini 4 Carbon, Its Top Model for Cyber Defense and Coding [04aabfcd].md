---
id: "04aabfcdcc962586"
title: "Google DeepMind Introduces Gemini 4 Carbon, Its Top Model for Cyber Defense and Coding"
url: "https://marktechpost.com/2026/10/28/google-deepmind-gemini-4-carbon-frontier-model"
link: "https://marktechpost.com/2026/10/28/google-deepmind-gemini-4-carbon-frontier-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T17:48:38Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google DeepMind has introduced Gemini 4 Carbon , its strongest model to date. Gemini 4 Carbon is a frontier model from Google built for long-horizon agentic coding and cybersecurity defense. It ranks #1 on the updated v5.0 Artificial Analysis Intelligence Index with a score of 59. For developers, the catch is access. Carbon starts with a vetted group of cyber defenders, not the public API. \n\n…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "Language Model", "Large Language Model", "New Releases", "Security", "Staff"]
orgs: ["Google", "OpenAI", "US government", "Anthropic"]
topics: ["models & research", "agents & coding", "products & launches", "safety & ethics"]
content_source: "summary"
word_count: 1406
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google DeepMind Introduces Gemini 4 Carbon, Its Top Model for Cyber Defense and Coding

MarkTechPost · Asif Razzaq · 2026-10-28

Google DeepMind has introduced Gemini 4 Carbon , its strongest model to date. Gemini 4 Carbon is a frontier model from Google built for long-horizon agentic coding and cybersecurity defense. It ranks #1 on the updated v5.0 Artificial Analysis Intelligence Index with a score of 59. For developers, the catch is access. Carbon starts with a vetted group of cyber defenders, not the public API. 

 TL;DR 

 Size: Parameter count and context window not disclosed. Its predecessor, Gemini 4 Argon , has a 1,048,576-token context. 

 Runs on: Google-hosted only. No open weights, no self-hosting, no quantized variants. 

 Performance: Leads 15 of 17 published benchmarks versus Argon, GPT-6 Astra, Opus 5.5 and Fable 5.1. 

 Best: 96.2% BFS F1 on GraphWalks (256K to 1M tokens), versus 84.2% for Argon. 

 Worst: 81.5% on OSWorld-2.1, trailing Claude Opus 5.5 at 87.2%. 

 Bottom line: Best: state-of-the-art vulnerability finding, exploitation and patching. Worst: you probably cannot call it yet. 

 What is Gemini 4 Carbon? 

 Carbon is the second Gemini 4 model, following Gemini 4 Argon . Google team states that the model targets hard, long-running engineering work. Internal teams saw Carbon run for days on single tasks. Examples include root-causing and patching subtle bugs across large codebases and low-level systems. 

 Google also tuned Carbon for full-stack web development and multimodal understanding. On WebDev Arena , Carbon gained 89 Elo points to reach #4 at 1769. 

 How does Gemini 4 Carbon perform on benchmarks? 

 Google published a 17-row comparison in its launch post . Carbon was run at the highest thinking setting. Most rival numbers are self-reported by each provider, per Google’s evaluation methodology . 

 Agentic coding : Carbon scores 65.2% on Terminal-Bench 4.0 (AA), ahead of Opus 5.5 at 59.6%. It hits 9.6% on SWE-sweep, narrowly ahead of GPT-6 Astra at 9.5%. On FrontierSWE, GPT-6 Astra leads at 65.5% versus Carbon’s 61.2%. 

 Computer use and knowledge work : Carbon reaches 77.4% on Agents’ Last Exam v1.1. On Vending-Bench 2, it ends with a $16,484 bank balance, the highest listed. 

 Long context and science : GraphWalks is the widest gap: 96.2% versus 71.8% for GPT-6 Astra. Carbon also posts 80.0% on RiemannBench. 

 Why does Carbon relevant for cybersecurity? 

 Google frames Carbon around the full defense lifecycle: find, validate, then fix. Cyber benchmarks were evaluated without guardrails. 

 Finding: 88.2% on SEC-bench Pro , versus 85.4% for GPT-6 Astra. 

 Exploiting: 54.8% on ExploitGym , versus 42.4% for GPT-6 Astra and 34.5% for Opus 5.5. 

 Patching: 71.0% on Collinear’s CWE-bench , versus 68.0% for Argon and GPT-6 Astra. 

 Google computed SEC-bench Pro and ExploitGym scores itself, using its Antigravity harness. ExploitGym ran with mitigations off. Internally, Carbon showed more than 2x higher success at generating secure code than Argon. Google team states that the Chrome team found Carbon over 10x better than another lab’s model at high-quality patches. Wiz reports Carbon leading its web penetration testing benchmarks. 

 Play the loop</button></div>
 </div>

 <div class="panel" id="p2">
 <div class="stage">
 <div>
 <div class="step on" data-s="0"><b>1 · Find</b><small>SEC-bench Pro: uncover real vulnerabilities</small></div>
 <div class="step" data-s="1"><b>2 · Validate</b><small>ExploitGym: check which flaws are exploitable</small></div>
 <div class="step" data-s="2"><b>3 · Patch</b><small>CWE-bench: fix the root cause in code</small></div>
 <div class="btns"><button class="btn" id="g4cnext">Next step →</button></div>
 </div>
 <div class="bars" id="g4ccyber"></div>
 </div>
 <p class="note">Cyber benchmarks evaluated without guardrails. Google self-computed SEC-bench Pro and ExploitGym (mitigations off). Not disclosed = no score published.</p>
 </div>

 <div class="panel" id="p3">
 <div class="chips" id="g4cchips"></div>
 <div class="bars" id="g4cbench"></div>
 <p class="note">Carbon and Argon run at highest thinking setting. Rivals at max available reasoning, mostly self-reported.</p>
 </div>

 <div class="panel" id="p4">
 <div class="sgrid">
 <div class="scard"><b>0.0%</b><span>Successful cheating on Terminal-Bench 4.0</span><em>Cheating attempts dropped to 0.4%, while accuracy improved.</em></div>
 <div class="scard"><b>~80%</b><span>Fewer high-severity misalignment alerts</span><em>Observed in live coding environments with Google's internal teams.</em></div>
 <div class="scard"><b>~2x</b><span>Fewer unsupported claims than Argon</span><em>Carbon writes caveats into the deliverable instead of hedging.</em></div>
 <div class="scard"><b>-26%</b><span>Overreach</span><em>Stays within scope on multi-step plans.</em></div>
 <div class="scard"><b>-29%</b><span>Under-service</span><em>Follows through on what was asked.</em></div>
 <div class="scard"><b>0.0%</b><span>Gray Swan IPI attack success</span><em>Argon was already at 0.7%. Carbon resisted every evaluated attack.</em></div>
 </div>
 <p class="note">Tap a card for detail. All figures are Google's internal or self-run results.</p>
 </div>

 <div class="panel" id="p5">
 <div class="tl" id="g4ctl">
 <div class="ti"><b>Pre-release testing</b><small>Google participates in the U.S. government's voluntary pre-release model testing.</small></div>
 <div class="ti"><b>This week: cyber defenders</b><small>A subset of cyber defenders gets access first.</small></div>
 <div class="ti"><b>Fairwind Program</b><small>Phased access for vetted partners: governments, critical infrastructure, core tech platforms.</small></div>
 <div class="ti"><b>Later: developers, businesses, consumers</b><small>No date announced. Google says "as soon as possible".</small></div>
 </div>
 <div class="calc">
 <label>Monthly input tokens: <b id="g4cin">50</b>M</label>
 <input type="range" id="g4crin" min="1" max="500" value="50">
 <label>Monthly output tokens: <b id="g4cout">10</b>M</label>
 <input type="range" id="g4crout" min="1" max="200" value="10">
 <div class="cost">
 <div><b id="g4cc1">$200</b><small>Intro price ($2 / $10)</small></div>
 <div><b id="g4cc2">$400</b><small>After intro ($4 / $20)</small></div>
 </div>
 </div>
 <p class="note">Estimate excludes caching. Cached input is 95% off the input price.</p>
 </div>

 <div class="foot">
 <span>Source: <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/" target="_blank" rel="noopener">Google launch post</a> · <a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_4_carbon_model_evaluation.pdf" target="_blank" rel="noopener">methodology</a></span>
 <span class="brand">© Marktechpost</span>
 </div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-g4c');
function post(){try{parent.postMessage({mtpEmbed:'g4c',height:R.offsetHeight+40},'*');}catch(e){}}
var M=['Gemini 4 Carbon','Gemini 4 Argon','GPT-6 Astra','Claude Opus 5.5','Claude Fable 5.1'];
function bars(el,title,vals,max,unit){
 var h='<p class="bt">'+title+'</p>';
 vals.forEach(function(v,i){
 h+='<div class="row"><span>'+M[i]+'</span><div class="track"><div class="fill'+(i==0?' me':'')+'" data-w="'+(v==null?0:v/max*100)+'"></div></div><span class="val">'+(v==null?'<span class="nd">Not disclosed</span>':(unit=='$'?'$'+v.toLocaleString('en-US'):v+unit))+'</span></div>';
 });
 el.innerHTML=h;
 setTimeout(function(){el.querySelectorAll('.fill').forEach(function(f){f.style.width=f.getAttribute('data-w')+'%';});},60);
 post();
}
var CY=[['SEC-bench Pro (find)',[88.2,83.4,85.4,null,null]],['ExploitGym (validate)',[54.8,42.0,42.4,34.5,null]],['CWE-bench (patch)',[71.0,68.0,68.0,67.0,58.0]]];
var cs=0,cyEl=document.getElementById('g4ccyber');
function cy(i){cs=i;document.querySelectorAll('#mtp-g4c .step').forEach(function(s,j){s.classList.toggle('on',j==i);});bars(cyEl,CY[i][0],CY[i][1],100,'%');}
document.querySelectorAll('#mtp-g4c .step').forEach(function(s,j){s.onclick=function(){cy(j);};});
document.getElementById('g4cnext').onclick=function(){cy((cs+1)%3);};
var B=[
 ['AA Index v5.0',[59,50,57,58,49],70,''],
 ['Terminal-Bench 4.0 (AA)',[65.2,57.1,59.1,59.6,52.0],100,'%'],
 ['FrontierSWE',[61.2,55.0,65.5,62.3,56.3],100,'%'],
 ['OSWorld-2.1 (offline subset)',[81.5,74.7,80.9,87.2,76.8],100,'%'],
 ['Agents’ Last Exam v1.1',[77.4,69.0,73.1,71.6,null],100,'%'],
 ['GraphWalks 256K to 1M (BFS F1)',[96.2,84.2,71.8,66.8,65.0],100,'%'],
 ['Vending-Bench 2 (bank balance)',[16484,13718,15515,9235,5422],18000,'$'],
 ['RiemannBench',[80.0,76.0,72.0,69.6,65.6],100,'%']
];
var ch=document.getElementById('g4cchips'),be=document.getElementById('g4cbench');
B.forEach(function(b,i){var x=document.createElement('button');x.className='btn'+(i==0?' on':'');x.textContent=b[0];x.onclick=function(){ch.querySelectorAll('.btn').forEach(function(y){y.classList.remove('on');});x.classList.add('on');bars(be,b[0],b[1],b[2],b[3]);};ch.appendChild(x);});
function flow(){var n=document.querySelectorAll('#g4cflow .node');n.forEach(function(x){x.classList.remove('lit');});n.forEach(function(x,i){setTimeout(function(){x.classList.add('lit');},i*550);});}
document.getElementById('g4cplay').onclick=flow;
function tl(){var t=document.querySelectorAll('#g4ctl .ti');t.forEach(function(x){x.classList.remove('lit');});t.forEach(function(x,i){setTimeout(function(){x.classList.add('lit');},i*450);});}
document.querySelectorAll('#mtp-g4c .scard').forEach(function(c){c.onclick=function(){c.classList.toggle('open');post();};});
var ri=document.getElementById('g4crin'),ro=document.getElementById('g4crout');
function calc(){var a=+ri.value,b=+ro.value;document.getElementById('g4cin').textContent=a;document.getElementById('g4cout').textContent=b;
 document.getElementById('g4cc1').textContent='$'+(a*2+b*10).toLocaleString('en-US');document.getElementById('g4cc2').textContent='$'+(a*4+b*20).toLocaleString('en-US');}
ri.oninput=calc;ro.oninput=calc;calc();
var started={};
document.querySelectorAll('#mtp-g4c .tab').forEach(function(t){t.onclick=function(){
 document.querySelectorAll('#mtp-g4c .tab').forEach(function(x){x.classList.toggle('on',x==t);});
 var id=t.getAttribute('data-t');
 document.querySelectorAll('#mtp-g4c .panel').forEach(function(p){p.classList.toggle('on',p.id==id);});
 if(id=='p1')flow(); if(id=='p2')cy(cs); if(id=='p3'){var on=ch.querySelector('.btn.on');on&&on.click();} if(id=='p5')tl();
 post();
};});
cy(0);bars(be,B[0][0],B[0][1],B[0][2],B[0][3]);
flow();
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body>
</html>
" style="width:100%;max-width:880px;height:600px;border:0;display:block;margin:24px auto;" loading="lazy"> 
 window.addEventListener("message",function(e){var d=e.data;if(d&&d.mtpEmbed==="g4c"&&d.height){var f=document.getElementById("mtp-g4c-frame");if(f)f.style.height=d.height+"px";}}); 

 What safety changes ship with Carbon? 

 Carbon keeps Argon’s layered stack: training, real-time misuse defenses, prompt-injection resilience and chain-of-thought monitoring. Google reports several alignment gains: 

 Successful cheating on Terminal-Bench 4.0 fell to 0.0%, with cheating attempts at 0.4%. 

 High-severity misalignment alerts in live internal coding dropped by almost 80%. 

 Unsupported claims fell roughly 2x versus Argon. 

 Overreach fell 26% and under-service fell 29%. 

 Attack success on Gray Swan’s Indirect Prompt Injection benchmark is 0.0%, down from Argon’s 0.7%. 

 These are Google’s internal or self-run figures. Independent replication is not yet available. 

 How can developers access Gemini 4 Carbon? 

 Not yet, for most. Google is participating in the U.S. government’s voluntary pre-release testing process. This week, a subset of cyber defenders gets access. More trusted partners follow through the Fairwind Program , which prioritizes governments, critical infrastructure operators and core tech platforms. Developers, businesses and consumers get Carbon later, with no date given. 

 Pricing matches Argon’s introductory rate: $2 per million input tokens and $10 per million output tokens. Cached input is 95% off. After the introductory period, prices rise to $4 and $20. 

 Gemini 4 Carbon vs competitors 

 Feature Gemini 4 Carbon Gemini 4 Argon GPT-6 Astra Claude Opus 5.5 Claude Fable 5.1 Parameters Not disclosed Not disclosed Not disclosed Not disclosed Not disclosed Context window Not disclosed 1,048,576 1,050,000 1M 1M Max output Not disclosed 65,536 (1,048,576 long decode) 128,000 128K 128K Price in / out (per 1M) $2 / $10 intro, then $4 / $20 $2 / $10 intro ( Google ) $10 / $50 $4 / $20 ( pricing ) $10 / $50 ( pricing ) Access Vetted cyber defenders, Fairwind Gemini API OpenAI API Claude API Claude API AA Index v5.0 59 50 57 58 49 SEC-bench Pro 88.2% 83.4% 85.4% Not disclosed Not disclosed ExploitGym 54.8% 42.0% 42.4% 34.5% Not disclosed OSWorld-2.1 81.5% 74.7% 80.9% 87.2% 76.8% FrontierSWE 61.2% 55.0% 65.5% 62.3% 56.3% 

 Benchmark rows: Google launch post ; rival scores mostly self-reported per methodology . 

 Key Takeaways 

 Gemini 4 Carbon ranks #1 on Artificial Analysis Index v5.0 at 59. 

 It leads SEC-bench Pro (88.2%), ExploitGym (54.8%) and CWE-bench (71.0%). 

 GraphWalks long context hits 96.2%, its widest margin. 

 Claude Opus 5.5 still wins OSWorld-2.1; GPT-6 Astra wins FrontierSWE. 

 Access starts with cyber defenders at $2/$10 per million tokens. 

 Check out the Google’s launch post , the evaluation methodology and the Fairwind Program page . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google DeepMind Introduces Gemini 4 Carbon, Its Top Model for Cyber Defense and Coding appeared first on MarkTechPost .
