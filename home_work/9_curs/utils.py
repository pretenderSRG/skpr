import requests
from random import shuffle
from basic_word import BasicWord


def load_data(url: str):
    """
       Load data form jsonkeeper
       :param url: url adress
       :return: list with data
       """
    response = requests.get(url)
    data = response.json()
    return data


def create_random_word(data: list) -> BasicWord:
    """
    Create random word
    :param data:
    :return:
    """
    shuffle(data)
    one_word = data[0]
    word = BasicWord(one_word.get("word"), one_word.get("subwords"))
    return word


def print_statistic(words: list, correct_answer: int) -> None:
    """

    :param words: list with correct answers
    :param correct_answer: number correct answers
    :return:
    """
    print("Гра закінчена")
    print(f"Ви відгадили {correct_answer} слів:")
    print(*words, sep="\n")


def game_start(name: str, variant: int, word: str) -> None:
    """
    Start game
    :param name: player name
    :param variant: number of word variants
    :param word: current word
    :return:
    """
    print("Привіт", name)
    print(f"Складіть {variant} слів із слова `{word}`")
    print("Слова повинні бути не коротше 3-х букв")
    print("Щоб завершити напишіть слово 'stop'")
