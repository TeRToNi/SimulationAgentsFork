from loguru import logger
import os
import time

import tasks
# from bacteria import Bacteria


try:
    os.remove("logs/query.log")
except FileNotFoundError:
    pass

logger.add("logs/query.log", format="{level}: {message}")


class Query:
    def __init__(self, coordinates, foodCoordinates, waterCoordinates):
        logger.info("Query created")
        self.query = []
        self.coordinates = coordinates
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates

    def addMoveTask(self, coordinates, target):
        self.query.append(tasks.Move(coordinates, target))
    def generatorMoveTasks(self, target, speed):
        speed = 1 / 100

        def tr_cash(func):
            value = {}

            def wrapper(a):
                if a in value:
                    return value[a]
                else:
                    value[a] = func(a)
                    return value[a]

            return wrapper

        @tr_cash
        def tr(a):
            return (a > 0) - (a < 0)

        def cahe(func):
            result = {}

            def wrapper(*args):

                if args in result:
                    return result[args]

                else:
                    result[args] = func(*[list(x) for x in args])
                    return result[args]

            return wrapper

        @cahe
        def move(coordinate: list[int, int], target: list[int, int]):
            x, y = (target[0] - coordinate[0]) / speed, (target[1] - coordinate[1]) / speed
            x, y = int(x), int(y)
            u, i = abs(x), abs(y)
            j, k = tr(x), tr(y)
            w = min(u, i)
            n = max(u, i)
            f = {u: j, i: k}
            result = []
            qw, ew = f[n] * speed, f[w] * speed
            for l in range(n):
                if l < u:
                    coordinate[0] += qw
                coordinate[1] += ew
                result.append(coordinate.copy())
            return result

        h = tuple(self.coordinates)
        j = tuple(target)

        d = move(h, j)
        for i in d[:1]:
            self.addMoveTask(self.coordinates, i)
        self.addMoveTask(self.coordinates, target)
        for i in range(1, len(self.query)):
            self.startTask()

    def addEatTask(self):
        self.query.append(tasks.Eat(self.coordinates, self.foodCoordinates))
    def generatorEatTask(self):
        self.addEatTask()
        self.startTask()

    def addWaterTask(self):
        self.query.append(tasks.Eat(self.coordinates, self.waterCoordinates))
    def generatorWaterTask(self):
        self.addWaterTask()
        self.startTask()

    def startTask(self):
        self.query[0].start()
        del self.query[0]
