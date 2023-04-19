import json
import random

with open("home_work\\morse-code.json") as file:
    MORSE_CODE = json.load(file)

WORDS = ["code", "bit", "list", "next"]
answers = []


def morse_encode(word: str) -> str:
    """Encoding word in morse code

    Args:
        word (str): incoming word

    Returns:
        str: encoding word
    """
    word_encoded = ""

    for letter in word:
        word_encoded += MORSE_CODE.get(letter, "") + " "

    return word_encoded.strip()


def get_word() -> str:
    """Get random word from list

    Returns:
        str: random word from list
    """
    return random.choice(WORDS)


def print_statistics(answers: list) -> None:
    """Print statistics of test

    Args:
        answers (list): list of answers
    """
    all_questions = len(answers)
    right_answers = sum(answers)
    fail_answers = all_questions - right_answers
    print(f"""Number of questions is {all_questions}
    Right answers is {right_answers}
    Fail answers is {fail_answers}""")


def main():
    print("Let's traing to encode word in morse")
    print("Press ENTER to start")
    input()

    for i in range(1, len(WORDS) + 1):
        current_word = get_word()
        current_encoded = morse_encode(current_word)
        print(f"Word {i} {current_encoded}")
        user_input = input("-> ")
        if user_input.lower() == current_word:
            print(f"That's rigth, {current_word}")
            answers.append(True)
        else:
            print(f"Fale, rigth answer is {current_word}")
            answers.append(False)

    print_statistics(answers)


if __name__ == "__main__":
    main()