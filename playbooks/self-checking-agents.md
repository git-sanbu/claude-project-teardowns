# Playbook: make the agent check its own work

The single highest-leverage habit across every project in this directory: give the agent eyes and a grade. Agents that can *perceive* their output catch what code review can't — and cheap runs become publishable.

**Evidence:** [fable52-fps-repro](../teardowns/fable52-fps-repro.md) (browser screenshots + autoplay) · [fable-five](../teardowns/fable-five.md) (ground-truth tests) · [BLACKOUT](../teardowns/blackout.md) (geometric QA) · [Portals](../teardowns/ai-portals.md) (frame checks + 10× playthrough) · [worm-rider](../teardowns/worm-rider.md) (asset lab) · [earth-whole-story](../teardowns/earth-whole-story.md) (ten test suites)

## The ladder of self-checks

From cheapest to strongest — combine at least two:

1. **Load check.** Open the file, count console errors, require zero. (Minimum bar; catches the embarrassing 70%.)
2. **Ground-truth test on the hard part.** fable-five tests the *one thing that can't be faked* per project: black-hole shadow vs analytic Kerr values for 4 spins; 93 backprop gradients vs finite differences; eigen decompositions round-tripped on 4,000 random matrices. Pick the numerically checkable core and test exactly that, not snapshots.
3. **Perception loop.** fps-repro's system prompt lets the model drive `agent-browser`: open the HTML it just wrote on real GPU, screenshot, read console errors back, fix, repeat. Audio checked by offline render (clipping/silence) — with the honest caveat "not human-listened".
4. **Behavioral test.** The model writes its own script to *finish the game* — fps-repro's experiment 04 played all three waves and verified win/death states; fable5.2demo's autopilot completes the game and records a replay, reproducibly.
5. **Geometric/structural QA.** BLACKOUT builds BVH trees over real geometry: no hand inside armour or ground, camera never inside a mesh, on every second frame; `smooth.mjs` flags camera jerks, `pops.mjs` flags mid-shot appear/vanish. Portals renders every changed world at three points along its flight and checks frames for broken pixels.
6. **Exploratory fuzz.** earth-whole-story runs ten minutes of random use hunting console errors, plus 150+ screenshot contact sheets.

## Enabling moves

- **Asset lab** (worm-rider): one page per hero asset under neutral light, reviewed before composition — find ugly assets while they're cheap.
- **Dated stills as checkpoints** (BLACKOUT departments render stills; `tools/snap.mjs t:47`).
- **Frame-locked capture** (worm-rider `capture.js`): step at exactly 60 fps, composite HUD, offline-render audio — turns "it feels smooth" into a measurable stream.
- **Checks defined before the run** (Sumi OS): 9 acceptance items written by humans, executed in QEMU after; the model's own "done" never entered the record.

## The honesty rules

Every self-check has a blind spot; say which:

- Report what was checked *and how* ("offline render only, not human-listened").
- Publish the model's own delivery notes untouched next to your evaluation (fable-5-2-benchmark's `TESLIM.md`) — the contrast is the review.
- If a check can't be run, the agent reports it couldn't (put that in the completion bar).

## Checklist

- [ ] Load check: zero console errors at load and after the main interaction
- [ ] One ground-truth test on the unfakeable core
- [ ] One perception or behavioral loop (screenshot readback / autoplay completion)
- [ ] Failure of a check blocks "done" — stated in the prompt
- [ ] Blind spots named in the README

## Starter

See [`prompts/self-verify-loop.md`](../prompts/self-verify-loop.md) — a system-prompt block that grants the browser loop and defines the completion bar.
