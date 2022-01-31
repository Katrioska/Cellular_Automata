from default_values import *
from cell import *
import threading


class World:
    def __init__(self):
        self.colony01_list = []
        self.colony02_list = []
        self.steps = 0
        self.running = False

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

        self.data_thread = threading.Thread(target=self.Thread_data_process)
        self.data_thread.daemon = True

        self.collisions_thread = threading.Thread(target=self.Thread_collisions_process, args=())
        self.collisions_thread.daemon = True

        self.colony01_list.append(Cell(10, 7, 1, 10, 1, [200, 200]))
        self.colony01_thread = threading.Thread(target=self.Thread_colony_process, args=(self.colony01_list, 0))
        self.colony01_thread.daemon = True

        self.colony02_list.append(Cell(10, 25, 1, 50, 2, [400, 400]))
        self.colony02_thread = threading.Thread(target=self.Thread_colony_process, args=(self.colony02_list, 1))
        self.colony02_thread.daemon = True

    def run(self):
        self.colonies_ready = {}
        self.collisions_ready = False
        self.cells_ready = False
        self.READY = True

        self.data_thread.start()
        self.colony01_thread.start()
        self.colony02_thread.start()
        self.collisions_thread.start()
        self.running = True
        self.totalCells = 0

    def Thread_collisions_process(self):
        while True:
            while self.running and self.READY and self.cells_ready and not self.collisions_ready:
                self.collisions_ready = False

                for c1 in self.colony01_list:
                    for c2 in self.colony01_list:
                        if c1.rect.colliderect(c2.rect) and c1 != c2:
                            c1.dead = True
                            #c2.dead = True
                            #c1.rect.move(c1.oldPOS[0], c1.oldPOS[1])
                            #c2.rect.move(c2.oldPOS[0], c2.oldPOS[1])
                            print(f"collision at {c1.rect.x}, {c1.rect.y}")

                for c3 in self.colony02_list:
                    for c4 in self.colony02_list:
                        if c3.rect.colliderect(c4.rect) and c3 != c4:
                            c3.dead = True
                            #c4.dead = True
                            #c3.rect.move(c3.oldPOS[0], c3.oldPOS[1])
                            #4.rect.move(c4.oldPOS[0], c4.oldPOS[1])
                            print(f"collision at {c3.rect.x}, {c3.rect.y}")
                self.collisions_ready = True

    def Thread_colony_process(self, colony, ID):
        toprocess_colony = colony

        while True:
            while self.running and self.READY:
                self.colonies_ready[ID] = False
                if self.steps == 0:
                    self.colonies_ready[ID] = True

                sleep(DELAY)

                for cell in toprocess_colony:
                    if cell.dead:
                        toprocess_colony.remove(cell)
                        continue
                    cell.process(toprocess_colony)
                self.colonies_ready[ID] = True
                print()

    def Thread_data_process(self):
        while True:
            while self.running:
                colony01_str = 0
                colony02_str = 0

                for cell1, cell2 in zip(self.colony01_list, self.colony02_list):
                    data1, data2 = cell1.get_values(), cell2.get_values()
                    colony01_str += data1[0]
                    colony02_str += data2[0]

                    colony01_lt =+ data1[3]
                    colony02_lt = + data2[3]
                self.world_data["Colony01"]["str"] = str(round(colony01_str / len(self.colony01_list), 3))
                self.world_data["Colony02"]["str"] = str(round(colony02_str / len(self.colony02_list), 3))

    def process(self):
        #while(self.running):

        if self.running:
            #'''
            print(f"""READY: {self.READY}
colony01_ready: {self.colonies_ready}
collisions_ready: {self.collisions_ready}
running: {self.running}\n""")
#'''
            if all(value == True for value in self.colonies_ready.values()):
                self.cells_ready = True
                #print("CELLS READY")
                #self.READY = True
                #self.steps += 1
                if self.cells_ready and self.collisions_ready:
                    self.READY = True
                    self.steps += 1
                    #print("ALL READY\n")
            else:
                self.READY = False
                self.cells_ready = False

            self.totalCells = len(self.colony01_list) + len(self.colony02_list)
            if self.totalCells == 0:
                self.running = False

    def render(self, window):
        for cell1, cell2 in zip(self.colony01_list, self.colony02_list):
            cell1.render(window)
            cell2.render(window)

    def PAUSE(self):
        self.running = not self.running