import pygame.font

from default_values import *
from world import *

class GUI:
    def __init__(self):
        self.window = pygame.display.set_mode((wX, wY))
        pygame.display.set_caption("Cellular Automata v1")
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.world = World()

        self.font = pygame.font.SysFont("Consolas", 12)

    def update_info(self):
        selfinfo = f"""FPS: {round(self.clock.get_fps())}
Steps: {self.world.steps}
Colony 1: {len(self.world.colony01_list)}"""
        lines = selfinfo.splitlines()
        for i, l in enumerate(lines):
            self.window.blit(self.font.render(l, 0, COLOR_WHITE), (0, 0+12*i))

    def run(self):
        self.world.run()
        while self.isRunning:
            self.clock.tick(FPS)
            self.eventHandler()
            self.processHandler()
            self.displayHandler()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.isRunning = False
                exit()

    def processHandler(self):
        self.world.process()

    def displayHandler(self):
        self.window.fill(COLOR_BLACK)

        self.world.render(self.window)

        self.update_info()
        pygame.display.flip()

