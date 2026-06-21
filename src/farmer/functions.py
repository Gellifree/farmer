from farmer.config import Config
from farmer.automation_engine import AutomationEngine
import time

def start_production():
    buildings = Config.load_city_layout()
    engine = AutomationEngine()
    engine.run_forever(buildings)