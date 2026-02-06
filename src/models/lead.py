from typing import List, Optional
from pydantic import Field
from src.fpf.ontology import Episteme
from src.fpf.trust import TrustScore

class Lead(Episteme):
    """
    Lead record in Attio.
    """
    email: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    company: Optional[str] = None

    channel_source: Optional[str] = None
    icp_tags: List[str] = []
    message_variant: Optional[str] = None

    fpf_score: Optional[TrustScore] = None

    shot_count: int = 0
    stage: str = Field(default="sourced", description="sourced | contacted | ai_spoken | interested | booked | dead")

    def update_stage(self, new_stage: str):
        valid_stages = ["sourced", "contacted", "ai_spoken", "interested", "booked", "dead"]
        if new_stage in valid_stages:
            self.stage = new_stage
