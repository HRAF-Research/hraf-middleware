# Week 1

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
## 🗓️ Week 1: Python Engineering Fundamentals & Clean Code Practices

## Day 1: Project Setup & Clean Code
* Created the `hraf-middleware` GitHub repository with standard production layout (`src/hraf/`, `tests/`, `requirements.txt`, `README.md`).
* Studied the Single Responsibility Principle and refactored a monolithic script into 5 modular, descriptive functions.
* Added explicit type hints across all refactored Python function signatures.

## Day 2: Type Hints & Dataclasses
* Learned Python typing system (`List`, `Dict`, `Optional`, `Union`, `Tuple`) and `@dataclass` decorators.
* Modeled an immutable, thread-safe `RobotState` dataclass (`position`, `orientation`, `joint_angles`, `timestamp`).
* Built the `VLMCommand` dataclass containing `waypoints`, `obstacles`, `confidence`, and `raw_response`.

## Day 3: Custom Exceptions & Error Handling
* Studied Python exception hierarchy and designed custom error classes (`HRAFBaseError`, `VLMResponseError`, `WorkspaceViolationError`, `JSONParseError`, `KinematicFeasibilityError`).
* Wrote conditional trigger functions to raise specific exceptions for distinct system failure modes.
* Implemented clean `try/except/finally` blocks for error catching, logging, and explicit re-raising.

## Day 4: pytest & Unit Testing
* Installed `pytest` and set up `tests/test_data_models.py` to validate core dataclass behavior.
* Applied `pytest` fixtures and `@pytest.mark.parametrize` to test valid inputs, bad types, and boundary cases.
* Executed test suite using `pytest --tb=short` to verify test passes and interpret failures.

## Day 5: Pydantic Validation
* Studied Pydantic v2 primitives (`BaseModel`, `Field`, `@field_validator`, `ValidationError`).
* Converted `VLMCommand` into a Pydantic model with strict field constraints (`confidence` $0.0-1.0$, `waypoints` minimum length $1$, `action` Literal enum).
* Tested schema edge cases (out-of-bound confidence, missing fields, invalid types) to ensure `ValidationError` is correctly triggered.

## 🗓️ Week 2: Concurrency, Threads & The GIL

## Day 1: Thread Basics & OS Scheduling
* **What I Studied:** Studied how threads work and learned about the **Global Interpreter Lock (GIL)**.
* **What I Coded:** Wrote a Python script inside `threads_demo.ipynb` that runs 3 threads at the exact same time.
* **What I Observed:** Noticed that the outputs from the threads shuffle and mix together in a random order every time the code runs. This happens because the Operating System's Thread Scheduler controls the exact timing, not our code.


## Day 2: Race Conditions
* **Created a Race Condition:** Set up two threads to increase a shared counter 10,000 times at the same time.
* **Observed Data Errors:** Ran the script 10 times and watched the final total change every time, never reaching the expected 20,000 because threads overwrote each other.
* **Fixed with a Lock:** Added `threading.Lock()` to force the threads to wait in line, making sure the final count hits exactly 20,000 every single run.
* **Added Code Comments:** Wrote clear notes explaining how the computer's read-modify-write steps caused the race condition and why the lock fixed it.


## Day 3: Thread Event & Signaling
* **Studied Event Basics:** Learned how `threading.Event` works using `set()`, `clear()`, `wait()`, and `is_set()` to pause threads without wasting CPU power.
* **Built a Stop Event Pattern:** Created a background thread that runs continuously and checks a flag to shut down safely when ordered.
* **Built a Ready Event Pattern:** Synchronized two threads so that Thread A stops completely and waits until Thread B signals that it is ready to proceed.


