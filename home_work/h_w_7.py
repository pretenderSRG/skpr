import json

QUESTIONS = "questions.json"
OUTPUT_FILE = "saved_statistics.json"


def load_questions(filename: str) -> dict:
    """_Load questions from file_

    Args:
        filename (str): _name of file/ path to file_

    Returns:
        dict: _dict with questions_
    """

    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def show_field(questions: dict) -> None:
    """_Show field_

    Args:
        questions (dict): _dict with questions_
    """
    for category, scores in questions.items():
        print(f"{str(category).ljust(10)}", end="  ")
        for score in scores:
            print(f"{score}", end="   ")
        print()


def parse_input() -> tuple:
    """_Parse user input_

    Returns:
        tuple: _category, price_
    """
    category, price = input("-> ").split()
    return category.title(), price


def is_question(questions):
    asked_list = []
    for categories in questions:
        for question in questions[categories].values():
            for k in question:
                if k["asked"]:
                    asked_list.append(True)
                else:
                    asked_list.append(False)

    return all(asked_list)


def show_questions(questions: dict, category: str, number: str):

    if category not in questions:
        print("Невірно обрана категорія")
        return questions, None

    for price, quest in questions[category].items():
        if number == price:
            print(f"Слово {quest['question']} в перекладі означає ...")
            return questions, quest['answer']
        else:
            print('Немає такої ціни')
            return questions, None


def show_statistics(scores, right, fail) -> None:
    """
    Show game statistics
    :param scores:
    :param right:
    :param fail:
    :return:
    """
    print(f"Ваш рахунок: {scores}")
    print(f"Правильних відповідей: {right}")
    print(f"Неправильних відповідей: {fail}")


def write_statistics(filename, scores, correct, incorect):
    with open(filename, "w") as file:
        statistic = {"point": scores, "correct": correct, "incorect": incorect}
        json.dump(statistic, file)

def main():
    scores = 0
    correct_answers = 0
    fail_answers = 0

    questions = load_questions(QUESTIONS)
    while True:
        show_field(questions)
        print("Виберіть тему та ціну")
        try:
            user_category, user_price = parse_input()
        except Exception as e:
            print('Помилка воду', e)
            continue
        questions, question = show_questions(questions, user_category,
                                             user_price)
        if question is None:
            continue
        user_answer = input("-> ").lower()
        if user_answer == question:
            print(f"Правильно! Ваш рахунок {scores}")
            scores += int(user_price)
            correct_answers += 1
        else:
            fail_answers += 1
            scores -= int(user_price)
            print(f"Неправильно, правильна відповідь \
            {questions[user_category][user_price]['answer']}, {-int(user_price)}\
                , Ваш рахунок {scores}")
        if is_question(questions):
            print("У нас закінчились запитання")
            show_statistics(scores, correct_answers, fail_answers)
            write_statistics(OUTPUT_FILE, scores, correct_answers, fail_answers)



if __name__ == '__main__':
    main()