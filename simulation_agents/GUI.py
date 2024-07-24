class GUI:
    def __init__(self, foodCoordinates, waterCoordinates, animalsAmount, amountProvisions):
        self.rectAnimal = {}
        self.rectWater = {}
        self.rectFood = {}
        self.animalObject = None
        self.food = None
        self.water = None
        self.sc = None
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates
        self.amountProvisions = amountProvisions
        self.animalsAmount = animalsAmount

    def createGUI(self):
        import pygame

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 100, 0)
        BLUE = (0, 191, 255)

        self.sc = pygame.display.set_mode((600, 600))

        self.animalObject = pygame.Surface((10, 10))
        self.animalObject.fill(BLACK)
        self.food = pygame.Surface((15, 15))
        self.food.fill(GREEN)
        self.water = pygame.Surface((15, 15))
        self.water.fill(BLUE)

        for r in range(1, self.animalsAmount):
            self.rectAnimal[r] = self.animalObject.get_rect()

        for j in range(1, self.amountProvisions):
            self.rectFood[j] = self.food.get_rect()
            self.rectWater[j] = self.water.get_rect()
            self.rectFood[j].x = self.foodCoordinates[j][0]
            self.rectWater[j].x = self.waterCoordinates[j][0]
            self.rectFood[j].y = self.foodCoordinates[j][1]
            self.rectWater[j].y = self.waterCoordinates[j][1]

    def printGUI(self, animalCoordinates):
        import pygame
        import sys

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 100, 0)
        BLUE = (0, 191, 255)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

        for r in range(0, len(animalCoordinates)):
            self.rectAnimal[r].x = animalCoordinates[r][0]
            self.rectAnimal[r].y = animalCoordinates[r][1]

        self.sc.fill(WHITE)

        for j in range(1, self.amountProvisions):
            self.sc.blit(self.food, self.rectFood[j])
            self.sc.blit(self.water, self.rectWater[j])

        for r in range(1, self.animalsAmount):
            self.sc.blit(self.animalObject, self.rectAnimal[r])

        pygame.display.update()
