# Paper Map｜问题目录、论文位置与阅读选择

Updated: 2026-09-11  
本文件是论文登记与选文的统一入口。当前动作以 [NOW](../NOW.md) 为准；研究方法见 [RESEARCH_LOOP](RESEARCH_LOOP.md)；论文 A/B/C 与执行方式见 [paper-review-plan](paper-review-plan.md) 和 [PAPER_READING_MODE](../ai-context/PAPER_READING_MODE.md)。

> **本文件是 Evidence Index，不是 Reading Queue。**

这里的 Q / M / R 映射属于选文定位，用于说明为什么考虑某篇，不等于作者结论，也不证明论文支持项目判断。论文编号是身份，不是优先级。

## 1. 几张地图各自回答什么

| 入口 | 职责 |
|---|---|
| Q1–Q5 与 [research-questions](research-questions.md) | 当前真正要解决什么 Concrete Problem、哪个问题还没有答案 |
| [RESEARCH_LOOP](RESEARCH_LOOP.md) | Problem 如何经过 Evidence、Engineering Hypothesis、Validation 进入 Principle |
| M1–M6 [theory-map](theory-map.md) | 用哪些经典理论理解问题 |
| 本文 | 每篇论文可能填补什么、证据是什么、是否值得现在读 |
| [industry/ROADMAP](../industry/ROADMAP.md) | 理论之外，还需哪些公开工程与治理证据 |
| [PRINCIPLES](../PRINCIPLES.md) | 哪些工程 / 方法原则正在形成、验证或修正 |

学者地图用于寻找理论来源，不承担阅读顺序。

## 2. 按长期问题看的论文证据位置

“已有”只表示本仓当前登记或精读情况，不宣称全领域没有其他研究。

| 方向 | 需要逐步弄懂的具体问题 | 理论入口 | 当前论文位置 | 当前缺口 |
|---|---|---|---|---|
| **Q1 决策权** | 谁更适合判断？何时专业化、何时聚合？能力优势如何与最终决定权区分？ | M1 有限理性；M2 分工；M3 权限；M5 AI 主体 | P-001 已提供基础框架；P-002 可补管理者工作 / purpose / normative boundary；P-005 可补聚合条件 | 还不能从模型准确率直接推出授权；缺少任务层面的比较验证 |
| **Q2 责任与代理** | 谁定目标、授予权限、处理异常并承担后果？这些是否可以分离？ | M3 委托代理、Authority、Accountability | P-002 / P-003 是候选概念入口 | 责任分配与治理的直接证据薄弱；管理者必要性论证不等于完整责任理论 |
| **Q3 协调机制** | 怎样分工、衔接、交换信息、处理冲突？共享语义何时有用？ | M2 组织设计、信息处理、协调；M5 多主体 | P-001 已完成；P-004 候选扩展到 Multi-Agent；P-006 提供 World Model / Orchestration 路线图视角 | Shared World Model 的必要性、替代机制与成本尚缺比较证据 |
| **Q4 企业边界** | 哪些能力内部组织，哪些外部采购或调用？成本下降是否足以改变边界？ | M1 Coase / Williamson；M3 治理 | 当前登记论文尚无该方向核心材料 | 需交易成本与治理理论，以及边界变化的公开证据 |
| **Q5 组织学习** | 反馈怎样使人或 AI 学习？局部变化怎样被组织保留、复用和验证？ | M4 学习、记忆、探索与利用；M2 信息结构 | P-001 已提供学习信息条件 | 尚未解释 / 验证从局部学习到组织长期能力的完整过程 |

具体 Problem 与工程桥接见 [`research-questions.md`](research-questions.md)。

## 3. 核心论文登记

### P-001｜组织设计的基础入口

