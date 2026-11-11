# Claude 项目拆解集

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE) [![Catalog check](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/catalog.yml/badge.svg)](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/catalog.yml) [![Link check](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/links.yml/badge.svg)](https://github.com/git-sanbu/claude-project-teardowns/actions/workflows/links.yml)

一个收录知名 Claude 项目的目录——每个项目都讲清楚**它是怎么做出来的**：过程、数字、值得照搬的门道、以及如何复现。拆解之外，还有跨项目提炼的[实战手册](#实战手册)（拿来就能用的经验）和可以直接复制的[提示词模板](#提示词模板)。

内容围绕 Claude Fable 5.2 发布潮（2026 年 11 月）策展，也欢迎任何过程记录完善的 Claude 项目。独立维护，与 Anthropic 无关。[English](README.md)

**调研截至 2026-11-11。** 成本、耗时与星标数字均来自作者自述或单次实测（另有标注除外）；本目录只链接来源、不复核。收录不构成背书或审计。

## 从这里开始

| 我想…… | 读这篇 |
|---|---|
| 看“一句话、无人干预”能做出什么 | [Saltline](teardowns/saltline.md) → [fable52-fps-repro](teardowns/fable52-fps-repro.md) |
| 自己安全地跑一次单发实验 | [单发 playbook](playbooks/one-shot-single-file.md) + [入门提示词](prompts/single-file-game.md) |
| 组织一次多 agent 协作构建 | [并行团队 playbook](playbooks/parallel-agent-teams.md) + [Portals](teardowns/ai-portals.md) / [BLACKOUT](teardowns/blackout.md) |
| 让 agent 自己检查自己的产出 | [自检 playbook](playbooks/self-checking-agents.md) + [自检循环模板](prompts/self-verify-loop.md) |
| 跑之前先弄清楚要花多少钱 | [成本 playbook](playbooks/cache-and-cost-control.md) |
| 用 AI 写内容又不留下幻觉 | [验证优先 playbook](playbooks/verification-first-content.md) + [EARTH](teardowns/earth-whole-story.md) |
| 正确地给 Fable 5.2 写提示词 | [effort 与早停](playbooks/effort-and-early-stopping.md) + [nativeprompt](teardowns/nativeprompt.md) |

## 项目目录

星标为 2026-11-11 的 GitHub API 快照，不代表质量排序；“单发”指构建过程从一条用户消息开始、中途无人工干预。

<!-- catalog:start -->
| 分类 | 项目 | 一句话拆解 | 单发 | 成本 / 耗时 | ★ 快照 |
| --- | --- | --- | :-: | --- | --: |
| 游戏与互动 | [Saltline — a browser FPS from one prompt](teardowns/saltline.md) | 发布周爆款：一句话提示词、零人工干预、8 小时生成的单文件 FPS，以及账单数字背后的门道。 | yes | ~$550 (author-reported) · ~8 hours (author-reported) | 46 |
| 游戏与互动 | [fable52-fps-repro — reproducing Saltline with published costs](teardowns/fable52-fps-repro.md) | 四个带完整提示词、日志和账单的一句话 3D 实验：目前关于 agent 运行经济学最好的公开数据。 | yes | $4.66–$15.96 per experiment (measured) · 16.6–40.8 min per experiment | 26 |
| 游戏与互动 | [Worm Rider — asset lab first, then the game](teardowns/worm-rider.md) | 单场景沙虫游戏，先建'资产实验室'再拼世界；不可分发的素材如何诚实处理也有示范。 | no | 未公布 · one working session | 18 |
| 游戏与互动 | [fable5.2demo — three sentences, three games and a film](teardowns/fable5.2demo.md) | 三句话需求做成三个游戏加一部短片；每个项目都带报告，写明实现、验证方式和'做了假的地方'。 | yes | 未公布 · 未公布 | 0 |
| 3D 世界与数据 | [Portals — 471 agent-built worlds in one endless flight](teardowns/ai-portals.md) | 人类只写了一段话；一个主管 agent、28 个世界构建小组和评审 agent 写出 140 万行代码并发布了每个版本。 | no | 未公布 · 204 worlds in first 20 hours; 10 days to s8f release | 132 |
| 3D 世界与数据 | [EARTH: The Whole Story — a verified 13.8-billion-year globe](teardowns/earth-whole-story.md) | 构建会拒绝任何没有取回来源的条目——一套验证优先的数据工程，撑起 6.7 万个事件的地球史。 | yes | 未公布 · 未公布 | 7 |
| 影视与动画 | [BLACKOUT — a 79-second anime short, all code](teardowns/blackout.md) | 一份制作契约、并行 agent 部门和渲染 pass 链把 three.js 变成赛璐璐动画，还有自动化连贯性 QA。 | no | 未公布 · 未公布 | 7 |
| 影视与动画 | [Blender Effort Test — same scenes at medium vs max effort](teardowns/blender-effort-test.md) | 三个 Blender 场景各建两遍：快速版 vs 满血版（并告知第一版的错处）——一次干净的努力档位对照实验。 | no | published on the live page · 未公布 | 2 |
| 影视与动画 | [Ballpoint — macro pen footage with zero footage](teardowns/ballpoint.md) | 22 秒微距镜头：手写动力学、纤维素纤维、墨水各是一个独立脚本——'这不是视频模型'的证明方式。 | no | 未公布 · ~4 h render on RTX 4060 laptop (660 frames) | 1 |
| 系统与引擎 | [Sumi OS — a bootable desktop OS in 96 minutes](teardowns/sumi-os.md) | 空文件夹加一份任务书，运行前先定好检查项；代码原样发布并附 SHA-256——严肃的实验记录学。 | yes | 未公布 · 96 min across 3 sessions | 2 |
| 系统与引擎 | [fable-five — black hole, C compiler, GPT, physics, SQL, zero-dep](teardowns/fable-five.md) | 五个零依赖项目：每个都配一个把最难部分对到解析解/数值基准上的测试——'酷'变成'对'。 | no | 未公布 · one Claude Code session | 1 |
| 方法与基准 | [Claude Fable 5.2 HTML Files — a gallery that verifies itself](teardowns/html-files-gallery.md) | 76 个视觉研究及其提示词；截图只在内容哈希变化时重新生成，部署门禁失败即阻断——画廊也能工程化。 | no | 未公布 · 未公布 | 68 |
| 方法与基准 | [fable-5-2-benchmark — ten single-message jobs, fully instrumented](teardowns/fable-5-2-benchmark.md) | 十个领域、共同提示词加两三行任务、全程零干预；模型自己写的交付说明原文发布——一套可抄的评测协议。 | yes | $278.26 total across 10 jobs (measured) · 23 h 41 min total | 1 |
| 工具 | [nativeprompt — rewriting prompts per model, by the vendor's rules](teardowns/nativeprompt.md) | 同一句话在 Claude 无害、在 GPT-5.x 有害——按官方规则改写提示词，并审计 CLAUDE.md 里写给旧模型的行。 | no | free, offline, no API keys | 128 |
| 工具 | [oh-my-fable — vendor prompting guides as a Claude Code plugin](teardowns/oh-my-fable.md) | 把 Anthropic 官方提示词指南变成每个会话自动注入的工作规则——'文档跟着会话走'的模式。 | no | free, local | 61 |
<!-- catalog:end -->

## 实战手册

从项目里提炼的跨领域经验，每篇都有证据链接和检查清单：

- [单文件单发演示](playbooks/one-shot-single-file.md) —— 让“一句话 → 能玩的东西”成立的五个约束
- [共享契约的并行 agent 团队](playbooks/parallel-agent-teams.md) —— 文件所有权、一张地图、一个时钟、评审与发布门禁
- [让 agent 自查产出](playbooks/self-checking-agents.md) —— 从加载检查到浏览器感知闭环
- [经济学：缓存、预算与公开账单](playbooks/cache-and-cost-control.md)
- [验证优先的内容与诚实的产物](playbooks/verification-first-content.md)
- [Fable 5.2 的 effort、早停与指令卫生](playbooks/effort-and-early-stopping.md) —— 依据 Anthropic 官方指南浓缩

## 提示词模板

填空即用的原创模板（本仓库撰写，非任何创作者提示词的抄录；正文为英文，便于直接投喂）：

- [单文件游戏 / 互动演示](prompts/single-file-game.md)
- [纯代码 3D 世界或场景](prompts/threejs-world.md)
- [用 Python 驱动 Blender 建景](prompts/blender-scene-script.md)
- [并行团队契约](prompts/parallel-team-contract.md)
- [自检循环（系统提示词块）](prompts/self-verify-loop.md)

## 每篇拆解的结构

[`teardowns/`](teardowns/) 下每篇都遵循同一骨架，方便速览也方便精读：**它是什么 → 怎么做的 → 花了多少 → 如何复现 → 可以带走什么 → 来源**。每个文件的 frontmatter（分类、技术栈、是否单发、成本、耗时、星标快照）由 `scripts/build_catalog.py` 汇总生成本页目录表——改完内容跑一次脚本即可，CI 会校验目录不漂移。

## 口径与免责

- 拆解基于公开材料（项目 README、帖子）做摘要与分析；引用的数字归其作者所有，并标注为“作者自述”。
- 只链接原始来源，不复刻创作者的媒体文件或完整提示词；本仓库的提示词模板均为原创。
- 可用性、定价与模型行为都会变化，请以链接来源的最新信息为准。

## 参与贡献

发现了过程记录完善的 Claude 项目想补充拆解？或需要勘误？见 [CONTRIBUTING.md](CONTRIBUTING.md)——新条目需要可访问的产物、可描述的过程，以及数字的来源。

## 许可

本仓库原创文本采用 [CC BY 4.0](LICENSE)。被链接项目保留其各自许可；本目录不重新授权任何第三方内容。
