# FPF Ontology Analysis for Corporate Context Automation

> **Purpose:** Systematic analysis of the First Principles Framework (FPF) to create an ontology meta-model for examining corporate context (docs, messages, emails, calls, communications) with the goal of identifying automations and shortcuts using AI models, tooling, MCP, skills, and tasks.

**Analysis Date:** 2026-02-05
**Source Document:** `First Principles Framework — Core Conceptual Specification (holonic).md`
**Total Lines:** 37,533
**Key Sections Analyzed:** A.1-A.3, A.15, B.3, F.17, Part G

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [FPF Core Concepts Extracted](#fpf-core-concepts-extracted)
3. [Corporate Context Ontology Mapping](#corporate-context-ontology-mapping)
4. [Automation Discovery Framework](#automation-discovery-framework)
5. [Final Ontology Meta-Model](#final-ontology-meta-model)
6. [FPF Skill Definition for Claude Code](#fpf-skill-definition-for-claude-code)
7. [References to Source Document](#references-to-source-document)

---

## Executive Summary

The First Principles Framework (FPF) provides a **generative pattern language** for modeling complex systems and knowledge. It is particularly well-suited for corporate context analysis because it:

1. **Distinguishes actors from artifacts** (U.System vs U.Episteme) - critical for separating who acts from what is acted upon
2. **Localizes meaning** (U.BoundedContext) - essential for multi-department organizations with different vocabularies
3. **Tracks trust and evidence** (F-G-R calculus) - vital for document reliability and compliance
4. **Models transformations explicitly** (Transformer Quartet) - key for identifying automatable workflows
5. **Bridges contexts with explicit loss tracking** (CL levels) - crucial for cross-team communication

**Key FPF Abstractions for Corporate Automation:**
- **Holon** → Any corporate entity (team, document, process)
- **Transformer Quartet** → Workflow automation patterns
- **Trust Calculus** → Document quality assessment
- **Bounded Context** → Department/project vocabularies
- **Unified Term Sheet** → Cross-team terminology alignment

---

## FPF Core Concepts Extracted

### 1. Holonic Foundation (A.1)

**Source:** Lines 756-912

| Concept | Definition | Corporate Mapping |
|---------|------------|-------------------|
| `U.Entity` | Anything that can be individuated | Any identifiable corporate item |
| `U.Holon` | Entity that is simultaneously whole and part | Teams, documents, processes |
| `U.System` | Physical/operational holon that can ACT | Employees, AI agents, automated systems |
| `U.Episteme` | Knowledge holon (cannot act, only BE ACTED UPON) | Documents, emails, policies, data |
| `U.Boundary` | What separates inside from outside | Department scope, access controls |
| `U.Interaction` | Flow crossing a boundary | Communications, data transfers |

**Key Invariant:** Only `U.System` can perform `U.Work`. An `U.Episteme` (document) never "does" anything - it is always transformed BY a system.

### 2. Bounded Context (A.1.1)

**Source:** Lines 915-1037

A `U.BoundedContext` is the **semantic frame** where terms have specific meanings.

**Corporate Examples:**
| Context | Glossary Example | Invariants |
|---------|------------------|------------|
| `SalesTeam:Q1_2026` | "Lead" = potential customer | "Lead cannot be Closed without Demo" |
| `Engineering:Sprint_42` | "Lead" = tech lead role | "PR requires 2 approvers" |
| `Legal:Contracts_2026` | "Lead" = primary party | "All clauses must have review date" |

**Key Rule:** The same word ("Lead") means different things in different contexts. Cross-context communication requires explicit **Bridges** with **Congruence Level (CL)**.

### 3. Role System (A.2, A.2.1)

**Source:** Lines 1038-1400

| Concept | Definition | Corporate Mapping |
|---------|------------|-------------------|
| `U.Role` | Contextual mask a holon wears | Job title, project role |
| `U.RoleAssignment` | Binding of holder to role in context | "Alice is ProjectManager in ProjectX" |
| `U.RoleEnactment` | Run-time record that Work was done under an assignment | Audit log entry |

**Canonical Format:** `Holder#Role:Context@Window`
- Example: `Alice#ProjectManager:ProjectX@2026-Q1`

**Role Families:**
| Family | Eligible Holder | Examples |
|--------|-----------------|----------|
| Agential/Behavioral | U.System only | Approver, Executor, Reviewer |
| Epistemic-Status | U.Episteme only | Evidence, Standard, Requirement |
| Normative-Status | U.Episteme only | Policy, Regulation, Guideline |

### 4. Transformer Quartet (A.3)

**Source:** Lines 4210-4409

The **fundamental pattern for modeling any action or change**:

```
┌─────────────────────────────────────────────────────────────┐
│                    TRANSFORMER QUARTET                       │
├─────────────────────────────────────────────────────────────┤
│  1. ACTING SIDE: System bearing TransformerRole             │
│     (WHO acts - employee, AI agent, automated system)       │
│                                                             │
│  2. METHOD DESCRIPTION: Recipe/SOP/Algorithm (U.Episteme)   │
│     (HOW to do it - design-time artifact)                   │
│                                                             │
│  3. METHOD: Capability the system can enact                 │
│     (WHAT capability is being exercised)                    │
│                                                             │
│  4. WORK: Dated execution producing state change            │
│     (WHAT actually happened - run-time record)              │
└─────────────────────────────────────────────────────────────┘
```

**Corporate Translation:**
| FPF Concept | Corporate Equivalent | Design/Run |
|-------------|---------------------|------------|
| MethodDescription | SOP, Playbook, Runbook | Design-time |
| Method | Skill, Competency, Tool | Design-time |
| Work | Task execution, Action log | Run-time |
| Transformer | Employee/AI performing the work | Run-time |

**Key Rule:** Never confuse the recipe (MethodDescription) with the execution (Work).

### 5. Trust & Assurance Calculus (B.3)

**Source:** Lines 14041-14240

Every claim has an **assurance tuple**: `⟨F, G, R, Notes⟩`

| Characteristic | Scale | Meaning | Corporate Use |
|---------------|-------|---------|---------------|
| **F (Formality)** | Ordinal (F0-F3) | How rigorous is the structure | Document formalization level |
| **G (ClaimScope)** | Set-based coverage | Where does it apply | Applicability scope |
| **R (Reliability)** | Ratio [0,1] | How well is it supported | Evidence quality |
| **CL (Congruence)** | Ordinal (CL0-CL3) | How well parts fit | Integration quality |

**Aggregation Rules (Conservative):**
```
F_eff = min(F_i)           // Weakest-link on formality
G_eff = SpanUnion({G_i})   // Coverage union
R_eff = max(0, min(R_i) - Φ(CL_min))  // Reliability with CL penalty
```

**Corporate Application:** Document quality scoring, compliance assessment, knowledge base reliability.

### 6. Unified Term Sheet (F.17)

**Source:** Lines 33957-34156

The **publication surface** for cross-context terminology alignment.

**Row Schema:**
| Field | Purpose |
|-------|---------|
| FPF U.Type | Canonical kernel type |
| Unified Tech name | Technical name for spec prose |
| Unified Plain name | Everyday name for non-specialists |
| SenseCells (by context) | How each context "says" this concept |
| Bridges (CL/Loss) | Cross-context mappings with CL level |
| Unification Rationale | Why these senses are the same concept |

---

## Corporate Context Ontology Mapping

### Document Types as U.Episteme Subtypes

| Corporate Artifact | FPF Role | Status Family | Trust Characteristics |
|-------------------|----------|---------------|----------------------|
| **Email** | U.Episteme:Message | Communication | F:0-1, R:varies, transient |
| **Meeting Notes** | U.Episteme:Record | Evidence | F:1, R:depends on author |
| **Policy Document** | U.Episteme:Normative | Standard/Requirement | F:2-3, R:high if approved |
| **Contract** | U.Episteme:Agreement | Commitment | F:3, R:legally binding |
| **Code** | U.Episteme:Specification | MethodDescription | F:2-3, R:depends on tests |
| **Report** | U.Episteme:Analysis | Evidence | F:1-2, R:depends on data |
| **Ticket/Issue** | U.Episteme:Request | Requirement | F:1, R:varies |
| **Slack Message** | U.Episteme:Ephemeral | Communication | F:0, R:context-dependent |

### Communication Flows as U.Interaction

| Communication Type | Boundary Crossing | Automation Potential |
|-------------------|-------------------|---------------------|
| Internal Email | Same context | Classification, routing, response drafting |
| External Email | Cross-context (requires Bridge) | CL assessment, translation, compliance check |
| Meeting | Synchronous multi-party | Transcription, action extraction, summary |
| Document Handoff | Context transition | Version control, approval workflow |
| API Call | System-to-system | Full automation, monitoring |

### Organizational Structure as Holarchy

```
Company (U.System:Organization)
├── Department (U.System:Department)
│   ├── Team (U.System:Team)
│   │   ├── Employee (U.System:Person)
│   │   │   └── Roles: [Manager, Engineer, Analyst]
│   │   └── AI Agent (U.System:Agent)
│   │       └── Roles: [Assistant, Reviewer, Generator]
│   └── Shared Services
│       └── Tools (U.System:Automated)
└── Knowledge Base (U.Episteme:Repository)
    ├── Policies (U.Episteme:Normative)
    ├── Procedures (U.Episteme:MethodDescription)
    └── Records (U.Episteme:Evidence)
```

---

## Automation Discovery Framework

Using FPF patterns to systematically identify automation opportunities:

### Step 1: Map Current State (Transformer Quartet Analysis)

For each business process, identify:

```
┌────────────────────────────────────────────────────────────┐
│ PROCESS: [Name]                                            │
├────────────────────────────────────────────────────────────┤
│ TRANSFORMER: Who currently performs this?                  │
│   □ Human only                                             │
│   □ Human + Tool assist                                    │
│   □ Automated with human oversight                         │
│   □ Fully automated                                        │
├────────────────────────────────────────────────────────────┤
│ METHOD DESCRIPTION: Where is the recipe?                   │
│   □ Tacit knowledge (undocumented)                        │
│   □ Informal docs (wiki, notes)                           │
│   □ Formal SOP/Playbook                                   │
│   □ Executable specification (code)                        │
├────────────────────────────────────────────────────────────┤
│ WORK OUTPUT: What is produced?                             │
│   □ Document/Episteme modification                         │
│   □ State change in system                                 │
│   □ Communication/Notification                             │
│   □ Decision/Approval                                      │
├────────────────────────────────────────────────────────────┤
│ TRUST REQUIREMENTS: What assurance level needed?           │
│   F: [0-3]  G: [scope]  R: [0-1]                          │
└────────────────────────────────────────────────────────────┘
```

### Step 2: Identify Automation Patterns

| Pattern | FPF Mapping | AI/Tool Application |
|---------|-------------|---------------------|
| **Document Classification** | U.Episteme → RoleAssignment | LLM classification to assign status roles |
| **Information Extraction** | U.Episteme → Structured data | NER, relation extraction |
| **Workflow Routing** | Method → RoleAssignment | Rule-based + ML routing |
| **Response Generation** | MethodDescription → Work | LLM with template/RAG |
| **Compliance Checking** | U.Episteme vs Normative | Rule engine + LLM |
| **Summary/Synthesis** | Multiple U.Episteme → New U.Episteme | LLM aggregation |
| **Translation/Bridge** | Context A → Bridge → Context B | LLM with CL assessment |

### Step 3: Assess Automation Candidates

Using Trust Calculus to evaluate automation suitability:

| Automation Level | F Requirement | R Requirement | Human Oversight |
|-----------------|---------------|---------------|-----------------|
| Full automation | F ≥ 2 (formal spec exists) | R ≥ 0.95 | None needed |
| Assisted automation | F ≥ 1 | R ≥ 0.80 | Review sample |
| Suggestion only | Any F | R ≥ 0.60 | Human decision |
| Not suitable | - | R < 0.60 | Keep manual |

### Step 4: Design Automation Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    AUTOMATION STACK                          │
├─────────────────────────────────────────────────────────────┤
│ Layer 5: GOVERNANCE                                          │
│   - Trust/Assurance monitoring (F-G-R tracking)             │
│   - Audit trails (Work → MethodDescription traceability)    │
│   - Evolution management (version control)                   │
├─────────────────────────────────────────────────────────────┤
│ Layer 4: ORCHESTRATION                                       │
│   - Workflow engine (Method composition via Γ_method)       │
│   - Role routing (RoleAssignment resolution)                 │
│   - Context bridging (CL-aware translation)                  │
├─────────────────────────────────────────────────────────────┤
│ Layer 3: AI CAPABILITIES                                     │
│   - LLMs (generation, classification, extraction)           │
│   - MCP servers (tool execution)                            │
│   - Skills (packaged MethodDescriptions)                    │
│   - RAG (evidence-grounded generation)                      │
├─────────────────────────────────────────────────────────────┤
│ Layer 2: DATA & KNOWLEDGE                                    │
│   - Document store (U.Episteme repository)                  │
│   - Context registry (U.BoundedContext catalog)             │
│   - Term sheets (UTS for cross-context alignment)           │
│   - Evidence graphs (provenance tracking)                    │
├─────────────────────────────────────────────────────────────┤
│ Layer 1: INTEGRATION                                         │
│   - Email/calendar connectors                               │
│   - Document management APIs                                 │
│   - Communication platform hooks                             │
│   - Database/CRM integrations                                │
└─────────────────────────────────────────────────────────────┘
```

---

## Final Ontology Meta-Model

### Core Types (U.Type Hierarchy)

```
U.Entity
└── U.Holon
    ├── U.System (CAN ACT)
    │   ├── U.Person
    │   ├── U.Team
    │   ├── U.Organization
    │   ├── U.AIAgent
    │   └── U.AutomatedService
    │
    └── U.Episteme (CANNOT ACT, only be acted upon)
        ├── U.Document
        │   ├── U.Policy (Normative role)
        │   ├── U.Procedure (MethodDescription role)
        │   ├── U.Contract (Commitment role)
        │   └── U.Report (Evidence role)
        ├── U.Message
        │   ├── U.Email
        │   ├── U.ChatMessage
        │   └── U.Notification
        ├── U.Record
        │   ├── U.MeetingNotes
        │   ├── U.AuditLog
        │   └── U.TransactionRecord
        └── U.Data
            ├── U.Dataset
            ├── U.Model
            └── U.Configuration
```

### Core Relations

```
TRANSFORMATION RELATIONS:
  U.System --[bears]--> U.Role --[in]--> U.BoundedContext
  U.System --[performs]--> U.Work --[executionOf]--> U.MethodDescription
  U.Work --[transforms]--> U.Holon
  U.Work --[produces]--> U.Episteme

STRUCTURAL RELATIONS:
  U.Holon --[partOf]--> U.Holon (mereology)
  U.Holon --[boundaryOf]--> U.Boundary
  U.BoundedContext --[bridges]--> U.BoundedContext --[withCL]--> CL_Level

EPISTEMIC RELATIONS:
  U.Episteme --[describesEntity]--> U.Holon
  U.Episteme --[hasEvidenceFor]--> U.Claim
  U.Claim --[hasAssurance]--> ⟨F, G, R⟩
```

### Automation-Relevant Patterns

#### Pattern 1: Document Processing Pipeline
```
Input: U.Episteme:Raw
→ Classification (assign U.Role to episteme)
→ Extraction (create structured U.Episteme)
→ Routing (determine U.RoleAssignment for action)
→ Action (U.System performs U.Work)
→ Output: U.Episteme:Processed + U.Work:Log
```

#### Pattern 2: Cross-Context Communication
```
Source: U.Episteme in Context_A
→ Bridge identification (F.9)
→ CL assessment (B.3)
→ Translation with loss notes
→ Target: U.Episteme in Context_B
→ Validation: R_target ≤ R_source - Φ(CL)
```

#### Pattern 3: Workflow Automation
```
Trigger: U.Episteme state change
→ Match MethodDescription
→ Resolve U.RoleAssignment (who should act)
→ If AI-eligible: spawn AI U.Work
→ Else: notify human Transformer
→ Record U.Work with full provenance
```

---

## FPF Skill Definition for Claude Code

### Skill Metadata

```yaml
name: fpf-ontology-modeling
version: 1.0.0
description: |
  Apply First Principles Framework (FPF) patterns for systematic ontology
  modeling of corporate contexts, enabling automation discovery and
  knowledge architecture design.

triggers:
  - "ontology"
  - "systematic modeling"
  - "FPF"
  - "corporate context"
  - "automation discovery"
  - "knowledge architecture"
  - "document classification"
  - "workflow analysis"
```

### Skill Prompt

```markdown
# FPF Ontology Modeling Skill

You are applying the First Principles Framework (FPF) for systematic modeling.

## Core Concepts to Apply

### 1. Holon Distinction (A.1)
- **U.System**: Anything that CAN ACT (people, AI, automated services)
- **U.Episteme**: Anything that CANNOT ACT (documents, data, knowledge)
- Rule: Only systems perform work; epistemes are transformed BY systems

### 2. Bounded Context (A.1.1)
- Every term has meaning ONLY within its context
- Cross-context communication requires explicit Bridges with Congruence Level (CL)
- CL0=weak guess, CL1=plausible, CL2=validated, CL3=verified equivalence

### 3. Transformer Quartet (A.3)
For any action or change, identify:
1. **Acting Side**: System bearing TransformerRole (WHO)
2. **MethodDescription**: Recipe/SOP (HOW - design-time)
3. **Method**: Capability being exercised (WHAT capability)
4. **Work**: Actual execution record (WHAT happened - run-time)

### 4. Trust Calculus (B.3)
Assess every claim with: ⟨F, G, R⟩
- **F (Formality)**: How rigorous (F0=informal → F3=proof-grade)
- **G (Scope)**: Where it applies (set-based coverage)
- **R (Reliability)**: How well supported [0-1]
- Aggregation: F_eff=min(F_i), R_eff=min(R_i)-Φ(CL_min)

### 5. Role Assignment (A.2)
- Format: `Holder#Role:Context@TimeWindow`
- Role families: Behavioral (systems only), Status (epistemes only)
- Example: `Alice#Approver:ProjectX@2026-Q1`

## Modeling Process

When asked to model a corporate context:

1. **Identify Holons**
   - List all systems (actors) and epistemes (artifacts)
   - Classify each: can it ACT or only BE ACTED UPON?

2. **Define Bounded Contexts**
   - What are the vocabulary boundaries?
   - Where do terms mean different things?
   - What bridges exist between contexts?

3. **Map Transformations**
   - For each process: who acts, what recipe, what output?
   - Distinguish design-time (MethodDescription) from run-time (Work)

4. **Assess Trust Requirements**
   - What formality level is needed?
   - What scope does each claim cover?
   - What evidence supports reliability?

5. **Identify Automation Opportunities**
   - Which transformations have formal MethodDescriptions?
   - Which can be performed by AI systems?
   - What CL level is required for cross-context automation?

## Output Format

Provide structured analysis with:
- Holon inventory (systems vs epistemes)
- Context map with bridges
- Transformation patterns (Quartet analysis)
- Trust assessment table
- Automation recommendations with required CL/F/R levels
```

### Usage Examples

**Example 1: Email Processing System**
```
User: Model our email triage process using FPF

Assistant Analysis:
HOLONS:
- U.System: EmailServer, TriageBot, SupportAgent, Manager
- U.Episteme: IncomingEmail, TriageRules, ResponseTemplate, TicketRecord

BOUNDED CONTEXTS:
- CustomerSupport:2026 (vocabulary: ticket, priority, SLA)
- Engineering:Sprint_N (vocabulary: bug, feature, story)
- Bridge: CustomerSupport ↔ Engineering, CL=2 (validated mapping)

TRANSFORMER QUARTET for "Triage Email":
1. Acting Side: TriageBot#Classifier:CustomerSupport
2. MethodDescription: TriageRules (F=2, formal decision tree)
3. Method: ClassifyAndRoute
4. Work: ClassificationRun_2026-02-05_14:32 (assigned priority=P2, routed to Engineering)

TRUST: ⟨F=2, G=all_incoming_email, R=0.87⟩
AUTOMATION: Full automation suitable (F≥2, R>0.80)
```

**Example 2: Contract Review Workflow**
```
User: Analyze our contract review process for automation opportunities

Assistant Analysis:
HOLONS:
- U.System: LegalTeam, ContractBot, Approver, ExternalCounsel
- U.Episteme: DraftContract, ReviewChecklist, ApprovalRecord, SignedContract

BOUNDED CONTEXTS:
- Legal:Contracts_2026
- Finance:Procurement_2026
- Bridge: Legal ↔ Finance, CL=2

TRANSFORMER QUARTET for "Review Contract Clause":
1. Acting Side: ContractBot#Reviewer:Legal
2. MethodDescription: ReviewChecklist (F=3, formal legal standards)
3. Method: ClauseAnalysis
4. Work: Review_Contract_1234_Clause_5.2

TRUST ASSESSMENT:
| Step | F | R | Automation |
|------|---|---|------------|
| Initial scan | 1 | 0.95 | Full auto |
| Risk flagging | 2 | 0.82 | Assisted |
| Final approval | 3 | - | Human required |
```

---

## References to Source Document

| Reference ID | Line Range | Topic | Key Concepts |
|--------------|------------|-------|--------------|
| REF-001 | 1-200 | Table of Contents | Structure overview, Part A-K |
| REF-002 | 289-620 | Preface | FPF philosophy, creativity + assurance |
| REF-003 | 756-912 | A.1 Holonic Foundation | U.Entity, U.Holon, U.System, U.Episteme |
| REF-004 | 915-1037 | A.1.1 Bounded Context | Semantic frames, local meaning |
| REF-005 | 1038-1400 | A.2 Role Taxonomy | U.Role, U.RoleAssignment |
| REF-006 | 1220-1400 | A.2.1 RoleAssignment | RCS, RSG, eligibility matrix |
| REF-007 | 4210-4409 | A.3 Transformer Quartet | Acting side, Method, MethodDescription, Work |
| REF-008 | 14041-14240 | B.3 Trust Calculus | F-G-R tuple, CL, aggregation rules |
| REF-009 | 33957-34156 | F.17 UTS | Unified Term Sheet, cross-context alignment |

---

## Appendix: Quick Reference Card

### FPF → Corporate Glossary

| FPF Term | Plain English | Example |
|----------|---------------|---------|
| U.Holon | Any thing that is both a whole and a part | A team (whole of members, part of department) |
| U.System | Actor that can do things | Employee, AI bot, automated service |
| U.Episteme | Knowledge artifact that cannot act | Document, email, policy |
| U.BoundedContext | Vocabulary boundary | Department jargon, project terminology |
| U.Role | Hat someone wears | Manager role, Reviewer role |
| U.RoleAssignment | Who wears what hat where | "Alice is Approver in ProjectX" |
| MethodDescription | Recipe/playbook | SOP document, runbook |
| Method | Capability to do | Skill, competency |
| Work | Actual execution | Task completion, action taken |
| F (Formality) | How rigorous | F0=informal, F3=legally binding |
| G (Scope) | Where it applies | "All contracts over $10K" |
| R (Reliability) | How trustworthy | 0.95 = very reliable |
| CL (Congruence) | How well things fit | CL3=perfect match, CL0=guess |

### Automation Decision Matrix

| MethodDescription exists? | F level | R level | Recommendation |
|--------------------------|---------|---------|----------------|
| No (tacit knowledge) | - | - | Document first |
| Yes, informal | F0-F1 | Any | Assisted automation |
| Yes, structured | F2 | R < 0.8 | Human oversight |
| Yes, structured | F2 | R ≥ 0.8 | Full automation OK |
| Yes, formal | F3 | Any | Full automation recommended |

---

*Document generated: 2026-02-05*
*Based on FPF Core Specification v2025-09*