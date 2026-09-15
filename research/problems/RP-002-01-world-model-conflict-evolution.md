# RP-002-01｜Enterprise World Model Conflict & Evolution

Status: Open / Exploratory  
Created: 2026-09-15  
Parent: RP-002 Enterprise Data–Model Relationship  
Primary Track: E2 Enterprise Context / World Model  
Related: E4 Feedback-Evaluation-Evolution / Q3 Coordination / Q5 Organizational Learning

> 核心子问题：**当专家认知、既有本体、权威规则、运行事实和 AI 判断相互冲突时，企业应依据什么机制判断“哪个认知可以进入正式业务世界模型”，并安全地完成模型演化？**

本文件保存一个尚未收敛的研究问题。当前不把“可证伪企业世界模型”升级为架构原则，也不预设最终一定需要统一 Canonical Ontology。

---

## 1. Trigger｜问题来源

此前对企业本体建设形成过一个初步工作假设：

```text
专家业务认知
↓
人工定义本体骨架
↓
Agent 运行
↓
发现 Ontology Gap
↓
AI 提出候选补充
↓
人工审核
↓
本体持续完善
```

该路线隐含了一个未经验证的前提：

> **人工定义的本体骨架本身相对正确，并可以作为后续演化的稳定基准。**

但真实企业中可能同时存在多种互不一致的业务解释：

- 不同专家对对象、关系、状态、规则和流程的划分不同；
- 制度定义的流程与真实运行流程不同；
- 权威业务系统记录与一线人员经验不同；
- AI 从大规模运行数据中发现的模式与既有本体或专家判断不同。

因此问题从：

> “本体应该由人建设还是由 AI 建设？”

进一步转变为：

> **企业如何判断自己当前对业务世界的描述是否仍然成立？**

---

## 2. Cognition Change｜认知变化

### Before

人工定义的 Ontology 被隐含地视为业务世界的基准模型，Agent 运行主要用于发现缺口并补充该模型。

### Now

当前更谨慎的认识是：

> **人工本体、专家经验、制度规则和 AI 模型都不是企业世界本身，而是不同主体对企业世界形成的模型、约束或解释。**

可暂时表示为：

```text
专家认知
        ↘
既有本体 → 真实业务运行 ← AI 模型判断
        ↗
制度 / 权威规则
```

它们可能一致，也可能发生冲突。

因此，本体演化不能简单采用“人定义，AI 补充”，而需要进一步研究：

> **冲突如何暴露、证据如何形成、谁拥有裁决权，以及什么认知最终有资格进入生产业务模型。**

---

## 3. Core Question｜核心研究问题

> **当专家定义的业务认知、现有本体模型、权威业务数据、真实运行轨迹以及 AI 模型判断相互冲突时，企业级 AI 系统应依据什么机制判断“哪个认知应该进入正式业务世界模型”，并安全地完成模型演化？**

该问题关注的不是一般意义上的“AI 和人谁更准确”，而是：

> **Enterprise World Model Conflict & Evolution：企业世界模型的冲突发现、证据裁决与演化机制。**

---

## 4. Why It Matters｜为什么重要

如果不存在这一机制，AI-native Ontology / Enterprise World Model 可能走向两个极端。

### 风险 A｜人工本体成为不可挑战的先验

```text
专家定义世界
↓
AI 只能按照既有世界运行
↓
现实与本体不一致
↓
继续修改 AI 去适应本体
```

结果可能是把错误、局部或已经过时的业务认知长期固化。

### 风险 B｜AI 发现被直接升级为业务真理

```text
AI 发现新的相关关系
↓
自动修改对象 / 关系 / 规则
↓
进入生产
```

统计相关、数据偏差、异常样本或模型误判可能被错误升级成正式业务知识。

因此企业世界模型需要同时避免：

- **专家永远正确**；
- **数据 / AI 发现即真理**。

---

## 5. Working Hypothesis v0.1｜当前工作假设

> **企业业务本体不应被视为企业世界的最终真相，而应被视为一个可版本化、可被运行事实持续挑战的“当前最佳可执行模型”。**

其演化可能需要由以下因素共同决定：

> **知识类型 × 权威来源 × 运行证据 × 变更治理**

当前先区分四类知识，不视为最终分类：

| 知识类型 | 示例 | 初步权威来源 |
|---|---|---|
| 规范性 | 谁有审批权、什么状态允许放行 | 法规、制度、责任主体 |
| 事实性 | 当前任务是否完成、设备实际状态 | 原始证据、权威业务系统 |
| 描述性 | 业务实际上如何运行、通常经过哪些环节 | Runtime Trace + 业务验证 |
| 推断性 | 哪些因素代表风险、什么模式预示故障 | 数据验证 + 模型 + 专家判断 |

因此可能的机制不是：

```text
Human > AI
```

也不是：

```text
AI > Human
```

而更像：

```text
现有世界模型
    ↓
Expected World

真实业务运行
    ↓
Observed World

Expected ≠ Observed
    ↓
产生 Model Conflict
    ↓
识别冲突知识类型
    ↓
收集对应权威来源与证据
    ↓
形成 Model Change Proposal
    ↓
验证 / 影响分析 / 责任主体审核
    ↓
新版本业务世界模型
```

状态：**Working Hypothesis，不进入 PRINCIPLES.md。**

---

## 6. Open Questions｜尚未想清的问题

### CQ-002-06｜什么才算“世界模型冲突”？

不是所有 AI 判断与人工判断不同都意味着 Ontology 错误。

至少需要区分：

