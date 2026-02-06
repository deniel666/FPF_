from typing import Optional
from datetime import datetime
from pydantic import Field
from src.fpf.ontology import Work

class Shot(Work):
    """
    A single outbound action (Work unit).
    """
    channel_id: str
    target_lead_id: str
    fired_at: datetime = Field(default_factory=datetime.now)

    # Outcome flags
    delivered: bool = False
    opened: bool = False
    replied: bool = False
    ai_conversation: bool = False
    interested: bool = False
    booked: bool = False
    closed: bool = False
