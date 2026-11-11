# Starter prompt: parallel team contract (director + departments)

The coordination artifact behind BLACKOUT and Portals: write this **before** spawning parallel agents. Fill it in, keep it in `CONTRACT.md` at the repo root, and give every team the same file. Pattern and rationale in the [parallel-teams playbook](../playbooks/parallel-agent-teams.md).

```text
# CONTRACT.md — [project name]

## Objective (stable; do not renegotiate mid-run)
[One paragraph: what this is, for whom, the feeling it must produce.
  Example: a 90-second, all-code anime short retelling X, 24 fps,
  cel + painted-background look, no image/video models.]

## Coordinates (single source of truth)
- Shared map: layout.[js/py] — all departments place things from
  these numbers. Nobody else invents coordinates.
- Shared clock: shots.[js/py] — shot list with start/end frames and
  cues. Every department times from this file.

## Departments and file ownership (exclusive)
| Team | Owns (files/dirs) | Exposes to others |
|---|---|---|
| world/terrain | src/world*, land* | build(scene) at map coords |
| [machines/props] | src/[machines]* | placed via layout.py |
| characters/rig | src/folk*, rigs/ | API: spawn(x), poses |
| FX | src/fx* | attach(shot, t) |
| camera/look | src/cams/*, look presets | shot → camera curve |
| sound/score | audio/* | cue list read from shots.py |

Rules: no team writes another team's files; cross-team needs go through
the Exposed API only; an interface change requires updating this table
first and notifying the director.

## Acceptance per unit
- Each team renders [stills at 3 points / its own shots] and checks
  them BEFORE integration.
- Integration drops any unit that fails its check.

## Release gate (automated where visual)
- [ ] every changed unit rendered and frame-checked; failures excluded
- [ ] [qa: collisions/BVH, camera smoothness, mid-shot pops] green
- [ ] full piece played [at 10x speed / end-to-end] before "live"
- [ ] named release + changelog entry

## Interruption protocol (long runs)
Save a resumption memo (state, next step, open blockers) at every stop;
resume from the memo, not from memory.
```

Director-session framing to open the run:

```text
You are the lead/director. Read CONTRACT.md and treat it as binding.
First propose the department briefs (one paragraph each). Wait for my
OK. Then spawn one team per row; each works only in its owned files,
checks itself against the acceptance rules, and reports via its
exposed API. You own integration and the release gate — nothing ships
that hasn't passed it.
```

Notes from the teardowns — let structure *emerge* then freeze it: Portals grew a lead agent + crews + judges over days from one paragraph; you don't need the org chart on day one, but once parallel work starts, file ownership and one map/clock are non-negotiable ([ai-portals](../teardowns/ai-portals.md), [blackout](../teardowns/blackout.md), [sumi-os](../teardowns/sumi-os.md)).