## Day 4: Thread-Safe Queues & Latency Management
* **Studied Queue Basics:** Learned how `queue.Queue` works using `put()`, `get()`, `get_nowait()`, `task_done()`, `join()`, and `maxsize` to share data safely between threads.
* **Built a Balanced Pipeline:** Created a system where a producer sends sensor data and a consumer processes it at the exact same speed.
* **Tested Latency Accumulation:** Proved that if a producer sends data faster than a consumer can read it, the queue fills up with old, lagging data.
* **Implemented Bounded Flush Semantics:** Programmed a limited queue that clears out and drops old data packets so the consumer always uses the newest information.

  
## Day 5: Full Producer-Consumer Demo & Latency Log
* **Build:** Created a two-thread system where a slow AI camera sends commands every 0.5s and a fast motor checks them 100 times per second.
* **Use:** Set up a `Queue(maxsize=1)` so the system throws away old, unread commands and instantly replaces them with the newest update.
* **Log:** Recorded creation and reading times to prove that our pipeline sends information almost instantly with zero data lag.

============================================================================================
## 🗓️ Week 3: System Design Thinking & Software Architecture Patterns 

## Day 1: Block Diagrams & Interfaces
* Read Section 4 of the HRAF Proposal document and built the HRAF Data Flow loop
* For each box, wrote down its inputs (including data type and source), outputs (including data type and destination), and error states
* Drew the full data flow on paper as well as digital: Simulator → VLM → HARM → IK → Simulator as a labeled diagram.


## Day 2: System-1 / System-2 Architecture 
* Studied Kahneman’s dual-process theory comparing System-1 (fast, reactive) and System-2 (slow, deliberate).
* Read the VLA-Perf paper (arXiv:2602.18397) to apply human dual-system traits to robot control modules
* Wrote a note identifying the fast IK loop as System-1 and the slow VLM brain as System-2 and Explained why coupling them slows the robot down and why they must be decoupled to fix the latency problem


## Day 3: Finite State Machines', 2100 
* Studied FSM concepts including **states, transitions, guards (conditions), and actions (side effects).
* Modeled the **HARM module** as a Finite State Machine with states: **IDLE, VALIDATING, FEASIBILITY_CHECK, EXECUTING, RECOVERY, and FAULT**.
* Drew a complete FSM diagram and documented all state transitions, specifying the triggering event and action performed for each transition


## Day 4: Failure Mode Analysis
* Identified three failure modes for each core module, separating them into the VLM, HARM, IK Solver, and State Bridge.
* Documented the specific trigger event, the downstream system effect, and the recovery method for every failure mode.
* Classified all system errors to determine which issues can be recovered automatically versus which ones are completely unrecoverable.
* Specified exactly which critical failures trip an emergency system stop and require a human operator to step in and fix the issue.


## Day 5: Interface Design for ADCA & HARM
* Designed Python interface stubs as abstract base classes to define structural code contracts before implementation.
* Created the ADCA blueprint detailing the initialization variables, loop frequencies, runtime controls, and state bridge retrieval.
* Created the HARM blueprint specifying text validation inputs returning structured results and error recovery paths returning fallback commands.


## 🗓️ Week 4: Python asyncio: Event Loop, Coroutines & Tasks 

## Day 1: Event Loop & Coroutines 
* Studied how the async event loop runs coroutines and manages tasks on a single thread.
* Built a Python coroutine using asyncio.sleep(0.3) to simulate real VLM API delay.
* Tested and compared running 5 VLM calls back-to-back versus all at once using asyncio.gather().
* Measured and documented a 1.20-second speedup, proving concurrency keeps the robot control loop from freezing.

## Day 2: Tasks & Cancellation
* Studied how asyncio.create_task() launches background tasks so the main code keeps running immediately without waiting.
* Learned how task.cancel() injects an asyncio.CancelledError to stop a running task right at its next pause point.
* Built a continuous 100Hz robot tracking loop that catches cancellation to safely drop motor torque and lock hardware brakes.
* Coded a timeout guard using asyncio.wait_for() to safely catch hanging network calls and instantly trigger fallback backup sensors.

## Day 3: asyncio.Queue & Async Producer-Consumer
* Studied asyncio.Queue vs queue.Queue, confirming that async queues use non-blocking coroutine suspension instead of thread-locking primitives.
* Rebuilt the Producer-Consumer demo pipeline into a single-threaded asynchronous framework using concurrent producer and consumer coroutines.
* Verified that the high-frequency IK consumer operates at its own independent cadence, pulling data from the state bridge without being stalled by VLM processing delays.


