from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from .trust import TrustScore

class Holon(BaseModel):
    id: str
    description: Optional[str] = None

class System(Holon):
    """
    U.System: An entity that CAN ACT.
    """
    can_act: bool = Field(default=True, frozen=True)
    roles: List[str] = []

class Episteme(Holon):
    """
    U.Episteme: An entity that CANNOT ACT, only be acted upon.
    """
    can_act: bool = Field(default=False, frozen=True)
    status_role: Optional[str] = None
    trust_score: Optional[TrustScore] = None

class MethodDescription(Episteme):
    """
    Recipe/SOP/Algorithm.
    """
    recipe: str

class Work(BaseModel):
    """
    Execution record.
    """
    work_id: str
    acting_system_id: str
    method_description_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    output: Optional[Dict] = None
