from storage import Storage


class Store(Storage):
    def __init__(self):
        super().__init__()
        self.capacity = 100

    def add(self, name: str, value: int) -> None:
        if self.get_free_space() > 0:
            super().add(name, value)
        else:
            raise ValueError(f'Exceeding the limit {self.capacity}')

    def remove(self, name: str, value: int) -> None:
        current_value = self.items.get(name)
        if current_value is None:
            raise ValueError(f"No such item {name}")
        elif current_value < value:
            raise ValueError(f"Value  {name} < 0")

        super().remove(name, value)


