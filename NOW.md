# NOW｜当前研究驾驶舱

> 这个文件只服务于“快速恢复研究状态”。现在的研究单位是 **Active Problem**，不是 Active Paper。

Updated: 2026-09-11

## 1. 当前研究方法：问题驱动，而不是材料驱动

主闭环保持为：

> **现象 / 真实问题 → 认知问题 → 架构问题 → 工程 / 验证问题 → 定向寻找证据 → 机制解释 → Engineering Hypothesis → Validation → Architecture / Method Principle → 新问题**

论文、产品、公开案例、开源项目、标准和分析报告都是 Evidence Provider，不构成独立学习队列。

当前判断研究是否推进，不看“读了多少篇”，而看：

- 问题是否从现象变成了可解释的问题；
- 是否形成了更清楚的架构选择；
- 是否知道还缺什么证据；
- 是否形成了可以验证的 Engineering Hypothesis；
- 是否最终沉淀 / 修正了 Principle。

完整方法见 [`research/RESEARCH_LOOP.md`](research/RESEARCH_LOOP.md)。

---

## 2. 当前 Active Problem｜RP-002 Enterprise Data–Model Relationship

> **企业已有的数据资产，与大模型之间到底应该建立什么关系？企业真实世界究竟通过哪些机制进入 Model / Agent？**

这个问题由真实工作现象启发，但公开仓只保留抽象后的问题，不记录私人项目来源或证据链。

当前之所以切换到 RP-002，是因为它直接影响正在形成的企业 AI 数据 / Context / World Model 架构判断；RP-001 暂停在已有明确停止点，不丢失已有成果。

完整问题树见 [`research/research-questions.md`](research/research-questions.md)。

---

## 3. RP-002 当前已经想清楚到哪里

### 3.1 认知层｜CQ

当前不是直接问“应该选 Ontology 还是 RAG”，而是先确认几个更上位的问题：

1. **企业数据对模型到底扮演哪些不同角色？**  
   当前候选包括：Learning Material、External Knowledge、Current Facts、Business Semantics、Task Context、Evaluation Evidence、Runtime Feedback。
2. **为什么传统数据治理完成不等于 AI-ready？**  
   当前需要区分 Data Availability 与 Context Usability、Schema 与 Business Semantics、历史数据与当前状态、数据质量错误与模型 / Context / Tool 错误。
3. **模型真正需要的是更多数据，还是更好的企业世界表达？**
4. **哪些模型错误可以通过数据治理改善，哪些不能？**

当前 Working Hypothesis：

> `Data Availability ≠ Context Usability`。

以及：

> 企业数据服务 Model / Agent 时，可能不是一种单一“数据接口”，而是多种不同目的、不同生命周期的数据—模型关系。

两者都只是 Hypothesis，不升级为 Judgment / Principle。

---

## 4. 下一轮优先研究的三个架构问题

下一次恢复研究时，不先继续读论文，也不先设计完整 AI 数据平台。围绕下面三个问题定向寻找理论与工程证据。

### RQ-002-A｜Relationship Types

> **业界现在真实存在几种 Data → Model / Agent 关系？**

重点检验当前候选：Dataset / Training、Knowledge / RAG、SQL / API / Query、Tool / Action、Semantic / Ontology、Context、Eval、Feedback。

目标不是继续增加名词，而是确认：

- 哪些真的是不同关系；
- 哪些只是实现手段；
- 哪些处于不同生命周期；
- 当前分类遗漏了什么。

**预期产物：`Enterprise Data–Model Relationship Map v0.1`**。

### RQ-002-B｜Mechanism Boundaries

> **Dataset、Knowledge Base、SQL、API、Tool、Ontology、Context、Eval、Feedback 的边界到底是什么，又怎样组合？**

需要明确每一种机制主要回答什么问题，例如：模型长期学什么、运行时查什么、当前事实是什么、事实在业务上意味着什么、当前任务该给什么、输出是否正确、运行经验如何回流。

**预期产物：`Data–Model Mechanism Boundary Table v0.1`**。

### RQ-002-C｜Architecture Evolution

> **哪些仍属于传统数据治理 / 数据平台问题，哪些是 Model / Agent 成为新消费者后显著新增的 Context / Semantic / Evidence 问题？**

重点研究传统链路：

