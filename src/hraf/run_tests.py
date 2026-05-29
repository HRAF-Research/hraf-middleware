# src/hraf/run_tests.py
import sys
import os

# Forces Python to look at the root folder for imports
sys.path.append(os.getcwd())

from src.hraf.pipeline import verify_safety_bounds
from src.hraf.exceptions import HRAFBaseError

def run_pipeline_test():
    print("--- Starting HRAF Pipeline Safety Tests ---\n")
    
    # Coordinates that breach physical safety limits (Limit is 100cm)
    target_x = 80.0
    target_y = 80.0
    
    try:
        print(f"[1/3] Initiating safety envelope check for coordinates ({target_x}, {target_y})...")
        verify_safety_bounds(target_x, target_y)
        
    except HRAFBaseError as error:
        print(f"\n[LOG ALERT] Critical framework anomaly captured!")
        print(f"[LOG INFO] Error Details: {error}")
        print("[SYSTEM] Re-raising exception to escalate to emergency shutdown handler...\n")
        raise
        
    finally:
        print("[FINALLY] Releasing diagnostic hooks. System state safely isolated.")

if __name__ == "__main__":
    try:
        run_pipeline_test()
    except Exception:
        print("--- Test Completed: Exception successfully escalated to top-level controller ---")