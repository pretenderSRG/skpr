class Request:
    def __init__(self, data: list) -> None:
        self.__action = data[0]
        self.__from = data[3]
        self.__to = data[4]
        self.__amount = data[1]
        self.__product = data[2]

    @property
    def from_(self):
        return self.__from

    @property
    def to_(self):
        return self.__to

    @property
    def amount_(self):
        return self.__amount

    @property
    def product_(self):
        return self.__product

    @property
    def action_(self):
        return self.__action
