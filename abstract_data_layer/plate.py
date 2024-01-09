from abc import ABC
from typing import Generic, List, Optional

from abstract_data_layer.base import ID, CRUD


class Plate(Generic[ID]):
    def __init__(self,
                 id: ID = None,
                 name: str = None,
                 description: str = None,
                 color: str = None,
                 manager: str = None,
                 slot: Optional[List[int]] = None,
                 enabled: bool = False,
                 ):
        if slot is None:
            slot = [0] * 2

        self.id = id
        self.name = name
        self.description = description
        self.color = color
        self.manager = manager
        self.slot = slot
        self.enabled = enabled


class PlateRepository(CRUD[Plate[ID], ID], ABC):
    def __init__(self):
        pass
