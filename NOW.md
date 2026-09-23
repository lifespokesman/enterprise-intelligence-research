---
view: "human_research_dashboard"
problem_family: "RP-002"
frontier: "RP-002-01"
---

# NOW｜当前研究驾驶舱

Updated: 2026-09-23

> 本文件只回答：**现在研究什么、为什么是它、下一步只做什么。**
>
> 长期研究地图与问题族关系见 [`RESEARCH_MAP.md`](RESEARCH_MAP.md)。详细问题树见 [`research/research-questions.md`](research/research-questions.md)。

---

## 1. Current Theme｜当前长期主题

**Q3｜Human-Agent 的协调机制**

当前聚焦：**企业世界表达、World Model 一致性，以及 Shared Context / Enterprise World Model 作为 Human-Agent 协调基础的作用。**

当前研究不是一般的数据治理问题，而是：

> 企业真实世界如何进入 Model / Agent，并在持续运行中保持与现实一致。

---

## 2. Current Problem Family｜当前问题族

**RP-002｜Enterprise Data–Model / World Relationship**

核心问题：

> 企业已有的数据、知识、规则、系统与运行事实，怎样转化为 Model / Agent 可理解、可调用、可验证、可持续更新的企业上下文与世界模型？

状态：**Active**

详细问题卡：[`research/problems/RP-002-enterprise-data-model-relationship.md`](research/problems/RP-002-enterprise-data-model-relationship.md)

---

## 3. Current Frontier｜当前唯一研究前沿

**RP-002-01｜Enterprise World Model Conflict & Evolution**

> **当专家认知、既有本体、权威规则、运行事实和 AI 判断相互冲突时，企业应依据什么机制判断“哪个认知可以进入正式业务世界模型”，并安全地完成模型演化？**

当前认知变化：

```text
原问题：本体应该由人建设还是由 AI 建设？
        ↓
工作假设：人定义骨架，AI 在运行中发现缺口并完善
        ↓
新问题：人工骨架本身也可能错误、局部或过时
        ↓
当前前沿：企业如何判断自己当前对业务世界的描述是否仍然成立？
```

问题卡：[`research/problems/RP-002-01-world-model-conflict-evolution.md`](research/problems/RP-002-01-world-model-conflict-evolution.md)

---

## 4. Current Working Hypothesis｜当前工作假设

> **企业业务本体 / 世界模型不应被视为企业世界的最终真相，而应被视为一个可版本化、可被运行事实持续挑战的“当前最佳可执行模型”。**

候选演化机制：

```text
现有世界模型
    ↓
Expected World

真实业务运行
    ↓
Observed World

Expected ≠ Observed
    ↓
Model Conflict
    ↓
先判断冲突类型
    ↓
Data / Ontology / Rule / Model / Human / Tool / Process ?
    ↓
收集对应证据
    ↓
Model Change Proposal
    ↓
验证 / 影响分析 / 审核
    ↓
新版本世界模型
```

状态：**Working Hypothesis，不进入 JUDGMENTS / PRINCIPLES。**

---

## 5. Next Action｜下一步只做这一件事

> **寻找 3–5 个公开的 `Expected World ≠ Observed World` 案例，并尝试建立第一版冲突分类。**

优先证据：

- Process Mining：制度流程与真实运行流程不一致；
- Ontology / Knowledge Graph Evolution；
- 数字孪生：模型状态与现场状态漂移；
- Human-in-the-loop Knowledge / Model Governance；
- Palantir Ontology 或类似产品中的模型变更机制；
- Counter Evidence：不维护稳定 Ontology 也能持续适应现实的 Agent 方式。

当前**不做**：

- 不继续扩展完整企业世界模型治理体系；
- 不同时推进 RP-002 下所有 RQ；
- 不先证明 Ontology 是正确答案；
- 不把 Working Hypothesis 提前升级为 Principle。

---

## 6. Stop Condition｜这一轮什么时候停

第一轮案例收集后，只判断三件事：

1. 是否稳定存在“现有业务模型无法解释现实”的冲突；
2. 冲突是否能形成相对稳定的类型；
3. 哪些冲突最终真的要求 World Model / Ontology 修改，哪些其实属于数据、模型、流程、工具或人员问题。

如果这三点不能成立，当前假设应被修正，而不是继续扩写。

---

## 7. Backlog｜重要但暂不推进

- Data → Model / Agent Relationship Types；
- Dataset / RAG / SQL / API / Tool / Ontology / Context / Eval / Feedback 的机制边界；
- 不同企业起点下 AI Context 的建设路径；
- AI Context Readiness Diagnostic；
- Canonical Ontology vs Shared Core + Domain View；
- Model Change 最终裁决权与治理角色。

这些内容继续保留在 RP-002 详细问题中，但**不构成当前 Next Steps**。

---

## 8. Resume Here｜下次从这里恢复

> **Current Problem Family**：RP-002 Enterprise Data–Model / World Relationship  
> **Current Frontier**：RP-002-01 Enterprise World Model Conflict & Evolution  
> **Working Hypothesis**：世界模型是可被现实持续挑战的“当前最佳可执行模型”，不是最终真相。  
> **Next Action**：找 3–5 个 `Expected World ≠ Observed World` 的公开案例，先做冲突分类。  
> **Do Not Expand Yet**：暂不建设完整治理体系，不同时展开全部 RP-002 子问题。
