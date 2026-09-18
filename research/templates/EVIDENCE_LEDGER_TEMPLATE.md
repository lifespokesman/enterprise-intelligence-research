# Evidence Ledger Template｜研究证据账本模板

状态：Active  
假设：H-XXX  
开始日期：YYYY-MM-DD

> 本文件同时服务两种读者：
>
> - 人：优先阅读 Research Finding 与 Cross-source Synthesis；
> - AI：继续使用 Evidence Ledger 做来源追溯、假设更新与自动研究。

---

## 1. 当前假设

### H0 / H1

> 用 1–3 段写清当前工作假设。

当前状态：Initial / Exploring / Revised / Validating

---

## 2. 当前研究 Gap

### GAP-XXX｜问题标题

> 本轮真正要回答的问题是什么？

本轮停止条件：

- 什么证据足以回答当前 Gap；
- 什么反例会迫使当前判断收窄；
- 什么未知量必须转入工程验证。

---

## 3. Research Finding｜研究发现

### 本轮问题

用一句话重述 Gap，不复述任务过程。

### 一句话结论

> 直接回答：这一轮研究以后，我们现在最应该相信什么？

### 跨来源关键发现

用 2–4 段说明多个论文 / 产品 / 案例放在一起后的稳定模式。

不要按“材料 A 讲了什么、材料 B 讲了什么”逐条复述。

### 关键差异 / 反例 / 边界

明确写出：

- 哪些来源不一致；
- 哪些场景不成立；
- 有没有更简单的替代解释；
- 哪些结论目前仍只是推断。

### 对原 Hypothesis 的影响

说明：

- 原来怎么想；
- 现在改了哪一部分；
- 哪一部分仍保留；
- 是否需要 proposed_revision。

### 对架构 / 产品 / 工程的意义

回答：

> 如果这个 Finding 成立，未来做架构设计、产品路线或工程验证时应该怎么不同？

### 当前最大未知量

> 现在最值得继续研究或验证的一个问题是什么？

### Supporting Evidence

- E-XXX
- E-XXX
- E-XXX

建议控制：约 300–800 个中文字符。  
目标：用户不展开 Evidence Detail，也能理解“研究了什么、发现了什么、为什么重要、下一步是什么”。

---

## 4. Cross-source Synthesis｜跨来源综合

当本轮包含多个产品、论文、开源项目或案例时，优先使用比较表。

| 对象 | 它提供了什么 | 真正由谁执行 / 生效 | 权限 / 治理在哪里 | 关键边界 | 对当前 Hypothesis 的意义 |
|---|---|---|---|---|---|
| Source A |  |  |  |  |  |
| Source B |  |  |  |  |  |
| Source C |  |  |  |  |  |

表格之后只补充真正重要的共同模式、差异与反例。

---

## 5. Evidence Index｜证据索引

| ID | Source | Type | Observed Fact | Target | Effect | Confidence |
|---|---|---|---|---|---|---|
| E-001 |  |  |  | H-XXX | Supports / Challenges / Narrows / Revises / Rejects / Opens Alternative |  |

> Evidence 数量不是 KPI。只保留真正影响判断的 Material Evidence；没有高价值增量时记录 `NO_MATERIAL_UPDATE`。

---

## 6. Evidence Detail｜证据明细

### E-001｜证据标题

来源：  
URL：  
日期：  
证据类型：

**观察事实**

只写来源真正支持的内容。

**机制**

解释这个事实为什么会影响当前问题。

**目标假设**

H-XXX

**Effect**

Supports / Challenges / Narrows / Revises / Rejects / Opens Alternative

**Confidence**

High / Medium / Low

**边界 / 限制**

这个证据不能证明什么？适用范围是什么？

**对当前 Finding 的作用**

它支撑 / 限制 / 反驳 Finding 的哪一部分？

---

## 7. 假设演进

### H0

原始假设。

### proposed H1

只有证据真正改变判断时才提出。

变化记录：

- 旧假设：
- 触发 Evidence：
- Research Finding：
- 变化原因：
- 新边界条件：
- 尚未解决 Gap：

---

## 8. 反证与替代解释

至少记录：

- 当前最强 Counter Evidence；
- Alternative Hypothesis；
- 哪种场景下当前 Finding 会失效。

---

## 9. 当前判断

当前状态：

`Exploring / Revised / Validating / NO_MATERIAL_UPDATE`

用 1–3 段说明当前最稳定判断。

不升级为 Principle，除非经过独立人工审核和工程验证。

---

## 10. 下一步行动

只留下一个明确的 next_action。

说明：

- 为什么是这一步；
- 需要什么 Evidence / Validation；
- 什么结果会让研究前进或停止。
