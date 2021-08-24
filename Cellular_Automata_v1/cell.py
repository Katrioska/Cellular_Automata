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

    def get_values(self):
        return [self.strength, self.maturity, self.maxchilds, self.lifetime]

    def random_move(self):
        x,y = self.rect.x, self.rect.y
        mx, my = 0,0

        isX_valid = False
        isY_valid = False

        rvalue = randint(1, 4)
        if rvalue == 4: ### LEFT
            x -= SPEED
            mx += -1
        if rvalue == 3: ### RIGHT
            x += SPEED
            mx += 1
        if rvalue == 2: ### UP
            y -= SPEED
            my += -1
        if rvalue == 1: ### DOWN
            y += SPEED
            my += 1
        if x>0 or x<wX-CELL_SIZE:
            isX_valid = True
        if y>0 or y<wY-CELL_SIZE:
            isY_valid = True

        #print(f"{rvalue}: {mx} = {my}\t X: {isX_valid} Y: {isY_valid}")

        if isX_valid and isY_valid:
            self.rect.move_ip(SPEED*mx, SPEED*my)

        """if rvalue == 4: ### LEFT
            self.rect.move_ip(-SPEED, 0)
        if rvalue == 3: ### RIGHT
            self.rect.move_ip(+SPEED, 0)
        if rvalue == 2: ### UP
            self.rect.move_ip(0, -SPEED)
        if rvalue == 1: ### DOWN
            self.rect.move_ip(0, +SPEED)
        """
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
                    #pass
                    self.reproduce(colonyList)
        else:
            self.dead = True

    def render(self, window):
        color = COLOR_WHITE
        if self.colonyID == 1:
            color = COLOR_BLUE
        elif self.colonyID == 2:
            color = COLOR_RED
        # TO DO Implement a random color system for each colony

        pygame.draw.rect(window, color, self.rect)