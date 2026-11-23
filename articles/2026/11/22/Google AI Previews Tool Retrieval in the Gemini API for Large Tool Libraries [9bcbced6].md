---
id: "9bcbced690e9829d"
title: "Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries"
url: "https://marktechpost.com/2026/11/22/google-gemini-api-tool-retrieval"
link: "https://marktechpost.com/2026/11/22/google-gemini-api-tool-retrieval"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-22T10:03:54Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Google has launched Tool Retrieval in the Gemini API , now in preview in the Interactions API. Gemini API Tool Retrieval lets an agent keep a large tool library available. It does not send every parameter schema in every prompt. The model loads a schema only when a task needs that tool. For agents wired to dozens of functions or MCP servers, it targets a real cost: tool definitions. You can…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Generative AI", "Guardrail", "New Releases", "Software Engineering", "Staff"]
orgs: ["Google", "Anthropic", "OpenAI", "Amazon"]
topics: ["agents & coding", "search & media", "models & research", "products & launches"]
content_source: "summary"
word_count: 1482
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries

MarkTechPost · Michal Sutter · 2026-11-22

Google has launched Tool Retrieval in the Gemini API , now in preview in the Interactions API. Gemini API Tool Retrieval lets an agent keep a large tool library available. It does not send every parameter schema in every prompt. The model loads a schema only when a task needs that tool. For agents wired to dozens of functions or MCP servers, it targets a real cost: tool definitions. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Tool: An API feature with no stated tool cap. Google advises static loading under 20 stable tools. 

 Runs on: Google’s servers (server-side search) or your own registry (client-side). Interactions API, v1beta only. 

 Performance: Search, schema load and function call resolve in 1 API request in server mode. 

 Best: 0 extra round trips and no index to host for server-side retrieval. 

 What is Gemini API Tool Retrieval? 

 Tool Retrieval is a Gemini API feature that defers tool parameter schemas until the model asks for them. Google’s documentation states the problem plainly. A few dozen function declarations can consume tens of thousands of tokens on every request. 

 With deferral, the model sees only each tool’s name and a short description. It does not see the parameter schema until retrieval. 

 How does defer_loading work in the Gemini Interactions API? 

 You add {"type": "tool_search"} to the tools array. Then you set defer_loading: true on each function to hold back. The @googledevs launch post shows a deferred issue_refund function on gemini-4-hydrogen . Its code comment mentions 50+ other deferred functions. 

 When the model needs a deferred tool, the response contains 3 steps: 

 tool_search_call : the model requests a tool by name. 

 tool_search_result : the API returns the full schema. 

 function_call : the model emits the call your code executes. 

 The API resolves the first 2 steps itself. Your app only runs the function_call and returns a function_result . 

 Deferred functions can carry an optional short_description . It is shown during retrieval and is valid only when defer_loading is true. 

 Server-side vs client-side retrieval 

 Server-side is the default. Gemini runs the search, so there is no index to build or host. 

 Client-side mode uses "execution": "client" . Your app runs its own lookup, such as an embedding index, registry or permission filter. It returns matching declarations in function_result.result . Those tools can join mid-conversation, even if absent from the initial tools array. Each client-side search costs 1 extra round trip. 

 The 2 modes cannot be combined in 1 request. Only 1 tool_search entry is allowed per request. 

 Does it work with MCP servers and prefix caching? 

 Yes on both, with caveats. Setting defer_loading: true on an mcp_server entry defers every tool that server exposes. Deferred MCP tools still execute remotely through the Gemini API MCP support . 

 On caching, deferred schemas stay out of the prompt prefix. Loaded schemas append inline, so implicit caching still applies. The docs add one catch: deferring tools can shrink a prompt below the minimum cacheable size. 

 What does Tool Retrieval cost? 

 There is no separate fee. Tokens bill at the model’s standard input, cached and output rates. Each server-side search triggers an extra model call over the full context. Those tokens appear in total_tool_use_tokens , billed at the input rate. 

 Each loaded schema then stays billed as input for the rest of the conversation. The docs say static loading can cost less for small libraries or per-turn searches. 

 How does it compare with Claude and OpenAI tool search? 

 Anthropic and OpenAI already ship similar tool search features, with published savings numbers. 

 Feature Gemini API Tool Retrieval Anthropic Tool Search Tool OpenAI tool search Status Preview, v1beta Not disclosed on docs page Not disclosed on docs page API surface Interactions API only Messages API; Bedrock InvokeModel Responses API Models Gemini 4 Carbon, Neon, Hydrogen, Argon; 3.8 Flash; 3.6 Flash Claude 5 series, Opus 4.5+, Sonnet 4.5+, Haiku 4.5 gpt-5.4 and later Search modes Server or client Regex, BM25 or custom Hosted or client-executed Max deferred tools Not disclosed 10,000 Not disclosed Results per search Not disclosed 5 by default Not disclosed MCP deferral Per mcp_server entry Per mcp_toolset On MCP server tool Separate fee No No Not disclosed Published token savings None 85% (77K to 8.7K tokens) 47% on 250 MCP Atlas tasks Published accuracy None Opus 4.5: 79.5% to 88.1% Not disclosed 

 Anthropic and OpenAI figures are self-reported in their own tests. They are not comparable to any Gemini result. 

 Play</button><button class="btn ghost" id="gnext">Next step</button><button class="btn ghost" id="greset">Reset</button></div>
 <p class="note">In server-side mode all 3 steps come back in 1 API request. Source: Google blog and Tool Retrieval docs.</p>
 </div>

 <div class="pane" data-p="1">
 <div class="grid2">
 <div class="ctx"><h4>Static: every schema, every request</h4><div id="gstatic"></div></div>
 <div class="ctx"><h4>Deferred: names now, schemas on demand</h4><div id="gdef"></div></div>
 </div>
 <div class="chips" id="gchips"></div>
 <p class="note">Click a tool to simulate the model retrieving it. Block sizes are illustrative, not measured. Google's docs: a few dozen declarations can cost tens of thousands of tokens per request. Loaded schemas stay in context and cannot be unloaded.</p>
 </div>

 <div class="pane" data-p="2">
 <div class="seg"><button class="on" data-m="s">Server-side (default)</button><button data-m="c">Client-side</button></div>
 <table><tbody id="gmode"></tbody></table>
 <p class="note">The 2 modes cannot be combined in 1 request. Only 1 tool_search entry per request. Google suggests static loading for fewer than 20 stable tools.</p>
 </div>

 <div class="pane" data-p="3">
 <p class="sub" style="margin:0 0 4px">Published token savings from each vendor's own tests</p>
 <div class="bar"><div class="lab"><span><b>Anthropic Tool Search Tool</b> (77K to 8.7K tokens)</span><b>85%</b></div><div class="tr"><div class="fl" data-w="85" style="background:#D97757"></div></div></div>
 <div class="bar"><div class="lab"><span><b>OpenAI tool search</b> (250 MCP Atlas tasks, 36 servers)</span><b>47%</b></div><div class="tr"><div class="fl" data-w="47" style="background:#10A37F"></div></div></div>
 <div class="bar"><div class="lab"><span><b>Gemini API Tool Retrieval</b></span><b>Not published</b></div><div class="tr"><div class="na">Google asks developers to measure on their own traffic</div></div></div>
 <button class="btn ghost" id="greplay" style="margin-top:6px">Replay bars</button>
 <p class="note">All figures self-reported and measured on different workloads, so they are not directly comparable. Anthropic also reports Opus 4.5 MCP eval accuracy rising from 79.5% to 88.1%.</p>
 </div>

 <div class="pane" data-p="4">
 <div class="cards">
 <div class="fc"><div class="in"><div class="fa"><span class="tag" style="color:#EA4335">CAVEAT</span>Preview only</div><div class="ba">v1beta, Interactions API only. generateContent is not supported. API may change before GA.</div></div></div>
 <div class="fc"><div class="in"><div class="fa"><span class="tag" style="color:#EA4335">CAVEAT</span>No unloading</div><div class="ba">Each loaded schema stays in context and is billed as input for the rest of the conversation.</div></div></div>
 <div class="fc"><div class="in"><div class="fa"><span class="tag" style="color:#F29900">COST</span>Extra model pass</div><div class="ba">Each server-side search adds a model call, reported in total_tool_use_tokens at the input rate.</div></div></div>
 <div class="fc"><div class="in"><div class="fa"><span class="tag" style="color:#F29900">GOTCHA</span>Resend all tools</div><div class="ba">Tool declarations are not persisted. Send the full tools array on every request.</div></div></div>
 <div class="fc"><div class="in"><div class="fa"><span class="tag" style="color:#F29900">GOTCHA</span>Strict replay</div><div class="ba">Stateless mode: dropping tool_search_call or a signature returns a 400 error.</div></div></div>
 <div class="fc"><div class="in"><div class="fa"><span class="tag" style="color:#34A853">TIP</span>Defer the long tail</div><div class="ba">Keep core tools and tools named in system instructions loaded. Prefix names by service.</div></div></div>
 </div>
 <p class="note">Tap a card to flip it. Source: Tool Retrieval docs.</p>
 </div>

 <div class="ft"><span>Sources: <a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/" target="_blank" rel="noopener">Google blog</a> · <a href="https://aistudio.google.com/docs/tool-retrieval" target="_blank" rel="noopener">Docs</a></span><span class="mtp">Built by Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('gtr-x');
