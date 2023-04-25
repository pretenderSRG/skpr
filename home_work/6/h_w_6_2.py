import random


def open_file(filename) -> list:
    """Open file with words.
    """

    with open(filename) as file:
        words = file.readlines()
        random.shuffle(words)
    return words


def write_data(filename, player, scores):
    """Writ data to file

    Args:
        filename (file): hystory file
        player (_str_): _player name_
        scores (_int_): _scores of player_
    """
    with open(filename, "a") as file:
        file.write(f"{player} {scores}\n")


def print_table(filename):
    """Print score table

    Args:
        filename (file): file
    """
    count = 0
    max_score = 0
    with open(filename) as file:
        for line in file:
            print(line.strip())
            count += 1
            _, score = line.split()
            score = int(score.strip())
            if score > max_score:
                max_score = score
        print(f"Game count = {count}")
        print(f"Max score = {max_score}")


def create_file(filename):
    """Create empty file for players statistics
    """
    with open(filename, "w") as file:
        file.write('')


def shuffle_word(word):
    """Suffle letters in word

    Args:
        word (str): word from file

    Returns:
        shuffling word: word from file
    """
    word_as_list = list(word)
    random.shuffle(word_as_list)  # shuffle letters in word
    return ''.join(word_as_list)


def main():
    """main program
    """
    data_file = "history.txt"
    print("Hello, do tou won to play? y/n")
    flag = input("-> ").lower()
    if flag == 'y':
        #  Creating file with games
        create_file(data_file)

    while flag == 'y':
        print("Enter your name:")
        player = input("-> ")
        words = open_file("words.txt")
        scores = 0

        #  read words from file
        for word in words:
            word = word.strip()
            temp_word = shuffle_word(word)
            print(f"Guess word: {temp_word}")

            #  Get user answer
            user_word = input("-> ")
            if user_word == word:
                scores += 10
                print("That's wright, you have 10 point")
            else:
                print(f"Wrong, Answer is {word}")
        #  write data to file
        write_data(data_file, player, scores)
        flag = input("Next player,do you won to play? y/n -> ").lower()

    #  print player history
    print("All players was played, print score table")
    print_table(data_file)


if __name__ == "__main__":
    main()