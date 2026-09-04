# Industry Research Roadmap｜产业研究路线图 v0.1

> 目标：研究“企业智能主体真正进入企业以后，产业界必须解决哪些长期工程与治理问题”。
>
> 本路线图不按厂商划分。公司、产品、框架和案例只是观察样本；真正的路线由工程问题和治理问题定义。

## 1. 总体结构

产业研究采用两条长期主线：

- **Track E｜Intelligent Subject Engineering｜智能主体工程**：如何把模型能力变成能够持续工作、理解企业、采取行动并不断演化的智能主体；
- **Track G｜Intelligent Subject Governance｜智能主体治理**：如何定义其身份、授权边界、人类控制与责任，并对其全生命周期进行追踪、审计和约束。

```text
                    Enterprise Intelligent Subject
                           企业智能主体
                                  │
               ┌──────────────────┴──────────────────┐
               │                                     │
       Engineering Track                       Governance Track
          智能主体工程                              智能主体治理
               │                                     │
     E1 → E2 → E3 → E4                   G1 → G2 → G3 → G4
     生产   理解   行动   演化               身份   权限   人控   追溯
     运行   世界   能力   学习               归属   策略   责任   生命周期
```

这八条不是八个独立产品模块，而是长期研究问题。具体技术名称会变化，问题本身需要持续验证。

---

# Track E｜Intelligent Subject Engineering

## E1｜Agent Production / Harness / Runtime

### 母问题

> **模型怎样从一次调用能力，变成能够围绕目标持续工作的智能主体？**

当前关注的演进链：

```text
Model Call
   ↓
Tool Use
   ↓
Workflow
   ↓
Agent Loop
   ↓
Harness
   ↓
Stateful Runtime
   ↓
Long-running Intelligent Subject
```

重点研究对象：

- Agent Definition：Role / Goal / Task / Skill / Tool / Memory / Context；
- Harness：谁控制连续推理、工具调用、观察、继续与停止；
- Runtime：Task / Session / State / Checkpoint / Sandbox / Recovery；
- Production：Define / Assemble / Bind / Evaluate / Release；
- Framework 与企业级 Runtime 的边界。

长期需要守住的概念边界：

> Agent ≠ Harness  
> Harness ≠ Runtime  
> Runtime ≠ Kubernetes  
> Agent Framework ≠ Enterprise Agent Runtime

### 希望最终回答

企业级智能主体的最小生产与运行模型是什么？哪些能力是长期基础设施，哪些只是当前框架实现？

---

## E2｜Enterprise Context / World Model / Ontology

### 母问题

> **一个通用智能主体怎样理解一家具体企业此时此刻的现实？**

当前观察的可能演进：

```text
Documents / Search
        ↓
RAG / Knowledge
        ↓
Context Engineering
        ↓
Semantic Context
        ↓
Operational Ontology
        ↓
Enterprise World Model ?
```

重点研究对象：

- Data / Document / History；
- Object / Relation；
- State / Transition；
- Event；
- Business Rule；
- Action；
- Task Context；
- Permission-aware Context；
- Context Compilation；
- Human-built Ontology 与 AI-discovered / Human-governed World Model 的边界。

本路线不预设“所有企业都需要 Ontology”。需要持续验证不同任务复杂度与世界表达强度之间的关系，例如：

```text
简单知识任务
→ Retrieval 是否足够？

复杂任务上下文
→ 是否需要 Context Engineering？

跨系统、跨对象持续判断
→ 是否需要 Semantic Model？

持续观察并作用现实
→ 是否需要 Operational World Model？
```

### 希望最终回答

智能主体在什么任务条件下需要何种强度的企业上下文与世界表达？Shared Enterprise World Model 在哪些场景是必要基础设施，哪些场景只是过度设计？

---

## E3｜Capability / Action Infrastructure

### 母问题

> **智能主体理解企业以后，怎样真正作用于企业世界？**

传统企业软件主要存在 Human Interface：

```text
Human
 ↓
UI
 ↓
Application
 ↓
Business Logic
```

智能主体可能增加 Agent Interface：

