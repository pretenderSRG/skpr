from abc import ABC, abstractmethod
from time import sleep


class Storage(ABC):
    def __init__(self, items, company):
        self._items = items
        self._capacity = company

    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        # super().__init__()
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items)


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20


class Request:
    def __init__(self, info):
        self.info = self._split_info(info)
        self.from_ = self.info[4].lower()
        self.to_ = self.info[6].lower()
        self.amount_ = int(self.info[1])
        self.product_ = self.info[2].lower()

    @staticmethod
    def _split_info(info):
        return info.split()

    def __repr__(self):
        return f"Доставити {self.amount_} {self.product_} з {self.from_} в {self.to_}"


def print_(text):
    for i in text:
        print(i, end="")
        sleep(0.0)
    print()


def main():

    print_("Вас вітає служба доставки")
    while True:
        user_input = input("Введіть запит: ")
        # user_input = "Доставити 3 банан з склад до магазин"
        if user_input.lower() in ("stop", "стоп"):
            continue
        request = Request(user_input)

        from_ = store if request.from_ == "склад" else shop
        to_ = store if request.to_ == "склад" else shop

        if request.product_ in from_.items:
            print_(f"Потрібний товар '{request.product_}' є в пункті '{request.from_}'")
        else:
            print_(f"В пункті '{request.from_}' немає такого товару '{request.product_}'")
            continue

        if from_.items[request.product_] >= request.amount_:
            print_(f"Потрібна кількість {from_.items[request.product_]} є в пункті '{request.from_}'")
        else:
            print_(f"В пункті '{request.from_}' не вистачає {request.amount_ - from_.items[request.product_]} товару")
            continue
        if to_.get_free_space >= request.amount_:
            print_(f"Потрібна кількість  місця є в пункті '{request.to_}'")

        else:
            print_(f"В пункті '{request.to_}' не висчтає {request.amount_ - to_.get_free_space}")
            continue

        if request.to_ == "магазин" and to_.get_unique_items_count == 5 and request.product_ not in to_.items:
            print_("В магазині достатньо унікальних значень")
            continue

        from_.remove(request.product_, request.amount_)
        print_(f"Кур'єр забрав {request.amount_} {request.product_} з {request.from_} до {request.to_}")
        print()
        to_.add(request.product_, request.amount_)

        print()
        print('В магазині')
        for k, v in store.items.items():
            print(f"{v}: {k}")


        print()
        print('На складі')
        for k, v in shop.items.items():
            print(f"{v}: {k}")
        # break
    print_("Завершення роботи")


if __name__ == '__main__':
    store = Store()
    shop = Shop()

    store_items = {
        "банан": 10,
        "сік": 5,
        "кава": 40,
        "чай": 6
    }

    store.items = store_items
    main()