`Source → Integration → Governance → Warehouse / Lake → Data Service → Application`

与候选 AI 链路之间到底是继承、扩展还是重构，而不是先假设一定需要一个全新的“AI 数据平台”。

**预期产物：`Traditional Data Platform → AI-ready Context Architecture v0.1`**，其中必须标记“继承能力 / 新增能力 / 待验证能力”。

---

## 5. 下一轮如何找证据

三个问题分别选择合适证据，不默认“找论文就是研究”。

优先证据类型：

- **[Product Fact]**：主流数据 / AI 平台公开架构和产品文档，观察实际怎样把数据提供给模型；
- **[Open-source Implementation]**：RAG、结构化数据查询、Context、Semantic / Knowledge Graph、Eval 等工程实现；
- **[Theory]**：解释语义、知识表示、Context、信息整合、数据与推理关系的理论 / 论文；
- **[Industry Case]**：公开企业案例，看这些机制是否真的进入业务闭环；
- **[Analyst View] / [Policy / Standard]**：帮助判断产业共性和治理约束；
- **[Counter Evidence]**：简单任务不需要复杂语义层的案例，以及复杂本体建设仍无法解决模型错误的反例。

研究顺序：

`Question → Evidence Search → Evidence Identity → Mechanism Synthesis → Architecture Hypothesis`

不要先画一个完整答案，再只寻找支持它的资料。

---

## 6. 本轮预期成果，不要求今天完成

这一轮 RP-002 暂时只追求四类成果：

1. **关系地图**：Data 与 Model / Agent 到底有哪些结构性关系；
2. **边界表**：Dataset / KB / SQL / API / Tool / Ontology / Context / Eval / Feedback 分别解决什么；
3. **架构演进图**：传统数据能力哪些继续有效，AI 时代新增哪些 Semantic / Context / Evidence 能力；
4. **问题收敛结果**：研究后哪些 Hypothesis 得到支持 / 修正，是否足以提出 Candidate Architecture Principle。

暂时不要求：

- 一次性形成完整企业 AI 数据平台方案；
- 把所有厂商收集齐；
- 为了完整性批量读论文；
- 现在就新增稳定 Principle。

只有证据能够支撑，才从 Working Hypothesis 推进到 Candidate Principle。

---

## 7. 后续工程层还没有启动

当前 EQ / VQ 已登记，但先不抢跑：

- 比较 RAG、SQL/API、Semantic Model / Ontology、组合 Context；
- 把治理后的数据转换成 Dataset / Knowledge / Eval / Semantic Asset；
- 让 Context 携带 Source / Lineage / Freshness / Permission / Evidence；
- 处理历史知识、实时 State、Event；
- 验证人工本体、AI 自动发现、动态语义模型的成本和收益。

这些要等前面的关系与边界更清楚后，再决定最小 Demo / Benchmark。

---

## 8. 其他问题状态

- **RP-001 Human–AI Decision Structure**：Paused / Candidate。P-001 已完成本轮理论理解；P-002 / P-005 保持证据候选。需要时从已有状态继续，不重开论文队列。
- **RP-003 Agent Experience → Organizational Learning**：Candidate。
- **RP-004 Effective Agency / Authority / Accountability**：Candidate。
- **RP-005 AI 与企业边界**：Backlog。

一个时期仍只保留一个主要 Active Problem。

---

## 9. Resume Here｜下次从这里继续

> 当前 Active Problem 已切换为 **RP-002 Enterprise Data–Model Relationship**。
>
> 当前不是要直接“给出 AI 数据平台答案”，而是围绕三个架构问题做证据研究：
>
> **A. Data → Model / Agent 有哪些真实关系？**  
> **B. Dataset / KB / SQL / API / Tool / Ontology / Context / Eval / Feedback 的机制边界是什么？**  
> **C. 哪些是传统数据平台能力，哪些是 AI 时代新增的 Semantic / Context / Evidence 问题？**
>
> 下一步：围绕 A / B / C 定向搜索公开 Theory、Product Fact、Open-source、Industry Case 与 Counter Evidence；先形成 Relationship Map、Boundary Table、Architecture Evolution v0.1，再判断是否能沉淀 Architecture Principle。
>
> 不按论文编号继续读，不预设 Ontology / Context 一定是答案。
