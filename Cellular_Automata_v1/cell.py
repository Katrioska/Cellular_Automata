from default_values import *

class Cell:
    def __init__(self, strength, maturity, maxchilds, lifetime, ColonyID, position):
        self.strength = strength        #Parent Inherited
        self.maturity = maturity        #Parent Inherited
        self.maxchilds = maxchilds      #Parent Inherited
        self.lifetime = lifetime        #Parent Inherited
        self.colonyID = ColonyID        #Parent Inherited

        self.current_lifetime = 0
        self.childs = 0

        self.dead = False

        self.rect = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)

    def random_move(self):
        x,y = self.rect.x, self.rect.y

        rvalue = randint(1, 4)
        if rvalue == 4: ### LEFT
            self.rect.move_ip(-SPEED, 0)
        if rvalue == 3: ### RIGHT
            self.rect.move_ip(+SPEED, 0)
        if rvalue == 2: ### UP
            self.rect.move_ip(0, -SPEED)
        if rvalue == 1: ### DOWN
            self.rect.move_ip(0, +SPEED)

        #TO DO Fix cells going out of the screen and add collision with other cells

    def mutation(self):
        if choice(MUTATION):
            strengthMut = self.strength + (self.strength * MUTATION_int * choice([-1, 1]))
            maturityMut = self.maturity + (self.maturity * MUTATION_int * choice([-1, 1]))
            maxchildMut = self.maxchilds + (self.maxchilds * MUTATION_int * choice([-1, 1]))
            lifetimeMut = self.lifetime + (self.lifetime * MUTATION_int * choice([-1, 1]))

            return (strengthMut, maturityMut, maxchildMut, lifetimeMut)
        else:
            return (self.strength, self.maturity, self.maxchilds, self.lifetime)

    def reproduce(self, colonyList):
        values = self.mutation()
        colonyList.append(Cell(values[0], values[1], values[2], values[3], self.colonyID, (self.rect.x, self.rect.y)))
        self.childs += 1

    def process(self, colonyList):
        self.current_lifetime += 1
        if not self.current_lifetime >= self.lifetime:
            self.random_move()
            if self.current_lifetime >= self.maturity and self.childs <= round(self.maxchilds):
                if choice([True, False]):
                    self.reproduce(colonyList)
        else:
            self.dead = True

    def render(self, window):
        pygame.draw.rect(window, COLOR_BLUE, self.rect)