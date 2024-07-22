from dataclasses import dataclass


@dataclass
class Metrics:
    tick: int
    tasksCounter: int
    bacteriasCounter: int


metric = Metrics(0, 0, 0)
