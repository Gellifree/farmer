from farmer.screen import Screen
from enum import Enum

class State(Enum):
    POPUP = "POPUP"
    SAFE = "SAFE"
    UNKNOWN = "UNKNOWN"

class BuildingState(Enum):
    IDLE = "IDLE"
    PRODUCING = "PRODUCING"
    UNKNOWN = "UNKNOWN"

class GlobalStateDetector:
    def __init__(self):
        pass

    ANCHOR = (551, 99)  # Example anchor point for state detection
    GRAY_FILTER = (50, 32, 17)  # Example RGB value for gray filter
    SAFE_COLOR = (84, 54, 28)  # Example RGB value for safe state

    @staticmethod
    def detect_state():
        r,g,b = Screen.get_pixel(*GlobalStateDetector.ANCHOR)
        if (r,g,b) == GlobalStateDetector.GRAY_FILTER:
            return State.POPUP
        elif (r,g,b) == GlobalStateDetector.SAFE_COLOR:
            return State.SAFE
        else:
            return State.UNKNOWN

class BuildingStateDetector:
    def __init__(self):
        pass

    ANCHOR = (744, 595)  # Example anchor point for state detection
    IDLE = (138, 73, 28)  # Example RGB value for idle state for building
    PRODUCING = (168, 127, 56)  # Example RGB value for producing state of 5 min type

    @staticmethod
    def detect_building_state():
        r,g,b = Screen.get_pixel(*BuildingStateDetector.ANCHOR)
        if (r,g,b) == BuildingStateDetector.IDLE:
            return BuildingState.IDLE
        elif (r,g,b) == BuildingStateDetector.PRODUCING:
            return BuildingState.PRODUCING
        else:
            return BuildingState.UNKNOWN