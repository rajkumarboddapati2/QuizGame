class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.result = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        if user_answer.lower() == current_question.answer.lower():
            self.result += 1
            print("Correct!")
        else:
            print("Wrong..")
        print(f"The answer is {current_question.answer}")
        print(f"the result is: {self.result}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
