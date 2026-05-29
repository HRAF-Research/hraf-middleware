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
```

### 2. VLMCommand (Vision-Language Model Output)
```python
from hraf.states import VLMCommand

# Capturing instruction sets from the high-level AI model
command = VLMCommand(
    waypoints=[(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)],
    obstacles=["table_leg", "human_hand"],
    confidence=0.92,
    raw_response="Move past the table leg while avoiding the human hand."
)
```

## Expected Pipeline Output Preview

Below is a snippet of the generated data processing output from yesterday's task.

### 3. Generated User Report Output (Text Snapshot)
```text
--- USER REPORT ---
ID: USR001 | Name: Guneet Kaur | Age: 25
ID: USR002 | Name: John Doe | Age: 42
-------------------
Total Users: 2
Average Age: 33.5
```

---

## Day 3 Validation: Middleware Exception Pipeline
Below is the execution stream of the custom exception handling architecture tracking an out-of-bounds physical coordinate constraint breach:

![HRAF Safety Pipeline Output](src/hraf/day-3_output_snippet.png)


## Day 4 Validation: Core Telemetry & Command Unit Test Suite
Below is the execution stream of the automated pytest verification matrix tracking data structure validation, type enforcement, immutability barriers, and boundary limits:

<img width="1918" height="277" alt="DAY-4_Output_snippet" src="https://github.com/user-attachments/assets/f0e4708d-5646-4c62-a74d-463f22406ada" />

## Day 5 Validation: Pydantic v2 Schema Gatekeeper
Below is the automated pytest output verifying our Stage 3 validation rules. This test execution stream demonstrates our defensive middleware pipeline successfully intercepting adversarial inputs (including type corruptions, out-of-range confidence thresholds, empty waypoint lists, and missing parameters) at the schema gate level:

<img width="775" height="220" alt="Day 5_output_snippet" src="https://github.com/user-attachments/assets/0ffc901f-a20b-4147-8a20-74cad166825b" />
