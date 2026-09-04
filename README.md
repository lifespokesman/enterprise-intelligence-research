# Enterprise Intelligence Research

**English** | [简体中文](README.zh-CN.md)

> A living research project on Enterprise Intelligence and AI-era Organization Design.

This repository starts from a question that sits above “how to build an AI agent”:

**What happens to cognition, decision rights, coordination, accountability, firm boundaries, and organizational learning when AI becomes a non-human actor capable of understanding, judging, planning, invoking capabilities, and acting over time?**

## Working Definition: Enterprise Intelligence

Current working definition:

> **Enterprise intelligence is an organizational capability: the ability of an organization to configure cognition, decision rights, action capacity, and learning under goals, resource constraints, institutional rules, and risk boundaries, so that it can continuously sense its environment, interpret reality, form judgments, organize capabilities, act, and adapt from feedback.**

A simplified loop:

`Sense → Understand → Judge → Organize → Act → Feedback → Learn`

This project distinguishes three levels of intelligence:

- **Model Intelligence** — reasoning, prediction, interpretation, and generation capabilities of a model.
- **Subject Intelligence** — the ability of an intelligent subject to pursue goals, maintain context, make judgments, act, and adapt over time.
- **Enterprise Intelligence** — an organizational property that emerges from how humans, AI, software, data, and assets are configured into a working system of cognition, decision, action, and learning.

A core proposition of this project is:

> **Enterprise intelligence is not an additive property of individual AI agents.**

A firm may deploy highly capable agents and still remain organizationally unintelligent if decision rights are poorly allocated, semantics are inconsistent, coordination fails, accountability is unclear, or experience does not become organizational learning.

[Read the full topic →](topics/en/enterprise-intelligence.md)

## Five Long-Term Research Questions

1. **Decision Rights** — How should decision rights be reallocated when humans and AI possess different cognitive advantages, limitations, and responsibility-bearing capacities?
2. **Accountability & Agency** — When AI can participate in decisions but cannot bear social, professional, or legal consequences in the human sense, how should authority, risk, and accountability remain connected?
3. **Coordination** — How should humans, agents, software, and enterprise assets coordinate? Could a shared enterprise world model become a new semantic coordination infrastructure?
4. **Firm Boundaries** — If AI lowers the cost of discovering, negotiating with, coordinating, and monitoring capabilities, which capabilities should remain inside the firm and which can be dynamically assembled across organizational boundaries?
5. **Organizational Learning** — How can traces, outcomes, failures, feedback, and agent experience become durable organizational knowledge, skills, rules, evaluation assets, and policies rather than disappear inside isolated AI sessions?

[Read the research questions →](topics/en/README.md)

## Public Evidence Architecture: Theory × Industry Evidence

The five questions above are the **problem map**. They are not answered by academic papers alone.

This public repository uses only evidence that can be independently supported by public sources:

- **Academic Theory** — concepts, mechanisms, boundary conditions, and testable propositions;
- **Product Fact** — publicly verifiable product mechanisms, architectures, and operating models;
- **Product Claim** — a vendor's public explanation of value, trends, advantages, or organizational implications;
- **Industry Case** — publicly verifiable enterprise practices and reported outcomes;
- **Analyst View** — cross-company analysis from consulting, investment, or industry research organizations;
- **Policy / Standard** — public laws, regulations, industry standards, and technical standards;
- **Counter Evidence** — failures, alternatives, contrary data, and boundary conditions.

The intended research loop is:

`Q1–Q5 → Theory + Public Industry Evidence → Hypothesis → Judgment → Engineering / Governance Implication`

A core boundary is:

> **Private experience may inspire a question, but every public claim must be independently supportable by public evidence.**

Evidence identities must remain distinct:

> **Product Claim ≠ Validated Theory**  
> **Vendor Case ≠ Independent Evidence**  
> **Analyst View ≠ Academic Theory**  
> **Public Success Case ≠ General Law**

Public industry research is maintained under [`industry/`](industry/).

## Industry Research Roadmap: Engineering × Governance

The industry roadmap is not organized by vendor. It is derived from the long-term engineering and governance problems that arise when intelligent subjects enter real enterprises.

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

A long-term hypothesis being tested here is that an AI-native enterprise may increasingly be organized around the interaction of:

