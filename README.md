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

## All test passing (pytest green)
<img width="1632" height="207" alt="all test passed" src="https://github.com/user-attachments/assets/e6f7a73c-9b8b-4f03-85cf-78e0c7ca8b71" />

============================================================================================

## 🗓️ Week 2: Concurrency, Threads & The GIL

### Day 1: Thread Basics & OS Scheduling
* **What I Studied:** Studied how threads work and learned about the **Global Interpreter Lock (GIL)**.
* **What I Coded:** Wrote a Python script inside `threads_demo.ipynb` that runs 3 threads at the exact same time.
* **What I Observed:** Noticed that the outputs from the threads shuffle and mix together in a random order every time the code runs. This happens because the Operating System's Thread Scheduler controls the exact timing, not our code.

**Deliverables:**
* PDF File: [threads_demo.pdf](https://github.com/user-attachments/files/28462305/threads_demo.pdf)

### Day 2: Race Conditions
* **Created a Race Condition:** Set up two threads to increase a shared counter 10,000 times at the same time.
* **Observed Data Errors:** Ran the script 10 times and watched the final total change every time, never reaching the expected 20,000 because threads overwrote each other.
* **Fixed with a Lock:** Added `threading.Lock()` to force the threads to wait in line, making sure the final count hits exactly 20,000 every single run.
* **Added Code Comments:** Wrote clear notes explaining how the computer's read-modify-write steps caused the race condition and why the lock fixed it.

**Deliverable:** 
* PDF File: [race_condition.pdf](https://github.com/user-attachments/files/28502197/race_condition.pdf)


### Day 3: Thread Event & Signaling
* **Studied Event Basics:** Learned how `threading.Event` works using `set()`, `clear()`, `wait()`, and `is_set()` to pause threads without wasting CPU power.

**Deliverables:**
* [Stop Event Pattern Notebook](./stop_event_pattern.ipynb)
* [Ready Event Synchronization Notebook](./ready_event.ipynb)
* [Sensor Middleware Simulation Notebook](./simulation.ipynb)


### Day 4: Thread-Safe Queues & Latency Management
* **Studied Queue Basics:** Learned how `queue.Queue` works using `put()`, `get()`, `get_nowait()`, `task_done()`, `join()`, and `maxsize` to share data safely between threads.
* **Built a Balanced Pipeline:** Created a system where a producer sends sensor data and a consumer processes it at the exact same speed.
* **Tested Latency Accumulation:** Proved that if a producer sends data faster than a consumer can read it, the queue fills up with old, lagging data.
* **Implemented Bounded Flush Semantics:** Programmed a limited queue that clears out and drops old data packets so the consumer always uses the newest information.
  
**Deliverables:**
* [Balanced Pipeline Notebook](./balanced_pipeline.ipynb)
* [Latency Accumulation Notebook](./latency_accumulation.ipynb)
* [Bounded Queue Flush Notebook](./bounded_queue_flush.ipynb)
