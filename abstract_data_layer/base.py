"""
abstract_data_layer base module.

This is the principal module of the abstract_data_layer project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
from abc import abstractmethod
from datetime import datetime
from typing import TypeVar, Generic, Protocol

ID = TypeVar('ID')
T = TypeVar('T')

class Entity(Protocol):
    createDate: datetime
    updateDate: datetime

class CRUD(Generic[T, ID]):

    @abstractmethod
    def get(self, target: ID) -> T:
        pass

    @abstractmethod
    def delete(self, target: ID) -> T:
        pass

    @abstractmethod
    def create(self, obj: T) -> T:
        pass

    @abstractmethod
    def update(self, obj: T) -> T:
        pass