from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from .metrics import compute_gmi
from .protocols import HandshakeRequest, verify_handshake

app = FastAPI(title="GoodShyt Core")


class ScorePayload(BaseModel):
    ecti: float
    csm: float
    stl_penalty: float
    kaq: float


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "goodshyt-core"}


@app.post("/score")
def score(payload: ScorePayload) -> dict[str, float]:
    return {"gmi": compute_gmi(payload.ecti, payload.csm, payload.stl_penalty, payload.kaq)}


@app.post("/handshake")
def handshake(payload: HandshakeRequest) -> dict[str, str | bool]:
    result = verify_handshake(payload)
    return result.model_dump()
