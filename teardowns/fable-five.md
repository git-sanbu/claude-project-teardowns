---
title: "fable-five — black hole, C compiler, GPT, physics, SQL, zero-dep"
repo: https://github.com/preacherxp/fable-five
author: "preacherxp"
category: systems
stack: [vanilla JS, WebGL, Web Workers, node test harnesses]
model: claude-fable-5-2
one-shot: false
prompt: none
cost: "not published"
time: "one Claude Code session"
stars: 1
stars-date: 2026-11-11
summary: "Five zero-dependency projects — each shipped next to a test that checks the hard part against ground truth."
summary-zh: "五个零依赖项目：每个都配一个把最难部分对到解析解/数值基准上的测试——'酷'变成'对'。"
---

# fable-five — black hole, C compiler, GPT, physics, SQL, zero-dep

Five browser projects written by Fable 5.2 **in one Claude Code session**: no dependencies, no build step, every project a page you can open. Live at [preacherxp.github.io/fable-five](https://preacherxp.github.io/fable-five/).

| Project | What it does | The hard part |
|---|---|---|
| blackhole | Rotating (Kerr) black hole; every pixel integrates a photon geodesic in Kerr–Schild coordinates, with Doppler beaming and gravitational redshift | shadow edge matches **analytic Kerr values for 4 spins, both directions** |
| cc | A C compiler writing a WebAssembly binary byte by byte (int/char/double/pointers/arrays/structs + type checker); demo is a C ray tracer | 48 checks |
| gpt | 4-layer transformer, 207k params, **hand-written backprop**, training on Shakespeare across CPU cores in Web Workers | 93 gradients checked against finite differences; worker shards equal the whole batch |
| mpm | Water, jelly and snow in one MLS-MPM solver, lit-sphere WebGL rendering | polar/eigen decompositions on 4,000 random matrices; 3,000 stable steps |
| sql | SQL engine: recursive CTEs, window functions, correlated subqueries, B+tree indexes, hash joins, 3-valued NULL logic | 84 checks |

## How it was built

Each project pairs a *demo you can see* with a `node test.js` that validates the numerically checkable core against ground truth rather than snapshots: geodesics against the analytic Kerr shadow, gradients against finite differences, decomposition round-trips on random matrices. The one-session constraint and zero-dependency rule forced small, complete cores (72–646 lines) instead of sprawling front-ends — and the README's **Limits** section itemizes, per project, exactly which corners were cut (static observer mapping a few percent off; `malloc` never frees; no `switch`/`enum`/`float` in the C subset; in-memory SQL without transactions…).

## What it cost

Not published; one Claude Code session.

## How to reproduce

`python3 -m http.server 8000`, open the pages; `for t in blackhole cc gpt mpm sql; do node $t/test.js; done`.

## What to take from it

1. **Test against ground truth, not snapshots.** "Shadow edge matches analytic values for 4 spins" is the difference between a physics toy and a physics demo — pick the one thing that can't be faked and test exactly that (more in the [self-checking playbook](../playbooks/self-checking-agents.md)).
2. **Constraints (zero deps, no build, one session) produce coherent small artifacts** — scope discipline as a quality tool.
3. **Publish the Limits section and make it specific.** Vague humility convinces no one; "rays that circle the hole many times come out black" does.
4. **Hard things make the best demos.** The list (compiler, transformer backprop, MPM, SQL engine) is basically a checklist of CS-course kernels — a durable genre for capability showcases.

## Sources

- [Repo](https://github.com/preacherxp/fable-five) — all numbers above from its README and test descriptions.
