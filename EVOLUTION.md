# EVOLUTION｜认知演进记录

> 本文件记录的不是“今天聊了什么”，而是**研究者的认知在什么触发下发生了什么实质变化**。
>
> `NOW.md` 回答“现在研究到哪里”；`JUDGMENTS.md` 回答“现在相信什么”；`EVOLUTION.md` 回答“为什么会变成现在这样相信”；`topics/` 负责把成熟判断组织成可公开讨论的完整表达。

---

## 1. 什么时候值得记录

只有发生实质认知变化时才新增条目，例如：

- 一个旧判断被推翻、收缩或改写；
- 一个模糊直觉形成了更清晰的概念；
- 原本分散的两个问题被连接起来；
- 发现过去混淆了两个不同层级；
- 研究方法本身发生重要变化；
- 一个长期命题获得新的边界条件或反例。

不记录普通聊天摘要、临时灵感、待办事项或没有形成变化的资料摘抄。

---

## 2. Origin｜观点来源标记

每个认知节点标记主要来源，用于区分“谁最先提出”与“最终是谁承担这个判断”。

- **`User Insight`**：研究者首先提出的问题、直觉、判断或关键区分；
- **`External Trigger`**：论文、演讲、产品、案例、事件等外部信息首先触发；
- **`Co-developed`**：研究者提出问题或不满，经多轮 Human–AI 碰撞后共同收敛；
- **`AI Proposal`**：AI 首先提出的候选解释或框架，尚不能自动视为研究者自己的判断。

重要原则：

> **文字由 AI 协助生成并不等于观点属于 AI；真正需要保留的是问题来源、理解过程、修改过程与最终判断责任。**
>
> `AI Proposal` 只有在研究者理解、质疑、修改或明确认可后，才可能进一步进入 `JUDGMENTS.md`。

---

## 3. 认知节点模板

```markdown
## EV-XXX｜标题

Date: YYYY-MM-DD  
Origin: User Insight / External Trigger / Co-developed / AI Proposal

### Before｜此前认知

### Trigger｜触发

### Shift｜关键转折

### Now｜当前认知

### Why It Matters｜为什么重要

### Impact｜影响

### Open Question｜仍未解决
```

---

# Baseline｜2026-09-04 仓库基础框架

这是本仓库第一次形成相对完整研究系统时的基线快照。后续不要求保持不变，变化本身应继续记录在本文件。

## A. 研究对象

当前研究对象不是某个 Agent 产品或技术栈，而是：

> **Enterprise Intelligence & AI-era Organization Design｜企业智能与 AI 时代组织设计。**

当前工作定义：

> 企业智能，是组织在目标、资源、制度与风险约束下，对认知能力、决策权、行动能力和学习能力进行配置，使组织能够持续感知环境、理解现实、形成判断、组织能力、采取行动，并根据现实反馈调整自身的组织能力。

持续区分：

- Model Intelligence
- Subject Intelligence
- Enterprise Intelligence

核心命题之一：

> **Enterprise Intelligence ≠ Agent Intelligence 的简单相加。**

## B. 五个长期问题 Q1–Q5

1. **Q1 Decision Rights｜决策权**：Human 与 AI 的认知优势变化后，决策权如何重新配置？
2. **Q2 Accountability & Agency｜责任与代理**：Authority、Risk、Accountability 如何保持对应？
3. **Q3 Coordination｜协调**：Human、Agent、Software、Asset 如何稳定协作？
4. **Q4 Firm Boundaries｜企业边界**：哪些 Capability 应内部化，哪些可以动态外部调用？
5. **Q5 Organizational Learning｜组织学习**：Agent 经验怎样变成企业长期能力？

Q1–Q5 是**问题地图**，不是论文目录、产品分类或产业目录。

## C. 两条公开证据线

公开仓只研究公开世界。

### Academic Theory

用于解释概念、机制、经典问题与边界条件。

### Public Industry Evidence

公开产业证据使用以下身份：

- `[Product Fact]`
- `[Product Claim]`
- `[Industry Case]`
- `[Analyst View]`
- `[Policy / Standard]`
- `[Counter Evidence]`

研究链条：

`Q1–Q5 → Theory + Public Industry Evidence → Hypothesis → Judgment → Engineering / Governance Implication`

关键纪律：

> Product Claim ≠ Validated Theory  
> Vendor Case ≠ Independent Evidence  
> Analyst View ≠ Academic Theory  
> Public Success Case ≠ General Law

## D. Industry Roadmap｜Engineering × Governance

产业研究不按厂商划分，而从智能主体进入企业必须解决的问题反推。

### Track E｜Intelligent Subject Engineering

- **E1 Agent Production / Harness / Runtime**：AI 怎样成为持续工作的智能主体？
- **E2 Enterprise Context / World Model / Ontology**：智能主体怎样理解具体企业世界？
- **E3 Capability / Action Infrastructure**：智能主体怎样作用于企业世界？
- **E4 Feedback / Evaluation / Evolution**：Agent 运行经验怎样进入企业长期能力？

### Track G｜Intelligent Subject Governance

