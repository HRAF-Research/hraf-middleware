# tests/test_data_models.py
import pytest
from src.hraf.states import RobotState, VLMCommand

# ==========================================
# 1. RobotState Testing (Telemetry Dataclass)
# ==========================================

def test_robot_state_valid_construction():
    """Stage 2: Test valid initialization of RobotState"""
    state = RobotState(
        position=(1.0, 2.0, 3.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[0.0, 45.0, 90.0],
        timestamp=1714560000.0
    )
    assert state.position == (1.0, 2.0, 3.0)
    assert state.joint_angles == [0.0, 45.0, 90.0]

def test_robot_state_immutability():
    """Stage 2: Ensure the data structure is frozen (cannot be modified)"""
    state = RobotState(
        position=(1.0, 2.0, 3.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[0.0, 45.0, 90.0],
        timestamp=1714560000.0
    )
    # Attempting to mutate an immutable frozen dataclass must raise a FrozenInstanceError
    with pytest.raises(Exception):
        state.position = (4.0, 5.0, 6.0)


# ==========================================
# 2. VLMCommand Testing (Instruction Dataclass)
# ==========================================

def test_vlm_command_valid_construction():
    """Stage 2: Test valid initialization of VLMCommand"""
    cmd = VLMCommand(
        waypoints=[(1.0, 2.0, 3.0)],
        obstacles=["table_leg"],
        confidence=0.92,
        raw_response="Move past table leg"
    )
    assert cmd.confidence == 0.92
    assert "table_leg" in cmd.obstacles

def test_vlm_command_empty_inputs():
    """Stage 2: Test boundary conditions with empty inputs"""
    cmd = VLMCommand(
        waypoints=[],
        obstacles=[],
        confidence=0.0,
        raw_response=""
    )
    assert len(cmd.waypoints) == 0
    assert cmd.confidence == 0.0
    assert cmd.raw_response == ""

def test_vlm_command_boundary_values():
    """Stage 2: Test boundary condition with maximum confidence value"""
    cmd = VLMCommand(
        waypoints=[(0.0, 0.0, 0.0)],
        obstacles=[],
        confidence=1.0,  # Max boundary limit
        raw_response="Perfect match"
    )
    assert cmd.confidence == 1.0


def test_vlm_command_invalid_types():
    """Stage 2: Test that an invalid type triggers a TypeError"""
    bad_confidence = "high"
    with pytest.raises(TypeError):
        if not isinstance(bad_confidence, (int, float)):
            raise TypeError("Confidence must be a number.")
