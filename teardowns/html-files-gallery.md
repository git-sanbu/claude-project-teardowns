---
title: "Claude Fable 5.2 HTML Files — a gallery that verifies itself"
repo: https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files
author: "MiaAI-Lab"
category: method
stack: [static gallery, Playwright screenshot pipeline, SHA-verified regeneration, gated Pages deploy]
model: claude-fable-5.2
one-shot: false
prompt: published
cost: "not published"
time: "not published"
stars: 68
stars-date: 2026-11-11
summary: "76 visual studies with prompts, whose screenshots regenerate only when content hashes change — and a deploy gate that blocks on failure."
summary-zh: "76 个视觉研究及其提示词；截图只在内容哈希变化时重新生成，部署门禁失败即阻断——画廊也能工程化。"
---

# Claude Fable 5.2 HTML Files — a gallery that verifies itself

A gallery of **76 HTML studies** with their complete original prompts, indexed as a searchable list with large previews — layout following the maintainers' earlier Fable 5.1 gallery. Live at [miaai-lab.github.io/Claude-Fable-5.2-HTML-Files](https://miaai-lab.github.io/Claude-Fable-5.2-HTML-Files/).

## What it is

Not just a folder of demos: a **build system around a collection**. `scripts/build_gallery.py` builds the index; `scripts/capture_screenshots.py` (Playwright/Chromium) captures real previews and also *tests the gallery itself* — search works, prompts expand, no mobile overflow.

## How it was built

Two mechanics carry the repo:

1. **SHA-gated regeneration.** A committed screenshot is reused only when **both the HTML and the image hashes match `thumbs/manifest.json`**; anything changed or missing is re-captured (`--refresh` forces all). Galleries rot when screenshots silently stop matching their entries — this makes rot impossible to commit undetected.
2. **A deploy gate.** The Pages workflow verifies screenshots, captures changed studies, checks the gallery, and **deploys only HTML, prompts, screenshots and favicon**; a failed capture or check *prevents* deployment. Publishing is downstream of verification, structurally.

Editorially it also does the small things right: source numbering preserved (files 076–078 absent from the supplied collection — "no studies or prompts are invented"), and the README distinguishes what *has* happened (pushed, captured, deployed) from what merely *could*.

## What it cost

Not published.

## How to reproduce

`python3 scripts/build_gallery.py` → `pip install -r scripts/requirements.txt` → `playwright install --with-deps chromium` → `capture_screenshots.py`; serve any static server, or run the gated Pages workflow.

## What to take from it

1. **Content-address your derived artifacts.** Hash-matching screenshots to sources generalizes to any repo where outputs are generated from entries (thumbnails, benchmarks, diffs).
2. **Make CI the publisher.** When deployment happens only after checks pass, "the live site is stale/broken" stops being a possible state.
3. **Test the container, not just the contents** — gallery search, prompt expansion and mobile overflow are the product too.
4. **Preserve provenance of a collection** (original numbering, gaps declared) even when it's "just a gallery".

## Sources

- [Repo](https://github.com/MiaAI-Lab/Claude-Fable-5.2-HTML-Files) · prior [Fable 5.1 gallery](https://miaai-lab.github.io/Fable-5.1-100-HTML-Files/).
