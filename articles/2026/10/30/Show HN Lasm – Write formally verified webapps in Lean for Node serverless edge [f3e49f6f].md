---
id: "f3e49f6f952398aa"
title: "Show HN: Lasm – Write formally verified webapps in Lean for Node/serverless/edge"
url: "https://github.com/Millillion/lasm"
link: "https://github.com/Millillion/lasm"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-30T02:05:41Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["lastmjs"]
language: "en"
summary: "Lasm has been my dream for a good part of 2026.\nI firmly believe that formal verification is the next evolution of software engineering and programming languages. This next wave will largely be enabled by the incredibly intelligent LLMs that understand formal verification and its programming languages. Lean is one of the most popular languages that allow for formal verification, and to me is…"
tags: []
orgs: ["Amazon", "Google", "Microsoft"]
topics: ["products & launches", "jobs & society", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 3627
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50299004"
score: 31
comments: 14
community: "Hacker News"
---

# Show HN: Lasm – Write formally verified webapps in Lean for Node/serverless/edge

GitHub · lastmjs · 2026-10-30

Lean 4 for the JavaScript and WebAssembly world. Lasm compiles ordinary Lean 4 programs ahead of time to WebAssembly. One Lean code base can become a Node server, a serverless or edge function, a WASI/Fastly module or a browser app. Because it is Lean, you can prove properties of the code you deploy. The flagship example, Conduit, is the RealWorld app with 117 proved theorems. Lasm ships on npm and brings Lean, Lake and its build tools with it; you only need Node (or Bun or Deno).
npm create @lasm@latest my-app -- --template hono    # then: cd my-app && npm install && npm run dev
AI agents: this README is complete on its own. llms.txt is the short
index, and docs/AI.md lists the rules that save you from wrong turns.
If Lasm is useful to you, I'd appreciate your sponsorship (more below).
Every row is tested in CI with the platform's own local runtime, image or emulator. By project policy CI never deploys to a real cloud account (how each is tested).
Node builds have Lean's full runtime (threads, files, processes, sockets). The edge, Bun/Deno, WASI and browser builds run Lean single-threaded, without sockets or processes (and without files, except on WASI); the rest of Lean works.
Every example has a README with a one-command run; examples/README.md lists them all.
examples/conduit is Conduit, the RealWorld app (a Medium clone), written entirely in Lean: the REST API, the server-rendered browser app and the proofs.
- 117 theorems about the code that actually runs, checked with no sorry and
only Lean's standard axioms (npm run proofs; PROOFS.md
lists each one in plain English). They cover authorization (only authors change
their articles and comments), follows and favorites, slugs that never collide,
pagination that never skips or repeats, validation shared by client and server
(the app never sends what the server would reject), JSON round trips and
Markdown link safety. The endpoints are written against a Store of functions,
and the proofs run that same code on a model of the tables.
- What is trusted, not proved: that each SQL statement does what its model says, the JSON text layer, concurrency between requests, and Lean, Lasm and the JavaScript runtime. Conformance to the whole RealWorld spec is tested, not proved.
- API: the official RealWorld API suite passes unmodified (13 of 13 files,
154 requests) on Node (node:sqlite), Cloudflare Workers (D1) and Bun
(bun:sqlite). Each target has one hand-written @[js] binding module.
- Frontend: Lasm.UI on RealWorld's official templates, with server-side
rendering, hydration and Markdown parsed in Lean. The official Playwright
end-to-end suite passes with no retries on Node with Chromium, Firefox and
WebKit, and on Workers and Bun with Chromium.
All of this runs in CI (conduit.yml, run 40615274657,
with @lasm/cli 0.3.4).
cd examples/conduit
npm install                                   # @lasm/cli, Hurl and Playwright (the official suites' runners)
npm run build && npm start                    # http://localhost:3000: the app and its API on Node
npm run proofs                                # check all 117 theorems
npm test                                      # the official API suite (also test:workers, test:bun)
npx playwright install chromium && npm run test:e2e   # the official end-to-end suite
npm run build:workers && npx wrangler dev     # Cloudflare Workers with local D1
npm run build:bun && npm run start:bun        # Bun with bun:sqlite
A single file needs no project. Save this complete program as Main.lean:
def main : IO Unit := do
  IO.println s!"Hello from Lean! 2 + 3 = {2 + 3}"npx @lasm/cli Main.lean          # builds and runs: Hello from Lean! 2 + 3 = 5
