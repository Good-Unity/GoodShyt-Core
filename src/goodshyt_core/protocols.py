from __future__ import annotations

from pydantic import BaseModel


class HandshakeRequest(BaseModel):
    service_name: str
    service_version: str
    supported_metrics: list[str]
    transparency_mode: bool = True
    audit_mode: bool = True


class HandshakeResponse(BaseModel):
    accepted: bool
    reason: str


def verify_handshake(request: HandshakeRequest) -> HandshakeResponse:
    if not request.supported_metrics:
        return HandshakeResponse(accepted=False, reason="no metrics declared")
    if not request.audit_mode:
        return HandshakeResponse(accepted=False, reason="audit mode required")
    return HandshakeResponse(accepted=True, reason="ok")
