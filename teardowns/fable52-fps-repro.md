---
title: "fable52-fps-repro — reproducing Saltline with published costs"
repo: https://github.com/wquguru/fable52-fps-repro
author: "wquguru"
category: games
stack: [Claude Code headless, three.js, Web Audio, agent-browser, metrics scripts]
model: claude-fable-5-2
one-shot: true
prompt: published
cost: "$4.66–$15.96 per experiment (measured)"
time: "16.6–40.8 min per experiment"
stars: 26
stars-date: 2026-11-11
summary: "Four measured one-shot 3D experiments with every prompt, log and bill published — the best public data on agent-run economics."
summary-zh: "四个带完整提示词、日志和账单的一句话 3D 实验：目前关于 agent 运行经济学最好的公开数据。"
---

# fable52-fps-repro — reproducing Saltline with published costs

Inspired by Saltline, this repo is not a mirror but a **controlled reproduction**: four independent single-prompt experiments (audio workstation, materials, hard-surface modelling, full FPS), each a single-file HTML demo, with the exact prompts, a run script, browser self-checking, and a measured cost table. Trilingual README (zh / en / ja).

Play everything at [wquguru.github.io/fable52-fps-repro](https://wquguru.github.io/fable52-fps-repro/).

## What it is

| Experiment | Output | Rounds | Cache hit | Measured cost |
|---|---|--:|--:|--:|
| 01 Procedural audio bench (5-min cache) | 56 KB, 14 synthesized sounds | 16 | 88.6% | $4.66 |
| 01 again (1-hour cache, control) | same task | 16 | 78.6% | $6.97 |
| 02 Rainy-dock materials | 55 KB, shader materials | 25 | 83.8% | $8.56 |
| 03 Hard-surface modelling | 69 KB, ~1.85M-tri dockyard | 19 | 76.1% | $10.38 |
| 04 One-sentence FPS "SUBLEVEL 07" | 131 KB, 3 waves, 18 sounds | 73 | **90.9%** | **$15.96** |

All figures measured 2026-11-10 on Claude Code 2.1.322 by the maintainer, who used subscription quota; dollar values are Claude Code's conversion at list prices. Without cache hits, experiment 04 would have been **$60.57 instead of $15.96**.

## How it was built

Three mechanics make this repo worth copying:

1. **Headless, unattended runs with a hard budget.** `scripts/run.sh 04-fps prompts/04-fps.md 5m 12` launches `claude -p` with the prompt and a `--max-budget-usd` cap; the run stops at the ceiling. No mid-run human input.
2. **The agent checks its own work in a real browser.** The system prompt allows `agent-browser`: the model opens the HTML it just wrote, screenshots it on real GPU (Apple M2 Pro), reads console errors back, and in experiment 04 wrote its own script to beat all three waves and verify win/death states before stopping. Audio was checked by offline render (clipping/silence) — honestly reported as *not* human-listened.
3. **Metrics captured per run.** `scripts/metrics.py` aggregates `runs/*.json` into a TSV with cache-hit rates, converted cost, and the no-cache counterfactual — which is how the 0.025× cache-hit price vs base input shows up as a 4× bill difference.

A fourth detail is the most instructive failure in the whole directory: experiments 01–03 ran inside a folder whose *name* contained "saltline", and Fable 5.2 printed **SALTLINE** on their title screens, straight from the folder name. Experiment 04, moved to a clean directory with no `CLAUDE.md`/`AGENTS.md`, named itself "SUBLEVEL 07". Agents read their environment; run creative work in a clean room.

## What it cost

$39.56 for the four experiments (plus the 1-hour-cache control and smoke tests: ~$47 total). The 5-minute vs 1-hour cache control produced a counterintuitive result — 1-hour cache *more expensive* on the same task ($6.97 vs $4.66) — and the README correctly refuses to over-conclude from n=1.

## How to reproduce

Clone, then `scripts/run.sh 01-audio prompts/01-audio.md 5m 12`, then `python3 scripts/metrics.py`. Requires Claude Code 2.1.242+, access to `claude-fable-5-2`, and Chrome + `agent-browser` for the self-check loop.

## What to take from it

1. **Publish the bill.** Measured runs with published prompts turn a viral claim into an reproducible protocol — this is the credibility bar other one-shot repos should aim for.
2. **Cache hits are the business model of long agent runs.** Rounds seconds apart keep the cache warm; that alone cut the flagship run's cost ~4×. See the [cost-control playbook](../playbooks/cache-and-cost-control.md).
3. **Give the agent eyes.** A browser-screenshot feedback loop caught visual/audio breakage the model could not see from code alone — cheap insurance on any generative-UI task.
4. **Budget flags, not hope.** `--max-budget-usd` converts "how bad could it get" into arithmetic.

## Sources

- [Repo](https://github.com/wquguru/fable52-fps-repro) · [data/metrics.tsv](https://github.com/wquguru/fable52-fps-repro/blob/main/data/metrics.tsv) — all figures are the maintainer's single-run measurements, not averages.
