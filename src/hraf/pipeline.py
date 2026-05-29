# src/hraf/pipeline.py

import json
from src.hraf.exceptions import (
    VLMResponseError,
    JSONParseError,
    WorkspaceViolationError,
    KinematicFeasibilityError,
)

def fetch_vlm_instruction(status_code: int):
    """
    Simulates pulling raw instruction text from a Vision-Language Model server.
    """
    if status_code != 200:
        raise VLMResponseError(f"VLM server returned critical error code: {status_code}")
    return "VLM connection successful! Instruction received: 'Move past table leg.'"


def parse_vlm_json(raw_string: str):
    """
    Simulates converting a raw string response into a structured JSON dictionary.
    """
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError:
        raise JSONParseError("Failed to parse incoming text payload stream into a valid JSON object.")


def verify_safety_bounds(x: float, y: float):
    """
    Checks if the targeted coordinate falls outside physical room constraints.
    """
    max_radius = 100.0  # safety envelope radius limit in cm
    distance = (x**2 + y**2)**0.5
    
    if distance > max_radius:
        raise WorkspaceViolationError(
            f"Target position ({x}, {y}) yields distance {distance:.2f}cm, "
            f"breaching max safety boundary of {max_radius}cm!"
        )
    return "Workspace boundaries clear."


def calculate_inverse_kinematics(joint_angle: float):
    """
    Verifies if a specific joint configuration violates hardware limit parameters.
    """
    max_limit = 180.0  # mechanical limit constraints in degrees
    if abs(joint_angle) > max_limit:
        raise KinematicFeasibilityError(
            f"Requested position angle {joint_angle}° exceeds hardware physical "
            f"joint boundary limits of ±{max_limit}°!"
        )
    return "Kinematic profile feasible."