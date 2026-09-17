# RP-004-01｜Probabilistic Judgment vs. Deterministic Control

Status: Open / Exploratory  
Created: 2026-09-17  
Parent: RP-004 Effective Agency / Authority / Accountability  
Primary Track: E3 Agent-callable Capability / G2 Authority / G3 Human Control  
Related: G4 Traceability / Agent Runtime Safety / Model Guardrail / AI Gateway

> 核心子问题：**企业级模型 / Agent 安全护栏应该如何在概率性 AI 风险判断与确定性安全控制之间分工？**

本文件保存一个尚未收敛的架构研究问题。当前不把任何具体安全模型、AI Gateway 或 Guardrail 产品路线升级为架构原则。

---

## 1. Trigger｜问题来源

在一次 AI 安全交流中，观察到当前部分厂商的产品路线主要围绕“小参数安全模型 + AI 网关 + 内审 / 鉴伪 / 模型测评”等能力展开。

这种路线能够处理一部分输入输出内容安全、提示词风险和语义识别问题，但也暴露出一个更上位的架构问题：

> **如果风险识别本身依赖概率模型，那么企业是否可以把最终安全边界也交给概率模型决定？**

特别是在 Agent 具备工具调用、数据访问、系统写入、流程触发甚至物理行动能力后，安全问题已经不再只是“输出内容是否安全”，还包括：

- 当前任务是否允许执行；
- 当前身份是否有权调用该工具；
- 当前参数是否超出授权范围；
- 某个高影响动作是否需要审批；
- 模型判断出错后是否存在不可绕过的执行边界；
- 整个判断、授权、执行链能否被审计和追责。

因此问题从：

> “模型安全护栏应该检测哪些风险？”

进一步转变为：

> **“AI 安全中的判断权、决策权与执行权应该如何分离？”**

---

## 2. Core Question｜核心研究问题

> **企业级模型 / Agent 安全护栏应该如何在概率性 AI 判断与确定性安全控制之间分工，使开放语义风险能够被识别，同时权限、行为边界和高影响动作仍然保持可验证、可审计和不可绕过？**

该问题不是简单比较“规则好还是模型好”，而是研究两类机制各自更适合承担什么责任：

- AI / Model：处理开放语义、上下文、意图与未知模式；
- Policy / IAM / Gateway / Sandbox / Approval：处理明确权限、行为边界、资源约束和强制执行。

---

## 3. Working Hypothesis v0.1｜当前工作假设

### H-RP004-01｜Probabilistic Detection × Deterministic Control

> **企业级 AI 安全可能需要拆分为概率性感知 / 判断平面与确定性决策 / 执行平面。模型负责发现和解释风险，确定性机制负责决定边界并强制执行。**

候选结构：

```text
Input / Context / Plan / Tool Call / Output
                ↓
        Sensor / Judge
   风险类型 / 分值 / 置信度 / 证据
                ↓
             Policy
  身份 / 权限 / 任务 / 资源 / 动作规则
                ↓
            Enforcer
 Gateway / IAM / Sandbox / Approval / Tool Runtime
                ↓
            Evidence
      Trace / Audit / Decision Record
                ↓
            Feedback
      Eval / Rule / Model Improvement
```

当前最核心的假设不是“规则一定优于模型”，而是：

> **随着行为权限、不可逆性和业务影响提高，最终安全控制权应越来越少依赖模型自主判断，而更多落在可验证、可审计、不可绕过的确定性控制机制上。**

状态：Hypothesis，不进入 `JUDGMENTS.md` / `PRINCIPLES.md`。

---

## 4. Candidate Architecture Variables｜候选架构变量

当前先记录四个可能影响分工的变量，不视为最终变量集合。

| 变量 | 偏向概率 AI 判断 | 偏向确定性控制 |
|---|---|---|
| **Semantic Openness｜语义开放度** | 高：攻击意图、敏感语义、越狱、未知模式 | 低：身份、接口、字段、资源、枚举规则 |
| **Privilege Impact｜权限影响** | 低权限、辅助判断 | 高权限访问、跨域调用、写操作 |
| **Reversibility｜行为可逆性** | 可重新生成、可撤回、低成本重试 | 删除、付款、写库、下发控制等不可逆动作 |
| **Error Cost｜错误代价** | 可容忍一定误报 / 漏报 | 单次错误可能造成重大业务、安全或合规后果 |

需要后续验证：这些变量是否足以解释 Guardrail / Agent Security 的控制分工，还是还应增加可观测性、时效性、责任主体等维度。

---

## 5. Relation to PMVAEB｜与模型安全护栏卡的关系

当前形成的 **PMVAEB 六维模型安全护栏模型**不作为独立母问题，而视为 AQ-004-01 的一版工程表达。

可暂时映射为：

```text
P / M / V  → Risk / Sensor / Judge
A          → Policy / Decision
E          → Enforcer / Runtime Control
B          → Benchmark / Evidence / Feedback
```

更一般化后，可归入：

