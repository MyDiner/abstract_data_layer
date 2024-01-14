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
from enum import Enum
from typing import TypeVar, Generic, Protocol, List

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


class SortOrder(Enum):
    ASC = 1
    DESC = 2


class Sorting(Generic[T]):
    def __init__(self, field: str, order: SortOrder):
        self.order = order
        if not hasattr(T, field):
            raise KeyError(f"Field {field} doesn't exists in object")

    @staticmethod
    def asc(field: str) -> 'Sorting':
        return Sorting(field, SortOrder.ASC)

    @staticmethod
    def desc(field: str) -> 'Sorting':
        return Sorting(field, SortOrder.DESC)


class PageRequest(Generic[T]):

    def __init__(self, page: int = 0, size: int = 20, query: T = None, sorting: SortOrder[T] = None):
        self.page = page
        self.size = size
        self.query = query
        self.sorting = sorting

    @staticmethod
    def on(page: int) -> 'PageRequest':
        return PageRequest(page)


class PageResponse(Generic[T]):

    def __init__(self, elements: List[T] = None,
                 page: int = 0,
                 page_size: int = 0,
                 total_pages: int = 0,
                 total_size: int = 0):
        self.elements = elements if elements is not None else []
        self.page = page
        self.page_size = page_size
        self.total_pages = total_pages
        self.total_size = total_size