```text
Agent
 ↓
Capability Discovery
 ↓
Tool / API / MCP / Workflow / CLI / Event
 ↓
Enterprise Software / Assets
```

重点研究对象：

- API / Tool / MCP / CLI / SQL / Workflow；
- Event / Action；
- Capability Registry；
- Capability Discovery；
- Capability Composition；
- Application 与 Capability 的关系；
- 软件能力与物理资产行动接口的边界。

当前谨慎假设：

> Application 不会简单消失，但企业软件可能越来越同时提供 Human Interface 与 Agent Interface。

### 希望最终回答

Agent 时代企业能力应如何暴露、发现、组合和执行？“Application → Capability-oriented”到底是一种局部演进还是更广泛的软件结构变化？

---

## E4｜Feedback / Evaluation / Evolution

### 母问题

> **Agent 完成一次任务以后，企业有没有因此变得更聪明？**

目标不是让每个 Agent 单独“越用越聪明”，而是研究运行经验如何成为组织级长期资产：

```text
Agent Run
   ↓
Trace / Evidence
   ↓
Outcome / Failure
   ↓
Human Feedback
   ↓
Pattern
   ↓
Candidate Improvement
   ↓
Evaluation
   ↓
Governed Promotion
   ↓
Knowledge / Skill / Rule / Eval / Policy / World Model
```

重点研究对象：

- Trace 与 outcome capture；
- Human feedback；
- Eval / Benchmark；
- Failure taxonomy；
- Candidate change；
- Validation；
- Governed promotion；
- Knowledge / Skill / Rule / Ontology / Policy 的演化。

### 希望最终回答

Agent Learning 与 Organizational Learning 之间缺少哪些工程机制？企业怎样避免运行经验停留在孤立 Session 中？

---

# Track G｜Intelligent Subject Governance

治理不是 Agent 完成以后再审核，而应从主体定义开始贯穿生产、发布、运行和演化。

```text
Define → Build → Evaluate → Release → Run → Observe → Evolve
   │        │         │         │        │       │
   └──────────────── Governance ────────────────┘
```

## G1｜Identity / Ownership

### 母问题

> **这个智能主体是谁，属于谁，谁对它的存在负责？**

重点研究对象：

- Agent Identity；
- Purpose；
- Owner；
- Producer；
- User / Delegator；
- Business Owner；
- Version；
- Lifecycle State。

### 希望最终回答

企业怎样把 Agent 从“一个技术实例”变成具有明确身份、归属和生命周期责任的治理对象？

---

## G2｜Authority / Policy

### 母问题

> **一个 Agent 有能力做某件事，不代表它有权做。企业如何把授权变成可执行约束？**

当前公式：

> **Effective Agency = Capability ∩ Authority**

进一步：

> **Effective Action = Business Validity ∩ Capability ∩ Authority**

重点研究对象：

- Data Permission；
- Tool Permission；
- Action Permission；
- Scope；
- Role；
- Quota；
- Risk Policy；
- Context Policy；
- Time / Environment Constraints；
- Policy Enforcement。

### 希望最终回答

Authority、Business Rule 与 Capability 怎样在 Runtime 中共同决定一个 Agent 此刻“能不能做这件事”？

---

## G3｜Human Control / Accountability

### 母问题

> **AI 自主性提高以后，人应该在哪些位置保留什么控制权，并承担什么责任？**

研究重点不是泛化的 Human-in-the-loop，而是不同任务、风险和责任条件下的控制模式：

```text
AI Suggest
Human Decide

      ↓

AI Decide
Human Confirm / Veto

      ↓

AI Execute
Human Monitor

      ↓

AI Autonomous
Human Exception Handling
```

重点研究对象：

- Approval；
- Review；
- Confirmation；
- Veto；
- Override；
- Escalation；
- Kill Switch；
- Decision Rights；
- Accountability Allocation。

长期边界：

> **Decision Rights ≠ Accountability**

决定、授权、监督和承担后果可能由不同主体承担，必须分别研究。

### 希望最终回答

Human 与 AI 的决策权、控制权、授权权和责任怎样动态配置，而不是简单采用“人在环中/不在环中”的二元设计？

---

## G4｜Trace / Audit / Lifecycle