npx @lasm/cli build Main.lean    # writes dist/; run it with: node dist/main.mjs
The first build on a new machine fetches Lean and the build tools once (about 250–275 MB; 19 s for that first build on the Linux CI runner). Later dev builds of a one-line change take about 1–2 s.
Each recipe is complete: create, develop, build, deploy. Lasm never installs or
starts a platform's own CLI (wrangler, vercel, fastly, …); you run those.
npm run dev is lasm dev: it rebuilds about 2 s after each save and restarts
the server, and keeps the last good build running when there is a type error.
Node server (Hono; also express, fastify, std-http, fetch).
npm create @lasm@latest my-api -- --template hono
cd my-api && npm install
npm run dev                                   # http://localhost:3000/hello/Ada
npm run build && npm start                    # dist/ needs only Node 24+
docker build -t my-api . && docker run -p 8080:8080 my-api   # the generated Dockerfile
AWS Lambda / Vercel / Netlify / Azure / Google Cloud Functions.
npm create @lasm@latest my-fn -- --template hono --deploy lambda-zip   # or vercel, netlify, azure, gcf, lambda-edge
cd my-fn && npm install
npm run build:lambda                          # dist/ and lambda.zip (handler lasm-lambda.handler)
# deploy lambda.zip with the AWS console, aws CLI or SAM; recipes: docs/deploy/lambda.md
Cloudflare Workers (and Vercel Edge, Netlify Edge, Deno Deploy, Supabase).
npm create @lasm@latest my-edge -- --template hono --deploy workers
cd my-edge && npm install
npm run build:workers                         # workers/ (wrangler.toml came from lasm init)
npx wrangler dev                              # local workerd; npx wrangler deploy to publish
Fastly Compute, WASI, Spin.
npm create @lasm@latest my-svc -- --template fetch --deploy fastly --deploy spin
cd my-svc && npm install
npm run build:fastly && fastly compute serve  # Viceroy on http://127.0.0.1:7676
npm run build:wasi-http && spin up            # or: wasmtime serve wasi-http/main.wasm
Browser app.
npm create @lasm@latest my-web -- --template web
cd my-web && npm install
npm run dev                                   # http://127.0.0.1:5173, live reload
npm run build                                 # dist/: a static site for any host or CDN
Full stack (server + browser + verified API).
npm create @lasm@latest my-app -- --template fullstack
cd my-app && npm install
npm run dev                                   # one URL: http://127.0.0.1:3000
npm run build && npm start                    # Node; also build:workers, build:bun, build:deno
Editor. Run npx lasm editor once per project; lasm init, lasm dev and
lasm build also do it. The Lean editor (VS Code's Lean 4 extension) then resolves
import Lasm.* (details).
The fullstack template is one Lean project with a server (Lasm.Fetch), a
browser app (Lasm.UI) and the API between them (Lasm.RPC). The rule a request
must satisfy is written and proved once, in Shared.lean, which both sides import
(templates/fullstack):
-- Shared.lean
@[irreducible] def checkTitle (title : String) : Except String Unit :=
  let n := (clean title).length
  if n = 0 then .error "Write something first."
  else if n > maxTitle then .error s!"Keep it under {maxTitle} characters."
  else .ok ()
/-- Proved once, holds in the browser and on the server. -/
theorem checkTitle_ok {title : String} (h : checkTitle title = .ok ()) :
    0 < (clean title).length ∧ (clean title).length ≤ maxTitle := by
  unfold checkTitle at h
  by_cases h0 : (clean title).length = 0
  · simp [h0] at h
  · by_cases h1 : (clean title).length > maxTitle
    · simp [h0, h1] at h
    · omega
def addTodo : Endpoint NewTodo Todo := { name := "addTodo", validate := fun r => checkTitle r.title }-- Server.lean: storing a todo demands the proof that its title passed the check,
-- and `addTodo.serve` hands the handler that proof (`ok`) after re-validating.
def Store.add (s : Store) (title : String) (_ : checkTitle title = .ok ()) : Store × Todo :=
  let t := { id := s.next, title := clean title, done := false }
  ({ todos := s.todos.push t, next := s.next + 1 }, t)
  addTodo.serve fun req ok => do
    let (s, t) := (← load kv).add req.title ok
    save kv s
    return .ok t-- Client.lean: a theorem about the browser app: it never sends an invalid title.
theorem add_invalid (m : Model) (e : String) (h : checkTitle m.draft = .error e) :
    (update .add m).2.effects = [.msg (.added (.error (.invalid e)))] :=
  addTodo.call_invalid { title := m.draft } Msg.added "" e h
Where proofs live and how they are checked.
Not proved, tested in CI instead: the JSON/HTTP transport between client and server, the JavaScript that applies patches to the real DOM, the Lasm compiler and runtime, and the browsers. Lean's own compiler is trusted, as in any Lean program (UI.md, RPC.md).
Declare each JavaScript function you call with one line; the Lean type says how
values convert. A complete program (Node's global fetch):
import Lasm.JS
open Lasm.JS
/-- `await fetch(url, init)` (Node's global fetch) -/
@[js "globalThis" "fetch"] opaque fetch : String → Data → IO Value
def main : IO Unit := do
  let response ← fetch "https://example.com" (obj [])
  IO.println s!"{← response.get "status" Nat}: {(← response.callMethodAwait "text" #[] String).length} characters"
The rules for writing bindings:
- @[js "module" "export"] opaque name : A → B → IO R binds module.export. The
module is an npm package ("marked"), a Node built-in ("node:fs"), or "globalThis" for globals. "new Hono" calls a constructor, and "" is the
module's own value.
- End the type in IO R for a value returned at once and in Async R for a
promise. An Async binding is awaited without holding a Lean thread.
- Use String, Nat, Int, Float, Bool, ByteArray, Array, List, Option,
tuples, Data (any JS data) or Value (a JS object reference: get, callMethod, callMethodAwait).
Your own structures convert with deriving ToJS, FromJS.
- Function.ofFn / Function.ofFnReply turn Lean functions into JS callbacks.
Framework handlers use them (see the hono, express and fastify templates).
- npm install the package next to the lakefile. lasm build checks every binding
against the installed package (Lasm.JS binding check failed: … export "x" is missing) and copies production dependencies into dist/node_modules.
- Each call crosses from a Lean thread to Node's main thread (about 24 µs), so prefer one coarse call over many small ones.
Full guide, with Express, Hono, pg, jose and fetch examples and an agent
checklist: docs/JS_BINDINGS.md.
All numbers are from CI on a free GitHub runner (4-CPU AMD EPYC, Linux x64), candidate 0.1.0-experimental.40494203854 (2026-10-27) unless another run is named. Full tables, method and caveats: BENCHMARKS.md.
Lean on Node pays for WebAssembly and its threads. A cold start is CPU-bound, so it
grows on small serverless CPU shares, and every JavaScript call crosses threads.
Pure-Lean Std.Http on Node is slow (1,290 req/s), so use Hono, Express, Fastify
or Lasm.Fetch for production HTTP. Arithmetic on numbers with thousands of digits
is slower than native Lean (no GMP).
- Ahead of time only. A deployed program cannot elaborate, evaluate or compile
Lean, load module data or plugins, or use Lean's C++ compiler/kernel at run time
(exact list). Proofs, tactics, macros and
#eval run while compiling, as usual.
- Lean 4.35.0 exactly. Other lean-toolchain versions are rejected with a
message.
- Node: give an app at least 512 MB; it reserves about 22 GB of virtual address
space. Prebuilt native libraries (-l, shared libraries) cannot be linked; a
package's bundled C source is compiled for you.
- Edge, Bun/Deno, browser, WASI: single-threaded Lean; no sockets, processes or
signals; no files except on WASI. In the browser, blocking waits stop the app
unless it is built with --suspend jspi for a browser with JSPI; use Async.
- No premade bindings for npm packages; Lasm.Web covers the core web platform.
- Editor: Lasm.* imports resolve in the editor after npx lasm editor (above).
- Platforms: no Windows ARM64 and no Alpine/musl build machines (built apps run on Alpine). Hosted platforms are tested with their local tools, never with a real account.
- Start: Getting started · All documentation · For AI agents · llms.txt
- Guides: servers and npm interop · serverless and containers · edge · Bun and Deno · browser and Lasm.UI · full stack (Lasm.RPC) · Lasm.Fetch · WASI and Fastly · the edit loop
- Evidence: benchmarks · where apps run · language coverage · compatible Lean packages · decisions
If Lasm is useful to you or you want to see it succeed, I'd appreciate your sponsorship: github.com/sponsors/lastmjs. It supports me and the work on Lasm and the other Millillion projects. My first goal is $250 a month, enough for one dedicated Claude Code account for Lasm. You can also help by starring the repo, trying it, and reporting what breaks.
Everything below is the precise contract: every command and option, supported machines and platforms, and exactly what a deployed Lean program cannot do.
Install in a project with npm install -D @lasm/cli (the bin is lasm), or run
without installing: npx @lasm/cli Main.lean. npm create @lasm runs lasm init
of the same @lasm/cli version with the arguments unchanged. With the Main.lean
from the quick start:
npx lasm Main.lean                          # build (dev profile) and run: Hello from Lean! 2 + 3 = 5
npx lasm build Main.lean                    # write dist/ (release profile)
npx lasm --version                          # version, Lean, runtime and platform (for bug reports)
node dist/main.mjs                          # run the deployment: only Node is needed
npx lasm build Main.lean --target lambda    # dist/ and an AWS Lambda zip
--rebuild and --verbose work with run and build. --output and --target are
build-only; arguments after -- are run-only. The application's exit status is
preserved. npx lasm --version (-v) prints the version, Lean release, JavaScript
runtime and platform (include it in bug reports). There is no install, clean or
uninstall subcommand.
Build profiles. Both link the same program with the same libraries and are
deterministic. release (lasm build, lasm Main.lean --release): the full
Binaryen size optimization; byte-reproducible; the one to deploy. dev
(lasm Main.lean, lasm dev, lasm build --dev): leaves those passes out and
compiles your modules at -O1; it behaves the same, builds several seconds faster,
and its program.wasm is about 15–20 % larger. A dev rebuild starts from the
project's previous build, so its bytes can depend on that build. build-info.json
records "profile". lasm package and lasm build --dev --target <platform>
refuse a dev build unless you pass --allow-dev.
Environment variables (all optional):
Other LASM_* variables in the source are maintainer diagnostics, not a supported
interface.
Installation. npm install @lasm/cli brings Lean and the build tools as
exact-pinned @lasm/… npm packages for your platform through your own registry,
proxy and cache. The Lake/Lean-import data and, only for Lake projects with C
code, the C tier (@lasm/lean-c-<platform>) are fetched with your npm on first use.
The terminal shows progress; later builds reuse verified tools and unchanged
outputs. On a new machine, without the download, a first Hono build took 25.7 s
(Linux x64), 27.8 s (Linux arm64), 44.4 s (Windows), 58.7 s (Apple Silicon) and
141.9 s (Intel Mac) on the CI runners
(build time, run 40131930601).
Cache locations and recovery: NODE_SUPPORT.md,
INSTALLATION_HARDENING.md.
Git is needed only for Lake projects with Git or Reservoir dependencies; Lasm
uses the git on your PATH and says how to install it when it is missing.
Existing Lake projects build with npx lasm build Main.lean from the project
directory. Pin leanprover/lean4:v4.35.0 in lean-toolchain; other versions are
rejected with Unsupported Lean toolchain … Lasm supports Lean v4.35.0. A
per-package compatibility list covers Batteries, Cli,
LSpec, Plausible, Aesop, Qq, leansqlite, UnicodeBasic, MD4Lean, lean-zip,
lean4-parser, lean-redis and others; packages not on it are untested.
Machines that build with Lasm (the compiler):
Node 24 or newer (tested: 24.0.0, 24.22.1, 26.12.1). No engine flags. Exact tested artifacts: NODE_ACCEPTANCE.md.
A Node dist/ needs Node 24 or newer (Node 22 and older stop with This application requires Node 24.0.0 or newer) and at least 512 MB of memory. It
runs on Linux x64 and arm64 (glibc 2.28+, or musl/Alpine) from a build on any
supported platform, and on the build machine's own platform. Copy all of dist/; no
Lean source, npm install or build tools are needed there. Each platform below is
tested in CI with the local runtime, image or emulator named; none with a real
cloud account. Full matrix: DEPLOYMENT.md.
A dist/ built on Windows and copied to Linux other than through docker build
needs chmod 755 dist/host/native/process/linux-*. Node's --jitless cannot work
(it disables WebAssembly). Hosts that cap virtual memory (ulimit -v,
vm.overcommit_memory=2) refuse the Node build, which reserves about 22 GB of
address space. Node 26's official binary needs libatomic1 on minimal images that
install the tarball themselves.
Builds enforce ahead-of-time execution. Ordinary functions, recursion,
closures, inductive types, pattern matching, type classes, dependent types and
compiled IO are supported. Imports, macros, elaboration, tactics, deriving, proofs
and #eval run during compilation in managed native Lean. Initializers count
as runtime dependencies: a broad import Lean can retain the compiler; use
meta import Lean when only macros or tactics need it, and narrower imports for
runtime data libraries (import Lean with Lean.Json, and deriving ToJson, FromJson, build and run). Each rejection is explained: Lasm prints the chain from
your code to the compiler code and, when a broad import is the cause, the narrower
modules your code uses. Deployed programs honor LEAN_ABORT_ON_NONLINEAR=1 as
native Lean does. Per-platform results: language coverage.
The deployed application cannot use:
The build checks reachable runtime dependencies, including imported libraries and indirect calls; a reachable forbidden call is rejected even if your input would not take that branch, and dead code removed by the linker does not count. The launcher also rejects missing, stale or incompatible capability records before loading the application (a consistency check, not a security sandbox). There is no large compatibility fallback.
Lake packages. Modules imported only for compilation (tactics, elaborators,
for example Aesop, Qq or import Lean for macros) do not keep Lean's compiler in
the deployment. Lasm runs a module's initializers only when the program uses
something they define or register, or when they are the program's own code doing
IO or calling C (--verbose shows how many were skipped). C source that a package
bundles (extern_lib, moreLinkObjs, for example leansqlite's SQLite) is compiled
with Lean's own clang, fetched once as the C tier (39–52 MB); no system C compiler
is needed (macOS needs the Xcode Command Line Tools SDK for C library headers).
Prebuilt native libraries (shared libraries, -l options: libcurl, OpenSSL,
libpq, BLAS) cannot be linked; the build names the library and the package.
Not release guarantees. Console output, arguments, exit codes, local Lake
imports and selected language/filesystem fixtures have native-versus-Node tests,
and before 0.1.0 Lean's runtime-capable upstream suite and 19 ecosystem projects
ran on all five platforms with zero regressions against the previous accepted
candidate (0.1.0 gate). Complete IO.FS, concurrency,
subprocess/signal/terminal parity, every third-party library and the full upstream
suite are not guaranteed (IO gaps). Big numbers (Nat/Int
beyond 63 bits) use Lean's own arbitrary-precision code instead of GNU MP, so apps
contain no LGPL code; results equal native Lean's, but at 10,000 digits
multiplication is about 5× and Nat.gcd about 60× slower than with GMP in Wasm
(numbers). Lake dependencies use
your system Git (system Git).
0.1.0 was the first npm release (notes); 0.2.0 adds
edge targets and Bun/Deno (notes); 0.3.0 adds the
browser, Lasm.UI, full-stack apps, WASI/Fastly and the editor support
(notes); 0.3.1 puts the starter code under MIT-0 and
adds bug-report pointers (notes); 0.3.2 fixes
Std.Internal.UV sockets, timers and signals (notes); 0.3.3 was never
published, and its changes shipped in 0.3.4 (notes); 0.3.5 updates the README and the Conduit example (notes). Lasm's npm
packages (@lasm/cli, @lasm/create and the @lasm/… tool packages) are
published only by the release.yml workflow,
through npm trusted publishing with provenance: no npm tokens exist. A release is a
pull request that bumps the package.json version and is published only after the
release-checks status (five-platform candidate checks; edge, Bun/Deno, browser,
Lasm.UI, WASI/Fastly, fullstack, unit and dev-loop checks; and an npm rehearsal of
the exact packages) passed for the released
commit. Found a bug? npx lasm --version gives the version line the
bug report form asks for. npm view @lasm/cli@<version> shows the provenance, and npm audit signatures in a project verifies it. Details: RELEASING.md.
Lasm's own source is under the MIT License (copyright Jordan Last).
The starter code — everything lasm init and npm create @lasm put in a new
project, templates/, examples/ and the code samples in this README and
docs/ — is also under MIT No Attribution (MIT-0), in every
version: it is yours, no attribution needed. @lasm/create is MIT, and
@lasm/cli's license field is an SPDX expression of Lasm's MIT, MIT-0 and
every component it bundles, with their texts in licenses/. The
license audit lists every distributed component, its
license and how each obligation is met.
- Built dist/. THIRD_PARTY_NOTICES.txt starts with Lasm's MIT notice and
the list of Lean files Lasm changed, then the licenses of what the build contains:
Lean's runtime and standard library (Apache-2.0), Emscripten (MIT OR NCSA), musl,
LLVM libc++, libc++abi, libunwind and compiler-rt, mimalloc, libuv, koffi and
Lasm's host (MIT). Apps contain no copyleft code. licenses/<package>/ holds the
license files of every Lake dependency compiled into program.wasm; with npm
interop, node_modules/ holds each package with its own license. Keep these
files when you distribute a dist/.
- Edge, browser, WASI, Fastly and wasi-http outputs get the same notices,
rewritten to say what their files contain, written automatically: a
THIRD_PARTY_NOTICES.txt in every output directory, a short /*! … */ licence
banner on the JavaScript a platform bundles (the edge glue, the browser loader),
the whole notices file inside the Wasm of server-side outputs (a lasm.notices custom section, so it travels with every deployment), the file in the Fastly
package, and THIRD_PARTY_NOTICES.lasm.txt in Vite builds. What this means for
your app: docs/LICENSING.md.
- Tool packages and release archives. Each @lasm/… tool package has an SPDX license field and the archive's license files. The exact sources of the (L)GPL
pieces the Lean archives contain (GNU MP, the GNU C Library, GCC's runtime
libraries, the Linux UAPI headers, MinGW-w64) and Lean's own source are mirrored
as assets of the release that publishes them
(lean-4.35.0-tiers-v2).
Lasm ships no Git and no Apple SDK files.
- The Lean name and logos are trademarks of Lean FRO. Lasm is not affiliated with or endorsed by Lean FRO.
