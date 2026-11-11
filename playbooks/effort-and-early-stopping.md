# Playbook: effort, early stopping and instruction hygiene on Fable 5.2

A condensed, source-linked working guide distilled from Anthropic's official [Fable 5.2 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) and [What's new](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2) pages, cross-referenced with what the projects in this directory actually do. Vendor-reported figures are marked as such; test on your own tasks.

## Calibrate effort — start at high, sweep, don't inherit

- Start at `high` (the API default). Most of the capability gain is already there; gains above it are uneven and task-dependent (Anthropic's reporting). Sweep `medium` and `xhigh` against *your* evals rather than carrying a setting tuned on an older model.
- fable-5-2-benchmark ran everything at **xhigh via `claude -p`** and says so — Claude Code's default is medium; when you publish results, your effort level is part of the method.
- blender-effort-test is the visual version of the same experiment: one quick pass vs max-effort agents briefed with the first pass's failures — 10× triangles, 2× materials, ~10× file size.
- Effort can change **per message mid-workflow** while preserving the prompt cache.

## Fix early stopping — the classic long-task failure

On long multistep tasks the model can end its turn early (more often at low/medium effort): a remaining-work list, an offer to continue, or a stop at an ordinary obstacle. The guide's system-prompt block tells the model to persist through ordinary obstacles while leaving deliberate blockers alone and reporting them — Anthropic reports it **halved sessions ending with doable work left, at roughly +30% output tokens**. Keep your own confirmation step for risky actions. (fps-repro's unattended runs are the practical version: a completion bar in the prompt plus a budget ceiling, so "stopping early" is detectable and costable.)

## Approvals: answer specifically

When resuming an approved step, send a concrete instruction — "Yes, run the migration on the staging database" — not a bare "yes", and name what the approval covers.

## Say who owns the code (it changes the diff)

With no ownership statement the model tends to extend existing structure even when that duplicates code; adding "This codebase is yours" made it merge duplicated code in about half of Anthropic's test tries (vs under a tenth without), at ~1.5× output tokens and more unrequested changes. Review the diff, not the summary; leave the sentence out when you want minimal changes.

## Delegation: set it via the tool description

How much the model delegates tracks your harness prompts. When it over-delegates, rewrite the subagent-starting tool's description to state, in order: what a subagent costs, when delegation is and isn't worth it, how to brief one (Anthropic reports the tested description cut delegation ~⅓ at equal task success). Check which model subagents run on — they can dominate session cost.

## Prune inherited caution

Fable 5.2 follows accumulated cautious instructions (memory, notes, instruction files, inter-agent messages) very closely and can over-ask for approvals. Delete stale notes and inherited caution instead of letting it pile up. On migration, remove or retest: standing delegation lines, written token budgets in prompts, harness code that edits earlier turns (it breaks preserved thinking — make instruction changes only in new conversations).

## Quick reference — breakage map for carried-over prompts

| Old habit | Behavior on Fable 5.2 |
|---|---|
| "Answer without thinking" lines | Don't stop thinking at medium+; remove them |
| `budget_tokens` / thinking `disabled` | Return 400 — thinking is always on; use `effort` |
| Forced tool use (`tool_choice: any/tool`) | Returns 400 — use `auto` |
| Unconditional "never…" lines | Accumulate caution → over-asking; prune |
| Hard word/length limits | Choppy prose; soften |
| Editing system/tools mid-conversation | Prefix-check 400; new conversations only |

[nativeprompt](../teardowns/nativeprompt.md) automates exactly this audit (`file:line: rule` over your CLAUDE.md/AGENTS.md); [oh-my-fable](../teardowns/oh-my-fable.md) injects the official rules per session.

## Checklist for a new task on Fable 5.2

- [ ] `effort: high` explicitly; sweep medium/xhigh on your evals
- [ ] Early-stopping block in the system prompt for long tasks
- [ ] Ownership sentence present (or deliberately absent)
- [ ] Subagent tool description states cost + when + briefing
- [ ] Instruction files audited for previous-model lines (nativeprompt or by hand)
- [ ] No instruction edits mid-conversation
