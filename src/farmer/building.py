class Building:
    def __init__(self, name, building_type, action, x, y, cycle_time, enabled):
        self.name = name
        self.building_type = building_type
        self.action = action
        self.x = x
        self.y = y
        self.cycle_time = cycle_time
        self.enabled = enabled
        self.next_check = 0  # Initialize next_check to 0

    def __str__(self):
        return (
            f"{self.name} "
            f"({self.building_type}) "
            f"[{self.action}] "
            f"({self.x}, {self.y}) "
            f"cycle_time={self.cycle_time}, "
            f"enabled={self.enabled}"
        )