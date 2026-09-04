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

## 9. 研究方法｜公开多证据驱动，而不是论文或厂商单线驱动

### 9.1 核心原则

Q1–Q5 是长期研究问题，不是“论文目录”。公开仓同时使用 Academic Theory 与 Public Industry Evidence 回答这些问题。

**本公开仓只研究公开世界。**

核心边界：

> **Private experience may inspire a question, but every public claim must be independently supportable by public evidence.**
>
> 私人经验可以启发研究问题，但公开观点必须能够仅依靠公开证据独立成立。

公开仓不得保存、引用、描述或建立任何私人、客户、公司内部、非公开项目的证据链。

公开证据包括：

1. **Academic Theory｜学术理论**：概念、机制、经典问题、边界条件与可检验命题；
2. **Product Fact｜产品事实**：公开产品文档可核验的机制、能力、架构与运行方式；
3. **Product Claim｜产品主张**：厂商对价值、优势、趋势或组织含义的公开解释；
4. **Industry Case｜产业案例**：基于公开来源、可核验的企业实践事实和结果；
5. **Analyst View｜第三方产业分析**：咨询、投研、行业研究机构的横向分析；
6. **Policy / Standard｜政策与标准**：公开法律、监管要求、行业标准与技术标准；
7. **Counter Evidence｜反向证据**：失败案例、替代机制、反向数据和边界条件。

研究链条：

`Q1–Q5 → Theory + Public Industry Evidence → Hypothesis → Judgment → Engineering / Governance Implication`

### 9.2 证据身份必须标记

尽量区分：

- `[Theory]`：论文或理论明确支持；
- `[Product Fact]`：公开产品文档可核验的机制、能力或架构；
- `[Product Claim]`：厂商对价值、优势、趋势或组织含义的主张；
- `[Industry Case]`：公开企业案例中的事实或结果；
- `[Analyst View]`：第三方机构的产业综合判断；
- `[Policy / Standard]`：公开政策、法律、监管或标准要求；
- `[Counter Evidence]`：与当前假设不一致的事实、案例、机制或边界；
- `[Our Judgment]`：本项目在多类公开证据基础上形成的判断。

重要纪律：

> Product Claim ≠ Validated Theory  
> Vendor Case ≠ Independent Evidence  
> Analyst View ≠ Academic Theory  
> Public Success Case ≠ General Law

不得机械要求每张卡凑齐所有证据类型。缺失证据应明确保留为 gap，不能由 AI 猜测补齐。

### 9.3 理论论文阅读｜先还原、再理解、再研究

研究卡首先必须帮助用户**真正看懂论文**，其次才用于更新研究框架。

用户可能不会完整阅读英文原文。AI 不得把论文直接压缩成 Q1-Q5 / JUDGMENTS 结论，因为“压缩”会删除概念形成和论证所需的中间步骤，使用户只能接受 AI 的二次结论，而不能建立自己的理论理解。

固定采用四层结构：

`Part A Source Walkthrough 原文精读`

→ `Part B Concept Reconstruction 关键概念/理论教学`

→ `Part C Research Interpretation Q1-Q5 + 七问`

→ `Part D Human Takeaways 人类吸收层`

### 9.4 Part A｜Source Walkthrough｜原文精读导读

目标不是摘要，而是**按作者自己的顺序陪用户走一遍文章**。

必须恢复：

1. 论文性质、证据类型、适用边界；
2. 作者原始研究问题；
3. 文章的论证链：作者为什么从 A 推到 B，再推到 C；
4. Figure / Table / Typology 在论证中的作用；
5. 作者使用的例子；
6. 作者明确提出什么结论；
7. 作者明确没有解决什么。

不能只写“作者提出 X”，还要解释作者“为什么提出 X”。

### 9.5 Part B｜Concept Reconstruction｜关键概念/理论教学

遇到用户不熟悉的概念，不能只保留英文术语或一句中文翻译。

每个关键概念统一回答：

1. 本文语境里到底是什么意思？
2. 作者为什么在这一段需要它？
3. 用一个简单例子如何理解？
4. 与邻近概念有什么区别？
5. 最容易误解成什么？
6. 论文自己解释到哪里为止？
7. 如果需要经典理论补充，明确标注为 `[背景补充]`，不能冒充 `[原文]`。

尤其重视概念对辨析，例如 task interdependence vs agent interdependence、coupled learning vs vicarious learning、decision rights vs accountability。

### 9.6 Part C｜Research Interpretation｜七问

只有 A/B 完成且用户能够理解论文主要概念后，才回答：

