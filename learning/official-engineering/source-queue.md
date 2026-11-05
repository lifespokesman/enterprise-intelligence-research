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



## Verified watch candidates (2026-11-05)

本轮基于最新 `origin/main`；OE-012–OE-018 已被历史学习分支使用（含 PR #29），保留编号，不复制未合并条目，不复用 ID。发现时间为 2026-11-05；下列资料首次发布为 2026-11-02，不写成本轮运行日发表。推荐不等于人类 `SELECTED`。

| ID | Publisher | Verified title | Official URL | Published / version | Axes | Verification / last checked | AI priority | Status | Increment / reading boundary |
|---|---|---|---|---|---|---|---|---|---|
| OE-019 | Anthropic | *Message threads* | <https://platform.claude.com/docs/en/build-with-claude/message-threads> | 2026-11-02：官方 release notes 首次发布；beta `message-threads-2026-08-12` 是标头版本，非发布日期；文档未列独立更新日期 | Context; Harness / Runtime; Agent / Workflow | 2026-11-05：完整指南与官方 release notes 交叉核验；<https://platform.claude.com/docs/en/release-notes/overview> | P1 | AI_ANALYZED | **NEWLY_PUBLISHED**：相对 OE-003 的上下文组织和 OE-005 的组件解耦，新增“传输增量 / 推理缓存 / 应用持久历史”三种职责的明确边界，以及并发与故障恢复协议。精读至能解释 cache expiry、并发冲突、compact 和 fallback；约 30–40 分钟。candidate：RP-002-04 H3 / RP-006，见下 |

## Latest watch (2026-11-05)

### 1. 本周最值得学习的问题

`AI_EXPLANATION`：服务端记住上一轮，是否就意味着 Agent 已获得可靠记忆？应把请求传输、推理缓存、可恢复历史、业务权威状态分别归责，再谈是否需要独立 Context Runtime。

### 2. 唯一主推荐 OE-019：Message threads

来源与日期见上表。首次发布依据 release notes；8 月 beta 标头不能反推公开发布时间；没有版本差异基线，不标 `UPDATED`。

**Part A｜Source Understanding**

- `SOURCE_CLAIM`：随着 tool loop 历史增长，反复发送完整历史造成客户端开销和网络上传成本；message threads 允许后续请求仅发送新增消息。原文解决传输和继续会话问题，不宣称减少模型所需的逻辑上下文或提供业务事务。
- `SOURCE_MECHANISM`：首轮携带完整历史并创建 thread；响应以消息 `id` 作为下一轮的 `previous_message_id`。后续只提交新增消息并省略 system/tools（沿用创建值），其余固定字段须与首轮一致；服务端重建完整上下文给模型。工具循环是说明案例。
- `SOURCE_CLAIM`：这是 ephemeral cache，不是 durable history storage。未解决跨缓存丢失的持久恢复、业务事实权威性、授权撤销后的事实刷新，也没有证明企业 ROI。

**Part B｜Mechanism Reconstruction**

- `SOURCE_MECHANISM`：thread 只追加；每个响应 id 只能续接一次，重复续接 / 仍在执行分别返回 400 `thread_already_continued` / `thread_continue_in_flight`。最后请求后 5 分钟过期；404 `thread_not_found` 时用客户端完整历史创建新 thread。SDK helper 对这些情况可自动重放一次，但仅在对象内存里保留历史，进程外持久化仍由应用负责。
- `SOURCE_MECHANISM`：thread 与 prompt caching 解决不同问题：前者减少上传，后者复用推理侧前缀计算；prompt caching 的缓存范围仍由 `cache_control` 决定。thread ID 本身不会免除输入 token 计费。thread 内不能替换旧消息；压缩需要应用生成摘要并用摘要新建 thread；on-demand compaction 不受支持。
- `AI_EXPLANATION`：可理解成“由服务端暂存的续接副本”：ID 是续接定位符，并非可靠任务档案。依赖客户端持久化、模型上下文上限、配置一致性、API beta 与请求调度；ID 丢失、并发写入、过时权限信息或错误重放都可能使继续会话失败。

**Part C｜Architecture Variables**

- `AI_EXPLANATION`：适合历史大、轮次多、客户端上行受限且可串行推进的任务；短问答收益可能不足。替代路线是完整历史请求加 prompt caching，或由应用数据库/现有 workflow 持有检查点。
- `SOURCE_MECHANISM`：文档要求保留客户端历史并处理冲突与 fallback。`AI_EXPLANATION`：因此应同时观察上传量、input/cache token、thread conflict、cache miss 与恢复结果，而非只看端到端延迟。
- `RESEARCH_INFERENCE`：持久历史、业务副作用幂等和授权检查仍需分别设计；恢复对话不证明外部操作可安全重试。维护负担包括两份历史的一致性、压缩边界、API 变更、日志隐私和恢复测试。`SOURCE_MECHANISM`：原文明确非 ZDR eligible，内存加密保存且最后使用后不超过 1 小时删除；无 list/read/delete thread API。`RESEARCH_INFERENCE`：部署时仍需核验租户和日志访问策略，不能由“ephemeral”推断合规。
- `RESEARCH_INFERENCE`：“临时缓存 ≠ 持久权威状态”可能是结构性职责约束；具体 beta 标头、冲突接口和压缩限制是当前实现条件，不能当稳定层定义。增量传输主要针对传输成本，并非单纯补偿模型智力不足。

