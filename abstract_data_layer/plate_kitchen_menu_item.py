from abc import ABC
from typing import Generic, List

from abstract_data_layer.base import ID, CRUD
from abstract_data_layer.stats import ItemStatus


class PlateKitchenMenuItem(Generic[ID]):
    def __init__(self, plate_id: str,
                 menu_item_id: str,
                 order_number: str,
                 status: ItemStatus = ItemStatus.TODO,
                 table_num: str = None,
                 client_name: str = None,
                 notes: str = None,
                 take_away: bool = False):
        self.plate_id = plate_id
        self.menu_item_id = menu_item_id
        self.order_number = order_number
        self.status = status
        self.table_num = table_num
        self.client_name = client_name
        self.notes = notes
        self.take_away = take_away


class PlateKitchenMenuItemRepository(CRUD[PlateKitchenMenuItem[ID], ID], ABC):
    def __init__(self):
        pass

    def find_by_plate_id(self, plate_id: str) -> List[PlateKitchenMenuItem]:
        """
        Find all the saved Item by plate id

        Returns: list of all PlateKitchenMenuItem
        """
        pass

    def find_not_in_plate(self) -> List[PlateKitchenMenuItem]:
        """
        Find all the saved Item with plate id None (not positioned yet)

        Returns: list of all PlateKitchenMenuItem
        """
        pass
