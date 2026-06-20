from farmer.config import Config

def check_layout():
    buildings = Config.load_city_layout()

    for building in buildings:
        print(building)

def check_buildings():
    print("check buildings")

def show_info():
    print("show info")