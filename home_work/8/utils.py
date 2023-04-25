from random import shuffle
import json
from question import Question


def load_questions(filename: str) -> dict:
    """
    Load questions from json file
    :param filename: name/path of file
    :return: dictionary with questions
    """
    with open(filename, encoding='utf-8',) as file:
        data = json.load(file)
        return data


def create_question_list(data: dict) -> list:
    """
    Create list with questions
    :param data: dict with data
    :return: list with Question objects
    """
    questions = [Question(item["q"], item["d"], item["a"]) for item in data]
    # for item in data:
    #     questions.append(Question(item["q"], item["d"], item["a"]))
    shuffle(questions)
    return questions


def print_statistics(questions: list, correct_questions: int, scores: int) -> None:
    """
    Print total statistic
    :param questions: list with Question object
    :param correct_questions: correct answers
    :param scores: total scores
    :return:
    """
    print("Гра закінчена")
    print(f"Правильних відповідей: {correct_questions} з {len(questions)}")
    print(f"Набрано: {scores} балів")



