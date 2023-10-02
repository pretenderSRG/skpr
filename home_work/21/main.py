from shop import Shop
from store import Store
from request import Request


def request_action():
    print("Введіть необхідну дію: 1 - добавити, 2 - забрати, 0 - вихід")
    data_for_transfer = []
    data_for_transfer.append(input("-> "))
    data_for_transfer.append(int(input("кількість: -> ")))
    data_for_transfer.append(input("товар: -> "))
    data_for_transfer.append(input("звідки: -> "))
    data_for_transfer.append(input("куди: -> "))


    return Request(data_for_transfer)




def main():

    print("Привіт вас вітає логістична компанія")
    while True:
        transfer = request_action()
        shop = Shop()
        store = Store()
        if transfer.action_ == 0:
            break
        # якщо добавити товар
        elif transfer.action_ == 1:
            pass


if __name__ == '__main__':
    main()