function post(){try{parent.postMessage({gtrHeight:R.offsetHeight+40},'*')}catch(e){}}
var tabs=R.querySelectorAll('.tab'),panes=R.querySelectorAll('.pane');
tabs.forEach(function(t){t.onclick=function(){tabs.forEach(function(x){x.classList.remove('on')});panes.forEach(function(p){p.classList.remove('on')});t.classList.add('on');R.querySelector('[data-p="'+t.dataset.t+'"]').classList.add('on');if(t.dataset.t==='3')bars();setTimeout(post,60)}});
// flow
var caps=['You send a request with tool_search plus deferred tools. Only names and short descriptions enter the prompt.','The model decides it needs issue_refund and emits tool_search_call.','The API loads the issue_refund parameter schema into context as tool_search_result.','The model emits function_call with order_id and amount. Your code runs the refund.'];
var st=R.querySelectorAll('.st'),cur=-1,timer=null,cap=R.querySelector('#gcap');
function show(i){cur=i;st.forEach(function(s,j){s.classList.toggle('on',j<=i)});cap.textContent=i>=0?caps[i]:'Press Play to step through a single Tool Retrieval request.';post()}
show(-1);
R.querySelector('#gnext').onclick=function(){clearInterval(timer);show(cur>=3?0:cur+1)};
R.querySelector('#greset').onclick=function(){clearInterval(timer);show(-1)};
R.querySelector('#gplay').onclick=function(){clearInterval(timer);show(0);timer=setInterval(function(){if(cur>=3){clearInterval(timer);return}show(cur+1)},1400)};
// static vs deferred
var tools=['issue_refund','get_order','billing_get_customer','ship_label','crm_update','calendar_book'];
var got={};
function draw(){var s='',d='';tools.forEach(function(t){s+='<div class="blk full">'+t+' {full schema}</div>';d+=got[t]?'<div class="blk loaded">'+t+' {schema loaded}</div>':'<div class="blk thin">'+t+': short description</div>'});R.querySelector('#gstatic').innerHTML=s;R.querySelector('#gdef').innerHTML=d;var c='';tools.forEach(function(t){c+='<button class="chip'+(got[t]?' got':'')+'" data-tool="'+t+'">'+(got[t]?'✓ ':'+ ')+t+'</button>'});R.querySelector('#gchips').innerHTML=c;R.querySelectorAll('.chip').forEach(function(b){b.onclick=function(){got[b.dataset.tool]=true;draw()}});post()}
draw();
// modes
var M={s:[['Who runs the search','Gemini, on Google servers'],['Retrieval code you write','None'],['Extra round trips','None'],['Remote MCP servers','Yes, defer a whole mcp_server'],['Best for','Large known libraries and MCP servers']],c:[['Who runs the search','Your app (registry, embeddings, permission filter)'],['Retrieval code you write','Yes'],['Extra round trips','1 per search'],['Remote MCP servers','Not applicable'],['Best for','Dynamic registries, namespaces, per-user tools']]};
function mode(m){var h='';M[m].forEach(function(r){h+='<tr><th>'+r[0]+'</th><td>'+r[1]+'</td></tr>'});R.querySelector('#gmode').innerHTML=h;R.querySelectorAll('.seg button').forEach(function(b){b.classList.toggle('on',b.dataset.m===m)});post()}
R.querySelectorAll('.seg button').forEach(function(b){b.onclick=function(){mode(b.dataset.m)}});mode('s');
function bars(){var f=R.querySelectorAll('.fl');f.forEach(function(x){x.style.width='0'});setTimeout(function(){f.forEach(function(x){x.style.width=x.dataset.w+'%'})},80)}
R.querySelector('#greplay').onclick=bars;
R.querySelectorAll('.fc').forEach(function(c){c.onclick=function(){c.classList.toggle('flip')}});
window.addEventListener('load',post);window.addEventListener('resize',post);setTimeout(post,300);
})();
</script>
</body></html>
" style="width:100%;height:600px;border:0;display:block;" loading="lazy"> 
 
 window.addEventListener("message",function(e){if(e.data&&e.data.gtrHeight){var f=document.getElementById("gtr-frame");if(f&&e.source===f.contentWindow)f.style.height=e.data.gtrHeight+"px";}}); 

 Key Takeaways 

 Gemini API Tool Retrieval defers tool schemas until the model requests them. 

 Server mode resolves search, load and call in 1 API request. 

 Client mode supports custom registries, at 1 extra round trip per search. 

 No extra fee, but loaded schemas stay billed and cannot be unloaded. 

 Google published no savings data; Anthropic reports 85%, OpenAI 47%. 

 Check out the Google blog post , the Tool Retrieval docs and the MCP function calling docs . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries appeared first on MarkTechPost .
