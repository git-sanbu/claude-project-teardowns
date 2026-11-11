---
title: "Sumi OS — a bootable desktop OS in 96 minutes"
repo: https://github.com/hama-jp/sumi-os-claude-fable-5-2
author: "hama-jp"
category: systems
stack: [C, NASM, GRUB, QEMU, Claude Code + 12 subagents]
model: claude-fable-5-2
one-shot: true
prompt: published
cost: "not published"
time: "96 min across 3 sessions"
stars: 2
stars-date: 2026-11-11
summary: "Empty folder, one task statement, checks defined before the run — and the untouched code published with SHA-256 hashes."
summary-zh: "空文件夹加一份任务书，运行前先定好检查项；代码原样发布并附 SHA-256——严肃的实验记录学。"
---

# Sumi OS — a bootable desktop OS in 96 minutes

From an **empty folder and a single prompt** ([prompts/os.txt](https://github.com/hama-jp/sumi-os-claude-fable-5-2/blob/main/prompts/os.txt)), Fable 5.2 (Claude Code, effort high) built a prototype x86 desktop OS that boots in QEMU — and chose its own name, look and work breakdown. The artifact and its records were made for a Japanese YouTube channel's demonstration.

## What it is

About **9,400 lines of C and NASM**: kernel, interrupts, scheduler, disk and network drivers, a file system, a window system, **nine applications** and an installer. Login `guest`/`guest`. Requires Linux + gcc (32-bit), nasm, GRUB, QEMU, OVMF to build and run.

## How it was built

The methodology is the teardown here:

- **One Claude Code session, three stretches** (31 + 20 + 45 = 96 minutes), interrupted by account usage limits — the "resumption memo" given after each stop is published in `prompts/`.
- The model spawned **12 subagents** across the run (its own choice of work breakdown).
- **Completion was defined before the run, by humans**: 9 acceptance items in `checks/`, executed by the producer driving QEMU, with screenshots; `RESULTS.md` records outcomes. Notably, **the model produced no final completion report** — the checks, not a claim of done, settled the question.
- **Integrity by hash.** No code was changed by hand; for publication the producer filled three gaps in the model-written README from source and removed one leftover file, and `SHA256SUMS.txt` preserves the run's exact bytes. The delta between "as-run" and "as-published" is fully specified.
- **Honest framing**: explicitly *not* a reproduction of Anthropic's official 1,000+ subagent, 8-day OS case — one run, much smaller scale.

## What it cost

Not published. 96 minutes of wall-clock work time.

## How to reproduce

`cd sumi-os && ./build.sh && ./run.sh` on Linux with the toolchain above. The prompt and resumption memos are in `prompts/`; conditions in `CONDITIONS.md`.

## What to take from it

1. **Write the acceptance checks before you run.** Pre-registered checks (in QEMU, driven by a human) are what make a spectacular claim land as evidence — the model's own "done" never enters the record. See the [verification-first playbook](../playbooks/verification-first-content.md).
2. **Publish interruption memos too.** How you resume a long run after a limit stop is a real, under-documented part of agent workflows; this repo shows the memos verbatim.
3. **Hash your artifacts.** SHA-256 manifests make "untouched as the run left it" a checkable statement, not a promise.
4. **Scope honesty compounds credibility.** The explicit "this is not the official case" paragraph is why the rest of the page is believable.

## Sources

- [Repo](https://github.com/hama-jp/sumi-os-claude-fable-5-2) (Japanese, with English summary) · model-written `sumi-os/README.md` inside.
