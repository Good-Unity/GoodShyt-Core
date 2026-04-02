from goodshyt_core.protocols import HandshakeRequest, verify_handshake


def test_handshake_requires_metrics() -> None:
    result = verify_handshake(
        HandshakeRequest(service_name="svc", service_version="0.1.0", supported_metrics=[])
    )
    assert result.accepted is False


def test_handshake_accepts_audited_service() -> None:
    result = verify_handshake(
        HandshakeRequest(
            service_name="svc",
            service_version="0.1.0",
            supported_metrics=["ECTI", "CSM"],
            audit_mode=True,
        )
    )
    assert result.accepted is True
