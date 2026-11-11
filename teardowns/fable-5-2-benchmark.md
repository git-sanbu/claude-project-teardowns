---
title: "fable-5-2-benchmark — ten single-message jobs, fully instrumented"
repo: https://github.com/fornhere/fable-5-2-benchmark
author: "fornhere"
category: method
stack: [claude -p headless, effort xhigh, Blender MCP, per-job TESLIM.md, Releases]
model: claude-fable-5-2
one-shot: true
prompt: published
cost: "$278.26 total across 10 jobs (measured)"
time: "23 h 41 min total"
stars: 1
stars-date: 2026-11-11
summary: "Ten domains, one common prompt + a 2–4 line task each, zero intervention — and the model's own delivery notes published untouched."
summary-zh: "十个领域、共同提示词加两三行任务、全程零干预；模型自己写的交付说明原文发布——一套可抄的评测协议。"
---

# fable-5-2-benchmark — ten single-message jobs, fully instrumented

A Turkish-language companion repo to a YouTube video: **ten jobs in ten domains** (web, motion, Blender, shader, 2D animation, fluid simulation, Three.js, motion explainer, Three.js game) given to Fable 5.2 as a *single message each* — no corrections, no retries, no mid-run intervention. Everything the model produced is here: verbatim prompts, all the code, its own delivery notes, timings and costs.

| # | Job | Time | Cost |
|---|---|--:|--:|
| 01 | İstanbul's 2,700 years in one scroll (web) | 2 h 51 m | $46.33 |
| 02 | Headphone launch film (motion) | 2 h 48 m | $35.51 |
| 03 | Istanbul coffeehouse mistaken for a photo (Blender) | 3 h 59 m | $14.09 |
| 04 | Stormy ocean in one shader file | 1 h 28 m | $24.73 |
| 05 | Cat pushing a tea glass (2D animation) | 59 m | $21.52 |
| 06 | Walk through the Grand Bazaar (Three.js) | 1 h 47 m | $34.50 |
| 07 | Aquarium you can reach into (fluids) | 1 h 56 m | $27.65 |
| 08 | Star birth to black hole (motion explainer) | 1 h 18 m | $22.66 |
| 09 | İznik vase breaking in slow-mo (Blender) | 4 h 07 m | $16.66 |
| 10 | Time-rewinding game (Three.js) | 2 h 28 m | $34.61 |
| | **Total** | **23 h 41 m** | **$278.26** |

## How it was built

The protocol is the artifact:

- **One common prompt + a 2–4 line task per job.** The shared prompt (published verbatim, cloud and local variants) fixes the machine description, environment and delivery format; the task adds only the job. Evaluation criteria and "traps" were **deliberately not told to the model**, and each job's page now documents them under "hidden checks".
- **`claude -p` at effort xhigh** — explicitly noted as *above* Claude Code's default medium, so readers can compare like with like.
- **Eight jobs ran on a GPU-less cloud machine; the two Blender jobs ran locally with an RTX 5060 and Blender MCP attached** — environment facts that materially change results, stated up front.
- **Zero intervention, untouched outputs.** No messages, hints or corrections during runs; outputs not edited by hand. Each job directory carries `TESLIM.md` — the model's own completion note, untouched — alongside the full source; only regenerable intermediates (node_modules, frames, caches, `.wav`/`.mp4`) were excluded, and videos/`.blend`s live in Releases.
- Cost = Claude Code's `total_cost_usd` (list-price estimate); time = wall clock from start until the model said it was done — both definitions stated, which most "benchmarks" never bother with.

## What it cost

$278.26 / 23 h 41 m total, measured, single runs — indicative, not statistical. Per-job cost varied 3× across domains ($14–$46) at similar quality bars.

## How to reproduce

Copy the common prompt, append the job's `GÖREV`/`TESLİM` lines, adapt machine details (GPU, Blender version, paths), send as one message in an empty folder. The repo invites publishing your own comparison results.

## What to take from it

1. **Fix the harness, vary only the task.** Common prompt + tiny task delta is what makes ten jobs comparable; hidden checks keep the model from teaching to the test.
2. **State the environment and effort level or the numbers are noise.** GPU-less cloud vs local RTX + Blender MCP is a bigger variable than most prompt tweaks.
3. **Publish the model's delivery notes untouched** (`TESLIM.md`) next to your own evaluation — the contrast is the review.
4. **Define cost and time operationally** (`total_cost_usd`, "until the model says done") and say so in one line.

## Sources

- [Repo](https://github.com/fornhere/fable-5-2-benchmark) (Turkish) · [Releases](https://github.com/fornhere/fable-5-2-benchmark/releases/tag/v1.0) for videos and `.blend` files.
