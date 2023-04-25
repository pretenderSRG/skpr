class Question:
    def __init__(self, question, difficult, answer):
        self.question = question
        self.difficult = int(difficult)
        self.__answer = answer

        # self.__asked = False
        self.__user_answer = None
        self.scores = self.difficult * 10

    @property
    def answer(self):
        return self.__user_answer

    @answer.setter
    def answer(self, input_answer):
        self.__user_answer = input_answer

    def get_points(self, total_scores):
        return self.scores + total_scores

    def is_correct(self):
        return self.__answer == self.__user_answer

    def build_question(self):
        print(f"Питання: {self.question} ?\nСкладність {self.difficult}/5")

    def build_feedback(self):
        if self.is_correct():
            print(f"Відповідь правильна, отримано {self.scores} балів")
        else:
            print(f"Відповідь неправильна, правильна відповідь {self.__answer}")
