from loguru import logger
import math
import os
import sys

from metrics import metric


try:
    os.remove("logs/tasks.log")
except FileNotFoundError:
    pass

logger.add("logs/tasks.log", format="{level}: {message}")


class Task:
    instances = {}
    def __init__(self):
        Task.instances[self] = metric.tasksCounter
        metric.tasksCounter += 1
        logger.info(f"{Task.instances[self]} task created")

    def start(self):
        logger.info(f"{Task.instances[self]} task started")


class Move(Task):
    def __init__(self, coordinates, target):
        super().__init__()

        self.coordinates = coordinates
        self.target = target

    def start(self):
        super().start()

        self.coordinates[0] = self.target[0]
        self.coordinates[1] = self.target[1]

class Eat(Task):
    def __init__(self, coordinates, foodCoordinates):
        super().__init__()

        self.coordinates = coordinates
        self.foodCoordinates = foodCoordinates
        #self.bacteria = bacteria

    def start(self):
        super().start()

        if self.coordinates == self.foodCoordinates:
            self.bacteria.hungry -= self.bacteria.foodCost

class Drink(Task):
    def __init__(self, coordinates, waterCoordinates, bacteria):
        super().__init__()

        self.coordinates = coordinates
        self.waterCoordinates = waterCoordinates
        self.bacteria = bacteria

    def start(self):
        super().start()

        if self.coordinates == self.waterCoordinates:
            self.bacteria.thirst -= self.bacteria.waterCost

