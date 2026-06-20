class Building:
    def __init__(self, name, building_type, action, x, y, enabled):
        self.name = name
        self.building_type = building_type
        self.action = action
        self.x = x
        self.y = y
        self.enabled = enabled

    def __str__(self):
        return (
            f"{self.name} "
            f"({self.building_type}) "
            f"[{self.action}] "
            f"({self.x}, {self.y}) "
            f"enabled={self.enabled}"
        )