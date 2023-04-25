from utils import load_questions, create_question_list, print_statistics


FILE_NAME: str = 'questions.json'


def main():
    scores: int = 0  # total scores
    correct_answers: int = 0
    data: dict = load_questions(FILE_NAME)
    questions: list = create_question_list(data)

    for question in questions:
        question.build_question()
        question.answer = input("-> ").lower()
        question.build_feedback()
        if question.is_correct():
            correct_answers += 1
            scores = question.get_points(scores)

    print_statistics(questions, correct_answers, scores)


if __name__ == '__main__':
    main()
