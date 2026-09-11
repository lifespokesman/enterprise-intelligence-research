# PRINCIPLES｜企业 AI 架构与方法原则库

> 本文件沉淀的不是论文观点，而是**经过问题牵引、机制理解、工程翻译与验证后，值得复用的架构 / 方法原则**。
>
> `JUDGMENTS.md` 回答“我们目前认为世界是怎样的”；本文件回答“如果这些判断成立，工程和研究应该怎样做”。

## 1. 状态

- **Candidate**：已有机制与工程含义，但验证不足；
- **Supported**：已有多类公开证据或可复核验证支持，仍保留边界；
- **Stable**：多轮问题与证据中持续成立，目前没有强反例；
- **Revised / Deprecated**：被新证据修改或不再采用。

原则不能因为“听起来合理”就升级。原则需要明确：问题、证据、工程含义、适用条件和反例。

## 2. 原则模板

```markdown
## AP-XXX / MP-XXX｜标题

Type: Architecture / Method  
Status: Candidate / Supported / Stable / Revised / Deprecated  
Origin: User Insight / External Trigger / Co-developed / AI Proposal

### Problem

### Principle

### Why

### Evidence

### Engineering / Method Implication

### Validation

### Boundary / Counter Evidence

### Related
```

---

# Method Principles｜研究与方法原则

## MP-001｜问题先于材料，原则先于论文数量

Type: Method  
Status: **Stable**  
Origin: `User Insight`

### Problem

如果把论文编号或阅读队列当成研究主线，容易出现“读完了一篇又一篇，但和真实工程问题连接很弱”，同时形成持续的学习债务。

### Principle

> **研究的基本单位是问题，不是论文。材料只有在帮助解释、设计或验证当前问题时才进入深度研究。**

主闭环：

`真实问题 → 理论 / 产业搜索 → 理解 → 工程翻译 → 小规模验证 → 架构 / 方法原则 → 新问题`

### Why

论文、产品、开源项目、案例都只是证据来源。最终要沉淀的是可复用的架构知识和方法原则，而不是资料收藏量。

### Evidence

- 当前研究过程中的效率与吸收问题；
- P-001 已完成理论理解，但应用问题仍需单独验证；
- `research/RESEARCH_LOOP.md` 对研究闭环的重新定义。

### Engineering / Method Implication

- 每篇论文先按当前问题判定 A / B / C；
- A 类精读，B 类定向理解，C 类只登记；
- 重要材料最终补 `Engineering Bridge`，而不是只写论文总结；
- 阅读数量不作为研究进度指标。

### Validation

后续用多个真实研究问题持续检验：是否减少无效精读、是否更快形成 Engineering Hypothesis 和可复用原则。

### Boundary / Counter Evidence

基础学科系统学习有时需要课程式连续阅读；本原则针对当前“企业 AI 架构 / 组织设计”问题导向研究，不否定系统性教育。

### Related

- `research/RESEARCH_LOOP.md`
- `research/paper-review-plan.md`
- `EVOLUTION.md`

---

# Architecture Principles｜架构原则

## AP-001｜从组织与业务问题反推工程和治理，不从技术组件反推企业架构

Type: Architecture / Method  
Status: **Supported**  
Origin: `Co-developed`

### Problem

Agent、MCP、RAG、Ontology、Harness 等技术变化快，如果直接以组件为一级架构，会把阶段性实现误当成长期不变量。

### Principle

> **先明确企业智能 / 组织问题，再推导主体关系、决策权、治理与工程实现。**

### Why

同一个组织问题可以由不同技术路线解决；长期稳定的是任务、协调、权限、责任、学习等问题，而不是当前框架名称。

### Evidence

- J-005；
- Q1–Q5 长期问题；
- Industry Roadmap 的 Engineering × Governance 结构。

### Engineering / Method Implication

技术选型前先回答：问题是什么、主体是谁、谁决策、谁负责、需要什么上下文、允许什么动作、如何反馈。

### Validation

继续用不同公开产品和架构路线检验：是否能够在不依赖具体厂商的情况下解释其工程机制。

### Boundary / Counter Evidence

