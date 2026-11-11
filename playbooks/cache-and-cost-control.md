# Playbook: the economics — caching, budgets and published bills

Why one run costs $15 and an identical-looking one costs $60, and how to make your numbers credible.

**Evidence:** [fable52-fps-repro](../teardowns/fable52-fps-repro.md) (measured cache economics) · [Saltline](../teardowns/saltline.md) (~$550, author-reported) · [fable-5-2-benchmark](../teardowns/fable-5-2-benchmark.md) ($278.26 / 10 jobs) · [blender-effort-test](../teardowns/blender-effort-test.md) (cost per version published)

## The one number that matters: cache hit rate

Long agent runs are **read-heavy loops**: the model re-reads its growing project every round (Saltline: ~165 input tokens per output token). On Claude, a cache hit costs a small fraction of base input price (fps-repro measures the hit price at **0.025×** base input at Fable 5.2 list prices) — so:

> **fps-repro experiment 04: 73 rounds, 6.61M input tokens, 90.9% cache hits → $15.96. Same run without cache: $60.57.**

Keeping the cache alive is behavioral, not lucky:

- **Rounds seconds apart keep it warm.** An agent working continuously never lets the 5-minute cache expire — this is the default you want.
- **1-hour cache is for gaps, not for speed.** fps-repro's control experiment found 1-hour cache *more expensive* on a continuously-running task ($6.97 vs $4.66): the higher write price ate the benefit while misses were what mattered. Reserve it for runs with >5-minute stalls (waiting on human approval, long builds).
- Don't edit earlier turns/system/tools mid-run — instruction changes belong in new conversations (per Anthropic's Fable guide, enforced by the preserved-thinking prefix check).

## Budgets are arithmetic, not vibes

- Run headless with a ceiling: `claude -p … --max-budget-usd 12` (fps-repro's runner). The run stops at the ceiling; you decide whether to resume.
- Track per-run `runs/*.json` and aggregate with a script (fps-repro's `metrics.py` writes cache-hit %, converted cost, and the no-cache counterfactual). The counterfactual column is what teaches.
- Escalate cheap-first: blender-effort-test's v1 (one quick pass) becomes the brief for v2 (expensive agents told what v1 got wrong) — you pay full price only for the delta.

## Publishing a credible bill

Copied from the repos that do it right:

1. **State the meter**: fps-repro uses Claude Code's `total_cost_usd` at list prices, independently recomputed per line item; fable-5-2-benchmark defines time as "wall clock until the model said done".
2. **State the environment**: GPU-less cloud vs local RTX + Blender MCP; hardware matters (fps-repro: Apple M2 Pro; benchmark: RTX 5060 local / cloud CPU×8).
3. **State effort + model id + versions**: `claude-fable-5-2`, effort xhigh, Claude Code 2.1.322 — a benchmark without these is noise.
4. **Single runs are single runs.** fps-repro flags "each experiment ran once"; don't average what you didn't repeat.
5. **Snapshot stars/claims with dates** if you cite them.

## What it costs, roughly (observed data points)

| Project | Scope | Reported cost |
|---|---|---|
| fps-repro exp. 01–04 | 4 single-file 3D demos | $39.56 measured |
| fable-5-2-benchmark | 10 single-message jobs, 23 h 41 m | $278.26 measured |
| Saltline | full FPS, ~8 h unattended | ~$550 author-reported |
| launch film (@furkancavlakcom) | self-made film, ~57 min | ~$21 author-reported |

The spread is scope and rounds, not model quality. Set the budget before you know which column you're in.

## Checklist

- [ ] Budget ceiling flag on every long run
- [ ] Runs logged to JSON; aggregated with a script, not by eye
- [ ] Cache-hit % and no-cache counterfactual in the summary
- [ ] Environment, model id, effort, tool versions recorded with the bill
- [ ] Subscription runs labeled "converted at list price", not "paid"
