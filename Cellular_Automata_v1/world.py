from default_values import *
from cell import *
import threading


class World:
    def __init__(self):
        self.colony01_list = []
        self.colony02_list = []
        self.steps = 0
        self.running = False
        self.delay = 0

        self.world_data = {
            "Colony01" : {
                "str" : "",
                "mat" : "",
                "mxc" : "",
                "lit" : "",
            },
            "Colony02" : {
                "str": "",
                "mat": "",
                "mxc": "",
                "lit": "",
            },
        }


        ### TO DO Fix desynchronized threads and a better implementation of steps

        self.data_thread = threading.Thread(target=self.Thread_data_process)
        self.data_thread.daemon = True

        self.colony01_list.append(Cell(10, 7, 1, 10, 1, [200, 200]))
        self.colony01_thread = threading.Thread(target=self.Thread_colony_process, args=(self.colony01_list,))
        self.colony01_thread.daemon = True

        self.colony02_list.append(Cell(10, 25, 1, 50, 2, [400, 400]))
        self.colony02_thread = threading.Thread(target=self.Thread_colony_process, args=(self.colony02_list,))
        self.colony02_thread.daemon = True

    def run(self):
        self.data_thread.start()
        self.colony01_thread.start()
        self.colony02_thread.start()
        self.running = True

    def Thread_colony_process(self, colony):
        toprocess_colony = colony

        while True:
            while self.running:
                sleep(DELAY)
                self.steps += 1

                for cell in toprocess_colony:
                    if cell.dead:
                        toprocess_colony.remove(cell)
                        continue
                    cell.process(toprocess_colony)

    def Thread_data_process(self):
        while True:
            while self.running:
                colony01_str = 0
                colony02_str = 0

                for cell1, cell2 in zip(self.colony01_list, self.colony02_list):
                    data1, data2 = cell1.get_values(), cell2.get_values()
                    colony01_str += data1[0]
                    colony02_str += data1[0]

                self.world_data["Colony01"]["str"] = str(round(colony01_str / len(self.colony01_list), 3))
                self.world_data["Colony02"]["str"] = str(round(colony02_str / len(self.colony02_list), 3))

    def process(self):
        if self.running:
            pass
            #self.steps += 1


    def render(self, window):
        for cell1, cell2 in zip(self.colony01_list, self.colony02_list):
            cell1.render(window)
            cell2.render(window)