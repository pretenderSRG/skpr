from config import URL
from player import Player
from utils import create_random_word, load_data, print_statistic, game_start


def main():
    correct_word_counter = 0  # Counter of correct answer
    data = load_data(URL)
    word = create_random_word(data)
    word_variant = word.correct_word_counter()
    player_name = input("Введіть ім'я гравця: ")
    player = Player(player_name)

    game_start(player_name, word_variant, word.current_word)
    while correct_word_counter <= word_variant:
        word.user_word = input("-> ").lower()

        if word.user_word in ("stop", "стоп"):
            break
        
        # Check if input word is too short
        if len(word.user_word) < 3:
            print("слово занадто коротке")
            continue
        
        #  Checking the word for repetition
        if not player.validate_word(word.user_word):
            print(f'Слово {word.user_word} вже використовувалось')
            continue
            
        #  If user input word is correct
        elif word.check_user_word():
            word.count_correct_answer()
            correct_word_counter += 1
            player.add_word(word.user_word)
            print('Правильно')
            
        #  If user input word is not correct
        else:
            print("Неправмльно")

    print_statistic(player.used_words, correct_word_counter)


if __name__ == '__main__':
    main()