底层基础设施仍有自己的技术约束；“问题反推”不意味着忽略性能、协议和实现现实。

### Related

- J-005
- `industry/ROADMAP.md`

---

## AP-002｜显式业务语义的强度应匹配任务复杂度，不默认所有 Agent 都需要完整 Ontology

Type: Architecture  
Status: **Candidate**  
Origin: `Co-developed`

### Problem

企业业务语义隐性、碎片化、散落在系统和人脑中，但“为所有 AI 任务建设完整本体”可能成本过高，也可能把当前技术形态误认为终局。

### Principle

> **按任务的跨系统程度、状态持续性、判断复杂度和行动风险，逐级选择 Retrieval / Context / Semantic Model / Operational Ontology / World Model。**

### Why

当前 Ontology 的价值主要来自填补通用模型与企业隐性业务语义之间的 Semantic Gap；长期稳定需求更可能是“可共享、可验证、可执行、可治理的企业世界表达”，而不是人工预建静态本体本身。

### Evidence

- EV-007；
- J-003 的弱证据判断；
- E2 Enterprise Context / World Model / Ontology。

### Engineering / Method Implication

不要以“是否有 Ontology”作为企业 AI 成熟度单一指标；先判断任务需要多强的显式语义与状态表达。

### Validation

需要公开产品机制、不同复杂度案例和替代路线比较；尤其验证低耦合任务是否无需 Ontology，高耦合持续行动任务是否显著受益。

### Boundary / Counter Evidence

模型直接处理非结构化信息、运行时证据链、动态校验等机制可能降低人工静态建模需求。

### Related

- EV-007
- J-003
- E2

---

## AP-003｜能力与授权必须同时成立，Agent 才能形成有效行动

Type: Architecture / Governance  
Status: **Candidate**  
Origin: `Co-developed`

### Problem

Agent“能调用某个工具”不等于“在当前业务条件下有权执行该动作”。

### Principle

`Effective Action = Business Validity ∩ Capability ∩ Authority`

### Why

业务规则决定动作是否合理，Capability 决定能否执行，Authority / Policy 决定该主体是否被允许执行。三者混在一起会导致越权或无法治理。

### Evidence

- 当前 Governance Roadmap G2；
- J-004 关于 Intent / Authority / Accountability 的探索判断。

### Engineering / Method Implication

- 区分 Business Rule 与 Governance Policy；
- Tool Registry 不能替代权限与策略系统；
- 高风险动作应支持审批、限制、审计和撤销 / 例外处理。

### Validation

需要公开 Agent Governance 产品事实、Policy / Standard 与案例验证。

### Boundary / Counter Evidence

低风险只读任务的治理强度可以显著降低；不能把高风险行动型 Agent 的治理模型机械套到所有 Copilot。

### Related

- J-004
- G2 / G3 / G4

---

## AP-004｜Agent Learning 不等于 Organizational Learning

Type: Architecture / Operating Model  
Status: **Candidate**  
Origin: `Co-developed`

### Problem

单个 Agent 在一次 Session 中获得反馈或调整行为，并不意味着企业形成了可复用、可治理的长期能力。

### Principle

> **只有运行经验经过提取、验证、治理并进入共享长期资产，才能称为组织学习。**

可能的资产包括 Knowledge、Skill、Rule、Dataset、Eval、Policy、World Model 和 Agent Definition。

### Why

如果经验只停留在模型上下文、单一 Trace 或个人操作中，下一次任务无法稳定复用，也无法形成组织层面的审计、比较和演进。

### Evidence

- Q5；
- P-001 对反馈与学习条件的理论启发；
- J-001 / E4 的现有研究假设。

### Engineering / Method Implication

Agent Runtime 后需要明确的 Observe → Evaluate → Candidate Change → Validate → Governed Promotion 机制，而不是把“有 Memory”当成组织学习。

### Validation

需要补组织学习理论、长期运行案例与产品机制。

### Boundary / Counter Evidence

并非所有经验都值得组织化；过度沉淀会造成知识污染、规则僵化和治理成本。

### Related

- Q5
- E4
- P-001

---

_Last updated: 2026-09-11_
