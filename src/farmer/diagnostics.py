from farmer.config import Config
from farmer.screen import Screen
from farmer.state_detector import GlobalStateDetector

def check_layout():
    buildings = Config.load_city_layout()

    for building in buildings:
        print(building)

def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def check_buildings():
    r,g,b = Screen.get_pixel(744, 595)
    hex_color = rgb_to_hex(r, g, b)
    print(f"Pixel at (744, 595): RGB({r}, {g}, {b}) = {hex_color}")

def show_info():
    print(GlobalStateDetector.detect_state())