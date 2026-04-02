from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field

MetricName = Literal["ECTI", "STL", "CSM", "KAQ", "GMI"]


class MetricScore(BaseModel):
    name: MetricName
    value: float = Field(ge=0.0, le=1.0)
    explanation: str


class ScoreReport(BaseModel):
    subject: str
    scores: list[MetricScore]
    summary: str
