ERRORS = {
    "out": "Вихід з системи",
    "noaccess": "Відсутній доступ",
    "unknow": "Невідома помилка",
    "timeout": "Система довго не відповідає",
    "robot": "Ваші дії схожі на бота"
}


def get_errors(*args: str) -> list:
    """Getmessage errors

    Returns:
        list: list of message
    """
    errors_messages = []
    for error in args:
        errors_messages.append(ERRORS.get(error, "помилки немає"))

    return errors_messages


print(get_errors("out", "noaccess"))
