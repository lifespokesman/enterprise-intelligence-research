# Enterprise Intelligence Research

> 企业智能与 AI 时代组织设计的长期研究仓库

[English](README.md) | **简体中文**

本仓库关注一个比“如何建设 Agent”更上位的问题：

**当 AI 开始成为能够理解、判断、规划、调用能力并持续行动的非人类智能主体后，企业的认知、决策、协调、责任、边界与学习机制将如何变化？**

## 当前定义：什么是企业智能

当前暂定：

> **企业智能，是组织在目标、资源、制度与风险约束下，对认知能力、决策权、行动能力和学习能力进行配置，使组织能够持续感知环境、理解现实、形成判断、组织能力、采取行动，并根据现实反馈调整自身的组织能力。**

可抽象为：

`感知 → 理解 → 判断 → 组织 → 行动 → 反馈 → 学习`

需要持续区分：

- **Model Intelligence**：模型自身的理解、推理、预测与生成能力；
- **Subject Intelligence**：一个智能主体围绕目标持续判断、行动与反馈的能力；
- **Enterprise Intelligence**：整个企业如何配置人、AI、软件、数据和资产形成组织层面的智能闭环。

企业智能不等于企业内部所有 Agent 智能的简单相加。

## 五个长期组织问题

1. **决策权**：Human 与 AI 的认知优势不同后，决策权应该如何重新配置？
2. **责任与代理**：AI 可以决策但不能像人一样承担后果时，权力、风险与责任如何保持对应？
3. **协调机制**：Human、Agent、Software、Asset 如何形成稳定协作？共享企业世界模型是否会成为新的协调基础？
4. **企业边界**：AI 降低能力发现、协调、监督和交易成本后，哪些能力应内部化，哪些可以动态调用？
5. **组织学习**：Agent 的运行经验怎样进入知识、Skill、Rule、World Model、Eval 与 Policy，真正转化为组织学习？

详见 [`topics/README.md`](topics/README.md)。

## 公开证据架构：Theory × Industry Evidence

Q1–Q5 是**问题地图**，不是“论文目录”。本项目同时从学术理论和公开产业证据寻找答案。

公开仓只接受能够由公开来源独立支持的证据：

- **Academic Theory｜学术理论**：概念、机制、经典问题、边界条件和可检验命题；
- **Product Fact｜产品事实**：公开产品文档可以核验的具体机制与架构；
- **Product Claim｜产品主张**：厂商对产品价值、趋势和组织含义的公开解释；
- **Industry Case｜公开产业案例**：公开来源能够核验的企业实践事实或结果；
- **Analyst View｜第三方产业分析**：咨询、投研和产业研究机构的横向判断；
- **Policy / Standard｜政策与标准**：公开法律、监管要求、行业与技术标准；
- **Counter Evidence｜反向证据**：失败案例、替代机制、反向数据和边界条件。

研究链条：

`Q1–Q5 → Theory + Public Industry Evidence → Hypothesis → Judgment → Engineering / Governance Implication`

核心边界：

> **私人经验可以启发研究问题，但公开观点必须能够仅依靠公开证据独立成立。**

必须持续区分：

> **Product Claim ≠ 已验证理论**  
> **Vendor Case ≠ 独立证据**  
> **Analyst View ≠ Academic Theory**  
> **Public Success Case ≠ 普遍规律**

产业证据见 [`industry/`](industry/)。

## 六个学习模块

1. 组织为什么存在：Simon、Coase、Williamson
2. 组织如何分工与协调：Mintzberg、Organization Design、Information Processing
3. 权力、委托与责任：Agency Theory、Decision Rights、Delegation、Accountability
4. 组织如何学习：March、Argyris & Schön、Organizational Learning
5. AI 作为新的组织主体：Human-AI Team、Multi-Agent Organization、AI Decision Making
6. 重新推导 Enterprise Intelligence：从组织问题反推智能主体关系、工程与治理

详见 [`research/theory-map.md`](research/theory-map.md)。

理论学习是公开证据线之一，不等于整个研究系统。

## 产业研究路线：Engineering × Governance

产业路线不按厂商划分，而从一个智能主体真正进入企业以后必须解决的工程与治理问题反推。

### Track E｜Intelligent Subject Engineering