1. 它对应 Q1-Q5 哪个问题？
2. 它继承哪个经典理论？
3. 原理论的关键假设是什么？
4. AI 改变了哪个假设？
5. 它提供的是新问题，还是旧问题的新解法？
6. 它支持、挑战还是修改了哪些 JUDGMENTS？有没有反例？
7. 哪些结论只是当前 AI 技术阶段成立？

七问是**研究映射层**，不是论文摘要层，也不是用户第一次接触论文时的入口。

### 9.7 Part D｜Human Takeaways｜吸收层

最后再压缩为：

- 真正学会的 3–5 个概念；
- 2–3 条长期记忆；
- 哪个 Judgment 被支持/挑战；
- 哪个问题还没有想清楚；
- 下一篇为什么值得接着读。

### 9.8 产业研究方法

产业研究不能退化成“厂商功能清单”或“成功案例摘抄”。

产业路线由工程与治理问题定义，而不是由公司定义：

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

研究一个产品/公司时重点回答：

- 它主要落在哪些 E/G Track？
- 它对应 Q1–Q5 哪些长期问题？
- 哪些是 Product Fact，哪些是 Product Claim？
- 有没有公开企业案例支撑？来源是否独立？
- Analyst View 如何评价？
- 是否存在 Policy / Standard 约束？
- 有哪些 Counter Evidence 或替代路线？
- 如果判断成立，对工程或治理有什么 Implication？

Industry Case 重点回答：

- AI 进入哪个真实任务？
- Human / AI 分工如何变化？
- Decision Rights / Accountability / Coordination / Learning 是否变化？
- 结果指标是什么，证据来源是什么？
- 案例有哪些前提和边界？

产业证据统一沉淀在 `industry/`。

### 9.9 防止确认偏误

不得因为仓库已有 Q1-Q5、E/G Roadmap 和 JUDGMENTS，就只寻找能支持已有观点的内容。

如果论文、公开案例、产品机制、Analyst View 或 Policy/Standard 与当前框架不匹配，应记录“不匹配”“新现象”或“反例”，而不是强行归类。

如果产业界出现理论坐标无法解释的新机制，优先回到理论线寻找更合适的理论解释；只有经过充分验证，才考虑修改一级框架。

## 10. Public Repository Boundary｜公开仓边界

本仓库是公开研究作品，不是工作项目知识库。

硬规则：

- 不保存私人、客户、公司内部或非公开项目材料；
- 不记录这些项目的名称、身份、数据、架构、截图、投标材料、内部产品信息或可反向识别的描述；
- 不把非公开项目经验标记为公共 `Field Observation`；
- 不以“已脱敏”为理由把私人项目证据链搬入公开仓；
- 公开 Judgment 必须能够仅使用公开来源进行论证和复核。

私人经验如果启发了一个问题，公开仓只接收这个**抽象后的研究问题**，随后必须重新寻找公开 Theory / Product / Case / Analyst / Policy / Counter Evidence 进行独立验证。

## 11. 工作台维护规则

### 人默认阅读

优先级：

1. `NOW.md`
2. `JUDGMENTS.md`
3. 当前论文的 `source-walkthrough.md` 或当前产业研究卡
4. 再进入七问 / 理论映射

### AI 默认加载

1. 本文件 `PROJECT_CONTEXT.md`
2. `NOW.md`
3. 当前任务相关文件

不要每次无差别读取整个仓库。

### 每次研究结束

优先更新：

- `NOW.md`：当前进度、卡点、下一步唯一动作、Resume Here；
- `JUDGMENTS.md`：只有发生实质认知升级时才更新；
- 对应 Topic：补公开证据或反例；
- `industry/`：只有与当前问题直接相关的公开案例/产品才建卡，不做厂商收藏；
- 如果只是新想法但公开证据不足，先保持为研究问题或 Hypothesis，不修改稳定判断。

## 12. 研究纪律

- 不为了追热点不断增加概念层级；
- Q1–Q5 是问题地图，Theory + Public Industry Evidence 是公开证据线，二者不要混为同一层；
- Industry Roadmap 是 Engineering + Governance 的问题路线，不是厂商分类；
- 不让教授论文垄断研究，也不让产业营销替代理论验证；
- 先原文还原，再概念理解，再研究解释；
- 不用“摘要效率”牺牲学习过程；
- 先问题，后技术；
- 先组织问题，后工程实现；
- 同时维护支持证据与反例；
- 将“作者观点 / 产品事实 / 产品主张 / 案例事实 / Analyst View / Policy / 我们判断 / 当前技术条件”严格区分；
- 任何公开结论都不得依赖非公开材料才能成立；
- 一个时期只保留一个 Active Research Question。

_Last updated: 2026-09-04_
