# Official Engineering Source Queue

Protocol: [`ops/official-engineering-learning.md`](../../ops/official-engineering-learning.md)
Updated: 2026-10-19
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

## Latest watch (2026-10-19)

- 本轮状态：发现 `NEWLY_PUBLISHED` 1 篇（OE-011；官方 release notes 于 2026-10-09 列出 dynamic workflows，文档版本为 `multiagent_20261001`）；未核验到 2026-10-16 之后新的 Anthropic 工程文章。官方文档另有 2026-10-14 的 OpenTelemetry export 更新，但主要是可观测性功能发布，暂不作为主推荐新增条目。OpenAI 官方页面仍无法稳定访问，OE-006 继续保留 `NEEDS_REVIEW`。
- 本周最值得学习的问题：当一个 Agent 可以把任务交给持久子 Agent、后台 workflow 或 advisor 时，编排方式如何改变上下文隔离、状态生命周期、权限继承、成本上限和结果可观测性？
- 推荐精读：OE-011《Multiagent orchestration》；来源 Anthropic Claude Platform Docs；URL <https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration>；2026-10-09 release note、版本 `multiagent_20261001`；`NEWLY_PUBLISHED`。它值得学习，因为现有队列已有多 Agent 研究系统与长运行 Harness 的工程文章，但缺少一个官方平台文档对 subagent、dynamic workflow 和 advisor 三种控制流的明确边界。
- Part A｜原文问题与作者结论：`SOURCE_CLAIM`：复杂工作可由多个 Agent 在各自隔离上下文中并行完成；平台提供 subagents、dynamic workflows 和 advisor 三种协作方式，使用哪一种由任务形态与系统配置决定。`SOURCE_CLAIM`：workflow 适合多片段、并行或长任务，但每个 Agent 都消耗 tokens，应配置 session budget；subagent thread 可持续跟进，workflow run 的线程在运行结束时归档，advisor 只服务主线程。作者没有证明多 Agent 在一般企业流程中必然优于单 Agent，也没有解决跨组织身份、跨系统事务一致性和结果责任归属。
- Part B｜核心技术机制：`SOURCE_MECHANISM`：subagents 由主 Agent 委派到独立 session thread，线程保留历史并可被后续消息跟进；dynamic workflows 由 Agent 写出分阶段程序，服务端在后台并行运行多个 Agent，结果通过 workflow events 回到 session stream；advisor 是平台生成的临时线程，在主线程关键时刻提供建议。`SOURCE_MECHANISM`：Agent 配置可列出预定义或 inline agents，并通过 `multiagent_20261001`、`workflows`、`subagents`、`advisor` 开关控制能力；MCP server 按 Agent 定义隔离，vault credential 按 session 作用于所有线程，环境 `allowed_hosts` 与 session budget 约束整个运行。`AI_EXPLANATION`：关键区别不是“有几个模型”，而是工作是否需要可回访的对话状态、可编排的批处理程序或一次性的判断输入；三者对应不同的状态持久性与控制权。
- Part C｜架构变量、边界和替代方案：有效条件包括任务可拆分、子任务边界清晰、共享 sandbox 足够、事件流可观测、预算可封顶且允许并行；失败条件包括强事务顺序、共享状态冲突、跨线程权限过宽、工作流失败语义不清和模型自行决定启动 run 造成不可预测成本。成本与维护变量包括 token 预算、线程归档、代理版本 pinning、MCP / vault 继承、区域与模型兼容性以及一层委派限制。替代方案包括单 Agent 顺序工具调用、应用层固定 DAG、外部队列 / durable workflow 或人工审批。`RESEARCH_INFERENCE`：持久线程、后台 run 和 advisor 的差异可能是结构性控制流约束；`multiagent` 这个厂商配置名本身更像当前 API 的组合入口，不足以证明企业需要独立 Multi-Agent Layer。
- Part D｜企业架构候选映射：`RESEARCH_INFERENCE`：subagent thread 可映射到 Agent / Context 的隔离执行单元，dynamic workflow 可映射到 Workflow / Harness 的后台编排，advisor 可映射到受限的审查或升级动作；session budget、permission policy、MCP server scope、vault 和 environment networking 可作为 Governance / Runtime 变量。未知量是这些边界能否跨企业身份、审批和持久业务状态稳定复用；文档不能推出跨 Agent 的业务 Action 契约或企业责任归属。
- Part E｜Human Learning Packet：前置知识为 session / thread、事件流、DAG 或 workflow、权限与 token budget。研究者应能用自己的话解释：①为什么“subagent follow-up”与“dynamic workflow run”在状态持久性和主线程控制权上不同；②为什么 vault 是 session-scoped 而 MCP server 是 agent-scoped，这会如何影响最小权限；③为什么让 Agent 自行决定何时启动 workflow 仍需要预算、失败报告和人工约束。自测：a) 合同审查中 3 份与 300 份文件分别选哪种控制流，为什么？b) 一个 workflow 子 Agent 读到了不该读的 MCP 数据，配置边界在哪一层修复？c) 如果一个子 Agent 失败但其他阶段成功，业务系统应如何表达“部分覆盖”而不是伪装成完整成功？只有研究者回答并记录 `HUMAN_TAKEAWAY` 后才能推进状态。
- Part F｜候选 Research Bridge：`RESEARCH_INFERENCE`：OE-011 可能补充 RP-006 关于 Harness / Runtime 的控制流变量，并挑战把 Multi-Agent 仅理解为并行调用的假设；它也可能为 T-001 / T-002 提供 Context 隔离与能力授权的候选边界。待验证问题：在公开企业 Agent 案例中，哪些任务变量决定采用持久线程、后台 DAG 还是单 Agent 顺序执行？公开验证方向：对照 Anthropic dynamic workflows 文档、OpenAI agent orchestration 指南、Temporal / Durable Functions 等公开 workflow 资料，比较失败恢复、权限继承、预算和审计语义；该桥接仅候选，不写入 Evidence Ledger。
- 可选参考资料：OE-010《Redesigning source control at Anthropic》—短读其在线 client / server API、缓存和故障域，观察 Agent 规模如何改变基础设施约束；OE-009《Introducing advanced tool use on the Claude Developer Platform》—短读工具发现与程序化调用，比较“工具编排”与“多 Agent 编排”的上下文和权限成本。两篇都不改变本轮主推荐。
- 暂不推荐资料及原因：OE-006 OpenAI《Harness engineering》仍无法稳定核验官方日期，继续 `NEEDS_REVIEW`；OpenTelemetry export 主要是可观测性能力更新，增量不足以支撑本轮完整 A–F 主推荐；已有 OE-001、OE-005 与本条目在 Agent / Harness 主题相邻，避免重复升级为多篇主推荐。
- 候选池变化：新增 OE-011；未改变既有条目状态，未创建知识卡，未标记 `SELECTED`、`READING`、`HUMAN_UNDERSTOOD` 或 `APPLIED`。本轮不修改任何正式研究状态。
- 下一步学习建议：先由研究者决定是否选择 OE-011 进入 `SELECTED`，阅读时画出 primary thread → subagent thread / workflow run / advisor 的状态流，并把权限、预算、失败和归档语义分别标注；完成 Part E 后再判断是否把候选 Research Bridge 交给原研究线评估。