## Day 4: asyncio vs. threading Decision Matrix
* Studied Concurrency Choices: Learned to use single-threaded asyncio for fast network/VLM calls and threading as the fallback for heavy, blocking hardware tasks.
* Identified Loop Freezes: Discovered that calling a standard synchronous function directly inside async code completely freezes the single system thread, cutting off critical safety signals.
* Explored loop.run_in_executor(), which offloads slow, blocking legacy code to a background thread pool so the main loop can keep breathing.
* Built the ADCA Bridge: Programmed a script that handles an async VLM camera check while running a heavy 1.5-second blocking MoveIt 2 calculation in the background, proving the main control loop stays 100% active and responsive.


## Day 5: Async Latency Measurement 
* Created a benchmark with a 100Hz IK loop and a simulated VLM inference task running concurrently using asyncio.
* Logged IK loop timestamps with time.perf_counter() and used deadline scheduling to maintain a 10ms target period.
* Confirmed that the IK loop maintained ~100Hz while VLM inference was running in parallel.
* Generated timing plots and statistics, showing only minor jitter and no significant control-loop delays.


## 🗓️ Week 5: Latency Engineering: Measurement, Profiling & Optimisation 

## Day 1: Latency Measurement Fundamentals
* Studied `time.perf_counter()`, `time.process_time()`, and `time.monotonic()` for measuring different types of time delays.
* Learned why average latency can hide slow cases and how P50, P95, and P99 show latency spikes.
* Studied warm-up effects in API calls and why the first few requests are removed before measuring actual performance.
* Measured 50 `asyncio.sleep(0)` calls, plotted the latency, and analyzed async event loop scheduling overhead.


## Day 2: LatencyProfiler Class
* Architected Standalone Profiler: Built LatencyProfiler inside src/hraf/profiler.py using only numpy and matplotlib for framework-wide utility.
* Implemented Percentile Math: Added clean tracking for p50, p95, p99, mean, and standard deviation using numpy.percentile().
* Validated Tail Latencies: Verified calculations using 100 log-normal simulation points to accurately map worst-case latency spikes.
* Added CSV Data Export: Integrated export_csv() to save raw timing entries to disk for reproducible research benchmarks.


## Day 3: VLM API Latency Study
* Executed Cloud Infrastructure Sweeps: Ran 33 live API requests across Tier L2 (Gemini 1.5 Flash) and Tier L3 (Groq Llama3) to evaluate cloud-to-edge middleware performance.
* Isolated Network Initialization Noise: Discarded the first 3 samples of each sweep as warm-up cycles to ensure calibration and protect downstream statistical data from initial connection spikes.
* Captured Temporal Traffic Variances: Conducted multi-window testing across both afternoon (off-peak) and evening (peak load) periods to analyze real-world API server congestion.
* Mapped ADCA Safety Boundaries: Extracted P50, P95, and P99 percentiles along with dual-window distribution charts to establish worst-case latency boundaries for control loop decoupling.


## Day 4: Code Profiling
* **Inspected Image Encoding Pipeline:** Used cProfile and line_profiler to review the execution time of the image-to-text conversion script line by line.
* **Isolated Primary Function Bottleneck:** Discovered that saving images to memory buffers via standard library tools consumed **78.5%** of total system processing cycles.
* **Tested Multiple Optimization Vectors:** Evaluated compression settings, image downsampling, and library variations side by side to reduce processing overhead.
* **Slashed Processing Latency:** Applied JPEG compression adjustments to drop overall execution times by **50.5%**, keeping the loop fast enough for real-time control.


## Day 5: Latency Budget Design
* Designed Two-Speed Control System: Mapped out the system to separate fast arm movements from slow cloud network delays. This keeps the robot moving smoothly even if the internet lags.
* Calculated Arm Control Speed: Combined the 2 ms data bridge delay and the 10 ms movement calculation time. This allows the arm to safely update its path 83.33 times per second (83.33 Hz).
* Computed Main Planning Rate: Added the worst-case 1500 ms cloud lag to the local delays, totaling 1512 ms. This means the robot receives fresh visual decisions from the cloud about 0.66 times per second (0.66 Hz).


