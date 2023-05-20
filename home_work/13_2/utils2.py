def get_verbal_grade(grade):
    if type(grade) != int:
        raise TypeError("Повинно бути ціле число між 2 і 5")
    if grade < 2 or grade > 5:
        raise ValueError("Повинно бути ціле число між 2 і 5")

    if grade == 2:
        return "Погано"
    elif grade == 3:
        return "Задовільно"
    elif grade == 4:
        return "Добре"
    elif grade == 5:
        return "Відмінно"
