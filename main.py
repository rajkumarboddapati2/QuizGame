from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []

for each_question in question_data:
    question = Question(each_question["text"], each_question["answer"])
    Question_bank.append(question)

Quiz = QuizBrain(Question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print("You've completed the quiz")
print(f"Final score is: {Quiz.result}/{Quiz.question_number}")
