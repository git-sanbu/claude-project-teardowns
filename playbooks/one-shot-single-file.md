# Playbook: the one-shot, single-file demo

How the viral "one prompt → finished playable thing" demos actually work — and the constraints that make them reliable enough to publish.

**Evidence:** [Saltline](../teardowns/saltline.md) · [fable52-fps-repro](../teardowns/fable52-fps-repro.md) · [fable5.2demo](../teardowns/fable5.2demo.md) · [fable-5-2-benchmark](../teardowns/fable-5-2-benchmark.md)

## When to use it

You want a self-contained artifact (game, world, visual study, instrument) that anyone can open from a link, built in one unattended run. Best for: demos, capability probes, launch-week experiments, portfolio pieces. Not for: products with users, anything with a backend or secrets.

## The pattern

Across the successful one-shot runs, five constraints recur. Put them **in the prompt** and the odds change from "sometimes magical" to "usually works":

1. **One file.** "Deliver exactly one `index.html`; everything inline." This kills asset pipelines, build steps and integration bugs — the three places one-shot builds die.
2. **No binary assets.** No downloaded or generated images/models/audio; geometry, textures and sound generated in code (Web Audio, shaders, procedural meshes). Saltline, worm-rider, fable5.2demo and the fps-repro experiments all enforce this.
3. **One library, from CDN.** three.js is the workhorse (r165–r170); pin the version. Everything else hand-written.
4. **A stated completion bar.** "It opens error-free, [specific interactions] work, console shows zero errors at load and after [action]" — otherwise the run stops at "looks plausible".
5. **A budget ceiling.** Run headless (`claude -p`) with `--max-budget-usd N` (fps-repro: `scripts/run.sh 04-fps prompts/04-fps.md 5m 12`). The ceiling turns risk into arithmetic.

## What "one prompt" really is

Every published run with numbers shows the same shape: **a long unattended loop with a 100:1+ input:output ratio** (Saltline: ~445M in / ~2.7M out). The model re-reads its growing file dozens of times, revising section by section. Plan for the loop, not the sentence:

- **Let it self-check** (see the [self-checking playbook](self-checking-agents.md)) — browser screenshots, console-error readback, an autoplay script that must be able to finish the game.
- **Keep rounds seconds apart** so prompt caching holds — that is where a 4× cost difference lives ([cost playbook](cache-and-cost-control.md)).
- **Run in a clean directory.** fps-repro's best gotcha: experiments run in a folder named `saltline` got "SALTLINE" printed on their title screens; the clean-folder run named itself. Agents read the room.

## Checklist before you publish

- [ ] Opens from a static server (or file://) with zero console errors
- [ ] Interacts on desktop and degrades acceptably on mobile
- [ ] States what it is *not* (no audio listened by ear, known visual gaps — copy fable5.2demo's "what was faked" section)
- [ ] Prompt, run log and (if you have them) cost published verbatim
- [ ] Budget, model id, effort level and date recorded

## Starter prompt

See [`prompts/single-file-game.md`](../prompts/single-file-game.md) — a fill-in template with all five constraints above plus a completion bar.
