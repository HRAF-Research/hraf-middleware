# hraf-middleware

This repository contains the production-ready middleware pipeline and data structures for the Hybrid Robot Action Framework (HRAF), built using the Single Responsibility Principle (SRP) and strict Python type hinting.

## Expected Data Structures & Usage

Below are the standardized, thread-safe data structures implemented in `src/hraf/states.py` for integration with ADCA and HARM in Week 8.

### 1. RobotState (Immutable Telemetry)
```python
from hraf.states import RobotState

# Instantiating a thread-safe snapshot of robot telemetry
state = RobotState(
    position=(1.0, 2.0, 3.0),
    orientation=(0.0, 0.0, 0.0, 1.0),
    joint_angles=[0.0, 45.0, 90.0],
    timestamp=1714560000.0
)

# Attempting to mutate a property will raise an AttributeError:
# state.position = (4.0, 5.0, 6.0)  # BLOCKED (Thread-Safe)


from hraf.states import VLMCommand

# Capturing instruction sets from the high-level AI model
command = VLMCommand(
    waypoints=[(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)],
    obstacles=["table_leg", "human_hand"],
    confidence=0.92,
    raw_response="Move past the table leg while avoiding the human hand."
)