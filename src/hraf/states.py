from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True)
class RobotState:
    position: Tuple[float, float, float]
    orientation: Tuple[float, float, float, float]
    joint_angles: List[float]
    timestamp: float

@dataclass(frozen=True)
class VLMCommand:
    waypoints: List[Tuple[float, float, float]]
    obstacles: List[str]
    confidence: float
    raw_response: str