class Query:
    def __init__(self, dependencies, coordinates, foodCoordinates, waterCoordinates, entity):
        self.dependencies = dependencies

        self.logger: dependencies.Logger = self.dependencies.Logger("logs/query.log")
        self.logger.info("Query created")

        self.query: list = []
        self.coordinates: list[int] = coordinates
        self.foodCoordinates: list[int] = foodCoordinates
        self.waterCoordinates: list[int] = waterCoordinates
        self.entity: dependencies.Bacteria = entity

    def __len__(self):
        return len(self.query)

    @staticmethod
    def distance(coordinates, target):
        import math

        return math.sqrt((coordinates[0] - target[0]) ** 2 + (coordinates[1] - target[1]) ** 2)

    def addMoveTask(self, coordinates, target):
        self.query.append(self.dependencies.tasks.Move(self.dependencies, coordinates, target))
    def generatorMoveTasks(self, target: list[int], speed: int):
        speed: float = 1 / 100

        def tr_cash(func):
            value: dict = {}
            def wrapper(a: int):
                if a in value:
                    return value[a]
                else:
                    value[a] = func(a)
                    return value[a]

            return wrapper

        @tr_cash
        def tr(a: int):
            return (a > 0) - (a < 0)

        def cache(func: callable):
            result: dict = {}
            def wrapper(*args: list):

                if args in result:
                    return result[args]

                else:
                    result[args] = func(*[list(x) for x in args])
                    return result[args]

            return wrapper

        @cache
        def move(coordinate: list[int, int], targetCoords: list[int, int]):
            x, y = (targetCoords[0] - coordinate[0]) / speed, (targetCoords[1] - coordinate[1]) / speed
            x, y = int(x), int(y)
            u, i = abs(x), abs(y)
            j, k = tr(x), tr(y)
            w: float = min(u, i)
            n: float = max(u, i)
            f: dict = {u: j, i: k}
            result: list = []
            qw, ew = f[n] * speed, f[w] * speed
            for l in range(n):
                if l < u:
                    coordinate[0] += qw
                coordinate[1] += ew
                result.append(coordinate.copy())
            return result

        h: tuple = tuple(self.coordinates)
        j: tuple = tuple(target)

        d = move(h, j)
        for i in d[:1]:
            self.addMoveTask(self.coordinates, i)
        self.addMoveTask(self.coordinates, target)
        for i in range(1, len(self.query)):
            self.startTask()

    def addEatTask(self):
        self.query.append(self.dependencies.tasks.Eat(self.dependencies, self.coordinates,
                                                      self.foodCoordinates, self.entity))
    def generatorEatTask(self):
        if len(self.query) == 0:
            for i in self.foodCoordinates:
                if self.coordinates == i:
                    self.addEatTask()
                    self.startTask()
                    return

            distances: list = []
            for i in self.foodCoordinates:
                distances.append(self.distance(self.coordinates, i))

            self.generatorMoveTasks(min(distances), 500)

    def addWaterTask(self):
        self.query.append(self.dependencies.tasks.Eat(self.dependencies, self.coordinates,
                                                      self.waterCoordinates, self.entity))
    def generatorWaterTask(self):
        if len(self.query) == 0:
            for i in self.waterCoordinates:
                if self.coordinates == i:
                    self.addWaterTask()
                    self.startTask()
                    return

            distances: list = []
            for i in self.waterCoordinates:
                distances.append(self.distance(self.coordinates, i))

            self.generatorMoveTasks(min(distances), 500)


    def startTask(self):
        self.query[0].start()
        del self.query[0]
