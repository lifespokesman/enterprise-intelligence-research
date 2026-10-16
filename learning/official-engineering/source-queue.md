# Official Engineering Source Queue

Protocol: [`ops/official-engineering-learning.md`](../../ops/official-engineering-learning.md)
Updated: 2026-10-16
Queue status: pilot; no item is marked `HUMAN_UNDERSTOOD` or `APPLIED`.

> 本表是官方工程资料候选入口，不是论文 Evidence Index。日期和标题只在来源核验后登记；无法稳定取得日期的资料明确保留 `NEEDS_REVIEW`。

## Status legend

`DISCOVERED` = 发现但尚未完成 AI 分析；`AI_ANALYZED` = 已核验并完成机器侧价值分析；`SELECTED` / `READING` / `HUMAN_UNDERSTOOD` / `APPLIED` = 需要研究者推进；`NEEDS_REVIEW` = 来源、日期、解释或确认存在问题；`ARCHIVED` = 已去重、低增量或已被其他卡片覆盖。

## Queue

| ID | Publisher | Verified title | Official URL | Published / version | Axes | Source verification | AI priority | Status | Why now / candidate bridge |
|---|---|---|---|---|---|---|---|---|---|
| OE-001 | Anthropic | *Building Effective AI Agents* | <https://www.anthropic.com/engineering/building-effective-agents> | 2024-12-19 | Agent / Workflow; Tool Calling | 页面标题、正文与 `datePublished` 已核验；页面提示部分工具 landscape 已变化 | P1 | AI_ANALYZED | 恢复 workflow 与 agent 的机制边界，以及“先用最简单可组合方案”的适用条件；可候选关联 RP-006 / RP-002，但不能把厂商经验直接升级为原则 |
| OE-002 | OpenAI | *A practical guide to building agents* | <https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf> | 2025-04-07（PDF CreationDate；页面发布日期未单列） | Agent / Workflow; Evaluation / Security | PDF 可访问；首页标题和目录已核验；日期来自文件元数据，需在后续页面核验时保持该说明 | P1 | AI_ANALYZED | 提供 agent 定义、何时构建、设计基础和 guardrails 的官方指南；适合与 OE-001 对读，Research Bridge 仅作为候选 |
| OE-003 | Anthropic | *Effective context engineering for AI agents* | <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents> | 2025-09-29 | Prompt / Context | 页面标题、正文与 `datePublished` 已核验 | P1 | AI_ANALYZED | 直接补充 Context 的有限性、动态整理和 context rot；候选关联 T-001 / RP-002-04；先完成人类机制理解再决定是否进入研究 |
| OE-004 | Anthropic | *Writing effective tools for AI agents—using AI agents* | <https://www.anthropic.com/engineering/writing-tools-for-agents> | 2025-09-11 | Tool Calling; Evaluation / Security | 页面标题、正文与 `datePublished` 已核验；页面显示标题短版为 “Writing effective tools for agents — with agents” | P1 | AI_ANALYZED | 解释面向非确定性 Agent 的工具契约、返回上下文、token 效率和评估；候选关联 T-002 / RP-002-02 |
| OE-005 | Anthropic | *Scaling Managed Agents: Decoupling the brain from the hands* | <https://www.anthropic.com/engineering/managed-agents> | 2026-04-08 | Harness / Runtime; Agent / Workflow | 页面标题、正文与 `datePublished` 已核验 | P1 | AI_ANALYZED | 提供 session / harness / sandbox 的解耦和稳定接口视角；可挑战“harness 是固定实现”的假设，候选关联 RP-006 |
| OE-006 | OpenAI | *Harness engineering: leveraging Codex in an agent-first world* | <https://openai.com/index/harness-engineering/> | 待官方页面日期复核 | Harness / Runtime; Skills; Evaluation / Security | 标题和正文可由官方页面读取；当前网络路径未稳定取得发布日期，禁止凭记忆补日期 | P1 | NEEDS_REVIEW | 文章涉及 repository knowledge、progressive disclosure、可执行约束和反馈回路；待日期核验后再进入 AI_ANALYZED / SELECTED |
| OE-007 | Anthropic | *How we contain Claude across products* | <https://www.anthropic.com/engineering/how-we-contain-claude> | 2026-05-25；更新 2026-06-06 | Agent / Workflow; Evaluation / Security; Harness / Runtime | 页面标题、正文、`article:published_time` 与 `article:modified_time` 已核验 | P1 | AI_ANALYZED | **FOUNDATIONAL**：按产品能力与用户信任边界选择 ephemeral container、HITL sandbox 或 sealed VM；补充 egress、未信任配置、工具返回和持久记忆的攻击面。候选关联 T-002 / RP-002-02；建议精读至三种隔离模式与失败案例，停止于能说明“边界在哪里、谁承担监督” |
| OE-008 | Anthropic | *Harness design for long-running application development* | <https://www.anthropic.com/engineering/harness-design-long-running-apps> | 2026-03-24；更新 2026-03-24 | Harness / Runtime; Agent / Workflow | 页面标题、正文、`article:published_time` 与 `article:modified_time` 已核验 | P1 | AI_ANALYZED | **FOUNDATIONAL**：补充长运行 Agent 的状态恢复、任务切片与反馈回路设计；相对 OE-005 聚焦应用开发 harness 的持久化和可恢复性。候选关联 RP-006；建议短读架构变量，停止于能列出恢复与维护成本 |
| OE-009 | Anthropic | *Introducing advanced tool use on the Claude Developer Platform* | <https://www.anthropic.com/engineering/advanced-tool-use> | 2025-11-24；更新 2026-03-16 | Tool Calling; Context; Evaluation / Security | 页面标题、正文、`article:published_time` 与 `article:modified_time` 已核验 | P2 | AI_ANALYZED | **UPDATED**：围绕 tool search、programmatic tool calling 与 tool use examples 讨论工具发现、上下文预算和调用编排；与 OE-004 有重叠，保留作可选对照。候选关联 T-002；建议只读机制图和限制，停止于能比较“工具契约”与“工具发现/编排” |

