# Claude Project Teardowns

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE) [![Catalog check](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/catalog.yml/badge.svg)](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/catalog.yml) [![Link check](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/links.yml/badge.svg)](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/links.yml)

A directory of notable projects built with Claude — and, for each one, **how it was actually made**: the process, the numbers, the tricks worth stealing, and how to reproduce it. Alongside the teardowns sit [playbooks](#playbooks) (cross-project patterns you can apply) and [prompt starters](#prompt-starters) you can copy.

Curated around the Claude Fable 5.2 launch wave (November 2026), with room for any well-documented Claude-built project. Maintained independently; not affiliated with Anthropic. [简体中文](README.zh-CN.md)

**Last researched: 2026-11-11.** Cost, time and star figures are author-reported or single-run measurements unless marked otherwise; we link sources rather than verify them. Inclusion is not an endorsement or audit.

## What can you learn from Claude project teardowns?

Claude Project Teardowns is an independent collection of sourced case studies on how Claude-built games, 3D scenes, animations, software and AI-agent workflows were made. Each teardown links to its underlying sources and separates reported costs and timings from missing information. Use it to study a documented build process; the entries are not independent replications or benchmarks.

For a broader directory of Claude Fable 5.2 documentation, prompting practices and projects, see the companion [Awesome Claude Fable 5.2](https://github.com/git-sanbu/awesome-claude-fable-5-2).

## Start here

| I want to… | Read |
|---|---|
| See what one unattended prompt can produce | [Saltline](teardowns/saltline.md) → [fable52-fps-repro](teardowns/fable52-fps-repro.md) |
| Run my own one-shot demo safely | [The one-shot playbook](playbooks/one-shot-single-file.md) + [starter prompt](prompts/single-file-game.md) |
| Organize a many-agent build | [Parallel teams playbook](playbooks/parallel-agent-teams.md) + [Portals](teardowns/ai-portals.md) / [BLACKOUT](teardowns/blackout.md) |
| Make the agent verify its own work | [Self-checking playbook](playbooks/self-checking-agents.md) + [self-verify loop](prompts/self-verify-loop.md) |
| Understand the bill before I run one | [Cost playbook](playbooks/cache-and-cost-control.md) |
| Publish AI-written content without inheriting hallucinations | [Verification-first playbook](playbooks/verification-first-content.md) + [EARTH](teardowns/earth-whole-story.md) |
| Prompt Fable 5.2 properly | [Effort & early stopping](playbooks/effort-and-early-stopping.md) + [nativeprompt](teardowns/nativeprompt.md) |

## The catalog

Stars are a GitHub API snapshot (2026-11-11), not a quality ranking; "one-shot" means the build ran from a single user message without mid-run human feedback.

<!-- catalog:start -->
| Category | Project | What the teardown covers | One-shot | Reported cost / time | ★ |
| --- | --- | --- | :-: | --- | --: |
| Games & interactive | [Saltline — a browser FPS from one prompt](teardowns/saltline.md) | The launch-week viral: one prompt, no human feedback, 8 hours — and what the numbers actually say. | yes | ~$550 (author-reported) · ~8 hours (author-reported) | 46 |
| Games & interactive | [fable52-fps-repro — reproducing Saltline with published costs](teardowns/fable52-fps-repro.md) | Four measured one-shot 3D experiments with every prompt, log and bill published — the best public data on agent-run economics. | yes | $4.66–$15.96 per experiment (measured) · 16.6–40.8 min per experiment | 26 |
| Games & interactive | [Worm Rider — asset lab first, then the game](teardowns/worm-rider.md) | A one-scene Dune prototype built lab-first: hero assets alone under the scene light, then world, loop, sound — plus honest asset exclusions. | no | not published · one working session | 18 |
| Games & interactive | [fable5.2demo — three sentences, three games and a film](teardowns/fable5.2demo.md) | Chinese-language repo where every game ships a report including 'what was faked' — honesty as a feature. | yes | not published · not published | 0 |
| 3D worlds & data | [Portals — 471 agent-built worlds in one endless flight](teardowns/ai-portals.md) | A solo human wrote one paragraph; a lead agent, 28 world-building crews and judge agents produced 1.4M lines and shipped every release. | no | not published · 204 worlds in first 20 hours; 10 days to s8f release | 132 |
| 3D worlds & data | [EARTH: The Whole Story — a verified 13.8-billion-year globe](teardowns/earth-whole-story.md) | The build refuses content whose source wasn't retrieved — verification-first data engineering for an AI-written atlas. | yes | not published · not published | 7 |
| Film & animation | [BLACKOUT — a 79-second anime short, all code](teardowns/blackout.md) | A production contract, parallel agent departments and a render-pass chain turn three.js into cel anime — with automated continuity QA. | no | not published · not published | 7 |
| Film & animation | [Blender Effort Test — same scenes at medium vs max effort](teardowns/blender-effort-test.md) | Three Blender scenes built twice — one quick pass, then three agents at max effort told what the first pass got wrong. | no | published on the live page · not published | 2 |
| Film & animation | [Ballpoint — macro pen footage with zero footage](teardowns/ballpoint.md) | A 22-second macro shot where handwriting dynamics, cellulose fibres and ink are each a separate script — provenance you can read. | no | not published · ~4 h render on RTX 4060 laptop (660 frames) | 1 |
| Systems & engines | [Sumi OS — a bootable desktop OS in 96 minutes](teardowns/sumi-os.md) | Empty folder, one task statement, checks defined before the run — and the untouched code published with SHA-256 hashes. | yes | not published · 96 min across 3 sessions | 2 |
| Systems & engines | [fable-five — black hole, C compiler, GPT, physics, SQL, zero-dep](teardowns/fable-five.md) | Five zero-dependency projects — each shipped next to a test that checks the hard part against ground truth. | no | not published · one Claude Code session | 1 |
| Method & benchmarks | [Claude Fable 5.2 HTML Files — a gallery that verifies itself](teardowns/html-files-gallery.md) | 76 visual studies with prompts, whose screenshots regenerate only when content hashes change — and a deploy gate that blocks on failure. | no | not published · not published | 68 |
| Method & benchmarks | [fable-5-2-benchmark — ten single-message jobs, fully instrumented](teardowns/fable-5-2-benchmark.md) | Ten domains, one common prompt + a 2–4 line task each, zero intervention — and the model's own delivery notes published untouched. | yes | $278.26 total across 10 jobs (measured) · 23 h 41 min total | 1 |
| Tooling | [nativeprompt — rewriting prompts per model, by the vendor's rules](teardowns/nativeprompt.md) | The same line helps Claude and hurts Codex — this tool rewrites prompts per current model and audits your CLAUDE.md for stale-model lines. | no | free, offline, no API keys | 128 |
| Tooling | [oh-my-fable — vendor prompting guides as a Claude Code plugin](teardowns/oh-my-fable.md) | Turns Anthropic's per-model prompting guides into per-session working rules — the docs-follow-you pattern. | no | free, local | 61 |
<!-- catalog:end -->

## Playbooks

Cross-project experience, distilled — each with evidence links, a checklist, and where useful a ready-to-run starter prompt:

- [The one-shot, single-file demo](playbooks/one-shot-single-file.md) — the five constraints that make it work
- [Parallel agent teams with a shared contract](playbooks/parallel-agent-teams.md) — file ownership, one map, one clock, judges, release gates
- [Make the agent check its own work](playbooks/self-checking-agents.md) — from load checks to browser perception loops
- [The economics: caching, budgets and published bills](playbooks/cache-and-cost-control.md)
- [Verification-first content and honest artifacts](playbooks/verification-first-content.md)
- [Effort, early stopping and instruction hygiene on Fable 5.2](playbooks/effort-and-early-stopping.md) — condensed from Anthropic's official guide

## Prompt starters

Fill-in templates, written for this repo (original wording, not copies of any creator's prompt):

- [Single-file game / interactive demo](prompts/single-file-game.md)
- [Code-only 3D world or scene](prompts/threejs-world.md)
- [Blender scene from Python](prompts/blender-scene-script.md)
- [Parallel team contract](prompts/parallel-team-contract.md)
- [Self-verify loop (system-prompt block)](prompts/self-verify-loop.md)

## How each teardown is structured

Every entry in [`teardowns/`](teardowns/) follows the same skeleton, so you can skim or deep-read: **What it is → How it was built → What it cost → How to reproduce → What to take from it → Sources**. Frontmatter on each file (category, stack, one-shot, cost, time, stars snapshot) feeds the generated catalog above — run `python3 scripts/build_catalog.py` after editing; CI checks it stays fresh.

## Sourcing and caveats

- Teardowns summarize and analyze public material (project READMEs, posts); quoted figures belong to their authors and are labeled as reported.
- We link the original sources rather than reproducing creators' media or full prompts; starter prompts here are original.
- Availability, pricing and model behavior change; consult the linked sources for current facts.

## How to cite this collection

Cite **Claude Project Teardowns**, maintained by git-sanbu, at https://github.com/git-sanbu/claude-project-teardowns. For a specific claim, link to the relevant teardown and its original source; include the commit or access date because the collection can change. GitHub's citation metadata is available in [CITATION.cff](CITATION.cff). The collection is independent of Anthropic, and its summaries should not be presented as independent verification of the creators' claims.

## Contributing

Found a well-documented Claude-built project worth a teardown? A correction? See [CONTRIBUTING.md](CONTRIBUTING.md) — additions need a public artifact, a describable process, and sources for any numbers.

## License

Original text is [CC BY 4.0](LICENSE). Linked projects keep their own licenses; nothing third-party is relicensed here.
