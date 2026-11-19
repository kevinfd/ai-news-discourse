---
id: "45afd8c4f87fde43"
title: "Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests"
url: "https://springcraft-ai.github.io/springrep"
link: "https://springcraft-ai.github.io/springrep"
source: "Springrep"
domain: "springcraft-ai.github.io"
source_type: "community"
collector: "hackernews"
date: "2026-11-18T21:08:47Z"
published_date: "2026-11-18"
collected_at: "2026-11-19T13:04:26Z"
authors: ["atomarch"]
language: "en"
summary: "Hey HN, I’m Tony. I’m a co-founder of Springcraft, where we have been doing a lot of CAD modeling for robot parts. Our team kept running into limitations with existing kernels, and so I decided to write a new B-rep kernel and a new comprehensive, kernel-agnostic B-rep conformance test suite. Both are available today under MIT licenses. The kernel, springrep, is written in safe Rust with no…"
tags: []
orgs: ["Anthropic"]
topics: ["robotics & autonomy"]
content_source: "fulltext"
word_count: 544
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50552140"
score: 31
comments: 7
community: "Hacker News"
---

# Show HN: Robotics needs better CAD, so I wrote a B-rep kernel and 3,487 tests

Springrep · atomarch · 2026-11-18

springrep
Exact CAD geometry
in pure Rust.
A boundary-representation (B-rep) kernel. Booleans, fillets, sweeps and STEP on exact geometry, accurate to 1e-7 mm, with every result validated.
Exact to 1e-7 mm
Surfaces are analytic or NURBS, not meshes, so volume, area, and mass properties are computed from the real shape.
Valid or a clear error
Every result is checked for validity, and if it fails you get an error instead of a broken solid, so nothing downstream gets built on a bad shape.
Fast and safe
It has the fastest median case time on brep-conformance, with public results anyone can check. It's pure Rust with no dependencies and no unsafe code, and it compiles to WebAssembly.
Get started01
Set up springrep, an exact B-rep CAD kernel in Rust, and run its first example.
1. If this folder is not a Cargo project, run `cargo new springrep-start` and work in that folder.
2. Run `cargo add springrep`.
3. Write the program below exactly as given. In a new project it replaces src/main.rs. If the
   project already has its own src/main.rs, save it as examples/bracket.rs instead.
4. Run it with `cargo run`, or `cargo run --example bracket` if you saved it as an example. It
   must print:
     volume  18276.001643 mm³
     area    6452.128187 mm²
     wrote bracket.step, 8 faces
   If it prints anything else, stop and tell me what it printed. Don't change the part to make
   the numbers match.
5. Run `cargo doc -p springrep` and read the module docs before writing any new geometry. Then
   ask me what I want to build.
```rust
use springrep::{
    blend::fillet,
    boolean::difference,
    math::{Frame, Vec2, Vec3},
    measure,
    profile::Profile,
    step,
    sweep::extrude,
};
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let base = Frame::new(Vec3::ZERO, Vec3::Z, Vec3::X)?;
    let below = Frame::new(Vec3::new(0.0, 0.0, -1.0), Vec3::Z, Vec3::X)?;
    let plate = extrude(&Profile::rect(Vec2::ZERO, 60.0, 40.0), &base, 8.0, "plate")?;
    let bore = extrude(&Profile::circle(Vec2::ZERO, 12.0), &below, 10.0, "bore")?;
    let part = difference(&plate, &bore)?;
    let part = fillet(&part, &[("plate.end", "bore.side")], 1.5, "round")?;
    println!("volume  {:.6} mm³", measure::volume(&part));
    println!("area    {:.6} mm²", measure::area(&part));
    std::fs::write("bracket.step", step::write(&part, "bracket")?)?;
    println!("wrote bracket.step, {} faces", part.face_count());
    Ok(())
}
```
Things to know:
- Every operation returns a Result. Propagate errors with ?; never unwrap a geometry result.
- Faces are named after the feature that made them: plate.end is the top of an extrusion named
  plate, bore.side is the wall of one named bore. Fillets and chamfers pick an edge by the names
  of the two faces either side of it.
- Run springrep::check::check on each new solid and treat any issue it reports as a bug.
- Units are millimetres.
        use springrep::{
    blend::fillet,
    boolean::difference,
    math::{Frame, Vec2, Vec3},
    measure,
    profile::Profile,
    step,
    sweep::extrude,
};
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let base = Frame::new(Vec3::ZERO, Vec3::Z, Vec3::X)?;
    let below = Frame::new(Vec3::new(0.0, 0.0, -1.0), Vec3::Z, Vec3::X)?;
    let plate = extrude(&Profile::rect(Vec2::ZERO, 60.0, 40.0), &base, 8.0, "plate")?;
    let bore = extrude(&Profile::circle(Vec2::ZERO, 12.0), &below, 10.0, "bore")?;
    let part = difference(&plate, &bore)?;
    let part = fillet(&part, &[("plate.end", "bore.side")], 1.5, "round")?;
    println!("volume  {:.6} mm³", measure::volume(&part));
    println!("area    {:.6} mm²", measure::area(&part));
    std::fs::write("bracket.step", step::write(&part, "bracket")?)?;
    println!("wrote bracket.step, {} faces", part.face_count());
    Ok(())
}
Best in class02
Results from brep-conformance, an open conformance suite for B-rep kernels. Each case's expected result is derived from closed-form mathematics, not from another kernel's output, and every kernel, springrep included, is held to the same criteria.