| OE-010 | Anthropic | *Redesigning source control at Anthropic* | <https://www.anthropic.com/engineering/redesigning-source-control> | 2026-10-13；更新 2026-10-15 | Harness / Runtime; Agent / Workflow; Evaluation / Security | 页面标题、正文、Published 与 Updated 已核验；官方索引列为最新工程文章 | P1 | AI_ANALYZED | **NEWLY_PUBLISHED**：以 agent-scale monorepo 为背景，说明在线客户端、server-side source control APIs、稀疏/虚拟 checkout、无锁增量 changeset、分层缓存、语义审查和可观测性如何共同降低 agent/job 基础设施瓶颈；候选关联 T-003 / RP-006 / T-002，但 Scion 明确只适合极大规模场景，不能直接当企业通用架构 |

## Reading recommendation

建议先由研究者选择一组最小对读：`OE-001 → OE-003 → OE-004`，分别理解 agent/workflow、context 和 tool 机制。`OE-002` 作为 OpenAI 的设计指南对照，`OE-005` / `OE-006` 在需要 Harness / Runtime 时再读。推荐不等于 `SELECTED`；研究者需在一次会话中明确选择，并按协议完成 Part E。

## Candidate Research Bridges

以下只是待人工判断的映射，不是 Evidence：

- OE-003 → T-001 / RP-002-04：Context 的动态组装、有限注意力与任务相关性是否补充现有 Task Context 假设？
- OE-004 → T-002 / RP-002-02：面向 Agent 的 tool contract、schema、权限和评估是否提供 Governed Capability Contract 的候选机制或反例？
- OE-005 → RP-006：Session / Harness / Sandbox 的接口解耦是否挑战固定 Harness / Runtime 边界？
- OE-001 / OE-002 → RP-006：Workflow 与 Agent 的适用条件是否能形成可验证的选择变量？
- OE-007 → T-002 / RP-002-02：按用户类型与能力边界选择容器、HITL sandbox 或 VM，是否能补充 Governed Capability 的责任与隔离变量？
- OE-008 → RP-006：长运行应用的恢复、持久状态与反馈回路，是否要求把 Harness 视为可恢复控制系统而非单一提示模板？
- OE-009 → T-002：工具发现与程序化调用对 token 成本、权限边界和可观测性的影响，是否挑战仅以 schema 定义 Governed Capability 的做法？

只有当研究者完成 Part E、指出具体假设影响并提出公开验证方式时，才可将某一桥接候选提交给原有 Research Runner 评估。不得自动创建 Evidence Card。

## Queue maintenance

