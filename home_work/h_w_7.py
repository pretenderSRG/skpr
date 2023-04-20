import json
from typing import Optional, Any

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
        print(f"{category.ljust(15)}", end="")
        for score, question in scores.items():
            if question['asked']:
                print("   ".ljust(5), end="")
            else:
                print(score.ljust(5), end="")
        print()


def parse_input() -> tuple:
    """_Parse user input_

    Returns:
        tuple: _category, price_
    """
    category, price = input("-> ").split()
    return category.title(), price


def is_question_ask(questions: dict) -> bool:
    """
    :param questions: dict with questions
    :return:
    """
    asked_list = []
    for categories in questions:
        for item in questions[categories].values():
            if item["asked"]:
                asked_list.append(True)
            else:
                asked_list.append(False)

    return all(asked_list)


def show_questions(questions: dict, category: str, number: str) -> Any:
    """
    Show question from dict with questions
    :param questions: dict with questions
    :param category: user category
    :param number: price of question
    :return: dict with questions, answer to question
    """
    if category not in questions:
        print("Невірно обрана категорія")
        return questions, None

    for price, quest in questions[category].items():
        if number == price and not quest['asked']:
            print(f"Слово {quest['question']} в перекладі означає ...")
            return questions, quest['answer']
    print('Немає такої ціни')
    return questions, None


def show_statistics(scores, right, fail) -> None:
    """
    Show game statistics
    :param scores:
    :param right:
    :param fail:
    :return: None
    """
    print(f"Ваш рахунок: {scores}")
    print(f"Правильних відповідей: {right}")
    print(f"Неправильних відповідей: {fail}")


def write_statistics(filename: str, scores: int, correct: int, incorrect: int) -> None:
    """
    Write statistic in json file
    :param filename: name of file
    :param scores: user scores
    :param correct: counter correct answers
    :param incorrect: counter incorrect answers
    :return: None
    """
    with open(filename, "w") as file:
        statistic = {"point": scores, "correct": correct, "incorrect": incorrect}
        json.dump(statistic, file, indent=4)


def main() -> None:
    """
    Main program
    :return: None
    """
    scores: int = 0
    correct_answers: int = 0
    fail_answers: int = 0

    #  load questions from file
    questions = load_questions(QUESTIONS)
    while True:
        show_field(questions)
        print('---------------------------')
        print("Виберіть тему та ціну")

        #  catch incorrect user input
        try:
            user_category, user_price = parse_input()
        except Exception as e:
            print('Помилка вводу', e)
            continue
        questions, question = show_questions(questions, user_category,
                                             user_price)
        #  checking category and price
        if question is None:
            continue
        user_answer = input("-> ").lower()
        if user_answer == question:
            scores += int(user_price)
            correct_answers += 1
            print(f"Правильно! Ваш рахунок {scores}")
        else:
            fail_answers += 1
            scores -= int(user_price)
            print(f"Неправильно, правильна відповідь \
            {questions[user_category][user_price]['answer']}, {-int(user_price)}, Ваш рахунок {scores}")
        questions[user_category][user_price]['asked'] = True  # disable question if question was in game

        #  check if all question was in game
        if is_question_ask(questions):
            print("У нас закінчились запитання")
            show_statistics(scores, correct_answers, fail_answers)
            write_statistics(OUTPUT_FILE, scores, correct_answers, fail_answers)
            break


if __name__ == '__main__':
    main()