**Part D｜Enterprise Translation**

- `RESEARCH_INFERENCE`：Context 对应本轮供模型消费的历史；Harness 负责追加、配置与冲突处理；应用 / 既有 Workflow 持有恢复档案；SoR 持有正式业务结果。这里是逻辑职责候选，不要求物理拆成四套服务。
- `RESEARCH_INFERENCE`：假设退款操作已经提交而响应丢失，恢复 thread 只能恢复对话路径；仍需查询 SoR、核对幂等键与当前权限再决定下一动作。此例为虚构边界测试，不是作者报告的案例。

**Part E｜Human Learning Packet**

- 需掌握四项：增量传输、prompt caching、持久检查点、压缩/恢复后的有效上下文。前置知识：Messages/tool loop、HTTP 并发与重试、缓存失效、基本 token 计费。
- 三个核心学习 / 自测问题：①只发新增 tool result 后，上传字节、模型看到的历史、计费 token 分别怎样变化？为什么不能用网络优化推断推理成本同比下降？②两个 worker 同时续接同一 thread，遇到冲突或缓存失效时，谁保存哪份有效历史、如何恢复？③虚构退款已入账但回复超时，为什么恢复对话不等于可以再退款一次？应查什么状态与权限？
- 读完应能用自己的话解释这四种状态由谁负责，并画出正常续接、缓存失效和重复副作用风险三条路径；不必背 API 参数。能回答即停止精读，再决定是否做公开小实验。
- `HUMAN_TAKEAWAY`：尚未形成，等待研究者亲自回答和确认。AI 分析不改变人类学习状态。

**Part F｜Candidate Research Bridge**

- `RESEARCH_INFERENCE`：候选关联 RP-002-04 H3（Context Runtime 与业务循环分工）及 RP-006（运行职责与持久状态）。这项实现补充并收窄“服务端会话状态意味着独立 Context Runtime”的推断：实现传输续接也可能无需独立持久任务服务；不能据此证明 H3 或某种固定部署边界成立。
- 待验证问题：客户端持久历史 + ephemeral thread 相比每轮完整历史，在固定模型、上下文内容和权限约束下，能否减少传输成本，同时保持缓存丢失、并发冲突和业务写入超时后的正确恢复？
- 公开验证方向：合成工具循环分别使用两种续接方式，注入缓存失效、双 worker 和写入后超时；比较上传字节、token/费用、恢复成功率与重复副作用；以外部状态断言验收。只登记候选，不创建实验、正式 Problem/Hypothesis 或 Evidence Ledger。

### 3. 可选参考资料

本轮不增加可选参考资料。优先完成主推荐的机制边界自测，避免重复上轮评估专题。

### 4. 暂不推荐与排除原因

- Anthropic Engineering 索引仍以 OE-010 为最新文章，已有条目，不重复登记；OE-016–OE-018 已在 PR #29 分析，本轮不重复推荐评估专题。
- OpenAI Developers Blog 索引的 skills、MCP、Codex workflow 文章与既有队列交叉，缺乏本轮优先级增量，不批量收录；本轮没有仅因“过难”排除已核验候选。
- Claude release notes 的近期模型、区域、限额等公告未选作机制精读；不将发布公告本身当架构增量。未逐篇证明所有产品公告均无价值。
- OpenAI `Scaling Git at OpenAI` 本轮因 TLS EOF 未取得可核验正文，撤出草稿，不登记标题/日期为已核验；OpenAI Engineering 覆盖不完整。成功核验 Developers Blog、Anthropic Engineering 与 Claude release notes / 指南（指南及 release notes 使用官方 `.md` 路径读取）。网页搜索工具没有返回可用结果，随后直接读取官方原文。不能据此宣称四站没有其他新文；没有差异证据的页面不归类为 `UPDATED`。

### 5. 候选池变化与筛选

评分 1–5，前四项越高越优先；Learning Cost 越高越费力。Novelty 只相对已登记队列，不代表研究者已掌握旧资料。

| Candidate | Relevance | Mechanism Depth | Architecture Value | Novelty | Learning Cost | Decision |
|---|---|---|---|---|---|---|
| OE-019 | 5 | 4 | 5 | 5 | 2 | 唯一主推荐，30–40 分钟 |

本轮新增 `NEWLY_PUBLISHED` 1 条 `AI_ANALYZED`，新增 `FOUNDATIONAL` 0、实质 `UPDATED` 0；OE-006 继续 `NEEDS_REVIEW`，未做本轮来源升级。旧条目状态不变。保留历史分支 ID；没有知识卡、人工确认状态或正式研究状态写入。

### 6. 下一步

先回答 OE-019 的三个自测问题，特别是“服务端续接与业务恢复”边界；人工确认后才讨论是否深入候选 Research Bridge。不要仅因存在 thread ID 就增加 Context Runtime 或迁移业务状态。