- 定期任务只更新本表；发现没有实质增量时写 `NO_MATERIAL_UPDATE`，不添加重复条目。
- 同一机制的新版本优先更新现有 ID 的来源核验和版本字段；除非内容发生实质分叉，不新建 ID。
- 被选中的条目由研究者在本表更新为 `SELECTED`，开始阅读时更新为 `READING`；状态变化应在同一 PR 中说明人类动作。
- 人类确认后的知识卡链接写回该行；自动任务不得创建链接指向的卡片。

## Latest watch (2026-10-12)

- 本轮状态：`FOUNDATIONAL` 2 篇（OE-007、OE-008）、`UPDATED` 1 篇（OE-009）；未核验到 2026-10-09 之后新发表且值得新增的资料。OpenAI 官方页面本轮 TLS 不稳定，OE-006 继续保留 `NEEDS_REVIEW`。
- 主推荐：OE-007。`SOURCE_CLAIM`：Agent 能力扩大时应通过限制可达环境来压缩 blast radius；`SOURCE_MECHANISM`：三种隔离模式分别把代码执行放入 ephemeral container、带 OS sandbox 的 HITL 环境或 sealed VM，并用文件系统边界、egress proxy、配置延迟解析和工具返回检查降低风险。`AI_EXPLANATION`：安全边界的关键不是“模型是否听话”，而是模型即使偏离也无法跨越的可达性。`RESEARCH_INFERENCE`：这为 T-002 / RP-002-02 提供责任主体、权限授予和审计边界的候选变量，尚非 Evidence。
- 学习自测：①为什么 claude.ai 的 server-side container 不能直接迁移给本地知识工作者？②“允许 api.anthropic.com”为什么仍可能造成数据外泄，代理如何修复？③项目启动前解析本地配置为何应被视为外部输入？前置知识为 sandbox / VM / egress、prompt injection 与 capability security；只有研究者回答并记录 HUMAN_TAKEAWAY 后才能推进状态。
- 暂不主推荐：OE-008 需要先理解 OE-005 的 session / harness / sandbox 解耦；OE-009 与 OE-004 的工具契约内容部分重叠，保留为短读对照。
- 候选池变化：新增 OE-007–OE-009；未修改既有条目状态，未创建知识卡，未标记 `HUMAN_UNDERSTOOD` 或 `APPLIED`。

## Latest watch (2026-10-16)

