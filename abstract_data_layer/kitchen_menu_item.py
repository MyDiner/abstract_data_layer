from abc import ABC
from typing import Generic, List

from abstract_data_layer.base import ID, CRUD


class KMI(Generic[ID]):
    def __init__(self, name: str, category_id: str, description: str = None):
        self.name = name
        self.category_id = category_id
        self.description = description

class KitchenMenuItemRepository(CRUD[KMI[ID], ID], ABC):
    def __init__(self):
        pass

    def find_by_category_id(self, category_id: str) -> List[KMI]:
        """
        Find all the saved KMI by categoryId

        Returns: list of all KMI
        """
        pass