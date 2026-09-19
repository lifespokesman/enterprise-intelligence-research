# RESEARCH_MAP｜长期研究地图

Updated: 2026-09-16

> 本文件只回答三个问题：**长期在研究什么？每条主线当前推进到哪里？当前真正的研究前沿是什么？**
>
> 它不是完整问题数据库，也不保存所有对话灵感。详细问题、假设、证据与验证仍放在 `research/` 下。

---

## 1. 使用原则

仓库采用四层轻量结构：

```text
Research Theme
长期研究主题（Q1–Q5）
        ↓
Problem Family
阶段性问题族（RP）
        ↓
Evolution
问题与认知如何发生变化
        ↓
Frontier
当前唯一值得继续推进的前沿
```

核心纪律：

1. **Signal 不等于 Problem**：临时想法不立即升级为正式研究问题；
2. **Problem 不等于 Active Problem**：同时只保留一个主要 Active Problem Family；
3. **一个问题族只有一个 Frontier**：避免同时维护过多“下一步”；
4. **只有认知真正发生变化才写 EVOLUTION**：不把普通讨论都变成维护任务；
5. **问题库优先变深，不优先变大**：能归入既有 Problem Family 的新问题，不新增母问题。

---

## 2. Long-term Research Themes｜长期研究主题

| Theme | 长期问题 | 当前关联问题族 |
|---|---|---|
| **Q1** | Human 与 AI 应如何重新分工、配置决策权与责任？ | RP-001 / RP-004 |
| **Q2** | Agent 如何获得持续判断、行动与工具调用能力，同时保持边界？ | RP-004 |
| **Q3** | AI 如何获得对企业真实世界的可计算、可验证理解？ | **RP-002** |
| **Q4** | AI 降低能力发现与协调成本后，企业能力边界如何变化？ | RP-005 |
| **Q5** | Agent 的局部经验如何转化为组织长期学习与演化能力？ | RP-003 / RP-002 |

Q1–Q5 是长期坐标，不因单次项目、论文或对话频繁变化。

---

## 3. Problem Families｜问题族

| Problem Family | 核心问题 | 状态 | 当前 Frontier |
|---|---|---|---|
| **RP-001 Human–AI Decision Structure** | Human 与 AI 的分工、聚合、最终决策权与反馈如何设计？ | Paused | 暂无；等待新的真实任务触发 |
| **RP-002 Enterprise Data–Model / World Relationship** | 企业真实世界如何通过 Data / Knowledge / Semantic / Context / Feedback 进入 Model / Agent，并持续保持与现实一致？ | **Active** | **RP-002-01 World Model Conflict & Evolution** |
| **RP-003 Agent Organizational Learning** | Agent 的局部运行经验如何沉淀为可保留、可复用、可验证的组织能力？ | Candidate | 暂无 |
| **RP-004 Agent Capability & Authority** | Agent 能调用工具后，能力、权限、人控、责任怎样组合？ | Candidate | 暂无 |
| **RP-005 Enterprise Capability Boundary** | 哪些能力应内部化，哪些可以由 AI 动态发现和外部调用？ | Backlog | 暂无 |

详细问题树仍见 [`research/research-questions.md`](research/research-questions.md)。

---

## 4. Current Evolution｜当前最重要的认知演进

RP-002 当前已经发生一次关键推进：

```text
问题 A：企业本体应该由人还是 AI 建？
        ↓
工作假设：人定义业务骨架，AI 在运行中发现缺口并持续完善
        ↓
新冲突：人工定义的骨架本身也可能错误、局部或过时
        ↓
问题 B：专家、本体、规则、运行事实、AI 判断冲突时，以谁为准？
        ↓
当前前沿：企业如何识别世界模型失效，并依据证据安全地完成模型演化？
```

这意味着研究重点正在从：

> **Ontology Construction｜如何构建企业本体**

推进到：

> **World Model Validation & Evolution｜如何判断企业对业务世界的描述是否仍然成立，以及何时应该改变。**

