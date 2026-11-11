---
title: "oh-my-fable — vendor prompting guides as a Claude Code plugin"
repo: https://github.com/Junhan2/oh-my-fable
author: "Junhan2"
category: tooling
stack: [Claude Code plugin, 1 hook + 4 skills, session-start rule injection, /fable command]
model: multi (Fable 5.2 / Fable 5.1 / Opus 5.5 rules)
one-shot: false
prompt: published
cost: "free, local"
time: "—"
stars: 61
stars-date: 2026-11-11
summary: "Turns Anthropic's per-model prompting guides into per-session working rules — the docs-follow-you pattern."
summary-zh: "把 Anthropic 官方提示词指南变成每个会话自动注入的工作规则——'文档跟着会话走'的模式。"
---

# oh-my-fable — vendor prompting guides as a Claude Code plugin

A Claude Code plugin that **packages Anthropic's official prompting guides as working rules**: at session start it injects the rules matching your session (autonomous progression, scope limits, finish-what-was-asked, partial edits, progress reporting, formatting, batched tool calls — English original wording), and a `/fable` command turns a vague request into a structured one (goal · context · scope · completion criteria filled from conversation context) before executing. Multilingual docs (ko/en/zh).

```text
/fable 로그인 버튼 눌러도 아무 반응 없어 고쳐줘
→  목표: /api/login 호출 후 /dashboard 이동
   맥락: src/components/LoginButton.tsx, 콘솔 오류 "TypeError: onSubmit is not a function"
   범위: 이 버튼과 핸들러만. 회원가입 폼은 건드리지 않고 후속 과제로 보고
   완료 기준: 실제 클릭 재현, 콘솔 오류 0, 변경 파일 목록 첨부
```

## What it is

- **One hook + four skills**, quoting the vendor guides nearly verbatim: [Prompting Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2), 5.1, Opus 5.5 and Opus 5.
- **Context-aware injection**: detects unattended sessions (`claude -p`, Agent SDK) and adds the unattended-only paragraph only there; subagents get a shorter variant; **touches no files** (no CLAUDE.md writes — removal leaves no trace).
- Companion commands: `/fable-status` (what's on, table), `/fable-audit` (diff your CLAUDE.md/rules against the guide), `/fable-setup` (move rule location, pin mode).

## How it was built

The design insight is **three layers of timing**: session-start injection for standing rules, command-time expansion for one-off vagueness, and an audit command for your *existing* instruction files. Installation is one sentence to Claude Code ("이 repo 설치해줘") — the install path is part of the product.

## What it cost

Free; local rules only. Requires Claude Code ≥ 2.1.258.

## How to reproduce

`claude plugin marketplace add Junhan2/oh-my-fable` then `claude plugin install oh-my-fable@oh-my-fable`.

## What to take from it

1. **Official docs are a product surface.** Converting vendor guidance into a zero-config plugin captured a real need (people don't read model-specific guides when prompts break) — the same pattern powers [nativeprompt](nativeprompt.md).
2. **Match injection to session type** — unattended vs interactive vs subagent — rather than one static system prompt.
3. **Don't write files to install behavior**; reversible plugins beat mutated CLAUDE.md.
4. **Give every automated behavior a read-only window command** (`/fable-status`): trust comes from visibility.

## Sources

- [Repo](https://github.com/Junhan2/oh-my-fable) (ko/en/zh) — rule text sources the four official guides above.
