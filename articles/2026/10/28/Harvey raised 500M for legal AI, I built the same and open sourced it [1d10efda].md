---
id: "1d10efda47a944fd"
title: "Harvey raised 500M for legal AI, I built the same and open sourced it"
url: "https://github.com/thomasunise/casecite"
link: "https://github.com/thomasunise/casecite"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-28T13:56:21Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["zztopisgreat"]
language: "en"
summary: "CaseCite is an open-source, self-hosted legal research platform. Upload your firm's documents, ask questions, and research cases & judges — on infrastructure you control. Documents, the search index and chat history are stored on your own servers. AI features send your questions and the relevant document text to the AI providers you configure, under your own API keys (BYOK); nothing is sent to…"
tags: []
orgs: ["OpenAI", "Anthropic", "Google", "Cohere"]
topics: ["models & research", "policy & regulation", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 1905
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50273623"
score: 69
comments: 38
community: "Hacker News"
---

# Harvey raised 500M for legal AI, I built the same and open sourced it

GitHub · zztopisgreat · 2026-10-28

CaseCite is an open-source, self-hosted legal research platform. Upload your firm's documents, ask questions, and research cases & judges — on infrastructure you control. Documents, the search index and chat history are stored on your own servers. AI features send your questions and the relevant document text to the AI providers you configure, under your own API keys (BYOK); nothing is sent to the CaseCite maintainers, and there is no telemetry. See What leaves your infrastructure.
Nine tools behind one login, all reading from the same document corpus.
Captured from the real UI against a mocked API with fictional firm, matter and
case data (frontend/e2e/screenshots.spec.ts). No real client or case appears.
Practice profile. Nothing about any practice area is baked into the product. You state what you practice, CaseCite drafts a profile of what matters in that practice, and you edit and own it (saved via Settings). It then rides along with every review, redline, and draft as standing context.
Every AI-generated answer, analysis and draft carries a notice to verify it against the source documents and current law before relying on it. CaseCite is a research aid, not a substitute for a lawyer's judgment or for a citator.
Documents, the vector index, chat history and analyses are stored only on your deployment. Using the AI features transmits content to third parties you choose:
- Uploading a document sends its text to the embeddings provider (OpenAI by default; Voyage or Cohere if configured).
- Asking a question, analysing or drafting sends the question and the relevant document text to the LLM provider (OpenAI, Anthropic or Gemini).
- Case-law tools send search queries and citations to CourtListener.
To keep document text entirely on your network, run both models yourself: set
OPENAI_BASE_URL (chat) and EMBEDDING_BASE_URL (embeddings) to
OpenAI-compatible servers you host. Setting only the first still sends
document text to OpenAI for embedding. The full list of outbound data flows,
and how to restrict them, is in docs/subprocessors.md.
Copyright 2026 Thomas Unise. CaseCite is open source under the Apache License 2.0 (LICENSE), an OSI-approved permissive license. In plain terms:
- ✅ Free to self-host, for internal use or for others, modified or not.
- ✅ Free to modify, fork, redistribute and sell, including inside proprietary products, as long as you keep the copyright and license notices and the NOTICE.md attributions, and state what you changed.
- ✅ Contributors grant an explicit patent license for their contributions, which the MIT license does not.
- Your documents, prompts and outputs are yours. The license covers the CaseCite code, not what you put through it.
Commercial support and private installs are available from the maintainer, @thomasunise. See SUPPORT.md. Versions up to 1.3.0 were released under the Elastic License 2.0; that license continues to apply to those versions.
- Docker + Docker Compose
- openssl (to generate secrets)
- An AI provider API key (OpenAI is the simplest start: it covers both chat and embeddings). Optional at the server level — users can each save their own.
git clone https://github.com/thomasunise/casecite.git && cd casecite
cp .env.example .env
# 1. Generate the three REQUIRED secrets (the .env.example placeholders
#    intentionally refuse to boot). Copy each value into .env:
openssl rand -hex 32   # -> SECRET_KEY
openssl rand -hex 32   # -> AUDIT_HMAC_KEY
openssl rand -hex 16   # -> ENCRYPTION_SALT
# 2. In .env also set OPENAI_API_KEY (or leave it empty and save a key under
#    Settings after signing in), then uncomment and set DOMAIN,
#    POSTGRES_PASSWORD and REDIS_PASSWORD in the "Bundled production stack"
#    section (generation hints are in the file; use DOMAIN=localhost to try it
#    on your machine). CORS_ORIGINS and ALLOWED_HOSTS default from DOMAIN.
#    Set REGISTRATION_BOOTSTRAP_TOKEN too (openssl rand -hex 16) — you need it
#    to create the first account.
# 3. Set DISK_ENCRYPTION_ACKNOWLEDGED=true in .env (required to boot).
#    What this acknowledges: the app encrypts BYOK keys and uploaded documents
#    at the application layer (AES-256-GCM), but derived text (vector chunks,
#    chat history, analyses) is stored in cleartext in the app, Postgres and
#    Redis volumes — full-disk encryption of the host is YOUR responsibility.
# 4. Start the full stack (bundled Postgres + Redis + Caddy):
docker compose -f docker-compose.prod.yml up -d
python3 scripts/setup_production.py --create-env --domain <host> does steps
1–2 for you (it generates every secret and writes .env with mode 0600).
Then open https://$DOMAIN (with DOMAIN=localhost: https://localhost).
On a localhost trial Caddy redirects HTTP to HTTPS and serves a certificate
from its own self-signed local CA — the browser warning on first visit is
expected. See "TLS on Internal Networks" in docs/deployment.md
to trust that CA or bring your own certificate.
The first account you register becomes the admin, and registering it requires
the REGISTRATION_BOOTSTRAP_TOKEN from .env — so nobody else who reaches a
fresh instance can claim it. The exact command is under "Create the admin
account" in docs/deployment.md. After that, invite
colleagues from Settings → Users; self-service registration is off by default.
Deploying behind an existing reverse proxy (Coolify/Traefik)? Use the root
docker-compose.yml instead (it expects an external Postgres and Redis and
declares the persistent data volume), and read deploy/COOLIFY-SETUP.md —
you must also set TRUSTED_PROXIES to the proxy's subnet or client IPs
collapse to one.
Users provide AI provider keys via the Settings modal. What firm evaluators should know about custody:
- Per-user keys are stored server-side, AES-256-GCM-encrypted (PBKDF2 key derivation, HKDF per-record separation), in a file store on the data volume.
- Keys are displayed masked-only and are never sent to the browser; the backend decrypts them on demand for each request.
- Env-configured fallback keys (e.g. OPENAI_API_KEY in .env) are shared by
all users of the install — per-user cost attribution requires per-user
BYOK keys.
- ENCRYPTION_SALT can be rotated without losing stored keys: keep the old
value in ENCRYPTION_SALT_PREVIOUS and run python -m app.utils.reencrypt inside the backend container — see docs/secret-rotation.md. SECRET_KEY cannot be rotated without making stored documents unreadable; keep it safe
and backed up off the server.
word-addin/ is a task-pane add-in for Microsoft Word that talks to your own
CaseCite server: analyze the open document and jump to each flagged passage,
insert a suggested rewrite as a tracked change, and research the firm's
documents with the answer inserted as footnoted paragraphs. It signs in with a
short code you approve in the web app (/device), so the pane never holds
your browser cookies, and its session shows up under Settings → Security →
Sessions as "Word add-in". Set WORD_ADDIN_ORIGIN on the server to the
origin the pane is served from. Build, sideloading on Windows, Mac and the
web, Centralized Deployment and the current limits are in
word-addin/README.md.
The stack fails closed on startup if any of these are missing or left as placeholders.
Not required to boot, but the product does little without them:
Using the root docker-compose.yml (external DB/Redis) instead of the bundled
stack? Then DATABASE_URL, REDIS_URL, CORS_ORIGINS, and ALLOWED_HOSTS
are required directly, and set DB_SSL=require for a managed database.
.env.example documents every setting.
- The sync API imports one folder (folder_id) or, with an explicit sync_all, the whole account. The UI has no folder picker yet: "Sync Now"
imports the whole connected account after a second confirmation that says so.
To bring in selected files, use the file pickers instead. Clio's listing is
account-wide, so Clio cannot sync a single folder.
- Filevine uses one firm-wide API key, so it is off until
FILEVINE_ENABLED=true and is then available to admins only.
- The iManage and NetDocuments connectors are experimental. They are
implemented against the vendors' published APIs but have not been tested
against a live tenant, so they are not registered by default: they do not
appear in the connector list and every route for them is refused. Set
EXPERIMENTAL_CONNECTORS=true to enable them (they are then listed with "experimental": true). If you test them against a real tenant, the
maintainer welcomes a report of what worked and what did not.
- Microsoft and Google connections request read-only scopes. Connections made before this release keep their broader grant until reconnected.
Legal tools, Judge intel, Case view, and the case-law side of the strategy engine all read from CourtListener. CourtListener is the only case-law source in the app. The app starts without a token, but the case-law half of the product is not usable without one:
- Citation check hard-fails without it — validate_citation refuses to run
and returns a "token required" error that names where to set the token
(_check_token in backend/app/services/courtlistener_client.py).
- Every other CourtListener call falls back to anonymous access, which is rate-limited hard enough that research features become unusable under any real load.
Get a free token at
https://www.courtlistener.com/help/api/rest/#permissions, then either set
COURTLISTENER_API_TOKEN in .env, or save it instance-wide as an admin
(Settings → API Keys, or POST /api/v1/admin/integrations/courtlistener) —
the stored token overrides the .env value at runtime without a restart.
backend/
  app/
    main.py              FastAPI app, middleware, health
    config.py            Pydantic settings
    routers/             API routers
    services/
      rag/               RAG pipeline (search, generation, citations, intent)
      vectordb.py        ChromaDB/Pinecone abstraction
      embeddings.py      Multi-provider embeddings
      auth.py            JWT auth
      strategy.py        Matter strategy briefs
      courtlistener.py   CourtListener API
      ...
    middleware/          Security, CSRF
  migrations/            Alembic migrations
frontend/
  src/
    App.tsx
    api/                 Per-domain API clients
    views/               Page views
    stores/              Zustand stores
    components/          Shared components + modals
    layout/              App shell
scripts/                 Backup/restore, production setup, key rotation, NOTICE generator
docs/                    Deployment, data flows, secret rotation, incident response, ADRs
Dockerfile               Unified image (frontend + backend)
docker-compose.prod.yml  Bundled stack: Caddy + Postgres + Redis + backend
docker-compose.yml       Behind an existing proxy (Coolify/Traefik); external Postgres + Redis
docker-compose.dev.yml   Local development
These are implemented and reachable over the API, but the frontend does not expose them yet. Treat them as preview:
- Matters (/api/v1/matters) — matter records, membership, and sharing of
documents and chats between members. Creating matters and changing
membership requires the matters.manage permission.
- Strategy briefs (/api/v1/strategy) — each proposition is searched on
CourtListener, candidate opinions are read, and a citation is kept only when
a verbatim quote can be located in the real opinion text. Unsupported
citations are dropped rather than shown.
- Azure AD SSO — backend token exchange only; there is no sign-in button. SAML, generic OIDC and SCIM are not supported.
Everything else in the feature table above, plus user administration and the audit log (Settings, admins only), has a UI.
- Password sign-in (PBKDF2-SHA256) with optional or mandatory TOTP MFA and recovery codes; password reset by email and change-password in the app
- JWT access tokens with rotating refresh tokens in httpOnly cookies, JTI revocation in Redis (required in production), "sign out everywhere"
- Sessions capped at 5 per user, with an 8-hour absolute lifetime and an idle timeout
- Role-based permissions (require_permission), adjustable per role by an admin
- Per-user (and per-matter) scoping on every document, chat and analysis
- CSRF double-submit cookies, HMAC-signed; per-IP rate limiting; account lockout
- AES-256-GCM at-rest encryption for uploaded originals, API keys, connector tokens and MFA secrets. The vector index and database rely on disk encryption that you provide
- CSP, HSTS, X-Frame-Options, Permissions-Policy headers
- Audit log with HMAC-SHA256 chain hashing, verified at startup and on demand
CaseCite holds no security certification (SOC 2, ISO 27001, HIPAA). What it does and does not do is described in SECURITY.md, which also explains how to report a vulnerability; known gaps are listed in ROADMAP.md.
See CONTRIBUTING.md. PRs welcome. Contributions are accepted under the Apache License 2.0 with a Developer Certificate of Origin sign-off (git commit -s).