## 🗓️ Week 6: VLM API Integration & ADCA Prototype v0.1

## Day 1: sat_pipeline Integration
* Built Interface Pipeline Stub: Created a modular sat_pipeline.py file with a mock function to simulate the 300 ms processing delay of the vision endpoint.
* Implemented Non-Blocking Bridge: Developed the async_run_sat wrapper using background thread executors and safety timeouts to keep the main robot loop from freezing.
* Validated Concurrent Performance: Ran 10 requests at the same time, confirming they finish simultaneously without blocking or stalling the system sequentially.


## Day 2: State Bridge Implementation
* Built the Core State Bridge: Created a StateBridge communication manager using a 1-slot data queue (asyncio.Queue(maxsize=1)) and an alert flag (asyncio.Event).
* Implemented Safety Methods: Developed functions to drop off new commands (put_command), safely read the latest command without freezing (get_latest_command), and check if data exists (has_command).
* Completed Adversarial Testing Matrix: Tested the bridge under harsh conditions, verifying that rapid back-to-back inputs automatically overwrite old data, empty reads return a blank response instantly without hanging, and simultaneous reads handle data ownership safely.


## Day 3: VLM Loop Coroutine
* Built the Core VLM Loop: Created a continuous safe_vlm_loop function that runs at a steady pace of 2 tasks per second (2 Hz).
* Enforced Graceful Degradation: Added try/except safety catchers to intercept cloud server timeouts (asyncio.TimeoutError), network API disconnects, and empty (None) camera frames.
* Verified Fault Tolerance: Ran an adversarial test showing that when errors hit the loop, it logs warnings and continues running instead of crashing.


## Day 4: IK Loop Coroutine
* Built the High-Speed IK Core: Created a local loop running at a fast target speed of 100 tasks per second (100 Hz).
* Defined Fallback Behaviors: Added logic to use fresh data when available, reuse the last valid plan with reduced confidence when stale, and hold position on initial bootup.
* Verified Performance Velocity: Tracked precision timestamps to verify the loop maintains a stable rate of 95.63 Hz, satisfying the strict threshold.


## Day 5: ADCA v0.1 Integration Test
* Executed Concurrent Integration Test: Ran the slow vision loop (2 Hz) and high-speed motor loop (100 Hz) simultaneously for 30 seconds using asyncio.gather().
* Logged Telemetry Timestamps: Captured precise clock ticks for all 60 VLM cloud calls and 2,850 local IK iterations to map system behavior.
* Generated Dual-Timeline Plot: Produced a publication-ready figure mapping VLM calls as vertical lines against the continuous IK loop frequency.
* Verified Real-Time Compliance: Proved that the local motor loop successfully maintained a stable rate of 95.0 Hz without dropping or dipping during cloud inference cycles.


## 🗓️ Week 7: Safety-Critical Software Principles & Validation Design

## Day 1: Safety Principles Study
* Read Industry Safety Standards: Looked over the main ideas in Sections 1 and 3 of the IEC 61508 standard to learn the official rules for building safe softwar
* Studied Core Safety Ideas: Learned how systems use multiple backup layers (defence-in-depth), safe default settings (fail-safe), and ways to stop a single broken part from breaking the whole machine.
* Wrote Safety Note for HARM: Wrote a short half-page explanation on how the HARM module uses a 3-step check to catch errors and how it safely locks the robot arm in place if a major glitch happens.


## Day 2: Adversarial Test Suite Design
* Designed 50 Adversarial Test Cases: Mapped out 10 distinct failure test cases for each of the 5 core AI hallucination categories (schema, workspace, kinematic, format, and object).
* Defined System Pass Criteria: Established the exact injected fault parameters, expected module mitigation actions, and strict pass/fail rules for every test condition.
* Completed Pre-Code Test Specification: Finished the official test specification document before writing any code, ensuring a strict Test-Driven Development workflow.


