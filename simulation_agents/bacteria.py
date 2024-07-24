class Entity:
    instances = {}
    counter = 0
    def __init__(self, dependencies, Logger):
        self.logger: dependencies.Logger = Logger("logs/bacterias")

        Entity.instances[self] = Entity.counter
        Entity.counter += 1
        self.logger.info(f"{Entity.instances[self]} bacteria created")

class Bacteria(Entity):
    def __init__(self, dependencies, coordinates: list[int],
                 foodCoordinates: list[list[int]], foodCost,
                 waterCoordinates: list[list[int]], waterCost,
                 visionDistance, speed):
        super().__init__(dependencies, dependencies.Logger)

        self.coordinates: list[int] = coordinates
        self.foodCoordinates: list[list[int]] = foodCoordinates
        self.waterCoordinates: list[list[int]] = waterCoordinates
        self.foodCost: dependencies.genes.Gene = foodCost
        self.waterCost: dependencies.genes.Gene = waterCost
        self.visionDistance: dependencies.genes.Gene = visionDistance
        self.speed: dependencies.genes.Gene = speed
        self.geneCluster = dependencies.genes.GeneCluster([foodCost, waterCost, visionDistance, speed])
        self.hungry: int = 100
        self.thirst: int = 100
        self.need: int = 0

        self.query: dependencies.Query = dependencies.Query(dependencies, self.coordinates,
                                                            self.foodCoordinates, self.waterCoordinates, self)

    def __str__(self) -> str:
        return ("Simulation Agents 1.9.2\n"
                "Type: Agent, bacteria")

    def detectNeed(self) -> None:
        import random

        if len(self.query) == 0:
            if self.hungry > self.thirst:
                self.need = 0
            elif self.thirst > self.hungry:
                self.need = 1
            else:
                self.need = random.choice([0, 1])
        else:
            self.query.startTask()

    def main(self) -> None:
        match self.need:
            case 0:
                self.query.generatorEatTask()
            case 1:
                self.query.generatorWaterTask()
