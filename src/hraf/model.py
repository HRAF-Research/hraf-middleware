%%writefile tests/test_models.py
import pytest
from pydantic import ValidationError
from src.hraf.models import RobotState, VLMCommand

# ==========================================
# 1. BASELINE REUSABLE DATA FIXTURES
# ==========================================
@pytest.fixture
def base_vlm_data():
    """Generates a pristine, valid set of baseline fields for VLMCommand testing."""
    return {
        "waypoints": [[0.5, 0.2, 1.1]],
        "obstacles": [],
        "confidence": 0.85,
        "action": "move",
        "raw_response": "raw_string_log"
    }

# ==========================================
# 2. FRIDAY TASKSHEET VALIDATION TESTS
# ==========================================

def test_pydantic_valid_input(base_vlm_data):
    """Verifies that flawless, compliant data builds successfully without errors."""
    cmd = VLMCommand(**base_vlm_data)
    assert cmd.action == "move"
    assert cmd.confidence == 0.85

def test_pydantic_out_of_range_confidence(base_vlm_data):
    """Verifies that confidence values outside 0.0-1.0 throw a ValidationError."""
    base_vlm_data["confidence"] = 1.5  # Invalid: Greater than 1.0 threshold 
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)

def test_pydantic_missing_required_field(base_vlm_data):
    """Verifies that removing a crucial structural field triggers validation blocks."""
    del base_vlm_data["action"]  # Invalid: 'action' is mandatory 
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)

def test_pydantic_wrong_type(base_vlm_data):
    """Verifies that injecting text strings into numeric containers is caught immediately."""
    base_vlm_data["confidence"] = "completely_confident"  # Invalid: expects a float 
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)

def test_pydantic_empty_waypoints(base_vlm_data):
    """Verifies that an empty trajectory list fails the min_length=1 rule."""
    base_vlm_data["waypoints"] = []  # Invalid: violating minimum length constraints 
    with pytest.raises(ValidationError):
        VLMCommand(**base_vlm_data)