- **G1 Identity / Ownership**：这个主体是谁、属于谁、谁负责？
- **G2 Authority / Policy**：它被允许看什么、调用什么、做什么？
- **G3 Human Control / Accountability**：Human 与 AI 如何配置控制权、决策权与责任？
- **G4 Trace / Audit / Lifecycle**：如何追溯、审计、变更和退役？

简化记忆：

> **主体成立 → 理解企业 → 作用企业 → 企业学习**
>
> 治理同步经历：**身份 → 权限 → 人类控制与责任 → 追溯与生命周期**

厂商、产品、框架和公开案例只是 **Observation Targets**，不是路线本身。

## E. 公开与私人边界

公开仓不保存、引用或描述私人、客户、公司内部或非公开项目的证据链。

当前硬规则：

> **Private experience may inspire a question, but every public claim must be independently supportable by public evidence.**
>
> 私人经验可以启发研究问题，但公开观点必须能够仅依靠公开证据独立成立。

因此公开仓不存在 `[Field Observation]` 证据类型。

## F. 研究资产的职责

- `NOW.md`：当前研究焦点、卡点、下一步动作；
- `EVOLUTION.md`：关键认知如何发生变化；
- `JUDGMENTS.md`：当前值得承担和保留的阶段性判断；
- `topics/`：成熟观点的体系化表达；
- `research/`：理论、学者、论文研究；
- `industry/`：公开产业工程、治理、产品与案例证据；
- `ai-context/PROJECT_CONTEXT.md`：AI 协作者的长期上下文与维护规则。

---

# Cognitive Evolution｜关键认知演进

## EV-001｜从“研究 Agent”上移到“研究 Enterprise Intelligence”

Date: 2026-09-04  
Origin: `Co-developed`

### Before｜此前认知

大量讨论围绕 Agent、Harness、Ontology、Runtime、MCP、智能体治理等具体技术与工程组件展开，容易形成一张越来越大的企业 AI 技术架构图。

### Trigger｜触发

持续追问：如果技术组件继续变化，什么问题是更长期的？为什么模型时代没有引发同样的企业架构变化，而 Agent 作为新的行动主体出现后问题发生了变化？

### Shift｜关键转折

研究对象从“Agent 应该怎么建”上移为：

> AI 作为新的非人类智能主体进入组织后，企业的认知、决策、协调、责任、边界和学习机制如何变化？

### Now｜当前认知

Agent 是当前重要的工程实例，但长期概念更适合使用 **Intelligent Subject**；Enterprise Intelligence 是组织属性，不能还原成单个主体或技术组件。

### Why It Matters｜为什么重要

避免让 MCP、RAG、Ontology、Harness 等阶段性实现定义长期研究框架。

### Impact｜影响

形成 Enterprise Intelligence 定义、Q1–Q5 长期问题，以及“先组织问题、后工程实现”的研究纪律。

### Open Question｜仍未解决

企业智能是否能够形成更稳定、可验证的测量或评价体系，目前仍未解决。

---

## EV-002｜从“直接得到论文结论”转向“先形成自己的理论理解”

Date: 2026-09-04  
Origin: `User Insight`

### Before｜此前认知

论文阅读曾采用“论文 → 七问 → Judgment”或“原文压缩 → 七问”的高效率路径。

### Trigger｜触发

研究者发现：如果没有真正阅读过英文原文，AI 直接给出 Q1–Q5 映射和研究结论，会让人只能接受 AI 的二次判断，而无法真正吸收论文中的概念、论证链和理论营养。

### Shift｜关键转折

论文研究流程改为：

`Source Walkthrough → Concept Reconstruction → Research Interpretation → Human Takeaways → Judgment Update`

### Now｜当前认知

AI 在理论阅读中的角色不是替研究者“读完并宣布答案”，而是把英文论文重新教成一堂能够建立独立判断能力的中文理论课。

### Why It Matters｜为什么重要

仓库要沉淀的是研究者真正理解并能够继续使用的理论，而不是高质量 AI 摘要。

### Impact｜影响

Puranam 2021 即使已经完成七问，也暂不视为“学习完成”，必须先吃透 Task Interdependence、Agent Interdependence、Coupled/Vicarious Learning 等关键概念。

### Open Question｜仍未解决

怎样在“充分理解”与“研究速度”之间建立稳定停止条件，仍需通过后续论文实践调整。

---

## EV-003｜从“理论驱动”扩展为“公开多证据驱动”

Date: 2026-09-04  
Origin: `User Insight`

### Before｜此前认知

Enterprise Intelligence 的研究路线主要围绕学者、经典理论、论文精读展开，产业实践只有零散位置。

### Trigger｜触发

研究者提出：未来企业智能不可能只依赖教授论文，还必须研究产业实践、企业案例、产品哲学和产品机制；理论形成以后仍然需要现实验证。

### Shift｜关键转折

Q1–Q5 保持为长期问题地图，但证据来源扩展为：

> Academic Theory + Public Industry Evidence

并正式引入 Product Fact / Product Claim / Industry Case / Analyst View / Policy & Standard / Counter Evidence。

### Now｜当前认知