- 本轮状态：发现 `NEWLY_PUBLISHED` 1 篇（OE-010，2026-10-13 发布、2026-10-15 更新）；未核验到 OpenAI 官方可稳定访问的新资料，OE-006 继续保留 `NEEDS_REVIEW`。本轮没有新的 `FOUNDATIONAL` 或 `UPDATED` 条目。
- 本周最值得学习的问题：当 Agent 与自动化 Job 成为主要客户端、代码变更量持续放大时，哪些 source-control / CI / review 约束必须从“人类离线工作流”改成在线、可查询、可分层和可治理的运行机制？
- 推荐精读：OE-010《Redesigning source control at Anthropic》；来源 Anthropic Engineering；URL <https://www.anthropic.com/engineering/redesigning-source-control>；2026-10-13 发布，2026-10-15 更新；`NEWLY_PUBLISHED`。它值得学习，因为现有队列已有 Agent、Context、Tool、Sandbox 与长运行 Harness 的文章，但缺少“Agent 规模如何反过来重塑开发基础设施”的完整案例。
- Part A｜原文问题与作者结论：`SOURCE_CLAIM`：Anthropic 的 merge rate 从 2026 年 5 月约 2,500 次/日升至 9 月超过 30,000 次/日，面向人类规模的 source control、build 和 CI 成为瓶颈；作者因此在五个月内迁移到自研 Scion，并分享其 agent-scale 设计取舍。`SOURCE_CLAIM`：Scion 不适合一般组织或替代通用 Git，前提是极大 monorepo、数万工程师或大量 Agent，以及高内部 token / 基础设施预算。作者没有解决跨组织迁移成本、通用 Git 生态兼容和非代码业务 Agent 的状态治理问题。
- Part B｜核心技术机制：`SOURCE_MECHANISM`：客户端默认在线，服务器承担历史、diff、merge、rebase 等查询与写入；客户端保留有界对象缓存和按需工作副本。`SOURCE_MECHANISM`：changeset 作为写前日志记录相对父节点的变更，内容寻址 blob 与递归派生数据分别支持高吞吐提交、blame、路径历史和按需索引。`SOURCE_MECHANISM`：server / regional cache / node daemon 通过同一 RPC 层级化供给对象，稀疏或虚拟 checkout 只取实际需要的树和 blob，并用故障域隔离避免缓存故障冲击上游。`AI_EXPLANATION`：核心转变不是“把 Git 换成另一种产品”，而是把客户端从完整副本持有者变成可查询服务的轻量消费者，让 Agent 的并发、重复读取和自动化检查成本集中在可扩展服务端处理。
- Part C｜架构变量、边界和替代方案：有效条件包括在线客户端、高频并发变更、超大 monorepo、可接受的服务端依赖和成熟的派生索引；失败条件包括离线开发、较小仓库、强 Git 兼容要求、迁移后仍需维护整套 review / search / CI 生态。成本包括重建服务端、权限与审查模型、缓存拓扑、数据一致性和运维人才；替代方案包括 Git 的 sparse/shallow/promisor、镜像与 snapshot、或只把 server-side RPC 与稀疏访问能力增量加入现有平台。`RESEARCH_INFERENCE`：Scion 的 server/client asymmetry、分层缓存和语义审查可能是 agent-scale 的结构性约束，但自研 VCS 本身更像当前规模下的特化实现。
- Part D｜企业架构候选映射：`RESEARCH_INFERENCE`：可把 source-control service 视为 Agent / Workflow 的共享 Runtime 依赖，把稀疏上下文获取映射到 Context，把目录级权限与语义审批映射到 Governance，把 server-side API 与 changeset 视为可治理 Action / Capability 的候选边界。未知量是这些机制是否能迁移到普通企业规模，以及“代码变更”治理是否能代表一般 Business Action；不能由本文推出独立 Harness / Runtime 层已成立。
- Part E｜Human Learning Packet：前置知识为 Git 对象模型、monorepo checkout、缓存与一致性、代码审查 / CI，以及 Agent 并发工作流。研究者应能用自己的话解释：①为什么“客户端始终在线 + server-side API”能降低 Agent 的重复 checkout 成本；②changeset 与派生数据怎样同时支持高吞吐写入和 blame / history 查询；③为什么分层缓存和故障域比单纯增加机器更重要。自测：a) 一个 500 人、离线需求强、多个小仓库的企业是否应采用 Scion，为什么？b) 如果区域 cache 故障，哪一层应承压、哪些指标能证明隔离生效？c) 语义审批如何区分 comment-only 与敏感逻辑变更，错误分类会造成什么后果？只有研究者回答并记录 `HUMAN_TAKEAWAY` 后才能推进状态。
- Part F｜候选 Research Bridge：`RESEARCH_INFERENCE`：OE-010 可能补充或收窄 RP-006 关于 Harness / Runtime 的讨论：当 Agent 数量和变更吞吐成为主导变量时，Harness 可能需要把可查询状态、增量提交、审查语义和故障域作为系统约束，而不只是提示模板或会话循环。待验证问题：在公开的 agentic coding / monorepo 案例中，哪些吞吐、在线性、缓存命中和审查变量决定“增强现有 Git”与“重建 source-control service”的分界？公开验证方向：Google Piper / Meta Mononoke / Git partial-clone 文档与其他公开 agent-scale coding 案例的机制对比；该桥接仅候选，不写入 Evidence Ledger。
- 可选参考资料：OE-008《Harness design for long-running application development》—短读恢复、持久状态与反馈回路，帮助把 OE-010 的基础设施约束与应用级 Harness 对齐；OE-009《Introducing advanced tool use on the Claude Developer Platform》—短读工具发现、程序化调用与上下文成本，帮助比较“服务端可查询 API”与“工具调用编排”的边界。两篇都不改变本轮主推荐。
- 暂不推荐资料及原因：OE-006 OpenAI《Harness engineering》仍无法稳定核验官方日期，继续 `NEEDS_REVIEW`；OE-008 已在队列中且与本轮主题相邻，避免重复升级为主推荐；Anthropic 索引中与 source control、Claude Code 具体实现相关但不直接增加 Agent / Context / Tool / Runtime 机制的文章，本轮暂不新增。
- 候选池变化：新增 OE-010；未改变既有条目状态，未创建知识卡，未标记 `SELECTED`、`READING`、`HUMAN_UNDERSTOOD` 或 `APPLIED`。本轮不修改任何正式研究状态。
- 下一步学习建议：先由研究者决定是否选择 OE-010 进入 `SELECTED`，阅读时优先画出 client → server → cache → blob / derived-data 的状态流，再回答 Part E 三题；若能明确规模边界，再决定是否把候选 Research Bridge 交给原研究线评估。