import pyautogui

class Screen:

    @staticmethod
    def get_pixel(x,y):
        return pyautogui.pixel(x,y)