### 母问题

> **企业怎样知道 Agent 做过什么、依据什么做、出了问题如何追溯，以及什么时候应该变更或退役？**

重点研究对象：

- Input / Context；
- Model / Agent Version；
- Tool Call；
- Action；
- Result；
- Policy Decision；
- Human Approval；
- Evidence；
- Trace；
- Audit；
- Change / Re-evaluation / Retirement。

治理生命周期可以暂时表示为：

```text
Register / Define
      ↓
Risk Classify
      ↓
Evaluate
      ↓
Approve
      ↓
Release
      ↓
Monitor / Audit
      ↓
Change / Re-evaluate
      ↓
Retire
```

### 希望最终回答

企业需要怎样的证据链和生命周期机制，才能让大量智能主体长期运行而仍然可追溯、可审计、可变更、可退役？

---

# 2. 四阶段压缩视图

八条路线可以压缩为四个更容易理解的阶段：

| 阶段 | Engineering | Governance | 核心问题 |
|---|---|---|---|
| **Phase 1 主体成立** | E1 Production / Harness / Runtime | G1 Identity / Ownership | 我们究竟生产了一个什么主体？ |
| **Phase 2 进入企业世界** | E2 Context / World Model | G2 Authority / Policy | 它知道什么现实，又被允许接触什么现实？ |
| **Phase 3 开始行动** | E3 Capability / Action | G3 Human Control / Accountability | 它能做什么，什么时候可自主做，人何时必须介入？ |
| **Phase 4 规模化与演化** | E4 Feedback / Evaluation / Evolution | G4 Trace / Audit / Lifecycle | 大量 Agent 长期运行后，企业怎样学习、治理和持续演化？ |

因此可以把整条产业路线记成：

> **主体成立 → 理解企业 → 作用企业 → 企业学习**

同时治理始终伴随：

> **身份 → 权限 → 人类控制与责任 → 追溯与生命周期**

---

# 3. 厂商、产品与案例的位置

公司不是路线，产品不是路线，技术热词也不是路线。

它们统一作为 **Observation Targets｜产业观察样本**，按当前 Active Research Question 选择。

每个产业对象优先回答：

1. 它主要落在哪些 E/G Track？
2. 对应 Q1–Q5 哪些长期问题？
3. `[Product Fact]`：它实际上做了什么？
4. `[Product Claim]`：它为什么认为应该这样做？
5. `[Industry Case]`：公开企业实践中发生了什么？
6. `[Analyst View]`：独立分析机构如何评价？
7. `[Policy / Standard]`：存在什么制度或标准约束？
8. `[Counter Evidence]`：哪里失败、哪里不需要、哪里有替代路线？
9. 是否足以影响 Hypothesis / Judgment？

不按厂商热度批量建卡，只在某个对象能帮助回答当前问题时研究。

---

# 4. 与 Academic Track 的连接

Academic Track 主要回答：

> **为什么？机制是什么？**

Industry Track 主要回答：

> **产业界正在怎样工程化？真实公开实践是否支持？**

二者最终通过 Q1–Q5 汇合：

```text
Theory
   ↓
Organizational Mechanism
   ↓
Industry Engineering / Governance Mechanism
   ↓
Product / Case / Analyst / Policy / Counter Evidence
   ↓
Hypothesis
   ↓
Judgment
   ↓
Engineering / Governance Implication
```

当产业界出现理论坐标无法解释的新机制时，再回到理论线补充新的经典理论或新研究，而不是直接制造新的一级概念。

---

# 5. 执行纪律

1. **ROADMAP 是地图，不是 TODO List。** 同一时期只激活与当前问题最相关的一条产业研究线。
2. 当前不因新增路线图而批量研究厂商。
3. 所有公共结论必须能够由公开来源独立支持。
4. Product Claim 不得替代独立验证。
5. Analyst View 不等于 Academic Theory。
6. 公开成功案例必须同时寻找边界条件和反例。
7. 当前技术名词可以作为实现机制，但不得自动升级为长期架构层。
8. 任何产业结论最终都应回到 Q1–Q5，而不是另建一套顶层问题体系。

_Status: v0.1 / 2026-09-04_