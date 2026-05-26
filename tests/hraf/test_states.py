import pytest
from hraf.states import RobotState, VLMCommand

def test_robot_state_immutability():
    """Verify that RobotState properties cannot be altered after creation."""
    state = RobotState(
        position=(1.0, 2.0, 3.0),
        orientation=(0.0, 0.0, 0.0, 1.0),
        joint_angles=[0.0, 45.0, 90.0],
        timestamp=1714560000.0
    )
    
    # Proves that trying to modify a frozen dataclass raises a FrozenInstanceError
    with pytest.raises(AttributeError):
        state.position = (4.0, 5.0, 6.0) # type: ignore

def test_vlm_command_structure():
    """Verify that VLMCommand instantiates correctly with strict types."""
    command = VLMCommand(
        waypoints=[(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)],
        obstacles=["table_leg", "human_hand"],
        confidence=0.92,
        raw_response="Move past the table leg while avoiding the human hand."
    )
    
    assert command.confidence == 0.92
    assert len(command.waypoints) == 2