完整认知变化记录见 [`EVOLUTION.md`](EVOLUTION.md)，当前问题卡见 [`research/problems/RP-002-01-world-model-conflict-evolution.md`](research/problems/RP-002-01-world-model-conflict-evolution.md)。

---

## 5. Current Frontier｜当前唯一研究前沿

### RP-002-01｜Enterprise World Model Conflict & Evolution

> **当专家认知、既有本体、权威规则、运行事实和 AI 判断相互冲突时，企业应依据什么机制判断“哪个认知可以进入正式业务世界模型”，并安全地完成模型演化？**

### Why Now

原先的“人工定义骨架 + AI 运行完善”隐含假设：人工骨架相对正确。

当前研究认为这个前提本身需要被验证，因此不能继续只研究“AI 怎样补本体”，而应先研究：

> **Expected World ≠ Observed World 时，究竟是 Data、Ontology、Rule、Model、Human、Tool 还是 Process 出了问题？**

### Next Action

只做一件事：

> **寻找 3–5 个公开的“现有业务模型 / 规则无法解释真实运行”的案例，并尝试建立第一版冲突分类。**

优先方向：

- Process Mining 中制度流程与实际流程冲突；
- Ontology / Knowledge Graph Evolution；
- 数字孪生模型与现场状态漂移；
- Human-in-the-loop Knowledge / Model Governance；
- Palantir Ontology 或类似产品如何处理模型变更；
- Counter Evidence：无需稳定 Canonical Ontology 也能长期运行的 Agent 架构。

### Stop Condition

在第一轮案例之前，暂时不继续扩展完整“企业世界模型治理体系”。

第一轮只判断：

1. 是否稳定存在 `Expected ≠ Observed` 的真实冲突；
2. 冲突能否被区分为 Data / Ontology / Rule / Model / Human / Tool / Process 等类型；
3. 哪些冲突最终真的要求 World Model / Ontology 发生变化。

---

## 6. Backlog｜不是当前要做的事

以下问题仍然重要，但暂时不与 Frontier 并行推进：

- RP-002 的 Data → Model / Agent Relationship Types；
- Dataset / RAG / SQL / API / Tool / Ontology / Context / Eval / Feedback 的机制边界；
- 不同企业数字化起点下的 AI Context 建设路径；
- AI Context Readiness 的诊断框架；
- Canonical Ontology vs Shared Core + Domain View；
- 谁拥有最终模型变更裁决权。

它们进入 Backlog，不代表删除；只有当前 Frontier 产生新证据后，再决定是否提升。

---

## 7. 仓库导航

- [`NOW.md`](NOW.md)：当前研究驾驶舱，只保留“现在在哪里、下一步做什么”；
- [`RESEARCH_MAP.md`](RESEARCH_MAP.md)：长期研究地图、问题族与当前 Frontier；
- [`EVOLUTION.md`](EVOLUTION.md)：只记录真正改变问题定义、假设或研究方向的认知变化；
- [`research/research-questions.md`](research/research-questions.md)：详细问题树与历史问题内容；
- [`research/problems/`](research/problems/)：重要 Problem / Subproblem 的详细问题卡；
- [`JUDGMENTS.md`](JUDGMENTS.md)：阶段性稳定判断；
- [`PRINCIPLES.md`](PRINCIPLES.md)：经过证据与验证后可复用的架构 / 方法原则。

---

## 8. 新问题准入规则

出现新想法时，先问：

```text
这个新想法改变了哪个已有判断？
        ↓
能否归入已有 Problem Family？
    ├─ 能 → 更新问题卡 / EVOLUTION，必要时改变 Frontier
    └─ 不能 → 先作为 Signal 暂存
                 ↓
        是否反复出现 / 影响架构 / 需要持续证据？
                 ↓
             再决定是否升级为 RP
```

只有满足至少两项，才建议升级为新的正式 Problem Family：

- 在不同项目或讨论中反复出现；
- 会改变架构、治理或产品设计；
- 需要持续外部证据才能判断；
- 能形成可验证的工程假设；
- 无法合理归入现有 Problem Family。

> **问题可以无限产生，但正式研究问题必须有限；仓库应越来越深，而不是越来越大。**
