from abc import ABC
from enum import Enum
from typing import Generic, List
from datetime import datetime

from abstract_data_layer.base import ID, CRUD


class ItemStatus(Enum):
    TODO, PROGRESS, DONE, CANCELLED = range(4)

class Stats(Generic[ID]):
    def __init__(self, count: int = 0):
        self.count = count

class StatsRepository(CRUD[Stats[ID], ID], ABC):
    def __init__(self):
        pass

    def find_by_date_range(self, f: datetime, t: datetime) -> List[Stats]:
        """
        Find all the saved stats in the input date range
        Args:
            f: from date
            t: to date

        Returns: list of all stats in range
        """
        pass
