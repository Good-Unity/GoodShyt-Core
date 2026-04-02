from goodshyt_core.metrics import compute_gmi, score_csm, score_ecti, score_kaq, score_stl


def test_gmi_is_bounded() -> None:
    value = compute_gmi(0.98, 0.88, 0.10, 0.84)
    assert 0.0 <= value <= 1.0


def test_component_scores_are_bounded() -> None:
    assert 0.0 <= score_ecti(0.95, 0.05) <= 1.0
    assert 0.0 <= score_stl(50, 80) <= 1.0
    assert 0.0 <= score_csm(8, 2) <= 1.0
    assert 0.0 <= score_kaq(7, 3) <= 1.0
