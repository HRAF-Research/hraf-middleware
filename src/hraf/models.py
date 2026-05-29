%%writefile src/hraf/models.py
from dataclasses import dataclass
from typing import List, Literal
from pydantic import BaseModel, Field

# --- ROBOT STATE DATACLASS (From Tuesday) ---
# Thread-safe read-only snapshot tracking the physical joint motor telemetry
@dataclass(frozen=True)
class RobotState:
    position: list          # [x, y, z] coordinate array
    orientation: list       # Quaternion array [qx, qy, qz, qw]
    joint_angles: list      # Individual actuator joint positions
    timestamp: float        # Chronological system epoch marker

# --- FRIDAY TASK: STAGE 2 PYDANTIC MODEL WITH FIELD CONSTRAINTS ---
class VLMCommand(BaseModel):
    # Enforces that the robot trajectory list cannot be completely empty
    waypoints: List[list] = Field(..., min_length=1)  
    
    # Defaults to an empty list layout if no obstacles are detected by the AI
    obstacles: List[list] = Field(default_factory=list) 
    
    # Enforces strict numeric limits: confidence must stay between 0.0 and 1.0
    confidence: float = Field(..., ge=0.0, le=1.0)      
    
    # Strict Enum Mapping: blocks any action outside this specific list
    action: Literal['move', 'hold', 'recover']          
    
    # Preserves the raw string response for developer logs
    raw_response: str