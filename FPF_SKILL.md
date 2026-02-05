# FPF Ontology Modeling Skill

> A Claude Code skill for applying First Principles Framework (FPF) patterns to corporate context analysis, systematic modeling, and automation discovery.

## Skill Overview

**Name:** `fpf-ontology`
**Version:** 1.0.0
**Purpose:** Apply FPF's rigorous ontology patterns to model corporate contexts (documents, communications, workflows) and systematically identify automation opportunities.

---

## When to Use This Skill

Invoke this skill when the user wants to:
- **Systematically model** a business domain, process, or organization
- **Analyze documents** for classification, routing, or processing automation
- **Map terminology** across teams or departments
- **Identify automation opportunities** in workflows
- **Assess document/data quality** using trust calculus
- **Design knowledge architectures** for corporate contexts
- **Brainstorm** with structured, auditable methodology

**Trigger phrases:**
- "Model this using FPF"
- "Systematic analysis of..."
- "Ontology for..."
- "What can we automate?"
- "Map the terminology between..."
- "Assess the reliability of..."

---

## Core FPF Concepts

### 1. The System/Episteme Split (A.1)

**Critical Distinction:** Everything is either:
- **U.System** - CAN ACT (people, AI agents, automated services, teams)
- **U.Episteme** - CANNOT ACT, only be acted upon (documents, data, knowledge)

**Rule:** Documents never "do" things. Only systems perform work.
- Wrong: "The policy enforces compliance"
- Right: "The compliance officer (System) enforces the policy (Episteme)"

### 2. Bounded Context (A.1.1)

Every term has meaning ONLY within its context. The word "lead" means:
- In Sales context: potential customer
- In Engineering context: tech lead role
- In Legal context: primary party

**Cross-context communication requires explicit Bridges** with declared Congruence Level:
- CL0: Weak guess
- CL1: Plausible mapping
- CL2: Validated mapping
- CL3: Verified equivalence

### 3. Transformer Quartet (A.3)

For ANY action or change, identify four components:

```
┌─────────────────────────────────────────────────────┐
│ 1. ACTING SIDE (WHO)                                │
│    System bearing TransformerRole                   │
│    → Employee, AI agent, automated service          │
├─────────────────────────────────────────────────────┤
│ 2. METHOD DESCRIPTION (HOW - design time)           │
│    Recipe/SOP/Playbook (an Episteme)                │
│    → The documented procedure                       │
├─────────────────────────────────────────────────────┤
│ 3. METHOD (WHAT capability)                         │
│    The ability being exercised                      │
│    → Skill, competency, tool capability             │
├─────────────────────────────────────────────────────┤
│ 4. WORK (WHAT happened - run time)                  │
│    Dated execution with resource consumption        │
│    → The actual task execution record               │
└─────────────────────────────────────────────────────┘
```

**Key Rule:** Never confuse the recipe (MethodDescription) with the execution (Work).

### 4. Trust Calculus (B.3)

Every claim has an assurance tuple: **⟨F, G, R⟩**

| Characteristic | Scale | Meaning |
|---------------|-------|---------|
| **F (Formality)** | F0-F3 (ordinal) | How rigorous the structure |
| **G (ClaimScope)** | Set-based | Where it applies |
| **R (Reliability)** | 0-1 (ratio) | How well supported by evidence |

**Conservative Aggregation:**
```
F_eff = min(F_i)                    // Weakest link
R_eff = min(R_i) - Φ(CL_min)        // Reliability with congruence penalty
```

### 5. Role Assignment (A.2)

**Canonical Format:** `Holder#Role:Context@TimeWindow`

Example: `Alice#ProjectManager:ProjectX@2026-Q1`

**Role Families:**
| Family | Can be held by | Examples |
|--------|---------------|----------|
| Behavioral/Agential | U.System only | Approver, Executor, Reviewer |
| Epistemic-Status | U.Episteme only | Evidence, Standard, Requirement |

---

## Modeling Process

When asked to model a corporate context, follow this process:

### Step 1: Identify Holons

List all entities and classify each:

| Entity | Type | Justification |
|--------|------|---------------|
| ? | U.System | Can it ACT? |
| ? | U.Episteme | Can only BE ACTED UPON? |

### Step 2: Define Bounded Contexts

For each vocabulary boundary:
- Name and version the context
- List key terms with local meanings
- Identify invariants (local rules)

### Step 3: Map Bridges

For cross-context communication:
- Identify source and target contexts
- Assess Congruence Level (CL0-CL3)
- Document loss notes (what information is lost in translation)

