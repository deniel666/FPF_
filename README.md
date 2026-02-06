# Erzy Sales Machine (DFM) - Core Implementation

This repository contains the core logic and data models for the Erzy Sales Machine (DFM), built on the First Principles Framework (FPF).

## Structure

- `src/fpf/`: Core FPF ontology (System, Episteme, Trust Calculus).
- `src/models/`: Data models for Attio (Lead) and Work (Shot).
- `src/methods/`: MethodDescriptions, including the Vapi Agent Prompt.
- `src/logic/`: Core business logic (Gate Logic, Scoring).
- `tests/`: Unit tests for verification.

## Core Components

### 1. Vapi Agent (Phase 1)
The Vapi Agent prompt is defined in `src/methods/vapi.py`. It implements the qualification script:
- Identity Confirmation
- Need Establishment
- Product Demo (The Reveal)
- Qualification (Need, Pain, Budget, Timeline)
- Booking

### 2. Trust Calculus
Implemented in `src/fpf/trust.py`. It calculates Trust Scores `<F, G, R>` and handles aggregation with Congruence Level (CL) penalties.

### 3. Gate Logic
Implemented in `src/logic/gate.py`. It determines the next action based on Vapi outcome and Lead Warmth ($R_{eff}$).

## Usage

To use this logic in your orchestration layer (e.g., Make.com via Cloud Functions or a generic webhook handler):

```python
from src.models.lead import Lead
from src.logic.gate import process_vapi_outcome

# 1. Load Lead from Attio Payload
lead = Lead(id="lead_123", stage="sourced", ...)

# 2. Receive Vapi Webhook Payload
vapi_payload = {
    "outcome": "interested",
    "qualification": {
        "R_interest": 0.9,
        "R_authority": 0.8,
        "R_budget": 0.7,
        "R_timeline": 0.8
    }
}

# 3. Process Outcome
new_stage, action = process_vapi_outcome(lead, vapi_payload)

# 4. Execute Action (e.g. update Attio, send booking link)
print(f"Update Stage to: {new_stage}")
print(f"Execute Action: {action}")
```

## Testing

Run tests with:
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 -m pytest
```
