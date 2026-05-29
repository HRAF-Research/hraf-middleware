import pytest
from pydantic import ValidationError
from src.hraf.models import RobotState, VLMCommand
from src.hraf.exceptions import (
    HRAFBaseError,
    HardwareFaultError,
    WorkspaceViolationError,
    NetworkTimeoutError,
    InvalidCommandError
)

# =========================================================================
# MODULE 1: CUSTOM DOMAIN EXCEPTIONS (5 TESTS)
# =========================================================================

def test_base_hraf_exception():
    with pytest.raises(HRAFBaseError):
        raise HRAFBaseError("Base error")

def test_hardware_fault_error():
    with pytest.raises(HardwareFaultError):
        raise HardwareFaultError("Joint 3 stuck")

def test_workspace_violation_error():
    with pytest.raises(WorkspaceViolationError):
        raise WorkspaceViolationError("Out of bounds")

def test_network_timeout_error():
    with pytest.raises(NetworkTimeoutError):
        raise NetworkTimeoutError("VLM dropped link")

def test_invalid_command_error():
    with pytest.raises(InvalidCommandError):
        raise InvalidCommandError("Malformed JSON")

# =========================================================================
# MODULE 2: ROBOTSTATE DATACLASS VALIDATION (5 TESTS)
# =========================================================================

def test_robot_state_valid_construction():
    state = RobotState(
        position=(1.0, 2.0, 3.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[0.0, 45.0, 90.0],
        timestamp=1714560000.0
    )
    assert state.position == (1.0, 2.0, 3.0)

def test_robot_state_immutability():
    state = RobotState(
        position=(1.0, 2.0, 3.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[0.0, 45.0, 90.0],
        timestamp=1714560000.0
    )
    with pytest.raises(Exception):
        state.position = (4.0, 5.0, 6.0)

def test_robot_state_joint_angles():
    state = RobotState(
        position=(0.0, 0.0, 0.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[15.5, -30.0],
        timestamp=1714560000.0
    )
    assert len(state.joint_angles) == 2

def test_robot_state_timestamp():
    state = RobotState(
        position=(0.0, 0.0, 0.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[],
        timestamp=111.1
    )
    assert state.timestamp == 111.1

def test_robot_state_orientation_tuple():
    state = RobotState(
        position=(0.0, 0.0, 0.0),
        orientation=(1.0, 0.0, 0.0, 0.0),
        joint_angles=[],
        timestamp=1.0
    )
    assert state.orientation[0] == 1.0

# =========================================================================
# MODULE 3: VLMCOMMAND PYDANTIC V2 RESILIENCE (5 TESTS)
# =========================================================================

@pytest.fixture
def base_vlm_data():
    return {
        "waypoints": [[0.5, 0.2, 1.1]],
        "obstacles": [],
        "confidence": 0.85,
        "action": "move",
        "raw_response": "raw_string_log"
    }

def test_pydantic_valid_input(base_vlm_data):
    cmd = VLMCommand(**base_vlm_data)
    assert cmd.action == "move"
    assert cmd.confidence == 0.85

def test_pydantic_out_of_range_confidence(base_vlm_data):
    base_vlm_data["confidence"] = 1.5
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)

def test_pydantic_missing_required_field(base_vlm_data):
    del base_vlm_data["action"]
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)

def test_pydantic_wrong_type(base_vlm_data):
    base_vlm_data["confidence"] = "completely_confident"
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)

def test_pydantic_empty_waypoints(base_vlm_data):
    base_vlm_data["waypoints"] = []
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)
