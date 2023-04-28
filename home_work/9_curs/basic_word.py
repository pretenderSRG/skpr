from typing import List


class BasicWord:
    def __init__(self, current_word: str, permissible_words: List[str]):
        self.__current_word = current_word
        self.permissible_words = permissible_words

        self.__user_word = None
        self.__words_counter = 0

    @property
    def words_counter(self):
        return self.__words_counter

    @property
    def user_word(self):
        return self.__user_word

    @user_word.setter
    def user_word(self, word: str) -> None:
        self.__user_word = word

    @property
    def current_word(self):
        return self.__current_word

    def check_user_word(self):
        """
        Check user input word in list in permission words
        :return:
        """
        return self.__user_word in self.permissible_words

    def count_correct_answer(self):
        """
        Correct answers counter
        :return: total correct word
        """
        if self.check_user_word():
            self.__words_counter += 1

    def correct_word_counter(self):
        return len(self.permissible_words)

    def __repr__(self):
        return f"{self.current_word} -> {self.permissible_words}"
