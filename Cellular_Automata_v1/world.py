from default_values import *
from cell import *
import threading
from time import sleep

class World:
    def __init__(self):
        self.colony01_list = []
        self.colony02_list = []
        self.steps = 0
        self.running = False

        self.colony01_list.append(Cell(10, 25, 1, 50, 1, [200, 200]))
        self.colony01_thread = threading.Thread(target=self.Thread_colony_process, args=(self.colony01_list))
        self.colony01_thread.daemon = True

    def run(self):
        self.running = True
        self.colony01_thread.start()

    def Thread_colony_process(self, colony):
        while self.running:
            sleep(DELAY)
            self.steps += 1

            for cell in self.colony01_list:
                if cell.dead:
                    self.colony01_list.remove(cell)
                    continue
                cell.process(self.colony01_list)

    def process(self):
        if self.running:
            pass
            #self.steps += 1


    def render(self, window):
        for cell in self.colony01_list:
            cell.render(window)