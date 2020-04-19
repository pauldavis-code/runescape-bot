import os
import time
import json

from pynput import mouse

class MouseInput:
    def __init__(self, objective):
        self.objective = objective
        self.total_recordings = 0
        self.data_store = []

        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed):
        if not pressed and button == mouse.Button.left:
            self.data_store.append({
                "x": x,
                "y": y,
                "button": str(button),
                "time": time.time()
            })
            print('{0}: {1}'.format(self.total_recordings, self.data_store[self.total_recordings]))
            self.total_recordings += 1
        elif button == mouse.Button.right:
            print("End Recording")
            self.write_json()
            return False

    def write_json(self):
        data = json.dumps(self.data_store)
        path = os.path.join(os.getenv("DATA_DIR"), self.objective + ".json")
        with open(path, "w+") as file:
            file.write(data)


