from store import Store


class Shop(Store):
    def __init__(self):
        super().__init__()
        self.capacity = 20
        self.__limit_items = 5

    def add(self, name: str, value: int) -> None:
        if len(self.items) > self.__limit_items:
            raise ValueError("Limit items is too large")
        super().add(name, value)
