# Enterprise Intelligence Research

**English** | [简体中文](README.zh-CN.md)

> A living research project on Enterprise Intelligence and AI-era Organization Design.

This repository starts from a question that sits above “how to build an AI agent”:

**What happens to cognition, decision rights, coordination, accountability, firm boundaries, and organizational learning when AI becomes a non-human actor capable of understanding, judging, planning, invoking capabilities, and acting over time?**

## Working Definition: Enterprise Intelligence

> **Enterprise intelligence is an organizational capability: the ability of an organization to configure cognition, decision rights, action capacity, and learning under goals, resource constraints, institutional rules, and risk boundaries, so that it can continuously sense its environment, interpret reality, form judgments, organize capabilities, act, and adapt from feedback.**

A simplified loop:

`Sense → Understand → Judge → Organize → Act → Feedback → Learn`

This project distinguishes:

- **Model Intelligence** — model-level reasoning, prediction, interpretation, and generation;
- **Subject Intelligence** — an intelligent subject’s ability to pursue goals, maintain context, judge, act, and adapt over time;
- **Enterprise Intelligence** — an organizational property emerging from how humans, AI, software, data, and assets are configured into a working system of cognition, decision, action, and learning.

A core proposition is:

> **Enterprise intelligence is not an additive property of individual AI agents.**

## Five Long-Term Research Questions

1. **Decision Rights** — How should decision rights be reallocated when humans and AI have different cognitive advantages, limitations, and responsibility-bearing capacities?
2. **Accountability & Agency** — How should authority, risk, and accountability remain connected when AI participates in decisions but cannot bear consequences in the human sense?
3. **Coordination** — How should humans, agents, software, and enterprise assets coordinate? Could a shared enterprise world model become semantic coordination infrastructure?
4. **Firm Boundaries** — If AI lowers discovery, coordination, monitoring, and transaction costs, which capabilities should remain internal and which can be dynamically assembled externally?
5. **Organizational Learning** — How can traces, outcomes, failures, feedback, and agent experience become durable organizational knowledge, skills, rules, evaluation assets, and policies?

[Read the research questions →](topics/en/README.md)

## Research Method: Problem-driven, not Paper-driven

Q1–Q5 are the long-term problem map. The actual unit of research is a **concrete problem**, not a paper.

The main loop is:

> **Real Problem → Theory / Industry Search → Understanding → Engineering Translation → Small-scale Validation → Architecture / Method Principle → New Problem**

or, more compactly:

`Problem → Evidence → Mechanism → Engineering Hypothesis → Validation → Principle → New Problem`

The point is not to read papers for their own sake. The method is to let real problems pull in theory, translate mechanisms into engineering hypotheses, use validation to filter those hypotheses, and accumulate reusable principles.

Papers are classified dynamically relative to the current problem:

- **A — Problem papers**: directly affect the current engineering decision; close-read and complete an Engineering Bridge.
- **B — Principle papers**: extract the core mechanism, changed judgment, and principle-level implication without full walkthrough.
- **C — Inspiration papers**: keep as candidates until a concrete problem gives them a reason to be read.

Research progress is therefore measured less by the number of papers read and more by **problems clarified, engineering hypotheses formed, hypotheses tested, and principles revised**.

[Read the full research loop →](research/RESEARCH_LOOP.md)

## Public Evidence Architecture

This public repository only uses claims that can be independently supported by public evidence:

- **Academic Theory**
- **Product Fact**
- **Product Claim**
- **Industry Case**
- **Analyst View**
- **Policy / Standard**
- **Counter Evidence**
- open-source implementations, synthetic demos, and public benchmarks where appropriate

A core boundary is:

> **Private experience may inspire a question, but every public claim must be independently supportable by public evidence.**

Evidence identities remain distinct:

> **Product Claim ≠ Validated Theory**  
> **Vendor Case ≠ Independent Evidence**  
> **Analyst View ≠ Academic Theory**  
> **Public Success Case ≠ General Law**  
> **Synthetic Demo ≠ Enterprise Outcome**

## Industry Research Roadmap: Engineering × Governance

The industry roadmap is organized around durable engineering and governance problems, not vendors.

### Track E — Intelligent Subject Engineering

- **E1 Agent Production / Harness / Runtime** — How does AI become a continuously operating intelligent subject?
- **E2 Enterprise Context / World Model / Ontology** — How does an intelligent subject understand a specific enterprise world?
- **E3 Capability / Action Infrastructure** — How does it invoke software and enterprise assets to act on that world?
- **E4 Feedback / Evaluation / Evolution** — How does agent experience become durable enterprise capability?

### Track G — Intelligent Subject Governance

- **G1 Identity / Ownership** — Who or what is this intelligent subject, who owns it, and who is responsible for it?
- **G2 Authority / Policy** — What may it see, invoke, and do?
- **G3 Human Control / Accountability** — When should humans retain control, when may AI act autonomously, and how should accountability be allocated?
- **G4 Trace / Audit / Lifecycle** — How should intelligent subjects be traced, audited, changed, and retired?

[Read the full industry roadmap →](industry/ROADMAP.md)

Vendors, products, frameworks, and cases are **observation targets**, not research tracks in themselves.

## Current Research Hypothesis