Theory 负责解释“为什么”；Industry Evidence 负责观察“产业正在怎样工程化、哪里成立、哪里失败”。两者共同服务 Q1–Q5，而不是互相替代。

### Why It Matters｜为什么重要

避免仓库逐渐变成纯组织理论学习项目，也避免产业营销材料未经验证直接成为研究判断。

### Impact｜影响

新增 `industry/` 产业证据线，并明确 Analyst View 与 Academic Theory、Product Claim 的身份差异。

### Open Question｜仍未解决

不同类型公开证据在形成 Judgment 时是否需要更明确的证据强度等级，暂时不增加复杂评分体系。

---

## EV-004｜从“厂商路线”转向“Engineering × Governance 产业路线”

Date: 2026-09-04  
Origin: `Co-developed`

### Before｜此前认知

一度尝试按照 Model / Agent Native、Enterprise Software、Enterprise World Platform、AI-native Application、Industrial AI 等厂商/产品类型组织产业研究。

### Trigger｜触发

研究者指出，真正长期关注的产业演进其实仍然是此前持续研究的 Harness、Runtime、本体/企业世界、Capability，以及 Agent 治理；按厂商分组虽然适合找样本，却不像真正的产业技术路线。

### Shift｜关键转折

将两个维度拆开：

- **Industry Roadmap**：研究长期工程与治理问题；
- **Observation Targets**：厂商、产品、框架、公开案例只是寻找证据的样本池。

### Now｜当前认知

产业路线稳定为：

`E1-E4 Intelligent Subject Engineering × G1-G4 Intelligent Subject Governance`

即从智能主体的生产运行、企业世界理解、行动能力、反馈演化，以及身份、权限、人类控制责任、追溯生命周期展开。

### Why It Matters｜为什么重要

五年后具体厂商和产品可能消失，但“主体怎样持续工作、怎样理解世界、怎样行动、怎样被治理”这些问题更可能长期存在。

### Impact｜影响

形成 `industry/ROADMAP.md`，并明确不使用“Palantir 路线”“OpenAI 路线”作为顶层产业分类。

### Open Question｜仍未解决

E1-E4 / G1-G4 是否已经最小完备，需要在真实公开产业研究中持续压力测试，而不是现在继续扩层。

---

## EV-005｜从“Field 可以脱敏公开”收紧为“公开仓只研究公开世界”

Date: 2026-09-04  
Origin: `User Insight`

### Before｜此前认知

曾把 `Field Observation` 视为公开仓的一类证据，并认为真实项目经过脱敏和抽象后可以进入公开研究。

### Trigger｜触发

研究者指出：私人、公司和非公开项目本身就不应该在公开仓留下可推断的行业、项目或一手案例线索；即使脱敏，也可能形成反向识别风险。

### Shift｜关键转折

彻底切断公开仓与私人工作世界的证据链：

> 私人经验可以启发问题，但公开观点必须重新由公开证据独立验证。

### Now｜当前认知

公开仓只接受 Academic Theory 与 Public Industry Evidence，不设置公共 `[Field Observation]` 标签，也不描述私人证据来自什么行业、组织或项目。

### Why It Matters｜为什么重要

这不只是信息安全规则，也提高了公开研究的可验证性：公开读者不需要相信研究者拥有某个私人案例，仍能独立检查公开论证。

### Impact｜影响

重写 README、Industry Evidence、NOW 和 AI Context 的公开/私人边界。

### Open Question｜仍未解决

私人研究环境如何长期保存“问题是怎样被现实启发的”而又不产生新的安全负担，留给私有研究系统独立设计。

---

## EV-006｜从“仓库保存结论”扩展为“仓库保存认知变化”

Date: 2026-09-04  
Origin: `User Insight`

### Before｜此前认知

仓库已经能够保存当前状态（NOW）、当前判断（JUDGMENTS）、理论证据和产业证据，但缺少“为什么判断发生变化”的长期记录。

### Trigger｜触发

研究者提出：真正能体现仓库发展轨迹和个人思维逻辑的，不只是最终观点，而是重要认知如何形成、被挑战和被修正。

### Shift｜关键转折

新增 `EVOLUTION.md`，把 File Evolution 与 Cognitive Evolution 区分开：

- Git Commit 保存文件怎么变；
- EVOLUTION 保存为什么要变。

同时加入 Origin：`User Insight / External Trigger / Co-developed / AI Proposal`。

### Now｜当前认知

研究系统形成四个不同层次：

`NOW → EVOLUTION → JUDGMENTS → TOPICS`

分别回答：

> 现在想到哪里？ → 为什么改变？ → 现在相信什么？ → 如何形成成熟表达？

### Why It Matters｜为什么重要

在 Human–AI 共创研究中，最终文字可能大量由 AI 协助完成；记录问题来源、转折和判断责任，比追求“每句话必须由人亲手写”更能真实呈现研究者的认知资产。

### Impact｜影响

从 2026-09-04 起，重大认知变化优先记录在本文件；只有稳定到值得承担的判断才进入 `JUDGMENTS.md`。

### Open Question｜仍未解决

随着条目增多，是否需要按年份拆分暂不预设；达到明显维护负担后再演化。

---

_Last updated: 2026-09-04_
