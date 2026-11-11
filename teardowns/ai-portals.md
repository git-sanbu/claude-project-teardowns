---
title: "Portals — 471 agent-built worlds in one endless flight"
repo: https://github.com/emollick/ai-portals
author: "Ethan Mollick + Claude agents"
category: worlds
stack: [three.js, static site, lead agent + parallel crews, judge agents]
model: claude (agent-built over 10 days)
one-shot: false
prompt: external
cost: "not published"
time: "204 worlds in first 20 hours; 10 days to s8f release"
stars: 132
stars-date: 2026-11-11
summary: "A solo human wrote one paragraph; a lead agent, 28 world-building crews and judge agents produced 1.4M lines and shipped every release."
summary-zh: "人类只写了一段话；一个主管 agent、28 个世界构建小组和评审 agent 写出 140 万行代码并发布了每个版本。"
---

# Portals — 471 agent-built worlds in one endless flight

An endless, hands-off flight through **471 generated 3D worlds** in the browser — each ends in a portal that opens on the next, two worlds rendering at once so crossings have no cut. As of release s8f (2026-11-09): about **1.4 million lines of JavaScript**, designed and written by AI agents apart from the three.js library and some short borrowed functions. Play it at [portals-endless-worlds.netlify.app](https://portals-endless-worlds.netlify.app).

## What it is

- Every world builds geometry, textures and sound **in code, in the browser** — no model, texture or audio files load. A shared kit (skies, water, terrain, plants, buildings, interiors) feeds all worlds.
- The engine builds the next world a few milliseconds at a time between frames and pre-warms shaders so nothing stalls the crossing frame.
- Agents graded their own output: every world carries a 1–5 band (40 in band 5, 28 in band 1), and the picker opens visits with the best-rated unseen worlds.
- Static site, no backend, no tracking; favorites and settings stay in browser storage.

## How it was built

The README's "How it was built" is the most detailed public account of a long-horizon multi-agent project:

1. **One paragraph from the human.** Ethan Mollick described the idea in October 2026 and "left the building to Claude". Twenty hours later there were 204 worlds live.
2. **Organization emerged, then hardened.** By day ten: a **lead agent** that owned the engine and shipped every release, and **28 teams of agents building worlds in parallel**. Judge agents scored worlds into the bands above.
3. **Release QA was automated and visual.** Before each release the lead agent's tools rendered every new or changed world at three points along its flight and checked frames for errors and broken pixels; failing worlds were dropped. Then the assembled site played at **10× speed** before going live.
4. **The agents left their own paper trail.** Comments in the code are agent-to-agent notes in a stable dialect — the lead agent is "the owner", teams are "crews", their heads "leads"/"designers". A pre-publish license check by agents found *more* borrowed Shadertoy/Stack Overflow functions than the notices file listed, which is why the repo carries CC BY-NC-SA 4.0 — an unusually honest provenance audit.

## What it cost

Not published. (Claude's own estimate, not a count: ~25,000 agents worked on the project.)

## How to reproduce

`npm start` serves the source; `npm run build -- --stamp s8f` reproduced the live site byte-for-byte on 2026-11-09. World = one file exporting a `build()` that returns scene + camera path + duration; the engine does the rest.

## What to take from it

1. **The human contribution was a paragraph and a decision to let go.** The scaling came from organization — one owner agent, many parallel crews, judges — not from a cleverer prompt.
2. **Quality control can itself be agents with eyes.** Frame-render checks plus a 10× playthrough is a pipeline any generative-visual project can steal (see the [self-checking playbook](../playbooks/self-checking-agents.md)).
3. **Ship releases, not a big-bang dump.** Named releases (s8f) with per-release QA let the site grow daily while staying up.
4. **License your output before your users do.** Agents copying shader snippets from the open web created real license obligations the project then honored.

## Sources

- [Repo](https://github.com/emollick/ai-portals) (README written by Claude and checked against the code by other agents) · [X post](https://x.com/emollick/status/2119918307457577163)
