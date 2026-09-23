# PROJECT_CONTEXT｜AI 长期上下文

> 本文件主要给 AI 使用。目标是让任何新的研究会话快速理解项目背景、边界和工作方式，而不是给人日常阅读。

## 1. 项目主题

Enterprise Intelligence & AI-era Organization Design｜企业智能与 AI 时代组织设计。

核心问题不是“如何建设一个 Agent”，而是：

> 当 AI 成为能够理解、判断、规划、调用能力并持续行动的非人类智能主体后，企业的认知、决策权、责任、协调机制、组织边界与组织学习如何变化？

## 2. 当前企业智能定义

企业智能，是组织在目标、资源、制度与风险约束下，对认知能力、决策权、行动能力和学习能力进行配置，使组织能够持续：

`感知 → 理解 → 判断 → 组织 → 行动 → 反馈 → 学习`

的重要组织能力。

必须区分：

- Model Intelligence：模型自身的认知能力；
- Subject Intelligence：单个智能主体持续判断和行动的能力；
- Enterprise Intelligence：组织整体配置 Human、AI、Software、Data、Asset 后形成的智能闭环。

## 3. 研究层次

当前更稳定的层次关系是：

`L0 企业智能`

→ `L1 AI 时代组织设计：决策权 / 责任 / 协调 / 企业边界 / 组织学习`

→ `L2 智能主体关系与治理`

→ `L3 智能主体工程：Context / World Model / Capability / Harness / Production / Runtime / Eval`

“关系 / 工程 / 治理”仍适合做解决方案表达，但不是最高层理论。

## 4. 五个长期问题

Q1 决策权：Human 与 AI 的认知优势不同后，Decision Rights 如何重新配置？

Q2 责任与代理：AI 可以决策但不能承担传统意义后果时，Authority、Risk、Accountability 如何保持对应？

Q3 协调机制：Human、Agent、Software、Asset 如何协作？Shared Enterprise World Model 是否形成新的协调基础？

Q4 企业边界：AI 降低交易与协调成本后，哪些 Capability 内部化，哪些可以动态外部调用？

Q5 组织学习：Agent 的运行经验怎样进入 Knowledge、Skill、Rule、World Model、Eval、Policy，真正变成企业能力？

不要轻易增加新的一级问题。新观点先映射到 Q1–Q5。

## 5. 当前关键判断

1. 企业智能不是 Agent 智能之和。
2. 经典组织问题可能长期存在，AI 主要改变主体属性和可行解决机制。
3. AI 的 Agency Problem 可能部分从 Interest Alignment 转向 Intent Alignment + Authority Alignment + Accountability Allocation。
4. Shared Enterprise World Model 暂时更适合定义为 Human-Agent 的共享语义与协调基础设施，而非直接宣称为新协调机制。
5. Application 不会简单消失，但企业软件可能提高 Capability-oriented 程度。
6. Agent Learning 不等于 Organizational Learning；只有经验进入组织级长期资产并经过验证治理，才形成组织学习。
7. 工程与治理应由企业智能和组织设计问题反推，而不是从当前技术组件反推。

## 6. 当前总假设

传统企业信息化主要由人理解业务世界，并通过 Application、Workflow 与组织分工组织企业数字能力。

AI 时代开始出现新的智能主体，逐渐承担理解、判断、规划、能力发现、能力编排、执行和学习。

长期值得验证的企业 AI 原生结构是：

`Intelligent Subject × Enterprise World Model × Capability Network × Real-world Feedback`

注意：这只是研究假设。不要把 Ontology、MCP、Agent、Harness 等当前技术实现当成长期不变量。

## 7. 智能主体工程现阶段理解

工程主线当前大致为：

1. 从 Model-centric 走向智能主体，出现：
   - 用什么智能？Model/MaaS
   - 谁控制连续工作？Harness/Workflow
   - 整个任务在哪里持续运行？Runtime
   - Agent 面对的企业世界是什么？Enterprise Context / World
2. Enterprise Context / World 由多类资产供给：
   - Semantic：Ontology / Object / Relation / State / Event / Business Rule
   - Data/Facts：Database / Operational Data / Event / Logs
   - Knowledge/Experience：Document / SOP / Case / Expert Experience
   - Interface/Action：API / MCP / CLI / Tool / Action
   - Learning/Evaluation：Dataset / Eval Set / Benchmark / Trace
3. FDE 与业务侧共创 Agent Definition。
4. Agent Assembly 是主体定义、Model/Harness、企业资产和 Governance Policy 的交叉点。
5. 企业最终需要稳定的 Production + Runtime 生命周期，而不是押注某个具体 Agent 框架。

产业工程路线进一步固化为：

- E1 Agent Production / Harness / Runtime
- E2 Enterprise Context / World Model / Ontology
- E3 Capability / Action Infrastructure
- E4 Feedback / Evaluation / Evolution

