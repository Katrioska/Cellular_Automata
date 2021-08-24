from random import randint, choice
from time import sleep, time
import pygame
pygame.init()

MUTATION = (False, False, False, False, False, False, False, False, False, True)
MUTATION_int = 0.1
CELL_SIZE = 5
SPEED = 4

### Delay for each step in Miliseconds
DELAY = 0.01

wX = 800
wY = 600

FPS = 60

COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

print(wY-CELL_SIZE)