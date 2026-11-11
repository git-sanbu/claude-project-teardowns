---
title: "Saltline — a browser FPS from one prompt"
repo: https://github.com/realcodebear/saltline-fable-5.2
author: "Run by Felix Rieseberg (Anthropic); mirrored by realcodebear"
category: games
stack: [three.js, single-file HTML, Web Audio, code-only assets]
model: claude-fable-5-2
one-shot: true
prompt: external
cost: "~$550 (author-reported)"
time: "~8 hours (author-reported)"
stars: 46
stars-date: 2026-11-11
summary: "The launch-week viral: one prompt, no human feedback, 8 hours — and what the numbers actually say."
summary-zh: "发布周爆款：一句话提示词、零人工干预、8 小时生成的单文件 FPS，以及账单数字背后的门道。"
---

# Saltline — a browser FPS from one prompt

A small first-person shooter set in a rainy container port: cut three uplink relays while drones ("Gulls") and robot dogs ("Hounds") hunt you. What made it the reference demo of Fable 5.2's launch week was not the game itself but how it came to exist — **one prompt, no human feedback during the run, every model, texture and sound made in code**.

- Original run set up by [Felix Rieseberg](https://x.com/felixrieseberg/status/2119925633564463609) (2026-11-09). No official repo exists; every GitHub Saltline is a third-party restoration or mirror.
- Playable mirror: [realcodebear.github.io/saltline-fable-5.2](https://realcodebear.github.io/saltline-fable-5.2/) · Original artifact: [claude.ai](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp)

## What it is

The entire game ships as **one ~1.4 MB `index.html`**: three.js bundled inline, fonts from Google Fonts, no other outside assets. The mirror's only changes were stripping the claude.ai frame-runtime scripts and adding doctype/charset/viewport tags so the file runs as a plain web page — a useful reminder that artifacts port to plain hosting almost for free.

## How it was built

Per the author's post (his numbers, not independently verified):

- **One prompt, unattended.** The run was set up once; there was no human steering during the ~8 hours of work.
- **~445M input / ~2.7M output tokens**, heavily cached. The input-to-output ratio (~165:1) is the signature of a long agentic loop: the model re-reads its growing file many times to write each next piece, which is exactly the workload prompt caching was built for.
- **Everything generated in code.** Models, sounds and textures are all procedural — no downloaded or generated media assets. This is the constraint that makes a single-file game possible at all, and it recurs across nearly every project in this directory.

## What it cost

About **$550 at API pricing, in ~8 hours** — author-reported. Two readings worth holding at once: it is a striking number for "one prompt", and it is cheap for a shipped playable game. The repro experiment in the next teardown shows where the money goes and how caching decides the bill.

## How to reproduce

The mirror repo has no build: `python3 -m http.server 8731` and open the page. To chase the *process* rather than the artifact, follow [fable52-fps-repro](fable52-fps-repro.md), which re-ran the same one-prompt recipe with published prompts, logs and measured costs.

## What to take from it

1. **A single hard constraint ("one file, everything in code") is doing enormous work** — it eliminates asset pipelines, build steps and integration bugs, leaving the model one coherent artifact to iterate on.
2. **The headline prompt is a system, not a sentence.** What the public saw as "one prompt" was a long unattended loop through a codebase the model kept re-reading; plan for that loop (see the [one-shot playbook](../playbooks/one-shot-single-file.md)), not for a magic sentence.
3. **Virality rewarded artifacts, not code.** The demo spread because it was *playable in a link*. Publishing an instantly-clickable version of an agent build is worth engineering deliberately.

## Sources

- [Original X post](https://x.com/felixrieseberg/status/2119925633564463609) · [Mirror README](https://github.com/realcodebear/saltline-fable-5.2) (cost/time/token figures are the author's own)
- Related restorations: [fable52-fps-repro](https://github.com/wquguru/fable52-fps-repro) · [fps3ademo-saltline](https://github.com/realskyrin/fps3ademo-saltline) · [saltline-field-archive](https://github.com/TholeG/saltline-field-archive)
