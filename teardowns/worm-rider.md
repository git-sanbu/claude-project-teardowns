---
title: "Worm Rider — asset lab first, then the game"
repo: https://github.com/amirmushichge/worm-rider
author: "Amir Mushich"
category: games
stack: [three.js r165 (CDN, no build), GPU texture baker, frame-locked capture]
model: claude-fable-5-2
one-shot: false
prompt: none
cost: "not published"
time: "one working session"
stars: 18
stars-date: 2026-11-11
summary: "A one-scene Dune prototype built lab-first: hero assets alone under the scene light, then world, loop, sound — plus honest asset exclusions."
summary-zh: "单场景沙虫游戏，先建'资产实验室'再拼世界；不可分发的素材如何诚实处理也有示范。"
---

# Worm Rider — asset lab first, then the game

A one-scene playable prototype: ride a giant sandworm around a ring road and eat the hauler convoys before they reach the gate. Every mesh and texture is generated in code at load — no 3D model or texture files; sand, drone and rumble sounds synthesized in the browser. The only dependency is three.js r165 from a CDN, with **no build step**. From the [launch-week X post](https://x.com/AmirMushich/status/2119937977426338283).

## What it is

A disciplined small codebase where each concern owns one file: `tex.js` is a **GPU baker** for every tiling texture (sand, metal, hide, flesh); `mats.js` adds triplanar micro-detail and sand dust to standard PBR; `wormskin.js` bakes the worm's hide as one height function to normal/mask maps read back for displacement; `wormrig.js` does GPU spine bending and dive/breach/landing simulation; `capture.js` records **frame-locked footage** (steps at exactly 60 fps, composites the HUD, posts JPEG frames to a local server, renders the soundtrack offline). `lab.html?a=truck|rock|worm&cam=N` puts each hero asset alone under the scene light.

## How it was built

> "Built in one working session with Claude (Fable 5.2) in Claude Code: **asset lab first** (hauler, rock, worm alone under the scene light), then the world, then the game loop, cameras, effects and sound."

That ordering — *review each hero asset in isolation before composing the scene* — is the transferable trick: it catches ugly assets while they are still cheap to fix. The repo is equally disciplined about **what it does not contain**: three licensed sound recordings and a horizon image can't be redistributed, so they are excluded, the game runs without them, and the README documents exactly which files to drop into `assets/` to restore the full mix. Known limits are itemized (no terrain deformation by the worm, baked far shadows for a fixed sun, capped internal resolution).

## What it cost

Not published; one working session.

## How to reproduce

`node serve.mjs` → `http://127.0.0.1:5350/`. `?start=1` skips the title, `?auto=0` manual control, `P` autopilot. Capture video from the console: `import('./src/capture.js').then(m => m.run(60))`.

## What to take from it

1. **Build an asset lab before the scene.** One page per hero asset under neutral light is a review loop that scales to any hero-asset project (see the [self-checking playbook](../playbooks/self-checking-agents.md)).
2. **Bake textures on the GPU at load** instead of shipping texture files — the pattern behind "no assets, still rich surfaces".
3. **Frame-locked capture as a feature** (`capture.js`) turns a game into a reproducible film source — pair with an offline-rendered soundtrack.
4. **Handle undistributable assets honestly**: exclude, document, provide the drop-in path. License problems you can *read about* beat takedowns.

## Sources

- [Repo](https://github.com/amirmushichge/worm-rider) (MIT) · [X post](https://x.com/AmirMushich/status/2119937977426338283).
