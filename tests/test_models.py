import pytest
from pydantic import ValidationError
from src.hraf.models import RobotState, VLMCommand

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
