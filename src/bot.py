import json
import os
import time

from src.mouse_output import MouseOutput

class Bot:
    def __init__(self, objective):
        self.objective = objective
        self.current_loops = 0 # number of loops elapsed
        self.brain = self._load_objective()
        self.mouse = MouseOutput()

    def _load_objective(self):
        data = os.path.join(os.getenv("DATA_DIR"), self.objective + ".json")
        print("script: ", data)
        with open(data, "r") as file:
            brain = file.read()
            return json.loads(brain)

    def loop(self):
        for index, action in enumerate(self.brain):
            x, y, button, game_time = action['x'], action['y'], action['button'], action['time']

            self.mouse.set_mouse(x=x, y=y) # sets mouse cursor for click and clicks

            if index < len(self.brain) - 1:  # if the index is less then the number of scrips, subtract times for delay
                interval = self.brain[index + 1]['time'] - game_time #calculated amount of time between each action
                time.sleep(interval) # this is the time between each action
            else:
                print("=== complete - next script ===")





