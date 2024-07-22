from loguru import logger
import os

from genes import Gene, GeneCluster
from metrics import metric


os.remove("logs/bacterias.log")
logger.add("logs/bacterias.log", format="{level}: {message}")


class Entity:
    instances = {}
    def __init__(self):
        Entity.instances[self] = metric.tasksCounter
        metric.tasksCounter += 1
        logger.info(f"{Entity.instances[self]} bacteria created")

class Bacteria(Entity):
    def __init__(self, coordinates: list[int],
                 foodCoordinates: list[int], foodCost: Gene,
                 waterCoordinates: list[int], waterCost: Gene,
                 visionDistance: Gene, speed: Gene):
        super().__init__()

        self.coordinates = coordinates
        self.foodCoordinates = foodCoordinates
        self.waterCoordinates = waterCoordinates
        self.foodCost = foodCost
        self.waterCost = waterCost
        self.visionDistance = visionDistance
        self.speed = speed
        self.geneCluster = GeneCluster([foodCost, waterCost, visionDistance, speed])
        self.hungry = 100
        self.thirst = 100

    def __str__(self):
        return ("Simulation Agents 1.9.0\n"
                "Type: Agent, bacteria")