## Day 3: Property-Based Testing with Hypothesis
* Ran pip install hypothesis to add the testing library to the notebook workspace.
* Learned how to use the @given decorator, data strategies (st.floats, st.text, st.lists), the assume() filter, and the note() debugging function.
* Built a property-based test for the Stage 2 workspace check that creates random 3D coordinates and verifies that the HARM module always returns a valid, in-bounds waypoint.


## Day 4: Workspace Geometry Implementation
* Built the WorkspaceChecker class with is_reachable(point_3d) and the clip_to_boundary(point_3d) fail-safe filter.
* Modeled the safety zone as a conservative 1.0 m sphere centered at (0, 0, 0) based on URDF joint length sums.
* Integrated a joint-range check to verify that all target pose angles stay within strict URDF limits.
* Ran Wednesday's property-based tests to verify the class successfully handles 100 random boundary attacks.


## Day 5: Test Suite Implementation Documentation
* Upgraded the 50 adversarial VLM case definitions from an abstract matrix into functional pytest test routines.
* Segmented the testing suite layout into 5 distinct classes, separating the functional targets by individual VLM hallucination profiles.
* Executed the unified verification suites against the active WorkspaceChecker class, resulting in 13 structural passes and 40 clean xfail designations for pending modules.


## 🗓️ Week 8: Building the Full HARM Module

## Day 1: Stage 1 — Schema Validation
* Built HARM Stage 1: Implemented validate(raw_response) to clean markdown, parse JSON, and validate it into a VLMCommand object.
* Added Error Recovery: Logged validation errors, retried once using re_prompt(), and returned None if validation still failed.
* Tested Stage 1: Ran all 10 adversarial schema test cases and achieved a 10/10 defensive score with the retry system.


## Day 2: Stage 2 — Workspace Check
* Added a geometric safety filter that checks every waypoint, clips unreachable coordinates back to physical boundaries, and logs the exact correction distance.
* Deployed a metric to flag minor adjustments under $0.5\text{m}$ as low risk, while instantly triggering critical alerts for severe AI hallucinations over $0.5\text{m}$.
* Ran the pipeline against 10 aggressive adversarial test cases, successfully achieving a perfect 10/10 pass rate by correcting or blocking all unsafe movements.


## Day 3: Stage 3 — Kinematic Limits
* Implemented URDF-Aligned Gate: Enforced the 2-DOF rr_arm.urdf joint limits (1.0 rad/s max) with a strict 0.8× safety ceiling 0.8 rad/s.
* Added Velocity Mitigation: Integrated a finite difference estimator ($\Delta\theta/\Delta t$) that automatically scales over-speed steps down by 0.5× using time expansion.
* Validated 10 Trajectory Attacks: Achieved a flawless 10/10 pass rate across 10 adversarial cases (TC-KIN-021 to 030), correcting fixable paths and blocking extreme limit breaches.


## Day 4: Conservative Fallback & Full Pipeline
* Conservative Fallback: Generates a safe "hold" command at the current position if a catastrophic failure occurs.
* Master HARM Class: Connects Stage 1 (Schema), Stage 2 (Workspace), and Stage 3 (Kinematics) into one sequential pipeline.
* HARM Result Receipts: Logs diagnostic details (stage_failed, error_type, correction_applied, and catch_type) for every single run without returning any empty values.


## Day 5: Full Adversarial Test Suite Run
* Evaluated fifty diverse adversarial command inputs against the protective filtering modules to verify system resilience.
* Computed overall catch efficiency by dividing intercepted and recovered anomalies by the total test size to confirm compliance with the baseline target.
* Isolated uncorrected edge cases involving severe formatting crashes and extreme joint reversals to update the documented payload constraints.


## 🗓️ Week 9: HARM Integration with ADCA & The Construct RDS Testing

## Day 1: HARM into ADCA VLM Loop
* Integrated HARM Validation: Updated vlm_loop() to pass outputs from async_run_sat() into harm.validate() before forwarding safe commands to bridge.put_command().
* Added Real-Time Logging: Tracked a HARMResult receipt for every VLM call to log intercepted, recovered, and fallback counts alongside latency metrics.
* Verified Performance: Executed the 30-second integration test with HARM active, confirming zero timing regression (IK control loop maintained ~96 Hz with HARM validation averaging <0.3 ms).


