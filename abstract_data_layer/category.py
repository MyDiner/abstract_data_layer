from abc import ABC
from typing import Generic

from abstract_data_layer.base import CRUD, ID


class Category(Generic[ID]):
    def __init__(self, id: ID = None, name: str = None, description: str = None, color: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.color = color


class CategoryRepository(CRUD[Category[ID], ID], ABC):
    def __init__(self):
        pass
