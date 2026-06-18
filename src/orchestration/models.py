from pydantic import BaseModel
from typing import List

class InvestigationResult(BaseModel):
    documents: List[str]
    risks: List[str]
    recommendations: List[str]
    report: str