Traditional enterprise information systems largely assume that humans interpret the business world and organize digital capabilities through applications, workflows, and organizational roles.

As AI becomes a new organizational actor, part of the work of interpretation, judgment, planning, capability discovery, orchestration, execution, and learning may shift toward intelligent subjects.

A long-term hypothesis being tested is that an AI-native enterprise may increasingly be organized around the interaction of:

**Intelligent Subject × Enterprise World Model × Capability Network × Real-world Feedback**

This is a research hypothesis, not a prediction presented as fact.

## Repository Structure

### Human-facing research cockpit

- [`NOW.md`](NOW.md) — current **Active Problem**, blocker, and next single action
- [`research/research-questions.md`](research/research-questions.md) — concrete problems, evidence gaps, engineering translation, and validation state
- [`EVOLUTION.md`](EVOLUTION.md) — major cognitive shifts and their origin
- [`JUDGMENTS.md`](JUDGMENTS.md) — what the project currently believes about the world
- [`PRINCIPLES.md`](PRINCIPLES.md) — reusable architecture and method principles, with validation status

A useful distinction:

> **Judgment = a current belief about how the world works. Principle = a reusable design rule for engineering or research.**

### Problem, theory, and papers

- [`research/RESEARCH_LOOP.md`](research/RESEARCH_LOOP.md) — canonical problem-driven research loop
- [`research/research-questions.md`](research/research-questions.md) — concrete problem map
- [`research/theory-map.md`](research/theory-map.md) — classical organization theory and AI pressure tests
- [`research/scholars.md`](research/scholars.md) — scholar map
- [`research/reading-list.md`](research/reading-list.md) — paper registry and evidence index, not a mandatory reading queue
- [`research/paper-review-plan.md`](research/paper-review-plan.md) — A/B/C classification, Part A–E, and stop conditions
- `research/paper-reviews/` — necessary source walkthroughs, concept reconstruction, interpretation, and Engineering Bridges

### Public industry evidence

- [`industry/README.md`](industry/README.md)
- [`industry/ROADMAP.md`](industry/ROADMAP.md)
- [`industry/cases/`](industry/cases/)
- [`industry/products/`](industry/products/)

### Context continuity

- [`context/CURRENT.md`](context/CURRENT.md) — repository-level current state for fast cross-session recovery
- [`context/TOPIC_INDEX.md`](context/TOPIC_INDEX.md) — lightweight routing index for long-lived topics
- [`context/topics/`](context/topics/) — current state of a small number of long-lived topics
- [`context/checkpoints/`](context/checkpoints/) — delta logs for meaningful cognitive or project-state changes
- [`context/README.md`](context/README.md) — schemas, update rules, progressive loading, and compaction

The context layer does **not** replace Questions, Hypotheses, Research, or Evidence:

`Checkpoint = change event` · `Topic = current state` · `Question = unknown` · `Hypothesis = testable belief` · `Research / Evidence = support and challenge`.

New AI sessions should use **progressive context loading**: start with `AGENTS.md → context/CURRENT.md → context/TOPIC_INDEX.md → 1–3 relevant Topic States`, and only then drill into Problems, Hypotheses, Checkpoints, Research, or Evidence as needed.

### AI context

- [`ai-context/PROJECT_CONTEXT.md`](ai-context/PROJECT_CONTEXT.md) — stable project background; no longer the default full-session bootstrap
- [`ai-context/PAPER_READING_MODE.md`](ai-context/PAPER_READING_MODE.md)

## Bilingual Publication Policy

> **Research in Chinese; publish mature ideas bilingually.**

Working notes, cognitive evolution, paper walkthroughs, and active research state remain Chinese-first. Stable public concepts are progressively rewritten in English rather than mechanically translated.

## Research Discipline

- **Problem first, material second; mechanism before engineering; hypothesis before principle.**
- The unit of work is an **Active Problem**, not an Active Paper.
- Papers are dynamically classified A / B / C; not every important paper deserves the same reading depth.
- Treat Q1–Q5 as the long-term problem map and public theory / industry evidence as evidence streams.
- Private experience may inspire a question, but public claims must stand on public evidence alone.
- Do not let academic theory monopolize the project, and do not let industry marketing substitute for validation.
- Maintain counter-evidence so that problem-driven research does not become confirmation bias.
- Do not create top-level frameworks around temporary technology labels such as MCP, RAG, Ontology, Agent, or Harness.
- Record major cognitive changes in `EVOLUTION.md`.
- Technical architecture should be traceable back to organizational and business problems where possible.
- A-class papers follow: **Source Walkthrough → Concept Reconstruction → Research Interpretation → Human Takeaways → Engineering Bridge**.
- An AI Proposal does not automatically become a Judgment or a Stable Principle.

## Status

Initialized on **2026-09-04**. On **2026-09-11**, the research method shifted from sequential paper progression toward a **problem-driven research loop**. The current human research Problem Family is **RP-002**, with **RP-002-01｜World Model Conflict & Evolution** as the human research frontier. Research Runner v0.4 is separately piloting **RP-002-02｜Business Action Layer**. These are different operating planes rather than competing definitions of one global “active problem”; the machine-readable registry is `REPOSITORY_STATE.yaml`.

---

This repository is a living research system rather than a finished framework. Claims and principles will be revised as evidence changes.
