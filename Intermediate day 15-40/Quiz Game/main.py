from question_model import Question
from data import question_data


question_bank = []
for item in question_data:
    question_bank.append(Question(q_text=item["text"], q_answer=item["answer"]))

print(question_bank[0].text)
