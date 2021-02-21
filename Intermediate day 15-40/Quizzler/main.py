from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for item in question_data:
    question_bank.append(Question(q_text=item["question"], q_answer=item["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_questions():
    quiz.next_question()

