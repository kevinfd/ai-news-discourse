---
id: "bc88fd72eab817d1"
title: "Vercel Labs Open-Sources agent-desktop for Agent Computer Use"
url: "https://marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use"
link: "https://marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-31T10:10:28Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Vercel Labs has released agent-desktop , an open-source CLI for AI agent computer use on macOS, Windows and Linux. agent-desktop reads each app through the operating system’s accessibility tree, not through screenshots. An agent gets a JSON snapshot with a ref for every element it can act on. Version 1.0.2 shipped on October 30, 2026, under Apache-2.0. For developers, any shell-capable coding…"
tags: ["Agentic AI", "AI Agents", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "New Releases", "Open Source", "Python", "Software Engineering", "Staff"]
orgs: ["Anthropic", "Apple", "Intel"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "summary"
word_count: 1573
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Vercel Labs Open-Sources agent-desktop for Agent Computer Use

MarkTechPost · Michal Sutter · 2026-10-31

Vercel Labs has released agent-desktop , an open-source CLI for AI agent computer use on macOS, Windows and Linux. agent-desktop reads each app through the operating system’s accessibility tree, not through screenshots. An agent gets a JSON snapshot with a ref for every element it can act on. Version 1.0.2 shipped on October 30, 2026, under Apache-2.0. For developers, any shell-capable coding agent can now drive native apps without a vision model. 

 TL;DR 

 Library: Rust CLI and a C library. 60 command names, 56 operational . 

 Runs on: macOS 13+, Windows 10 1809+ or Server 2019+, Ubuntu 24.04+ , on x64 and ARM64. Plain CPU, no GPU. 

 Performance: Deterministic, retry-safe ref actions. No independent computer-use benchmark yet. 

 Best: 78% to 96% fewer tokens on dense Electron apps via skeleton traversal ( self-reported ). 

 What is agent-desktop? 

 agent-desktop is a Rust CLI and C library from Vercel Labs for reading and operating desktop apps. It is a tool that agents call, not an agent . It embeds no LLM and has no GUI. Every command prints one JSON envelope and exits. The observe, act and verify loop stays in your agent. 

 How does agent-desktop work? 

 Each command flows through a fixed chain. The CLI or C library calls agent-desktop-core , which reaches the OS only through a PlatformAdapter trait. One platform crate then talks to the native accessibility API: 

 macOS: AX API 

 Windows: UI Automation 

 Linux: AT-SPI 

 Core never imports a platform crate. Each binary is compiled to drive exactly one OS. 

 Snapshots and refs 

 A snapshot assigns qualified refs such as @s8f3k2p9:e8 . The snapshot ID inside the ref makes it self-describing. A bare @e8 is rejected with INVALID_ARGS . When the UI changes, an action returns STALE_REF or AMBIGUOUS_TARGET . The agent then takes a fresh snapshot. 

 Every error carries a disposition . Agents should retry only when it says safe . Ref resolution is strict and fails closed rather than guessing. 

 Skeleton and drill-down 

 Dense apps can expose thousands of accessibility nodes. A --skeleton snapshot reads only 3 levels deep . Cut containers report a children_count and get a drill ref. snapshot --root then reads one region into the same snapshot. 

 The builder reported a 78% to 96% token cut versus full-tree dumps in Slack, VS Code and Notion. In Apple Maps, he reported 3,811 tokens per look falling to 273 . A simulated 52-step task dropped from 198k to 31k tokens. These are self-reported figures, not an independent benchmark. 

 Headless by default 

 Ref actions go through the accessibility API without moving the pointer or taking focus . That is what lets agents work while you keep using the machine. The global --headed flag allows physical input when needed. Every ref action also auto-waits up to 5,000 ms for a visible, enabled, stable target. 

 Trace a command</button><button class="b g" id="ad-step">Step</button></div>
 </div>

 <div class="pane" data-p="1">
 <p class="lead">Map, drill, act, verify. Click a step. Example output is trimmed from the official docs (GNOME Calculator).</p>
 <div class="steps" id="ad-steps">
 <div class="st on" data-s="0"><i>1</i><b>Skeleton</b></div>
 <div class="st" data-s="1"><i>2</i><b>Drill</b></div>
 <div class="st" data-s="2"><i>3</i><b>Act</b></div>
 <div class="st" data-s="3"><i>4</i><b>Verify</b></div>
 </div>
 <pre id="ad-code"></pre>
 <p class="note" id="ad-note"></p>
 <div class="btns"><button class="b" id="ad-next">Next step →</button></div>
 </div>

 <div class="pane" data-p="2">
 <p class="lead">Builder-reported numbers for skeleton drilling, next to Anthropic's documented screenshot cost.</p>
 <div class="bars" id="ad-bars">
 <div class="grp">Apple Maps, tokens per look (self-reported)</div>
 <div class="bar"><div class="lb"><span>Full window snapshot</span><em>3,811</em></div><div class="trk"><div class="fill" data-w="100" style="background:#ededed">3,811</div></div></div>
 <div class="bar"><div class="lb"><span>Skeleton, then drill</span><em>273</em></div><div class="trk"><div class="fill" data-w="7.2" style="background:#0070f3"></div></div></div>
 <div class="grp">Simulated 52-step task, total tokens (self-reported)</div>
 <div class="bar"><div class="lb"><span>Full window every step</span><em>198k</em></div><div class="trk"><div class="fill" data-w="100" style="background:#ededed">198k</div></div></div>
 <div class="bar"><div class="lb"><span>Skeleton, then drill</span><em>31k</em></div><div class="trk"><div class="fill" data-w="15.7" style="background:#0070f3">31k</div></div></div>
 <div class="grp">Reference: pixel-based computer use</div>
 <div class="bar"><div class="lb"><span>One Claude computer-use screenshot (Anthropic docs)</span><em>~1,000 to 1,800</em></div><div class="trk"><div class="fill" data-w="47" style="background:#f5a623">~1.8k max</div></div></div>
 </div>
 <div class="btns"><button class="b g" id="ad-replay">↻ Replay</button></div>
 <p class="note" style="margin-top:10px!important">Builder also reports 78% to 96% savings on Slack, VS Code and Notion. No independent benchmark yet.</p>
 </div>

 <div class="pane" data-p="3">
 <p class="lead">Same 60 command names everywhere. Click a platform for requirements.</p>
 <div class="os">
 <div class="oc"><h4>macOS</h4><div class="api">AX API</div><div class="more">macOS 13+, Intel or Apple Silicon. Grant Accessibility permission with <code>permissions --guide</code>. Shell surfaces still planned.</div></div>
 <div class="oc"><h4>Windows</h4><div class="api">UI Automation</div><div class="more">Windows 10 1809+ or Server 2019+, x64 or ARM64. No grant for apps at your terminal's integrity level. Higher-integrity apps refuse input.</div></div>
 <div class="oc"><h4>Linux</h4><div class="api">AT-SPI</div><div class="more">Ubuntu 24.04+, glibc 2.35 floor, x86_64 or aarch64. Needs <code>at-spi2-core</code>. Mouse input and cursor overlay need X11.</div></div>
 </div>
 <pre style="min-height:0;margin-top:14px!important"><span class="c"># one install for all 3</span>
<span class="k">npm</span> install -g agent-desktop
<span class="k">agent-desktop</span> skills get desktop</pre>
 </div>

 <div class="pane" data-p="4">
 <p class="lead">Where it falls short. Click to expand.</p>
 <div class="lim">
 <div class="li"><b><span class="x">!</span>No tree, no vision</b><div class="more">It reads accessibility trees and never matches pixels. A UI that publishes no tree is invisible to it.</div></div>
 <div class="li"><b><span class="x">!</span>Parallel, with a lease</b><div class="more">Multi-agent cursors are presentation-only. A machine-wide interaction lease still serializes physical input. Headless semantic actions avoid the pointer entirely.</div></div>
 <div class="li"><b><span class="x">!</span>Slow cold Electron apps</b><div class="more">A cold Chromium or Electron app can take 10 to 25 seconds to expose its web tree.</div></div>
 <div class="li"><b><span class="x">!</span>Private data in outputs</b><div class="more">Snapshots, clipboard reads and screenshots can contain private desktop content. Keep them out of public logs.</div></div>
 </div>
 </div>

 <div class="ft"><span>Sources: github.com/vercel-labs/agent-desktop · agent-browser.dev/desktop · Anthropic docs</span><span class="mtp">© Marktechpost</span></div>
</div>
<script>
(function(){
var R=document.getElementById('mtp-ad');
function rs(){try{parent.postMessage({mtpH:R.offsetHeight+40},'*')}catch(e){}}
var tabs=R.querySelectorAll('.tab'),panes=R.querySelectorAll('.pane');
tabs.forEach(function(t){t.onclick=function(){tabs.forEach(function(x){x.classList.remove('on')});panes.forEach(function(x){x.classList.remove('on')});t.classList.add('on');var p=R.querySelector('[data-p="'+t.dataset.t+'"]');p.classList.add('on');if(t.dataset.t==='2')bars();setTimeout(rs,60);}});
/* chain */
var L=R.querySelectorAll('#ad-chain .layer'),ci=-1,tm=null;
function lite(i){L.forEach(function(x,j){x.classList.toggle('lit',j===i)})}
R.querySelector('#ad-step').onclick=function(){clearInterval(tm);ci=(ci+1)%L.length;lite(ci)};
R.querySelector('#ad-play').onclick=function(){clearInterval(tm);ci=-1;tm=setInterval(function(){ci++;if(ci>=L.length){clearInterval(tm);L.forEach(function(x){x.classList.add('lit')});return}lite(ci)},450)};
/* loop */
var S=[
['<span class="c"># 1. map a dense window: depth clamped to 3</span>\n<span class="k">agent-desktop</span> snapshot --app gnome-calculator --skeleton -i --compact\n\n{ "snapshot_id": <span class="s">"s2txcl95uvubmn"</span>, "ref_count": 2,\n "children": [\n { "role": "group", "ref_id": <span class="s">"@s2txcl95uvubmn:e1"</span>, "children_count": 2 },\n { "role": "group", "ref_id": <span class="s">"@s2txcl95uvubmn:e2"</span>, "children_count": 1 } ] }','Only top levels are read. Cut containers carry children_count and a drill ref.'],
['<span class="c"># 2. drill into one region by ref</span>\n<span class="k">agent-desktop</span> snapshot --root @s2txcl95uvubmn:e1 -i --compact\n\n{ "snapshot_id": <span class="s">"s2txcl95uvubmn"</span>, "ref_count": 33,\n "children": [\n { "role": "button", "name": "C", "ref_id": <span class="s">"@s2txcl95uvubmn:e8"</span> },\n { "role": "button", "name": "7", "ref_id": <span class="s">"@s2txcl95uvubmn:e11"</span>,\n "available_actions": ["Click","SetFocus"] } ] }','New refs join the same snapshot. Cost follows the region, not the whole window.'],
['<span class="c"># 3. act on a qualified ref: headless, pointer stays put</span>\n<span class="k">agent-desktop</span> click @s2txcl95uvubmn:e11\n\n<span class="c"># a bare ref is refused</span>\n<span class="k">agent-desktop</span> click @e11\n{ "ok": false, "error": { "code": <span class="s">"INVALID_ARGS"</span> } }','Auto-wait holds the action up to 5,000 ms until the target is visible, enabled and stable.'],
['<span class="c"># 4. verify: success does not prove the UI changed</span>\n<span class="k">agent-desktop</span> wait --element @s2txcl95uvubmn:e6 --predicate value --value 7\n\n<span class="c"># stale after a re-drill?</span>\n{ "code": <span class="s">"STALE_REF"</span>,\n "disposition": { "delivery": "not_delivered", "retry": <span class="s">"safe"</span> } }','Errors say whether a retry is safe. On STALE_REF, snapshot again and retry.']];
var si=0,code=R.querySelector('#ad-code'),note=R.querySelector('#ad-note'),st=R.querySelectorAll('.st');
function show(i){si=i;st.forEach(function(x,j){x.classList.toggle('on',j===i)});code.style.opacity=0;setTimeout(function(){code.innerHTML=S[i][0];note.textContent=S[i][1];code.style.opacity=1;rs()},150)}
code.style.transition='opacity .15s';
st.forEach(function(x){x.onclick=function(){show(+x.dataset.s)}});
R.querySelector('#ad-next').onclick=function(){show((si+1)%4)};
show(0);
/* bars */
function bars(){var f=R.querySelectorAll('#ad-bars .fill');f.forEach(function(x){x.style.transition='none';x.style.width='0'});void R.offsetWidth;setTimeout(function(){f.forEach(function(x,i){x.style.transition='width 1.1s cubic-bezier(.2,.8,.2,1) '+(i*0.12)+'s';x.style.width=x.dataset.w+'%'})},30)}
R.querySelector('#ad-replay').onclick=bars;
/* expanders */
R.querySelectorAll('.oc,.li').forEach(function(x){x.onclick=function(){x.classList.toggle('on');setTimeout(rs,380)}});
window.addEventListener('load',rs);setTimeout(function(){R.querySelector('#ad-play').click()},700);window.addEventListener('resize',rs);setTimeout(rs,300);
})();
</script>
</body></html>" style="width:100%;max-width:880px;height:600px;border:0;display:block;margin:0 auto;background:transparent;" loading="lazy"> 
 window.addEventListener("message",function(e){if(e.data&&e.data.mtpH){var f=document.getElementById("mtp-ad-frame");if(f&&e.source===f.contentWindow){f.style.height=e.data.mtpH+"px";}}}); 

 How does it compare with pixel-based computer use? 

 Model-side computer use tools work from screenshots and pixel coordinates. Anthropic’s docs say each screenshot costs roughly 1,000 to 1,800 input tokens . Its toolset definition adds about 4,500 input tokens per request. OpenAI’s tool similarly returns click, type and scroll actions your code executes. 

 agent-desktop is model-agnostic and returns structure, not images. Microsoft’s UFO² also uses UI Automation, but ships as a full Windows agent. 

 Feature agent-desktop (Vercel Labs) Claude computer use OpenAI computer use Microsoft UFO² Type CLI + C library tool API client toolset API tool Full agent framework How it sees the UI OS accessibility tree Screenshots Screenshots or code (PyAutoGUI, Playwright) UIA + visual hybrid Model bundled None, any agent Claude models OpenAI models Configurable LLM Platforms macOS, Windows, Linux Any env you host (reference: Linux Docker) Browser or desktop you host Windows (UFO²) Moves your cursor No, headless by default Yes, pixel clicks Yes, pixel clicks GUI + API actions Token cost per look 273 (Apple Maps skeleton, self-reported) ~1,000 to 1,800 per screenshot Not disclosed Not disclosed License Apache-2.0 Proprietary API Proprietary API MIT Price Free Standard token pricing Standard token pricing Free (plus LLM costs) 

 How do you install and use agent-desktop? 

 Install with npm install -g agent-desktop . Bun, Yarn and pnpm work too. The package bundles native binaries for x64 and ARM64. 

 macOS: grant Accessibility permission with agent-desktop permissions --guide . 

 Windows: no grant needed for apps at your terminal’s integrity level. 

 Linux: needs a graphical session with at-spi2-core . 

 Agents learn the tool from bundled docs via agent-desktop skills get desktop . A skill is also listed on skills.sh . The C library lets Python, Swift, Go, Ruby and Node hosts call it in process. For Electron web contents, launch --cdp opens a DevTools port for agent-browser . 

 Key Takeaways 

 agent-desktop gives any agent computer use through OS accessibility trees. 

 It runs on macOS, Windows and Linux, x64 and ARM64, under Apache-2.0. 

 Headless ref actions never move your pointer or steal focus. 

 Skeleton snapshots cut tokens 78% to 96% (self-reported). 

 Apps without an accessibility tree remain out of reach. 

 Check out the GitHub repo , docs and npm package . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Vercel Labs Open-Sources agent-desktop for Agent Computer Use appeared first on MarkTechPost .
