# First Principles Framework (FPF) — Core Conceptual Specification

> **An Operating System for Thought**  
> *Architecting transdisciplinary reasoning for systems, epistemes, and communities.*

**Version:** September 2025  
**Primary Author:** Anatoly Levenchuk (with LLM assistance)  
**Status:** Stable / Normative Core / Constantly Evolving (eternal alpha)

---

## 📖 Overview

The **First Principles Framework (FPF)** is a rigorous, transdisciplinary architecture for thinking. It provides a generative pattern language to model complex systems, manage knowledge evolution, and ensure auditable assurance across engineering, research, and management domains.

FPF is not a specific methodology (like Agile or Waterfall) nor a static encyclopedia. It is a **generative scaffold**—a set of architectural decisions that enables you to construct, evolve, and verify concepts with precision. It bridges the gap between **rigorous assurance** (audits, proofs) and **open-ended creativity** (innovation, novelty) by treating them as complementary engines within a single evolution.

## 🎯 Who is this for?

*   **Engineers** building reliable physical or cyber-physical systems (`U.System`).
*   **Researchers** constructing trustworthy knowledge and theories (`U.Episteme`).
*   **Managers** orchestrating collective intelligence, budgets, and evolutionary cycles.

## 🔑 Key Concepts & Commitments

FPF is built on a micro-kernel of non-negotiable principles. If you are new, start with these core ideas:

1.  **Holonic Foundation (`A.1`):** Everything is a `U.Holon`—simultaneously a whole and a part. We strictly distinguish between physical actors (**Systems**) and knowledge artifacts (**Epistemes**).
2.  **Contextual Meaning (`A.1.1`, `F.0.1`):** Meaning is local. A term like "Service" or "Process" is defined strictly within a `U.BoundedContext`. Cross-context communication happens only via explicit **Bridges** with declared translation loss.
3.  **Strict Distinction (`A.7`):** We never confuse the map with the territory.
    *   **Role** (Assignment/Mask) $\neq$ **Method** (Recipe) $\neq$ **Work** (Execution/Occurrence).
    *   Documents do not "act"; only Systems enact Work.
4.  **Trust & Assurance Calculus (`B.3`):** Trust is not a feeling; it is a computed tuple **$\langle F, G, R \rangle$**:
    *   **F (Formality):** How rigorously is it expressed?
    *   **G (Claim Scope):** Where does it apply? (Set-valued over context slices).
    *   **R (Reliability):** How well is it supported by evidence?
5.  **Evolution & Creativity (`B.4`, `C.18`):** Systems must evolve. FPF operationalizes the "Bitter Lesson" by favoring general, scalable search methods (**NQD**: Novelty-Quality-Diversity) over hand-tuned heuristics, governed by explicit **Explore-Exploit policies**.
6.  **Universal Aggregation ($\Gamma$):** A single algebra (`B.1`) governs how parts combine into wholes, ensuring invariants like "Weakest-Link" reliability are preserved across scales.

## 📂 Repository Structure

The specification is divided into clusters of patterns:

### **Part A: Kernel Architecture Cluster**
The immutable ontological core.
*   **Ontology:** Holons, Systems, Epistemes, and Bounded Contexts.
*   **Transformation:** The `Transformer` quartet (Agent, Method, Description, Work).
*   **State Space:** Characteristics, Scales, and Dynamics.

### **Part B: Trans-disciplinary Reasoning Cluster**
The logic of composition and trust.
*   **$\Gamma$ Algebra:** How to aggregate systems (`Γ_sys`), knowledge (`Γ_epist`), and resources (`Γ_work`).
*   **Assurance:** The `F-G-R` calculus and evidence graphs.
*   **Evolution:** The canonical loops for observing, refining, and deploying updates.

### **Part C: Architheory Specifications**
Pluggable domain-specific calculi (CAL), logics (LOG), and characterizations (CHR).
*   **Sys-CAL:** Physics and conservation laws.
*   **KD-CAL:** Knowledge dynamics and truth-maintenance.
*   **NQD-CAL:** Novelty, Quality, and Diversity search.
*   **Kind-CAL:** Typed reasoning and taxonomy.