> **Sensor → Judge → Policy → Enforcer → Evidence → Feedback**

因此后续研究 PMVAEB 的重点不只是继续增加功能项，而是验证：

1. 哪些风险真的需要模型判断；
2. 哪些边界必须由 Policy 定义；
3. 哪些控制必须在模型之外强制执行；
4. 怎样形成可重复验证的 Evidence / Benchmark；
5. 哪些 Guardrail 能力属于 Model Safety，哪些已经属于 Agent Runtime / Enterprise Security。

---

## 6. Architecture Question｜当前架构问题

### AQ-004-01｜Probabilistic Judgment vs. Deterministic Control

> 企业级 AI 安全如何划分 Judge、Policy 与 Enforcement 的责任，使模型能够理解开放风险，但不能自行定义和突破最终安全边界？

需要重点研究：

- Prompt / Input 风险；
- RAG / Context 污染与间接 Prompt Injection；
- Agent Plan / Intent 风险；
- Tool Selection / Tool Parameter 风险；
- Data Access / Data Exfiltration；
- High-impact Action；
- Output / Content Safety；
- Identity / Authorization / Delegation；
- Runtime Isolation / Sandbox；
- Audit / Trace / Evidence。

---

## 7. Engineering Question｜工程验证方向

### EQ-004-01｜Control Point & Enforcement

> **Input、Context、Model、Tool、Data、Action、Output 等不同控制点，哪些适合模型判断，哪些必须落到确定性 Policy / IAM / Gateway / Sandbox / Approval？**

候选验证结构：

```text
风险类型
×
控制点
×
判断机制
×
决策机制
×
执行机制
×
Evidence
```

预期形成一张：

> `AI Runtime Safety Control Matrix v0.1`

而不是继续形成产品功能清单。

---

## 8. Validation Question｜验证问题

### VQ-004-01｜Probabilistic-only vs. Hybrid Control

> **如何比较“主要依赖安全模型”与“概率判断 + 确定控制”两种架构的实际安全差异？**

至少观察：

- False Positive；
- False Negative；
- Prompt / Policy Bypass；
- Unauthorized Tool Call；
- Parameter Manipulation；
- Privilege Escalation；
- Irreversible Action；
- Auditability / Traceability；
- Latency / Cost；
- Policy Maintenance Cost。

需要主动寻找反例：

- 哪些场景纯确定性规则已经足够，不需要模型判断；
- 哪些场景即使增加 Policy / Enforcer，也无法弥补 Judge 的严重漏报；
- 哪些情况下过重控制会让 Agent 无法完成有效任务。

---

## 9. Evidence Plan｜后续证据方向

优先寻找：

- `[Policy / Standard]`：AI / Agent Security、模型安全、身份授权、运行时安全相关公开标准；
- `[Product Fact]`：主流 AI Gateway、Guardrail、Agent Runtime、IAM / Policy 产品真实架构；
- `[Open-source Implementation]`：Guardrail、Policy Engine、Agent Sandbox、Tool Permission 等开源实现；
- `[Industry Case]`：高权限 Agent / Copilot 在真实企业系统中的控制方式；
- `[Counter Evidence]`：模型护栏或规则护栏在真实攻击中的绕过与失败案例；
- `[Benchmark]`：Prompt Injection、Jailbreak、Tool-use Security、Agent Security Eval。

研究时必须区分：

- 模型安全能力；
- 产品宣传 Claim；
- 运行时强制控制；
- 合规 / 测评要求；
- 实际攻击与防御证据。

---

## 10. Relation to RP-004｜为什么挂在这里

本问题不单独升级为新的 Research Problem，因为它本质上属于 RP-004 的 Authority / Human Control / Accountability 结构。

关系可以表示为：

```text
RP-004
Effective Agency / Authority / Accountability
        ↓
Agent 获得 Capability
        ↓
谁有权决定是否执行？
        ↓
AQ-004-01
Probabilistic Judgment vs. Deterministic Control
        ↓
Judge / Policy / Enforcer 分工
        ↓
Runtime Safety / Authority / Evidence
```

它与 RP-002 的边界也需要保持清楚：

- RP-002 主要回答：企业现实如何进入 Model / Agent Context；
- RP-004-01 主要回答：当 Model / Agent 基于这些 Context 进行判断和行动时，安全控制权如何配置。

---

## 11. Current Stop Point｜当前停止点

本轮先完成三个动作：

1. 将 AQ-004-01 注册到 RP-004；
2. 将“概率判断 + 确定控制”记录为 H-RP004-01；
3. 将 PMVAEB 定位为该问题的一版工程表达，而不是新增独立问题族。

当前不继续扩展新的 Security Problem Family，也不进入 `JUDGMENTS.md` / `PRINCIPLES.md`。

下一次真正继续研究时，从以下问题开始：

> **先收集公开标准、主流产品架构和开源实现，验证 Judge / Policy / Enforcer 是否真的是一个稳定、可解释的结构，再决定 PMVAEB 是否需要重构。**
