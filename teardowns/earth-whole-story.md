---
title: "EARTH: The Whole Story — a verified 13.8-billion-year globe"
repo: https://github.com/arpitpatel25/earth-whole-story
author: "arpitpatel25"
category: worlds
stack: [vanilla ES modules, three.js, data pipeline, acceptance-test suite]
model: claude-fable-5-2
one-shot: true
prompt: none
cost: "not published"
time: "not published"
stars: 7
stars-date: 2026-11-11
summary: "The build refuses content whose source wasn't retrieved — verification-first data engineering for an AI-written atlas."
summary-zh: "构建会拒绝任何没有取回来源的条目——一套验证优先的数据工程，撑起 6.7 万个事件的地球史。"
---

# EARTH: The Whole Story — a verified 13.8-billion-year globe

One globe, one clock: set the time anywhere from the Big Bang to today, turn the Earth, and see what was happening there. Described by its maintainer as a single-prompt experiment; the result is a serious data product — **67,721 dated, located events** from open databases, real plate tectonics, 16 scroll-driven stories, 23 explorable 3D scenes, and a deep India module (1,006 curated events, 229 biographies).

## What it is

- Static site, no backend, no keys, no cross-origin requests; music synthesized in the browser per era.
- Curated content is **data**: a story is a text file in `content/stories`, a trail in `content/trails` — each record *names the retrieved source it was written from*.
- Documents carry the decisions: `PLAN.md` (architecture and pipeline steps), `DECISIONS.md`, `DESIGN.md`, `FINAL.md` (what was built and how it was verified).

## How it was built

The architecture is a pipeline with a spine of checks:

1. **`pipeline/` — numbered scripts** turn open datasets (downloaded to git-ignored `data-raw/`) into `site/data`, tiles and textures. Python handles plates and ice; Node builds the site.
2. **The build refuses unverified content.** A record whose source was not retrieved cannot enter the build — the workflow rule is "write only what the source says", enforced by tooling rather than goodwill.
3. **A ten-suite test taxonomy**, each doing one job: acceptance tests of the written specification, coverage counts against every target, a random 300-link audit, **200 curated claims re-checked against re-retrieved sources** (plus an offline sweep of every claim against the source text already fetched), placeholder scans (no filler, no empty fields), size/secrets/local-path checks, performance, a ten-minute random-use console-error hunt, 150+ screenshot contact sheets, sub-path serving, and music behavior.

That list reads like a checklist for any AI-authored content site: links, facts, coverage, placeholders, secrets, perf, fuzzing, screenshots.

## What it cost

Not published.

## How to reproduce

`npm install`, `node pipeline/build-site.mjs`, then `node tests/run-all.mjs` (writes `tests/results/summary.md`). Serve `site/` with `node pipeline/serve.mjs 4173`.

## What to take from it

1. **Gate content on provenance mechanically.** "Every record names its retrieved source" + a build that refuses violations is how you let an agent write 67k events without inheriting 67k hallucinations. See the [verification-first playbook](../playbooks/verification-first-content.md).
2. **Curated content as plain files** keeps agent contributions reviewable one record at a time — diffs are the review interface.
3. **Write the spec, then test against the spec.** The acceptance suite tests *section 18 of the specification*; AI-written software needs a written definition of done even more than human software does.
4. **Audit samples, sweep everything.** 300 random links + 200 re-verified claims + an offline full sweep balances cost against coverage — a copyable triad.

## Sources

- [Repo](https://github.com/arpitpatel25/earth-whole-story) · data keeps its sources' licenses (share-alike and non-commercial sets isolated per `LICENSES.md`).
