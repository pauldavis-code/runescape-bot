import random


class Randomizer:
    def __init__(self, min, max, step):
        self.min = min
        self.max = max
        self.step = step

    def select(self):
        # print(random.randint(self.min, self.max))
        return str(random.randint(self.min, self.max))
