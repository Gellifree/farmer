import json
from farmer.building import Building
from pathlib import Path

class Config:

    @staticmethod
    def load_city_layout():

        DATA_FILE = (
            Path(__file__).parent
            / "data"
            / "city_layout.json"
        )

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        buildings = []

        for item in data["buildings"]:
            building = Building(
                name=item["name"],
                building_type=item["type"],
                action=item["action"],
                x=item["x"],
                y=item["y"],
                cycle_time=item["cycle_time"],
                enabled=item["enabled"]
            )
            buildings.append(building)
        return buildings