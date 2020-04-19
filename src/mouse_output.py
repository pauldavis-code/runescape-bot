import time

from pynput.mouse import Button, Controller

class MouseOutput:
    def __init__(self):
        self.mouse = Controller()

    def set_mouse(self, x, y):
        self.mouse.position = (x, y)
        time.sleep(.2)
        self.l_click_mouse()

    def l_click_mouse(self):
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)
