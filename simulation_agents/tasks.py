class Task:
    instances: dict = {}
    counter: int = 0
    def __init__(self, dependencies):
        self.dependencies = dependencies

        self.logger: dependencies.Logger = self.dependencies.Logger("logs/tasks.log")

        Task.instances[self]: int = Task.counter
        Task.counter += 1
        self.logger.info(f"{Task.instances[self]} task created")

    def start(self):
        self.logger.info(f"{Task.instances[self]} task started")


class Move(Task):
    def __init__(self, dependencies, coordinates: list[int], target: list[int]):
        super().__init__(dependencies)

        self.coordinates: list[int] = coordinates
        self.target: list[int] = target

    def start(self):
        super().start()

        self.coordinates[0]: int = self.target[0]
        self.coordinates[1]: int = self.target[1]

class Eat(Task):
    def __init__(self, dependencies, coordinates: list[int], foodCoordinates: list[int], bacteria):
        super().__init__(dependencies)

        self.coordinates: list[int] = coordinates
        self.foodCoordinates: list[int] = foodCoordinates
        self.bacteria: dependencies.Bacteria = bacteria

    def start(self):
        super().start()

        self.bacteria.hungry -= self.bacteria.foodCost

class Drink(Task):
    def __init__(self, dependencies, coordinates: list[int], waterCoordinates: list[int], bacteria):
        super().__init__(dependencies)

        self.coordinates: list[int] = coordinates
        self.waterCoordinates: list[int] = waterCoordinates
        self.bacteria: dependencies.Bacteria = bacteria

    def start(self):
        super().start()

        self.bacteria.thirst -= self.bacteria.waterCost