详见 `industry/ROADMAP.md`。

## 8. 治理现阶段理解

治理不是 Agent 做完后再审核，而应内化到生产与运行：

`企业治理原则 → Governance Policy → 生产约束 → Agent Definition / Assembly / Eval / Release → Runtime Enforcement`

重要对象：Identity、Owner、Authority Source、Risk、Autonomy、Permission、Approval、Trace、Evidence、Audit、Retirement。

当前公式：

`Effective Agency = Capability ∩ Authority`

更细可以理解为：

`Effective Action = Business Validity ∩ Capability ∩ Authority`

其中 Business Rule 和 Governance Policy 必须区分：

- Business Rule：业务上这件事能不能做；
- Governance Policy：这个主体有没有权做。

产业治理路线进一步固化为：

- G1 Identity / Ownership
- G2 Authority / Policy
- G3 Human Control / Accountability
- G4 Trace / Audit / Lifecycle

详见 `industry/ROADMAP.md`。

## 9. 研究方法｜Problem-driven Research，不是 Paper-driven Learning

### 9.1 主原则

研究的基本单位是**Concrete Problem**，不是论文、厂商或技术名词。

核心闭环：

> **真实问题 → 理论 / 产业搜索 → 理解 → 工程翻译 → 小规模验证 → 架构 / 方法原则 → 新问题**

展开为：

`Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle → New Problem`

完整方法见：`research/RESEARCH_LOOP.md`。

Q1–Q5 是长期问题地图；真正执行时使用 `research/research-questions.md` 把它们拆成可研究、可工程翻译的问题。

论文、开源项目、产品、公开案例、Analyst View、Policy / Standard 都只是 Evidence Source。

研究进度不以“读了多少论文”衡量，而优先看：

- 解决了几个具体问题；
- 形成了哪些 Engineering Hypothesis；
- 哪些假设被支持、否定或修正；
- 形成或修改了哪些 Architecture / Method Principle。

### 9.2 公开多证据原则

**本公开仓只研究公开世界。**

核心边界：

> **Private experience may inspire a question, but every public claim must be independently supportable by public evidence.**
>
> 私人经验可以启发研究问题，但公开观点必须能够仅依靠公开证据独立成立。

公开仓不得保存、引用、描述或建立任何私人、客户、公司内部、非公开项目的证据链。

公开证据包括：

1. **Academic Theory｜学术理论**；
2. **Product Fact｜产品事实**；
3. **Product Claim｜产品主张**；
4. **Industry Case｜公开产业案例**；
5. **Analyst View｜第三方产业分析**；
6. **Policy / Standard｜政策与标准**；
7. **Counter Evidence｜反向证据**；
8. 开源实现、合成 Demo、公开 Benchmark 等可复核验证材料。

必须区分：

> Product Claim ≠ Validated Theory  
> Vendor Case ≠ Independent Evidence  
> Analyst View ≠ Academic Theory  
> Public Success Case ≠ General Law  
> Synthetic Demo ≠ Enterprise Outcome

不得机械要求每个问题凑齐所有证据类型。缺口可以保留，不能由 AI 猜测补齐。

### 9.3 论文 A / B / C 分级

论文等级相对于当前 Problem 动态判断，不是论文永久属性。

- **A 类｜问题型论文**：直接改变当前工程设计，需要精读；
- **B 类｜原则型论文**：只需理解核心机制和原则性增量；
- **C 类｜启发型论文**：没有当前问题承接，只登记，不制造学习债务。

执行细节见：

- `research/paper-review-plan.md`
- `ai-context/PAPER_READING_MODE.md`

A 类采用：

`Part A Source Walkthrough`
→ `Part B Concept Reconstruction`
→ `Part C Research Interpretation`
→ `Part D Human Takeaways`
→ `Part E Engineering Bridge`

Part E 必须回答：现实问题、改变的旧判断、Engineering Hypothesis、Validation Plan、Candidate Principle、Boundary / Counterexample。

B 类不要求完整 walkthrough；C 类不进入多轮精读。

### 9.4 Judgment 与 Principle 分开

- `JUDGMENTS.md`：我们目前认为“世界可能是怎样的”；
- `PRINCIPLES.md`：如果这些判断与证据成立，工程 / 方法应该怎样设计。

Principle 状态：Candidate / Supported / Stable / Revised / Deprecated。

论文逻辑完整不等于 Principle 已验证。AI Proposal 不能自动升级为 Judgment 或 Stable Principle。

### 9.5 产业研究方法

产业研究不能退化成“厂商功能清单”或“成功案例摘抄”。

产业路线由 Engineering + Governance 问题定义，而不是公司定义：

**Engineering**
- E1 Agent Production / Harness / Runtime
- E2 Enterprise Context / World Model / Ontology
- E3 Capability / Action Infrastructure
- E4 Feedback / Evaluation / Evolution

