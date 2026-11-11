# Starter prompt: single-file game / interactive demo

Fill in the `[brackets]` and send as **one message in an empty folder** (environment matters — a folder named after an existing project will leak into the output). Run headless with a budget ceiling, e.g. `claude -p --max-budget-usd 12`. Constraints modeled on the patterns in the [one-shot playbook](../playbooks/one-shot-single-file.md); adapt freely.

```text
Build [a small first-person / third-person / arcade] browser game: [one
sentence of fantasy — setting, player goal, one opponent or hazard]. Tone:
[e.g. rainy industrial, low-poly cozy, neon nocturnal].

Hard constraints:
- Deliver exactly one file, index.html. Everything inline. No build step.
- one library only: three.js r170 from a CDN. Everything else you write.
- No image, model, audio or font files; generate geometry, textures and
  sounds in code (Web Audio, shaders, procedural meshes).
- Playable with keyboard and mouse; degrade acceptably on a phone.
- Performance budget: hold [60] fps on a laptop iGPU; adaptive resolution
  is welcome.

Game requirements:
- A complete 2–4 minute loop: start screen → objective → escalating
  challenge → win and lose states → restart.
- [2–4 concrete verbs: e.g. move, aim/shoot, one interactable, one hazard]
- Synthesized audio for [3] key moments; a mute toggle.

Completion bar (all must pass before you stop):
- The page loads with zero console errors.
- A scripted autoplay run can win and can lose, and you have run it.
- You opened the page in a browser (agent-browser or equivalent), read
  back the console after [the main interaction], and fixed what it
  reported.
- Known visual gaps listed in a closing report, not hidden.

Report at the end: what works, what you verified and how, known gaps,
and anything you could not check.
```

Tips from the teardowns

- **Saltline-shaped runs are loops, not sentences**: expect dozens of rounds and a high input:output ratio; keep rounds seconds apart so caching holds ([why](../playbooks/cache-and-cost-control.md)).
- **Add a stopping rule** for long-horizon work ([early-stopping block](../playbooks/effort-and-early-stopping.md)) if your run exceeds an hour.
- After it lands, publish the prompt, log and cost verbatim — that's what separates a demo from a reproducible experiment ([fable52-fps-repro](../teardowns/fable52-fps-repro.md)).
