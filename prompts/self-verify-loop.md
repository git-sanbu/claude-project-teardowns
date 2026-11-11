# Starter prompt: the self-verify loop (system-prompt block)

A system-prompt block granting the agent a browser-perception loop and defining a completion bar that includes verification — the mechanism fps-repro used for its unattended runs. Append to your task prompt or add to the system prompt of a headless run (`claude -p`). Companion to the [self-checking playbook](../playbooks/self-checking-agents.md).

```text
Verification loop — you are expected to use it before claiming done:

- You may open pages you write in a browser (agent-browser or the
  harness's browser tool): load the file, screenshot it, and read the
  console back. You are looking at real GPU output, not a guess.
- Fix what the console and the screenshots report, then re-check. A
  check you could not run is reported as "not checked", never skipped
  silently.
- For interactive work: write and run a scripted driver (autoplay,
  headless clicks, or the page's own debug API) that exercises the
  main path end-to-end, including one win and one failure state.
- For audio: verify by offline render (peak/clipping/silence), and
  state plainly that it was not human-listened.
- For geometry: a collision/containment pass (no object intersecting
  what it must not; camera never inside geometry) counts as a check.

Completion bar — "done" means ALL of:
1. Loads with zero console errors; still zero after the main
   interaction.
2. The perception loop ran at least [2] times (initial + post-fix).
3. The scripted driver completed the main path.
4. A closing report: what works, what you verified and HOW (which
   tool saw it), known gaps, and what you could not check.

Early-stopping rule: persist through ordinary obstacles (a failing
check is a task, not a stopping point). Stop only at deliberate
blockers (missing credentials, destructive actions, ambiguity about
scope) — and report those explicitly with what you need.
```

Why each piece is there

- **"Which tool saw it"** turns self-reports into evidence ([Sumi OS](../teardowns/sumi-os.md): checks, not claims, settle done).
- **"Not human-listened" honesty clause** comes straight from fps-repo's audio handling — blind spots named, not hidden.
- **The early-stopping rule** mirrors the official Fable guidance for long tasks ([effort playbook](../playbooks/effort-and-early-stopping.md): persist through ordinary obstacles, report deliberate blockers).
- Pair with `--max-budget-usd` so the loop is bounded ([cost playbook](../playbooks/cache-and-cost-control.md)).
