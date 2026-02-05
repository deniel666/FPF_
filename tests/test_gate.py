import pytest
from src.models.lead import Lead
from src.logic.gate import process_vapi_outcome

def test_gate_interested_hot():
    lead = Lead(id="L1", stage="sourced")
    outcome = {
        "outcome": "interested",
        "qualification": {
            "R_interest": 0.9,
            "R_authority": 0.8,
            "R_budget": 0.7,
            "R_timeline": 0.8
        }
    }
    # Min R = 0.7 >= 0.6

    new_stage, action = process_vapi_outcome(lead, outcome)

    assert new_stage == "interested"
    assert action == "SEND_BOOKING_LINK"
    assert lead.stage == "interested"

def test_gate_interested_warm_but_low_authority():
    lead = Lead(id="L2", stage="sourced")
    outcome = {
        "outcome": "interested",
        "qualification": {
            "R_interest": 0.9,
            "R_authority": 0.4, # Low
            "R_budget": 0.7,
            "R_timeline": 0.8
        }
    }
    # Min R = 0.4 < 0.6

    new_stage, action = process_vapi_outcome(lead, outcome)

    assert new_stage == "contacted"
    assert "NURTURE_SEQUENCE" in action
    assert "R_authority" in action
    assert lead.stage == "contacted"

def test_gate_not_interested():
    lead = Lead(id="L3", stage="sourced")
    outcome = {"outcome": "not_interested"}

    new_stage, action = process_vapi_outcome(lead, outcome)

    assert new_stage == "dead"
    assert action == "DO_NOT_CONTACT"