- Data Gap；
- Ontology Gap；
- Rule Gap；
- Tool Gap；
- Model Error；
- Human Error；
- Process Exception。

当前尚无稳定诊断方法。

### AQ-002-04｜企业世界是否真的需要唯一 Canonical Ontology？

不同岗位、部门和任务可能天然需要不同视角。

需要验证：

> **Shared Core + Domain View**

是否比“大一统企业本体”更合理，以及共享核心应该稳定到什么程度。

### CQ-002-07｜什么情况下运行事实有资格挑战人工本体？

例如 1000 次流程中 800 次没有按照制度流程执行，这可能意味着：

- 本体错误；
- 制度与现实脱节；
- 现场长期违规；
- Trace 本身存在采集偏差。

因此高频事实本身不能自动决定规范模型如何变化。

### VQ-002-01｜AI 发现达到什么证据门槛，才值得形成 Model / Ontology Change Proposal？

候选指标包括：

- 出现次数；
- 统计显著性；
- 跨时间稳定性；
- 跨场景稳定性；
- 对业务结果的解释或改善；
- 可复现性；
- 专家认可度；
- 与权威规则的一致 / 冲突程度。

当前不知道这些指标如何组合，也不预设存在单一通用阈值。

### GQ-002-01｜谁拥有最终裁决权？

需要进一步明确 Domain Expert、Ontology Owner、业务负责人、数据负责人、模型 / Agent 系统分别应该拥有什么权限。

尤其要区分：

- 提出候选变更；
- 提供证据；
- 技术验证；
- 业务影响评估；
- 审核；
- 批准进入生产；
- 回滚。

---

## 7. Diagnostic Direction｜一个待验证的诊断方向

后续不应把所有 `Expected ≠ Observed` 都归为 Ontology Gap，而应先做冲突诊断。

候选诊断链：

```text
Observed ≠ Expected
        ↓
证据是否可信？
        ├─ 否 → Data / Trace Problem
        ↓ 是
现有规则是否明确覆盖？
        ├─ 是但未执行 → Process / Human / Tool Problem
        ↓ 否
现有 Ontology 是否能表达该对象 / 状态 / 关系 / 事件？
        ├─ 否 → Ontology Gap Candidate
        ↓ 是
推断是否稳定可复现？
        ├─ 否 → Model Error / Noise
        ↓ 是
形成 Model Change Proposal Candidate
```

这只是 **Diagnostic Hypothesis v0.1**，需要真实案例验证。

---

## 8. Relation to Parent Problem｜与上层问题的关系

本问题不替代 RP-002，而是 RP-002 中关于 `Semantic / Ontology / Enterprise World Representation` 的进一步下钻。

```text
RP-002：
企业真实世界如何通过 Data / Knowledge / Fact / Semantic / Context / Eval / Feedback
进入 Model / Agent？
│
└─ RP-002-01：Enterprise World Model Conflict & Evolution
   │
   ├─ 初始世界模型如何构建？
   ├─ 多场景如何沉淀共享业务模型？
   ├─ Agent 如何基于世界模型理解与行动？
   └─ 当专家、本体、事实与 AI 冲突时，模型何时以及如何改变？
```

它直接承接 RP-002 中已有的工程问题：

> `EQ-002-05：Ontology / Semantic Model 应由专家建设、AI 自动发现还是运行时动态生成？如何校验？`

但把研究重点从“由谁建设”推进到了：

> **不同认知来源发生冲突时，怎样诊断、形成证据、裁决并治理变更。**

---

## 9. Minimum Research Goal｜当前最小研究目标

暂时不设计完整的“企业世界模型治理体系”。

下一步只验证一个更小的问题：

> **真实 Agent 运行中，是否会稳定出现“现有业务模型无法解释现实”的冲突案例？**

如果存在，再继续验证：

1. 冲突是否可以归纳出稳定类型；
2. 每类冲突依赖什么证据裁决；
3. 哪些冲突最终会导致 Ontology / World Model 修改；
4. 哪些冲突实际属于模型、数据、工具、流程或人员问题。

只有这一步成立，才继续发展完整的“本体冲突与演化机制”假设。

---

## 10. Evidence Plan｜下一步证据方向

第一轮优先寻找能够直接观察“模型与现实发生冲突”的公开证据，而不是先找宏观 Ontology 方法论。

优先证据：

- 有持续模型 / 规则演化机制的企业软件或知识图谱产品；
- Palantir Ontology、数字孪生、Process Mining、Knowledge Graph Evolution 等公开机制；
- 运行 Trace 与制度流程不一致的案例；
- Ontology Learning / Ontology Evolution / Schema Evolution 研究；
- Human-in-the-loop Knowledge Base / Model Governance 机制；
- Counter Evidence：强模型是否可以在不维护稳定 Ontology 的条件下，通过 Runtime Context 动态适应变化。

研究时继续标注证据身份：

`[Theory] / [Product Fact] / [Product Claim] / [Industry Case] / [Open Source] / [Counter Evidence]`

---

## 11. Stop Condition｜当前停止点

当前只记录到以下程度：

- 问题已经从“人建还是 AI 建”推进为“多种认知冲突如何裁决”；
- 已形成一个可验证的 Working Hypothesis；
- 已明确最小验证目标；
- 尚无足够证据升级为 Architecture Principle。

下一次恢复研究时，从下面这个问题开始：

> **寻找 3–5 个真实系统中 `Expected World ≠ Observed World` 的案例，并判断它们最终是 Ontology Gap、Rule Gap、Data Gap、Model Error、Human Error 还是 Process Exception。**

在完成这一步之前，不继续扩展完整治理框架。
