# P-001｜Puranam 2021 阅读卡

**论文**：Phanish Puranam (2021), *Human–AI collaborative decision-making as an organization design problem*

**状态：2026-09-07 本轮理论精读完成；2026-09-11 补齐 Part E 工程桥接；企业应用验证未完成。**

**阅读原则**：统一采用 A 原文导读 → B 概念还原 → C 七问研究解释 → D 人类吸收 → E 工程桥接。完整 A/B 以[原文精读导读](P001_puranam_2021_source-walkthrough.md)为入口；本卡保留此前 A 部分概要用于定位，并承接 C/D/E。概要不能替代原文导读与概念教学。

**本轮收尾**：学习卡点已补清，研究者已表示理解分类框架，并提出“从分类走向收益条件与企业应用验证”的进一步问题。该问题已并入当前 Active Problem R-001；不因尚未形成企业实施方法而把理论精读标记为未完成。

**证据纪律**：[原文] / [作者引用的既有研究] / [背景补充] / [我们的推论] 分开。C 中的工程应用建议均为 AI Proposal；下列 JUDGMENTS 关联只是研究解释，本轮不修改 JUDGMENTS.md。

原文：[Puranam (2021), DOI: 10.1007/s41469-021-00095-2](https://doi.org/10.1007/s41469-021-00095-2)。

---

# Part A｜原文概要索引：这篇论文到底写了什么？

> 本部分保留此前概要以便定位；主要依据作者原文及其引用的既有研究。首次阅读或概念不熟悉时，转到 source walkthrough，不从本概要跳入七问。

## A0｜论文性质与研究边界

- 这是一篇 **Point of View**，发表于 *Journal of Organization Design*，不是实证研究，也没有使用数据集做检验。
- 作者研究的对象是 **Human–AI Collaborative Decision-Making（HACD）**。
- 作者主动限定的主要场景是：在知识工作中，Human 与 AI 通过某种协作 **共同产生一个 decision**，然后由第三方实施，例如选股、投资、量刑、候选人筛选。
- 作者说明，这套分析可能对“人训练 AI / AI 训练人 / 算法帮助匹配人”等场景也有启发，但这些情况需要额外考虑，本文没有展开。
- 文中为方便把 AI、algorithm、machine learning 基本混用，这是 2020–2021 年的技术语境，不能直接等同于今天完整的 LLM Agent。

## A1｜作者明确提出的两个核心观点

论文开篇明确说要做两件事：

1. **Human 与 AI 的分工不只有“各做自己更擅长的部分”这一种形式。**
2. **Human 与 AI 的共同学习也存在多种 learning configurations。**

作者的目的不是给出唯一最佳 Human-AI 组织，而是画出一个更完整的 **design space**，帮助理论研究和实际试验更系统地比较不同组合。

## A2｜作者为什么把 Human + AI 看成“组织”

作者认为，从 organization design 角度看，Human 和 Algorithm 的组合可以视为一个：

> **multi-agent, goal-oriented system**

这个 HACD organization 的目标是：**产生一个最终 decision**。

作者用组织设计语言描述这个系统：

- **Division of Labor**：目标如何拆成任务，以及任务如何分配给不同主体；
- **Integration of Effort**：如何通过信息、反馈、奖励、异常处理等方式，把多个主体的工作重新整合起来。

因此，文章的起点不是“AI 是一个什么工具”，而是“多个主体怎样被组织起来完成一个共同决策”。

## A3｜Figure 1：Human-AI 协同为什么可能比单独 Human 或 AI 更好

作者先区分三类 decision task。这里的分类不是永久的，会随技术水平变化。

### Type A｜Algorithm equal or better than Human

当前技术条件下，Algorithm 已经达到或超过 Human。

作者举例：当时的图像识别、手写识别。

此时可以把任务交给 Algorithm。

### Type B｜Human better than Algorithm

Human 仍明显强于 Algorithm。

作者举例：判断求职者 integrity，当时仍更适合 Human。

如果一个大任务可以进一步拆成 A/B 子任务，就可以形成基于 specialization 的分工：各自做相对擅长的部分。

### Type C｜Neither clearly superior, but combination may be better

这是作者认为更有意思的一类。

Human 和 Algorithm 可能单独都没有明显优势，但让两边 **都做同一个判断，再聚合结果**，可能因为 error cancellation 提高整体准确率。

作者借用了 wisdom of crowds、Condorcet jury theorem、ensemble learning 等直觉说明这一点。

**原文事实要点**：HACD 的价值不只来自 specialization，也可能来自 **redundant / parallel judgment + aggregation**。

## A4｜Figure 2：作者给出的 Human-AI 分工二维设计空间

作者没有把 Human-AI 分工简化成“AI 做 A、人做 B”，而是用两个维度描述。

### 维度一｜任务之间的 interdependence

- **Sequential**：一个主体的输出成为另一个主体的输入，最终只有序列后端的输出直接进入最终结果；
- **Parallel**：Human 和 AI 的输出都直接对最终结果产生作用。

### 维度二｜是否 specialization

- **Different types of decisions**：Human 与 AI 做不同类型的判断；
- **Same type of decision**：Human 与 AI 做相同判断。

因此形成四种组合：

| | Parallel | Sequential |
| --- | --- | --- |
| Different decisions | Human/AI分别完成不同分析，最终组合 | 一方先处理一部分信息，另一方基于前者结果形成最终判断 |
| Same decision | Human和AI独立做同一判断，再聚合/比较 | Human和AI依次做同一判断，后者可接受、修正或否决前者 |

作者用股票研究/选股作为示例说明这个四格。

论文脚注还指出：**decision rights 可以被理解为谁有权接受/拒绝另一方输出，在串行结构中也可以近似看成谁位于最后。**

## A5｜为什么“谁更擅长”并不足以决定分工

作者强调，分工效果还取决于：

- specialization gains；
- customization / managing dependencies；
- coordination cost；
- task interdependence。

所以即使 Human 与 AI 各有所长，也不能直接推导出“拆开做一定更优”。

作者引用传统组织设计研究说明：任务怎样拆、任务之间怎样依赖，本身就会影响总体价值。

## A6｜从静态分工进入动态问题：Human 与 AI 都会学习

文章后半部分从“现在谁更强”转向：**两边在共同工作以后会怎么变。**

作者把 learning 定义为：因为 experience 导致 belief 或 behavior 发生变化，并不要求 performance 一定提高。

在 decision-making 中，如果同样的输入在两个时间点得到不同决策，可能是主体在中间根据过去的输入、输出、过程和反馈改变了决策方式。

作者认为 HACD 的特殊性之一是：

> Human 与基于 ML 的 Algorithm 都可以是 adaptive systems，因此不仅各自学习，还可能互相调整、互相学习。

## A7｜Table 1：四种 Learning Configurations

作者用两个维度划分 Human-AI 的学习环境。

### 维度一｜反馈是否 interdependent

- **Independent feedback**：分别得到针对自身贡献的反馈；仅把共同结果分别发送给双方不算独立反馈；
- **Interdependent feedback**：一方的反馈受另一方决策影响，反过来也如此；只评价共同结果是文中的典型例子，学习因此耦合。

### 维度二｜Communication 是否 feasible

这里的 communication 不只是“能不能聊天”，而是能否交换：

- inputs；
- process；
- outputs；
- feedback。

组合以后得到四种 learning configurations：

| Feedback / Communication | 交流受限 | 可以交流 |
| --- | --- | --- |
| Independent feedback | **Isolated Learning** | **Vicarious Learning** |
| Interdependent feedback | **Coupled Learning** | **Coupled + Vicarious Learning** |

作者用股票研究报告、木匠合作等例子说明：如果只知道整体结果，而不知道各自哪部分做得好坏，两边的学习会被绑定；如果能够看到另一方的经历、输入和反馈，就可能形成 vicarious learning。

## A8｜作者特别提醒的几个动态风险

这些不是我们的外部推论，而是文章引用既有 organization design / learning literature 后明确讨论的现象。

### 1. Coupled Learning 可能出现错误学习

当反馈只针对整体结果时，个体很难知道成功/失败究竟由谁造成，可能产生 false positive、false negative，甚至 superstitious learning。

### 2. Communication constraints 会影响互相学习

Human 可能因为 Algorithm 使用的信息规模太大而无法理解，也可能因为 explainability 问题无法看到 Algorithm 的 decision process。

### 3. Sequential architecture 会改变学习机会

如果上游主体先筛选数据/案例，下游主体只能看到经过筛选后的输入，那么组织结构本身已经改变了下游主体未来可以学习的数据。

### 4. Division of labor 会反过来塑造能力

作者借 Smith / Mintzberg 的传统观点提醒：分工不仅利用现有能力差异，也可能在长期运行中制造新的能力差异。

## A9｜作者最后真正得出的结论

作者没有声称找到了 Human-AI 最佳组织形式。

最后的结论是：

- Human-AI collaborative decision-making 存在一个比“专业化分工”更大的组织设计空间；
- division of labor 与 learning configuration 应该联合考虑；
- 现有 organization design literature 已能解释其中一些组合，但远没有覆盖全部组合；
- 还需要更多 conceptual work 和 empirical data；
- organization design researchers 与 HACD practitioners 之间存在很大的合作研究空间。

## A10｜读完原文以后，先记住作者自己的五个关键词

在进入我们的七问之前，只需要先记住：

> **HACD = Organization**  
> **Division of Labor**  
> **Task Interdependence**  
> **Aggregation**  
> **Learning Configuration**

这五个词是作者这篇论文真正提供的骨架。

---

# Part B｜Concept Reconstruction：本轮补清的概念关系

详细教学见[source walkthrough](P001_puranam_2021_source-walkthrough.md)第 7–12 节及第 16 节，前半篇分工概念见第 1–5 节。

| 先前容易混淆的内容 | 本轮明确的区分 |
|---|---|
| 专业化、聚合与分工分类轴 | 前两者解释可能收益；Figure 2 的维度是任务相同 / 不同、并行 / 串行 |
| Task Interdependence 与 Agent Interdependence | 任务联合价值或输入输出关系，与主体反馈受对方行动影响的关系不同 |
| 两种反馈与四种学习配置 | 反馈只是一条轴，还需加入经验交流是否可行 |
| Coupled 与看不清对方 | Coupled 指反馈耦合；交流可行时也可以 Coupled |
| 独立反馈与 Vicarious | 独立反馈不保证能借鉴对方经验；后者需要经验交流与利用 |
| Learning Configuration 与输入筛选、错误归因 | 前者描述学习信息条件；后两者描述学习机会受到的限制或学习中可能产生的错误 |
| Learning 与能力提高 | 因经验改变信念或行为，不保证性能改善，也不保证变化被长期保留 |

四种配置是条件分类，不是从差到好的等级；木匠教学例子用于解释，不是验证企业效果的证据。

# Part C｜Research Interpretation：七问研究拆解

> 从这里开始才进入我们的 Q1-Q5、经典理论和 JUDGMENTS。以下内容包含研究映射和我们的解释，不再等同于作者原文。

## 1｜它对应 Q1-Q5 哪个问题？

### Q1｜认知与决策权配置：★★★★★ 主问题

论文从“一个最终决策应该怎样拆成若干子决策，并分配给 Human 和 Algorithm”开始，而不是从“AI 能不能替代人”开始。

它提出两个重要设计维度：

1. **任务依赖方式**
   - Parallel：人和 AI 并行判断；
   - Sequential：前一个主体的结果成为后一个主体的输入。
2. **是否专业化**
   - Human 与 AI 做不同子任务；
   - Human 与 AI 做相同判断，再聚合结果。

特别重要的是，论文把 **decision rights** 放进序列关系中理解：谁处在决策序列后端、谁能接受或拒绝另一方输出，实际上体现了决策权配置。

**对当前研究的启发**：Human-AI 分工不能只用“谁更擅长什么”来决定，还要看任务依赖、顺序、结果聚合与决策权位置。

### Q3｜Human-Agent 协调机制：★★★★★ 主问题

论文明确把 Human + Algorithm 的组合视为一个 **multi-agent, goal-oriented system**。

组织设计需要解决：

`Goal → Task Decomposition → Task Allocation → Interdependence → Integration of Effort`

[我们的推论] 对本项目，Human-AI 协同可以先在组织设计层定义，再考虑技术工作流实现。这是从论文获得的方法启发。

这意味着 Workflow / Harness 等只是实现层；更上位的问题是：为什么这样拆任务、这样安排顺序、这样聚合结果？

### Q5｜组织学习：★★★★☆ 重要问题

论文不只研究静态分工，还提出 **Learning Configuration**。

两个维度：

- 反馈是否独立或耦合；
- Human 与 AI 是否能交换彼此的输入、过程、输出与反馈。

组合成四种学习形态：

| Feedback / Communication | 交流受限 | 可以交流 |
| --- | --- | --- |
| Independent feedback | Isolated Learning | Vicarious Learning |
| Interdependent feedback | Coupled Learning | Coupled + Vicarious Learning |

关键启发：同样是两个会学习的主体，反馈怎么设计、信息是否共享，会产生不同的长期学习结果。

### Q2｜责任与代理：★☆☆☆☆ 低

论文涉及 decision rights、information、reward provision，但没有系统讨论：

- 谁承担后果；
- Authority；
- Accountability；
- 法律/伦理责任。

因此不能用本篇直接支撑当前关于 AI Agency Problem 的判断。

### Q4｜企业边界：★☆☆☆☆ 低

论文用 outsourcing / offshoring、Smith / Ricardo 解释专业化收益，但没有研究 AI 是否重新定义企业边界。

---

## 2｜它继承哪个经典理论？

### 主干：Organization Design

Puranam 将组织设计归结为两个基本问题：

> **Division of Labor + Integration of Effort**

并连接四条理论线：

1. **分工与专业化**：Adam Smith / Ricardo；
2. **Task Interdependence**：Thompson、Burton & Obel、Milgrom & Roberts，以及 Puranam 自身的组织设计研究；
3. **Organizational Learning**：Cyert & March、Lave & March、Lounamaa & March；
4. **Vicarious / Social Learning**：Bandura 及组织学习传统。

所以这篇文章更准确地说是：

> **Organization Design × Organizational Learning** 用来解释 Human-AI collaborative decision-making。

---

## 3｜原理论的关键假设是什么？

### 假设 A｜组织是多个主体围绕共同目标协作

`Goal → Task Decomposition → Task Allocation → Interdependence → Coordination`

这个假设本身并不要求组织成员必须是 Human。

### 假设 B｜主体存在知识与能力差异

传统组织中是不同专业人员能力不同；Human-AI 组织中则表现为不同类型主体能力结构不同。

### 假设 C｜任务之间存在依赖

专业化收益不能独立看，必须同时考虑协调成本和任务依赖。

### 假设 D｜组织成员会根据经验学习

组织结构不仅决定“现在谁做什么”，还会改变“以后谁能够学到什么”。

---

## 4｜AI 改变了哪个假设？

[我们的推论] 本篇更适合被解释为主体类型与设计条件的扩展，而不是“AI 推翻经典组织设计”：

> **AI 扩展了组织成员的主体类型，并改变了可行的分工、协调和学习机制。**

### 变化 1｜已有的聚合机制扩展到 Human–AI 组合

Human 和 AI 可以做同一种决策，再聚合输出，通过 error cancellation 获得更高决策质量。

因此“重复判断”本身也可能是一种有效组织设计，而不只是浪费。聚合早已存在于人类群体判断和算法集成中，并非 AI 首次创造的新机制。

### 变化 2｜Human 与 AI 都可以是 adaptive systems

两者都能根据反馈改变未来判断，因此会出现 mutual adjustment，而不是“人使用一个固定工具”。

### 变化 3｜Human-AI 的信息交换约束具有新形态

Human 可能无法处理算法使用的大量输入，也可能无法理解算法内部决策过程。传统的 epistemic interdependence 与 communication constraint 在 Human-AI 组织中出现新的形式。

---

## 5｜它提供的是新问题，还是旧问题的新解法？

### 当前判断：主要是“旧组织问题 + 新主体 + 新设计空间”

长期问题仍然是：

- Division of Labor；
- Coordination / Integration of Effort；
- Organizational Learning。

AI 改变的是主体属性，从而扩大了可行解空间。

因此本篇更适合被理解为：

> **Substrate expansion，而不是 Theory replacement。**

但它确实带来两类 Human-AI 更突出的设计空间：

1. Human 与 AI 对同一决策进行平行判断并聚合；
2. Human 与 Algorithm 之间的 mutual adaptation / coupled learning。

---

## 6｜它支持、挑战还是修改哪些 JUDGMENTS？有没有反例？

### J-001｜企业智能不是 Agent 智能之和

**关系：在 HACD 范围内提供机制层面的理论支持；不能据此验证整个企业智能判断。**

论文说明最终表现不仅取决于单个主体能力，还取决于：

- 任务怎么拆；
- 谁做什么；
- 并行还是串行；
- 如何整合；
- 反馈给谁；
- 主体之间能否互相学习。

**AI Proposal｜可供后续验证的补充表述，本轮不写入 JUDGMENTS：**

> 企业智能不仅是主体能力问题，也是主体配置、任务依赖、信息整合和反馈结构问题。

### J-002｜AI 改变的是组织主体属性，不一定是组织基本问题本身

**关系：提供理论支持；仍需跨场景验证。**

这是本篇最直接支持的 Judgment。论文把 Human + Algorithm 继续放在 division of labor、interdependence、coordination、learning 等经典组织设计问题中分析。

**状态处理：**此前提出过提升证据状态的建议；2026-09-07 收尾仍保留为候选解释，J-002 在 JUDGMENTS.md 中维持“探索中”。

### J-003｜Enterprise World Model 更可能先成为协调基础

**关系：不直接支持，但提供理论接口。**

论文没有讨论 Enterprise World Model，不能把它当作 J-003 的直接证据。

但它说明 Human-AI 协调依赖 inputs / process / outputs / feedback / communication，因此可以提出新的验证问题：

> Enterprise World Model 是否能够降低 Human-Agent 之间的信息交换与 epistemic interdependence 成本？

### J-004｜AI Agency Problem 转向 Intent / Authority / Accountability

**关系：基本不支持。**

Decision Rights ≠ Accountability。本篇没有足够内容支持责任配置判断。

### J-005｜工程与治理应从组织问题反推，而不是从技术组件反推

**关系：为从组织问题反推工程提供间接启发；本文没有验证完整治理体系。**

论文从最终决策任务、任务分解和主体配置开始，而不是从 AI 技术组件开始。

[我们的推论｜AI Proposal，尚未验证为企业实施方法] 可形成一个工程前置顺序：

`业务目标 → Task Decomposition → Human/AI Allocation → Interdependence → Decision Rights → Information/Feedback Architecture → Workflow/Agent/Harness/Tool`

### J-006｜Application → Capability-oriented

**关系：不涉及。**

### 作者讨论的风险与补充边界

1. **协调成本可能吃掉专业化收益**：Human 与 AI 各自更擅长不同任务，不代表拆分后一定更优；
2. **[背景补充] Human + AI 不一定 1+1>2**：错误相关性、偏差和聚合规则会影响收益；本文未推导企业选型所需的完整数学条件；
3. **Coupled Learning 可能学错**：整体反馈无法识别到底是谁导致成功/失败，可能产生 false positive / false negative 与 superstitious learning；
4. **Sequential Architecture 会塑造学习数据**：上游主体的筛选会改变下游主体未来能看到和学习的数据分布。

第四点尤其重要：

> **组织设计本身会塑造未来可学习的数据。**

---

## 7｜哪些结论只是当前 AI 技术阶段成立？

### 明显带有 2020–2021 技术阶段特征

1. **Type A / B / C 的具体任务举例**会随着 AI 技术变化而迁移；
2. 文中为方便将 AI / Algorithm / Machine Learning 混用，不能直接覆盖今天 LLM / Agent / Tool Use / Long-horizon autonomy；
3. 论文研究范围主要是：
   `Human + AI → Decision → Third Party Executes`
   而不是今天更常见的：
   `Human/Event → Agent Decision → Tool Action → Environment Change → Feedback`。

因此本篇天然较少涉及行动权、Runtime 与直接执行后的责任治理。

### 更可能具有长期价值

1. 多主体系统仍然需要任务分解；
2. Task Interdependence 仍会存在；
3. 主体能力差异只是分工设计的一个变量，不能单独决定组织设计；
4. 多主体学习高度依赖 Feedback Architecture；
5. Organization Design 会改变未来的数据分布与学习机会。

---

## 应用解释补充｜收益条件、失败条件、验证办法

**身份：[我们的推论｜AI Proposal]。以下是候选比较方法，不是 Puranam 的实证结论，也不是已验证的企业实施路线。**

### 1. 选择候选安排的条件

| 候选安排 | 何时值得尝试 | 需要验证的失败条件 |
|---|---|---|
| 单主体完成 | 一方已足够可靠，另一方没有提供明显信息或判断增量 | 环境变化使单主体优势失效；单项准确率不能替代责任与授权要求 |
| 专业化分工 | 任务可拆，各方在不同部分有可测优势，交接信息与成本可控 | 局部优化损害整体；交接成本抵消收益；仅有角色名称、没有真实能力差异 |
| 独立判断后聚合 | 各判断者对同一问题有有效信息，错误不总同向，有可验证的聚合规则 | 同源错误、弱判断拉低强判断、错误聚合或同一个错误被多数重复 |

“AI 做基础、人做高级”不能代替能力比较。专业化与聚合可以组合使用，不必为整条企业流程只选择一种结构。

### 2. 反馈与借鉴可能增加什么

- 针对贡献的反馈可能帮助定位错误，但现实中不一定能可靠分离贡献；
- 整体反馈用于检查共同目标是否实现，但不能直接证明每个局部做法正确；
- 交流经验可能减少重复试错，也可能传播错误、使原本不同的判断趋同；
- “先保留初判，再交换证据、按明确规则整合”只是可测试的候选安排，不是普遍最优规则；
- 反馈改变当前任务中的后续行为，不等于未来任务持续改善；持续改进需要能够保留、复用并验证变化的机制。日志保存、相互聊天、参数更新都不能单独证明组织学习完成。

### 3. Agent–Agent 的收益来源需要拆开测量

- 专长互补：不同知识、工具与上下文的有效分工，不能靠给同一模型起不同角色名证明；
- 判断聚合：多个候选答案的比较或集成；同一模型多次采样也可能实现，不必总依赖多 Agent 对话；
- 并行扩容：增加计算量与上下文容量、提高搜索覆盖；不能全部归为专业化收益。

将 P-001 延伸到可调用工具、改变环境的 Agent，属于研究外推。原文主要研究共同形成决策、由第三方实施；行动权限、持续运行和责任等仍需额外分析。

### 4. 本轮补充的公开证据｜仅核对相关结果，未完成这些论文的精读

- **[背景补充｜Academic Empirical Evidence / Counter Evidence]** Vaccaro、Almaatouq 与 Malone (2024) 的元分析覆盖百余项实验研究；在所纳入任务与指标上，人机组合平均未超过表现更好的单独一方。[作者论文版本](https://arxiv.org/abs/2405.06087)。这不能直接推为所有当前 Agent 系统的结论。
- **[背景补充｜Academic Empirical Evidence / Counter Evidence]** Choi、Zhu 与 Li (2025) 在七个 NLP 基准上的实验发现，多数投票解释了通常归于多 Agent 辩论的大部分收益。[Debate or Vote](https://arxiv.org/abs/2508.17536)。结论受模型、任务、协议与实验设置约束，不代表交流永远无用。
- **[背景补充｜Product Fact / 厂商自述]** Anthropic (2025-06-13) 公开说明其研究系统采用主 Agent 协调、子 Agent 分头搜索。[工程报告](https://www.anthropic.com/engineering/multi-agent-research-system)。**[Product Claim / 厂商经验]** 其关于适合广泛并行研究、紧密依赖任务协调困难和额外成本的描述，保留为特定系统经验，不等同于独立验证的组织规律。

这些补充只服务 R-001 的证据缺口，不改变当前唯一动作，也不把补充材料自动升级为核心精读对象。

### 5. R-001｜企业决策协作选型与反馈验证

**状态：Active；P-001 已提供理论机制，工程比较验证尚未启动。主要对应 Q1 / Q3 / Q5。**

问题：给定一个具体企业决策任务，怎样选择单主体、专业化分工或判断聚合，并设计能够验证整体收益的反馈？

启动时至少具备：

1. 明确决策任务、最终输出、现有流程、责任与权限边界；
2. 可公开核查的样例或明确标记的合成样例，以及评价依据；
3. 可比较的单主体基线、候选分工/聚合方案与资源预算；
4. 质量、错误类型、耗时、成本及相关运行约束；
5. 如声称学习收益，使用后续新任务验证，而不只比较当前一次输出。

候选最小产物：任务定义、两三个可比较安排、评价记录与边界结论。此清单是 AI Proposal，不代表企业通用方法已成立。合成样例可用于机制试验，不能单独证明真实企业效果；公开仓始终不接收私人项目证据链。

### 6. H-P001-01｜原有假设继续保留

> 企业智能不仅取决于“谁做决策”，还取决于企业如何设计反馈，使 Human 与 AI 的局部学习能够转化为整体组织学习。

状态：Exploring / AI Proposal。本轮没有升级为 Judgment；也不把“单次人机合作有效”直接等同于“组织形成长期能力”。

---

# Part D｜Human Takeaways：2026-09-07 本轮收尾

## 五组应保留的概念

| 概念组 | 恢复时要能解释什么 |
|---|---|
| Specialization Gains | 不同主体在不同任务上的优势如何产生收益，协调成本为何可能抵消收益 |
| Aggregation Gains | 同一问题的多个判断为何可能有价值，为什么不保证更准 |
| Division of Labor / Task Interdependence | 做什么、怎样衔接；串行/并行描述输出关系，不只是钟表时间 |
| Learning Configuration / Agent Interdependence | 反馈是否相互依赖、是否能从对方经验中学习；任务依赖不等于反馈依赖 |
| Learning / Mutual Adjustment / Censored Inputs / Superstitious Learning | 经验怎样改变行为；可见样本与错误归因怎样影响学习，学习为何不保证改善 |

## 三条长期记忆

1. 人机合作的效果取决于主体能力、工作结构、整合方式与协调成本，不能只比较模型能力。
2. 工作安排会影响各方以后能接触什么经验；反馈与交流安排会影响如何学习，也可能强化错误。
3. 分类框架帮助提出候选方案；选择企业方案还需要任务证据、收益与失败条件，以及比较验证。

## 本轮认知变化与理解证据

- 从将全篇压缩为“四个名词 / 一张四格表”，转向区分收益来源、两套分类维度与学习后果；
- 能区分共同工作与反馈耦合，指出共同结果不足以证明个人做法正确；
- 已明确理解分类框架，并进一步要求解释何时产生收益以及如何用于企业任务；
- 因而区分“原文理解完成”“应用假设形成”“企业方法验证”三个完成标准。应用验证缺口不再无限延长本篇概念补课。

这里记录本轮学习进度，不宣称所有概念已永久掌握。以后若出现具体误解，局部回看相应原文即可。

## EVOLUTION 与 JUDGMENTS

- 候选方法节点：[EV-008](../../EVOLUTION.md)；Origin 为 Co-developed，研究者提出应用价值问题，AI 协助提出分层停止条件。
- J-001 / J-002 获得的是有限范围内的机制解释；J-005 获得工程启发。本文不足以验证整个企业智能或治理体系。
- **本轮 JUDGMENTS.md 内容与状态均不修改。**应用建议、R-001 的工程假设和 H-P001-01 均不自动变成研究者的稳定判断。

## 尚未解决与下一篇

- 尚未解决：R-001 所列企业选型与反馈验证问题；没有形成可直接交付的通用实施方法。
- P-002 值得继续的理由：[我们的阅读目的] 扩展对管理者工作与 AI 作用的理解，不要求 P-001 一篇承担全部组织与企业应用问题。
- P-002：[Purpose not prediction: the role of managers in the age of AI](https://doi.org/10.1007/s41469-026-00205-y)，期刊类型为 Editorial；完整 PDF 已核验可读，并已完成文献类型、开场问题与五类管理者工作的初步梳理。
- 下一步唯一动作：围绕 R-001 对 P-002 做 B 类定向阅读，获得 Engineering Bridge 后决定是否升级 A 类。当前状态见 [NOW](../../NOW.md)。

---

# Part E｜Engineering Bridge：从 P-001 到 R-001

> **身份：[我们的推论｜AI Proposal]。**以下是基于论文机制形成的工程假设，不是作者结论，也不自动进入 `PRINCIPLES.md`。

## Problem

给定一个高价值企业判断任务，何时应由单一主体完成，何时采用 Human–AI 专业化分工或独立判断后聚合？最终决策权和反馈怎样设计，才能同时获得质量收益、保持责任边界并支持后续学习？

## What the paper explains

P-001 解释了为什么不能只比较 Human 与 AI 的单体能力：任务相同 / 不同、并行 / 串行、整合方式、反馈依赖与经验交流条件，会共同改变当前决策表现和未来学习机会。它没有证明哪一种配置普遍最优。

## Changed judgment

旧直觉容易把协作设计压缩为“AI 做基础、人做高级”或“让两边都给答案”。当前改变是：

> **能力差异只能提出候选分工，不能单独决定协作结构、最终决定权与反馈机制。**

## Engineering hypothesis

对具体任务按以下顺序设计并记录候选方案：

`业务目标与评价标准 → 任务分解 → 单主体基线 → Human / AI 能力证据 → 并行 / 串行 / 聚合结构 → 最终决定权 → 局部与整体反馈 → 后续任务验证`

其中，专业化与聚合可以在不同子任务上组合，不要求整条流程只使用一种模式。

## Validation plan

选择公开可核查或明确标记为合成的高价值判断任务，至少比较：

1. 当前最强单主体基线；
2. 专业化分工；
3. Human 与 AI 独立判断后按预先规定的规则聚合；
4. 必要时增加串行复核方案。

同时记录质量、错误类型、耗时、成本和人工投入。若声称产生学习收益，必须在未见过的后续任务上测试，而不是只看本轮输出。

## Candidate principle

> **Human–AI 决策架构不能只按模型能力选型；应联合设计任务结构、结果整合、最终决定权，以及局部 / 整体反馈。**

当前状态：Candidate / AI Proposal。完成比较验证并获得反例边界前，不升级为正式 Architecture Principle。

## Boundary / counterexample

- P-001 是 Point of View，没有提供企业实证数据或通用最优配置；
- 聚合可能因同源错误或错误规则变差；
- 专业化收益可能被交接与协调成本抵消；
- 原文主要研究共同形成判断、由第三方执行，不足以直接推出行动型 Agent 的授权、审计和责任机制。

---

## 本阅读卡的层级边界

- **Part A = Source Walkthrough**：本文保留概要索引，详细原文导读在配套 source walkthrough；
- **Part B = Concept Reconstruction**：本卡保留辨析导航，详细概念教学在配套 source walkthrough；
- **Part C = Research Interpretation**：Q1–Q5 / 七问、补充证据、应用推论与待验证问题；
- **Part D = Human Takeaways**：本轮吸收记录、认知变化、剩余问题与下一步；
- **Part E = Engineering Bridge**：从论文机制形成可验证工程假设，明确候选原则与边界。

后续 A 类论文使用 A–E；B 类定向理解并形成简版 Engineering Bridge；C 类只登记价值与升级条件。

_Last updated: 2026-09-11_