**Governance**
- G1 Identity / Ownership
- G2 Authority / Policy
- G3 Human Control / Accountability
- G4 Trace / Audit / Lifecycle

公司、产品、框架和案例只是 Observation Targets。

研究一个产品 / 公司时重点回答：

- 它落在哪些 E/G Track？
- 它对应哪个 Concrete Problem / Q1–Q5？
- 哪些是 Product Fact，哪些是 Product Claim？
- 有哪些公开案例与独立来源？
- Analyst View / Policy / Counter Evidence 怎么说？
- 能形成什么 Engineering Hypothesis？
- 是否影响某条 Candidate Principle？

### 9.6 防止确认偏误

问题驱动不等于“只找支持直觉的材料”。

每个重要 Problem 都主动寻找：

- 替代解释；
- 失败案例；
- 反向数据；
- 不需要该机制也能工作的场景；
- 技术阶段性解释。

如果材料与当前框架不匹配，记录“不匹配 / 新现象 / 反例”，不要强行归类。

## 10. Public Repository Boundary｜公开仓边界

本仓库是公开研究作品，不是工作项目知识库。

硬规则：

- 不保存私人、客户、公司内部或非公开项目材料；
- 不记录这些项目的名称、身份、数据、架构、截图、投标材料、内部产品信息或可反向识别的描述；
- 不把非公开项目经验标记为公共 `Field Observation`；
- 不以“已脱敏”为理由把私人项目证据链搬入公开仓；
- 公开 Judgment 与 Principle 必须能够仅使用公开来源进行论证和复核。

私人经验如果启发了一个问题，公开仓只接收这个**抽象后的研究问题**，随后重新寻找公开 Theory / Product / Case / Analyst / Policy / Counter Evidence 进行独立验证。

## 11. 工作台维护规则

### 人默认阅读

优先级：

1. `NOW.md`
2. `research/research-questions.md`
3. `PRINCIPLES.md` / `JUDGMENTS.md`（按当前问题需要）
4. 当前 A 类论文、产业卡或验证记录
5. 再进入 theory-map / reading-list

### AI 默认加载

跨会话恢复现在以 Context Continuity Layer 为默认入口：

1. `AGENTS.md`
2. `context/CURRENT.md`
3. `context/TOPIC_INDEX.md`
4. 当前任务最相关的 1–3 个 Topic State
5. 信息不足时，再按 Topic 链接下钻到 Problem / Hypothesis / Checkpoint / Research / Evidence

本文件 `PROJECT_CONTEXT.md` 继续保存相对稳定的项目背景与研究边界，但**不再要求每个新会话默认全文加载**。

Research Heartbeat / Weekly Synthesis 等专项任务，在完成仓库级定位后，还必须继续遵守 `AGENTS.md` 中 Research Runner 的专项读取顺序。

论文任务按需读取 `research/paper-review-plan.md` 与 `ai-context/PAPER_READING_MODE.md`；选文任务按需读取 `research/reading-list.md`。

核心原则：**Progressive Context Loading｜先少量上下文，不够再展开。**

### 每次研究结束

优先更新：

- `NOW.md`：Active Problem、当前状态、下一步唯一动作；
- `research/research-questions.md`：Problem / Evidence Gap / Engineering Translation / Validation；
- `PRINCIPLES.md`：只有 Candidate Principle 或原则状态发生变化时；
- `EVOLUTION.md`：只有实质认知变化时；
- `JUDGMENTS.md`：只有研究者明确认可且证据足够时；
- `research/reading-list.md`：论文 / 材料身份与实际增量；
- `industry/`：只有与当前 Problem 直接相关的公开案例 / 产品才建卡。

## 12. 研究纪律

- **先问题，后材料；先机制，后工程；先假设，后原则。**
- 研究单位是 Active Problem，不是 Active Paper。
- 一次只保留一个 Active Problem；可以有多个 Evidence Candidate，但不要同时深读多篇。
- 论文按 A / B / C 动态分级，不默认所有重要论文都精读。
- 不用“论文阅读数量”或“笔记长度”衡量研究进度。
- Q1–Q5 是问题地图，Theory + Public Industry Evidence 是证据线，二者不要混为同一层。
- Industry Roadmap 是 Engineering + Governance 的问题路线，不是厂商分类。
- 不让教授论文垄断研究，也不让产业营销替代理论验证。
- 同时维护支持证据与反例，防止问题驱动退化为确认偏误。
- 将作者观点 / 产品事实 / 产品主张 / 案例事实 / Analyst View / Policy / Engineering Hypothesis / Principle / Judgment 严格区分。
- 任何公开结论都不得依赖非公开材料才能成立。
- AI Proposal 不自动变成研究者 Judgment 或 Stable Principle。

_Last updated: 2026-09-23_
