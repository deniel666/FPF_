from typing import Dict, Any, Tuple
from src.models.lead import Lead
from src.logic.scoring import calculate_lead_warmth

def process_vapi_outcome(lead: Lead, call_outcome: Dict[str, Any]) -> Tuple[str, str]:
    """
    Processes the outcome of a Vapi call and determines the next action.
    Returns: (New Stage, Action Description)
    """
    outcome_status = call_outcome.get("outcome") # interested, not_interested, etc.
    qualification_data = call_outcome.get("qualification", {})

    # Calculate R_eff
    r_eff = calculate_lead_warmth(qualification_data)

    if outcome_status == "interested":
        if r_eff >= 0.6:
            lead.update_stage("interested")
            return ("interested", "SEND_BOOKING_LINK")
        else:
            lead.update_stage("contacted") # Still just contacted, not warm enough
            # Find weak dimension if data exists, else generic
            if qualification_data:
                weakest = min(qualification_data, key=qualification_data.get)
                return ("contacted", f"NURTURE_SEQUENCE: Low {weakest}")
            else:
                 return ("contacted", "NURTURE_SEQUENCE: Missing Qualification Data")

    elif outcome_status == "callback_requested":
        lead.update_stage("contacted")
        return ("contacted", "SCHEDULE_CALLBACK")

    elif outcome_status == "not_interested":
        lead.update_stage("dead")
        return ("dead", "DO_NOT_CONTACT")

    elif outcome_status in ["no_answer", "voicemail"]:
        # Keep current stage
        return (lead.stage, "RETRY_LATER")

    return (lead.stage, "UNKNOWN_OUTCOME")
