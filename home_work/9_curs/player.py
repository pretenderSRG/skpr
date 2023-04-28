class Player:

    def __init__(self, player_name: str):
        self.player_name = player_name
        self.__used_words: list = []

    @property
    def used_words(self):
        return self.__used_words

    def get_count_words(self):
        return len(self.__used_words)

    def add_word(self, word: str) -> None:
        self.__used_words.append(word)

    def validate_word(self, word: str) -> bool:
        return word not in self.__used_words

    def __repr__(self):
        return f"{self.player_name}: {self.__used_words}"
