from abc import ABC, abstractmethod
from typing import Dict


class Storage(ABC):
    def __init__(self):
        self.items = {}
        self.capacity = 0

    # @property
    # @abstractmethod
    # def items(self) -> Dict[str:int]:
    #     pass
    #
    # @property
    # @abstractmethod
    # def capacity(self) -> int:
    #     pass

    def add(self, name: str, value: int) -> None:
        self.items[name] = self.items.get(name, 0) + value

    def remove(self, name, value):
        self.items[name] = self.items.get(name, 0) - value

    def get_free_space(self):
        return self.capacity - len(self.items)

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)






