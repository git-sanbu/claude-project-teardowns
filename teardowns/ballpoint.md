---
title: "Ballpoint — macro pen footage with zero footage"
repo: https://github.com/crossps/ballpoint
author: "crossps"
category: film
stack: [Blender 4.5 LTS Cycles, Python asset pipeline, resumable renderer]
model: claude (Fable 5.2 per the launch-week post)
one-shot: false
prompt: none
cost: "not published"
time: "~4 h render on RTX 4060 laptop (660 frames)"
stars: 1
stars-date: 2026-11-11
summary: "A 22-second macro shot where handwriting dynamics, cellulose fibres and ink are each a separate script — provenance you can read."
summary-zh: "22 秒微距镜头：手写动力学、纤维素纤维、墨水各是一个独立脚本——'这不是视频模型'的证明方式。"
---

# Ballpoint — macro pen footage with zero footage

The complete source for a **22-second macro shot of a ballpoint pen writing on paper**, rendered in Blender Cycles. No footage, no generated video, no downloaded models or texture packs: the pen, paper fibres, ink, handwriting, camera and lights all come from the Python in `tools/`. The only outside file is Blender's stock studio HDRI. Open-sourced (per the author's launch-week post) precisely **to show it is code rather than a video model**.

## What it is

A pipeline of six purpose-built scripts, each owning one physical layer:

| Script | Owns |
|---|---|
| `hand.py` | strokes as centrelines + **handwriting dynamics**: two-thirds power law speed, wrist acceleration limits, pressure rising as the hand slows, minimum-jerk pen-up arcs, tremor — everything downstream reads this output |
| `paper.py` | several hundred thousand individual cellulose fibres laid into a seamless 41 mm tile at 5 µm/texel, then calendered flat |
| `ink.py` | the line laid texel by texel — ink lands where paper actually touches the ball, edges break up on fibre tops; bakes the groove and each texel's arrival time |
| `rig.py` | per-frame pen, wrist sway, camera, focus, and the ball's rolling rotation integrated from the path it draws |
| `build.py` / `render.py` / `finish.py` | scene assembly; frames (resumable); grade + encode (halation, chromatic aberration, vignette, grain) |

World units are millimetres. 660 frames at 1080p/96 spp ≈ 20 s/frame on an RTX 4060 laptop (~4 h total); an interrupted render resumes where it stopped.

## How it was built

The decomposition is the lesson: **physics-behaving layers as separate scripts with a one-way data flow** (hand → paper → ink → rig → render). No layer reaches into another; the ink script doesn't know a hand exists, only the pressure/path data it receives. That is what makes "every frame is code" an auditable claim: you can read exactly where the line's ragged edge comes from.

## What it cost

Not published; ~6 GB disk for textures and 16-bit frames.

## How to reproduce

Blender 4.5 LTS + Python 3.11 + ffmpeg: run `hand.py`, `paper.py`, `ink.py`, `build.py`, then `render.py` and `finish.py` — commands verbatim in the README, including `--device` flags for CUDA/HIP/METAL/CPU.

## What to take from it

1. **Split by physical cause, not by scene object.** Hand, paper, ink as independent scripts beats a monolithic scene builder for debuggability and believability alike.
2. **To prove "it's not a video model", publish the generator.** The repo *is* the proof; screenshots argue, pipelines demonstrate.
3. **Make long renders resumable** and state the per-frame cost — an agent-driven render farm needs exactly this.
4. **Real-behavior details sell realism**: power-law stroke speed and pressure-slow coupling cost nothing and read as "real" where texture polish doesn't.

## Sources

- [Repo](https://github.com/crossps/ballpoint) (MIT) · launch-week [X post](https://x.com/camperaigg/status/2119777467074580741).
