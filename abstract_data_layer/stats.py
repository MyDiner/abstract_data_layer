from enum import Enum
from typing import Generic

from abstract_data_layer.base import ID


class ItemStatus(Enum):
    TODO, PROGRESS, DONE, CANCELLED = range(4)

class Stats(Generic[ID]):
    def __init__(self, count: int = 0):
        self.count = count