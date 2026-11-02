# Official Engineering Source Queue

Protocol: [`ops/official-engineering-learning.md`](../../ops/official-engineering-learning.md)

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
| OE-011 | Anthropic | *Multiagent orchestration* | <https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration> | 2026-10-09（官方 release notes 首次列出 dynamic workflows）；版本 `multiagent_20261001` | Multi-Agent; Agent / Workflow; Harness / Runtime; Evaluation / Security | 文档标题、正文、动态 workflows / subagents / advisor 的配置与限制已核验；发布日期依据官方 2026-10-09 release notes，文档页未暴露独立发布日期 | P1 | AI_ANALYZED | **NEWLY_PUBLISHED**：把多 Agent 协作拆成持久 subagent thread、后台 dynamic workflow run 与一次性 advisor consultation，并明确上下文隔离、线程生命周期、代理版本 pinning、MCP / sandbox 继承和 session budget 边界；相对 OE-001、OE-005 增加了平台化编排与治理约束。候选关联 T-001 / T-002 / RP-006，但不把 `multiagent` 当成稳定架构层 |

| OE-010 | Anthropic | *Redesigning source control at Anthropic* | <https://www.anthropic.com/engineering/redesigning-source-control> | 2026-10-13；更新 2026-10-15 | Harness / Runtime; Agent / Workflow; Evaluation / Security | 页面标题、正文、Published 与 Updated 已核验；官方索引列为最新工程文章 | P1 | AI_ANALYZED | **NEWLY_PUBLISHED**：以 agent-scale monorepo 为背景，说明在线客户端、server-side source control APIs、稀疏/虚拟 checkout、无锁增量 changeset、分层缓存、语义审查和可观测性如何共同降低 agent/job 基础设施瓶颈；候选关联 T-003 / RP-006 / T-002，但 Scion 明确只适合极大规模场景，不能直接当企业通用架构 |

## Verified watch candidates (2026-11-02)

OE-012–OE-015 已由此前未合并的学习分支使用，本轮保留编号，不复用、不将旧发现当作本轮新增。本轮从最新 `origin/main` 单独登记以下三篇；推荐不等于人类 `SELECTED`。

| ID | Publisher | Verified title | Official URL | Published / version | Axes | Source verification / last checked | AI priority | Status | Why now / candidate bridge |
|---|---|---|---|---|---|---|---|---|---|
| OE-016 | Anthropic | *Demystifying evals for AI agents* | <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents> | 2026-01-09；页面 modified 元数据 2026-10-18（没有内容差异基线，不认定实质更新） | Agent Evaluation; Agent / Workflow; Harness / Runtime | 2026-11-02：标题、完整正文、作者、`article:published_time` / `article:modified_time` 已核验 | P1 | AI_ANALYZED | **FOUNDATIONAL**：相对既有工具、隔离和编排资料，新增 task / trial / transcript / outcome、混合 grader、独立环境和重复试验的评估机制。适合先建立业务状态验收语言；精读至能区分最终状态与完成声明、pass@k 与 pass^k，以及模型失败与评估失败即可停止。candidate：RP-002-02 / H-RP002-06 的两路线比较如何排除 grader 与环境混淆；不证明独立 Action Runtime 必需 |
| OE-017 | Anthropic | *Quantifying infrastructure noise in agentic coding evals* | <https://www.anthropic.com/engineering/infrastructure-noise> | 2026-02-05；页面 modified 元数据 2026-10-18（没有内容差异基线，不认定实质更新） | Agent Evaluation; Harness / Runtime | 2026-11-02：官方标题、正文、`article:published_time` / `article:modified_time` 已核验 | P2 | AI_ANALYZED | **FOUNDATIONAL**：相对 OE-016，新增 CPU / RAM 保底与硬上限、OOM、资源余量影响可用解法的实验变量；短读实验设计和限制，停止于能解释为何增加资源既可能修复基础设施，也可能改变测试难度。candidate：比较通用 API + Policy 与显式契约时，固定执行预算并单列基础设施失败；原文倍率不是企业推荐值 |
| OE-018 | OpenAI | *Testing Agent Skills Systematically with Evals* | <https://developers.openai.com/blog/eval-skills> | 2026-01-22（页面可见日期）；未列独立更新日期 / 版本 | Skills; Agent Evaluation; Tool Calling | 2026-11-02：官方标题、可见完整日期和正文已核验 | P2 | AI_ANALYZED | **FOUNDATIONAL**：相对 OE-016，新增 skill 显式 / 隐式 / 情境触发和负例，以及 trace + artifacts + deterministic checks + structured rubric 的小型闭环；短读触发集和评分设计即可，代码与 CLI 参数按实施时文档复核。它检验约定步骤，不意味着任意业务任务都应锁死工具序列；本轮不新增研究桥接 |

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

