import GUI
import bacteria
import genes
import logger
import query
import tasks



class Environment:
    def __init__(self, amountAgents: int, amountProvisions: int):
        self.coordinates: dict = {}
        self.amountAgents: int = amountAgents
        self.amountProvisions: int = amountProvisions
        self.foodCoordinates: list[list[int]] = []
        self.waterCoordinates: list[list[int]] = []

    def createEnvironment(self):
        import random

        for i in range(0, self.amountAgents):
            self.coordinates[i] = random.randint(10, 590), random.randint(10, 590)

        for i in range(0, self.amountProvisions):
            self.foodCoordinates.append([random.randint(10, 590), random.randint(10, 590)])
            self.waterCoordinates.append([random.randint(10, 590), random.randint(10, 590)])

class Dependencies:
    Bacteria = bacteria.Bacteria
    Logger = logger.Logger
    Query = query.Query

    genes = genes
    tasks = tasks


class Simulation:
    def __init__(self, amountAgents: int, amountProvisions: int):
        self.amountAgents: int = amountAgents
        self.amountProvisions: int = amountProvisions
        self.environment: Environment = Environment(self.amountAgents, self.amountProvisions)
        self.environment.createEnvironment()
        self.dependencies: Dependencies = Dependencies()

        self.entities: list = []


    @staticmethod
    def methodWrapper(entities: list[bacteria.Bacteria]):
        for entity in entities:
            yield entity.main

    def firstClass(self, coordinates: list[int],
                   foodCoordinates: list[list[int]], waterCoordinates: list[list[int]]):  #Первый класс
        animal = bacteria.Bacteria(self.dependencies, coordinates,
                                   foodCoordinates, genes.Gene(1, 0.5),
                                   waterCoordinates, genes.Gene(2, 0.5),
                                   10, genes.Gene(5, 0.5))
        return animal
    def secondClass(self, coordinates: list[int],
                    foodCoordinates: list[list[int]], waterCoordinates: list[list[int]]):  #Второй класс
        animal = bacteria.Bacteria(self.dependencies, coordinates,
                                   foodCoordinates, genes.Gene(1, 0.5),
                                   waterCoordinates, genes.Gene(2, 0.5),
                                   5, genes.Gene(5, 0.5))
        return animal
    def thirstClass(self, coordinates: list[int],
                    foodCoordinates: list[list[int]], waterCoordinates: list[list[int]]):  #Третий класс
        animal = bacteria.Bacteria(self.dependencies, coordinates,
                                   foodCoordinates, genes.Gene(1, 0.5),
                                   waterCoordinates, genes.Gene(2, 0.5),
                                   5, genes.Gene(5, 0.5))
        return animal


    def main(self):
        import random
        import multiprocessing as mp


        for i in range(0, self.amountAgents):  # Создание объектов класса бактерии
            self.entities.append(self.thirstClass(self.environment.coordinates[i],
                                 self.environment.foodCoordinates,
                                 self.environment.waterCoordinates))

        window = GUI.GUI(self.environment.foodCoordinates, self.environment.waterCoordinates, 5, 5)
        window.createGUI()
        # p = mp.Pool(self.amountAgents)

        while True:
            self.entities[0].main()
            window.printGUI([self.entities[0].coordinates])

simulation = Simulation(10, 5)
simulation.main()
