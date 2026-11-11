---
id: "04e0737ed2a70ebc"
title: "Show HN: Aircad – Professional drafting and 3D modeling in the browser"
url: "https://aircad.com"
link: "https://aircad.com"
source: "Draft, model, and document. Together."
domain: "aircad.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-10T15:01:19Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["peetle"]
language: "en"
summary: "Aircad is a professional CAD system running in the browser with deep AI integration. It includes professional grade drafting and documentation tools, NURBS-based solid modeling, and a lot more. You can make professional quality design documents with it. It is all integrated behind a scripting API that can do anything you can do in the interface and also perform complex modeling operations…"
tags: []
orgs: []
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1098
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50441350"
score: 38
comments: 17
community: "Hacker News"
---

# Show HN: Aircad – Professional drafting and 3D modeling in the browser

Draft, model, and document. Together. · peetle · 2026-11-10

Draft, model, and document. Together.
Precision 2D drafting and 3D modeling, with multiplayer editing and an AI agent that drafts, models, and renders alongside you.
Read the docs
- No installs
- Open a browser and start drawing, always on the latest version.
- Pro 2D & 3D drafting
- Precision drafting and solid modeling in one app.
- Version history
- Every change is on record.
- Opens your DWGs
- With their layouts, blocks, and dimensions.
Pro 2D & pro 3D in one app.
2D drafting and 3D solid modeling in one fast, beautiful workspace, from a command line that takes the shortcuts you already know.
Browse every command
- Familiar drafting tools
- Trim, split, extend, stretch, arcs, hatches, blocks, and layers, with command line precision and snaps.
- NURBS-based solid modeling
- Booleans, fillets, shells, lofts, and sweeps.
- Push/pull modeling
- Pick a face and push or pull it with precision.
- Block libraries built in
- Doors, windows, furniture, and plumbing in Imperial and Metric, plus your team’s own blocks, shared in one place.
Powerful AI on your terms.
Ask a question or describe an edit in plain words, and the agent works right in your drawing.
How the agent works
- Help with the whole job
- It drafts, models, and writes commands, and renders your model as an image or right in a viewport.
- Nothing changes without your OK
- Every change arrives as a draft, highlighted in the drawing, for you to apply or discard.
- Right where you work
- Ask from the command line or the Agents panel, with your choice of model. Threads are saved with the file, private to you.
- Entirely optional
- Everything in Aircad works without it. Use it as much or as little as you like.
Always up to date. Every change on record.
One source of truth for every drawing. No emailed copies, no files checked out, no “final_v3.” Every edit is kept with who made it and when.
Sharing and comments in the docs
Multiplayer editing
Share a link and everyone works in the same file, so there's never a stale copy, and you can see who's working where.
- Always the latest revision
- Everyone edits the same file at once, and each change shows up for everyone as it's made.
- Comments on the drawing
- Feedback stays pinned to the spot it's about, not lost in email, so the context is kept as the drawing changes.
- Review is built in
- Comments, redlines, and marked-up PDFs are part of Aircad. No separate review subscription required.
- Control who can edit
- Share with a link, and decide who can edit and who can only view.
A clear record of every change.
Every file keeps unlimited version history, so nothing is lost and any change can be traced back.
- A complete audit trail
- Every edit is kept with who made it and when, in an activity feed for the file.
- Compare any two versions
- See what was added, changed, and deleted, tinted right in the drawing.
- Fork and edit
- Experiment on a fork from any point in the history. The original stays as it was.
- Restore earlier work
- Bring back an earlier version whenever you need it.
Document everything, beautifully.
A drawing set is only as good as its annotation. Dimensions, GD&T, leaders, text, and tables, on layouts with viewports at any scale that print exactly as they look.
Annotation in the docs
- Every dimension type
- Linear, angular, radius, diameter, arc length, ordinate, baseline, and continue. Each follows the geometry it measures, so it stays right as the design changes.
- GD&T and leaders
- Feature control frames on their own or on a leader, and leaders for notes and callouts.
- Text, tables, and title blocks
- Styled text, tables for schedules and parts lists, and title blocks with attributes. Styles keep a whole set consistent.
- Beautiful view styles
- Sections with hatching, hidden line from the model, line weights, shadows, and physically based materials, with a print preview that matches the PDF.
Bring your files. Take them anywhere.
Open DWG and DXF with their layouts, blocks, and dimensions, and bring in Rhino, STEP, glTF, and SVG. Send drawings back as DWG, DXF, or PDF, and models as STL or OBJ.
What each format brings in
Performance
Serious CAD performance.
250,000+ entities in one file. Keep the whole model in one place instead of splitting it across files to keep your CAD responsive.
108 floors. 38,510 editable solids.
- Big models stay smooth
- Pan, zoom, and orbit stay fluid with thousands of solids on screen, and repeated parts and blocks barely add to the load.
- Edits stay quick
- Changing one part updates just that part, so a big file feels as quick as a small one.
- Heavy work runs in the background
- Booleans, edge fillets, lofts, sweeps, and Make2D run off to the side. The drawing stays live, and Esc stops them.
- Views switch without reloading
- Split the screen, change view styles, or turn on print preview, and the model doesn’t load again.
Make the command you wish you had.
Write commands in JavaScript on the same API our built-in commands use: inputs with snaps, live previews, options, and one undo step. Keep them in the file or share them with your team. Or describe the command and let the agent write it.
Read the script APIimport { BRep, Curve, Plane } from "aircad";
export const manifest = {
  name: "Torus",
  kind: "command",
  capabilities: ["document:read", "document:write"],
  inputs: {
    center: { type: "point", prompt: "Pick the center" },
    radius: { type: "length", prompt: "Major radius" },
    tube: { type: "length", prompt: "Tube radius" },
  },
  api: 1,
};
export default async function main(cad) {
  const center = await cad.input.point("center");
  // Draw the ring while the pointer moves.
  const ring = cad.display.show();
  const radius = await cad.input.length("radius", {
    from: center,
    onChange: (r) => ring.set(Curve.circle(Plane.at(center), r)),
  });
  const tube = await cad.input.length("tube");
  return cad.doc.add(BRep.torus(Plane.at(center), radius, tube));
}
- Deep scripting API
- No matter how strange the problem, our scripting API has you covered.
- Live previews
- Draw as the pointer moves; commit on the click.
- Shared through libraries
- Publish commands to your team and keep everyone current.
- Safe by design
- Scripts run in a sandbox with no network access.
Start drawing together.
Bring your next idea to life, together in one team workspace.