## Latest watch (2026-11-02)

- 范围：核验 Anthropic Engineering 索引、Claude Platform release notes、OpenAI Developers Blog 索引与 OpenAI `Evaluate agent workflows` 指南。OpenAI `openai.com/news/engineering/` 本轮 TLS EOF，未取得正文，不能据此声称所有官方来源都没有新文。Claude release notes 已读至 2026-10-30，最近的 fast mode 弃用、成本 API 与请求大小变更不作为本轮架构精读。
- 分类：本轮新增 `FOUNDATIONAL` 3 篇；在成功读取的范围内，未选出值得新增的 `NEWLY_PUBLISHED`；未核验出有实质内容差异的 `UPDATED`。OE-016 / OE-017 的相同修改日期可能来自站点维护，不能据元数据判断机制更新。此前分支已登记的 OE-012–OE-015 不重复计入本轮。
- 排序（1–5；前四项越高越有价值，Learning Cost 越高越费力；Novelty 只相对队列，不推断人已掌握）：

  | Candidate | Relevance | Mechanism Depth | Architecture Value | Novelty | Learning Cost | Recommendation |
  |---|---|---|---|---|---|---|
  | OE-016 | 5 | 5 | 5 | 5 | 3 | 唯一主推荐；约 40–50 分钟精读与自测 |
  | OE-017 | 5 | 4 | 5 | 4 | 2 | 可选；约 10–15 分钟读实验变量与限制 |
  | OE-018 | 4 | 4 | 4 | 4 | 2 | 可选；约 10–15 分钟读触发集与评分设计 |

- `SOURCE_CLAIM`（OE-016）：评估需要持续维护，并与生产监控、用户反馈及人工校准结合。文中客户案例和 benchmark 数值是厂商报告，不是独立验证的企业成效。
- `SOURCE_MECHANISM`（OE-016）：task 定义输入及成功标准，每次 trial 从干净环境运行；记录 transcript 并检查 outcome；按维度组合代码、模型和人工 grader；多次试验区分至少一次成功的 pass@k 与全部成功的 pass^k；区分能力集与回归集，并检查评分器是否拒绝有效解法。
- `AI_EXPLANATION`：模型、agent harness、资源预算、测试环境和 grader 一起决定分数；完成声明、合法执行和业务提交结果要分别验证。只锁定工具调用顺序会误伤等价解法，但必要授权约束仍需检查。
- candidate Research Bridge（`RESEARCH_INFERENCE`）：OE-016 / OE-017 → T-002 / RP-002-02 / H-RP002-06。它们补充现有两路线比较的判别方法，并收窄“成功率更高就支持显式契约”的推断；不能据文章判定该假设成立。待验证：固定模型、任务、执行预算和初态后，显式契约相对 Domain API + Policy 是否仍改善授权正确性、幂等和最终状态一致性，且收益覆盖维护成本？公开验证方向为合成退款系统的两种公开实现，注入重复提交、权限撤销、并发和部分失败；由外部数据库断言、权限日志和故障分类共同评分。此处不创建实验、Problem、Hypothesis 或 Evidence。
- 暂不推荐：OE-010 / OE-011 已有机制覆盖；OE-006 日期仍待核验，保持 `NEEDS_REVIEW`；OpenAI `Evaluate agent workflows` 指南正文可读但没有稳定发表 / 更新日期或独立版本，本轮只作来源比较，不新增已核验候选。偏产品发布、定价和限额消息没有足够机制增量。没有因“太难”而排除本轮三篇，也没有假定研究者已理解旧资料。
- 候选池：新增 3 条 `AI_ANALYZED`；当前分支累计 14 条，`NEEDS_REVIEW` 1 条（OE-006）；未改变既有条目状态。推荐不等于 `SELECTED`；`HUMAN_TAKEAWAY` 等待研究者回答自测并确认。未创建知识卡，未写入正式研究状态或 Evidence Ledger。
- 下一步：先用自己的话解释 outcome / transcript、pass@k / pass^k、干净环境与 grader 校准；再判断是否值得把候选桥接交人工研究讨论，不自动交 Research Runner。


