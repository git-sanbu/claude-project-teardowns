---
title: "Blender Effort Test — same scenes at medium vs max effort"
repo: https://github.com/realcodebear/blender-fable-5.2
author: "realcodebear"
category: film
stack: [Blender 5.2, Python scene scripting, Cycles, GLB atlas export, three.js viewer]
model: claude-fable-5-2
one-shot: false
prompt: published
cost: "published on the live page"
time: "not published"
stars: 2
stars-date: 2026-11-11
summary: "Three Blender scenes built twice — one quick pass, then three agents at max effort told what the first pass got wrong."
summary-zh: "三个 Blender 场景各建两遍：快速版 vs 满血版（并告知第一版的错处）——一次干净的努力档位对照实验。"
---

# Blender Effort Test — same scenes at medium vs max effort

Three Blender scenes — a lamp-lit still life, a low-poly floating island, a rainy neon city street — each **built twice from Python with no downloaded models and no image textures**, so you can compare effort levels apples-to-apples. The live page gives you a render-compare slider, orbitable 3D of both versions, the exact prompts, the costs, and downloadable `.blend` files.

Live: [realcodebear.github.io/blender-fable-5.2](https://realcodebear.github.io/blender-fable-5.2/)

## What it is

| Scene | v1 (quick pass) | v2 (max effort) |
|---|---|---|
| Still life | 0.23 MB, 19k tris, 17 materials | 2.38 MB, 182k tris, 24 materials |
| Floating island | 0.36 MB, 13k tris | 1.34 MB, 50k tris |
| Neon city | 0.95 MB, 94k tris, 85 materials | 7.50 MB, **795k tris**, 191 materials |

Whole repo ~58 MB; nothing over 100 MB so no Git LFS needed.

## How it was built

The experimental design is the story:

- **v1 = one prompt, one session, medium effort, all three scenes.**
- **v2 = three separate agents, one scene each, at max effort — each told what v1 got wrong.** Not just "try harder": feedback from the cheap run becomes the brief for the expensive run, a two-stage pattern that generalizes far beyond Blender.
- **The web bridge is engineered, not faked.** `.blend` files use procedural node materials, volumes and path tracing that don't exist in a browser, so `tools/export_glb.py` bakes procedural materials into one 4096px atlas per scene (colour, glow, roughness), applies all modifiers, joins meshes, drops volumes for simple distance fog, and writes the render camera and lights to JSON so the three.js viewer starts where the render was. The README then itemizes *what looks different from Blender* per scene — an honest gap list, not a claim of parity.
- `tools/build_site.py` assembles the comparison page from the artifacts, keeping the site a function of the data.

## What it cost

Cost figures are published on the live page alongside each version (the repo README links them; see the page for current numbers).

## How to reproduce

Open the `.blend` files in Blender 5.2+ (Cycles). Rebuild web assets: `blender -b blend/S1_StillLife_v2.blend --python tools/export_glb.py -- models s1_v2 4096 16`; serve with any static server. GLB loads only on click — a good bandwidth courtesy worth copying.

## What to take from it

1. **Cheap run first, then brief the expensive run with its failures.** Effort/agent-count escalation with explicit "what went wrong last time" beats re-rolling the same prompt at higher cost.
2. **Effort shows up in geometry and materials, not screenshots alone** — 10× triangles and 2× materials between v1 and v2 is the measurable shape of "max effort" here.
3. **Bridge heavyweight DCC output to the web deliberately**: bake to atlas, export camera/lights, then publish an honest difference list. Reusable for any Blender→web showcase.
4. **Ship the `.blend` files.** downloadable sources are what make a demo a learning artifact.

## Sources

- [Repo](https://github.com/realcodebear/blender-fable-5.2) — code MIT, scenes/renders CC BY 4.0.
