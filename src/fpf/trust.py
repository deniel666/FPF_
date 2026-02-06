from typing import List, Optional, Any, Set
from pydantic import BaseModel, Field, field_validator

class TrustScore(BaseModel):
    """
    FPF Trust & Assurance Tuple <F, G, R>
    """
    F: int = Field(..., ge=0, le=3, description="Formality (0-3)")
    G: str = Field(..., description="Scope (Context/Domain)")
    R: float = Field(..., ge=0.0, le=1.0, description="Reliability (0.0-1.0)")
    CL: int = Field(default=3, ge=0, le=3, description="Congruence Level (0-3) if bridged")
    notes: Optional[str] = None

    @staticmethod
    def phi(cl: int) -> float:
        """Penalty function for Congruence Level."""
        penalties = {
            3: 0.0,  # Verified equivalence
            2: 0.1,  # Validated mapping
            1: 0.2,  # Plausible mapping
            0: 0.5   # Weak guess
        }
        return penalties.get(cl, 0.5)

    @classmethod
    def aggregate(cls, scores: List['TrustScore'], scope_merge: str = "Union") -> 'TrustScore':
        """
        Conservative aggregation:
        F_eff = min(F_i)
        R_eff = max(0, min(R_i) - phi(CL_min))
        """
        if not scores:
            return cls(F=0, G="Empty", R=0.0)

        f_eff = min(s.F for s in scores)
        r_min = min(s.R for s in scores)
        cl_min = min(s.CL for s in scores)

        r_eff = max(0.0, r_min - cls.phi(cl_min))

        # G aggregation is complex (set union), simplifying to joined string for now
        g_eff = f"Union({[s.G for s in scores]})" if scope_merge == "Union" else scope_merge

        return cls(F=f_eff, G=g_eff, R=r_eff, CL=cl_min)
