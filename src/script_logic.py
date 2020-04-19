from src.bot import Bot
from src.randomizer import Randomizer

class Logic:
    def __init__(self):
        self.current_loops = 0 # current loop of the full script
        self.n_loops = 1 # number of times the full script repeats

    def run(self):
        while self.current_loops < self.n_loops:

            script_list = ("weeds_clean2",
                           "east_bank1"
                           ) # scripts to run

            # + Randomizer(1, 8, 1).select() <====#==== randomizer(min,max,step)

            for index, current_script in enumerate(script_list):
                # print(index, current_script)
                bot = Bot(current_script)
                bot.loop()

            self.current_loops += 1
            print("loop number: " + str(self.current_loops))
