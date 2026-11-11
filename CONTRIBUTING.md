# Contributing to Claude Project Teardowns

Thanks for helping. This directory earns trust through sourcing discipline — please read the short rules before opening an issue or PR.

## What belongs here

A **teardown** of a project that (a) was built with Claude in a way the builders have *described publicly*, (b) has an accessible artifact (repo, playable demo, film), and (c) has a describable *process* — not just a result. Viral-with-no-method projects can't be torn down yet.

## Sourcing rules

- Every number (cost, time, tokens, stars) needs a linkable source and a date; author-reported figures are labeled as such.
- Quote sparingly and attribute; do not copy creators' media files or their full prompts. Starter prompts in this repo are original.
- Star counts are API snapshots — record the date in frontmatter (`stars-date`) and never present them as growth claims.
- If you could not verify something, write that down in the teardown. "Not verified" is a feature here.

## Teardown format

Copy the skeleton from any existing file in [`teardowns/`](teardowns/). Required frontmatter fields:

```yaml
---
title: "Name — one-line hook"
repo: https://github.com/owner/name
author: "who built it"
category: games | worlds | film | systems | method | tooling
stack: [main technologies]
model: claude-fable-5-2        # or other, as documented
one-shot: true | false
prompt: published | external | none
cost: "figure (source-labeled)"
time: "figure"
stars: 0
stars-date: YYYY-MM-DD
summary: "one line for the EN catalog"
summary-zh: "一行中文摘要"
---
```

Sections in order: **What it is → How it was built → What it cost → How to reproduce → What to take from it → Sources**. Keep "What to take from it" concrete — patterns a reader can apply, not praise.

After writing or editing a teardown, regenerate the catalog and commit both:

```sh
python3 scripts/build_catalog.py
```

CI fails if the READMEs' catalog blocks are stale.

## Playbooks and prompts

New playbooks should synthesize evidence from **at least two** teardowns (link them), end with a checklist, and link a starter prompt if one helps. Prompt starters must be original fill-in templates — patterned after public work, never copies.

## Pull requests

Small, focused PRs. Describe what changed and why; for corrections, quote the source that justifies the change. By contributing you agree your text is licensed CC BY 4.0 like the rest of the repository.
