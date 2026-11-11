---
title: "BLACKOUT — a 79-second anime short, all code"
repo: https://github.com/anstapnever/blackout
author: "anstapnever"
category: film
stack: [three.js WebGL2, render-pass chain, BVH QA tools, code-mixed score, Claude Code]
model: claude-fable-5-2
one-shot: false
prompt: none
cost: "not published"
time: "not published"
stars: 7
stars-date: 2026-11-11
summary: "A production contract, parallel agent departments and a render-pass chain turn three.js into cel anime — with automated continuity QA."
summary-zh: "一份制作契约、并行 agent 部门和渲染 pass 链把 three.js 变成赛璐璐动画，还有自动化连贯性 QA。"
---

# BLACKOUT · 停電 — a 79-second anime short, all code

A 79-second anime short where **every frame is made by code**: no video model, no image model, no hand-drawn frames. A harbour country switches off all its lights to fire a mountain-sized rail cannon at a golden astrolabe; a mech shields the gun with its body; the lights come back. Shot-for-shot retelling of a famous anime sequence with every visual designed from scratch.

Watch: [`film/blackout.mp4`](https://github.com/anstapnever/blackout/blob/main/film/blackout.mp4) (1920×1080, 24 fps, 79.4 s).

## What it is

Under the drawing everything is 3D: terraced towns, pylons, the cannon, two mechs, an otter-and-snow-leopard cast on a shared rig — about **5.7 million triangles**. The anime look is a chain of full-screen passes: hard-edged shadow map → cel-lit main (with depth/ID/normal buffers) → Kuwahara gouache pass on backgrounds → ink lines from edge detection only where a material asks for ink → atmosphere → bloom and film grade. Animation runs **on twos, FX on threes**, like film anime, with anticipation, overshoot and follow-through. The score mixes real CC0 orchestral samples with designed SFX from `audio/render.py`, staying in C minor until the last lamp lights.

## How it was built

> "One director session and parallel agent teams in Claude Code, working from a shared contract ([CONTRACT.md](https://github.com/anstapnever/blackout/blob/main/CONTRACT.md)): world, enemy, machines, characters, FX, sound. Each team owned its own files and cameras and rendered stills to check its work before the final render."

That single sentence is a complete production methodology:

- **The contract is the coordination mechanism.** Shot list, designs, the shared map, **file ownership**, APIs between departments, and QA rules — written down once, in one file, before parallel work starts.
- **One map and one clock.** `src/layout.js` holds the shared map; `src/shots.js` the cues and 34 shots; every department places and times things from those numbers, so the world stays continuous across cuts.
- **Departments check themselves with stills.** Each team rendered its own shots before the final render — the same "agents with eyes" loop as Portals, at department scale.
- **QA is geometric, not vibes.** `tools/qa.mjs` builds BVH trees over the real geometry and tests that no hand, foot or body is inside armour, ground or another body and the camera never enters a mesh — on every second frame. `tools/smooth.mjs` flags camera jerks; `tools/pops.mjs` flags anything appearing or vanishing mid-shot.

## What it cost

Not published. Final render: 1,906 frames.

## How to reproduce

Node 18+, Chrome, ffmpeg, Python 3.11+ (numpy/scipy/soundfile). `npm install`, serve, `node tools/qa.mjs --step 2`, build the score, then `node tools/render.mjs --scale 2 --name blackout`.

## What to take from it

1. **A written contract beats a chatty director.** For parallel agent teams, the highest-leverage document assigns *file ownership* and *shared coordinates* — collisions and continuity breaks both die there. Template in the [parallel-teams playbook](../playbooks/parallel-agent-teams.md).
2. **Style is a pipeline, not a prompt word.** "Make it anime" became six concrete render passes with specific inputs (ID buffers, depth edges) — decompose aesthetic goals into inspectable stages.
3. **Test animation like code.** BVH intersection tests over real geometry catch the failure modes (clipping, pops, jerks) that eyeballing a timeline misses.
4. **Music by cue sheet.** `audio/cuesheet.md` + code-mixed rendering kept score, SFX and picture in one reviewable place.

## Sources

- [Repo](https://github.com/anstapnever/blackout) — render engine partly adapted from the MIT "Leviathan" project; see vendor licenses there.