### **Part D: Ethics & Conflict-Optimisation**
*   Multi-scale ethics (from agent to planetary).
*   Bias audits and trust-aware mediation.

### **Part E: Constitution & Authoring**
The governance of the framework itself.
*   **The 11 Pillars:** Constitutional invariants (e.g., *Cognitive Elegance*, *Didactic Primacy*).
*   **Guard-Rails:** DevOps Lexical Firewall, Notational Independence.
*   **MVPK:** Multi-View Publication Kit for generating consistent views/documents.

### **Part F: The Unification Suite**
Techniques for aligning vocabularies across disciplines using **SenseCells**, **Concept-Sets**, and **Alignment Bridges**.

### **Part G: Discipline SoTA Kit**
Tools for harvesting "State of the Art" (SoTA) knowledge, benchmarking methods, and creating selector-ready portfolios of solutions.

> *"A principle that works in only one world is local folklore; a first principle architects every world."* — **Pattern A.8**

## 🚀 Using FPF with LLMs (Worked Prompt Examples)

FPF is designed to be loaded as a file into an LLM (ChatGPT, Gemini, local models with RAG, etc.) and then *asked to think with you* about concrete projects.  
Below are example prompts that have been used in practice; adapt them to your domain and language.

### 1. Characterisation & indicators for a new project

**Goal:** get a step-by-step chain from “vague idea” to measurable characteristics, indicators, scoring and decision criteria.
**Prompt:** 
> You have the FPF specification loaded as a file.  
> We are starting work on <brief description of project>, design has not yet begun.  
> Propose a step-by-step chain for characterising the objects of our project, normalising measurements, defining indicators, scoring alternatives, and choosing design decisions.  
> Include steps that I may have forgotten.  
> Write in the language of engineer-managers, not in FPF jargon.*

Typical follow-ups:
* “Now take object <X> from this chain and work it through in detail: list 10–15 characteristics, their scales, indicators, and a rough dashboard format for decision-makers.”
* “Show how this chain maps to P2W in E.TGA for this project.”

### 2. UTS (Unified Term Sheet) for a domain

**Goal:** build a disciplined vocabulary for a niche field using FPF Part F.
**Prompt:**
> You have the FPF specification loaded.  
> Produce a Unified Term Sheet (UTS) block for the core terms of <your domain>: at least 10 rows.  
> Use F.17 and F.18: distinguish Tech vs Plain names, show SenseCells for 2–3 key bounded contexts, and flag risky aliases.

Follow-up for quantitative structure:
* “For the same domain, propose a Q-bundle that captures the quality of <your object/process> and produce a UTS block for its characteristics (CHR) and indicators.”

### 3. Naming via F.18 (Name Cards)

**Goal:** design better names for roles, programs, artefacts when existing labels are misleading.
**Prompt:**
> Using F.18, develop a complete Name Card for what to call <current name of an Entity> in the following situation:  
> <short narrative of current practice and complaints about existing name>  
> Do not assume current names are correct; perform an honest search on the local Pareto-front of candidate names and explain trade-offs.

### 4. P2W (from principles to work) paths with E.TGA

**Goal:** make “from principles to work” explicit for a concrete project.
**Prompt:**
> Using E.TGA and TEVB, unpack the canonical P2W flow for my situation <describe your project>.  
> Give the list of nodes (P1…Pn), their Kinds, and explain each node in engineer-manager language.

Follow-up:
* “Now build a mini Flow specification table for this P2W graph”.

### 5. SoTA harvesting & discipline packs

**Goal:** use Part G to organise a frontier discipline around first principles.
**Prompt:**
> We are in search for SoTA of <discipline>.
> Using G.2 and G.4, extract: (a) TraditionCards for competing schools of thought; (b) OperatorCards for their main operators / update rules; (c) a first draft of a SoTA Pack and selector-ready portfolio. This is expected to be a long text, therefore start with only TraditionCards.