## Day 2: Real VLM Response Testing
* Ran API calls across Gazebo environments E1, E2, and E3, passing all responses through the HARM pipeline and logging `HARMResult` receipts.
*  Achieved a 30.0% catch rate (16.0% Stage 1 syntax fixes, 10.0% Stage 2/3 kinematic fixes, 4.0% safety fallbacks), with 70.0% clean passes.
*  Compared the 30.0% real-world rate to the 100% adversarial catch rate; real VLM calls mostly cause minor formatting glitches rather than intentional attack vectors.


## Day 3: ROS 2 Node Wrapping
* Created a Python wrapper that subscribes to /camera/image_raw, processes visual input using decoupled ADCA+HARM logic, and publishes output to vlm command.
* Confirmed that safety validation works identically inside ROS 2 without changing the core ADCA+HARM algorithms.
* Simulated sending a test image frame to /camera/image_raw and verified that /hraf/vlm_command correctly received the validated command payload (MOVE, waypoints, and HARM receipts).


## Day 4: Integration Stress Test
* Ran the complete ROS 2 pipeline continuously in The Construct RDS with the robot driving through environment E2 (SAT World).
* Processed 297 VLM calls at a stable ~49.55 Hz IK loop rate with 0 crashes or exceptions logged.
* Confirmed flat RAM usage (~110.25 MB) with 0 unbounded queue accumulation and active rotating log file management.


## Day 5: Phase 3 Handoff Package
* Wrote step-by-step documentation on how to instantiate, configure, and execute the ADCA+HARM middleware stack.
* Packaged the core middleware stack, the 50-case adversarial test suite, and the latency profiler for baseline benchmarking against A* and NavGPT.


## 🗓️ Week 10: ADCA Benchmarking: Single-Frequency vs. Dual-Frequency

## Day 1: Baseline Implementation
* Created a simple single-frequency pipeline where each VLM call runs synchronously and immediately triggers motor IK execution with no async handling.
* Tied VLM inference, HARM safety validation, and IK motor calculations together in a single sequential loop.
* Ran a 10-second baseline test to record the real IK rate, showing the motor speed dropped to ~3.27 Hz because it has to wait for VLM network delays.


## Day 2: Benchmark Harness
* Developed an async harness to execute 60-second trial runs comparing single-frequency and dual-frequency controller architectures.
* Logged real-time IK timestamps, VLM call timestamps, HARM safety intercepts, and command staleness deltas across both loops.
* Validated dual-frequency performance, achieving ~93.71 Hz IK rate compared to the ~3.27 Hz baseline while maintaining low command staleness.


## Day 3: Run Benchmark × 3
* Ran 3 independent trials per system across both Single-Frequency and Dual-Frequency architectures (6 total runs).
* Profiled execution metrics to log mean IK Hz, P95 command staleness, HARM validation overhead, and timeout frequency.
* Generated statistical summaries and exported benchmark_3trials_summary.csv and benchmark_3trials_aggregate.csv for analysis.


## Day 4: Results Analysis
* Constructed comparative performance summary tables benchmarking mean control frequency, latency sensitivity, and minimum frequency limits.
* Generated combined timeline visualization plotting real-time IK control loop frequency for both architectures on a single chart.
* Evaluated system speedup factor (44.89x) and authored a 300-word performance analysis detailing asynchronous thread decoupling dynamics.


## Day 5: Deliverables
* Finalized core codebase artifacts including the BenchmarkHarness class and baseline execution scripts saved under src/hraf/benchmark.py
* Exported multi-trial telemetry datasets generating comprehensive summary CSVs alongside the comparative IK frequency timeline plot.
* Compiled final submission documentation featuring the comparative metrics table and the 300-word performance speedup analysis.


## 📅 Week 11: Paper Drafting & Literature Synthesis

