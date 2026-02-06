import pytest
from src.fpf.trust import TrustScore

def test_trust_score_aggregation():
    s1 = TrustScore(F=2, G="ContextA", R=0.8, CL=3)
    s2 = TrustScore(F=3, G="ContextB", R=0.9, CL=2)

    agg = TrustScore.aggregate([s1, s2])

    # F_eff = min(2, 3) = 2
    assert agg.F == 2

    # R_eff = min(0.8, 0.9) - phi(CL_min=2)
    # phi(2) = 0.1
    # R_eff = 0.8 - 0.1 = 0.7
    assert agg.R == pytest.approx(0.7)

    assert agg.CL == 2

def test_phi_function():
    assert TrustScore.phi(3) == 0.0
    assert TrustScore.phi(2) == 0.1
    assert TrustScore.phi(0) == 0.5
