from typing import List, Optional, Any

from pydantic import BaseModel
from pydantic import BaseModel, ValidationError, field_validator
from services.models.ModelTriageCategory import TriageCategory


class InteractionOption(BaseModel):
    sequence: int
    option_name: str
    option_description: str


class Interaction(BaseModel):
    variable_name: str
    variable_type: str
    question: str
    options: Optional[List[InteractionOption]]
    answer: Optional[str]
    complete: bool = False


class InteractionRequest(BaseModel):
    request_id: str
    params: dict = {}
    interactions: Optional[List[Interaction]] = None
    complete: Optional[bool] = False


class BookingInteractionRequest(InteractionRequest):
    booking_id: Optional[str] = None


class TriageInteractionRequest(InteractionRequest):
    patient_id: Optional[str] = None
    triage_category: Optional[TriageCategory] = None
    score: Optional[float] = None


class EvacStrandedPersonnelInteractionRequest(InteractionRequest):
    booking_id: Optional[str] = None
