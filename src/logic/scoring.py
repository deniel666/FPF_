from typing import Dict, Any

def calculate_lead_warmth(qualification_scores: Dict[str, float]) -> float:
    """
    Calculates R_eff for a lead based on Vapi qualification.
    R_eff = min(R_interest, R_authority, R_budget, R_timeline)

    If any key is missing, assumes 0.0 (conservative).
    """
    required_keys = ["R_interest", "R_authority", "R_budget", "R_timeline"]

    scores = [qualification_scores.get(k, 0.0) for k in required_keys]
    return min(scores)