- **E1 Agent Production / Harness / Runtime**：AI 怎样成为持续工作的智能主体？
- **E2 Enterprise Context / World Model / Ontology**：智能主体怎样理解具体企业世界？
- **E3 Capability / Action Infrastructure**：智能主体怎样调用软件与资产作用于企业世界？
- **E4 Feedback / Evaluation / Evolution**：Agent 运行经验怎样进入企业长期能力？

### Track G｜Intelligent Subject Governance

- **G1 Identity / Ownership**：这个智能主体是谁、属于谁、谁负责？
- **G2 Authority / Policy**：它被允许看什么、调用什么、做什么？
- **G3 Human Control / Accountability**：人何时保留控制权、AI 何时自主、责任怎样配置？
- **G4 Trace / Audit / Lifecycle**：如何追溯、审计、变更和退役？

完整路线见 [`industry/ROADMAP.md`](industry/ROADMAP.md)。

厂商、产品、框架和案例只是路线上的观察样本，不是路线本身。

## 当前总假设

传统企业信息化主要由人理解业务世界，并通过 Application、Workflow 与组织分工组织数字能力。AI 时代开始出现新的智能主体，逐渐承担理解、判断、规划、能力发现、能力编排、执行与学习。

由此，一个值得长期验证的假设是：

**Intelligent Subject × Enterprise World Model × Capability Network × Real-world Feedback**

可能逐步构成企业持续演化的智能运行系统。

这只是当前研究假设，而不是既定结论。仓库会同时维护支持证据、反例和观点演进。

## 如何使用本仓库

### 给人看的“驾驶舱”

- [`NOW.md`](NOW.md)：当前研究焦点、卡点与下一步唯一动作
- [`JUDGMENTS.md`](JUDGMENTS.md)：目前值得保留的阶段性判断

### 给 AI 的长期上下文

- [`ai-context/PROJECT_CONTEXT.md`](ai-context/PROJECT_CONTEXT.md)：研究目标、边界、概念与研究纪律

### 理论与论文

- [`research/scholars.md`](research/scholars.md)：国内外重点学者地图
- [`research/theory-map.md`](research/theory-map.md)：经典组织理论与 AI 压力测试
- [`research/reading-list.md`](research/reading-list.md)：当前阅读路线
- `research/paper-reviews/`：原文精读、概念还原与七问研究映射

### 产业证据

- [`industry/README.md`](industry/README.md)：公开产业证据研究原则
- [`industry/ROADMAP.md`](industry/ROADMAP.md)：智能主体 Engineering × Governance 产业路线图
- [`industry/cases/`](industry/cases/)：公开企业实践案例
- [`industry/products/`](industry/products/)：产品机制、产品哲学与公司 AI 路线

### 长期主题

- [`topics/`](topics/)：五个长期组织问题 + 企业智能定义

## 双语策略

本仓库采用“**中文研究生产，成熟观点双语发布**”的方式：

- `NOW.md`、论文精读、研究过程、AI Context 等默认保留中文；
- README、企业智能定义、五个长期问题等对外成熟内容优先提供中英双语；
- 英文版不是机械翻译，而是面向国际研究者进行概念重写与学术化表达。

## 研究纪律

- **Q1–Q5 是问题地图；Theory 与 Public Industry Evidence 是公开证据线；不要混成一层。**
- 本公开仓不保存、引用或描述私人、客户、公司内部或非公开项目材料。
- 私人经验可以启发问题，但公开结论必须由公开来源独立支持。
- 不让教授论文垄断研究，也不让产业营销替代理论验证。
- 不以 MCP、RAG、Ontology、Agent、Harness 等技术名词无限增加一级框架。
- 区分 **长期问题 / 当前判断 / 演进假设 / 证据 / 反例**。
- 新技术首先用于修改已有问题的答案，而不是制造新的概念树。
- 技术架构必须尽量能够追溯到组织问题。
- 论文阅读坚持：**原文精读 → 概念还原 → 七问研究映射 → 人类吸收 → 是否更新 Judgment**。
- 产业研究坚持：**Product Fact / Claim → Public Case → Analyst / Policy / Counter Evidence → Q1–Q5 → Judgment**。

## 当前状态

仓库于 **2026-09-04** 初始化。当前仍在建立组织理论坐标系，同时已经形成以 **Intelligent Subject Engineering × Governance** 为主轴的公开产业研究路线。当前 Active Research Question 仍以论文理解为主，不因路线图建立而批量收集厂商案例。

---

This repository is a living research system rather than a finished framework. Claims will be revised as evidence changes.
