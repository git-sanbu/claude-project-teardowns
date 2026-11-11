---
title: "nativeprompt — rewriting prompts per model, by the vendor's rules"
repo: https://github.com/edvardgrishin27/nativeprompt
author: "edvardgrishin27"
category: tooling
stack: [Python, zero dependencies, offline, 2749 tests]
model: multi (rules for Fable 5.2, Opus 5.5, GPT-6.x, Sonnet/Haiku 5.5…)
one-shot: false
prompt: published
cost: "free, offline, no API keys"
time: "—"
stars: 128
stars-date: 2026-11-11
summary: "The same line helps Claude and hurts Codex — this tool rewrites prompts per current model and audits your CLAUDE.md for stale-model lines."
summary-zh: "同一句话在 Claude 无害、在 GPT-5.x 有害——按官方规则改写提示词，并审计 CLAUDE.md 里写给旧模型的行。"
---

# nativeprompt — rewriting prompts per model, by the vendor's rules

A zero-dependency, offline CLI with **2,749 tests** and no API keys that does two things: **rewrite a prompt for the model you're actually sitting behind** (Claude Code vs Codex rules differ — "think step by step" is harmless on Claude and counterproductive on GPT-5.x per OpenAI's own docs), and **audit instruction files** (`CLAUDE.md`, `AGENTS.md`, skills, memory) for lines written for *earlier* models, printing `file:line: rule` with a link to the primary source for every edit. It also advises which **effort level** to set for a task, with the vendor citation.

Fable 5.2 rules landed **two days after the model shipped** (2026-11-11), targeting exactly the migration hazards the official guide names: "answer without thinking" lines that no longer disable thinking, unconditional "never" lines that pile up caution, standing "always spawn subagents" lines that dominate session cost. `nativeprompt migrate --from <old> --to <new>` shows what changes across a model transition.

## How it was built

- **Rules are sourced, not vibes**: every rewrite rule cites the vendor's prompting documentation; the README leads with a same-phrase-two-verdicts table (Claude vs GPT-5.x) drawn from those docs.
- **The unit of analysis is your instruction files**, not one-off prompts — because that's where stale lines actually live and accumulate.
- Ship discipline: Fable 5.1 rules next-day, Opus 5.5 next-day, GPT-6 family decoded within days — a *maintenance cadence* as the product, plus per-file `file:line` output so audits are actionable.

## What it cost

Free; runs offline on your subscription workflow.

## How to reproduce

Install per repo (Python 3.9+); `nativeprompt audit` over your repo; `nativeprompt migrate --from fable-5-1 --to fable-5-2` for a transition diff.

## What to take from it

1. **Prompts are model-bound artifacts with a shelf life.** Treat instruction files like code that compiles against a specific model version — audit them on every migration (the [effort playbook](../playbooks/effort-and-early-stopping.md) covers the same hazards).
2. **Cite the vendor doc per rule** — it's what makes a rewriting tool trustworthy rather than another opinion.
3. **Freshness as a feature**: dating your rule updates in the changelog ("added 2 days after release") is a moat bots can't fake.

## Sources

- [Repo](https://github.com/edvardgrishin27/nativeprompt) (ru/en) — all claims above from its README and changelog notes.
