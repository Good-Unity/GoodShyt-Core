from __future__ import annotations


def clamp(value: float) -> float:
    return max(0.0, min(1.0, round(value, 4)))


def score_ecti(intent_alignment: float, contradiction_penalty: float = 0.0) -> float:
    return clamp(intent_alignment - contradiction_penalty)


def score_stl(detection_latency_ms: int, remediation_latency_ms: int) -> float:
    latency = detection_latency_ms + remediation_latency_ms
    score = 1.0 - min(latency / 1000.0, 1.0)
    return clamp(score)


def score_csm(successful_handoffs: int, failed_handoffs: int) -> float:
    total = successful_handoffs + failed_handoffs
    if total == 0:
        return 0.0
    return clamp(successful_handoffs / total)


def score_kaq(memory_hits: int, context_misses: int) -> float:
    total = memory_hits + context_misses
    if total == 0:
        return 0.0
    return clamp(memory_hits / total)


def compute_gmi(ecti: float, csm: float, stl_penalty: float, kaq: float) -> float:
    return clamp((ecti * 0.30) + (csm * 0.30) + ((1.0 - stl_penalty) * 0.20) + (kaq * 0.20))
