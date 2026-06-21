import random
import time
import pyautogui

from farmer.state_detector import GlobalStateDetector, State, BuildingStateDetector, BuildingState
from farmer.screen import Screen

class AutomationEngine:
    UI_ANCHOR = (551, 99)  # Example anchor point for UI detection

    def __init__(self):
        pass

    def reset_ui(self):
        while GlobalStateDetector.detect_state() != State.SAFE:
            print(f"[{time.ctime()}] Popup detected. Attempting to reset UI...")
            pyautogui.click(*self.UI_ANCHOR)  # Click on the anchor point to reset the UI
            time.sleep(1)  # Wait for the UI to reset
        time.sleep(1)  # Wait for the UI to reset
    
    def click_building(self, building):
        pyautogui.click(building.x, building.y)
        time.sleep(1)
    
    def schedule_next_check(self, building):
        base = building.cycle_time + 5  # Add a small buffer to the cycle time
        jitter = random.uniform(-0.05, 0.10) * building.cycle_time  # Add a jitter of -5% to +10% of the cycle time
        building.next_check = time.time() + base + jitter  # Update next_check based on

    def handle_collect_flow(self, building):
        # CASE: building was already finishing production, click happened on first click
        print(f"[{time.ctime()}] [COLLECT] {building.name}")
        time.sleep(2)

    def handle_production_flow(self, building):
        # CASE: building was idle, clicking opened production popup

        state = BuildingStateDetector.detect_building_state()
        if state == BuildingState.IDLE:
            print(f"[{time.ctime()}] [START PRODUCTION] {building.name}")
            pyautogui.click(744, 595) # clicking on start prod button
            time.sleep(3)  # Wait for the production to start and windows to close
        elif state == BuildingState.PRODUCING:
            print(f"[{time.ctime()}] [ALREADY PRODUCING] {building.name}")
            self.reset_ui()  # Reset UI to close the popup
            time.sleep(3)

    def handle_production_building(self, building):
        print(f"Handling building: {building}")
        self.reset_ui()  # Ensure UI is in a safe state before interacting with the building
        self.click_building(building)  # Click on the building to interact with it
        state = GlobalStateDetector.detect_state()
        if state == State.SAFE:
            self.handle_collect_flow(building)  # Handle the collect flow
            self.click_building(building)
            self.handle_production_flow(building)  # Handle the production flow
            self.schedule_next_check(building)
            return
        self.handle_production_flow(building)  # Handle the production flow
        self.schedule_next_check(building)

    def handle_residential(self, building):
        print(f"[{time.ctime()}] [HANDLE RESIDENTIAL] {building.name}")
        self.reset_ui()  # Ensure UI is in a safe state before interacting with the building
        self.click_building(building)  # Click on the building to interact with it
        state = GlobalStateDetector.detect_state()
        if state == State.SAFE:
            print(f"[{time.ctime()}] [COLLECT TAX] {building.name}")
            self.schedule_next_check(building)
        else:
            print(f"[{time.ctime()}] [STILL PRODUCING TAX] {building.name}")
            self.reset_ui()  # Reset UI to close the popup
            building.next_check = time.time() + (building.cycle_time / 4)

    def run_cycle(self, buildings):
        current_time = time.time()
        for building in buildings:
            if not building.enabled:
                print(f"Skipping disabled building: {building.name}")
                continue
            if current_time < building.next_check:
                print(f"Skipping {building.name}, next check at {time.ctime(building.next_check)}")
                continue
            if building.building_type == "residential":
                self.handle_residential(building)  # Handle residential buildings
            elif building.building_type == "production":
                self.handle_production_building(building)  # Handle each building in the cycle

    def run_forever(self, buildings):
        cycle = 0
        while True:
            cycle += 1
            if cycle > 10000:
                break
            print(f"\n=== NEW CYCLE {cycle} START ===\n")
            random.shuffle(buildings)
            self.run_cycle(buildings)

            print("\n=== CYCLE DONE → WAITING ===\n")

            next_wakeup = min(building.next_check for building in buildings if building.enabled)
            sleep_time = max(1, next_wakeup - time.time())
            print(f"[{time.ctime()}] Next wakeup at {time.ctime(next_wakeup)} (in {sleep_time:.2f} seconds)")
            time.sleep(sleep_time)  # small breathing room
