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
| OE-012 | OpenAI | *Introducing the Agents API* | <https://openai.com/index/introducing-the-agents-api/> | 2026-09-10；公开 beta；页面未列独立更新时间 | Agent / Workflow; Context; Tool Calling; Harness / Runtime; Multi-Agent | 官方页面标题、正文与发布日期已核验；页面说明 public beta、Codex harness、hosted / BYO sandbox、context compaction、tool search、programmatic tool calling 与 multi-agent | P1 | AI_ANALYZED | **NEWLY_PUBLISHED**：把长会话 context compaction、按需 tool search、程序化并行调用、子代理上下文隔离、可替换 sandbox 与版本化 harness 作为同一运行接口；相对 OE-005、OE-011 增加了“托管 Harness 与执行环境分离”的 OpenAI 实现样本。候选关联 T-001 / T-002 / RP-006；应重点学习接口边界和失败成本，不能把产品 beta 能力直接当企业架构原则 |
| OE-013 | Anthropic | *OpenTelemetry export for Messages API and Claude Managed Agents* | <https://platform.claude.com/docs/en/release-notes/overview> | 2026-10-14；beta；Claude Platform release notes | 官方 release notes 标题、日期与正文已核验；SDK spans 覆盖 Python、TypeScript、C#、Go、Java、PHP、Ruby，API traces 需在 Console 配置 destination | P2 | AI_ANALYZED | **NEWLY_PUBLISHED**：补充 Agent / API 可观测性的具体出口，把 SDK spans 与 Managed Agents session traces 接入外部 observability；相对 OE-008、OE-011 增加运行时追踪与审计可见性的工程变量。候选关联 T-002 / RP-006；短读即可，停止于能说明 trace 边界、成本和无法由 tracing 单独证明的业务效果 |
| OE-014 | OpenAI | *Securing our frontier model training environment* | <https://openai.com/index/securing-our-frontier-model-training-environment/> | 2026-10-23；页面发布日期已核验 | Agent Security; Harness / Runtime; Evaluation / Security | 官方页面标题、正文与发布日期已核验；文章描述训练环境的隔离、离线运行、纵深防御和高算力 red-team 机制 | P1 | AI_ANALYZED | **NEWLY_PUBLISHED**：把高能力模型训练环境的安全问题拆成隔离边界、最小网络出口、分层监控和主动攻击测试；相对 OE-007 增加训练阶段、内部威胁和高算力自主行为的机制变量。候选关联 T-002 / RP-006；建议精读至能解释“隔离、监控、测试”如何互相补位，停止于能指出其不等同于企业 Agent 运行时安全 |
| OE-015 | OpenAI | *How we detect and prevent frontier model misalignment* | <https://openai.com/index/how-we-detect-and-prevent-frontier-model-misalignment/> | 2026-10-28；页面发布日期已核验 | Model / Reasoning; Agent Security; Evaluation / Security | 官方页面标题、正文与发布日期已核验；文章描述对抗性评估、持续监控、行为信号和分层缓解 | P2 | AI_ANALYZED | **NEWLY_PUBLISHED**：补充从模型行为信号到部署前后监控和缓解的安全闭环；相对 OE-014 更聚焦 misalignment 检测与响应，而非训练环境隔离。候选关联 T-002 / RP-006；建议短读机制与限制，停止于能区分行为检测、能力评估和企业责任审计 |

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

## Latest watch (2026-10-28)

- 本轮状态：新增 **NEWLY_PUBLISHED** 2 篇（OE-012、OE-013）；未发现需要更新的既有条目。Anthropic 2026-10-13 的 source control 文章已在 OE-010，2026-10-09 的 dynamic workflows 已在 OE-011，本轮不重复登记。
- 主推荐：**OE-012**。`SOURCE_CLAIM`：OpenAI 将 Codex harness 及其基础设施以 Agents API public beta 提供给开发者，并允许选择 OpenAI-hosted、自己的基础设施或合作方 sandbox。`SOURCE_MECHANISM`：session 接近上下文上限时自动 compaction；tool search 按需加载工具定义；programmatic tool calling 在代码中并行、串联和过滤调用；multi-agent 子代理拥有独立上下文；Harness 与 sandbox 可替换并按模型发布版本演进。`AI_EXPLANATION`：文章把“模型循环”和“执行环境”拆成两个可替换接口，降低单次上下文窗口和工具定义规模对长任务的限制，但也把恢复、预算、权限和跨环境一致性变成系统责任。`RESEARCH_INFERENCE`：这为 T-001 / T-002 / RP-006 提供“Context 管理、协调 Harness、执行 Sandbox、Governance 边界”之间的候选变量，尚非 Evidence。
- 学习自测：①为什么 compaction 能延长会话，却不能保证关键状态完整保留？②tool search 与 programmatic tool calling 分别减少哪一种成本，何时会增加可观测性负担？③将 Harness 与 sandbox 分离后，谁应承担文件、秘密、网络和恢复状态的一致性？前置知识为 context window / summarization、MCP 或 tool schema、sandbox / capability boundary、异步工作流与预算；读完后研究者应能用自己的话画出 session → tool discovery → subagent → sandbox 的状态流，并指出至少两个失败边界。
- 可选参考：**OE-013** 短读 OpenTelemetry export，理解 traces 如何暴露 API 请求与 Managed Agents session 的运行路径；它适合在需要补 observability 时阅读，不足以单独证明 Agent 质量或企业结果。**OE-011** 作为对照阅读，比较 OpenAI 的托管 Harness / 可替换 sandbox 与 Anthropic 的 subagent thread / dynamic workflow / advisor 三种编排形态。
- 暂不推荐：OE-010 已覆盖本轮发现的 Anthropic source-control 主题；OE-009 与 OE-004 在工具契约和工具编排上存在重叠，继续作为短读对照；OE-006 仍缺稳定官方日期，保持 `NEEDS_REVIEW`。
- 候选池变化：新增 OE-012、OE-013；未创建知识卡，未标记 `SELECTED`、`READING`、`HUMAN_UNDERSTOOD` 或 `APPLIED`。候选 Research Bridge 仅写入本队列，未写入 Evidence Ledger。