### Step 4: Analyze Transformations

For each process/workflow, fill out the Quartet:

```
PROCESS: [Name]
─────────────────────────────────
Acting Side: [System]#[Role]:[Context]
MethodDescription: [Document/SOP] (F=[0-3])
Method: [Capability name]
Work: [Execution record pattern]
Output: [What is produced]
```

### Step 5: Assess Trust Requirements

For each transformation:
- Required Formality (F): What rigor is needed?
- Required Reliability (R): What confidence level?
- Evidence sources: What supports the claim?

### Step 6: Identify Automation Opportunities

| Automation Level | Requirements | Human Oversight |
|-----------------|--------------|-----------------|
| Full automation | F ≥ 2, R ≥ 0.95 | None |
| Assisted | F ≥ 1, R ≥ 0.80 | Sample review |
| Suggestion only | Any F, R ≥ 0.60 | Human decision |
| Not suitable | R < 0.60 | Keep manual |

---

## Output Templates

### Holon Inventory

```markdown
## Holon Inventory

### Systems (Can Act)
| ID | Name | Type | Roles |
|----|------|------|-------|
| S1 | ... | Person/Team/AI/Service | ... |

### Epistemes (Cannot Act)
| ID | Name | Type | Status Role |
|----|------|------|-------------|
| E1 | ... | Document/Data/Record | Evidence/Standard/Requirement |
```

### Context Map

```markdown
## Bounded Contexts

### Context: [Name]:[Version]
**Glossary:**
- Term1 = local meaning
- Term2 = local meaning

**Invariants:**
- Rule1
- Rule2

### Bridges
| From | To | CL | Loss Notes |
|------|----|----|------------|
| CtxA | CtxB | CL2 | Minor term differences |
```

### Transformation Analysis

```markdown
## Transformation: [Process Name]

**Transformer Quartet:**
- Acting Side: [System]#[Role]:[Context]
- MethodDescription: [Doc] (F=[level])
- Method: [Capability]
- Work Pattern: [Description]

**Trust Assessment:**
- Formality: F[0-3] - [justification]
- Scope: [where it applies]
- Reliability: R=[0-1] - [evidence]

**Automation Recommendation:**
- Level: [Full/Assisted/Suggestion/Manual]
- Requirements: [what's needed]
- Tools: [suggested implementations]
```

---

## Example Application

**User Request:** "Model our invoice approval process using FPF"

**Response Structure:**

```markdown
## Invoice Approval Process - FPF Analysis

### Holons

**Systems:**
| ID | Name | Type | Roles |
|----|------|------|-------|
| S1 | SubmitterEmployee | Person | Submitter#Finance |
| S2 | ApprovalBot | AIAgent | Reviewer#Finance |
| S3 | Manager | Person | Approver#Finance |
| S4 | PaymentSystem | Service | Executor#Finance |

**Epistemes:**
| ID | Name | Type | Status |
|----|------|------|--------|
| E1 | Invoice | Document | Requirement |
| E2 | ApprovalPolicy | Document | Standard (F=2) |
| E3 | ApprovalRecord | Record | Evidence |

### Context: Finance:Invoicing_2026

**Glossary:**
- Invoice = vendor payment request
- Approval = authorization to pay
- Threshold = amount requiring manager approval ($5000)

**Invariants:**
- Invoice > $5000 requires Manager approval
- All approvals must be recorded

### Transformation: "Review Invoice"

**Quartet:**
- Acting Side: ApprovalBot#Reviewer:Finance
- MethodDescription: ApprovalPolicy (F=2, formal rules)
- Method: InvoiceValidation
- Work: Review_INV_2026_001234

**Trust:** ⟨F=2, G=all_invoices, R=0.92⟩

**Automation:** Full automation suitable for:
- Invoice validation (R=0.92)
- Auto-approve under threshold (F=2, clear rules)

Requires human:
- Over-threshold approval (policy requirement)
- Exception handling (R < 0.80 for edge cases)
```

---

## Integration with AI Tools

### MCP Server Integration
- Document classification → assign U.Role to U.Episteme
- Workflow routing → resolve U.RoleAssignment
- Response generation → execute MethodDescription as Work

### Skill/Task Design
- Each skill = packaged MethodDescription
- Task = single Work unit with provenance
- Agent = U.System bearing appropriate Role

### Trust Monitoring
- Track F-G-R for all AI outputs
- Apply CL penalties for cross-context use
- Maintain evidence graphs for auditability

---

*Skill version 1.0.0 | Based on FPF Core Specification v2025-09*