**Intelligent Subject × Enterprise World Model × Capability Network × Real-world Feedback**

This is a research hypothesis, not a prediction presented as fact. The repository is designed to preserve supporting evidence, counter-evidence, and revisions over time.

## Research Architecture

The current academic study map has six learning modules:

1. **Why organizations exist** — Simon, Coase, Williamson
2. **Division of labor and coordination** — Mintzberg, Organization Design, Information Processing
3. **Authority, delegation, and accountability** — Agency Theory, Decision Rights, Delegation
4. **Organizational learning** — March, Argyris & Schön, Organizational Memory
5. **AI as an organizational actor** — Human-AI teams, multi-agent organizations, AI decision-making
6. **Re-deriving Enterprise Intelligence** — using organizational questions to rethink intelligent-subject relationships, engineering, and governance

Academic theory is one public evidence stream, not the whole research system.

## Repository Structure

### Human-facing research cockpit

- [`NOW.md`](NOW.md) — current research focus, progress, blockers, and the next single action
- [`JUDGMENTS.md`](JUDGMENTS.md) — current working judgments worth preserving over time

### Public research topics

- [`topics/enterprise-intelligence.md`](topics/enterprise-intelligence.md) — 中文：企业智能
- [`topics/en/enterprise-intelligence.md`](topics/en/enterprise-intelligence.md) — English: Enterprise Intelligence
- [`topics/README.md`](topics/README.md) — 中文：五个长期组织问题
- [`topics/en/README.md`](topics/en/README.md) — English: Five Long-Term Research Questions

### Academic research

- [`research/scholars.md`](research/scholars.md) — scholar map
- [`research/theory-map.md`](research/theory-map.md) — classical organization theory and AI pressure tests
- [`research/reading-list.md`](research/reading-list.md) — current reading path
- `research/paper-reviews/` — source walkthroughs and research interpretations, currently Chinese-first

### Public industry evidence

- [`industry/README.md`](industry/README.md) — evidence rules for public industry research
- [`industry/ROADMAP.md`](industry/ROADMAP.md) — Intelligent Subject Engineering × Governance roadmap
- [`industry/cases/`](industry/cases/) — public enterprise cases
- [`industry/products/`](industry/products/) — product mechanisms, product philosophy, and company-level AI assumptions

### AI context

- [`ai-context/PROJECT_CONTEXT.md`](ai-context/PROJECT_CONTEXT.md) — long-term research context and maintenance rules for AI collaborators

## Bilingual Publication Policy

This repository does **not** mechanically translate every research note.

The current policy is:

> **Research in Chinese; publish mature ideas bilingually.**

Working notes, paper walkthroughs, open hypotheses, and research state remain Chinese-first so that the research process stays cognitively efficient. Stable concepts and public-facing topics are progressively rewritten in English for international discussion.

English versions are intended to be **conceptual and academic reframings**, not literal translations.

## Research Discipline

- Treat **Q1–Q5 as the problem map** and **Theory + Public Industry Evidence as public evidence streams**; do not confuse these levels.
- This public repository does not store, cite, or describe private, customer, company-internal, or non-public project material.
- Private experience may inspire research questions, but public claims must stand on public evidence alone.
- Do not let academic theory monopolize the project, and do not let industry marketing substitute for validation.
- Do not create top-level frameworks around temporary technology labels such as MCP, RAG, Ontology, Agent, or Harness.
- Separate **long-term questions, current judgments, evolutionary hypotheses, evidence, and counter-evidence**.
- New technologies should first be used to update an existing research question rather than create a new conceptual tree.
- Technical architecture should, where possible, be traceable back to organizational problems.
- New papers are read in this order: **source walkthrough → concept reconstruction → research interpretation → human takeaways → possible judgment update**.
- Industry research follows: **Product Fact / Claim → Public Case → Analyst / Policy / Counter Evidence → Q1–Q5 → Judgment**.

## Status

Initialized on **2026-09-04**. The project is still building its organization-theory coordinate system while establishing a public industry roadmap around **Intelligent Subject Engineering × Governance**. The current active research question remains paper comprehension rather than broad vendor collection.

---

This repository is a living research system rather than a finished framework. Claims will be revised as evidence changes.
