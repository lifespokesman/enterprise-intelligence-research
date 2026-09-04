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

不要轻易增加新的一级问题。新观点先映射到 Q1-Q5。

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
3. FDE 与客户共创 Agent Definition。
4. Agent Assembly 是主体定义、Model/Harness、企业资产和 Governance Policy 的交叉点。
5. 企业最终需要稳定的 Production + Runtime 生命周期，而不是押注某个具体 Agent 框架。

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

## 9. 研究方法

所有新论文、新学者、新技术、新项目观察，优先回答：

1. 它对应 Q1-Q5 哪个问题？
2. 它继承哪个经典理论？
3. 原理论的关键假设是什么？
4. AI 改变了哪个假设？
5. 它提供的是新问题，还是旧问题的新解法？
6. 它支持、挑战还是修改了哪些 JUDGMENTS？
7. 有没有反例？
8. 哪些结论只是当前 AI 技术阶段成立？

## 10. 项目证据使用规则

真实公安、海关、能源、电网、制造等项目可以用于理论压力测试，但公开仓必须脱敏。

不要存放：

- 客户真实名称与敏感身份；
- 原始数据；
- 内部系统地址；
- 招投标敏感材料；
- 未公开公司内部产品信息。

只沉淀抽象后的组织现象，例如：

“风险研判 Agent 出现以后，管理者从直接分析者变成建议审核者，这是否构成 Decision Rights 的重新配置？”

## 11. 工作台维护规则

### 人默认阅读

优先级：

1. `NOW.md`
2. `JUDGMENTS.md`
3. 必要时进入 `topics/` 或 `research/`

### AI 默认加载

1. 本文件 `PROJECT_CONTEXT.md`
2. `NOW.md`
3. 当前任务相关文件

不要每次无差别读取整个仓库。

### 每次研究结束

优先更新：

- `NOW.md`：当前进度、卡点、下一步唯一动作、Resume Here；
- `JUDGMENTS.md`：只有发生实质认知升级时才更新；
- 对应 Topic：补证据或反例；
- 如果只是新想法但证据不足，优先建 GitHub Issue，而不是修改稳定判断。

## 12. 研究纪律

- 不为了追热点不断增加概念层级；
- 先问题，后技术；
- 先组织问题，后工程实现；
- 同时维护支持证据与反例；
- 将“当前判断”与“未来必然”严格区分；
- 一个时期只保留一个 Active Research Question。

_Last updated: 2026-09-04_
