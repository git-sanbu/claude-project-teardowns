#!/usr/bin/env python3
"""Generate the project catalog tables in README.md and README.zh-CN.md.

Reads YAML-ish frontmatter from teardowns/*.md (single source of truth)
and rewrites the block between <!-- catalog:start --> / <!-- catalog:end -->
markers in both READMEs. Standard library only.

Usage:
  python3 scripts/build_catalog.py          # regenerate in place
  python3 scripts/build_catalog.py --check  # exit 1 if READMEs are stale
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORY_ORDER = ["games", "worlds", "film", "systems", "method", "tooling"]
CATEGORY_LABEL = {
    "games": "Games & interactive",
    "worlds": "3D worlds & data",
    "film": "Film & animation",
    "systems": "Systems & engines",
    "method": "Method & benchmarks",
    "tooling": "Tooling",
}
CATEGORY_LABEL_ZH = {
    "games": "游戏与互动",
    "worlds": "3D 世界与数据",
    "film": "影视与动画",
    "systems": "系统与引擎",
    "method": "方法与基准",
    "tooling": "工具",
}
MARK_START = "<!-- catalog:start -->"
MARK_END = "<!-- catalog:end -->"


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise ValueError("missing frontmatter")
    out: dict = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            out[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        elif re.fullmatch(r"-?\d+", value):
            out[key] = int(value)
        elif value in ("true", "false"):
            out[key] = value == "true"
        else:
            out[key] = value.strip('"')
    return out


def esc(cell: str) -> str:
    return cell.replace("|", "\\|").replace("\n", " ")


def load_entries() -> list[dict]:
    entries = []
    for path in sorted((ROOT / "teardowns").glob("*.md")):
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        meta["_slug"] = path.stem
        meta["_category"] = meta.get("category", "other")
        entries.append(meta)
    order = {c: i for i, c in enumerate(CATEGORY_ORDER)}
    entries.sort(key=lambda e: (order.get(e["_category"], 99), -int(e.get("stars") or 0), e["_slug"]))
    return entries


def table(entries: list[dict], zh: bool = False) -> str:
    lines = []
    if zh:
        header = "| 分类 | 项目 | 一句话拆解 | 单发 | 成本 / 耗时 | ★ 快照 |"
        align = "| --- | --- | --- | :-: | --- | --: |"
    else:
        header = "| Category | Project | What the teardown covers | One-shot | Reported cost / time | ★ |"
        align = "| --- | --- | --- | :-: | --- | --: |"
    lines += [header, align]
    for e in entries:
        cat = (CATEGORY_LABEL_ZH if zh else CATEGORY_LABEL).get(e["_category"], e["_category"])
        title = e.get("title", e["_slug"])
        one = e.get("summary-zh" if zh else "summary", "")
        shot = "yes" if e.get("one-shot") else "no"
        cost = e.get("cost", "—")
        time_ = e.get("time", "—")
        if zh:
            cost = {"not published": "未公布"}.get(cost, cost)
            time_ = {"not published": "未公布", "—": "—"}.get(time_, time_)
        costcell = cost if time_ == "—" else f"{cost} · {time_}"
        stars = e.get("stars", 0)
        lines.append(
            f"| {cat} | [{esc(title)}](teardowns/{e['_slug']}.md) | {esc(one)} | {shot} | {esc(costcell)} | {stars} |"
        )
    return "\n".join(lines)


def inject(readme: Path, block: str) -> bool:
    text = readme.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(MARK_START) + r"\n.*?" + re.escape(MARK_END), re.DOTALL)
    if not pattern.search(text):
        raise SystemExit(f"{readme.name}: catalog markers not found")
    new = pattern.sub(MARK_START + "\n" + block + "\n" + MARK_END, text, count=1)
    if new != text:
        readme.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    check = "--check" in sys.argv
    entries = load_entries()
    changed = [
        inject(ROOT / "README.md", table(entries, zh=False)),
        inject(ROOT / "README.zh-CN.md", table(entries, zh=True)),
    ]
    n = len(entries)
    print(f"{n} teardown entries indexed")
    if check and any(changed):
        print("catalog is STALE — run: python3 scripts/build_catalog.py")
        sys.exit(1)
    if check:
        print("catalog up to date")


if __name__ == "__main__":
    main()