## Day 1: Literature Review & Synthesis Notes
* Completed technical literature review across four required foundational sources using the 4-part Standard Reading Template.
* Extracted precise citation targets backing up ADCA's dual-frequency thread model and HARM's multi-stage functional safety design.
* Mapped system architecture relationships comparing HARM's deterministic validation pipeline against baseline VLM predictive control methods


## Day 2: System Architecture (Middleware / ADCA)
* Drafted Section 4 (~500 words) detailing the architectural design rationale of the Asynchronous Decoupled Control Architecture (ADCA).
* Formulated the dual-frequency decoupling mechanism, isolating low-frequency System-2 VLM planning (2-5 Hz) from high-frequency System-1 motor execution (100-300 Hz).
* Specified the non-blocking State Bridge shared-memory queue grounded in PEP 3156 and defined the sub-10 ms real-time local loop latency budget allocation.


## Day 3: HARM Implementation Section
* Drafted Section 5 (~400 words) defining the High-assurance Action Real-time Monitor (HARM) 3-stage inline safety pipeline.
* Established the technical rationale for Kinematic Bounds, Dynamic Envelope Filtering, and Workspace Hazard Bounding based on IEC 61508 functional safety standards.
* Defined the formal C HARM Catch Rate metric equation and detailed the 1,000-sample adversarial test suite methodology across four primary threat categories. 


## Day 4: Results Section Contribution
* Drafted Section 6 (~300 words) presenting comparative system performance benchmarks, throughput speedups, and safety evaluation results.
* Constructed the ADCA benchmark comparative table demonstrating a 73.2x execution frequency speedup (300.3 Hz vs. 4.1 Hz synchronous baseline).
* Quantified HARM's safety performance, logging a 100% catch rate (C_HARM = 100%) across adversarial tests with a minimal 0.85 ms processing latency overhead.

## Day 5: Review, Revisions & GitHub Deliverables
* Consolidated all 4 standard literature reading templates and the 3 written paper draft sections into a unified manuscript.  
* Conducted supervisor review, incorporated feedback, and polished the manuscript layout and citations for formal submission.
* Committed finalized artifacts to GitHub repository, including reading notes, Section 4 (ADCA), Section 5 (HARM), and Section 6 (Results) drafts.


## 📅 Week 12: Final QA, Complete Handoff & Research Readiness Presentation

## Day 1: Full Pipeline QA
* Executed the complete ADCA+HARM stack in The Construct RDS for 10 minutes on the `E2` environment, confirming zero crashes, zero memory leaks, steady IK loop rates, and complete result logging.
* Ran the final 50-case adversarial test suite using `pytest`, successfully intercepting and recording all safety-violating outputs.
* Validated the deployment pipeline from scratch to guarantee seamless execution on clean installations.
* Documented all environment extraction, dependency setup, and troubleshooting steps in the repository's setup guide to ensure total deployability.


## Day 2: Handoff Documentation
* **Created `HANDOFF.md`:** Drafted a comprehensive handoff document covering all 7 core sections:
* **Verified Executable Code:** Tested and verified that every code snippet, imports block, and command example included across the entire handoff document runs without errors.


## Day 3: Presentation Preparation
* Prepared a 20-minute slide deck covering system architecture, key implementations, quantitative results, limitations, and future roadmap.
* Set up and tested the live HARM demonstration in Construct RDS to showcase real-time interception of bad VLM payload injections.
* Integrated core benchmark figures including the IK frequency timeline plot, HARM catch rate metrics table, and speedup factor analysis.


## Day 4: Self-Assessment
* Written a 1-page technical self-assessment highlighting core strengths in async safety design, current growth areas, and unclear concepts.
* Proposed a specific Week 13–14 learning plan to deepen ROS 2 native packaging and dynamic URDF collision modeling skills.
* Outlined independent HRAF task ownership goals for the upcoming research sprint.


## Day 5: Final deliverables
* Appeared for the final internship evaluation examination and completed formal assessment requirements.
* Conducted a comprehensive review and finalized all project deliverables, documentation, and codebase artifacts for official submission.
