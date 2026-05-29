# src/hraf/exceptions.py

class HRAFBaseError(Exception):
    """Base exception class for the Hybrid Robot Action Framework."""
    pass

class VLMResponseError(HRAFBaseError):
    """Raised when the Vision-Language Model returns an invalid response."""
    pass

class JSONParseError(HRAFBaseError):
    """Raised when parsing a VLM string response into JSON fails."""
    pass

class WorkspaceViolationError(HRAFBaseError):
    """Raised when a commanded coordinate falls outside the safety boundary."""
    pass

class KinematicFeasibilityError(HRAFBaseError):
    """Raised when a joint configuration is mathematically unreachable."""
    pass
  
class HardwareFaultError(HRAFBaseError):  
    """Raised when a hardware component reports a critical failure."""  
    pass 
class NetworkTimeoutError(HRAFBaseError):  
    """Raised when a VLM or network request times out."""  
    pass 
class NetworkTimeoutError(HRAFBaseError):  
    """Raised when a VLM or network request times out."""  
    pass 
class InvalidCommandError(HRAFBaseError):  
    """Raised when a commanded action fails validation requirements."""  
    pass 
