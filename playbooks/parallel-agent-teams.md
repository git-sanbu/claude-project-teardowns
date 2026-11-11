# Playbook: parallel agent teams with a shared contract

How the big builds — 471 worlds, an anime short, an OS — organize work across many agents without collapsing into mush.

**Evidence:** [Portals](../teardowns/ai-portals.md) (lead agent + 28 crews + judges) · [BLACKOUT](../teardowns/blackout.md) (director session + departments from `CONTRACT.md`) · [Sumi OS](../teardowns/sumi-os.md) (12 subagents, 96 min)

## When to use it

The work decomposes into parallel, mostly-independent chunks (worlds, scenes, departments, apps) and one coherent whole must come out. Scale: hours-to-days of agent time. Below ~3 parallel chunks or ~1 hour of work, a single session is simpler — don't build an org chart for a demo.

## The pattern

### 1. One human paragraph, then structure

Portals started from one paragraph of intent; by day ten the structure had *hardened on its own*: a **lead agent owning the engine and shipping every release**, 28 **crews building worlds in parallel**, **judge agents scoring** output into bands the product then used (the picker opens visits with best-rated unseen worlds). The lesson: don't design the org chart upfront — let a director session grow it, then write down whatever worked.

### 2. The contract is the coordination mechanism

BLACKOUT's `CONTRACT.md` is one file containing: the shot list, designs, the **shared map**, **file ownership**, the APIs between departments, and QA rules. That single document replaces "coordination". Steal these fields:

```text
CONTRACT.md
- Objective & audience (one paragraph, stable)
- Work breakdown: departments/teams, each with OWNED FILES (exclusive) 
  and PUBLIC INTERFACES it exposes to others
- Shared coordinate systems: one map file, one clock/cue file everyone reads
- Per-deliverable acceptance: what "done" means, checked how, by whom
- QA rules: which automated checks gate a release
- Change protocol: how an interface change propagates
```

The two load-bearing lines are **file ownership** (two agents never write the same file — collisions die here) and **shared coordinates** (`layout.js` + `shots.js` in BLACKOUT: every department places and times things from the same numbers, so the world stays continuous across cuts).

### 3. Teams check themselves before integration

Each BLACKOUT department rendered stills of its own shots before the final render; each Portals crew's world was frame-checked at three points along its flight. Self-check at the smallest unit, integrate only what passed (see the [self-checking playbook](self-checking-agents.md)).

### 4. Judges and release gates

Portals' judge agents scored every world 1–5; releases were named (s8f), and before each went live the lead agent rendered every new/changed world, dropped failures, and played the assembled site at **10× speed**. The pattern: *evaluation is also agents*, and *shipping is a ritual with gates*, not a git push.

### 5. Expect agent culture

Portals' comments are agent-to-agent notes in a stable dialect ("the owner's ruling of 14 Oct"). Sumi OS's model chose its own name and work breakdown. Don't sand this out of the repo — it's evidence of how the work actually happened.

## Checklist

- [ ] Decomposition has ≤ 1 shared file per pair of teams, and it's named in the contract
- [ ] Every team owns files exclusively; interfaces are written down
- [ ] One map / one clock / one source of dimensional truth
- [ ] Per-unit acceptance + per-release gate, both automated where visual
- [ ] A lead/director owns integration and the release ritual
- [ ] Interruption memos saved if runs span sessions (Sumi OS publishes theirs)

## Starter

See [`prompts/parallel-team-contract.md`](../prompts/parallel-team-contract.md) for a fill-in contract + director prompt.