## Latest watch (2026-10-30)

- 本轮状态：新增 **NEWLY_PUBLISHED** 2 篇（OE-014、OE-015）；未发现既有条目需要更新。OE-010、OE-011 已覆盖 Anthropic 近期 source control 与 dynamic workflows，未重复登记。
- 本周最值得学习的问题：当模型能力、训练算力和自主行为上升时，安全边界应由哪些可验证的隔离、监控和主动测试机制共同承担？
- 主推荐：**OE-014**。推荐理由是它把安全机制放在训练环境这一高能力、高权限场景中讨论，能补足 OE-007 面向产品隔离的视角；它也提供了把“模型是否听话”转成“模型即使偏离也能否跨越边界”的工程学习入口。
  - **Part A｜Source Understanding**：`SOURCE_CLAIM`：OpenAI 将 frontier model training environment 视为需要分层保护的高价值目标，并通过隔离、限制网络可达性、监控和主动测试降低失控风险。作者原始问题是：训练中的高能力模型若出现恶意或未预期行为，如何阻止其获得持续外部影响能力。文章没有证明这些措施足以解决所有 misalignment，也没有给出企业业务系统的完整治理模型。
  - **Part B｜Mechanism Reconstruction**：`SOURCE_MECHANISM`：把训练环境放入受限执行边界，减少不必要的网络与凭据可达性；用多层检测和日志观察异常行为；用高算力 red-team / 对抗性测试主动寻找越界路径；在发现信号后通过分级响应、暂停或收紧权限降低影响。`AI_EXPLANATION`：隔离压缩 blast radius，监控提高发现概率，主动测试暴露监控覆盖不到的路径，三者分别解决“能否到达、是否看见、是否提前试出”的问题。
  - **Part C｜Architecture Variables**：关键变量包括网络出口是否默认拒绝、秘密和配置是否延迟注入、监控是否能观察到模型与工具的真实交互、red-team 是否覆盖长时程和协同行为、暂停与恢复由谁执行，以及隔离带来的训练效率和可观测性成本。结构性约束可能是可达性边界和独立的停止权；具体探针、阈值和模型分类器更可能随能力演进。替代方案包括更强 VM 隔离、离线训练、人工审批和 capability-based 权限；失败方式包括监控只看输出文本、允许过宽的代理出口、或把测试样例当成真实覆盖率。
  - **Part D｜企业架构候选映射**：`RESEARCH_INFERENCE`：可将其映射为 Context / Harness / Runtime / Governance 的候选变量：Harness 管理实验与暂停，Runtime 施加网络、凭据和文件边界，Governance 定义独立停止权与审计责任。该映射不说明企业 Agent 必须复制训练环境，也不把 OpenAI 的实现主张升级为通用原则。
  - **Part E｜Human Learning Packet**：前置知识为 sandbox / VM、egress control、capability security、red-team、遥测与 incident response。研究者应能用自己的话解释：①隔离、监控、主动测试各自解决哪一种失败；②为什么“看见异常”不等于“能阻止影响”；③训练环境的高权限假设与普通企业 Agent 运行时有哪些边界差异。自测可用一个虚构的自动化训练集群，画出模型、工具、网络、凭据、监控和停止控制的状态流，并指出两个监控失效场景。只有研究者确认后才能形成 `HUMAN_TAKEAWAY`。
  - **Part F｜Research Bridge**：候选关联 T-002 / RP-002-02 / RP-006：文章可能支持把 Governed Capability 的安全变量拆为可达性、观测性和停止权，也可能挑战仅依赖 policy / prompt 的治理假设。待验证问题：企业 Agent 的“独立停止权”是否需要与业务审批和 durable workflow 分离？公开验证方向：对比 OpenAI 训练环境文章、Anthropic `How we contain Claude across products`、云厂商 sandbox / egress 文档和公开 incident / red-team 报告；此处仅为 candidate Research Bridge，不写入 Evidence Ledger。
- 可选参考：**OE-015** 短读。增量在于把 misalignment 检测、行为信号、部署前后监控和缓解串成安全闭环；适用于补模型行为评估与响应机制，建议读到检测信号的边界和误报 / 漏报成本即可。
- 暂不推荐资料及原因：本轮没有新增应排除的官方资料；OE-013 继续作为 observability 短读，OE-010 / OE-011 与本轮安全主题不重复但不承担主推荐。
- 候选池变化：新增 OE-014、OE-015；保留 `AI_ANALYZED`，未标记 `SELECTED`、`READING`、`HUMAN_UNDERSTOOD` 或 `APPLIED`，未创建知识卡，未修改任何正式研究状态。
