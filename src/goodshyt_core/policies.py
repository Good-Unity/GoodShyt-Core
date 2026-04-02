from __future__ import annotations

from pathlib import Path
import yaml
from pydantic import BaseModel


class PolicyBundle(BaseModel):
    ecti_minimum: float = 0.90
    csm_minimum: float = 0.75
    stl_max_penalty: float = 0.25
    kaq_minimum: float = 0.70


def load_policy_bundle(path: str | Path) -> PolicyBundle:
    data = yaml.safe_load(Path(path).read_text())
    return PolicyBundle.model_validate(data)