- **文献**：Phanish Puranam (2021), *Human–AI collaborative decision-making as an organization design problem*。
- **原文**：[DOI / Journal of Organization Design](https://doi.org/10.1007/s41469-021-00095-2)，10:75–80。
- **类型**：Point of View；概念设计框架，借用既有组织设计与学习研究。
- **阅读状态**：2026-09-07 完成本轮理论理解、研究解释与 Human Takeaways。
- **位置**：Q1 / Q3 / Q5；M2 / M4 / M5；当前主要服务 R-001 / R-003。
- **已获得增量**：区分收益来源、工作结构、学习条件；能解释结构怎样影响学习机会与归因。
- **尚未完成**：企业协作选型与反馈的实际验证；不能把分类框架直接当企业设计原则。
- **记录**：[原文与概念](paper-reviews/P001_puranam_2021_source-walkthrough.md)；[研究解释与吸收](paper-reviews/P001_puranam_2021_hacd.md)。
- **当前处理**：对 R-001 视为已完成的 A 类理论证据；局部按需回看，不重开整篇。

### P-002｜管理者工作与 AI 的作用

- **文献**：Amir Goldberg & Phanish Puranam (2026), *Purpose not prediction: the role of managers in the age of AI*。
- **原文**：[DOI / Journal of Organization Design](https://doi.org/10.1007/s41469-026-00205-y)，15:1–7；2026-04-24 在线发表。
- **类型**：Editorial；以管理者工作与 AI 的比较为核心的概念论证，不是新增企业实验报告。
- **来源状态**：2026-09-08 已核验研究者提供的 7 页完整 PDF 可读；全文不上传公开仓。
- **位置**：主 Q1；关联 Q2 / Q3；M2 / M3 / M5；可能服务 R-001 / R-004。
- **阅读进度**：已完成文献类型、开场问题与五类管理者工作的初步梳理；尚未形成 Engineering Bridge。
- **潜在增量**：管理者工作、technical performance、normative appropriateness、purpose 与 AI 作用边界。
- **当前处理**：对 R-001 先按 **B → 可升级 A**。先定向判断上述机制是否真正改变 Human / AI 决策权设计；有重大直接增量再升级完整精读。
- **停止条件**：获得足够 Engineering Bridge 即可，不因为“它是第二篇”而必须读到统一深度。

### P-003｜管理主体扩展候选

- **既有登记**：吕源，《管理者—人工智能关系中的管理主体扩展》。
- **来源状态**：正式题录、出版物、年份与原文仍待核验；保留原编号，不编造 DOI。
- **候选位置**：Q1 / Q2 / Q3；M5；可能服务 R-004。
- **潜在增量**：管理主体、工具与主体关系的概念辨析。
- **当前处理**：没有 Active Problem 明确需要时保持 **C / Backlog**；升级前先核实材料身份。

### P-004｜从人机决策扩展到 Multi-Agent 组织

- **文献**：Jose Arrieta, Vivianna Fang He, Phanish Puranam & Yash Raj Shrestha (2026), *Multi-Agent AI Systems Are Organizations*。
- **原文入口**：[INSEAD Working Paper 2026/49/STR](https://www.insead.edu/faculty-research/publications/working-papers/multi-agent-ai-systems-are-organizations)；[SSRN 6813862](https://ssrn.com/abstract=6813862)。
- **类型与证据**：工作论文；组织理论论证，并把既有 MAST 失败分类映射到组织问题。引用的执行轨迹来自既有研究，不能登记成作者重新采集的企业实验。
- **位置**：主 Q3，关联 Q1 / Q2；M2 / M5；可能服务 R-001 的 Multi-Agent 扩展。
- **潜在增量**：检查 P-001 的组织设计语言如何延伸到多个 Agent 的分工、信息、目标与异常处理。
- **当前处理**：**C → 条件升级 B/A**。只有 Active Problem 扩展到 Multi-Agent 失败机制时启动。

### P-005｜聚合在什么条件下值得尝试

- **文献**：Vivek Choudhary, Arianna Marchetti, Yash Raj Shrestha & Phanish Puranam, *Human-AI Ensembles: When Can They Work?*
- **年份**：2023-10-03 在线首发；卷期版为 *Journal of Management* **51(2), 536–569（2025）**。同一 DOI，不重复登记。
- **原文**：[期刊全文 / DOI](https://doi.org/10.1177/01492063231194968)。
- **类型与范围**：规范性设计理论，主要讨论数据丰富情境中、基于预测的项目评价；不是实证企业操作手册。
- **位置**：主 Q1、关联 Q3；M2 / M5；与 R-001 的“判断聚合何时值得”直接相关。
- **潜在增量**：从 P-001 的“聚合可能有收益”进一步理解组合价值的条件、假设和限制。
- **历史处理（2026-09-11 语境）**：当时若 R-001 进入“aggregation condition”子问题可升级为 **A 类**；该判断保留为历史执行语境。当前是否升级应重新对照 `REPOSITORY_STATE.yaml` 中的 human frontier。

### P-006｜通用世界模型的原则与路线图候选

- **文献**：Jun Zhu, Hengkai Tan, Jintao Zhang, Min Zhao, Fan Bao & Bo Zhang (2026), *General World Models from First-Principles*。
- **来源状态**：研究者提供的 23 页完整 PDF 可读；正式出版 / 预印本入口与版本仍待核验，全文不上传公开仓。
- **类型与证据**：Position / roadmap paper；以 `Understanding → Imagination → Action` 闭环和 L1–L5 路线图组织论点，不是对完整通用世界模型的实证验证。
- **位置**：主 Q3，关联 Q1；可能服务 R-002，并与 P-002 的 purpose、P-004 的 Multi-Agent orchestration 形成概念接口。
- **潜在增量**：区分 World Generation、Interactive World、Actionable World、Autonomous World Agent 与 World Orchestrator，帮助提出“世界表达怎样进入目标形成、行动与多主体编排”的新问题。
- **证据边界**：文中关联的系统主要说明 L1–L3；作者明确把 L4 / L5 作为尚未建立的未来方向，不能据此声称自主世界主体或编排层已经实现。
- **历史处理（2026-09-11 语境）**：当时对 R-001 属于 **C**，不打断 P-002；若未来 human frontier 转向 Enterprise Context / World Model、Agent 自主性或跨主体编排，可重新评估是否升级为 **B**。

## 4. 阅读顺序与收集边界

> **Historical Execution Context｜历史执行语境（2026-09-11）**  
> 以下 R-001 相关顺序记录当时为什么这样读，不再定义当前研究前沿。当前状态请读取 `REPOSITORY_STATE.yaml`。

- **当时驱动对象是 R-001，不是 P-002。**
- 原计划 `P-001 → P-002 → P-003` 只保留为历史记录，不再承担执行顺序。
- 当时 P-002 先做 B 类定向阅读；如果对 R-001 有直接重大增量再升级 A。
- 如果 R-001 转入“聚合条件”，P-005 比按编号继续 P-003 更有优先级。
- 如果 R-001 转入 Multi-Agent 组织失败，再考虑 P-004。
- 当时 P-006 对 R-001 只作 C 类登记；不要把这条历史顺序解释为当前 Frontier。
- 一次只深读一篇 A 类论文，但同一 Problem 可以同时维护多个 Evidence Candidate。
- 当前 P-001、P-002、P-004、P-005 均含 Puranam；它们有连续性，但不构成四份独立研究传统的交叉验证。后续需要主动寻找不同作者、方法、失败结果和替代解释。
- Q4 暂时留白，不为“看起来完整”补长列表。

## 5. 判断新文章是否值得读

不要先问“是不是名家 / 新文章”，先问当前 Problem。

| 判断 | 必须写出的内容 |
|---|---|
| Problem 关联 | 它试图解释哪个具体 R / Q？不能只写“AI 管理” |
| 相对增量 | 相比已有材料新增什么机制、条件、数据、反例或对照？ |
| 证据与可读性 | 原文是否可得？理论、实验、观察、综述还是其他类型？ |
| Engineering Bridge | 读后应该改变什么解释、设计或验证？ |
| 阅读等级 | 相对当前 Problem 是 A / B / C？为什么？ |

据此处理：

- **A｜问题型论文**：当前核心问题需要完整论证才能工程翻译；
- **B｜原则型论文**：只需获得核心机制与原则性增量；
- **C｜启发型论文**：登记线索与升级条件，不制造学习债务。

最小登记句：

> 这篇文章试图帮助解释【Concrete Problem】，相对【已有证据】可能新增【机制 / 条件 / 证据 / 反例】；因此当前归为【A / B / C】，读后应能形成【Engineering Bridge / Principle 影响 / 升级条件】。

## 6. 什么表示研究在推进

完成一轮后更新：

1. Problem 是否被解释得更清楚；
2. 是否形成新的 Engineering Hypothesis；
3. 是否知道怎样验证，或已经得到验证 / 反例；
4. 哪条 Candidate Principle 被形成、支持、修正或否定；
5. 暴露了什么 New Problem。

不以篇数、术语数、下载量或 M1–M6 是否填满衡量进度。

> **论文知识 → 工程假设 → 实践证据 → 自己的原则**，而不是 **论文 → 笔记 → 更多论文**。
